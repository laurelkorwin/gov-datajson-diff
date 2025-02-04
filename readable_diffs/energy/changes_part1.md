# Change History for energy.json

### Changes from 43f2c5a to 93b0cee
**Author:** Automated

**Date:** 2025-02-04 09:11:56+00:00

**Message:** Updated data: Tue Feb  4 09:11:56 UTC 2025

```diff
diff --git a/energy.json b/energy.json
index 10d7813..9f62cf5 100644
--- a/energy.json
+++ b/energy.json
@@ -29273,6 +29273,101 @@
                 "name": "DOE Office of Electricity"
             },
             "title": "Office of Electricity Information Center"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kyle Weatherholt",
+                "hasEmail": "mailto:kyle.weatherholt@ports.pppo.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://pegasis.ports.pppo.gov/Documents/UserGuides/AnalyticalDataUserGuide.pdf",
+            "describedByType": "application/pdf",
+            "description": "Environmental Geographic Analytical Spatial Information System",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://pegasis.ports.pppo.gov/Pegasis/Default.aspx",
+                    "description": "PPPO Environmental Geographic Analytical Spatial Information System",
+                    "title": "PPPO Environmental Geographic Analytical Spatial Information System"
+                }
+            ],
+            "identifier": "Ports Pegasis",
+            "issued": "2024-08-08",
+            "keyword": [
+                "arcgis"
+            ],
+            "landingPage": "https://pegasis.ports.pppo.gov/Pegasis/Default.aspx",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-15T20:42:37.090Z",
+            "programCode": [
+                "015:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Paducah Portsmouth Project Office"
+            },
+            "rights": "true",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "PPPO Portsmouth Pegasis"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bruce Meadows",
+                "hasEmail": "mailto:bruce.meadows@pad.pppo.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://pegasis.pad.pppo.gov/pdf/PEGASIS%20User%20Manual%202024.pdf",
+            "describedByType": "application/pdf",
+            "description": "PPPO Environmental Geographic Analytical Spatial Information System",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://pegasis.pad.pppo.gov/",
+                    "conformsTo": "https://pegasis.pad.pppo.gov/",
+                    "description": "PPPO Environmental Geographic Analytical Spatial Information System",
+                    "title": "Paducah Pegasis"
+                }
+            ],
+            "identifier": "Paducah Pegasis",
+            "issued": "2025-01-12",
+            "keyword": [
+                "arcgis"
+            ],
+            "landingPage": "https://pegasis.pad.pppo.gov/",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-15T20:52:14.034Z",
+            "programCode": [
+                "015:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Paducah Portsmouth Project Office"
+            },
+            "rights": "true",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "PPPO Paducah Pegasis"
         }
     ],
     "describedBy": "https://project-open-data.cio.gov/v1.1/schema/catalog.json"
```

### Changes from e21c7d2 to 43f2c5a
**Author:** Automated

**Date:** 2025-02-04 08:12:08+00:00

**Message:** Updated data: Tue Feb  4 08:12:08 UTC 2025

```diff
diff --git a/energy.json b/energy.json
index 9f62cf5..10d7813 100644
--- a/energy.json
+++ b/energy.json
@@ -29273,101 +29273,6 @@
                 "name": "DOE Office of Electricity"
             },
             "title": "Office of Electricity Information Center"
-        },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
-            "bureauCode": [
-                "015:11"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kyle Weatherholt",
-                "hasEmail": "mailto:kyle.weatherholt@ports.pppo.gov"
-            },
-            "dataQuality": true,
-            "describedBy": "https://pegasis.ports.pppo.gov/Documents/UserGuides/AnalyticalDataUserGuide.pdf",
-            "describedByType": "application/pdf",
-            "description": "Environmental Geographic Analytical Spatial Information System",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://pegasis.ports.pppo.gov/Pegasis/Default.aspx",
-                    "description": "PPPO Environmental Geographic Analytical Spatial Information System",
-                    "title": "PPPO Environmental Geographic Analytical Spatial Information System"
-                }
-            ],
-            "identifier": "Ports Pegasis",
-            "issued": "2024-08-08",
-            "keyword": [
-                "arcgis"
-            ],
-            "landingPage": "https://pegasis.ports.pppo.gov/Pegasis/Default.aspx",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2025-01-15T20:42:37.090Z",
-            "programCode": [
-                "015:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Paducah Portsmouth Project Office"
-            },
-            "rights": "true",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "PPPO Portsmouth Pegasis"
-        },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
-            "bureauCode": [
-                "015:11"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bruce Meadows",
-                "hasEmail": "mailto:bruce.meadows@pad.pppo.gov"
-            },
-            "dataQuality": true,
-            "describedBy": "https://pegasis.pad.pppo.gov/pdf/PEGASIS%20User%20Manual%202024.pdf",
-            "describedByType": "application/pdf",
-            "description": "PPPO Environmental Geographic Analytical Spatial Information System",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://pegasis.pad.pppo.gov/",
-                    "conformsTo": "https://pegasis.pad.pppo.gov/",
-                    "description": "PPPO Environmental Geographic Analytical Spatial Information System",
-                    "title": "Paducah Pegasis"
-                }
-            ],
-            "identifier": "Paducah Pegasis",
-            "issued": "2025-01-12",
-            "keyword": [
-                "arcgis"
-            ],
-            "landingPage": "https://pegasis.pad.pppo.gov/",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2025-01-15T20:52:14.034Z",
-            "programCode": [
-                "015:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Paducah Portsmouth Project Office"
-            },
-            "rights": "true",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "PPPO Paducah Pegasis"
         }
     ],
     "describedBy": "https://project-open-data.cio.gov/v1.1/schema/catalog.json"
```

### Changes from d9b5301 to e21c7d2
**Author:** Automated

**Date:** 2025-02-04 07:11:23+00:00

**Message:** Updated data: Tue Feb  4 07:11:23 UTC 2025

```diff
diff --git a/energy.json b/energy.json
index 10d7813..9f62cf5 100644
--- a/energy.json
+++ b/energy.json
@@ -29273,6 +29273,101 @@
                 "name": "DOE Office of Electricity"
             },
             "title": "Office of Electricity Information Center"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kyle Weatherholt",
+                "hasEmail": "mailto:kyle.weatherholt@ports.pppo.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://pegasis.ports.pppo.gov/Documents/UserGuides/AnalyticalDataUserGuide.pdf",
+            "describedByType": "application/pdf",
+            "description": "Environmental Geographic Analytical Spatial Information System",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://pegasis.ports.pppo.gov/Pegasis/Default.aspx",
+                    "description": "PPPO Environmental Geographic Analytical Spatial Information System",
+                    "title": "PPPO Environmental Geographic Analytical Spatial Information System"
+                }
+            ],
+            "identifier": "Ports Pegasis",
+            "issued": "2024-08-08",
+            "keyword": [
+                "arcgis"
+            ],
+            "landingPage": "https://pegasis.ports.pppo.gov/Pegasis/Default.aspx",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-15T20:42:37.090Z",
+            "programCode": [
+                "015:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Paducah Portsmouth Project Office"
+            },
+            "rights": "true",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "PPPO Portsmouth Pegasis"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bruce Meadows",
+                "hasEmail": "mailto:bruce.meadows@pad.pppo.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://pegasis.pad.pppo.gov/pdf/PEGASIS%20User%20Manual%202024.pdf",
+            "describedByType": "application/pdf",
+            "description": "PPPO Environmental Geographic Analytical Spatial Information System",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://pegasis.pad.pppo.gov/",
+                    "conformsTo": "https://pegasis.pad.pppo.gov/",
+                    "description": "PPPO Environmental Geographic Analytical Spatial Information System",
+                    "title": "Paducah Pegasis"
+                }
+            ],
+            "identifier": "Paducah Pegasis",
+            "issued": "2025-01-12",
+            "keyword": [
+                "arcgis"
+            ],
+            "landingPage": "https://pegasis.pad.pppo.gov/",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-15T20:52:14.034Z",
+            "programCode": [
+                "015:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Paducah Portsmouth Project Office"
+            },
+            "rights": "true",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "PPPO Paducah Pegasis"
         }
     ],
     "describedBy": "https://project-open-data.cio.gov/v1.1/schema/catalog.json"
```

### Changes from 75d151c to d9b5301
**Author:** Automated

**Date:** 2025-02-04 06:15:20+00:00

**Message:** Updated data: Tue Feb  4 06:15:20 UTC 2025

```diff
diff --git a/energy.json b/energy.json
index 9f62cf5..10d7813 100644
--- a/energy.json
+++ b/energy.json
@@ -29273,101 +29273,6 @@
                 "name": "DOE Office of Electricity"
             },
             "title": "Office of Electricity Information Center"
-        },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
-            "bureauCode": [
-                "015:11"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kyle Weatherholt",
-                "hasEmail": "mailto:kyle.weatherholt@ports.pppo.gov"
-            },
-            "dataQuality": true,
-            "describedBy": "https://pegasis.ports.pppo.gov/Documents/UserGuides/AnalyticalDataUserGuide.pdf",
-            "describedByType": "application/pdf",
-            "description": "Environmental Geographic Analytical Spatial Information System",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://pegasis.ports.pppo.gov/Pegasis/Default.aspx",
-                    "description": "PPPO Environmental Geographic Analytical Spatial Information System",
-                    "title": "PPPO Environmental Geographic Analytical Spatial Information System"
-                }
-            ],
-            "identifier": "Ports Pegasis",
-            "issued": "2024-08-08",
-            "keyword": [
-                "arcgis"
-            ],
-            "landingPage": "https://pegasis.ports.pppo.gov/Pegasis/Default.aspx",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2025-01-15T20:42:37.090Z",
-            "programCode": [
-                "015:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Paducah Portsmouth Project Office"
-            },
-            "rights": "true",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "PPPO Portsmouth Pegasis"
-        },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
-            "bureauCode": [
-                "015:11"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bruce Meadows",
-                "hasEmail": "mailto:bruce.meadows@pad.pppo.gov"
-            },
-            "dataQuality": true,
-            "describedBy": "https://pegasis.pad.pppo.gov/pdf/PEGASIS%20User%20Manual%202024.pdf",
-            "describedByType": "application/pdf",
-            "description": "PPPO Environmental Geographic Analytical Spatial Information System",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://pegasis.pad.pppo.gov/",
-                    "conformsTo": "https://pegasis.pad.pppo.gov/",
-                    "description": "PPPO Environmental Geographic Analytical Spatial Information System",
-                    "title": "Paducah Pegasis"
-                }
-            ],
-            "identifier": "Paducah Pegasis",
-            "issued": "2025-01-12",
-            "keyword": [
-                "arcgis"
-            ],
-            "landingPage": "https://pegasis.pad.pppo.gov/",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2025-01-15T20:52:14.034Z",
-            "programCode": [
-                "015:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Paducah Portsmouth Project Office"
-            },
-            "rights": "true",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "PPPO Paducah Pegasis"
         }
     ],
     "describedBy": "https://project-open-data.cio.gov/v1.1/schema/catalog.json"
```

### Changes from fc84d1a to 75d151c
**Author:** Automated

**Date:** 2025-02-04 04:12:27+00:00

**Message:** Updated data: Tue Feb  4 04:12:27 UTC 2025

```diff
diff --git a/energy.json b/energy.json
index 10d7813..9f62cf5 100644
--- a/energy.json
+++ b/energy.json
@@ -29273,6 +29273,101 @@
                 "name": "DOE Office of Electricity"
             },
             "title": "Office of Electricity Information Center"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kyle Weatherholt",
+                "hasEmail": "mailto:kyle.weatherholt@ports.pppo.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://pegasis.ports.pppo.gov/Documents/UserGuides/AnalyticalDataUserGuide.pdf",
+            "describedByType": "application/pdf",
+            "description": "Environmental Geographic Analytical Spatial Information System",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://pegasis.ports.pppo.gov/Pegasis/Default.aspx",
+                    "description": "PPPO Environmental Geographic Analytical Spatial Information System",
+                    "title": "PPPO Environmental Geographic Analytical Spatial Information System"
+                }
+            ],
+            "identifier": "Ports Pegasis",
+            "issued": "2024-08-08",
+            "keyword": [
+                "arcgis"
+            ],
+            "landingPage": "https://pegasis.ports.pppo.gov/Pegasis/Default.aspx",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-15T20:42:37.090Z",
+            "programCode": [
+                "015:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Paducah Portsmouth Project Office"
+            },
+            "rights": "true",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "PPPO Portsmouth Pegasis"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bruce Meadows",
+                "hasEmail": "mailto:bruce.meadows@pad.pppo.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://pegasis.pad.pppo.gov/pdf/PEGASIS%20User%20Manual%202024.pdf",
+            "describedByType": "application/pdf",
+            "description": "PPPO Environmental Geographic Analytical Spatial Information System",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://pegasis.pad.pppo.gov/",
+                    "conformsTo": "https://pegasis.pad.pppo.gov/",
+                    "description": "PPPO Environmental Geographic Analytical Spatial Information System",
+                    "title": "Paducah Pegasis"
+                }
+            ],
+            "identifier": "Paducah Pegasis",
+            "issued": "2025-01-12",
+            "keyword": [
+                "arcgis"
+            ],
+            "landingPage": "https://pegasis.pad.pppo.gov/",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-15T20:52:14.034Z",
+            "programCode": [
+                "015:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Paducah Portsmouth Project Office"
+            },
+            "rights": "true",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "PPPO Paducah Pegasis"
         }
     ],
     "describedBy": "https://project-open-data.cio.gov/v1.1/schema/catalog.json"
```

### Changes from 8cd3dfd to fc84d1a
**Author:** Automated

**Date:** 2025-02-04 01:38:52+00:00

**Message:** Updated data: Tue Feb  4 01:38:52 UTC 2025

```diff
diff --git a/energy.json b/energy.json
index 9f62cf5..10d7813 100644
--- a/energy.json
+++ b/energy.json
@@ -29273,101 +29273,6 @@
                 "name": "DOE Office of Electricity"
             },
             "title": "Office of Electricity Information Center"
-        },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
-            "bureauCode": [
-                "015:11"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Kyle Weatherholt",
-                "hasEmail": "mailto:kyle.weatherholt@ports.pppo.gov"
-            },
-            "dataQuality": true,
-            "describedBy": "https://pegasis.ports.pppo.gov/Documents/UserGuides/AnalyticalDataUserGuide.pdf",
-            "describedByType": "application/pdf",
-            "description": "Environmental Geographic Analytical Spatial Information System",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://pegasis.ports.pppo.gov/Pegasis/Default.aspx",
-                    "description": "PPPO Environmental Geographic Analytical Spatial Information System",
-                    "title": "PPPO Environmental Geographic Analytical Spatial Information System"
-                }
-            ],
-            "identifier": "Ports Pegasis",
-            "issued": "2024-08-08",
-            "keyword": [
-                "arcgis"
-            ],
-            "landingPage": "https://pegasis.ports.pppo.gov/Pegasis/Default.aspx",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2025-01-15T20:42:37.090Z",
-            "programCode": [
-                "015:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Paducah Portsmouth Project Office"
-            },
-            "rights": "true",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "PPPO Portsmouth Pegasis"
-        },
-        {
-            "@type": "dcat:Dataset",
-            "accessLevel": "public",
-            "accrualPeriodicity": "irregular",
-            "bureauCode": [
-                "015:11"
-            ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Bruce Meadows",
-                "hasEmail": "mailto:bruce.meadows@pad.pppo.gov"
-            },
-            "dataQuality": true,
-            "describedBy": "https://pegasis.pad.pppo.gov/pdf/PEGASIS%20User%20Manual%202024.pdf",
-            "describedByType": "application/pdf",
-            "description": "PPPO Environmental Geographic Analytical Spatial Information System",
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://pegasis.pad.pppo.gov/",
-                    "conformsTo": "https://pegasis.pad.pppo.gov/",
-                    "description": "PPPO Environmental Geographic Analytical Spatial Information System",
-                    "title": "Paducah Pegasis"
-                }
-            ],
-            "identifier": "Paducah Pegasis",
-            "issued": "2025-01-12",
-            "keyword": [
-                "arcgis"
-            ],
-            "landingPage": "https://pegasis.pad.pppo.gov/",
-            "language": [
-                "en-US"
-            ],
-            "modified": "2025-01-15T20:52:14.034Z",
-            "programCode": [
-                "015:001"
-            ],
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Paducah Portsmouth Project Office"
-            },
-            "rights": "true",
-            "theme": [
-                "geospatial"
-            ],
-            "title": "PPPO Paducah Pegasis"
         }
     ],
     "describedBy": "https://project-open-data.cio.gov/v1.1/schema/catalog.json"
```

### Changes from dd2190f to 8cd3dfd
**Author:** Automated

**Date:** 2025-02-04 00:32:07+00:00

**Message:** Updated data: Tue Feb  4 00:32:07 UTC 2025

```diff
diff --git a/energy.json b/energy.json
index 10d7813..9f62cf5 100644
--- a/energy.json
+++ b/energy.json
@@ -29273,6 +29273,101 @@
                 "name": "DOE Office of Electricity"
             },
             "title": "Office of Electricity Information Center"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kyle Weatherholt",
+                "hasEmail": "mailto:kyle.weatherholt@ports.pppo.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://pegasis.ports.pppo.gov/Documents/UserGuides/AnalyticalDataUserGuide.pdf",
+            "describedByType": "application/pdf",
+            "description": "Environmental Geographic Analytical Spatial Information System",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://pegasis.ports.pppo.gov/Pegasis/Default.aspx",
+                    "description": "PPPO Environmental Geographic Analytical Spatial Information System",
+                    "title": "PPPO Environmental Geographic Analytical Spatial Information System"
+                }
+            ],
+            "identifier": "Ports Pegasis",
+            "issued": "2024-08-08",
+            "keyword": [
+                "arcgis"
+            ],
+            "landingPage": "https://pegasis.ports.pppo.gov/Pegasis/Default.aspx",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-15T20:42:37.090Z",
+            "programCode": [
+                "015:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Paducah Portsmouth Project Office"
+            },
+            "rights": "true",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "PPPO Portsmouth Pegasis"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Bruce Meadows",
+                "hasEmail": "mailto:bruce.meadows@pad.pppo.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://pegasis.pad.pppo.gov/pdf/PEGASIS%20User%20Manual%202024.pdf",
+            "describedByType": "application/pdf",
+            "description": "PPPO Environmental Geographic Analytical Spatial Information System",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://pegasis.pad.pppo.gov/",
+                    "conformsTo": "https://pegasis.pad.pppo.gov/",
+                    "description": "PPPO Environmental Geographic Analytical Spatial Information System",
+                    "title": "Paducah Pegasis"
+                }
+            ],
+            "identifier": "Paducah Pegasis",
+            "issued": "2025-01-12",
+            "keyword": [
+                "arcgis"
+            ],
+            "landingPage": "https://pegasis.pad.pppo.gov/",
+            "language": [
+                "en-US"
+            ],
+            "modified": "2025-01-15T20:52:14.034Z",
+            "programCode": [
+                "015:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Paducah Portsmouth Project Office"
+            },
+            "rights": "true",
+            "theme": [
+                "geospatial"
+            ],
+            "title": "PPPO Paducah Pegasis"
         }
     ],
     "describedBy": "https://project-open-data.cio.gov/v1.1/schema/catalog.json"
```

### Changes from 31606f9 to dd2190f (Part 1/2)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
diff --git a/energy.json b/energy.json
index fc968d2..10d7813 100644
--- a/energy.json
+++ b/energy.json
@@ -1,39 +1,31 @@
 {
-    "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
-    "describedBy": "https://project-open-data.cio.gov/v1.1/schema/catalog.json",
     "@context": "https://project-open-data.cio.gov/v1.1/schema/catalog.jsonld",
     "@type": "dcat:Catalog",
+    "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
     "dataset": [
         {
             "@type": "dcat:Dataset",
-            "title": "DOE Hearings and Appeals Case Decisions",
-            "description": "The Office of Hearings and Appeals (HG) is the quasi-judicial arm of the Department of Energy that conducts hearings and issues initial Departmental decisions with respect to a wide range of legal issues and programs delegated to the Office by the Secretary of Energy, including: 1) personnel security clearance eligibility determinations, 2) DOE contractor employee \"whistleblower\" cases, 3) Freedom of Information and Privacy Act appeals, as well as other appeals involving administrative determinations reached by Department officials, 4) Applications for Exception from the requirements of a DOE rule, regulation or order, and 5) Petitions for Special Redress seeking \"extraordinary relief\" -- apart from or in addition to -- any other remedy provided in the Department's enabling statutes.",
-            "modified": "2014-04-25",
             "accessLevel": "public",
-            "identifier": "DOE-019-4381227569",
-            "dataQuality": true,
-            "landingPage": "http://energy.gov/oha/",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "United States",
-            "temporal": "1994/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE/Office of Hearings and Appeals"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "019:60"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Fred Brown",
                 "hasEmail": "mailto:Fred.Brown@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "The Office of Hearings and Appeals (HG) is the quasi-judicial arm of the Department of Energy that conducts hearings and issues initial Departmental decisions with respect to a wide range of legal issues and programs delegated to the Office by the Secretary of Energy, including: 1) personnel security clearance eligibility determinations, 2) DOE contractor employee \"whistleblower\" cases, 3) Freedom of Information and Privacy Act appeals, as well as other appeals involving administrative determinations reached by Department officials, 4) Applications for Exception from the requirements of a DOE rule, regulation or order, and 5) Petitions for Special Redress seeking \"extraordinary relief\" -- apart from or in addition to -- any other remedy provided in the Department's enabling statutes.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://energy.gov/oha/",
                     "mediaType": "text/csv",
-                    "title": "Case Decisions",
-                    "downloadURL": "https://energy.gov/oha/"
+                    "title": "Case Decisions"
                 }
             ],
+            "identifier": "DOE-019-4381227569",
             "keyword": [
                 "Appeals",
                 "Crude",
@@ -52,92 +44,90 @@
                 "Worker Appeal",
                 "Worker Health"
             ],
-            "bureauCode": [
-                "019:60"
+            "landingPage": "http://energy.gov/oha/",
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2014-04-25",
             "programCode": [
                 "019:053"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE/Office of Hearings and Appeals"
+            },
+            "spatial": "United States",
+            "temporal": "1994/2014",
             "theme": [
                 "corporate management"
-            ]
+            ],
+            "title": "DOE Hearings and Appeals Case Decisions"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Energy.gov",
-            "description": "Energy.gov is hosted in the Drupal environment at a BlackMesh provided data center.  Public access information is continuously updated by various DOE elements in an unstructured format.",
-            "modified": "2015-01-22",
             "accessLevel": "public",
-            "identifier": "DOE-019-3665989539",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "rights": "Content Management functions are Private.  Content itself is public.",
-            "spatial": "DOE",
-            "temporal": "2014-01-01/2014-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Office of Chief Information Officer"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "019:60"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Oneill",
                 "hasEmail": "mailto:Thomas.Oneill@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "Energy.gov is hosted in the Drupal environment at a BlackMesh provided data center.  Public access information is continuously updated by various DOE elements in an unstructured format.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://energy.gov/",
                     "format": "text/csv",
-                    "title": "Energy.gov",
-                    "downloadURL": "https://energy.gov/"
+                    "mediaType": "text/html",
+                    "title": "Energy.gov"
                 }
             ],
+            "identifier": "DOE-019-3665989539",
             "keyword": [
                 "energy saver",
                 "offices",
                 "public service",
                 "service and innovation"
             ],
-            "bureauCode": [
-                "019:60"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2015-01-22",
             "programCode": [
                 "019:053"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Office of Chief Information Officer"
+            },
+            "rights": "Content Management functions are Private.  Content itself is public.",
+            "spatial": "DOE",
+            "temporal": "2014-01-01/2014-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Energy.gov"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "ARPA-E Projects",
-            "description": "ARPA-E\u2019s initial $400 million budget was a part of the 2009 American Recovery and Reinvestment Act. ARPA-E received $180 million in Fiscal Year 2011 and $275 million in Fiscal Year 2012. Below you will find information on ARPA-E\u2019s fiscal year budget requests.",
-            "modified": "2022-09-14T16:33:43.937Z",
             "accessLevel": "public",
-            "identifier": "DOE-019-3478552234",
-            "dataQuality": true,
-            "landingPage": "http://www.energy.gov",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "rights": "true",
-            "spatial": "DOE",
-            "temporal": "2005/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE ARPA-E"
-            },
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dane Boysen",
                 "hasEmail": "mailto:dane.boysen@doe.gov"
             },
+            "dataQuality": true,
+            "description": "ARPA-E\u2019s initial $400 million budget was a part of the 2009 American Recovery and Reinvestment Act. ARPA-E received $180 million in Fiscal Year 2011 and $275 million in Fiscal Year 2012. Below you will find information on ARPA-E\u2019s fiscal year budget requests.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -147,16 +137,17 @@
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://arpa-e.energy.gov/",
-                    "title": "ARPA Web Page",
-                    "description": "This is the starting point for ARPA-E information."
+                    "description": "This is the starting point for ARPA-E information.",
+                    "title": "ARPA Web Page"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://arpa-e.energy.gov/technologies/projects",
-                    "title": "ARPA-e Projects",
-                    "description": "This web page contains the ARPA-e technologies."
+                    "description": "This web page contains the ARPA-e technologies.",
+                    "title": "ARPA-e Projects"
                 }
             ],
+            "identifier": "DOE-019-3478552234",
             "keyword": [
                 "appropriation language",
                 "arpa-e program direction",
@@ -165,87 +156,87 @@
                 "overview",
                 "small business innovation research"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "http://www.energy.gov",
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2022-09-14T16:33:43.937Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE ARPA-E"
+            },
+            "rights": "true",
+            "spatial": "DOE",
+            "temporal": "2005/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "ARPA-E Projects"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Congressional and Intergovernmental Affairs Testimony",
-            "description": "This site contains five years of testimonies.",
-            "modified": "2014-11-30",
             "accessLevel": "public",
-            "identifier": "DOE-019-2257845237",
-            "dataQuality": true,
-            "landingPage": "http://energy.gov/congressional/listings/congressional-testimony",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "DOE",
-            "temporal": "2009/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Congressional and Intergovernmental Affairs"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "019:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Shari Davenport",
                 "hasEmail": "mailto:shari.davenport@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "This site contains five years of testimonies.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://energy.gov/congressional/listings/congressional-testimony",
                     "mediaType": "text/html",
-                    "title": "CI Testimony",
-                    "downloadURL": "https://energy.gov/congressional/listings/congressional-testimony"
+                    "title": "CI Testimony"
                 }
             ],
+            "identifier": "DOE-019-2257845237",
             "keyword": [
                 "testimony"
             ],
-            "bureauCode": [
-                "019:00"
+            "landingPage": "http://energy.gov/congressional/listings/congressional-testimony",
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2014-11-30",
             "programCode": [
                 "019:000"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Congressional and Intergovernmental Affairs"
+            },
+            "spatial": "DOE",
+            "temporal": "2009/2014",
             "theme": [
                 "corporate management"
-            ]
+            ],
+            "title": "Congressional and Intergovernmental Affairs Testimony"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Administrative Record Publishing Website",
-            "description": "Website that communicates certain Hanford information to the public. Tri-party agreement.",
-            "modified": "2014-10-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-7545783421-1",
-            "dataQuality": true,
-            "landingPage": "http://pdw.hanford.gov/arpir/",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "DOE",
-            "temporal": "1940/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE/Richland Operations and the Office of River Protection"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "019:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Miljana Mijic",
                 "hasEmail": "mailto:miljana_g_mijic@rl.gov"
             },
+            "dataQuality": true,
+            "description": "Website that communicates certain Hanford information to the public. Tri-party agreement.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -253,47 +244,47 @@
                     "title": "ARPIR Data Warehouse"
                 }
             ],
+            "identifier": "DOE-019-7545783421-1",
             "keyword": [
                 "Hanford",
                 "cleanup",
                 "environment",
                 "mission"
             ],
-            "bureauCode": [
-                "019:10"
+            "landingPage": "http://pdw.hanford.gov/arpir/",
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2014-10-01",
             "programCode": [
                 "019:051"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE/Richland Operations and the Office of River Protection"
+            },
+            "spatial": "DOE",
+            "temporal": "1940/2014",
             "theme": [
                 "environment"
-            ]
+            ],
+            "title": "Administrative Record Publishing Website"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Congressional and Intergovernmental Affairs webpage",
-            "description": "The Office of Congressional and Intergovernmental Affairs is dedicated to its mission of providing guidance on legislative and policy issues, informing constituencies on energy matters, and serving as a liaison between the Department, Congress, State, local, and Tribal governments, as well as other Federal agencies and stakeholder groups.",
-            "modified": "2015-02-20",
             "accessLevel": "public",
-            "identifier": "DOE-019-4578239451",
-            "dataQuality": true,
-            "landingPage": "http://energy.gov/congressional/office-congressional-and-intergovernmental-affairs",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "DOE",
-            "temporal": "2009/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Congressional and Intergovernmental Affairs"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "019:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Shari Davenport",
                 "hasEmail": "mailto:shari.davenport@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "The Office of Congressional and Intergovernmental Affairs is dedicated to its mission of providing guidance on legislative and policy issues, informing constituencies on energy matters, and serving as a liaison between the Department, Congress, State, local, and Tribal governments, as well as other Federal agencies and stakeholder groups.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -301,58 +292,55 @@
                     "title": "CI Web"
                 }
             ],
+            "identifier": "DOE-019-4578239451",
             "keyword": [
                 "about us",
                 "mission"
             ],
-            "bureauCode": [
-                "019:00"
+            "landingPage": "http://energy.gov/congressional/office-congressional-and-intergovernmental-affairs",
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2015-02-20",
             "programCode": [
                 "019:000"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Congressional and Intergovernmental Affairs"
+            },
+            "spatial": "DOE",
+            "temporal": "2009/2014",
             "theme": [
                 "corporate management"
-            ]
+            ],
+            "title": "Congressional and Intergovernmental Affairs webpage"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Economic Impact and Diversity webpage",
-            "description": "The Office of Economic Impact and Diversity develops and executes Department-wide policies to implement applicable legislation and Executive Orders that strengthen diversity goals affecting equal employment opportunities, small and disadvantaged businesses, minority educational institutions, and historically underrepresented communities.\r\n\r\nOur mission is to identify and implement ways of ensuring that minorities are afforded an opportunity to participate fully in the energy programs of the Department. We encourage partnership opportunities with Minority Serving Institutions (Historically Black Colleges and Universities, Hispanic Serving Institutions, Asian American, Native American, and Pacific Islander Institutions, and Tribal Colleges and Universities) and other minority-owned and serving entities on our mission-critical work.\r\n\r\nWe serve as a strong advocate for equal employment opportunities, civil rights concerns, and non-discriminatory practices at the Department. In addition, the Office of Economic Impact and Diversity is charged with creating and sustaining a high performing, inclusive workforce by leveraging diversity and empowering all employees to achieve superior results in the service of our Nation.\r\n\r\nOur office measures success in its effectiveness in aiding the disadvantaged in finding opportunities at the Department of Energy and in other Federal programs. Through extensive research and close partnerships, we have been able to specifically target barriers to minorities and execute strategies to overcome them. The Office of Economic Impact and Diversity is a model of how diversity positively impacts the Energy Department and provides a unique, cutting-edge quality to the Department.",
-            "modified": "2014-11-28",
             "accessLevel": "public",
-            "identifier": "DOE-019-2367548921",
-            "dataQuality": true,
-            "landingPage": "http://energy.gov/diversity/office-economic-impact-and-diversity",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "DOE",
-            "temporal": "2012/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of Civil Rights",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "DOE Economic Impact and Diversity"
-                }
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "019:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Andre Sayles",
                 "hasEmail": "mailto:andre.sayles@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "The Office of Economic Impact and Diversity develops and executes Department-wide policies to implement applicable legislation and Executive Orders that strengthen diversity goals affecting equal employment opportunities, small and disadvantaged businesses, minority educational institutions, and historically underrepresented communities.\r\n\r\nOur mission is to identify and implement ways of ensuring that minorities are afforded an opportunity to participate fully in the energy programs of the Department. We encourage partnership opportunities with Minority Serving Institutions (Historically Black Colleges and Universities, Hispanic Serving Institutions, Asian American, Native American, and Pacific Islander Institutions, and Tribal Colleges and Universities) and other minority-owned and serving entities on our mission-critical work.\r\n\r\nWe serve as a strong advocate for equal employment opportunities, civil rights concerns, and non-discriminatory practices at the Department. In addition, the Office of Economic Impact and Diversity is charged with creating and sustaining a high performing, inclusive workforce by leveraging diversity and empowering all employees to achieve superior results in the service of our Nation.\r\n\r\nOur office measures success in its effectiveness in aiding the disadvantaged in finding opportunities at the Department of Energy and in other Federal programs. Through extensive research and close partnerships, we have been able to specifically target barriers to minorities and execute strategies to overcome them. The Office of Economic Impact and Diversity is a model of how diversity positively impacts the Energy Department and provides a unique, cutting-edge quality to the Department.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
-                    "title": "ED Web",
                     "description": "ED Web",
-                    "downloadURL": "https://energy.gov/diversity/office-economic-impact-and-diversity"
+                    "downloadURL": "https://energy.gov/diversity/office-economic-impact-and-diversity",
+                    "mediaType": "text/html",
+                    "title": "ED Web"
                 }
             ],
+            "identifier": "DOE-019-2367548921",
             "keyword": [
                 "STEM",
                 "civil rights",
@@ -366,40 +354,44 @@
                 "tribal communities",
                 "under-represented communities"
             ],
-            "bureauCode": [
-                "019:00"
+            "landingPage": "http://energy.gov/diversity/office-economic-impact-and-diversity",
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2014-11-28",
             "programCode": [
                 "019:000"
             ],
-            "language": [
-                "en-US"
-            ],
-            "theme": [
-                "civil rights"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Energy Policy and Systems Analysis webpage",
-            "description": "The Director of the Office of Energy Policy and Systems Analysis is the primary energy policy advisor to the Secretary and Deputy Secretary on domestic energy policy development and implementation as well as DOE policy analysis and activities.\r\n\r\nThe role of the Office of Energy Policy and Systems Analysis is to deliver unbiased energy analysis to the Department of Energy's leadership on existing and prospective energy-related policies, focusing in part on integrative analysis of energy systems.\r\n\r\nThe Office of Energy Policy and Systems Analysis includes the Secretariat of the Quadrennial Energy Review with primary responsibility for supporting the White House interagency process and providing to it data collection, analysis, stakeholder engagement, and data synthesis.",
-            "modified": "2014-11-15",
-            "accessLevel": "public",
-            "identifier": "DOE-019-0334675232",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "DOE",
-            "temporal": "2012/2014",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "DOE Energy Policy and Systems Analysis"
+                "name": "Office of Civil Rights",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "DOE Economic Impact and Diversity"
+                }
+            },
+            "spatial": "DOE",
+            "temporal": "2012/2015",
+            "theme": [
+                "civil rights"
+            ],
+            "title": "Economic Impact and Diversity webpage"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "019:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Melanie Kenderdine",
                 "hasEmail": "mailto:melanie.kenderdine@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "The Director of the Office of Energy Policy and Systems Analysis is the primary energy policy advisor to the Secretary and Deputy Secretary on domestic energy policy development and implementation as well as DOE policy analysis and activities.\r\n\r\nThe role of the Office of Energy Policy and Systems Analysis is to deliver unbiased energy analysis to the Department of Energy's leadership on existing and prospective energy-related policies, focusing in part on integrative analysis of energy systems.\r\n\r\nThe Office of Energy Policy and Systems Analysis includes the Secretariat of the Quadrennial Energy Review with primary responsibility for supporting the White House interagency process and providing to it data collection, analysis, stakeholder engagement, and data synthesis.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -407,6 +399,7 @@
                     "title": "EPSA Web"
                 }
             ],
+            "identifier": "DOE-019-0334675232",
             "keyword": [
                 "QER",
                 "climate",
@@ -417,41 +410,39 @@
                 "revolution now",
                 "vulnerability report"
             ],
-            "bureauCode": [
-                "019:00"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2014-11-15",
             "programCode": [
                 "019:000"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Energy Policy and Systems Analysis"
+            },
+            "spatial": "DOE",
+            "temporal": "2012/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Energy Policy and Systems Analysis webpage"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "The Quadrennial Energy Review (QER)",
-            "description": "Affordable, clean, and secure energy and energy services are essential for improving U.S. economic productivity, enhancing our quality of life, protecting our environment, and ensuring our Nation's security. To help the federal government meet these energy goals, President Obama issued a Presidential Memorandum on January 9 directing the administration to conduct a Quadrennial Energy Review (QER). As described in the President\u2019s Climate Action Plan, this first-ever review will focus on energy infrastructure and will identify the threats, risks, and opportunities for U.S. energy and climate security, enabling the federal government to translate policy goals into a set of integrated actions. The Presidential Memorandum created an interagency task force co-chaired by the Director of the Office of Science and Technology Policy and the Special Assistant to the President for Energy and Climate Change. The Department of Energy will help coordinate interagency activities and provide policy analysis and modeling, and stakeholder engagement.",
-            "modified": "2022-09-26T17:11:58.556Z",
             "accessLevel": "public",
-            "identifier": "DOE-019-0334675231",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "rights": "true",
-            "spatial": "DOE",
-            "temporal": "2012/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Energy Policy and Systems Analysis"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOE-QTR2015 Mailbox",
                 "hasEmail": "mailto:DOE-QTR2015@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "Affordable, clean, and secure energy and energy services are essential for improving U.S. economic productivity, enhancing our quality of life, protecting our environment, and ensuring our Nation's security. To help the federal government meet these energy goals, President Obama issued a Presidential Memorandum on January 9 directing the administration to conduct a Quadrennial Energy Review (QER). As described in the President\u2019s Climate Action Plan, this first-ever review will focus on energy infrastructure and will identify the threats, risks, and opportunities for U.S. energy and climate security, enabling the federal government to translate policy goals into a set of integrated actions. The Presidential Memorandum created an interagency task force co-chaired by the Director of the Office of Science and Technology Policy and the Special Assistant to the President for Energy and Climate Change. The Department of Energy will help coordinate interagency activities and provide policy analysis and modeling, and stakeholder engagement.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -459,44 +450,45 @@
                     "title": "QER"
                 }
             ],
+            "identifier": "DOE-019-0334675231",
             "keyword": [
                 "QER report",
                 "stakeholder"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2022-09-26T17:11:58.556Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Energy Policy and Systems Analysis"
+            },
+            "rights": "true",
+            "spatial": "DOE",
+            "temporal": "2012/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "The Quadrennial Energy Review (QER)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Indian Energy Policy and Programs webpage",
-            "description": "The U.S. Department of Energy (DOE) Office of Indian Energy Policy and Programs, or the Office of Indian Energy, is charged by Congress to direct, foster, coordinate, and implement energy planning, education, management, and programs that assist tribes with energy development, capacity building, energy infrastructure, energy costs, and electrification of Indian lands and homes.\r\n\r\nThe Office of Indian Energy works within DOE, across government agencies, and with Indian Tribes and organizations to promote Indian energy policies and initiatives. The Office of Indian Energy performs these functions within the scope of DOE's mission and consistently with the federal government's trust responsibility, tribal self-determination policy, and government-to-government relationship with Indian Tribes.",
-            "modified": "2014-11-15",
             "accessLevel": "public",
-            "identifier": "DOE-019-3478123451",
-            "dataQuality": true,
-            "license": "http://opendatacommons.org/licenses/pddl/",
-            "spatial": "DOE",
-            "temporal": "2012/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Indian Energy Policy and Programs"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "019:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tracey A. Lebeau",
                 "hasEmail": "mailto:tracey.lebeau@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "The U.S. Department of Energy (DOE) Office of Indian Energy Policy and Programs, or the Office of Indian Energy, is charged by Congress to direct, foster, coordinate, and implement energy planning, education, management, and programs that assist tribes with energy development, capacity building, energy infrastructure, energy costs, and electrification of Indian lands and homes.\r\n\r\nThe Office of Indian Energy works within DOE, across government agencies, and with Indian Tribes and organizations to promote Indian energy policies and initiatives. The Office of Indian Energy performs these functions within the scope of DOE's mission and consistently with the federal government's trust responsibility, tribal self-determination policy, and government-to-government relationship with Indian Tribes.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -504,6 +496,7 @@
                     "title": "Indian Energy web"
                 }
             ],
+            "identifier": "DOE-019-3478123451",
             "keyword": [
                 "Alaska native villages",
                 "strategic technical assistance response team",
@@ -512,41 +505,39 @@
                 "tribal leader and best practices forums",
                 "tribal summit"
             ],
-            "bureauCode": [
-                "019:00"
+            "language": [
+                "en-US"
             ],
+            "license": "http://opendatacommons.org/licenses/pddl/",
+            "modified": "2014-11-15",
             "programCode": [
                 "019:000"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Indian Energy Policy and Programs"
+            },
+            "spatial": "DOE",
+            "temporal": "2012/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Indian Energy Policy and Programs webpage"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Loan Programs Office website",
-            "description": "The Department of Energy's Loan Programs-administered by LPO-enable DOE to work with private companies and lenders to mitigate the financing risks associated with clean energy projects, and thereby encourage their development on a broader and much-needed scale.\r\n\r\nThe Loan Programs consist of three separate programs managed by two offices, the Loan Guarantee Program Office (LGP) and the Advanced Technology Vehicles Manufacturing Loan Program Office. LPO originates, guarantees, and monitors loans to support clean energy projects through these programs. The programs are:\r\n\r\nSection 1703: Under Section 1703 of Title XVII, DOE LGP is authorized to guarantee loans for projects that employ new or significantly improved energy technologies and avoid, reduce or sequester air pollutants or greenhouse gases. \r\nSection 1705: Under Section 1705 of Title XVII, added by the American Reinvestment and Recovery Act (ARRA), DOE LGP is authorized to guarantee loans for certain clean energy projects that commenced construction on or before September 30, 2011. The Section 1705 program expired, pursuant to statute, on September 30, 2011 and will actively monitor projects that previously received loan guarantees under the 1705 program. LPO will no longer issue new loan guarantees under the 1705 program. \r\nAdvanced Technology Vehicles Manufacturing (ATVM): Under Section 136 of the Energy Independence and Security Act of 2007, DOE is authorized to provide direct loans to finance advanced vehicle technologies.",
-            "modified": "2014-11-15",
             "accessLevel": "public",
-            "identifier": "DOE-019-4444578911",
-            "dataQuality": true,
-            "landingPage": "http://energy.gov/lpo/loan-programs-office",
-            "license": "http://opendatacommons.org/licenses/pddl/",
-            "spatial": "United States",
-            "temporal": "2005/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Loan Programs Office"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "019:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Peter Davidson",
                 "hasEmail": "mailto:peter.davidson@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "The Department of Energy's Loan Programs-administered by LPO-enable DOE to work with private companies and lenders to mitigate the financing risks associated with clean energy projects, and thereby encourage their development on a broader and much-needed scale.\r\n\r\nThe Loan Programs consist of three separate programs managed by two offices, the Loan Guarantee Program Office (LGP) and the Advanced Technology Vehicles Manufacturing Loan Program Office. LPO originates, guarantees, and monitors loans to support clean energy projects through these programs. The programs are:\r\n\r\nSection 1703: Under Section 1703 of Title XVII, DOE LGP is authorized to guarantee loans for projects that employ new or significantly improved energy technologies and avoid, reduce or sequester air pollutants or greenhouse gases. \r\nSection 1705: Under Section 1705 of Title XVII, added by the American Reinvestment and Recovery Act (ARRA), DOE LGP is authorized to guarantee loans for certain clean energy projects that commenced construction on or before September 30, 2011. The Section 1705 program expired, pursuant to statute, on September 30, 2011 and will actively monitor projects that previously received loan guarantees under the 1705 program. LPO will no longer issue new loan guarantees under the 1705 program. \r\nAdvanced Technology Vehicles Manufacturing (ATVM): Under Section 136 of the Energy Independence and Security Act of 2007, DOE is authorized to provide direct loans to finance advanced vehicle technologies.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -554,6 +545,7 @@
                     "title": "Loan Program"
                 }
             ],
+            "identifier": "DOE-019-4444578911",
             "keyword": [
                 "ATVM loan program",
                 "application process",
@@ -562,49 +554,50 @@
                 "section 1703 loan program",
                 "section 1705 loan program"
             ],
-            "bureauCode": [
-                "019:00"
+            "landingPage": "http://energy.gov/lpo/loan-programs-office",
+            "language": [
+                "en-US"
             ],
+            "license": "http://opendatacommons.org/licenses/pddl/",
+            "modified": "2014-11-15",
             "programCode": [
                 "019:000"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Loan Programs Office"
+            },
+            "spatial": "United States",
+            "temporal": "2005/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Loan Programs Office website"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Office of the Chief Information Officer web",
-            "description": "The mission of the Office of the Chief Information Officer (OCIO) is to enable the Department of Energy\u2019s urgent missions in energy, science and nuclear security through the power of information and technology in a manner that balances risk with required outcomes in programs that span from open science to national security.",
-            "modified": "2014-11-15",
             "accessLevel": "public",
-            "identifier": "DOE-019-3478654789",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "DOE",
-            "temporal": "2013-01-01/2014-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Office of Chief Information Officer"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "019:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "CIO Webmaster",
                 "hasEmail": "mailto:cio.webmaster@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "The mission of the Office of the Chief Information Officer (OCIO) is to enable the Department of Energy\u2019s urgent missions in energy, science and nuclear security through the power of information and technology in a manner that balances risk with required outcomes in programs that span from open science to national security.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
-                    "title": "CIO web",
                     "description": "The beginning point for information regarding the OCIO.",
-                    "downloadURL": "https://www.energy.gov/cio/office-chief-information-officer"
+                    "downloadURL": "https://www.energy.gov/cio/office-chief-information-officer",
+                    "mediaType": "text/html",
+                    "title": "CIO web"
                 }
             ],
+            "identifier": "DOE-019-3478654789",
             "keyword": [
                 "FY 2014-2018 DOE IRM Strategic Plan",
                 "IT services",
@@ -620,40 +613,39 @@
                 "mobility",
                 "remote access"
             ],
-            "bureauCode": [
-                "019:00"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2014-11-15",
             "programCode": [
                 "019:000"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Office of Chief Information Officer"
+            },
+            "spatial": "DOE",
+            "temporal": "2013-01-01/2014-12-31",
             "theme": [
                 "corporate management"
-            ]
+            ],
+            "title": "Office of the Chief Information Officer web"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Affairs webpage",
-            "description": "IA has the primary responsibility for coordinating the efforts of diverse elements in the Department to ensure a unified voice in our international energy policy. IA works closely with Departmental elements, other Federal agencies, national and international organizations and institutions, and the private sector to coordinate and align our international energy activities with our national energy policies. IA coordinates DOE international initiatives on clean energy, climate change, and technology exports.\r\n\r\nIA works closely with DOE program Assistant Secretaries and other DOE Secretarial officers to identify top international priorities among the activities of the Department, and to engage with other Federal departments and agencies (including the National Security Council, Office of Management and Budget, and other White House offices), members of Congress and Congressional Committees, and energy producers and consumers.\r\n\r\nThe Assistant Secretary coordinates and manages DOE cooperation with counterparts from other nations and international organizations. IA also negotiates and manages a variety of bilateral and multilateral agreements with other countries and international agencies for cooperation in research and development for energy, environmental, and technology cooperation.",
-            "modified": "2014-11-15",
             "accessLevel": "public",
-            "identifier": "DOE-019-3489568912",
-            "dataQuality": true,
-            "license": "http://opendatacommons.org/licenses/pddl/",
-            "spatial": "Global",
-            "temporal": "2012/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE International Affairs"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "019:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Miyoshi W. Stith",
                 "hasEmail": "mailto:miyoshi.stith@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "IA has the primary responsibility for coordinating the efforts of diverse elements in the Department to ensure a unified voice in our international energy policy. IA works closely with Departmental elements, other Federal agencies, national and international organizations and institutions, and the private sector to coordinate and align our international energy activities with our national energy policies. IA coordinates DOE international initiatives on clean energy, climate change, and technology exports.\r\n\r\nIA works closely with DOE program Assistant Secretaries and other DOE Secretarial officers to identify top international priorities among the activities of the Department, and to engage with other Federal departments and agencies (including the National Security Council, Office of Management and Budget, and other White House offices), members of Congress and Congressional Committees, and energy producers and consumers.\r\n\r\nThe Assistant Secretary coordinates and manages DOE cooperation with counterparts from other nations and international organizations. IA also negotiates and manages a variety of bilateral and multilateral agreements with other countries and international agencies for cooperation in research and development for energy, environmental, and technology cooperation.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -661,6 +653,7 @@
                     "title": "IA Web"
                 }
             ],
+            "identifier": "DOE-019-3489568912",
             "keyword": [
                 "U.S.-Africa energy ministerial",
                 "U.S.-Canada clean energy dialogue",
@@ -674,40 +667,39 @@
                 "international energy agency",
                 "turkey near-zero zone"
             ],
-            "bureauCode": [
-                "019:00"
+            "language": [
+                "en-US"
             ],
+            "license": "http://opendatacommons.org/licenses/pddl/",
+            "modified": "2014-11-15",
             "programCode": [
                 "019:000"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE International Affairs"
+            },
+            "spatial": "Global",
+            "temporal": "2012/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Affairs webpage"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Inspector General webpage",
-            "description": "Office of Inspector General mission is to help the Department and the American taxpayer by:\r\n\r\n--Identifying opportunities for cost savings and operational efficiencies in Department programs; and \r\n--Returning hard dollars to the Department and the U.S. Treasury as a result of Office of Inspector General civil and criminal investigations. \r\n\r\nIn our service we have:\r\n\r\n--Assisted the Department, including the National Nuclear Security Administration, in identifying key management challenges such as the aging of the nuclear weapons complex infrastructure and the emerging human capital crisis; \r\n--Facilitated efforts to reform Department security, by identifying both systemic and situational vulnerabilities; \r\n--Annually audited the agency's financial statements, helping to ensure that the Department does that which every American business must do: balance its books; \r\n--Highlighted opportunities for reductions in overhead costs in environmental management and defense programs; \r\n--Investigated and helped bring to justice those who have committed crimes against the Department, with recent special emphasis on cyber crimes at an agency which owns and operates some of the most sophisticated supercomputers in the world; and \r\n--Issued a host of reports identifying concrete opportunities to reform Department: contract management; waste management; environment, safety and health stewardship; research and development; major facilities and project construction and operation; and human capital.",
-            "modified": "2014-11-15",
             "accessLevel": "public",
-            "identifier": "DOE-019-3423678761",
-            "dataQuality": true,
-            "license": "http://opendatacommons.org/licenses/pddl/",
-            "spatial": "DOE",
-            "temporal": "2012/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Inspector General"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "019:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tara Porter",
                 "hasEmail": "mailto:tara.porter@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "Office of Inspector General mission is to help the Department and the American taxpayer by:\r\n\r\n--Identifying opportunities for cost savings and operational efficiencies in Department programs; and \r\n--Returning hard dollars to the Department and the U.S. Treasury as a result of Office of Inspector General civil and criminal investigations. \r\n\r\nIn our service we have:\r\n\r\n--Assisted the Department, including the National Nuclear Security Administration, in identifying key management challenges such as the aging of the nuclear weapons complex infrastructure and the emerging human capital crisis; \r\n--Facilitated efforts to reform Department security, by identifying both systemic and situational vulnerabilities; \r\n--Annually audited the agency's financial statements, helping to ensure that the Department does that which every American business must do: balance its books; \r\n--Highlighted opportunities for reductions in overhead costs in environmental management and defense programs; \r\n--Investigated and helped bring to justice those who have committed crimes against the Department, with recent special emphasis on cyber crimes at an agency which owns and operates some of the most sophisticated supercomputers in the world; and \r\n--Issued a host of reports identifying concrete opportunities to reform Department: contract management; waste management; environment, safety and health stewardship; research and development; major facilities and project construction and operation; and human capital.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -716,107 +708,107 @@
                     "title": "IG web"
                 }
             ],
+            "identifier": "DOE-019-3423678761",
             "keyword": [
                 "FOIA",
                 "audits and inspections",
                 "investigations",
                 "whistleblower"
             ],
-            "bureauCode": [
-                "019:00"
+            "language": [
+                "en-US"
             ],
+            "license": "http://opendatacommons.org/licenses/pddl/",
+            "modified": "2014-11-15",
             "programCode": [
                 "019:000"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Inspector General"
+            },
+            "spatial": "DOE",
+            "temporal": "2012/2014",
             "theme": [
                 "corporate managemetn"
-            ]
+            ],
+            "title": "Inspector General webpage"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Survey Tool",
-            "description": "Survey tool that allows the administrator to email a survey to a specific individual or to multiple people.  It is used for feds and contractors.",
-            "modified": "2022-08-30T12:48:33.230Z",
             "accessLevel": "non-public",
-            "identifier": "DOE-019-2239024589",
-            "dataQuality": true,
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "conformsTo": "https://www.id.energy.gov/",
-            "describedBy": "https://www.id.energy.gov/Surveys/",
-            "describedByType": "text/html",
-            "issued": "2016-01-01",
-            "landingPage": "https://www.id.energy.gov/Surveys/",
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "rights": "Access is only available to DOE-ID Feds and Contractors",
-            "systemOfRecords": "none",
-            "spatial": "DOE",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Idaho Operations Office",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Idaho Operations Office"
-                }
-            },
-            "accrualPeriodicity": "irregular",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tammy Peterson",
                 "hasEmail": "mailto:peterste@id.doe.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.id.energy.gov/Surveys/",
+            "describedByType": "text/html",
+            "description": "Survey tool that allows the administrator to email a survey to a specific individual or to multiple people.  It is used for feds and contractors.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.id.energy.gov/surveys",
+                    "description": "This is a tool used to allow DOE Idaho Operations to conduct surveys of employees for valuable feedback",
                     "format": "aspx",
-                    "title": "Survey",
-                    "description": "This is a tool used to allow DOE Idaho Operations to conduct surveys of employees for valuable feedback"
+                    "title": "Survey"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.id.energy.gov/surveys",
-                    "title": "Survey Tool",
-                    "description": "This is a site the is utilized by DOE-ID people and subcontractors to get helpful information for the organizations and where the issues are. this allows orgs to address concerns with in the DOE-ID departments. this is not available to the public."
+                    "description": "This is a site the is utilized by DOE-ID people and subcontractors to get helpful information for the organizations and where the issues are. this allows orgs to address concerns with in the DOE-ID departments. this is not available to the public.",
+                    "title": "Survey Tool"
                 }
             ],
+            "identifier": "DOE-019-2239024589",
+            "issued": "2016-01-01",
             "keyword": [
                 "DOE-ID",
                 "Peterson",
                 "survey"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.id.energy.gov/Surveys/",
+            "language": [
+                "en-US"
             ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2022-08-30T12:48:33.230Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Idaho Operations Office",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Idaho Operations Office"
+                }
+            },
+            "rights": "Access is only available to DOE-ID Feds and Contractors",
+            "spatial": "DOE",
+            "systemOfRecords": "none",
+            "title": "Survey Tool"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Public Affairs Open Data",
-            "description": "Public Affairs is responsible for the open data effort at DOE.",
-            "modified": "2014-10-30",
             "accessLevel": "public",
-            "identifier": "DOE-019-3345623431",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "DOE",
-            "temporal": "2005/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Public Affairs"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "019:60"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Marissa Newhall",
                 "hasEmail": "mailto:marissa.newhall@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "Public Affairs is responsible for the open data effort at DOE.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -824,46 +816,46 @@
                     "title": "DOE Open Data"
                 }
             ],
+            "identifier": "DOE-019-3345623431",
             "keyword": [
                 "energy star",
                 "energy.data.gov",
                 "green button",
                 "open data"
             ],
-            "bureauCode": [
-                "019:60"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2014-10-30",
             "programCode": [
                 "019:053"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Public Affairs"
+            },
+            "spatial": "DOE",
+            "temporal": "2005/2014",
             "theme": [
                 "data"
-            ]
+            ],
+            "title": "Public Affairs Open Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Small and Disadvantaged Business Utilization website",
-            "description": "The mission of the Office of Small and Disadvantaged Business Utilization (OSDBU) is to implement and execute the functions and duties of Section 8 and 15 of the Small Business Act (SBAct).  Section 15 states that a fair proportion of the total purchases and contracts for property and services for the Government are to be placed with small business concerns. \r\n\r\nThe implementation and execution of Section 8 and 15 of the SBAct are demonstrated and measured by the Department\u2019s ability to work towards exceeding statutory prime, sub and socio-economic small business goals, providing education on the management & operations business model, continuous improvement of best practices such as the Mentor-Prot\u00e9g\u00e9 Program, providing information on financial assistance opportunities, providing training to small businesses, participating and conducting outreach events for small businesses, ensuring compliance with Federal Acquisition Regulations and other applicable small business laws and regulations, issuing new small business policies and updating existing small business policies at the Department.",
-            "modified": "2014-10-30",
             "accessLevel": "public",
-            "identifier": "DOE-019-3576439991",
-            "dataQuality": true,
-            "license": "http://opendatacommons.org/licenses/pddl/",
-            "spatial": "DOE",
-            "temporal": "2006/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Small and Disadvantaged Business Utilization"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "019:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Hale",
                 "hasEmail": "mailto:john.hale@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "The mission of the Office of Small and Disadvantaged Business Utilization (OSDBU) is to implement and execute the functions and duties of Section 8 and 15 of the Small Business Act (SBAct).  Section 15 states that a fair proportion of the total purchases and contracts for property and services for the Government are to be placed with small business concerns. \r\n\r\nThe implementation and execution of Section 8 and 15 of the SBAct are demonstrated and measured by the Department\u2019s ability to work towards exceeding statutory prime, sub and socio-economic small business goals, providing education on the management & operations business model, continuous improvement of best practices such as the Mentor-Prot\u00e9g\u00e9 Program, providing information on financial assistance opportunities, providing training to small businesses, participating and conducting outreach events for small businesses, ensuring compliance with Federal Acquisition Regulations and other applicable small business laws and regulations, issuing new small business policies and updating existing small business policies at the Department.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -871,45 +863,45 @@
                     "title": "Small and Disadvantaged Business web"
                 }
             ],
+            "identifier": "DOE-019-3576439991",
             "keyword": [
                 "mentor-protege",
                 "mentor-protege program",
                 "small business services"
             ],
-            "bureauCode": [
-                "019:00"
+            "language": [
+                "en-US"
             ],
+            "license": "http://opendatacommons.org/licenses/pddl/",
+            "modified": "2014-10-30",
             "programCode": [
                 "019:000"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Small and Disadvantaged Business Utilization"
+            },
+            "spatial": "DOE",
+            "temporal": "2006/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Small and Disadvantaged Business Utilization website"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Intelligence and Counterintelligence webpage",
-            "description": "The U.S. Department of Energy\u2019s Office of Intelligence and Counterintelligence is responsible for all intelligence and counterintelligence activities throughout the DOE complex, including nearly thirty intelligence and counterintelligence offices nationwide.\r\n\r\nThe Office protects vital national security information and technologies, representing intellectual property of incalculable value. Our distinctive contribution to national security is the ability to leverage the Energy Department\u2019s unmatched scientific and technological expertise in support of policymakers as well as national security missions in defense, homeland security, cyber security, intelligence, and energy security.",
-            "modified": "2014-11-15",
             "accessLevel": "public",
-            "identifier": "DOE-019-3342378941",
-            "dataQuality": true,
-            "license": "http://opendatacommons.org/licenses/pddl/",
-            "spatial": "DOE",
-            "temporal": "2012/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Intelligence and Counterintelligence"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "019:60"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Charles Durant",
                 "hasEmail": "mailto:charles.durant@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "The U.S. Department of Energy\u2019s Office of Intelligence and Counterintelligence is responsible for all intelligence and counterintelligence activities throughout the DOE complex, including nearly thirty intelligence and counterintelligence offices nationwide.\r\n\r\nThe Office protects vital national security information and technologies, representing intellectual property of incalculable value. Our distinctive contribution to national security is the ability to leverage the Energy Department\u2019s unmatched scientific and technological expertise in support of policymakers as well as national security missions in defense, homeland security, cyber security, intelligence, and energy security.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -917,45 +909,44 @@
                     "title": "IN web"
                 }
             ],
+            "identifier": "DOE-019-3342378941",
             "keyword": [
                 "counter-intelligence",
                 "intelligence"
             ],
-            "bureauCode": [
-                "019:60"
+            "language": [
+                "en-US"
             ],
+            "license": "http://opendatacommons.org/licenses/pddl/",
+            "modified": "2014-11-15",
             "programCode": [
                 "019:000"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Intelligence and Counterintelligence"
+            },
+            "spatial": "DOE",
+            "temporal": "2012/2014",
             "theme": [
                 "corporate management"
-            ]
+            ],
+            "title": "Intelligence and Counterintelligence webpage"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Loan Programs Projects",
-            "description": "The Loan Programs projects have created more than 55,000 jobs.",
-            "modified": "2014-11-15",
             "accessLevel": "public",
-            "identifier": "DOE-019-4499333756",
-            "dataQuality": true,
-            "landingPage": "http://energy.gov/lpo/loan-programs-office",
-            "license": "http://opendatacommons.org/licenses/pddl/",
-            "spatial": "United States",
-            "temporal": "2010/2011",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Loan Programs Office"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "019:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Peter Davidson",
                 "hasEmail": "mailto:peter.davidson@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "The Loan Programs projects have created more than 55,000 jobs.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -963,6 +954,7 @@
                     "title": "Loan Projects"
                 }
             ],
+            "identifier": "DOE-019-4499333756",
             "keyword": [
                 "currently generating energy",
                 "date of agreement",
@@ -973,41 +965,41 @@
                 "status",
                 "technology"
             ],
-            "bureauCode": [
-                "019:00"
+            "landingPage": "http://energy.gov/lpo/loan-programs-office",
+            "language": [
+                "en-US"
             ],
+            "license": "http://opendatacommons.org/licenses/pddl/",
+            "modified": "2014-11-15",
             "programCode": [
                 "019:000"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Loan Programs Office"
+            },
+            "spatial": "United States",
+            "temporal": "2010/2011",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Loan Programs Projects"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Declassification Mission Application Server (DMAS)",
-            "description": "Declassification Mission Application Server (DMAS) is a collection of applications that support the department's classification mission.  Applications include the electronic Document Review System, electronic Publication system, electronic Classification Guidance System, OpenNet, Tracking and Distribution System and the Reference Library System.\r\n\r\n[Applications include the Authorities and Training Tracking System (ATTS) which contains training records for individuals who have attended classification training courses and those individuals who have been granted official authorities such as Authorized Derivative Classifiers and Authorized Derivative De-classifiers , Executive Order Review System (EOReview) which contains information for tracking reviews of classified documents, Guidance Distribution Tracking System (GDTS) contains information used to distribute classification guidance, and Policy Reference Library System (PRL) is a reference library of scanned documents relevent to classification policy.]",
-            "modified": "2014-11-15",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-7658334569",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "rights": "Contains CUI access limited to those with official need to know",
-            "spatial": "DOE",
-            "temporal": "1957/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE"
-            },
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "019:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ray Holmer",
                 "hasEmail": "mailto:raymond.holmer@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "Declassification Mission Application Server (DMAS) is a collection of applications that support the department's classification mission.  Applications include the electronic Document Review System, electronic Publication system, electronic Classification Guidance System, OpenNet, Tracking and Distribution System and the Reference Library System.\r\n\r\n[Applications include the Authorities and Training Tracking System (ATTS) which contains training records for individuals who have attended classification training courses and those individuals who have been granted official authorities such as Authorized Derivative Classifiers and Authorized Derivative De-classifiers , Executive Order Review System (EOReview) which contains information for tracking reviews of classified documents, Guidance Distribution Tracking System (GDTS) contains information used to distribute classification guidance, and Policy Reference Library System (PRL) is a reference library of scanned documents relevent to classification policy.]",
+            "identifier": "DOE-019-7658334569",
             "keyword": [
                 "classification",
                 "declassification",
@@ -1016,44 +1008,46 @@
                 "restricted data",
                 "security"
             ],
-            "bureauCode": [
-                "019:10"
+            "language": [
+                "en-US"
             ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2014-11-15",
             "programCode": [
                 "019:000"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE"
+            },
+            "rights": "Contains CUI access limited to those with official need to know",
+            "spatial": "DOE",
+            "temporal": "1957/2014",
             "theme": [
                 "corporate management"
-            ]
+            ],
+            "title": "Declassification Mission Application Server (DMAS)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EHSS Web Services",
-            "description": "EHSS Web Services (AUWS) provides for the maintenance of content for EHSS information on Energy.Gov, Powerpedia and the EHSS intranet.",
-            "modified": "2022-09-26T17:47:25.986Z",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-5643271114",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "rights": "true",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE"
-            },
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ray Holmer",
                 "hasEmail": "mailto:raymond.holmer@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "EHSS Web Services (AUWS) provides for the maintenance of content for EHSS information on Energy.Gov, Powerpedia and the EHSS intranet.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.energy.gov/ehss/environment-health-safety-security"
                 }
             ],
+            "identifier": "DOE-019-5643271114",
             "keyword": [
                 "classification",
                 "declassification",
@@ -1065,39 +1059,37 @@
                 "security",
                 "training"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2022-09-26T17:47:25.986Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE"
+            },
+            "rights": "true",
             "theme": [
                 "corporate management"
-            ]
+            ],
+            "title": "EHSS Web Services"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "National Training Center",
-            "description": "National Training Center provides for the infrastructure and applications necessary to develop and deliver safety and security training courses across the department.",
-            "modified": "2022-09-26T17:23:34.113Z",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-4376543851",
+            "bureauCode": [
+                "015:11"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Rudy Pino",
+                "hasEmail": "mailto:rpino@ntc.doe.gov"
+            },
             "dataQuality": true,
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "rights": "true",
-            "spatial": "DOE",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE"
-            },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Rudy Pino",
-                "hasEmail": "mailto:rpino@ntc.doe.gov"
-            },
+            "description": "National Training Center provides for the infrastructure and applications necessary to develop and deliver safety and security training courses across the department.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1105,6 +1097,7 @@
                     "title": "NTC"
                 }
             ],
+            "identifier": "DOE-019-4376543851",
             "keyword": [
                 "classification",
                 "declassification",
@@ -1117,40 +1110,38 @@
                 "security",
                 "training"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2022-09-26T17:23:34.113Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE"
+            },
+            "rights": "true",
+            "spatial": "DOE",
             "theme": [
                 "corporate management"
-            ]
+            ],
+            "title": "National Training Center"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EA Web Services (EAWS)",
-            "description": "IEA Web Services (EAWS) provides for the maintenance of content for EA information on Energy.Gov, Powerpedia.",
-            "modified": "2014-10-29",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-4389367251",
-            "dataQuality": true,
-            "landingPage": "http://energy.gov/iea/office-independent-enterprise-assessments",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "rights": "Internal reports server contains CUI access limited to those with need to know except for public access site",
-            "spatial": "DOE",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE"
-            },
+            "bureauCode": [
+                "019:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rudy Pino",
                 "hasEmail": "mailto:rpino@ntc.doe.gov"
             },
+            "dataQuality": true,
+            "description": "IEA Web Services (EAWS) provides for the maintenance of content for EA information on Energy.Gov, Powerpedia.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1158,767 +1149,761 @@
                     "title": "EA Webpage"
                 }
             ],
+            "identifier": "DOE-019-4389367251",
             "keyword": [
                 "enforcement",
                 "nuclear safety",
                 "oversight",
                 "training"
             ],
-            "bureauCode": [
-                "019:00"
+            "landingPage": "http://energy.gov/iea/office-independent-enterprise-assessments",
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2014-10-29",
             "programCode": [
                 "019:000"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE"
+            },
+            "rights": "Internal reports server contains CUI access limited to those with need to know except for public access site",
+            "spatial": "DOE",
             "theme": [
                 "corporate management"
-            ]
+            ],
+            "title": "EA Web Services (EAWS)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Enterprise Data Inventory",
-            "description": "A JSON file of the datasets",
-            "modified": "2015-11-24",
             "accessLevel": "public",
-            "identifier": "DOE-019-1254627400",
-            "dataQuality": true,
-            "describedByType": "text/json",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE"
-            },
+            "bureauCode": [
+                "019:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Brenda Coblentz",
                 "hasEmail": "mailto:brenda.coblentz@hq.doe.gov"
             },
+            "dataQuality": true,
+            "describedByType": "text/json",
+            "description": "A JSON file of the datasets",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/plain",
-                    "format": "JSON",
-                    "title": "Enterprise Data Inventory",
                     "description": "Energy Enterprise Datasets -",
-                    "downloadURL": "https://www.energy.gov/data.json"
+                    "downloadURL": "https://www.energy.gov/data.json",
+                    "format": "JSON",
+                    "mediaType": "text/plain",
+                    "title": "Enterprise Data Inventory"
                 }
             ],
+            "identifier": "DOE-019-1254627400",
             "keyword": [
                 "datasets"
             ],
-            "bureauCode": [
-                "019:00"
-            ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2015-11-24",
             "programCode": [
                 "019:000"
-            ]
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE"
+            },
+            "title": "Enterprise Data Inventory"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "DOE IT Reform Cost Savings/Avoidance",
-            "description": "Per FITARA reporting requirements, this is the Department of Energy\u2019s Realized Cost Savings and Avoidance Decisions.",
-            "modified": "2015-11-24",
             "accessLevel": "public",
-            "identifier": "DOE-019-0334675236",
-            "dataQuality": true,
-            "landingPage": "http://www.energy.gov/digitalstrategy/costsavings.json",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Energy"
-            },
+            "bureauCode": [
+                "019:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Michelle Miles",
                 "hasEmail": "mailto:Michelle.Miles@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "Per FITARA reporting requirements, this is the Department of Energy\u2019s Realized Cost Savings and Avoidance Decisions.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
-                    "format": "json",
-                    "title": "DOE IT Reform Cost Savings/Avoidance",
-                    "description": "Per FITARA reporting requirements, this is the Department of Energy\u2019s Realized Cost Savings and Avoidance Decisions.",
                     "conformsTo": "https://management.cio.gov/schemaexamples/costSavingsAvoidanceSchema.json",
-                    "downloadURL": "https://www.energy.gov/downloads/federal-information-technology-acquisition-reform-act-fitara-data-resources"
+                    "description": "Per FITARA reporting requirements, this is the Department of Energy\u2019s Realized Cost Savings and Avoidance Decisions.",
+                    "downloadURL": "https://www.energy.gov/downloads/federal-information-technology-acquisition-reform-act-fitara-data-resources",
+                    "format": "json",
+                    "mediaType": "application/json",
+                    "title": "DOE IT Reform Cost Savings/Avoidance"
                 }
             ],
+            "identifier": "DOE-019-0334675236",
             "keyword": [
                 "cost avoidance",
                 "cost savings"
             ],
-            "bureauCode": [
-                "019:00"
-            ],
+            "landingPage": "http://www.energy.gov/digitalstrategy/costsavings.json",
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2015-11-24",
             "programCode": [
                 "019:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Locator",
-            "description": "Holds information such as name, title, phone number, email address and location of employees at Department of Energy (DOE)",
-            "modified": "2016-05-04",
-            "accessLevel": "non-public",
-            "identifier": "DOE-019-NP-10001",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "rights": "The publishing of the data asset cannot be done due to one or more of the following reasons: contains personal identifying information, contains federal tax information, contains sensitive information, or a data assessment has not been completed.",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Energy"
             },
+            "title": "DOE IT Reform Cost Savings/Avoidance"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "019:60"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Brenda Coblentz",
                 "hasEmail": "mailto:brenda.coblentz@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "Holds information such as name, title, phone number, email address and location of employees at Department of Energy (DOE)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/json",
-                    "format": "json",
-                    "title": "Locator",
                     "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
-                    "downloadURL": "https://inventory.data.gov/dataset/d3be1ce3-99e5-41d1-8cdf-dd6bc811fd0e/resource/67f8b165-5487-42d2-b888-808233816904/download/locator.json"
+                    "downloadURL": "https://inventory.data.gov/dataset/d3be1ce3-99e5-41d1-8cdf-dd6bc811fd0e/resource/67f8b165-5487-42d2-b888-808233816904/download/locator.json",
+                    "format": "json",
+                    "mediaType": "text/json",
+                    "title": "Locator"
                 }
             ],
+            "identifier": "DOE-019-NP-10001",
             "keyword": [
                 "LOCATOR"
             ],
-            "bureauCode": [
-                "019:60"
-            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2016-05-04",
             "programCode": [
                 "019:060"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Records Archives",
-            "description": "System preserves electronic Records",
-            "modified": "2016-05-04",
-            "accessLevel": "non-public",
-            "identifier": "DOE-019-NP-10002",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Energy"
             },
+            "rights": "The publishing of the data asset cannot be done due to one or more of the following reasons: contains personal identifying information, contains federal tax information, contains sensitive information, or a data assessment has not been completed.",
+            "title": "Locator"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "019:60"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Brenda Coblentz",
                 "hasEmail": "mailto:brenda.coblentz@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "System preserves electronic Records",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/json",
-                    "format": "json",
-                    "title": "Records Archives",
                     "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
-                    "downloadURL": "https://inventory.data.gov/dataset/1f31403d-dcee-403b-b1ab-6c855c79b4c2/resource/24cac18e-0c4c-4be2-875a-740d86a8983b/download/recordsarchives.json"
+                    "downloadURL": "https://inventory.data.gov/dataset/1f31403d-dcee-403b-b1ab-6c855c79b4c2/resource/24cac18e-0c4c-4be2-875a-740d86a8983b/download/recordsarchives.json",
+                    "format": "json",
+                    "mediaType": "text/json",
+                    "title": "Records Archives"
                 }
             ],
+            "identifier": "DOE-019-NP-10002",
             "keyword": [
                 "records"
             ],
-            "bureauCode": [
-                "019:60"
-            ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2016-05-04",
             "programCode": [
                 "019:060"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Personnel",
-            "description": "The Personnel application is used by the Human Resources Staff and records a wide variety of employment and position information on Government employees working for the Department of Energy",
-            "modified": "2016-05-04",
-            "accessLevel": "non-public",
-            "identifier": "DOE-019-NP-10003",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Energy"
             },
+            "title": "Records Archives"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "019:60"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Brenda Coblentz",
                 "hasEmail": "mailto:brenda.coblentz@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "The Personnel application is used by the Human Resources Staff and records a wide variety of employment and position information on Government employees working for the Department of Energy",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/plain",
-                    "format": "json",
-                    "title": "Personnel",
                     "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
-                    "downloadURL": "https://inventory.data.gov/dataset/f3c73eeb-bc2c-4b05-b433-2d222ef974ea/resource/1e5ac120-ac67-4f42-865d-95c4aa078d37/download/personnel.json"
+                    "downloadURL": "https://inventory.data.gov/dataset/f3c73eeb-bc2c-4b05-b433-2d222ef974ea/resource/1e5ac120-ac67-4f42-865d-95c4aa078d37/download/personnel.json",
+                    "format": "json",
+                    "mediaType": "text/plain",
+                    "title": "Personnel"
                 }
             ],
+            "identifier": "DOE-019-NP-10003",
             "keyword": [
                 "Personnel"
             ],
-            "bureauCode": [
-                "019:60"
-            ],
+            "license": "https://project-open-data.cio.gov/unknown-license",
+            "modified": "2016-05-04",
             "programCode": [
                 "019:060"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Agency Parking",
-            "description": "Agency parking application that provides the capability to record and query parking assignments. Access is limited to designated personnel of the Facilities and Logistics",
-            "modified": "2016-05-04",
-            "accessLevel": "non-public",
-            "identifier": "DOE-019-NP-10004",
-            "license": "https://project-open-data.cio.gov/unknown-license",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Energy"
             },
+            "title": "Personnel"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "019:60"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Brenda Coblentz",
                 "hasEmail": "mailto:brenda.coblentz@hq.doe.gov"
             },
+            "description": "Agency parking application that provides the capability to record and query parking assignments. Access is limited to designated personnel of the Facilities and Logistics",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/json",
-                    "format": "json",
-                    "title": "Agency Parking",
                     "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
-                    "downloadURL": "https://inventory.data.gov/dataset/d1b72314-a49f-43fc-b38b-a1e6e35ac7fd/resource/2f311a5d-cd9f-4983-a811-3bd48531c390/download/agencyparking.json"
+                    "downloadURL": "https://inventory.data.gov/dataset/d1b72314-a49f-43fc-b38b-a1e6e35ac7fd/resource/2f311a5d-cd9f-4983-a811-3bd48531c390/download/agencyparking.json",
+                    "format": "json",
+                    "mediaType": "text/json",
+                    "title": "Agency Parking"
                 }
             ],
+            "identifier": "DOE-019-NP-10004",
             "keyword": [
                 "parking"
             ],
-            "bureauCode": [
-                "019:60"
-            ],
+            "license": "https://project-open-data.cio.gov/unknown-license",
+            "modified": "2016-05-04",
             "programCode": [
                 "019:060"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Pay Administration",
-            "description": "Pay Administration is a application that provides the capability to denote final acceptance of various personnel actions.",
-            "modified": "2016-05-04",
-            "accessLevel": "non-public",
-            "identifier": "DOE-019-NP-10005",
-            "license": "https://project-open-data.cio.gov/unknown-license",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Energy"
             },
+            "title": "Agency Parking"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "019:60"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Brenda Coblentz",
                 "hasEmail": "mailto:brenda.coblentz@hq.doe.gov"
             },
+            "description": "Pay Administration is a application that provides the capability to denote final acceptance of various personnel actions.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/json",
-                    "format": "json",
-                    "title": "Pay Administration",
                     "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
-                    "downloadURL": "https://inventory.data.gov/dataset/9364736f-f2ba-4c91-a3bc-05e68dbbff9f/resource/dbec3bef-c8e8-443d-83a6-5fba84f7ca0e/download/payadministration.json"
+                    "downloadURL": "https://inventory.data.gov/dataset/9364736f-f2ba-4c91-a3bc-05e68dbbff9f/resource/dbec3bef-c8e8-443d-83a6-5fba84f7ca0e/download/payadministration.json",
+                    "format": "json",
+                    "mediaType": "text/json",
+                    "title": "Pay Administration"
                 }
             ],
+            "identifier": "DOE-019-NP-10005",
             "keyword": [
                 "Pay"
             ],
-            "bureauCode": [
-                "019:60"
-            ],
+            "license": "https://project-open-data.cio.gov/unknown-license",
+            "modified": "2016-05-04",
             "programCode": [
                 "019:060"
-            ]
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Energy"
+            },
+            "title": "Pay Administration"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Agency IT Policy Archive",
-            "description": "IT Policy Archive",
-            "modified": "2016-08-25",
             "accessLevel": "public",
-            "identifier": "DOE-019-FITARA-0001",
-            "dataQuality": true,
-            "describedByType": "text/html",
-            "issued": "2016-08-25",
-            "landingPage": "http://www.enegy.gov/digitalstrategy",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "Washington D.C.",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "019:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Cuttie Bacon",
                 "hasEmail": "mailto:cuttie.bacon@hq.doe.gov"
             },
+            "dataQuality": true,
+            "describedByType": "text/html",
+            "description": "IT Policy Archive",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://www.energy.gov/digitalstrategy/policyarchive",
                     "format": "html",
-                    "title": "Agency IT Policy Archive",
-                    "downloadURL": "https://www.energy.gov/digitalstrategy/policyarchive"
+                    "mediaType": "text/html",
+                    "title": "Agency IT Policy Archive"
                 }
             ],
+            "identifier": "DOE-019-FITARA-0001",
+            "issued": "2016-08-25",
             "keyword": [
                 "Agency IT Policy Archive",
                 "IT Policy",
                 "Policy"
             ],
-            "bureauCode": [
-                "019:00"
+            "landingPage": "http://www.enegy.gov/digitalstrategy",
+            "language": [
+                "us-EN"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2016-08-25",
             "programCode": [
                 "019:000"
             ],
-            "language": [
-                "us-EN"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE"
+            },
+            "spatial": "Washington D.C.",
+            "title": "Agency IT Policy Archive"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Bureau IT Leadership Directory",
-            "description": "A list of agency employees with the title of \u201cchief information officer\u201d or who performs the duties and responsibilities of a CIO but does not necessarily have the title of \u201cCIO.\u201d",
-            "modified": "2016-08-28",
             "accessLevel": "public",
-            "identifier": "DOE-019-FITARA-0002",
-            "dataQuality": true,
-            "describedByType": "TEXT/JSON",
-            "issued": "2016-08-26",
-            "landingPage": "HTTP://WWW.ENERGY.GOV/DIGITALSTRATEGY",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "Washington, D.C.",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Energy"
-            },
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "019:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Doug Upperman",
                 "hasEmail": "mailto:Doug.Upperman@hq.doe.gov"
             },
+            "dataQuality": true,
+            "describedByType": "TEXT/JSON",
+            "description": "A list of agency employees with the title of \u201cchief information officer\u201d or who performs the duties and responsibilities of a CIO but does not necessarily have the title of \u201cCIO.\u201d",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.energy.gov/digitalstrategy/bureaudirectory.json",
+                    "description": "Listing of DOE employees with the title of CIO.",
                     "format": "json",
-                    "title": "Bureau IT Leadership Directory JSON",
-                    "description": "Listing of DOE employees with the title of CIO."
+                    "title": "Bureau IT Leadership Directory JSON"
                 }
             ],
+            "identifier": "DOE-019-FITARA-0002",
+            "issued": "2016-08-26",
             "keyword": [
                 "CIO",
                 "Chief Information Officer",
                 "FITARA"
             ],
-            "bureauCode": [
-                "019:00"
+            "landingPage": "HTTP://WWW.ENERGY.GOV/DIGITALSTRATEGY",
+            "language": [
+                "us-EN"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2016-08-28",
             "programCode": [
                 "019:000"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Energy"
+            },
+            "spatial": "Washington, D.C.",
             "theme": [
                 "FITARA"
-            ]
+            ],
+            "title": "Bureau IT Leadership Directory"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "CIO Governance Board Membership List",
-            "description": "A listing of all governance boards the DOE CIO is a member of. Agencies shall keep this list up to date at least annually beginning in April 2016.",
-            "modified": "2016-08-28",
             "accessLevel": "public",
-            "identifier": "DOE-019-FITARA-0003",
-            "dataQuality": true,
-            "describedByType": "TEXT/JSON",
-            "issued": "2016-08-28",
-            "landingPage": "HTTP://www.energy.gov/digitalstrategy",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "Washington, D.C.",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Energy"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "019:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Doug Upperman",
                 "hasEmail": "mailto:Doug.Upperman@hq.doe.gov"
             },
+            "dataQuality": true,
+            "describedByType": "TEXT/JSON",
+            "description": "A listing of all governance boards the DOE CIO is a member of. Agencies shall keep this list up to date at least annually beginning in April 2016.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.energy.gov/digitalstrategy/governanceboards.json",
+                    "description": "A list of governance boards the CIO is a member of.",
                     "format": "json",
-                    "title": "DOE CIO Governance Board Membership List",
-                    "description": "A list of governance boards the CIO is a member of."
+                    "title": "DOE CIO Governance Board Membership List"
                 }
             ],
+            "identifier": "DOE-019-FITARA-0003",
+            "issued": "2016-08-28",
             "keyword": [
                 "CIO",
                 "CIO Governance Board",
                 "Chief Information Officer",
                 "Governance"
             ],
-            "bureauCode": [
-                "019:00"
+            "landingPage": "HTTP://www.energy.gov/digitalstrategy",
+            "language": [
+                "us-EN"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2016-08-28",
             "programCode": [
                 "019:000"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Energy"
+            },
+            "spatial": "Washington, D.C.",
             "theme": [
                 "FITARA"
-            ]
+            ],
+            "title": "CIO Governance Board Membership List"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "DOE FITARA Milestones",
-            "description": "A listing of FITARA Milestone in JSON format.",
-            "modified": "2022-08-23T18:41:53.375Z",
             "accessLevel": "public",
-            "identifier": "DOE-019-FITARA-0004",
-            "dataQuality": true,
-            "describedByType": "text/json",
-            "landingPage": "http://www.energy.gov/digitalstrategy",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "rights": "true",
-            "spatial": "Washington, D.C.",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Energy"
-            },
             "accrualPeriodicity": "R/P3M",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jeffrey Williams",
                 "hasEmail": "mailto:jeffrey.williams@hq.doe.gov"
             },
+            "dataQuality": true,
+            "describedByType": "text/json",
+            "description": "A listing of FITARA Milestone in JSON format.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.energy.gov/digitalstrategy/fitaramilestones.json",
+                    "description": "Listing of Agency FITARA Milestones",
                     "format": "json",
-                    "title": "DOE Agency FITARA Milestone",
-                    "description": "Listing of Agency FITARA Milestones"
+                    "title": "DOE Agency FITARA Milestone"
                 }
             ],
+            "identifier": "DOE-019-FITARA-0004",
             "keyword": [
                 "FITARA",
                 "FITARA Milestones",
                 "MILESTONES"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "http://www.energy.gov/digitalstrategy",
+            "language": [
+                "us-EN"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2022-08-23T18:41:53.375Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "us-EN"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Energy"
+            },
+            "rights": "true",
+            "spatial": "Washington, D.C.",
+            "title": "DOE FITARA Milestones"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "No FEAR Act",
-            "description": "The No FEAR Act requires each Federal agency to post on its public website summary statistical data relating to equal employment opportunity complaints filed against the agency on a quarterly basis during each fiscal year, and cumulative fiscal year end data for the five preceding years.",
-            "modified": "2016-12-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-563857741",
-            "dataQuality": true,
-            "issued": "2015-01-01",
-            "landingPage": "http://energy.gov/diversity/services/protecting-civil-rights/no-fear-act",
-            "license": "https://creativecommons.org",
-            "spatial": "Department of Energy",
-            "temporal": "2008-10-01/2014-09-30",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of Economic Impact and Diversity"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "019:60"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Civil Rights",
                 "hasEmail": "mailto:civilrights@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "The No FEAR Act requires each Federal agency to post on its public website summary statistical data relating to equal employment opportunity complaints filed against the agency on a quarterly basis during each fiscal year, and cumulative fiscal year end data for the five preceding years.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://www.energy.gov/diversity/no-fear-act-data",
                     "format": "HTML",
-                    "title": "Equal Employment Opportunity Data Posted",
-                    "downloadURL": "https://www.energy.gov/diversity/no-fear-act-data"
+                    "mediaType": "text/html",
+                    "title": "Equal Employment Opportunity Data Posted"
                 }
             ],
+            "identifier": "DOE-019-563857741",
+            "issued": "2015-01-01",
             "keyword": [
                 "comparative",
                 "complaint"
             ],
-            "bureauCode": [
-                "019:60"
+            "landingPage": "http://energy.gov/diversity/services/protecting-civil-rights/no-fear-act",
+            "language": [
+                "us-EN"
             ],
+            "license": "https://creativecommons.org",
+            "modified": "2016-12-01",
             "programCode": [
                 "019:000"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of Economic Impact and Diversity"
+            },
+            "spatial": "Department of Energy",
+            "temporal": "2008-10-01/2014-09-30",
             "theme": [
                 "administrative"
-            ]
+            ],
+            "title": "No FEAR Act"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "U.S. Department of Energy Budget",
-            "description": "This webpage provides links to the current and past U.S. Department of Energy budgets.",
-            "modified": "2018-10-10",
             "accessLevel": "public",
-            "identifier": "DOE-019-675342399",
-            "dataQuality": true,
-            "describedByType": "text/csv",
-            "issued": "2005-01-01",
-            "landingPage": "https://www.energy.gov/budget-performance",
-            "license": "https://creativecommons.org",
-            "spatial": "DOE",
-            "temporal": "2005-01-01/2019-01-01",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Headquarters"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "019:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DOE Budget Office",
                 "hasEmail": "mailto:The.Secretary@hq.doe.gov"
             },
+            "dataQuality": true,
+            "describedByType": "text/csv",
+            "description": "This webpage provides links to the current and past U.S. Department of Energy budgets.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.energy.gov/budget-performance",
+                    "description": "Current and past budgets",
                     "format": "text",
-                    "title": "U.S. Department of Energy Budget",
-                    "description": "Current and past budgets"
+                    "title": "U.S. Department of Energy Budget"
                 }
             ],
+            "identifier": "DOE-019-675342399",
+            "issued": "2005-01-01",
             "keyword": [
                 "budget"
             ],
-            "bureauCode": [
-                "019:00"
+            "landingPage": "https://www.energy.gov/budget-performance",
+            "language": [
+                "us-EN"
             ],
+            "license": "https://creativecommons.org",
+            "modified": "2018-10-10",
             "programCode": [
                 "019:000"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Headquarters"
+            },
+            "spatial": "DOE",
+            "temporal": "2005-01-01/2019-01-01",
             "theme": [
                 "Administrative"
-            ]
+            ],
+            "title": "U.S. Department of Energy Budget"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "U.S. Department of Energy Budget Justifications",
-            "description": "This webpage contains current and past U.S. Department of Energy budget justifications.  The link will go to the 2019 budget.  Justifications for other years can be obtained by clicking on Budget and then selecting the justification link for the desired budget year.",
-            "modified": "2018-10-10",
             "accessLevel": "public",
-            "identifier": "DOE-019-777888665",
-            "dataQuality": true,
-            "describedByType": "text/csv",
-            "issued": "2005-01-01",
-            "landingPage": "https://www.energy.gov/cfo/downloads/fy-2019-budget-justification",
-            "license": "https://creativecommons.org",
-            "spatial": "Department of Energy",
-            "temporal": "2005-01-01/2019-01-01",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Headquarters"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "019:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Budget Office",
                 "hasEmail": "mailto:The.Secretary@hq.doe.gov"
             },
+            "dataQuality": true,
+            "describedByType": "text/csv",
+            "description": "This webpage contains current and past U.S. Department of Energy budget justifications.  The link will go to the 2019 budget.  Justifications for other years can be obtained by clicking on Budget and then selecting the justification link for the desired budget year.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.energy.gov/cfo/listings/agency-financial-reports",
+                    "description": "Current and past budget justifications.  The link will go to the current and past budgets.  Justifications for other years can be obtained by clicking on Budget and then selecting the justification link for the desired budget year.",
                     "format": "csv",
-                    "title": "U.S. Department of Energy Budget Justifications",
-                    "description": "Current and past budget justifications.  The link will go to the current and past budgets.  Justifications for other years can be obtained by clicking on Budget and then selecting the justification link for the desired budget year."
+                    "title": "U.S. Department of Energy Budget Justifications"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.energy.gov/cfo/listings/budget-justification-supporting-documents",
+                    "description": "This is a direct link to several years of budget justifications.",
                     "format": "csv",
-                    "title": "U.S. Department of Energy Budget Justifications",
-                    "description": "This is a direct link to several years of budget justifications."
+                    "title": "U.S. Department of Energy Budget Justifications"
                 }
             ],
+            "identifier": "DOE-019-777888665",
+            "issued": "2005-01-01",
             "keyword": [
                 "budget"
             ],
-            "bureauCode": [
-                "019:00"
+            "landingPage": "https://www.energy.gov/cfo/downloads/fy-2019-budget-justification",
+            "language": [
+                "us-EN"
             ],
+            "license": "https://creativecommons.org",
+            "modified": "2018-10-10",
             "programCode": [
                 "019:000"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Headquarters"
+            },
+            "spatial": "Department of Energy",
+            "temporal": "2005-01-01/2019-01-01",
             "theme": [
                 "Administrative"
-            ]
+            ],
+            "title": "U.S. Department of Energy Budget Justifications"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "U.S. Department of Energy Performance Reports",
-            "description": "This webpage contains U.S. Department of Energy performance reports for current and past years.",
-            "modified": "2018-10-10",
             "accessLevel": "public",
-            "identifier": "DOE-019-665486555",
-            "dataQuality": true,
-            "issued": "2005-01-01",
-            "landingPage": "https://www.energy.gov/budget-performance",
-            "license": "https://creativecommons.org",
-            "spatial": "U.S. Department of Energy",
-            "temporal": "2005-01-01/2019-01-01",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Headquarters"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "019:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Budget Office",
                 "hasEmail": "mailto:The.Secretary@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "This webpage contains U.S. Department of Energy performance reports for current and past years.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.energy.gov/budget-performance",
+                    "description": "This webpage contains current and past budget performance information.",
                     "format": "csv",
-                    "title": "U.S. Department of Energy Budget Performance",
-                    "description": "This webpage contains current and past budget performance information."
+                    "title": "U.S. Department of Energy Budget Performance"
                 }
             ],
+            "identifier": "DOE-019-665486555",
+            "issued": "2005-01-01",
             "keyword": [
                 "performance"
             ],
-            "bureauCode": [
-                "019:00"
+            "landingPage": "https://www.energy.gov/budget-performance",
+            "language": [
+                "us-EN"
             ],
+            "license": "https://creativecommons.org",
+            "modified": "2018-10-10",
             "programCode": [
                 "019:000"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Headquarters"
+            },
+            "spatial": "U.S. Department of Energy",
+            "temporal": "2005-01-01/2019-01-01",
             "theme": [
                 "Administrative"
-            ]
+            ],
+            "title": "U.S. Department of Energy Performance Reports"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "DATA Act for U.S. Department of Energy",
-            "description": "This is a link where the U.S. Department of Energy DATA Act reporting can be found.",
-            "modified": "2018-10-10",
             "accessLevel": "public",
-            "identifier": "DOE-019-100675435",
-            "dataQuality": true,
-            "landingPage": "https://www.USAspending.gov",
-            "license": "https://creativecommons.org",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Headquarters"
-            },
+            "bureauCode": [
+                "019:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Budget Office",
                 "hasEmail": "mailto:The.Secretary@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "This is a link where the U.S. Department of Energy DATA Act reporting can be found.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.USAspending.gov/#",
+                    "description": "This is a link to the U.S. Department of Energy DATA Act Information",
                     "format": "csv",
-                    "title": "U.S. Department of Energy DATA Act Information",
-                    "description": "This is a link to the U.S. Department of Energy DATA Act Information"
+                    "title": "U.S. Department of Energy DATA Act Information"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.usaspending.gov/agency/department-of-energy?fy=2022",
+                    "description": "This link should go to the data for the U.S. Department of Energy",
                     "format": "csv",
-                    "title": "U.S. Department of Energy DATA Act Information",
-                    "description": "This link should go to the data for the U.S. Department of Energy"
+                    "title": "U.S. Department of Energy DATA Act Information"
                 }
             ],
+            "identifier": "DOE-019-100675435",
             "keyword": [
                 "energy"
             ],
-            "bureauCode": [
-                "019:00"
-            ],
+            "landingPage": "https://www.USAspending.gov",
+            "license": "https://creativecommons.org",
+            "modified": "2018-10-10",
             "programCode": [
                 "019:000"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Headquarters"
+            },
             "theme": [
                 "Administrative"
-            ]
+            ],
+            "title": "DATA Act for U.S. Department of Energy"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Federal Comprehensive Annual Performance Data Department of Energy",
-            "description": "This webpage contains sources of  (1) Data tables of federal agency energy and water consumption; (2) Interactive graphics associated with most data tables; (3) Energy costs by end-use sector and efficiency investment information; (4) Progress toward key goals outlined in the National Energy Conservation Policy Act, as amended (42 U.S.C. 8253-8258); Energy Policy Act of 2005 (42 U.S.C. 15852); (5) Historical data tables of agency energy use and costs by facility and mobility sectors by energy type are also available for fiscal year (FY) 1975 through FY 2020",
-            "modified": "2022-01-19T15:07:17.536Z",
             "accessLevel": "public",
-            "identifier": "DOE-019856321",
-            "dataQuality": true,
-            "issued": "1975-01-01",
-            "landingPage": "https://www.energy.gov/eere/femp/federal-comprehensive-annual-energy-performance-data",
-            "license": "https://project-open-data-cio.gov/unknown-license/#v1-legacy",
-            "rights": "true",
-            "spatial": "Department of Energy",
-            "temporal": "1975-01-01/2020-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of Energy Efficiency and Renewable Energy",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Department of Energy"
-                }
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Chris Tremper",
                 "hasEmail": "mailto:chris.tremper@ee.doe.gov"
             },
+            "dataQuality": true,
+            "description": "This webpage contains sources of  (1) Data tables of federal agency energy and water consumption; (2) Interactive graphics associated with most data tables; (3) Energy costs by end-use sector and efficiency investment information; (4) Progress toward key goals outlined in the National Energy Conservation Policy Act, as amended (42 U.S.C. 8253-8258); Energy Policy Act of 2005 (42 U.S.C. 15852); (5) Historical data tables of agency energy use and costs by facility and mobility sectors by energy type are also available for fiscal year (FY) 1975 through FY 2020",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1926,6 +1911,8 @@
                     "title": "Federal Comprehensive Annual Energy Performance Data"
                 }
             ],
+            "identifier": "DOE-019856321",
+            "issued": "1975-01-01",
             "keyword": [
                 "FEMP",
                 "climate",
@@ -1934,29 +1921,15 @@
                 "energy type",
                 "performance"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.energy.gov/eere/femp/federal-comprehensive-annual-energy-performance-data",
+            "language": [
+                "en-US"
             ],
+            "license": "https://project-open-data-cio.gov/unknown-license/#v1-legacy",
+            "modified": "2022-01-19T15:07:17.536Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EISA Federal Covered Facility Management and Benchmarking Data Department of Energy",
-            "description": "This data illustrates Federal progress in meeting the requirements outlined in Section 432 of the Energy Independence and Security Act of 2007 (EISA 432) (42 U.S.C. 8253(f)).  The data is accessible through the FEMP EISA 432 Compliance Tracking System, which offers:  (1) Top-tier agency aggregates, representing all reported data subject to the EISA 432 requirements; (2) Facility-level detailed data that excludes information for facilities that have requested exemption from public disclosure for national-security purposes.",
-            "modified": "2022-01-19T15:22:42.290Z",
-            "accessLevel": "public",
-            "identifier": "DOE-019883924",
-            "dataQuality": true,
-            "issued": "2020-01-01",
-            "landingPage": "https://www.energy.gov/eere/femp/eisa-federal-covered-facility-management-and-benchmarking-data",
-            "license": "https://project-open-data-cio.gov/unknown-license/#v1-legacy/",
-            "rights": "true",
-            "spatial": "Government-wide",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Energy Efficiency and Renewable Energy",
@@ -1965,12 +1938,25 @@
                     "name": "Department of Energy"
                 }
             },
+            "rights": "true",
+            "spatial": "Department of Energy",
+            "temporal": "1975-01-01/2020-12-31",
+            "title": "Federal Comprehensive Annual Performance Data Department of Energy"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Chris Tremper",
                 "hasEmail": "mailto:chris.tremper@ee.doe.gov"
             },
+            "dataQuality": true,
+            "description": "This data illustrates Federal progress in meeting the requirements outlined in Section 432 of the Energy Independence and Security Act of 2007 (EISA 432) (42 U.S.C. 8253(f)).  The data is accessible through the FEMP EISA 432 Compliance Tracking System, which offers:  (1) Top-tier agency aggregates, representing all reported data subject to the EISA 432 requirements; (2) Facility-level detailed data that excludes information for facilities that have requested exemption from public disclosure for national-security purposes.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -1978,45 +1964,47 @@
                     "title": "EISA Federal Covered Facility Management and Benchmarking Data"
                 }
             ],
+            "identifier": "DOE-019883924",
+            "issued": "2020-01-01",
             "keyword": [
                 "FEMP",
                 "facilities"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.energy.gov/eere/femp/eisa-federal-covered-facility-management-and-benchmarking-data",
+            "language": [
+                "en-US"
             ],
+            "license": "https://project-open-data-cio.gov/unknown-license/#v1-legacy/",
+            "modified": "2022-01-19T15:22:42.290Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Artic Energy Webpage",
-            "description": "The Arctic Energy Office (AEO) serves as the principal advisor to the Under Secretary on all domestic Arctic issues, including energy, science, and national security. AEO has primary responsibility for coordinating efforts across the Department of Energy\u2019s (DOE) Program Offices and National Laboratories to ensure a unified voice on all Arctic issues.",
-            "modified": "2022-09-26T17:33:45.879Z",
-            "accessLevel": "public",
-            "identifier": "DOE-019-678459789",
-            "dataQuality": true,
-            "issued": "2022-09-26",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Artic Energy Office",
+                "name": "Office of Energy Efficiency and Renewable Energy",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Department of Energy"
                 }
             },
+            "rights": "true",
+            "spatial": "Government-wide",
+            "title": "EISA Federal Covered Facility Management and Benchmarking Data Department of Energy"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "George Roe",
                 "hasEmail": "mailto:george.roe@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "The Arctic Energy Office (AEO) serves as the principal advisor to the Under Secretary on all domestic Arctic issues, including energy, science, and national security. AEO has primary responsibility for coordinating efforts across the Department of Energy\u2019s (DOE) Program Offices and National Laboratories to ensure a unified voice on all Arctic issues.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2024,44 +2012,44 @@
                     "title": "AEO"
                 }
             ],
+            "identifier": "DOE-019-678459789",
+            "issued": "2022-09-26",
             "keyword": [
                 "artic energy"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-09-26T17:33:45.879Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Artificial Intelligence and Technology",
-            "description": "Coordinate responsible and trustworthy artificial intelligence (AI) governance and capabilities.  AITO is the connective tissue for all things AI at the Department of Energy.",
-            "modified": "2022-09-26T17:53:39.311Z",
-            "accessLevel": "public",
-            "identifier": "DOE-019-0005554321",
-            "dataQuality": true,
-            "issued": "2022-09-26",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Artificial Intelligence and Technology",
+                "name": "Artic Energy Office",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Department of Energy"
                 }
             },
+            "rights": "true",
+            "title": "Artic Energy Webpage"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jonnie Bradley",
                 "hasEmail": "mailto:jonnie.bradley@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "Coordinate responsible and trustworthy artificial intelligence (AI) governance and capabilities.  AITO is the connective tissue for all things AI at the Department of Energy.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2069,44 +2057,44 @@
                     "title": "AITO Webpage"
                 }
             ],
+            "identifier": "DOE-019-0005554321",
+            "issued": "2022-09-26",
             "keyword": [
                 "artificial intelligence"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-09-26T17:53:39.311Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Clean Energy Demonstrations",
-            "description": "The Office of Clean Energy Demonstrations (OCED) was established in December 2021 as part of the Bipartisan Infrastructure Law to accelerate clean energy technologies from the lab to market and fill a critical innovation gap on the path to achieving our nation\u2019s climate goals of net zero emissions by 2050.\n\nOCED\u2019s mission is to deliver clean energy demonstration projects at scale in partnership with the private sector to accelerate deployment, market adoption, and the equitable transition to a decarbonized energy system.",
-            "modified": "2022-09-26T18:32:03.717Z",
-            "accessLevel": "public",
-            "identifier": "DOE-019-9994443476",
-            "dataQuality": true,
-            "issued": "2022-09-26",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Clean Energy Demonstrations",
+                "name": "Artificial Intelligence and Technology",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Department of Energy"
                 }
             },
+            "rights": "true",
+            "title": "Artificial Intelligence and Technology"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Cummins",
                 "hasEmail": "mailto:kelly.cummins@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "The Office of Clean Energy Demonstrations (OCED) was established in December 2021 as part of the Bipartisan Infrastructure Law to accelerate clean energy technologies from the lab to market and fill a critical innovation gap on the path to achieving our nation\u2019s climate goals of net zero emissions by 2050.\n\nOCED\u2019s mission is to deliver clean energy demonstration projects at scale in partnership with the private sector to accelerate deployment, market adoption, and the equitable transition to a decarbonized energy system.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2114,44 +2102,44 @@
                     "title": "CED Webpage"
                 }
             ],
+            "identifier": "DOE-019-9994443476",
+            "issued": "2022-09-26",
             "keyword": [
                 "clean energy"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-09-26T18:32:03.717Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Cybersecurity-Energy Security-and Emergency Response",
-            "description": "To enhance the security and resilience of U.S. critical energy infrastructure to all hazards, mitigate the impacts of disruptive events and risk to the sector overall through preparedness and innovation, and respond to and facilitate recovery from energy disruptions in collaboration with other Federal agencies, the private sector, and State, local, tribal, and territory governments.",
-            "modified": "2022-09-26T18:34:01.508Z",
-            "accessLevel": "public",
-            "identifier": "DOE-019-7698435212",
-            "dataQuality": true,
-            "issued": "2022-09-26",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Cybersecurity, Energy Security, and Emergency Response",
+                "name": "Office of Clean Energy Demonstrations",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Department of Energy"
                 }
             },
+            "rights": "true",
+            "title": "Clean Energy Demonstrations"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Marsha Manning",
                 "hasEmail": "mailto:marsha.manning@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "To enhance the security and resilience of U.S. critical energy infrastructure to all hazards, mitigate the impacts of disruptive events and risk to the sector overall through preparedness and innovation, and respond to and facilitate recovery from energy disruptions in collaboration with other Federal agencies, the private sector, and State, local, tribal, and territory governments.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2159,44 +2147,44 @@
                     "title": "CESER Webpage"
                 }
             ],
+            "identifier": "DOE-019-7698435212",
+            "issued": "2022-09-26",
             "keyword": [
                 "security"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-09-26T18:34:01.508Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Grid Deployment Office",
-            "description": "The Grid Deployment Office (GDO) works to provide electricity to everyone, everywhere by maintaining and investing in critical generation facilities to ensure resource adequacy and improving and expanding transmission and distribution systems. Currently, the Office is focused on ensuring the resilience of critical power generation facilities like hydroelectric and nuclear facilities and developing high-capacity electric transmission lines nationwide. GDO\u2019s work within the Transmission, Grid Modernization, and Power Generation Assistance Divisions will leverage unique authorities to drive transmission investment, improve resource adequacy by maintaining and investing in critical generation facilities, improve transmission and distribution system resilience, and provide access to technical assistance and national laboratory expertise, modeling, and analytical capabilities. \n\nAdministering the Building a Better Grid Initiative, GDO works to modernize and upgrade the nation\u2019s power sector, deploying cost-effective, cleaner, reliable, and more resilient electricity delivery technologies to Tribal, urban, and rural communities. With a strong commitment to collaboration, the office brings together community and industry stakeholders to identify national transmission and distribution needs.",
-            "modified": "2022-09-26T18:21:08.882Z",
-            "accessLevel": "public",
-            "identifier": "DOE-019-6667774356",
-            "dataQuality": true,
-            "issued": "2022-09-26",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Grid Deployment Office",
+                "name": "Office of Cybersecurity, Energy Security, and Emergency Response",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Department of Energy"
                 }
             },
+            "rights": "true",
+            "title": "Cybersecurity-Energy Security-and Emergency Response"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Maria Robinson",
                 "hasEmail": "mailto:maria.robinson@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "The Grid Deployment Office (GDO) works to provide electricity to everyone, everywhere by maintaining and investing in critical generation facilities to ensure resource adequacy and improving and expanding transmission and distribution systems. Currently, the Office is focused on ensuring the resilience of critical power generation facilities like hydroelectric and nuclear facilities and developing high-capacity electric transmission lines nationwide. GDO\u2019s work within the Transmission, Grid Modernization, and Power Generation Assistance Divisions will leverage unique authorities to drive transmission investment, improve resource adequacy by maintaining and investing in critical generation facilities, improve transmission and distribution system resilience, and provide access to technical assistance and national laboratory expertise, modeling, and analytical capabilities. \n\nAdministering the Building a Better Grid Initiative, GDO works to modernize and upgrade the nation\u2019s power sector, deploying cost-effective, cleaner, reliable, and more resilient electricity delivery technologies to Tribal, urban, and rural communities. With a strong commitment to collaboration, the office brings together community and industry stakeholders to identify national transmission and distribution needs.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2204,88 +2192,88 @@
                     "title": "GDO Webpage"
                 }
             ],
+            "identifier": "DOE-019-6667774356",
+            "issued": "2022-09-26",
             "keyword": [
                 "grid deployment"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-09-26T18:21:08.882Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Manufacturing and Energy Supply Chain",
-            "description": "The Office of Manufacturing and Energy Supply Chains is responsible for strengthening and securing manufacturing and energy supply chains needed to modernize the nation\u2019s energy infrastructure and support a clean and equitable energy transition.  \n\nThe office is catalyzing the development of an energy sector industrial base through targeted investments that establish and secure domestic clean energy supply chains and manufacturing, and by engaging with private-sector companies, other Federal agencies, and key stakeholders to collect, analyze, respond to, and share data about energy supply chains to inform future decision making and investment. The office manages programs that develop clean domestic manufacturing and workforce capabilities, with an emphasis on opportunities for small and medium enterprises and communities in energy transition.  \n\nThe Office of Manufacturing and Energy Supply Chains coordinates closely with the Office of Clean Energy Demonstrations for the management of major demonstration projects, and across all of DOE\u2019s programs on manufacturing and supply chain issues, including with the Advanced Manufacturing Office in the Office of Energy Efficiency and Renewable Energy.",
-            "modified": "2022-09-26T18:29:05.800Z",
-            "accessLevel": "public",
-            "identifier": "DOE-019-9977557651",
-            "dataQuality": true,
-            "issued": "2022-09-26",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Manufacturing and Energy Supply Chains",
+                "name": "Grid Deployment Office",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Department of Energy"
                 }
             },
+            "rights": "true",
+            "title": "Grid Deployment Office"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David Howell",
                 "hasEmail": "mailto:david.howell@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "The Office of Manufacturing and Energy Supply Chains is responsible for strengthening and securing manufacturing and energy supply chains needed to modernize the nation\u2019s energy infrastructure and support a clean and equitable energy transition.  \n\nThe office is catalyzing the development of an energy sector industrial base through targeted investments that establish and secure domestic clean energy supply chains and manufacturing, and by engaging with private-sector companies, other Federal agencies, and key stakeholders to collect, analyze, respond to, and share data about energy supply chains to inform future decision making and investment. The office manages programs that develop clean domestic manufacturing and workforce capabilities, with an emphasis on opportunities for small and medium enterprises and communities in energy transition.  \n\nThe Office of Manufacturing and Energy Supply Chains coordinates closely with the Office of Clean Energy Demonstrations for the management of major demonstration projects, and across all of DOE\u2019s programs on manufacturing and supply chain issues, including with the Advanced Manufacturing Office in the Office of Energy Efficiency and Renewable Energy.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.energy.gov/mesc/office-manufacturing-and-energy-supply-chains"
                 }
             ],
+            "identifier": "DOE-019-9977557651",
+            "issued": "2022-09-26",
             "keyword": [
                 "energy supply"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-09-26T18:29:05.800Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "NEPA Policy and Compliance",
-            "description": "NEPA is our basic national charter for protection of the environment. Signed into law by President Richard Nixon on January 1, 1970, NEPA was established to foster and promote the general welfare, to create and maintain conditions under which man and nature can exist in productive harmony, and fulfill the social, economic, and other requirements of present and future generations of Americans. NEPA establishes policy, sets goals (section 101), and provides means (section 102) for carrying out the policy. Section 102(2) contains \u201caction-forcing\u201d provisions to make sure that federal agencies act according to the letter and spirit of the Act. The President, federal agencies, and the courts share responsibility for enforcing the Act so as to achieve the substantive requirements of section 101.",
-            "modified": "2022-09-26T18:39:01.706Z",
-            "accessLevel": "public",
-            "identifier": "DOE-019-3434565689",
-            "dataQuality": true,
-            "issued": "2022-09-26",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of NEPA Policy and Compliance",
+                "name": "Office of Manufacturing and Energy Supply Chains",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Department of Energy"
                 }
             },
+            "rights": "true",
+            "title": "Manufacturing and Energy Supply Chain"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Brian Costner",
                 "hasEmail": "mailto:brian.costner@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "NEPA is our basic national charter for protection of the environment. Signed into law by President Richard Nixon on January 1, 1970, NEPA was established to foster and promote the general welfare, to create and maintain conditions under which man and nature can exist in productive harmony, and fulfill the social, economic, and other requirements of present and future generations of Americans. NEPA establishes policy, sets goals (section 101), and provides means (section 102) for carrying out the policy. Section 102(2) contains \u201caction-forcing\u201d provisions to make sure that federal agencies act according to the letter and spirit of the Act. The President, federal agencies, and the courts share responsibility for enforcing the Act so as to achieve the substantive requirements of section 101.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2293,44 +2281,44 @@
                     "title": "NEPA Webpage"
                 }
             ],
+            "identifier": "DOE-019-3434565689",
+            "issued": "2022-09-26",
             "keyword": [
                 "nepa"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-09-26T18:39:01.706Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Policy",
-            "description": "The Office of Policy supports the Secretary of Energy, Deputy Secretary, Under Secretaries, and the entire Department of Energy, providing analysis on domestic energy policy and related integration of energy systems. Its work spans technology policy, deployment and infrastructure, state, local, tribal, and territorial policy, and energy jobs. It provides expertise in electricity systems, buildings and industry, mobility, energy security, and all parts of the transition to a clean energy economy for all. Working in coordination with the White House, Capitol Hill, other federal agencies, and local stakeholders, the Office of Policy aims to facilitate the transition to a zero-emissions, equitable, and secure energy economy.",
-            "modified": "2022-09-26T18:45:06.893Z",
-            "accessLevel": "public",
-            "identifier": "DOE-019-6745348900",
-            "dataQuality": true,
-            "issued": "2022-09-26",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Policy",
+                "name": "Office of NEPA Policy and Compliance",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Department of Energy"
                 }
             },
+            "rights": "true",
+            "title": "NEPA Policy and Compliance"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jim Fores",
                 "hasEmail": "mailto:jim.fores@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "The Office of Policy supports the Secretary of Energy, Deputy Secretary, Under Secretaries, and the entire Department of Energy, providing analysis on domestic energy policy and related integration of energy systems. Its work spans technology policy, deployment and infrastructure, state, local, tribal, and territorial policy, and energy jobs. It provides expertise in electricity systems, buildings and industry, mobility, energy security, and all parts of the transition to a clean energy economy for all. Working in coordination with the White House, Capitol Hill, other federal agencies, and local stakeholders, the Office of Policy aims to facilitate the transition to a zero-emissions, equitable, and secure energy economy.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2338,44 +2326,44 @@
                     "title": "OP Webpage"
                 }
             ],
+            "identifier": "DOE-019-6745348900",
+            "issued": "2022-09-26",
             "keyword": [
                 "policy"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-09-26T18:45:06.893Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Project Management",
-            "description": "the Department of Energy\u2019s Enterprise Project Management Organization (EPMO), providing leadership and assistance in developing and implementing DOE-wide policies, procedures, programs, and management systems pertaining to project management, and independently monitors, assesses, and reports on project execution performance. The office validates project performance baselines\u2013scope, cost and schedule\u2013of the Department\u2019s largest construction and environmental clean-up projects prior to budget request to Congress\u2014an active project portfolio totaling over $30 billion. The office also serves as Executive Secretariat for the Department\u2019s Energy Systems Acquisition Advisory Board (ESAAB) and the Project Management Risk Committee (PMRC). In these capacities, the Director is accountable to the Deputy Secretary.",
-            "modified": "2022-09-26T18:53:02.252Z",
-            "accessLevel": "public",
-            "identifier": "DOE-019-7755645755",
-            "dataQuality": true,
-            "issued": "2022-09-26",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Project Management",
+                "name": "Office of Policy",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Department of Energy"
                 }
             },
+            "rights": "true",
+            "title": "Policy"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Garrett Richardson",
                 "hasEmail": "mailto:garrett.richardson@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "the Department of Energy\u2019s Enterprise Project Management Organization (EPMO), providing leadership and assistance in developing and implementing DOE-wide policies, procedures, programs, and management systems pertaining to project management, and independently monitors, assesses, and reports on project execution performance. The office validates project performance baselines\u2013scope, cost and schedule\u2013of the Department\u2019s largest construction and environmental clean-up projects prior to budget request to Congress\u2014an active project portfolio totaling over $30 billion. The office also serves as Executive Secretariat for the Department\u2019s Energy Systems Acquisition Advisory Board (ESAAB) and the Project Management Risk Committee (PMRC). In these capacities, the Director is accountable to the Deputy Secretary.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2383,44 +2371,44 @@
                     "title": "PM Webpage"
                 }
             ],
+            "identifier": "DOE-019-7755645755",
+            "issued": "2022-09-26",
             "keyword": [
                 "project management"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-09-26T18:53:02.252Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "State and Community Energy Progralms",
-            "description": "The Office of State and Community Energy Programs was established in January 2022 and is responsible for managing a portfolio of nearly $6 billion in funding from the Bipartisan Infrastructure Law and annual appropriations. \n\nThe Office of State and Community Energy Programs works with state and local organizations to significantly accelerate the deployment of clean energy technologies, catalyze local economic development and create jobs, reduce energy costs, and avoid pollution through place-based strategies involving a wide range of government, community, business and other stakeholders.  \n\nFoundational programs like the Weatherization Assistance Program and State Energy Program, which both have more than 40 years of successfully delivering energy savings across the country, will complement newly formed programs such as the Local Government Energy Program and Energy Futures Grants, enabling DOE to work for the first time ever, with local governments and communities for the long term.  \n\nThrough the disbursement of formula grants, DOE will extend the core capabilities of state energy offices and expand the weatherization provider network to assist low-income families with home energy retrofits. Competitive awards will further the innovation by states and local governments seeking to implement high-impact and self-sustaining clean energy projects. In addition, technical assistance will help to facilitate clean energy programs and practices through \"best practice\" tools, \u201clead-by-example\u201d methods, peer-to-peer forums, and other strategic partnerships.",
-            "modified": "2022-09-26T19:06:07.316Z",
-            "accessLevel": "public",
-            "identifier": "DOE-019-5432543211",
-            "dataQuality": true,
-            "issued": "2022-09-26",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of State and Community Energy Programs",
+                "name": "Office of Project Management",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Department of Energy"
                 }
             },
+            "rights": "true",
+            "title": "Project Management"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Henry McKoy",
                 "hasEmail": "mailto:henry.mckoy@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "The Office of State and Community Energy Programs was established in January 2022 and is responsible for managing a portfolio of nearly $6 billion in funding from the Bipartisan Infrastructure Law and annual appropriations. \n\nThe Office of State and Community Energy Programs works with state and local organizations to significantly accelerate the deployment of clean energy technologies, catalyze local economic development and create jobs, reduce energy costs, and avoid pollution through place-based strategies involving a wide range of government, community, business and other stakeholders.  \n\nFoundational programs like the Weatherization Assistance Program and State Energy Program, which both have more than 40 years of successfully delivering energy savings across the country, will complement newly formed programs such as the Local Government Energy Program and Energy Futures Grants, enabling DOE to work for the first time ever, with local governments and communities for the long term.  \n\nThrough the disbursement of formula grants, DOE will extend the core capabilities of state energy offices and expand the weatherization provider network to assist low-income families with home energy retrofits. Competitive awards will further the innovation by states and local governments seeking to implement high-impact and self-sustaining clean energy projects. In addition, technical assistance will help to facilitate clean energy programs and practices through \"best practice\" tools, \u201clead-by-example\u201d methods, peer-to-peer forums, and other strategic partnerships.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2428,45 +2416,45 @@
                     "title": "SCEP Webpage"
                 }
             ],
+            "identifier": "DOE-019-5432543211",
+            "issued": "2022-09-26",
             "keyword": [
                 "community",
                 "state"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-09-26T19:06:07.316Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Technology Transitions",
-            "description": "The Office of Technology Transitions (OTT) serves as the central hub for the technology transfer activities across the Department of Energy\u2019s extensive R&D enterprise. At OTT, we work to ensure groundbreaking scientific discoveries achieve their maximum public return and impact, advancing the economic, energy, and national security interests of the United States. Getting that done means streamlining access to our user facilities at our 17 National Labs and sites, our world-class scientific researchers, and our sprawling portfolio of intellectual property \u2013 fostering strong internal and external partnerships that guide innovations from the lab toward the marketplace.\n\nTechnology transfer is a complex and dynamic process, and OTT is here to help you connect with DOE-powered innovation to advance discoveries and commercialize transformative, impactful technologies.",
-            "modified": "2022-09-26T19:23:11.648Z",
-            "accessLevel": "public",
-            "identifier": "DOE-019-6547658899",
-            "dataQuality": true,
-            "issued": "2022-09-26",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "rights": "true",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Technology Transitions",
+                "name": "Office of State and Community Energy Programs",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Department of Energy"
                 }
             },
+            "rights": "true",
+            "title": "State and Community Energy Progralms"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Robert Bectel",
                 "hasEmail": "mailto:robert.bectel@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "The Office of Technology Transitions (OTT) serves as the central hub for the technology transfer activities across the Department of Energy\u2019s extensive R&D enterprise. At OTT, we work to ensure groundbreaking scientific discoveries achieve their maximum public return and impact, advancing the economic, energy, and national security interests of the United States. Getting that done means streamlining access to our user facilities at our 17 National Labs and sites, our world-class scientific researchers, and our sprawling portfolio of intellectual property \u2013 fostering strong internal and external partnerships that guide innovations from the lab toward the marketplace.\n\nTechnology transfer is a complex and dynamic process, and OTT is here to help you connect with DOE-powered innovation to advance discoveries and commercialize transformative, impactful technologies.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2474,68 +2462,72 @@
                     "title": "TT Webpage"
                 }
             ],
+            "identifier": "DOE-019-6547658899",
+            "issued": "2022-09-26",
             "keyword": [
                 "technology transitions"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-09-26T19:23:11.648Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of Technology Transitions",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Department of Energy"
+                }
+            },
+            "rights": "true",
+            "title": "Technology Transitions"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "DOE Legacy Management Sites",
-            "description": "Each point is a representation of an U.S. Department of Energy Office of Legacy Management (LM) site. The coordinates of each site point are either the location of a site monument, the centroid of the site boundary, or a general location of the site. This dataset is automatic synchronized with the LM environmental database on a weekly basis. The location and attributes of each site are maintained within the LM environmental database.",
-            "modified": "2024-01-11T13:53:57.703Z",
             "accessLevel": "public",
-            "identifier": "DOE-LM-0000001",
-            "dataQuality": true,
-            "landingPage": "https://gems.lm.doe.gov/arcgis/rest/services/GEMS_EXT/",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "rights": "true",
-            "spatial": "-165.765589,18.213480,179.179778,68.106924",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Energy Office of Legacy Management, Technical Data Manager"
-            },
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Technical Data Manager",
                 "hasEmail": "mailto:gis@lm.doe.gov"
             },
+            "dataQuality": true,
+            "description": "Each point is a representation of an U.S. Department of Energy Office of Legacy Management (LM) site. The coordinates of each site point are either the location of a site monument, the centroid of the site boundary, or a general location of the site. This dataset is automatic synchronized with the LM environmental database on a weekly basis. The location and attributes of each site are maintained within the LM environmental database.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://gems.lm.doe.gov/arcgis/rest/services/GEMS_EXT/LMSites_GWh/MapServer",
+                    "description": "REST API to allow querying of LM data",
                     "format": "API",
-                    "title": "REST API",
-                    "description": "REST API to allow querying of LM data"
+                    "title": "REST API"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://gems.lm.doe.gov",
+                    "description": "Graphical interface for viewing LM spatial data",
                     "format": "HTML",
-                    "title": "Website",
-                    "description": "Graphical interface for viewing LM spatial data"
+                    "title": "Website"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
-                    "format": "json",
-                    "title": "download json",
                     "description": "Legacy Management Sites information in json format",
-                    "downloadURL": "https://gems.lm.doe.gov/arcgis/rest/services/GEMS_EXT/LMSites_GWh/MapServer/0/query?where=1=1&outFields=*&returnGeometry=true&f=pjson"
+                    "downloadURL": "https://gems.lm.doe.gov/arcgis/rest/services/GEMS_EXT/LMSites_GWh/MapServer/0/query?where=1=1&outFields=*&returnGeometry=true&f=pjson",
+                    "format": "json",
+                    "mediaType": "application/json",
+                    "title": "download json"
                 },
                 {
                     "@type": "dcat:Distribution"
                 }
             ],
+            "identifier": "DOE-LM-0000001",
             "keyword": [
                 "Blue Book",
                 "CERCLA",
@@ -2584,41 +2576,40 @@
                 "USACE",
                 "Uranium Mill Tailings Radiation Control Act"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://gems.lm.doe.gov/arcgis/rest/services/GEMS_EXT/",
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2024-01-11T13:53:57.703Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Energy Office of Legacy Management, Technical Data Manager"
+            },
+            "rights": "true",
+            "spatial": "-165.765589,18.213480,179.179778,68.106924",
             "theme": [
                 "geospatial"
-            ]
+            ],
+            "title": "DOE Legacy Management Sites"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Legacy Management Geospatial Environmental Mapping System",
-            "description": "Geospatial Environmental Mapping System (GEMS) provides geospatial layers and access to dynamic mapping and environmental monitoring data for LM sites.  Analytical chemistry data, groundwater depths and elevations, well logs, well construction data, georeferenced boundaries, sampling locations and photo's are available via GEMS.",
-            "modified": "2024-01-11T13:51:52.738Z",
             "accessLevel": "public",
-            "identifier": "DOE-019-6657386541",
-            "dataQuality": true,
-            "landingPage": "https://gems.lm.doe.gov",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "rights": "true",
-            "spatial": "CONUS plus Alaska and Puerto Rico",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Office of Legacy Management"
-            },
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "LM Technical Data Manager",
                 "hasEmail": "mailto:gis@lm.doe.gov"
             },
+            "dataQuality": true,
+            "description": "Geospatial Environmental Mapping System (GEMS) provides geospatial layers and access to dynamic mapping and environmental monitoring data for LM sites.  Analytical chemistry data, groundwater depths and elevations, well logs, well construction data, georeferenced boundaries, sampling locations and photo's are available via GEMS.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2626,6 +2617,7 @@
                     "title": "GEMS"
                 }
             ],
+            "identifier": "DOE-019-6657386541",
             "keyword": [
                 "GEMS",
                 "GIS",
@@ -2634,69 +2626,65 @@
                 "maps",
                 "usg-artificial-intelligence"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://gems.lm.doe.gov",
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2024-01-11T13:51:52.738Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Office of Legacy Management"
+            },
+            "rights": "true",
+            "spatial": "CONUS plus Alaska and Puerto Rico",
             "theme": [
                 "geospatial"
-            ]
+            ],
+            "title": "Legacy Management Geospatial Environmental Mapping System"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "DOE Legacy Management Sample Locations",
-            "description": "Each feature within this dataset is the authoritative representation of the location of a sample within the U.S. Department of Energy (DOE) Office of Legacy Management (LM) Environmental Database. The dataset includes sample locations from Puerto Rico to Alaska, with point features representing different types of sample locations such as boreholes, wells, geoprobes, etc. All sample locations are maintained within the LM Environmental Database, with feature attributes defined within the associated data dictionary.",
-            "modified": "2023-04-04T20:32:10.770Z",
             "accessLevel": "public",
-            "identifier": "LM-DOE-SampleLocations",
-            "dataQuality": true,
-            "describedByType": "application/json",
-            "landingPage": "https://gems.lm.doe.gov/#",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "rights": "true",
-            "spatial": "DOE nationwide",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of Legacy Management",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of Legacy Management"
-                }
-            },
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Technical Data Manager",
                 "hasEmail": "mailto:gis@lm.doe.gov"
             },
+            "dataQuality": true,
+            "describedByType": "application/json",
+            "description": "Each feature within this dataset is the authoritative representation of the location of a sample within the U.S. Department of Energy (DOE) Office of Legacy Management (LM) Environmental Database. The dataset includes sample locations from Puerto Rico to Alaska, with point features representing different types of sample locations such as boreholes, wells, geoprobes, etc. All sample locations are maintained within the LM Environmental Database, with feature attributes defined within the associated data dictionary.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://gems.lm.doe.gov/arcgis/rest/services/GEMS_EXT/SampleLocations_GWh/MapServer",
-                    "title": "Sample Locations",
-                    "description": "Each feature within this dataset is the authoritative representation of the location of a sample within the U.S. Department of Energy (DOE) Office of Legacy Management (LM) Environmental Database. The dataset includes sample locations from Puerto Rico to Alaska, with point features representing different types of sample locations such as boreholes, wells, geoprobes, etc. All sample locations are maintained within the LM Environmental Database, with feature attributes defined within the associated data dictionary."
+                    "description": "Each feature within this dataset is the authoritative representation of the location of a sample within the U.S. Department of Energy (DOE) Office of Legacy Management (LM) Environmental Database. The dataset includes sample locations from Puerto Rico to Alaska, with point features representing different types of sample locations such as boreholes, wells, geoprobes, etc. All sample locations are maintained within the LM Environmental Database, with feature attributes defined within the associated data dictionary.",
+                    "title": "Sample Locations"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/xml",
-                    "format": "FGDC CSDGM Metadata",
-                    "title": "Sample Locations metadata",
                     "description": "FGDC metadata compliant with the CSDGM standard.",
-                    "downloadURL": "https://inventory.data.gov/dataset/9e1b35fd-4df6-4285-8e63-5647d623bc14/resource/951cb629-fc6e-4ca0-aeba-41b716a893e4/download/samplelocations.xml"
+                    "downloadURL": "https://inventory.data.gov/dataset/9e1b35fd-4df6-4285-8e63-5647d623bc14/resource/951cb629-fc6e-4ca0-aeba-41b716a893e4/download/samplelocations.xml",
+                    "format": "FGDC CSDGM Metadata",
+                    "mediaType": "application/xml",
+                    "title": "Sample Locations metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://gems.lm.doe.gov/arcgis/rest/services/GEMS_EXT/SampleLocations_GWh/MapServer",
+                    "description": "REST API for querying LM data",
                     "format": "API",
-                    "title": "REST API",
-                    "description": "REST API for querying LM data"
+                    "title": "REST API"
                 }
             ],
+            "identifier": "LM-DOE-SampleLocations",
             "keyword": [
                 "Blue Book",
                 "CERCLA",
@@ -2745,40 +2733,44 @@
                 "USACE",
                 "Uranium Mill Tailings Radiation Control Act"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://gems.lm.doe.gov/#",
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2023-04-04T20:32:10.770Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of Legacy Management",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of Legacy Management"
+                }
+            },
+            "rights": "true",
+            "spatial": "DOE nationwide",
             "theme": [
                 "geospatial"
-            ]
+            ],
+            "title": "DOE Legacy Management Sample Locations"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Legacy Management Public Website",
-            "description": "To fulfill the Department's post-closure responsibilities and ensure the future protection of human health and the environment. Legacy Management has control and custody for legacy land, structures, and facilities and is responsible for maintaining them at levels consistent with Departmental long-term plans.",
-            "modified": "2024-01-11T13:54:55.532Z",
             "accessLevel": "public",
-            "identifier": "DOE-019-4378945672",
-            "dataQuality": true,
-            "landingPage": "https://www.energy.gov/lm/office-legacy-management",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "rights": "true",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Office of Legacy Management"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Technical Data Manager",
                 "hasEmail": "mailto:gis@lm.doe.gov"
             },
+            "dataQuality": true,
+            "description": "To fulfill the Department's post-closure responsibilities and ensure the future protection of human health and the environment. Legacy Management has control and custody for legacy land, structures, and facilities and is responsible for maintaining them at levels consistent with Departmental long-term plans.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2786,6 +2778,7 @@
                     "title": "Legacy Management web"
                 }
             ],
+            "identifier": "DOE-019-4378945672",
             "keyword": [
                 "LM sites",
                 "applied studies and technology",
@@ -2799,57 +2792,56 @@
                 "programmatic framework",
                 "property"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.energy.gov/lm/office-legacy-management",
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2024-01-11T13:54:55.532Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Office of Legacy Management"
+            },
+            "rights": "true",
+            "title": "Legacy Management Public Website"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "DOE Legacy Management Site Boundaries",
-            "description": "Each feature within this dataset is the authoritative representation of the boundary of each U.S. Department of Energy Office of Legacy Management (LM) site listed as a current in the Site Management Guide (https://www.energy.gov/lm/downloads/site-management-guide). The dataset includes boundaries from Puerto Rico to Alaska and is only applicable to the extents contained within the dataset. All features are maintained as derived boundaries that were created by combining all component extents defined by a legal description for Category 1, 2, and 3 sites or a historic report for Category 1 sites as defined in the Site Management Guide. A general description of the components is included in the feature attributes. The dataset was designed to align with the NGDA Real Property Theme (https://www.fgdc.gov/initiatives/ngda-management-plan).",
-            "modified": "2024-01-11T13:52:59.561Z",
             "accessLevel": "public",
-            "identifier": "DOE-LM-0000005",
-            "dataQuality": true,
-            "describedByType": "application/json",
-            "issued": "2018-05-01",
-            "landingPage": "https://gems.lm.doe.gov/#",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "rights": "true",
-            "spatial": "DOE LM Legacy Sites - boundary polygons",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Energy Office of Legacy Management, Technical Data Manager"
-            },
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Technical Data Manager",
                 "hasEmail": "mailto:gis@lm.doe.gov"
             },
+            "dataQuality": true,
+            "describedByType": "application/json",
+            "description": "Each feature within this dataset is the authoritative representation of the boundary of each U.S. Department of Energy Office of Legacy Management (LM) site listed as a current in the Site Management Guide (https://www.energy.gov/lm/downloads/site-management-guide). The dataset includes boundaries from Puerto Rico to Alaska and is only applicable to the extents contained within the dataset. All features are maintained as derived boundaries that were created by combining all component extents defined by a legal description for Category 1, 2, and 3 sites or a historic report for Category 1 sites as defined in the Site Management Guide. A general description of the components is included in the feature attributes. The dataset was designed to align with the NGDA Real Property Theme (https://www.fgdc.gov/initiatives/ngda-management-plan).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://gems.lm.doe.gov/arcgis/rest/services/GEMS_EXT/SiteBoundaries/MapServer",
+                    "description": "ESRI Map Service",
                     "format": "API",
-                    "title": "Site Boundaries",
-                    "description": "ESRI Map Service"
+                    "title": "Site Boundaries"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/xml",
-                    "format": "xml",
-                    "title": "Site Boundaries Metadata",
                     "description": "FGDC CSDGM metadata",
-                    "downloadURL": "https://inventory.data.gov/dataset/4827456c-b2eb-41e2-b0b4-2f9f8f167ebe/resource/54851bf4-d87b-4825-890b-725e26262df5/download/siteboundariesmetadata.xml"
+                    "downloadURL": "https://inventory.data.gov/dataset/4827456c-b2eb-41e2-b0b4-2f9f8f167ebe/resource/54851bf4-d87b-4825-890b-725e26262df5/download/siteboundariesmetadata.xml",
+                    "format": "xml",
+                    "mediaType": "application/xml",
+                    "title": "Site Boundaries Metadata"
                 }
             ],
+            "identifier": "DOE-LM-0000005",
+            "issued": "2018-05-01",
             "keyword": [
                 "CERCLA",
                 "Category 1",
@@ -2897,46 +2889,44 @@
                 "U.S. Army Corps of Engineers",
                 "U.S. Department of Energy",
                 "U.S. Nuclear Regulatory Commission",
-                "UMTRCA",
-                "USACE",
-                "Uranium Mill Tailings Radiation Control Act"
-            ],
-            "bureauCode": [
-                "015:11"
-            ],
-            "programCode": [
-                "015:001"
+                "UMTRCA",
+                "USACE",
+                "Uranium Mill Tailings Radiation Control Act"
             ],
+            "landingPage": "https://gems.lm.doe.gov/#",
             "language": [
                 "us-EN"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2024-01-11T13:52:59.561Z",
+            "programCode": [
+                "015:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Energy Office of Legacy Management, Technical Data Manager"
+            },
+            "rights": "true",
+            "spatial": "DOE LM Legacy Sites - boundary polygons",
             "theme": [
                 "geospatial"
-            ]
+            ],
+            "title": "DOE Legacy Management Site Boundaries"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Legacy Management Remote Sites Telemetry Data",
-            "description": "System Operation and Analysis at Remote Sites (SOARS) used by LM scientists, regulators and stakeholders; providing real-time data for evaluating progress of groundwater remediation at distant project sites.  Data collected from flow meters, water level meters, pressure sensors, unsaturated zone water-flux meters, moisture sensors, water quality instruments and meterological instruments.",
-            "modified": "2023-04-04T20:30:50.297Z",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-6674567845",
-            "dataQuality": true,
-            "landingPage": "https://soars.lm.doe.gov/",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "rights": "Scientists, Regulators and Stakeholders are provided user accounts to access SOARS.",
-            "spatial": "DOE",
-            "temporal": "2006/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Office of Legacy Management"
-            },
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "LM Technical Data Manager",
                 "hasEmail": "mailto:gis@lm.doe.gov"
             },
+            "dataQuality": true,
+            "description": "System Operation and Analysis at Remote Sites (SOARS) used by LM scientists, regulators and stakeholders; providing real-time data for evaluating progress of groundwater remediation at distant project sites.  Data collected from flow meters, water level meters, pressure sensors, unsaturated zone water-flux meters, moisture sensors, water quality instruments and meterological instruments.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -2944,88 +2934,91 @@
                     "title": "SOARS"
                 }
             ],
+            "identifier": "DOE-019-6674567845",
             "keyword": [
                 "SOARS",
                 "groundwater remediation",
                 "sensor data"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://soars.lm.doe.gov/",
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2023-04-04T20:30:50.297Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Yucca Mountain License Support Network (LSN)",
-            "description": "DOE has preserved its Licensing Support Network (LSN) Collection of some 3.6 million documents and over 30 million pages relevant to the Yucca Mountain licensing proceeding.  Prior to Aug. 2011 it was available to the public via the NRC website.",
-            "modified": "2022-10-06T17:20:37.660Z",
-            "accessLevel": "restricted public",
-            "identifier": "DOE-019-494237290",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "rights": "An electronic copy of the collection is preserved at DOE's Office of Legacy Management Business Center (LMBC) in Morgantown, West Virginia. Members of the public seeking access to this data should file a FOIA request with the U.S. Department of Energy.",
-            "spatial": "Yucca Mountain",
-            "temporal": "1990/2010",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DOE Office of Legacy Management"
             },
+            "rights": "Scientists, Regulators and Stakeholders are provided user accounts to access SOARS.",
+            "spatial": "DOE",
+            "temporal": "2006/2014",
+            "title": "Legacy Management Remote Sites Telemetry Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Montgomery",
                 "hasEmail": "mailto:John.Montgomery@lm.doe.gov"
             },
+            "dataQuality": true,
+            "description": "DOE has preserved its Licensing Support Network (LSN) Collection of some 3.6 million documents and over 30 million pages relevant to the Yucca Mountain licensing proceeding.  Prior to Aug. 2011 it was available to the public via the NRC website.",
+            "identifier": "DOE-019-494237290",
             "keyword": [
                 "yucca mountain"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2022-10-06T17:20:37.660Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Office of Legacy Management"
+            },
             "references": [
                 "http://pbadupws.nrc.gov/docs/ML0417/ML041760035.pdf"
-            ]
+            ],
+            "rights": "An electronic copy of the collection is preserved at DOE's Office of Legacy Management Business Center (LMBC) in Morgantown, West Virginia. Members of the public seeking access to this data should file a FOIA request with the U.S. Department of Energy.",
+            "spatial": "Yucca Mountain",
+            "temporal": "1990/2010",
+            "title": "Yucca Mountain License Support Network (LSN)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Lifecycle Assessment/Analysis (LCA)",
-            "description": "Life Cycle Analysis (LCA) is a comprehensive form of analysis that utilizes the principles of Life Cycle Assessment, Life Cycle Cost Analysis, and various other methods to evaluate the environmental, economic, and social attributes of energy systems ranging from the extraction of raw materials from the ground to the use of the energy carrier to perform work (commonly referred to as the \u201clife cycle\u201d of a product). Results are used to inform research at NETL and evaluate energy options from a National perspective.",
-            "modified": "2022-10-24T18:44:11.606Z",
             "accessLevel": "public",
-            "identifier": "DOE-019-000667788",
-            "dataQuality": true,
-            "landingPage": "https://www.netl.doe.gov/lca",
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "rights": "true",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Energy Technology Laboratory"
-            },
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tim Skone",
                 "hasEmail": "mailto:Timothy.Skone@netl.doe.gov"
             },
+            "dataQuality": true,
+            "description": "Life Cycle Analysis (LCA) is a comprehensive form of analysis that utilizes the principles of Life Cycle Assessment, Life Cycle Cost Analysis, and various other methods to evaluate the environmental, economic, and social attributes of energy systems ranging from the extraction of raw materials from the ground to the use of the energy carrier to perform work (commonly referred to as the \u201clife cycle\u201d of a product). Results are used to inform research at NETL and evaluate energy options from a National perspective.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.netl.doe.gov/research/energy-analysis/life-cycle-analysis",
+                    "description": "Energy analysis search tool",
                     "format": "xml",
-                    "title": "Life Cycle Analysis",
-                    "description": "Energy analysis search tool"
+                    "title": "Life Cycle Analysis"
                 }
             ],
+            "identifier": "DOE-019-000667788",
             "keyword": [
                 "analysis",
                 "biomass",
@@ -3044,38 +3037,36 @@
                 "solar",
                 "wind"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.netl.doe.gov/lca",
+            "language": [
+                "en-US"
             ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2022-10-24T18:44:11.606Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Energy Technology Laboratory"
+            },
+            "rights": "true",
+            "title": "Lifecycle Assessment/Analysis (LCA)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Energy Data Exchange",
-            "description": "EDX is the Department of Energy (DOE)/Fossil Energy Carbon Management (FECM) virtual library and data laboratory built to find, connect, curate, use and re-use data to advance fossil energy and environmental R&D. Developed and maintained by the National Energy Technology Laboratory (NETL), EDX supports the entire life cycle of data by offering secure, private collaborative workspaces for ongoing research projects until they mature and become catalogued, curated, and published. EDX adheres to DOE Cyber policies as well as domestic and international standards for data curation and citation. This ensures data products pushed public via EDX are afforded a citation for proper accreditation and complies with journal publication requirements.",
-            "modified": "2022-10-24T18:21:04.361Z",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-6734569023",
-            "dataQuality": true,
-            "landingPage": "https://edx.netl.doe.gov/dataset",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "rights": "Public users may submit searches for public data. Registered users utilize role-based security to contribute public data and if appropriate access (private) workspaces.",
-            "spatial": "DOE/Office of Fossil Energy",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE/Office of Fossil Energy"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "EDX Support",
                 "hasEmail": "mailto:EDXSupport@netl.doe.gov"
             },
+            "dataQuality": true,
+            "description": "EDX is the Department of Energy (DOE)/Fossil Energy Carbon Management (FECM) virtual library and data laboratory built to find, connect, curate, use and re-use data to advance fossil energy and environmental R&D. Developed and maintained by the National Energy Technology Laboratory (NETL), EDX supports the entire life cycle of data by offering secure, private collaborative workspaces for ongoing research projects until they mature and become catalogued, curated, and published. EDX adheres to DOE Cyber policies as well as domestic and international standards for data curation and citation. This ensures data products pushed public via EDX are afforded a citation for proper accreditation and complies with journal publication requirements.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3083,6 +3074,7 @@
                     "title": "NETL EDX"
                 }
             ],
+            "identifier": "DOE-019-6734569023",
             "keyword": [
                 "Alaska",
                 "Appalachian Basin",
@@ -3131,55 +3123,54 @@
                 "water use",
                 "white paper"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://edx.netl.doe.gov/dataset",
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2022-10-24T18:21:04.361Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE/Office of Fossil Energy"
+            },
             "references": [
                 "https://edx.netl.doe.gov/about"
             ],
+            "rights": "Public users may submit searches for public data. Registered users utilize role-based security to contribute public data and if appropriate access (private) workspaces.",
+            "spatial": "DOE/Office of Fossil Energy",
             "theme": [
                 "geospatial"
-            ]
+            ],
+            "title": "Energy Data Exchange"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "NETL's Carbon Capture and Storage Database",
-            "description": "NETL's Carbon Capture and Storage Database includes active, proposed, canceled, and terminated CCS projects worldwide. Information in the database regarding technologies being developed for capture, evaluation of sites for carbon dioxide (CO2) storage, estimation of project costs, and anticipated dates of completion is sourced from publicly available information. The CCUS Database provides the public with information regarding efforts by various industries, public groups, and governments towards development and eventual deployment of CCUS technology. This is an active database that will be updated as information regarding these or new projects are released to the public.",
-            "modified": "2022-10-24T17:27:45.798Z",
             "accessLevel": "public",
-            "identifier": "DOE-019-4664126543",
-            "dataQuality": true,
-            "landingPage": "https://netl.doe.gov/carbon-management/carbon-storage/worldwide-ccs-database",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "rights": "true",
-            "spatial": "Global",
-            "temporal": "2011-01-01/2015-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE/Office of Fossil Energy"
-            },
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NETL Projects",
                 "hasEmail": "mailto:netl.ccsprojectlist@netl.doe.gov"
             },
+            "dataQuality": true,
+            "description": "NETL's Carbon Capture and Storage Database includes active, proposed, canceled, and terminated CCS projects worldwide. Information in the database regarding technologies being developed for capture, evaluation of sites for carbon dioxide (CO2) storage, estimation of project costs, and anticipated dates of completion is sourced from publicly available information. The CCUS Database provides the public with information regarding efforts by various industries, public groups, and governments towards development and eventual deployment of CCUS technology. This is an active database that will be updated as information regarding these or new projects are released to the public.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "zipped KMZ",
-                    "title": "NETL CCS DatabaseCarbon",
                     "description": "Zipped KMZ file. In Google Earth, go to 'File, Open,' and find the downloaded CCS Database file and open. Users can also double-click the CCS Database file to open the layer in Google Earth\u00a9 once the file is saved to your computer.",
-                    "downloadURL": "https://www.netl.doe.gov/File%20Library/Research/Carbon%20Seq/CCSprojects-Version-5-2015.zip"
+                    "downloadURL": "https://www.netl.doe.gov/File%20Library/Research/Carbon%20Seq/CCSprojects-Version-5-2015.zip",
+                    "format": "zipped KMZ",
+                    "mediaType": "application/zip",
+                    "title": "NETL CCS DatabaseCarbon"
                 }
             ],
+            "identifier": "DOE-019-4664126543",
             "keyword": [
                 "CCUS",
                 "Google Earth",
@@ -3188,48 +3179,50 @@
                 "carbon utilization",
                 "projects"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://netl.doe.gov/carbon-management/carbon-storage/worldwide-ccs-database",
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2022-10-24T17:27:45.798Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE/Office of Fossil Energy"
+            },
+            "rights": "true",
+            "spatial": "Global",
+            "temporal": "2011-01-01/2015-12-31",
             "theme": [
                 "geospatial"
-            ]
+            ],
+            "title": "NETL's Carbon Capture and Storage Database"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Fossil Energy and Carbon Management News Feed",
-            "description": "U.S. Department of Energy, Office of Fossil Energy and Carbon Management (FECM) Press Releases and Techlines",
-            "modified": "2022-10-13T18:49:34.440Z",
             "accessLevel": "public",
-            "identifier": "DOE-019-4663235647",
-            "dataQuality": true,
-            "landingPage": "https://www.energy.gov/fecm/listings/fecm-press-releases-and-techlines",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "rights": "true",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE/Office of Fossil Energy"
-            },
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Marc Willis",
                 "hasEmail": "mailto:Marc.Willis@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "U.S. Department of Energy, Office of Fossil Energy and Carbon Management (FECM) Press Releases and Techlines",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://energy.gov/fe/techlines?view=rss",
                     "mediaType": "application/rss+xml",
-                    "title": "FE RSS",
-                    "downloadURL": "https://energy.gov/fe/techlines?view=rss"
+                    "title": "FE RSS"
                 }
             ],
+            "identifier": "DOE-019-4663235647",
             "keyword": [
                 "coal",
                 "fossil energy",
@@ -3239,141 +3232,140 @@
                 "rss",
                 "techline"
             ],
-            "bureauCode": [
-                "015:11"
+            "landingPage": "https://www.energy.gov/fecm/listings/fecm-press-releases-and-techlines",
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2022-10-13T18:49:34.440Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Natural Gas Import & Export Regulation - Authorizations",
-            "description": "Authorizations related to the import and export of natural gas.",
-            "modified": "2016-11-07",
-            "accessLevel": "public",
-            "identifier": "DOE-019-4554416604",
-            "dataQuality": true,
-            "landingPage": "https://energy.gov/fe/downloads/electronic-docket-room-e-docket-room",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "Global",
-            "temporal": "1977/2016",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DOE/Office of Fossil Energy"
             },
+            "rights": "true",
+            "title": "Fossil Energy and Carbon Management News Feed"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Eugene Duah",
                 "hasEmail": "mailto:eugene.duah@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "Authorizations related to the import and export of natural gas.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
-                    "title": "FE Natural Gas Authorizations",
                     "description": "Authorizations related to the import and export of natural gas in the United States.",
-                    "downloadURL": "https://energy.gov/fe/downloads/electronic-docket-room-e-docket-room"
+                    "downloadURL": "https://energy.gov/fe/downloads/electronic-docket-room-e-docket-room",
+                    "mediaType": "text/html",
+                    "title": "FE Natural Gas Authorizations"
                 }
             ],
+            "identifier": "DOE-019-4554416604",
             "keyword": [
                 "natural gas",
                 "natural gas exports",
                 "natural gas imports",
                 "pipeline"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "https://energy.gov/fe/downloads/electronic-docket-room-e-docket-room",
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2016-11-07",
             "programCode": [
                 "019:013"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE/Office of Fossil Energy"
+            },
+            "spatial": "Global",
+            "temporal": "1977/2016",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Natural Gas Import & Export Regulation - Authorizations"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Northeast Home Heating Oil Reserve System",
-            "description": "An on-line anonymous open bidding system used for emergency sales of product from the Northeast Home Heating Oil Reserve.",
-            "modified": "2022-10-13T20:32:15.428Z",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-1125771301",
-            "dataQuality": true,
-            "license": "https://project-open-data.cio.gov/unknown-license/",
-            "rights": "Prospective bidders must register to use the system to practice or to participate in an actual emergency sale.",
-            "spatial": "United States",
-            "temporal": "2000/2016",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE/Office of Fossil Energy"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "015:11"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Eugene Duah",
                 "hasEmail": "mailto:eugene.duah@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "An on-line anonymous open bidding system used for emergency sales of product from the Northeast Home Heating Oil Reserve.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://heatingoil.fossil.energy.gov/heatingoil/",
                     "mediaType": "text/html",
-                    "title": "FE Heating Oil",
-                    "downloadURL": "https://heatingoil.fossil.energy.gov/heatingoil/"
+                    "title": "FE Heating Oil"
                 }
             ],
+            "identifier": "DOE-019-1125771301",
             "keyword": [
                 "bidding system",
                 "heating oil",
                 "heating oil reserve",
                 "home heating"
             ],
-            "bureauCode": [
-                "015:11"
+            "language": [
+                "en-US"
             ],
+            "license": "https://project-open-data.cio.gov/unknown-license/",
+            "modified": "2022-10-13T20:32:15.428Z",
             "programCode": [
                 "015:001"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE/Office of Fossil Energy"
+            },
             "references": [
                 "https://energy.gov/fe/northeast-home-heating-oil-reserve-online-bidding-system",
                 "https://heatingoil.fossil.energy.gov/docs/QnAs.pdf",
                 "https://energy.gov/fe/services/petroleum-reserves/heating-oil-reserve"
             ],
+            "rights": "Prospective bidders must register to use the system to practice or to participate in an actual emergency sale.",
+            "spatial": "United States",
+            "temporal": "2000/2016",
             "theme": [
                 "geospatial"
-            ]
+            ],
+            "title": "Northeast Home Heating Oil Reserve System"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Office of the Chief Financial Officer Website",
-            "description": "The mission of the Office of the Chief Financial Officer is to assure the effective management and financial integrity of Department of Energy programs, activities, and resources by developing and implementing and monitoring Department-wide policies and systems in the areas of budget administration, program analysis and evaluation, finance and accounting, internal controls, corporate financial systems, and strategic planning.",
-            "modified": "2019-08-06",
             "accessLevel": "public",
-            "identifier": "DOE-019-6784520391",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "DOE",
-            "temporal": "2005/2020",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Office of Chief Financial Officer"
-            },
             "accrualPeriodicity": "R/PT1S",
+            "bureauCode": [
+                "019:60"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelsey Simmons, Webmaster",
                 "hasEmail": "mailto:kelsey.simmons@hq.doe.gov"
             },
+            "dataQuality": true,
+            "description": "The mission of the Office of the Chief Financial Officer is to assure the effective management and financial integrity of Department of Energy programs, activities, and resources by developing and implementing and monitoring Department-wide policies and systems in the areas of budget administration, program analysis and evaluation, finance and accounting, internal controls, corporate financial systems, and strategic planning.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3381,6 +3373,7 @@
                     "title": "CFO Website"
                 }
             ],
+            "identifier": "DOE-019-6784520391",
             "keyword": [
                 "Agency Financial",
                 "Annual Performance",
@@ -3389,51 +3382,50 @@
                 "Financial Management Handbook",
                 "Reports"
             ],
-            "bureauCode": [
-                "019:60"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2019-08-06",
             "programCode": [
                 "019:053"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Office of Chief Financial Officer"
+            },
+            "spatial": "DOE",
+            "temporal": "2005/2020",
             "theme": [
                 "corporate management"
-            ]
+            ],
+            "title": "Office of the Chief Financial Officer Website"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "HC Website",
-            "description": "The Office of the Chief Human Capital Officer (OCHCO) provides effective leadership on policies, programs, and partnerships related to all aspects of human capital management. We support the Department in achieving its mission by proactively planning, recruiting, developing, and retaining the best workforce possible.",
-            "modified": "2015-04-28",
             "accessLevel": "public",
-            "identifier": "CHCO-000001",
-            "dataQuality": true,
-            "describedByType": "text/html",
-            "landingPage": "http://energy.gov/hc/office-chief-human-capital-officer",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "DOE",
-            "temporal": "2015-01-01/2015-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE Office of Chief Human Capital Officer"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "019:60"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tony Nguyen",
                 "hasEmail": "mailto:tony.nguyen@hq.doe.gov"
             },
+            "dataQuality": true,
+            "describedByType": "text/html",
+            "description": "The Office of the Chief Human Capital Officer (OCHCO) provides effective leadership on policies, programs, and partnerships related to all aspects of human capital management. We support the Department in achieving its mission by proactively planning, recruiting, developing, and retaining the best workforce possible.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://energy.gov/hc/office-chief-human-capital-officer",
                     "format": "html",
-                    "title": "HC Web",
-                    "downloadURL": "https://energy.gov/hc/office-chief-human-capital-officer"
+                    "mediaType": "text/html",
+                    "title": "HC Web"
                 }
             ],
+            "identifier": "CHCO-000001",
             "keyword": [
                 "HQ human resources operations",
                 "benefits",
@@ -3447,83 +3439,83 @@
                 "performance management",
                 "policy and guidance"
             ],
-            "bureauCode": [
-                "019:60"
+            "landingPage": "http://energy.gov/hc/office-chief-human-capital-officer",
+            "language": [
+                "us-EN"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2015-04-28",
             "programCode": [
                 "019:000"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE Office of Chief Human Capital Officer"
+            },
+            "spatial": "DOE",
+            "temporal": "2015-01-01/2015-12-31",
             "theme": [
                 "corporate management"
-            ]
+            ],
+            "title": "HC Website"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "D&D Knowledge Management Information Tool",
-            "description": "To provide single point  access into collective knowledge base of the D&D community for DOE-EM.  System aims to preserve and maintain existing knowledge of D&D workforce and gurantees transfer to future generations.",
-            "modified": "2014-11-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-4534567452",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE/Office of Environmental Management"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "019:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Himanshu Upadhyay",
                 "hasEmail": "mailto:upadhyay@fiu.edu"
             },
+            "dataQuality": true,
+            "description": "To provide single point  access into collective knowledge base of the D&D community for DOE-EM.  System aims to preserve and maintain existing knowledge of D&D workforce and gurantees transfer to future generations.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.dndkm.org",
                     "mediaType": "application/pdf",
-                    "title": "D&D KMI Tool",
-                    "downloadURL": "https://www.dndkm.org"
+                    "title": "D&D KMI Tool"
                 }
             ],
+            "identifier": "DOE-019-4534567452",
             "keyword": [
                 "deactivation and decommissioning"
             ],
-            "bureauCode": [
-                "019:10"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2014-11-01",
             "programCode": [
                 "019:051"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE/Office of Environmental Management"
+            },
             "theme": [
                 "environment"
-            ]
+            ],
+            "title": "D&D Knowledge Management Information Tool"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Environmental Management webpage",
-            "description": "As the largest environmental cleanup program in the world, EM has been charged with the responsibility of cleaning up 107 sites across the country whose area is equal to the combined area of Rhode Island and Delaware. EM has made substantial progress in nearly every area of nuclear waste cleanup and as of September 2012, completed cleanup at 90 of these sites.",
-            "modified": "2014-08-30",
             "accessLevel": "public",
-            "identifier": "DOE-019-3321756490",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "DOE",
-            "temporal": "2013/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE/Office of Environmental Management"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "019:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Michelle Primack",
                 "hasEmail": "mailto:michelle.primack@em.doe.gov"
             },
+            "dataQuality": true,
+            "description": "As the largest environmental cleanup program in the world, EM has been charged with the responsibility of cleaning up 107 sites across the country whose area is equal to the combined area of Rhode Island and Delaware. EM has made substantial progress in nearly every area of nuclear waste cleanup and as of September 2012, completed cleanup at 90 of these sites.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3531,226 +3523,227 @@
                     "title": "EM Web"
                 }
             ],
+            "identifier": "DOE-019-3321756490",
             "keyword": [
                 "active sites",
                 "completed sites",
                 "site facility restoration",
                 "waste management"
             ],
-            "bureauCode": [
-                "019:10"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2014-08-30",
             "programCode": [
                 "019:051"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE/Office of Environmental Management"
+            },
+            "spatial": "DOE",
+            "temporal": "2013/2014",
             "theme": [
                 "environment"
-            ]
+            ],
+            "title": "Environmental Management webpage"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "West Valley Phase 1 Studies",
-            "description": "Information on Decommissioning and Long-Term Stewardship of the West Valley Demonstration Project (WVDP) and Western New York Nuclear Service Center (WNYNSC).",
-            "modified": "2014-10-08",
             "accessLevel": "public",
-            "identifier": "DOE-019-7869564535",
-            "dataQuality": true,
-            "issued": "2012-05-14",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "DOE",
-            "temporal": "1980/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE/Environmental Management Consolidated Business Center"
-            },
+            "bureauCode": [
+                "019:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ward Best",
                 "hasEmail": "mailto:ward.best@emcbc.doe.gov"
             },
+            "dataQuality": true,
+            "description": "Information on Decommissioning and Long-Term Stewardship of the West Valley Demonstration Project (WVDP) and Western New York Nuclear Service Center (WNYNSC).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.westvalleyphaseonestudies.org/",
                     "mediaType": "application/pdf",
-                    "title": "WV Studies",
-                    "downloadURL": "https://www.westvalleyphaseonestudies.org/"
+                    "title": "WV Studies"
                 }
             ],
+            "identifier": "DOE-019-7869564535",
+            "issued": "2012-05-14",
             "keyword": [
                 "NYSERDA",
                 "WNYNSC",
                 "WVDP",
                 "West Valley"
             ],
-            "bureauCode": [
-                "019:10"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2014-10-08",
             "programCode": [
                 "019:051"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE/Environmental Management Consolidated Business Center"
+            },
+            "spatial": "DOE",
+            "temporal": "1980/2014",
             "theme": [
                 "environment"
-            ]
+            ],
+            "title": "West Valley Phase 1 Studies"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EM Groundwater Database",
-            "description": "The EM Groundwater Database provides a centralized location for information relating to groundwater flow, contamination, and remedial approaches across the DOE complex.",
-            "modified": "2014-02-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-4942372905",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "rights": "Need to contact POC",
-            "spatial": "DOE",
-            "temporal": "2001/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE/Office of Environmental Management"
-            },
             "accrualPeriodicity": "R/P2Y",
+            "bureauCode": [
+                "019:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Latrincy Bates",
                 "hasEmail": "mailto:latrincy.bates@em.doe.gov"
             },
+            "dataQuality": true,
+            "description": "The EM Groundwater Database provides a centralized location for information relating to groundwater flow, contamination, and remedial approaches across the DOE complex.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://energy.gov/em/groundwater-database",
                     "mediaType": "application/pdf",
-                    "title": "Groundwater",
-                    "downloadURL": "https://energy.gov/em/groundwater-database"
+                    "title": "Groundwater"
                 }
             ],
+            "identifier": "DOE-019-4942372905",
             "keyword": [
                 "cleanup"
             ],
-            "bureauCode": [
-                "019:10"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2014-02-27",
             "programCode": [
                 "019:051"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE/Office of Environmental Management"
+            },
+            "rights": "Need to contact POC",
+            "spatial": "DOE",
+            "temporal": "2001/2014",
             "theme": [
                 "environment"
-            ]
+            ],
+            "title": "EM Groundwater Database"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Central Internet Database (CID)",
-            "description": "CID provides users with Department of Energy (DOE) waste management, cleanup, and facility information.",
-            "modified": "2009-10-19",
             "accessLevel": "public",
-            "identifier": "DOE-019-4536758911",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "DOE",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE/Office of Environmental Management"
-            },
+            "bureauCode": [
+                "019:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Doug Tonkay",
                 "hasEmail": "mailto:douglas.tonkay@em.doe.gov"
             },
+            "dataQuality": true,
+            "description": "CID provides users with Department of Energy (DOE) waste management, cleanup, and facility information.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://cid.doe.gov/Pages/CIDHome.aspx",
                     "mediaType": "pdf/xls",
-                    "title": "CID",
-                    "downloadURL": "https://cid.doe.gov/Pages/CIDHome.aspx"
+                    "title": "CID"
                 }
             ],
+            "identifier": "DOE-019-4536758911",
             "keyword": [
                 "cleanup"
             ],
-            "bureauCode": [
-                "019:10"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2009-10-19",
             "programCode": [
                 "019:051"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE/Office of Environmental Management"
+            },
+            "spatial": "DOE",
             "theme": [
                 "environment"
-            ]
+            ],
+            "title": "Central Internet Database (CID)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Manifest Information Management System (MIMS)",
-            "description": "NIMS reports information on waste shipments received at commercial low-level radioactive waste disposal facilities.",
-            "modified": "2014-02-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-6789334467",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "DOE",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE/Office of Environmental Management"
-            },
             "accrualPeriodicity": "R/P6M",
+            "bureauCode": [
+                "019:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Doug Tonkay",
                 "hasEmail": "mailto:douglas.tonkay@em.doe.gov"
             },
+            "dataQuality": true,
+            "description": "NIMS reports information on waste shipments received at commercial low-level radioactive waste disposal facilities.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://mims.doe.gov/",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "MIMS",
-                    "downloadURL": "https://mims.doe.gov/"
+                    "title": "MIMS"
                 }
             ],
+            "identifier": "DOE-019-6789334467",
             "keyword": [
                 "waste transportation"
             ],
-            "bureauCode": [
-                "019:10"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2014-02-01",
             "programCode": [
                 "019:051"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE/Office of Environmental Management"
+            },
+            "spatial": "DOE",
             "theme": [
                 "environment"
-            ]
+            ],
+            "title": "Manifest Information Management System (MIMS)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Waste Information Management System (WIMS)",
-            "description": "WIMS provides the ability to easily visualize, understand, and manage the vast volumes, categories, and problems of forecasted waste streams.",
-            "modified": "2014-05-18",
             "accessLevel": "public",
-            "identifier": "DOE-019-4578320069",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "spatial": "DOE",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE/Office of Environmental Management"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "019:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Himanshu Upadhyay",
                 "hasEmail": "mailto:upadhyay@fiu.edu"
             },
+            "dataQuality": true,
+            "description": "WIMS provides the ability to easily visualize, understand, and manage the vast volumes, categories, and problems of forecasted waste streams.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -3758,104 +3751,103 @@
                     "title": "WIMS"
                 }
             ],
+            "identifier": "DOE-019-4578320069",
             "keyword": [
                 "waste management"
             ],
-            "bureauCode": [
-                "019:10"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2014-05-18",
             "programCode": [
                 "019:051"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE/Office of Environmental Management"
+            },
+            "spatial": "DOE",
             "theme": [
                 "environment"
-            ]
+            ],
+            "title": "Waste Information Management System (WIMS)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Administrative Record Publishing Website",
-            "description": "Website that communicates certain Hanford information to the public. Tri-party agreement.",
-            "modified": "2014-10-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-7545783421",
-            "dataQuality": true,
-            "license": "http://pdw.hanford.gov/arpir/",
-            "rights": "Open to anyone externally",
-            "spatial": "DOE",
-            "temporal": "1940/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "DOE/Richland Operations and the Office of River Protection"
-            },
+            "bureauCode": [
+                "019:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Debbi Isom",
                 "hasEmail": "mailto:Debra_A_Debbi_Isom@rl.gov"
             },
+            "dataQuality": true,
+            "description": "Website that communicates certain Hanford information to the public. Tri-party agreement.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
-                    "format": "text, csv,pdf",
-                    "title": "Administrative Record Publishing Website",
                     "description": "Website that communicates certain Hanford information to the public. Tri-party agreement.",
-                    "downloadURL": "https://pdw.hanford.gov/arpir/"
+                    "downloadURL": "https://pdw.hanford.gov/arpir/",
+                    "format": "text, csv,pdf",
+                    "mediaType": "text/html",
+                    "title": "Administrative Record Publishing Website"
                 }
             ],
+            "identifier": "DOE-019-7545783421",
             "keyword": [
                 "Hanford",
                 "cleanup",
                 "environment etc.",
                 "mission"
             ],
-            "bureauCode": [
-                "019:10"
+            "language": [
+                "en-US"
             ],
+            "license": "http://pdw.hanford.gov/arpir/",
+            "modified": "2014-10-01",
             "programCode": [
                 "019:051"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "DOE/Richland Operations and the Office of River Protection"
+            },
+            "rights": "Open to anyone externally",
+            "spatial": "DOE",
+            "temporal": "1940/2014",
             "theme": [
                 "corporate management"
-            ]
+            ],
+            "title": "Administrative Record Publishing Website"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "New England Dashboard",
-            "description": "To increase customer understanding of weather-related energy issues in New England, EIA released an interactive dashboard showing energy market conditions in that region. The dashboard will help analysts and interested participants examine many key aspects of the New England energy market such as fuel diversification, wholesale price volatility, energy delivery dynamics, the effect of weather on operations, the effect of fuel prices on electricity prices, regional and onsite fuel stocks.",
-            "modified": "2020-02-23",
             "accessLevel": "public",
-            "identifier": "DOE-019-540449999",
-            "dataQuality": true,
-            "issued": "2019",
-            "landingPage": "https://www.eia.gov/dashboard/newengland/overview",
-            "rights": "public",
-            "spatial": "New England",
-            "temporal": "2020-01-01/2020-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "To increase customer understanding of weather-related energy issues in New England, EIA released an interactive dashboard showing energy market conditions in that region. The dashboard will help analysts and interested participants examine many key aspects of the New England energy market such as fuel diversification, wholesale price volatility, energy delivery dynamics, the effect of weather on operations, the effect of fuel prices on electricity prices, regional and onsite fuel stocks.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
-                    "title": "New England Dashboard",
                     "description": "To increase customer understanding of weather-related energy issues in New England, EIA released an interactive dashboard showing energy market conditions in that region. The dashboard will help analysts and interested participants examine many key aspects of the New England energy market such as fuel diversification, wholesale price volatility, energy delivery dynamics, the effect of weather on operations, the effect of fuel prices on electricity prices, regional and onsite fuel stocks.",
-                    "downloadURL": "https://www.eia.gov/dashboard/newengland/overview"
+                    "downloadURL": "https://www.eia.gov/dashboard/newengland/overview",
+                    "mediaType": "text/html",
+                    "title": "New England Dashboard"
                 }
             ],
+            "identifier": "DOE-019-540449999",
+            "issued": "2019",
             "keyword": [
                 "commercial electricity price industrial electricity price",
                 "electricity",
@@ -3865,47 +3857,47 @@
                 "weather",
                 "wholesale price"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "https://www.eia.gov/dashboard/newengland/overview",
+            "modified": "2020-02-23",
             "programCode": [
                 "019:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "rights": "public",
+            "spatial": "New England",
+            "temporal": "2020-01-01/2020-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "New England Dashboard"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Liquids pipeline projects database",
-            "description": "EIA launched a new liquids pipeline projects database that tracks more than 200 pipeline projects for crude oil, hydrocarbon gas liquids (HGL), and other petroleum products. The database contains project information such as project type, start date, capacity, mileage, and geographic information for historical (completed since 2010) and future pipeline projects. The information in the database is based on the latest public information from company documents, government filings, and trade press, but it does not reflect any assumptions on the likelihood or timing of project completion. The liquids pipeline projects database complements EIA\u2019s natural gas pipeline projects table.",
-            "modified": "2019-12-02",
             "accessLevel": "public",
-            "identifier": "DOE-019-540449998",
-            "dataQuality": true,
-            "issued": "2019",
-            "landingPage": "https://www.eia.gov/petroleum/data.php#movements",
-            "rights": "public",
-            "spatial": "Petroleum Administration for Defense District",
-            "temporal": "2010-01-01/2021-09-30",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "EIA launched a new liquids pipeline projects database that tracks more than 200 pipeline projects for crude oil, hydrocarbon gas liquids (HGL), and other petroleum products. The database contains project information such as project type, start date, capacity, mileage, and geographic information for historical (completed since 2010) and future pipeline projects. The information in the database is based on the latest public information from company documents, government filings, and trade press, but it does not reflect any assumptions on the likelihood or timing of project completion. The liquids pipeline projects database complements EIA\u2019s natural gas pipeline projects table.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                     "description": "This file contains a list of liquids pipeline projects slated to commence operations in coming years, and completed in past years. \"Liquids\" include crude oil, petroleum products, and hydrocarbon gas liquids. The data are not collected on an EIA survey. This information was compiled from various sources including trade press, pipeline company websites, and government agencies. The amount of capacity additions that come online may be significantly different from that reflected in accompanying data. These data are not a forecast, and represent last-known public information on a project, including the start date. Projects that are announced, but have no start date, capacity, or route information are not included. Projects that are under indefinite legal or regulatory holds are included, but without start dates.",
-                    "downloadURL": "https://www.eia.gov/petroleum/xls/EIA_LiqPipProject.xlsx"
+                    "downloadURL": "https://www.eia.gov/petroleum/xls/EIA_LiqPipProject.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "DOE-019-540449998",
+            "issued": "2019",
             "keyword": [
                 "hgl",
                 "hydrocarbon gas liquids",
@@ -3914,48 +3906,48 @@
                 "pipeline mileage",
                 "pipelines"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "https://www.eia.gov/petroleum/data.php#movements",
+            "modified": "2019-12-02",
             "programCode": [
                 "019:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "rights": "public",
+            "spatial": "Petroleum Administration for Defense District",
+            "temporal": "2010-01-01/2021-09-30",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Liquids pipeline projects database"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2018 Electric Generator Report",
-            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 data. Data contained in a zip file.                                                                                                                                                        The zip file contains generator-specific information such as initial date of commercial operation, prime movers, generating capacity, energy sources, status of existing and proposed generators, proposed changes to existing generators, county and State location (including power plant address), ownership, and FERC qualifying facility status. The file also includes data on the ability to use multiple fuels; specifically, data on co-firing and fuel switching are included.",
-            "modified": "2019-09-03",
             "accessLevel": "public",
-            "identifier": "DOE-019-6358888819",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2018-01-01/2018-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-EIA-AEGR-COLL1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
+            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 data. Data contained in a zip file.                                                                                                                                                        The zip file contains generator-specific information such as initial date of commercial operation, prime movers, generating capacity, energy sources, status of existing and proposed generators, proposed changes to existing generators, county and State location (including power plant address), ownership, and FERC qualifying facility status. The file also includes data on the ability to use multiple fuels; specifically, data on co-firing and fuel switching are included.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia860/xls/eia8602018.zip",
                     "mediaType": "application/zip",
-                    "title": "Annual 2018 Electric Generator Report",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia860/xls/eia8602018.zip"
+                    "title": "Annual 2018 Electric Generator Report"
                 }
             ],
+            "identifier": "DOE-019-6358888819",
+            "isPartOf": "DOE-019-EIA-AEGR-COLL1",
             "keyword": [
                 "EIA-860",
                 "annual data",
@@ -3982,97 +3974,100 @@
                 "winter capability",
                 "winter capacity"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2019-09-03",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_860/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2018-01-01/2018-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 2018 Electric Generator Report"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "State carbon dioxide emissions data",
-            "description": "Annual state-level estimates of energy consumption, prices, and expenditures for jet fuel.",
-            "modified": "2019-10-23",
             "accessLevel": "public",
-            "identifier": "DOE-019-540449997",
-            "dataQuality": true,
-            "issued": "2019",
-            "landingPage": "https://www.eia.gov/environment/emissions/state/",
-            "rights": "public",
-            "spatial": "State",
-            "temporal": "2017-01-01/2017-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Annual state-level estimates of energy consumption, prices, and expenditures for jet fuel.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/environment/emissions/state/",
                     "mediaType": "text/html",
-                    "title": "State carbon dioxide emissions data",
-                    "downloadURL": "https://www.eia.gov/environment/emissions/state/"
+                    "title": "State carbon dioxide emissions data"
                 }
             ],
+            "identifier": "DOE-019-540449997",
+            "issued": "2019",
             "keyword": [
                 "carbon dioxide",
                 "carbon dioxide emissions",
                 "emissions"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "https://www.eia.gov/environment/emissions/state/",
+            "modified": "2019-10-23",
             "programCode": [
                 "019:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "rights": "public",
+            "spatial": "State",
+            "temporal": "2017-01-01/2017-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "State carbon dioxide emissions data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2018 Electric Power Industry Data",
-            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
-            "modified": "2019-10-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-63576357791",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "landingPage": "https://www.eia.gov/electricity/data/eia861/index.php",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-AEPID-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:melinda.hobbs@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f8612018.zip",
                     "mediaType": "application/zip",
-                    "title": "Annual Electric Power Industry Report",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f8612018.zip"
+                    "title": "Annual Electric Power Industry Report"
                 }
             ],
+            "identifier": "DOE-019-63576357791",
+            "isPartOf": "DOE-019-AEPID-Collection1",
             "keyword": [
                 "electric purchases",
                 "electric utility",
@@ -4081,50 +4076,47 @@
                 "electricity sales",
                 "net-metering"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "https://www.eia.gov/electricity/data/eia861/index.php",
+            "modified": "2019-10-01",
             "programCode": [
                 "019:220"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 2018 Electric Power Industry Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 2018",
-            "description": "Monthly 2018 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2019-09-30",
             "accessLevel": "public",
-            "identifier": "DOE-019-3456435495",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2018-01-01/2018-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 2018 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2018/data/impa18d.xlsx",
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "title": "Company Level Imports",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2018/data/impa18d.xlsx"
+                    "title": "Company Level Imports"
                 }
             ],
+            "identifier": "DOE-019-3456435495",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -4136,54 +4128,54 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2019-09-30",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2018-01-01/2018-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports 2018"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Monthly 2018 Utility and Nonutility Fuel Receipts and Fuel Quality Data",
-            "description": "Monthly 2018 data on U.S. electric power generation and fuel consumption, stocks, receipts, quality, costs, fuel supplier, and coal mine source from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant-level.  Based on Form EIA-923 data. Monthly time series extend back to 2001.",
-            "modified": "2019-09-20",
             "accessLevel": "public",
-            "identifier": "DOE-019-5463727498",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2018-01-01/2018-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-MUNF-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
+            "description": "Monthly 2018 data on U.S. electric power generation and fuel consumption, stocks, receipts, quality, costs, fuel supplier, and coal mine source from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant-level.  Based on Form EIA-923 data. Monthly time series extend back to 2001.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/archive/xls/f923_2018.zip",
                     "mediaType": "application/zip",
-                    "title": "Monthly 2018 Utility and Nonutility Fuel Receipts and Fuel Quality Data",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/archive/xls/f923_2018.zip"
+                    "title": "Monthly 2018 Utility and Nonutility Fuel Receipts and Fuel Quality Data"
                 }
             ],
+            "identifier": "DOE-019-5463727498",
+            "isPartOf": "DOE-019-MUNF-COLLECTION1",
             "keyword": [
                 "coal receipts",
                 "electricity generating fuels",
@@ -4192,54 +4184,53 @@
                 "gas receipts",
                 "oil receipts"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2019-09-20",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_923/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2018-01-01/2018-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Monthly 2018 Utility and Nonutility Fuel Receipts and Fuel Quality Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Monthly Electric Utility Sales and Revenue Data 2018",
-            "description": "Utility level retail sales of electricity and associated revenue in 2018. Organized by reporting month, state, and by end-use sector, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 data.",
-            "modified": "2021-05-19T15:46:43.944Z",
             "accessLevel": "public",
-            "identifier": "DOE-019-4567895692",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_826/instructions.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia826/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "rights": "true",
-            "spatial": "United States",
-            "temporal": "2018-01-01/2018-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-MEUSR-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_826/instructions.pdf",
+            "description": "Utility level retail sales of electricity and associated revenue in 2018. Organized by reporting month, state, and by end-use sector, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861m/archive/xls/net_metering2018.xlsx",
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "title": "Monthly Electric Utility Sales and Revenue Data 2018",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861m/archive/xls/net_metering2018.xlsx"
+                    "title": "Monthly Electric Utility Sales and Revenue Data 2018"
                 }
             ],
+            "identifier": "DOE-019-4567895692",
+            "isPartOf": "DOE-019-MEUSR-COLLECTION1",
             "keyword": [
                 "cents per kWh",
                 "commercial electric prices",
@@ -4259,49 +4250,52 @@
                 "state electric prices",
                 "transportation electric prices"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia826/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2021-05-19T15:46:43.944Z",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_826/form.pdf"
             ],
+            "rights": "true",
+            "spatial": "United States",
+            "temporal": "2018-01-01/2018-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Monthly Electric Utility Sales and Revenue Data 2018"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Electric Power Annual",
-            "description": "Annual data on electricity generating capacity, electricity generation and useful thermal output, fuel receipts, fuel stocks, sales, consumption, and emissions in the United States. Based on Form EIA-861 and Form EIA-860 data. Annual time series extend back to 1994.",
-            "modified": "2013-12-12",
             "accessLevel": "public",
-            "identifier": "DOE-019-540445799",
-            "landingPage": "http://www.eia.gov/electricity/annual/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "description": "Annual data on electricity generating capacity, electricity generation and useful thermal output, fuel receipts, fuel stocks, sales, consumption, and emissions in the United States. Based on Form EIA-861 and Form EIA-860 data. Annual time series extend back to 1994.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.eia.gov/electricity/annual/",
+                    "description": "National-level data on electricity generating capacity, electricity generation and useful thermal output, fuel receipts, consumption, and emissions.",
                     "format": "html",
-                    "title": "Electric Power Annual",
-                    "description": "National-level data on electricity generating capacity, electricity generation and useful thermal output, fuel receipts, consumption, and emissions."
+                    "title": "Electric Power Annual"
                 }
             ],
+            "identifier": "DOE-019-540445799",
             "keyword": [
                 "Transmission",
                 "biomass",
@@ -4327,53 +4321,51 @@
                 "trade",
                 "utility cost"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/annual/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2013-12-12",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_860/instructions.pdf",
                 "http://www.eia.gov/survey/form/eia_860/form.pdf",
                 "http://www.eia.gov/survey/form/eia_861/form.pdf",
                 "http://www.eia.gov/survey/form/eia_861/instructions.pdf"
-            ]
+            ],
+            "title": "Electric Power Annual"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Employee Hours 1999",
-            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, and union status. Annual time series extend back to 1983. Based on EIA Form-7A data.",
-            "modified": "2008-09-12",
             "accessLevel": "public",
-            "identifier": "DOE-019-4840639285",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
-            "landingPage": "http://www.eia.gov/coal/data.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "State and County",
-            "temporal": "1999-01-01/1999-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
+            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, and union status. Annual time series extend back to 1983. Based on EIA Form-7A data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic1999.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "1999 Coal Production",
-                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic1999.xls"
+                    "title": "1999 Coal Production"
                 }
             ],
+            "identifier": "DOE-019-4840639285",
+            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
             "keyword": [
                 "coal data",
                 "coal data file",
@@ -4384,83 +4376,83 @@
                 "coal production file",
                 "energy"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/data.cfm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2008-09-12",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_7a/form.pdf"
             ],
+            "spatial": "State and County",
+            "temporal": "1999-01-01/1999-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Employee Hours 1999"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "U.S. Energy Mapping System",
-            "description": "Map data for energy production and consumption in geospatial format.",
-            "modified": "2019-02-27",
             "accessLevel": "public",
-            "identifier": "DOE-019-9999999991",
-            "license": "https://creativecommons.org/licenses/by/4.0",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "description": "Map data for energy production and consumption in geospatial format.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://www.eia.gov/state/maps.php",
                     "format": "csv file",
-                    "title": "U.S. Energy Mapping System",
-                    "downloadURL": "https://www.eia.gov/state/maps.php"
+                    "mediaType": "text/html",
+                    "title": "U.S. Energy Mapping System"
                 }
             ],
+            "identifier": "DOE-019-9999999991",
             "keyword": [
                 "energy",
                 "georeferenced maps",
-                "historical maps",
-                "interactive maps",
-                "maps",
-                "state"
-            ],
-            "bureauCode": [
-                "019:20"
-            ],
-            "programCode": [
-                "019:022"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Natural Gas Data and Statistics",
-            "description": "Data and statistics on natural gas prices, exploration and reserves, production, imports and exports, storage, pipelines, and consumption. Data released on a weekly, monthly and annual basis. International data on natural gas production, consumption, imports and exports, CO2 emissions, and reserves.",
-            "modified": "2019-03-21",
-            "accessLevel": "public",
-            "identifier": "DOE-019-3858899129",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/naturalgas/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+                "historical maps",
+                "interactive maps",
+                "maps",
+                "state"
+            ],
+            "license": "https://creativecommons.org/licenses/by/4.0",
+            "modified": "2019-02-27",
+            "programCode": [
+                "019:022"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Energy Information Administration"
             },
-            "isPartOf": "DOE-019-NGD-COLLECTION1",
+            "title": "U.S. Energy Mapping System"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data and statistics on natural gas prices, exploration and reserves, production, imports and exports, storage, pipelines, and consumption. Data released on a weekly, monthly and annual basis. International data on natural gas production, consumption, imports and exports, CO2 emissions, and reserves.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4479,6 +4471,8 @@
                     "title": "API Web Page"
                 }
             ],
+            "identifier": "DOE-019-3858899129",
+            "isPartOf": "DOE-019-NGD-COLLECTION1",
             "keyword": [
                 "LNG",
                 "base gas",
@@ -4503,51 +4497,49 @@
                 "vented and flared",
                 "working gas"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/naturalgas/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2019-03-21",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Natural Gas Data and Statistics"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Average Number of Employees and Hours 2013",
-            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, union status, labor hours, and employment data. Annual time series extend back to 1983. Based on EIA Form-7A data.",
-            "modified": "2015-01-20",
             "accessLevel": "public",
-            "identifier": "DOE-019-540445801",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
-            "issued": "2015-01-20",
-            "landingPage": "http://www.eia.gov/coal/data.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2013-01-01/2013-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
+            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, union status, labor hours, and employment data. Annual time series extend back to 1983. Based on EIA Form-7A data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic2013.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2013 Coal Production",
-                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic2013.xls"
+                    "title": "2013 Coal Production"
                 }
             ],
+            "identifier": "DOE-019-540445801",
+            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
+            "issued": "2015-01-20",
             "keyword": [
                 "coal-data",
                 "coal-data-file",
@@ -4557,50 +4549,50 @@
                 "coal-production",
                 "coal-production-file"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/data.cfm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-01-20",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_7a/form.pdf",
                 "http://www.eia.gov/survey/form/eia_7a/instructions.pdf"
-            ]
+            ],
+            "spatial": "United States",
+            "temporal": "2013-01-01/2013-12-31",
+            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Average Number of Employees and Hours 2013"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual U. S. Electric Power Industry Estimated Emissions by State From 1990 - Latest Year Available",
-            "description": "Data on annual emissions of Carbon Dioxide (CO2), Sulfur Dioxide (SO2), and Nitrogen Oxides (NOx). Data organized by type of electric power producer, by energy source, and by U.S. state. Annual time series extend back to 1990. Based on Form EIA-861 data.                                 \r\n                                                                                                                                    Electric Power Producer: Commercial Cogen, Commercial Non-Cogen, Electric Utility, Industrial Cogen, Industrial Non-Cogen, IPP NAICS-22 Cogen, IPP NAICS-22 Non-Cogen, and Total Electric Power Industry \r\n\r\nEnergy Source: Coal, Geothermal, Natural Gas, Other, Other Biomass, Other Gases, Wood and Wood Derived Fuels, Petroleum, and All Energy Sources",
-            "modified": "2018-10-22",
             "accessLevel": "public",
-            "identifier": "DOE-019-5285457823",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/electricity/annual/pdf/tech_notes.pdf",
-            "landingPage": "http://www.eia.gov/electricity/annual/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1990/2012",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/electricity/annual/pdf/tech_notes.pdf",
+            "description": "Data on annual emissions of Carbon Dioxide (CO2), Sulfur Dioxide (SO2), and Nitrogen Oxides (NOx). Data organized by type of electric power producer, by energy source, and by U.S. state. Annual time series extend back to 1990. Based on Form EIA-861 data.                                 \r\n                                                                                                                                    Electric Power Producer: Commercial Cogen, Commercial Non-Cogen, Electric Utility, Industrial Cogen, Industrial Non-Cogen, IPP NAICS-22 Cogen, IPP NAICS-22 Non-Cogen, and Total Electric Power Industry \r\n\r\nEnergy Source: Coal, Geothermal, Natural Gas, Other, Other Biomass, Other Gases, Wood and Wood Derived Fuels, Petroleum, and All Energy Sources",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/state/emission_annual.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Electric Power Industry Estimated Emissions (1990 - Latest Year Available)",
-                    "downloadURL": "https://www.eia.gov/electricity/data/state/emission_annual.xls"
+                    "title": "Electric Power Industry Estimated Emissions (1990 - Latest Year Available)"
                 }
             ],
+            "identifier": "DOE-019-5285457823",
             "keyword": [
                 "carbon dioxide emissions",
                 "climate",
@@ -4613,53 +4605,53 @@
                 "so2",
                 "sulfur dioxide emissions"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/annual/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2018-10-22",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/electricity/annual/pdf/tech_notes.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "1990/2012",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual U. S. Electric Power Industry Estimated Emissions by State From 1990 - Latest Year Available"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2004 Electric Power Industry Data",
-            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
-            "modified": "2007-03-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-3976767676",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2004-01-01/2004-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-AEPID-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f86104.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2004 EPI Data EIA-861",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f86104.zip"
+                    "title": "2004 EPI Data EIA-861"
                 }
             ],
+            "identifier": "DOE-019-3976767676",
+            "isPartOf": "DOE-019-AEPID-Collection1",
             "keyword": [
                 "AMI",
                 "AMR",
@@ -4694,54 +4686,54 @@
                 "revenues",
                 "sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2007-03-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2004-01-01/2004-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 2004 Electric Power Industry Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual Solar Photovoltaic Module Shipments Report",
-            "description": "Data on domestic shipments of photovoltaic cells and modules by market sector, end use, and type.  Based on information reported on Form EIA-63B, \u201cAnnual Photovoltaic Cell/Module Shipments Report.\u201d  Shipments as reported by respondents are for terrestrial (land-based) use only. Shipments intended for applications in space programs (satellites, military projects, etc.) are excluded.                                                                                                                                                                                          Market Sector: Residential; Commercial; Industrial; Electric Power End use: Grid-connected Centralized PV System; Grid-connected Distributed PV System; Off-grid Domestic PV System; Off-grid Non-domestic PV System Type: Crystalline Silicon; Thin-Film; Concentrator",
-            "modified": "2018-08-09",
             "accessLevel": "public",
-            "identifier": "DOE-019-5402452378",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_63b/form.pdf",
-            "landingPage": "http://www.eia.gov/renewable/annual/solar_photo/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2012-01-01/2012-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_63b/form.pdf",
+            "description": "Data on domestic shipments of photovoltaic cells and modules by market sector, end use, and type.  Based on information reported on Form EIA-63B, \u201cAnnual Photovoltaic Cell/Module Shipments Report.\u201d  Shipments as reported by respondents are for terrestrial (land-based) use only. Shipments intended for applications in space programs (satellites, military projects, etc.) are excluded.                                                                                                                                                                                          Market Sector: Residential; Commercial; Industrial; Electric Power End use: Grid-connected Centralized PV System; Grid-connected Distributed PV System; Off-grid Domestic PV System; Off-grid Non-domestic PV System Type: Crystalline Silicon; Thin-Film; Concentrator",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "title": "Annual Solar Photovoltaic Module Shipments Report",
                     "description": "This report includes summary data for the photovoltaic industry from annual and monthly respondents. Data include manufacturing, imports, and exports of modules in the United States and its territories. Summary data include volumes in peak kilowatts and average prices. Where possible, imports and exports are listed by country, and shipments to the United States are listed by state.",
-                    "downloadURL": "https://www.eia.gov/renewable/annual/solar_photo/pdf/pv_full.pdf"
+                    "downloadURL": "https://www.eia.gov/renewable/annual/solar_photo/pdf/pv_full.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Annual Solar Photovoltaic Module Shipments Report"
                 }
             ],
+            "identifier": "DOE-019-5402452378",
             "keyword": [
                 "photovoltaic",
                 "renewable capacity",
@@ -4749,45 +4741,43 @@
                 "renewable energy consumption",
                 "solar energy"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/renewable/annual/solar_photo/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2018-08-09",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_63b/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2012-01-01/2012-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual Solar Photovoltaic Module Shipments Report"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data and Statistics",
-            "description": "International and domestic data on coal production, consumption, prices, reserves, stocks, imports, exports, distribution, and transportation rates. Weekly, monthly, and annual data available.",
-            "modified": "2014-10-06",
             "accessLevel": "public",
-            "identifier": "DOE-019-3290918838",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1940/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1W",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "International and domestic data on coal production, consumption, prices, reserves, stocks, imports, exports, distribution, and transportation rates. Weekly, monthly, and annual data available.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4797,9 +4787,9 @@
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://api.eia.gov/category?api_key=YOUR_API_KEY_HERE&category_id=717234",
+                    "description": "API",
                     "format": "API",
-                    "title": "Coal Data API",
-                    "description": "API"
+                    "title": "Coal Data API"
                 },
                 {
                     "@type": "dcat:Distribution",
@@ -4807,6 +4797,8 @@
                     "title": "API Web Page"
                 }
             ],
+            "identifier": "DOE-019-3290918838",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "Demonstrated Reserve Base",
                 "coal consumption",
@@ -4832,47 +4824,47 @@
                 "spot price",
                 "underground mining"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "http://www.eia.gov/coal/",
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2014-10-06",
             "programCode": [
                 "019:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "spatial": "Global",
+            "temporal": "1940/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data and Statistics"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 2012",
-            "description": "Monthly 2012 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2013-09-27",
             "accessLevel": "public",
-            "identifier": "DOE-019-1134456789",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2012-01-01/2012-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 2012 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2012/data/impa12d.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2012 Petroleum Imports",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2012/data/impa12d.xls"
+                    "title": "2012 Petroleum Imports"
                 }
             ],
+            "identifier": "DOE-019-1134456789",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -4884,45 +4876,43 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2013-09-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2012-01-01/2012-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports 2012"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Portal",
-            "description": "Country-level data on all energy sources, i.e., coal, electricity, petroleum, primary energy, biofuels, and natural gas. Data on production, consumption, reserves, prices, stocks, imports, exports, emissions, capacity, generation, and carbon dioxide intensity. The portal gives users the option to visualize data on a bubble map, heat map, column chart, or time-series chart.",
-            "modified": "2018-12-31",
             "accessLevel": "public",
-            "identifier": "DOE-019-0492888273",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/international/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-IEDAD-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Country-level data on all energy sources, i.e., coal, electricity, petroleum, primary energy, biofuels, and natural gas. Data on production, consumption, reserves, prices, stocks, imports, exports, emissions, capacity, generation, and carbon dioxide intensity. The portal gives users the option to visualize data on a bubble map, heat map, column chart, or time-series chart.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4930,6 +4920,8 @@
                     "title": "International Energy Portal"
                 }
             ],
+            "identifier": "DOE-019-0492888273",
+            "isPartOf": "DOE-019-IEDAD-COLLECTION1",
             "keyword": [
                 "annual data",
                 "coal price",
@@ -4953,40 +4945,39 @@
                 "petroleum reserves",
                 "petroleum stocks"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/international/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2018-12-31",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "spatial": "Global",
+            "temporal": "1980/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Portal"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Renewable and Alternative Fuels Data and Statistics",
-            "description": "Monthly and annual data on renewable energy, i.e., biomass, geothermal, hydropower, solar, and wind. Also data on alternative transportation fuels, i.e., hydrogen, natural gas, propane, ethanol, and electricity. Data on renewable energy production, consumption, electricity generation, and consumption by end-use sector.",
-            "modified": "2019-03-26",
             "accessLevel": "public",
-            "identifier": "DOE-019-4509183883",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/renewable/data.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "2013/2040",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Monthly and annual data on renewable energy, i.e., biomass, geothermal, hydropower, solar, and wind. Also data on alternative transportation fuels, i.e., hydrogen, natural gas, propane, ethanol, and electricity. Data on renewable energy production, consumption, electricity generation, and consumption by end-use sector.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -4994,6 +4985,7 @@
                     "title": "Renewable and Alternative Fuels"
                 }
             ],
+            "identifier": "DOE-019-4509183883",
             "keyword": [
                 "alternative transportation fuels",
                 "and alternative fueled vehicles",
@@ -5012,49 +5004,49 @@
                 "wood",
                 "wood waste"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/renewable/data.cfm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2019-03-26",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "spatial": "Global",
+            "temporal": "2013/2040",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Renewable and Alternative Fuels Data and Statistics"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Residential Energy Consumption Survey (RECS) Files, All Data, 2015",
-            "description": "The 2015 study represents the 14th iteration of the RECS program. First conducted in 1978, the Residential Energy Consumption Survey is a national sample survey that collects energy-related data for housing units occupied as a primary residence and the households that live in them. Data were collected from more than 5,600 households selected at random using a complex multistage, area-probability sample design. The sample represents 118.2 million U.S. households. The 1st version of the 2015 RECS microdata file, released in April 2017, reflected preliminary household characteristics data. The file was updated in October 2017 (Version 2) to include additional square footage and household energy insecurity data. The file was updated again in May 2018 (Version 3) and included final household characteristics data, as well as final consumption and expenditures data. The final version of the microdata file was updated in December 2018 (Version 4) and contains wood consumption variables, as well as additional weather and climate-related variables used in the end-use modeling process.",
-            "modified": "2018-05-15",
             "accessLevel": "public",
-            "identifier": "DOE-019-1056347890",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/consumption/residential/data/2005/layoutfiles/RECS05layoutAllData.csv",
-            "landingPage": "https://www.eia.gov/consumption/residential/data/2015/index.php?view=microdata",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1978/2005",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/consumption/residential/data/2005/layoutfiles/RECS05layoutAllData.csv",
+            "description": "The 2015 study represents the 14th iteration of the RECS program. First conducted in 1978, the Residential Energy Consumption Survey is a national sample survey that collects energy-related data for housing units occupied as a primary residence and the households that live in them. Data were collected from more than 5,600 households selected at random using a complex multistage, area-probability sample design. The sample represents 118.2 million U.S. households. The 1st version of the 2015 RECS microdata file, released in April 2017, reflected preliminary household characteristics data. The file was updated in October 2017 (Version 2) to include additional square footage and household energy insecurity data. The file was updated again in May 2018 (Version 3) and included final household characteristics data, as well as final consumption and expenditures data. The final version of the microdata file was updated in December 2018 (Version 4) and contains wood consumption variables, as well as additional weather and climate-related variables used in the end-use modeling process.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/consumption/residential/data/2015/csv/recs2015_public_v4.csv",
                     "mediaType": "text/csv",
-                    "title": "2015 Residential Energy Consumption",
-                    "downloadURL": "https://www.eia.gov/consumption/residential/data/2015/csv/recs2015_public_v4.csv"
+                    "title": "2015 Residential Energy Consumption"
                 }
             ],
+            "identifier": "DOE-019-1056347890",
             "keyword": [
                 "Household use of energy",
                 "RECS data",
@@ -5071,52 +5063,52 @@
                 "national",
                 "statistics"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "https://www.eia.gov/consumption/residential/data/2015/index.php?view=microdata",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2018-05-15",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/consumption/residential/data/2005/index.cfm?view=microdata"
             ],
+            "spatial": "United States",
+            "temporal": "1978/2005",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Residential Energy Consumption Survey (RECS) Files, All Data, 2015"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Residential Energy Consumption Survey (RECS) Files, Energy Consumption, 2009",
-            "description": "This 2009 version represents the 13th iteration of the RECS program. First conducted in 1978, the Residential Energy Consumption Survey is a national sample survey that collects energy-related data for housing units occupied as a primary residence and the households that live in them. Data were collected from 12,083 households selected at random using a complex multistage, area-probability sample design. The sample represents 113.6 million U.S. households, the Census Bureau's statistical estimate for all occupied housing units in 2009 derived from their American Community Survey (ACS).",
-            "modified": "2013-03-15",
             "accessLevel": "public",
-            "identifier": "DOE-019-5945672389",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/consumption/residential/data/2009/xls/recs2009_public_codebook.xlsx",
-            "landingPage": "http://www.eia.gov/consumption/residential/data/2009/index.cfm?view=microdata",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1978/2009",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/consumption/residential/data/2009/xls/recs2009_public_codebook.xlsx",
+            "description": "This 2009 version represents the 13th iteration of the RECS program. First conducted in 1978, the Residential Energy Consumption Survey is a national sample survey that collects energy-related data for housing units occupied as a primary residence and the households that live in them. Data were collected from 12,083 households selected at random using a complex multistage, area-probability sample design. The sample represents 113.6 million U.S. households, the Census Bureau's statistical estimate for all occupied housing units in 2009 derived from their American Community Survey (ACS).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/consumption/residential/data/2009/csv/recs2009_public.csv",
                     "mediaType": "text/csv",
-                    "title": "2009 Energy Consumption Survey",
-                    "downloadURL": "https://www.eia.gov/consumption/residential/data/2009/csv/recs2009_public.csv"
+                    "title": "2009 Energy Consumption Survey"
                 }
             ],
+            "identifier": "DOE-019-5945672389",
             "keyword": [
                 "Household use of energy data",
                 "RECS data",
@@ -5130,50 +5122,49 @@
                 "housing",
                 "national"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/consumption/residential/data/2009/index.cfm?view=microdata",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2013-03-15",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/consumption/residential/data/2009/index.cfm?view=microdata"
             ],
+            "spatial": "United States",
+            "temporal": "1978/2009",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Residential Energy Consumption Survey (RECS) Files, Energy Consumption, 2009"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Short-Term Energy Outlook - Real and Nominal Petroleum Prices",
-            "description": "Provides annual, quarterly, and monthly prices back to 1976 for gasoline , heating oil, and diesel fuel. Also provides annual prices from 1968 and quarterly and monthly prices from 1974 for imported crude oil. Based on Form EIA-878 data.",
-            "modified": "2019-03-12",
             "accessLevel": "public",
-            "identifier": "DOE-019-8613456873",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_878/instructions.pdf",
-            "landingPage": "http://www.eia.gov/forecasts/steo/data.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1968/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_878/instructions.pdf",
+            "description": "Provides annual, quarterly, and monthly prices back to 1976 for gasoline , heating oil, and diesel fuel. Also provides annual prices from 1968 and quarterly and monthly prices from 1974 for imported crude oil. Based on Form EIA-878 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/outlooks/steo/realprices/real_prices.xlsx",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Petroleum Energy Outlook",
-                    "downloadURL": "https://www.eia.gov/outlooks/steo/realprices/real_prices.xlsx"
+                    "title": "Petroleum Energy Outlook"
                 },
                 {
                     "@type": "dcat:Distribution",
@@ -5181,6 +5172,7 @@
                     "title": "Real Prices Viewer"
                 }
             ],
+            "identifier": "DOE-019-8613456873",
             "keyword": [
                 "DOE",
                 "Department of Energy",
@@ -5192,51 +5184,50 @@
                 "real diesel fuel prices",
                 "real gasoline prices"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/forecasts/steo/data.cfm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2019-03-12",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_878/form.pdf",
                 "http://www.eia.gov/survey/form/eia_878/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "1968/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Short-Term Energy Outlook - Real and Nominal Petroleum Prices"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "State Energy Data System (SEDS)",
-            "description": "EIA's State Energy Data System (SEDS) is a comprehensive data set that consists of annual time series estimates of state-level energy use by major economic sectors, energy production and and State-level energy price and expenditure data. The system provides data back from 1960. Data are presented in physical units, BTUs, and dollars. While some SEDS data series come directly from surveys conducted by EIA, many are estimated using other available information. These estimations are necessary for the compilation of \"total energy\" estimates.",
-            "modified": "2018-06-29",
             "accessLevel": "public",
-            "identifier": "DOE-019-1915345678",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/state/seds/CDF/Codes_and_Descriptions.xlsx",
-            "landingPage": "http://www.eia.gov/state/seds/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1960/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/state/seds/CDF/Codes_and_Descriptions.xlsx",
+            "description": "EIA's State Energy Data System (SEDS) is a comprehensive data set that consists of annual time series estimates of state-level energy use by major economic sectors, energy production and and State-level energy price and expenditure data. The system provides data back from 1960. Data are presented in physical units, BTUs, and dollars. While some SEDS data series come directly from surveys conducted by EIA, many are estimated using other available information. These estimations are necessary for the compilation of \"total energy\" estimates.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/state/seds/CDF/Complete_SEDS.csv",
                     "mediaType": "text/csv",
-                    "title": "SEDS",
-                    "downloadURL": "https://www.eia.gov/state/seds/CDF/Complete_SEDS.csv"
+                    "title": "SEDS"
                 },
                 {
                     "@type": "dcat:Distribution",
@@ -5244,6 +5235,7 @@
                     "title": "State Energy Data System (SEDS): Back to 1960 (Complete)"
                 }
             ],
+            "identifier": "DOE-019-1915345678",
             "keyword": [
                 "BTU",
                 "State energy consumption",
@@ -5254,43 +5246,43 @@
                 "State energy production",
                 "physical units"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/state/seds/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2018-06-29",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/state/seds/seds-technical-notes-complete.cfm"
             ],
+            "spatial": "United States",
+            "temporal": "1960/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "State Energy Data System (SEDS)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "State Energy Data System (SEDS) Application Programming Interface (API)",
-            "description": "State-level data on all energy sources. Data include production, consumption, reserves, stocks, prices, imports, and exports. Data are collated from state-specific data reported elsewhere on the EIA website and are the most recent values available. The system provides data back from 1960. While some SEDS data series come directly from surveys conducted by EIA, many are estimated using other available information. These estimations are necessary for the compilation of \"total energy\" estimates.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2014-02-27T18:35:43.965018",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-3988165895",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/state/seds/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "State",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "State-level data on all energy sources. Data include production, consumption, reserves, stocks, prices, imports, and exports. Data are collated from state-specific data reported elsewhere on the EIA website and are the most recent values available. The system provides data back from 1960. While some SEDS data series come directly from surveys conducted by EIA, many are estimated using other available information. These estimations are necessary for the compilation of \"total energy\" estimates.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5304,6 +5296,7 @@
                     "title": "API Web Page"
                 }
             ],
+            "identifier": "DOE-019-3988165895",
             "keyword": [
                 "annual data",
                 "coal price",
@@ -5324,46 +5317,44 @@
                 "petroleum consumption",
                 "petroleum price",
                 "petroleum production",
-                "petroleum reserves",
-                "petroleum stocks"
-            ],
-            "bureauCode": [
-                "019:20"
-            ],
-            "programCode": [
-                "019:022"
+                "petroleum reserves",
+                "petroleum stocks"
             ],
+            "landingPage": "http://www.eia.gov/state/seds/",
             "language": [
                 "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2014-02-27T18:35:43.965018",
+            "programCode": [
+                "019:022"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/state/seds/seds-technical-notes-complete.cfm"
             ],
+            "spatial": "State",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "State Energy Data System (SEDS) Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Total Energy Data and Statistics",
-            "description": "Comprehensive monthly and annual time series on all energy sources. Data on production, consumption, reserves, stocks, prices, imports, and exports. Monthly time series extend back to 1973 and annual time series extend back to 1949. National-level data on major end-use sectors ,i.e., residential, commercial, industrial, and transportation.",
-            "modified": "2019-03-26",
             "accessLevel": "public",
-            "identifier": "DOE-019-1295783927",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/totalenergy/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1949/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Comprehensive monthly and annual time series on all energy sources. Data on production, consumption, reserves, stocks, prices, imports, and exports. Monthly time series extend back to 1973 and annual time series extend back to 1949. National-level data on major end-use sectors ,i.e., residential, commercial, industrial, and transportation.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5376,6 +5367,7 @@
                     "title": "Annual Total Energy Data"
                 }
             ],
+            "identifier": "DOE-019-1295783927",
             "keyword": [
                 "annual data",
                 "coal price",
@@ -5402,50 +5394,50 @@
                 "petroleum stocks",
                 "time series"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/totalenergy/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2019-03-26",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "spatial": "United States",
+            "temporal": "1949/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Total Energy Data and Statistics"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "U.S. Crude Oil, Natural Gas, and Natural Gas Liquids Reserves",
-            "description": "Annual data on proved reserves of crude oil, natural gas, and natural gas liquids in the U.S. Based on EIA Form-23L data.                                                                                                                                                                   Proved reserves are estimated volumes of hydrocarbon resources that analysis of geologic and engineering data demonstrates with reasonable certainty are recoverable under existing economic and operating conditions. Reserves estimates change from year to year as new discoveries are made, existing fields are more thoroughly appraised, existing reserves are produced, and prices and technologies change.",
-            "modified": "2018-11-29",
             "accessLevel": "public",
-            "identifier": "DOE-019-5404456523",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_23l/instructions.pdf",
-            "landingPage": "http://www.eia.gov/naturalgas/crudeoilreserves/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2018-01-01/2018-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_23l/instructions.pdf",
+            "description": "Annual data on proved reserves of crude oil, natural gas, and natural gas liquids in the U.S. Based on EIA Form-23L data.                                                                                                                                                                   Proved reserves are estimated volumes of hydrocarbon resources that analysis of geologic and engineering data demonstrates with reasonable certainty are recoverable under existing economic and operating conditions. Reserves estimates change from year to year as new discoveries are made, existing fields are more thoroughly appraised, existing reserves are produced, and prices and technologies change.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/naturalgas/crudeoilreserves/excel/reserves_tables_2018.xlsx",
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "title": "2018 Reserves",
-                    "downloadURL": "https://www.eia.gov/naturalgas/crudeoilreserves/excel/reserves_tables_2018.xlsx"
+                    "title": "2018 Reserves"
                 }
             ],
+            "identifier": "DOE-019-5404456523",
             "keyword": [
                 "Oil reserves",
                 "crude oil",
@@ -5460,55 +5452,55 @@
                 "oil resources",
                 "oil supply"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/naturalgas/crudeoilreserves/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2018-11-29",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_23l/instructions.pdf",
                 "http://www.eia.gov/survey/form/eia_23l/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2018-01-01/2018-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "U.S. Crude Oil, Natural Gas, and Natural Gas Liquids Reserves"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2009 Electric Generator Report",
-            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 data. Data contained in a zip file. The zip file contains generator-specific information such as initial date of commercial operation, prime movers, generating capacity, energy sources, status of existing and proposed generators, proposed changes to existing generators, county and State location (including power plant address), ownership, and FERC qualifying facility status. The file also includes data on the ability to use multiple fuels; specifically, data on co-firing and fuel switching are included.",
-            "modified": "2010-12-20",
             "accessLevel": "public",
-            "identifier": "DOE-019-4816727272",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2009-01-01/2009-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-EIA-AEGR-COLL1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
+            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 data. Data contained in a zip file. The zip file contains generator-specific information such as initial date of commercial operation, prime movers, generating capacity, energy sources, status of existing and proposed generators, proposed changes to existing generators, county and State location (including power plant address), ownership, and FERC qualifying facility status. The file also includes data on the ability to use multiple fuels; specifically, data on co-firing and fuel switching are included.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia860/xls/eia8602009.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2009 EG Report EIA-860",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia860/xls/eia8602009.zip"
+                    "title": "2009 EG Report EIA-860"
                 }
             ],
+            "identifier": "DOE-019-4816727272",
+            "isPartOf": "DOE-019-EIA-AEGR-COLL1",
             "keyword": [
                 "EIA-860",
                 "annual data",
@@ -5535,53 +5527,53 @@
                 "winter capability",
                 "winter capacity"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2010-12-20",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_860/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2009-01-01/2009-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 2009 Electric Generator Report"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2009 Electric Power Industry Data",
-            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
-            "modified": "2010-12-10",
             "accessLevel": "public",
-            "identifier": "DOE-019-4815666666",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2009-01-01/2009-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-AEPID-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f86109.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2009 EPI Data",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f86109.zip"
+                    "title": "2009 EPI Data"
                 }
             ],
+            "identifier": "DOE-019-4815666666",
+            "isPartOf": "DOE-019-AEPID-Collection1",
             "keyword": [
                 "AMI",
                 "AMR",
@@ -5616,53 +5608,53 @@
                 "revenues",
                 "sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2010-12-10",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2009-01-01/2009-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 2009 Electric Power Industry Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Average Number of Employees and Hours 2008",
-            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, union status, labor hours, and employment data. Annual time series extend back to 1983. Based on EIA Form-7A data.",
-            "modified": "2009-12-07",
             "accessLevel": "public",
-            "identifier": "DOE-019-4832323232",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
-            "landingPage": "http://www.eia.gov/coal/data.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "State and County",
-            "temporal": "2008-01-01/2008-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
+            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, union status, labor hours, and employment data. Annual time series extend back to 1983. Based on EIA Form-7A data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic1990.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2008 Coal Production",
-                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic1990.xls"
+                    "title": "2008 Coal Production"
                 }
             ],
+            "identifier": "DOE-019-4832323232",
+            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
             "keyword": [
                 "coal data",
                 "coal data file",
@@ -5673,44 +5665,43 @@
                 "coal production file",
                 "energy"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/data.cfm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2009-12-07",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_7a/form.pdf"
             ],
+            "spatial": "State and County",
+            "temporal": "2008-01-01/2008-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Average Number of Employees and Hours 2008"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Consumption & Efficiency Data and Statistics",
-            "description": "Data and statistics on energy consumption in homes, commercial buildings, manufacturing, and transportation.  Data released monthly or annually.",
-            "modified": "2014-10-06",
             "accessLevel": "public",
-            "identifier": "DOE-019-6992338902",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/consumption/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1991/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data and statistics on energy consumption in homes, commercial buildings, manufacturing, and transportation.  Data released monthly or annually.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5718,6 +5709,7 @@
                     "title": "Consumption Data"
                 }
             ],
+            "identifier": "DOE-019-6992338902",
             "keyword": [
                 "buildings",
                 "commercial",
@@ -5735,49 +5727,50 @@
                 "residential",
                 "transportation energy"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/consumption/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2014-10-06",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "spatial": "United States",
+            "temporal": "1991/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Consumption & Efficiency Data and Statistics"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Energy Analysis & Projections",
-            "description": "Monthly and yearly forecasts of energy production, consumption, and price at the national level and by energy type.  Monthly forecasts extend 18 months and yearly forecasts extend to 2040.  International yearly projections by region extend to 2040.",
-            "modified": "2019-03-12",
             "accessLevel": "public",
-            "identifier": "DOE-019-5492098884",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/analysis/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1940/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/analysis/",
+            "description": "Monthly and yearly forecasts of energy production, consumption, and price at the national level and by energy type.  Monthly forecasts extend 18 months and yearly forecasts extend to 2040.  International yearly projections by region extend to 2040.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/analysis/",
                     "mediaType": "text/html",
-                    "title": "Energy Analysis & Projections",
-                    "downloadURL": "https://www.eia.gov/analysis/"
+                    "title": "Energy Analysis & Projections"
                 }
             ],
+            "identifier": "DOE-019-5492098884",
             "keyword": [
                 "annual data",
                 "coal price",
@@ -5804,41 +5797,39 @@
                 "petroleum stocks",
                 "time series"
             ],
-            "bureauCode": [
-                "019:20"
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2019-03-12",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "spatial": "United States",
+            "temporal": "1940/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Energy Analysis & Projections"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Energy Markets & Finance Data and Statistics",
-            "description": "Information on price volatility and forecast uncertainty for crude oil and natural gas as well as an analysis of 7 key factors that may influence oil prices, physical market factors and factors related to trading and financial markets.",
-            "modified": "2019-03-12",
             "accessLevel": "public",
-            "identifier": "DOE-019-4099288841",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/finance/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1940/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Information on price volatility and forecast uncertainty for crude oil and natural gas as well as an analysis of 7 key factors that may influence oil prices, physical market factors and factors related to trading and financial markets.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5846,6 +5837,7 @@
                     "title": "Energy Finance Data and Statistics"
                 }
             ],
+            "identifier": "DOE-019-4099288841",
             "keyword": [
                 "RBOB futures prices",
                 "WTI crude oil price confidence intervals",
@@ -5860,40 +5852,39 @@
                 "oil price",
                 "price volatility"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/finance/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2019-03-12",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "spatial": "Global",
+            "temporal": "1940/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Energy Markets & Finance Data and Statistics"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Energy-Related Environmental Data",
-            "description": "Environmental data on carbon dioxide emissions from energy and industry, by consuming sector (residential, commercial, industrial, transportation, electric power), and other emissions. Most data available from 1973.",
-            "modified": "2018-02-27",
             "accessLevel": "public",
-            "identifier": "DOE-019-9386767389",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/environment/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1940/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Environmental data on carbon dioxide emissions from energy and industry, by consuming sector (residential, commercial, industrial, transportation, electric power), and other emissions. Most data available from 1973.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -5901,6 +5892,7 @@
                     "title": "Energy Environmental Data"
                 }
             ],
+            "identifier": "DOE-019-9386767389",
             "keyword": [
                 "CO2",
                 "Flue Gas Desulfurization",
@@ -5911,50 +5903,50 @@
                 "greenhouse gases",
                 "power plant emissions"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/environment/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2018-02-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "spatial": "Global",
+            "temporal": "1940/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Energy-Related Environmental Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual Number of Retail Customers by State by Sector From 1990 - Latest Year Available",
-            "description": "Annual data on the number of electricity retail customers. Organized by U.S. state and by sector, i.e., residential, commercial, industrial, and transportation. Annual time series extend back to 1990. Based on EIA Form-861 data.",
-            "modified": "2013-12-12",
             "accessLevel": "public",
-            "identifier": "DOE-019-5286457823",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/state/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1990/2012",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-AEPS-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Annual data on the number of electricity retail customers. Organized by U.S. state and by sector, i.e., residential, commercial, industrial, and transportation. Annual time series extend back to 1990. Based on EIA Form-861 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/state/customers_annual.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Number of Retail Customers From 1990 - Latest Year Available",
-                    "downloadURL": "https://www.eia.gov/electricity/data/state/customers_annual.xls"
+                    "title": "Number of Retail Customers From 1990 - Latest Year Available"
                 }
             ],
+            "identifier": "DOE-019-5286457823",
+            "isPartOf": "DOE-019-AEPS-COLLECTION1",
             "keyword": [
                 "commercial customers",
                 "electric customers",
@@ -5963,53 +5955,53 @@
                 "number of customers",
                 "residential customers"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/state/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2013-12-12",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "1990/2012",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual Number of Retail Customers by State by Sector From 1990 - Latest Year Available"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2005 Electric Power Industry Data",
-            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
-            "modified": "2007-03-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-3977543722",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2005-01-01/2005-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-AEPID-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f86105.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2005 EPI Data EIA-861",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f86105.zip"
+                    "title": "2005 EPI Data EIA-861"
                 }
             ],
+            "identifier": "DOE-019-3977543722",
+            "isPartOf": "DOE-019-AEPID-Collection1",
             "keyword": [
                 "AMI",
                 "AMR",
@@ -6044,53 +6036,53 @@
                 "revenues",
                 "sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2007-03-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2005-01-01/2005-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 2005 Electric Power Industry Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2007 Electric Power Industry Data",
-            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
-            "modified": "2009-03-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-397239724",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2007-01-01/2007-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-AEPID-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f86107.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2007 EPI Data EIA-861",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f86107.zip"
+                    "title": "2007 EPI Data EIA-861"
                 }
             ],
+            "identifier": "DOE-019-397239724",
+            "isPartOf": "DOE-019-AEPID-Collection1",
             "keyword": [
                 "AMI",
                 "AMR",
@@ -6125,54 +6117,54 @@
                 "revenues",
                 "sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2009-03-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2007-01-01/2007-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 2007 Electric Power Industry Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual Average Retail Sales of Electricity by State by Provider From 1990 - Latest Year Available",
-            "description": "Annual data on the average retail sales of electricity in the U.S. Data organized by state and by provider,i.e., total electric industry, full-service providers, and energy-only providers. Annual time series extend back to 1990. Based on Form EIA-861 data.",
-            "modified": "2013-12-12",
             "accessLevel": "public",
-            "identifier": "DOE-019-5395457823",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/state/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1990/2012",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-AEPS-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Annual data on the average retail sales of electricity in the U.S. Data organized by state and by provider,i.e., total electric industry, full-service providers, and energy-only providers. Annual time series extend back to 1990. Based on Form EIA-861 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
+                    "downloadURL": "https://www.eia.gov/electricity/data/state/sales_annual.xls",
                     "format": "xls",
-                    "title": "Retail Sales of Electricity by State by Provider From 1990-Latest Year Available",
-                    "downloadURL": "https://www.eia.gov/electricity/data/state/sales_annual.xls"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Retail Sales of Electricity by State by Provider From 1990-Latest Year Available"
                 }
             ],
+            "identifier": "DOE-019-5395457823",
+            "isPartOf": "DOE-019-AEPS-COLLECTION1",
             "keyword": [
                 "commercial electricity consumption",
                 "commercial electricity sales",
@@ -6183,54 +6175,54 @@
                 "residential electricity consumption",
                 "residential electricity sales"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
-            "programCode": [
-                "019:022"
-            ],
+            "landingPage": "http://www.eia.gov/electricity/data/state/",
             "language": [
                 "en-US"
             ],
-            "references": [
-                "http://www.eia.gov/survey/form/eia_861/form.pdf"
-            ],
-            "theme": [
-                "energy"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual 2007 Electric Generator Report",
-            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 data. Data contained in a zip file. The zip file contains generator-specific information such as initial date of commercial operation, prime movers, generating capacity, energy sources, status of existing and proposed generators, proposed changes to existing generators, county and State location (including power plant address), ownership, and FERC qualifying facility status. The file also includes data on the ability to use multiple fuels; specifically, data on co-firing and fuel switching are included.",
-            "modified": "2009-02-01",
-            "accessLevel": "public",
-            "identifier": "DOE-019-3968885645",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
             "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2007-01-01/2007-12-31",
+            "modified": "2013-12-12",
+            "programCode": [
+                "019:022"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Energy Information Administration"
             },
+            "references": [
+                "http://www.eia.gov/survey/form/eia_861/form.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "1990/2012",
+            "theme": [
+                "energy"
+            ],
+            "title": "Annual Average Retail Sales of Electricity by State by Provider From 1990 - Latest Year Available"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-EIA-AEGR-COLL1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
+            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 data. Data contained in a zip file. The zip file contains generator-specific information such as initial date of commercial operation, prime movers, generating capacity, energy sources, status of existing and proposed generators, proposed changes to existing generators, county and State location (including power plant address), ownership, and FERC qualifying facility status. The file also includes data on the ability to use multiple fuels; specifically, data on co-firing and fuel switching are included.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia860/xls/eia8602007.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2007 EG Report EIA-860",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia860/xls/eia8602007.zip"
+                    "title": "2007 EG Report EIA-860"
                 }
             ],
+            "identifier": "DOE-019-3968885645",
+            "isPartOf": "DOE-019-EIA-AEGR-COLL1",
             "keyword": [
                 "EIA-860",
                 "annual data",
@@ -6257,107 +6249,107 @@
                 "winter capability",
                 "winter capacity"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2009-02-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_860/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2007-01-01/2007-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 2007 Electric Generator Report"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual Average Electricity Price by State by Provider From 1990 - Latest Year Available",
-            "description": "Annual data on the average price of retail electricity to consumers. Data organized by U.S. state and by provider, i.e., total electric industry, full-service providers, restructured retail service providers, energy-only providers, and delivery-only service. Annual time series extend back to 1990. Based on Form EIA-861 data.",
-            "modified": "2018-10-12",
             "accessLevel": "public",
-            "identifier": "DOE-019-5409456723",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/state/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1990/2012",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-AEPS-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Annual data on the average price of retail electricity to consumers. Data organized by U.S. state and by provider, i.e., total electric industry, full-service providers, restructured retail service providers, energy-only providers, and delivery-only service. Annual time series extend back to 1990. Based on Form EIA-861 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/state/avgprice_annual.xlsx",
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "title": "Electricity Price From 1990 - Latest Year Available",
-                    "downloadURL": "https://www.eia.gov/electricity/data/state/avgprice_annual.xlsx"
+                    "title": "Electricity Price From 1990 - Latest Year Available"
                 }
             ],
+            "identifier": "DOE-019-5409456723",
+            "isPartOf": "DOE-019-AEPS-COLLECTION1",
             "keyword": [
                 "commercial electricity price industrial electricity price",
                 "electricity price",
                 "residential electricity price"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/state/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2018-10-12",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "1990/2012",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual Average Electricity Price by State by Provider From 1990 - Latest Year Available"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2005 Electric Generator Report",
-            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 data. Data contained in a zip file.  The zip file contains generator-specific information such as initial date of commercial operation, prime movers, generating capacity, energy sources, status of existing and proposed generators, proposed changes to existing generators, county and State location (including power plant address), ownership, and FERC qualifying facility status. The file also includes data on the ability to use multiple fuels; specifically, data on co-firing and fuel switching are included.",
-            "modified": "2007-03-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-3970009954",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2005-01-01/2005-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-EIA-AEGR-COLL1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
+            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 data. Data contained in a zip file.  The zip file contains generator-specific information such as initial date of commercial operation, prime movers, generating capacity, energy sources, status of existing and proposed generators, proposed changes to existing generators, county and State location (including power plant address), ownership, and FERC qualifying facility status. The file also includes data on the ability to use multiple fuels; specifically, data on co-firing and fuel switching are included.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia860/xls/eia8602005.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2005 EG Report EIA-860",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia860/xls/eia8602005.zip"
+                    "title": "2005 EG Report EIA-860"
                 }
             ],
+            "identifier": "DOE-019-3970009954",
+            "isPartOf": "DOE-019-EIA-AEGR-COLL1",
             "keyword": [
                 "EIA-860",
                 "annual data",
@@ -6384,53 +6376,53 @@
                 "winter capability",
                 "winter capacity"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2007-03-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_860/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2005-01-01/2005-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 2005 Electric Generator Report"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2010 Electric Power Industry Data",
-            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
-            "modified": "2011-11-09",
             "accessLevel": "public",
-            "identifier": "DOE-019-6357635777",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2010-01-01/2010-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-AEPID-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f86110.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2010 EPI Data",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f86110.zip"
+                    "title": "2010 EPI Data"
                 }
             ],
+            "identifier": "DOE-019-6357635777",
+            "isPartOf": "DOE-019-AEPID-Collection1",
             "keyword": [
                 "AMI",
                 "AMR",
@@ -6465,44 +6457,43 @@
                 "revenues",
                 "sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2011-11-09",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2010-01-01/2010-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 2010 Electric Power Industry Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Commercial Buildings Energy Consumption Survey",
-            "description": "The Commercial Buildings Energy Consumption Survey (CBECS) is a national sample survey that collects information on the stock of U.S. commercial buildings, their energy-related building characteristics, and their energy consumption and expenditures. Commercial buildings include all buildings in which at least half of the floorspace is used for a purpose that is not residential, industrial, or agricultural, so they include building types that might not traditionally be considered \"commercial,\" such as schools, correctional institutions, and buildings used for religious worship. The CBECS was first conducted in 1979; the eighth, and most recent survey, was conducted in 2003. CBECS is currently conducted on a quadrennial basis.",
-            "modified": "2016-05-17",
             "accessLevel": "public",
-            "identifier": "DOE-019-4919528404",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/consumption/commercial/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1979/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "The Commercial Buildings Energy Consumption Survey (CBECS) is a national sample survey that collects information on the stock of U.S. commercial buildings, their energy-related building characteristics, and their energy consumption and expenditures. Commercial buildings include all buildings in which at least half of the floorspace is used for a purpose that is not residential, industrial, or agricultural, so they include building types that might not traditionally be considered \"commercial,\" such as schools, correctional institutions, and buildings used for religious worship. The CBECS was first conducted in 1979; the eighth, and most recent survey, was conducted in 2003. CBECS is currently conducted on a quadrennial basis.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6510,6 +6501,7 @@
                     "title": "Commercial Buildings"
                 }
             ],
+            "identifier": "DOE-019-4919528404",
             "keyword": [
                 "Buildings",
                 "Commercial",
@@ -6526,53 +6518,53 @@
                 "Survey",
                 "Trends"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/consumption/commercial/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2016-05-17",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/consumption/commercial/survey-background-technical-information.cfm"
             ],
+            "spatial": "United States",
+            "temporal": "1979/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Commercial Buildings Energy Consumption Survey"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 1986",
-            "description": "Monthly 1986 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2005-11-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-2345673489",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1986-01-01/1986-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 1986 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/1986/data/impa86d.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "1986 Petroleum Imports",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/1986/data/impa86d.xls"
+                    "title": "1986 Petroleum Imports"
                 }
             ],
+            "identifier": "DOE-019-2345673489",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -6584,46 +6576,45 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2005-11-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "1986-01-01/1986-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports 1986"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual Company Level Natural Gas Supply and Disposition From 1997-Latest Year Available",
-            "description": "Annual company level data on the supply and disposition of natural gas in the United States from an identified universe of pipelines, local distribution companies, and operators of fields, wells or gas processing plants, who distribute gas to end users or transport gas across State borders; or underground natural gas storage operators.  Annual time series extend back to 1997. Based on Form EIA-176 data.",
-            "modified": "2018-09-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-5397458712",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/cfapps/ngqs/ngqs_notes.html",
-            "landingPage": "http://www.eia.gov/naturalgas/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2008-01-01/2008-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/cfapps/ngqs/ngqs_notes.html",
+            "description": "Annual company level data on the supply and disposition of natural gas in the United States from an identified universe of pipelines, local distribution companies, and operators of fields, wells or gas processing plants, who distribute gas to end users or transport gas across State borders; or underground natural gas storage operators.  Annual time series extend back to 1997. Based on Form EIA-176 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6631,6 +6622,7 @@
                     "title": "Natural Gas Supply and Disposition"
                 }
             ],
+            "identifier": "DOE-019-5397458712",
             "keyword": [
                 "gas processing plants",
                 "local distribution companies",
@@ -6638,55 +6630,55 @@
                 "natural gas supply",
                 "natural gas transporters",
                 "natural gas wells",
-                "underground natural gas storage operators"
-            ],
-            "bureauCode": [
-                "019:20"
-            ],
-            "programCode": [
-                "019:022"
+                "underground natural gas storage operators"
             ],
+            "landingPage": "http://www.eia.gov/naturalgas/",
             "language": [
                 "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2018-09-01",
+            "programCode": [
+                "019:022"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/cfapps/ngqs/ngqs_user_guide.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2008-01-01/2008-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual Company Level Natural Gas Supply and Disposition From 1997-Latest Year Available"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 1987",
-            "description": "Monthly 1987 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2005-11-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-2346464646",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1987-01-01/1987-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 1987 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/1987/data/impa87d.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "1987 Petroleum Imports",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/1987/data/impa87d.xls"
+                    "title": "1987 Petroleum Imports"
                 }
             ],
+            "identifier": "DOE-019-2346464646",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -6698,54 +6690,55 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2005-11-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "1987-01-01/1987-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports 1987"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 1993",
-            "description": "Monthly 1993 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2005-11-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-2352372849",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1993-01-01/1993-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 1993 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/1993/data/impa93d.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "1993 Petroleum Imports",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/1993/data/impa93d.xls"
+                    "title": "1993 Petroleum Imports"
                 }
             ],
+            "identifier": "DOE-019-2352372849",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -6757,54 +6750,53 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2005-11-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "1993-01-01/1993-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports 1993"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 1999",
-            "description": "Monthly 1999 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2005-11-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-2358444555",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1999-01-01/1999-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 1999 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/1999/data/impa99d.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "1999 Petroleum Imports",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/1999/data/impa99d.xls"
+                    "title": "1999 Petroleum Imports"
                 }
             ],
+            "identifier": "DOE-019-2358444555",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -6816,54 +6808,54 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2005-11-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "1999-01-01/1999-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports 1999"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 2001",
-            "description": "Monthly 2001 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2005-11-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-2360472845",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001-01-01/2001-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 2001 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2001/data/impa01d.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2001 Petroleum Imports",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2001/data/impa01d.xls"
+                    "title": "2001 Petroleum Imports"
                 }
             ],
+            "identifier": "DOE-019-2360472845",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -6875,54 +6867,54 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2005-11-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2001-01-01/2001-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports 2001"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 2006",
-            "description": "Monthly 2006 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2007-10-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-2365529472",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2006-01-01/2006-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 2006 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2006/data/impa06d.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2006 Petroleum Imports",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2006/data/impa06d.xls"
+                    "title": "2006 Petroleum Imports"
                 }
             ],
+            "identifier": "DOE-019-2365529472",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -6934,44 +6926,43 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2007-10-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2006-01-01/2006-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports 2006"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Energy Data and Statistics from U.S. States",
-            "description": "State-level data on all energy sources. Data on production, consumption, reserves, stocks, prices, imports, and exports. Data are collated from state-specific data reported elsewhere on the EIA website and are the most recent values available.  Data on U.S. territories also available.",
-            "modified": "2018-06-29",
             "accessLevel": "public",
-            "identifier": "DOE-019-1296988438",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/state/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "State",
-            "temporal": "1940/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "State-level data on all energy sources. Data on production, consumption, reserves, stocks, prices, imports, and exports. Data are collated from state-specific data reported elsewhere on the EIA website and are the most recent values available.  Data on U.S. territories also available.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -6979,6 +6970,7 @@
                     "title": "Energy Data and Statistics"
                 }
             ],
+            "identifier": "DOE-019-1296988438",
             "keyword": [
                 "annual data",
                 "coal price",
@@ -7002,50 +6994,50 @@
                 "petroleum reserves",
                 "petroleum stocks"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/state/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2018-06-29",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "spatial": "State",
+            "temporal": "1940/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Energy Data and Statistics from U.S. States"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2002 Electric Power Industry Data",
-            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
-            "modified": "2007-03-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-3974125479",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2002-01-01/2002-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-AEPID-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f86102.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2002 EIA Data EIA-861",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f86102.zip"
+                    "title": "2002 EIA Data EIA-861"
                 }
             ],
+            "identifier": "DOE-019-3974125479",
+            "isPartOf": "DOE-019-AEPID-Collection1",
             "keyword": [
                 "AMI",
                 "AMR",
@@ -7080,53 +7072,53 @@
                 "revenues",
                 "sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
+            "language": [
+                "us-EN"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2007-03-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2002-01-01/2002-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 2002 Electric Power Industry Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2003 Electric Power Industry Data",
-            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
-            "modified": "2007-03-02",
             "accessLevel": "public",
-            "identifier": "DOE-019-3975666645",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2003-01-01/2003-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-AEPID-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f86103.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2003 EIA Data EIA-861",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f86103.zip"
+                    "title": "2003 EIA Data EIA-861"
                 }
             ],
+            "identifier": "DOE-019-3975666645",
+            "isPartOf": "DOE-019-AEPID-Collection1",
             "keyword": [
                 "AMI",
                 "AMR",
@@ -7161,53 +7153,53 @@
                 "revenues",
                 "sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2007-03-02",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2003-01-01/2003-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 2003 Electric Power Industry Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2006 Electric Power Industry Data",
-            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
-            "modified": "2007-11-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-3978888845",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2006-01-01/2006-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-AEPID-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f86106.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2006 EPI Data EIA-861",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f86106.zip"
+                    "title": "2006 EPI Data EIA-861"
                 }
             ],
+            "identifier": "DOE-019-3978888845",
+            "isPartOf": "DOE-019-AEPID-Collection1",
             "keyword": [
                 "AMI",
                 "AMR",
@@ -7242,53 +7234,53 @@
                 "revenues",
                 "sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2007-11-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2006-01-01/2006-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 2006 Electric Power Industry Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2008 Electric Power Industry Data",
-            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
-            "modified": "2010-05-28",
             "accessLevel": "public",
-            "identifier": "DOE-019-4810000032",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2008-01-01/2008-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-AEPID-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f86108.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2008 EPI Data",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f86108.zip"
+                    "title": "2008 EPI Data"
                 }
             ],
+            "identifier": "DOE-019-4810000032",
+            "isPartOf": "DOE-019-AEPID-Collection1",
             "keyword": [
                 "AMI",
                 "AMR",
@@ -7323,53 +7315,53 @@
                 "revenues",
                 "sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2010-05-28",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2008-01-01/2008-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 2008 Electric Power Industry Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 1991",
-            "description": "Monthly 1991 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2005-11-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-2350538393",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1991-01-01/1991-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 1991 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/1991/data/impa91d.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "1991 Petroleum Imports",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/1991/data/impa91d.xls"
+                    "title": "1991 Petroleum Imports"
                 }
             ],
+            "identifier": "DOE-019-2350538393",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -7381,54 +7373,54 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2005-11-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "1991-01-01/1991-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports 1991"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 1995",
-            "description": "Monthly 1995 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2005-11-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-2354482945",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1995-01-01/1995-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 1995 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/1995/data/impa95d.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "1995 Petroleum Imports",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/1995/data/impa95d.xls"
+                    "title": "1995 Petroleum Imports"
                 }
             ],
+            "identifier": "DOE-019-2354482945",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -7440,54 +7432,54 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2005-11-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "1995-01-01/1995-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports 1995"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 1997",
-            "description": "Monthly 1997 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2005-11-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-2356342748",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1997-01-01/1997-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 1997 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/1997/data/impa97d.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "1997 Petroleum Imports",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/1997/data/impa97d.xls"
+                    "title": "1997 Petroleum Imports"
                 }
             ],
+            "identifier": "DOE-019-2356342748",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -7499,55 +7491,55 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2005-11-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "1997-01-01/1997-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports 1997"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 2003",
-            "description": "Monthly 2003 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2005-11-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-2362482937",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2003-01-01/2003-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 2003 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2003/data/impa03d.xls",
                     "format": "xlsx",
-                    "title": "2003 Petroleum Imports",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2003/data/impa03d.xls"
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "2003 Petroleum Imports"
                 }
             ],
+            "identifier": "DOE-019-2362482937",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -7559,54 +7551,54 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2005-11-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2003-01-01/2003-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports 2003"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 2009",
-            "description": "Monthly 2009 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2010-09-09",
             "accessLevel": "public",
-            "identifier": "DOE-019-4817171717",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2009-01-01/2009-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 2009 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2009/data/impa09d.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2009 Petroleum Imports",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2009/data/impa09d.xls"
+                    "title": "2009 Petroleum Imports"
                 }
             ],
+            "identifier": "DOE-019-4817171717",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -7618,52 +7610,52 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2010-09-09",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2009-01-01/2009-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports 2009"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual Distribution and Production of Oil and Gas Wells by State From 1919-Latest Year Available",
-            "description": "Annual data on the number and production volumes of oil and natural gas wells by state. Annual time series extend back to 1919.",
-            "modified": "2011-01-07",
             "accessLevel": "public",
-            "identifier": "DOE-019-5418154829",
-            "dataQuality": true,
-            "landingPage": "https://www.eia.gov/naturalgas/archive/petrosystem/petrosysog.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2009-01-01/2009-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Annual data on the number and production volumes of oil and natural gas wells by state. Annual time series extend back to 1919.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/naturalgas/archive/petrosystem/petrosysog.html",
                     "mediaType": "text/html",
-                    "title": "Distribution and Production of Oil and Gas Wells by State",
-                    "downloadURL": "https://www.eia.gov/naturalgas/archive/petrosystem/petrosysog.html"
+                    "title": "Distribution and Production of Oil and Gas Wells by State"
                 }
             ],
+            "identifier": "DOE-019-5418154829",
             "keyword": [
                 "energy",
                 "gas condensate wells",
@@ -7672,43 +7664,43 @@
                 "oil well production",
                 "oil wells"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "https://www.eia.gov/naturalgas/archive/petrosystem/petrosysog.html",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2011-01-07",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/naturalgas/annual/pdf/appendix_a.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2009-01-01/2009-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual Distribution and Production of Oil and Gas Wells by State From 1919-Latest Year Available"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Short-Term Energy Outlook Application Programming Interface (API)",
-            "description": "The API provides data back to 1990 and projections annually, monthly, and quarterly for 18 months.  Summarizes the outlook for demand, supply and prices for petroleum, natural gas, electricity and coal as well as projections of carbon dioxide emissions from the production of fossil fuels, and a discussion of price forecast uncertainty.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2014-09-09",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-5566437856",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/forecasts/steo/index.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "The API provides data back to 1990 and projections annually, monthly, and quarterly for 18 months.  Summarizes the outlook for demand, supply and prices for petroleum, natural gas, electricity and coal as well as projections of carbon dioxide emissions from the production of fossil fuels, and a discussion of price forecast uncertainty.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -7723,6 +7715,7 @@
                     "title": "API Web Page"
                 }
             ],
+            "identifier": "DOE-019-5566437856",
             "keyword": [
                 "OPEC surplus production capacity",
                 "biofuels",
@@ -7748,48 +7741,47 @@
                 "residential usage",
                 "weather"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/forecasts/steo/index.cfm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2014-09-09",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "spatial": "United States",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Short-Term Energy Outlook Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Monthly and Annual Energy Consumption by Sector",
-            "description": "Monthly data since January 1973 and annual data since 1949 on U.S. primary and total energy consumption by end-use sector (residential, commercial, industrial, transportation) and electric power sector.",
-            "modified": "2019-03-26",
             "accessLevel": "public",
-            "identifier": "DOE-019-5416563059",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/totalenergy/data/monthly/index.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1973/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Monthly data since January 1973 and annual data since 1949 on U.S. primary and total energy consumption by end-use sector (residential, commercial, industrial, transportation) and electric power sector.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/totalenergy/data/monthly/query/mer_data_excel.asp?table=T02.01",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Energy Consumption",
-                    "downloadURL": "https://www.eia.gov/totalenergy/data/monthly/query/mer_data_excel.asp?table=T02.01"
+                    "title": "Energy Consumption"
                 }
             ],
+            "identifier": "DOE-019-5416563059",
             "keyword": [
                 "commercial energy consumption",
                 "electric power energy consumption",
@@ -7800,106 +7792,106 @@
                 "residential energy consumption",
                 "transportation energy consumption"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/totalenergy/data/monthly/index.cfm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2019-03-26",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/totalenergy/data/annual/index.cfm"
             ],
+            "spatial": "United States",
+            "temporal": "1973/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Monthly and Annual Energy Consumption by Sector"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Monthly Gross Withdrawals of Natural Gas",
-            "description": "Data from 2005 to the latest month available on gross withdrawals of natural gas. Data organized by area and by month. Based on Form EIA-914 data.",
-            "modified": "2019-02-28",
             "accessLevel": "public",
-            "identifier": "DOE-019-5283463849",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/oil_gas/natural_gas/data_publications/eia914/methodology.html",
-            "landingPage": "http://www.eia.gov/petroleum/production/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2005/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/oil_gas/natural_gas/data_publications/eia914/methodology.html",
+            "description": "Data from 2005 to the latest month available on gross withdrawals of natural gas. Data organized by area and by month. Based on Form EIA-914 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/production/xls/table3.xlsx",
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "title": "Natural Gas Withdrawals",
-                    "downloadURL": "https://www.eia.gov/petroleum/production/xls/table3.xlsx"
+                    "title": "Natural Gas Withdrawals"
                 }
             ],
+            "identifier": "DOE-019-5283463849",
             "keyword": [
                 "gross withdrawal",
                 "natural gas production",
                 "natural gas withdrawal"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/production/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2019-02-28",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/oil_gas/natural_gas/data_publications/eia914/methodology.html",
                 "http://www.eia.gov/survey/form/eia_914/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2005/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Monthly Gross Withdrawals of Natural Gas"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Average Number of Employees and Hours 2006",
-            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, union status, labor hours, and employment data. Annual time series extend back to 1983. Based on EIA Form-7A data.",
-            "modified": "2008-09-11",
             "accessLevel": "public",
-            "identifier": "DOE-019-4833659358",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
-            "landingPage": "http://www.eia.gov/coal/data.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "State and County",
-            "temporal": "2006-01-01/2006-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
+            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, union status, labor hours, and employment data. Annual time series extend back to 1983. Based on EIA Form-7A data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic2006.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2006 Coal Production",
-                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic2006.xls"
+                    "title": "2006 Coal Production"
                 }
             ],
+            "identifier": "DOE-019-4833659358",
+            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
             "keyword": [
                 "coal data",
                 "coal data file",
@@ -7910,53 +7902,53 @@
                 "coal production file",
                 "energy"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/data.cfm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2008-09-11",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_7a/form.pdf"
             ],
+            "spatial": "State and County",
+            "temporal": "2006-01-01/2006-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Average Number of Employees and Hours 2006"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Average Number of Employees and Hours 2003",
-            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, union status, labor hours, and employment data. Annual time series extend back to 1983. Based on EIA Form-7A data.",
-            "modified": "2008-09-11",
             "accessLevel": "public",
-            "identifier": "DOE-019-4836445588",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
-            "landingPage": "http://www.eia.gov/coal/data.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "State and County",
-            "temporal": "2003-01-01/2003-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
+            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, union status, labor hours, and employment data. Annual time series extend back to 1983. Based on EIA Form-7A data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic2003.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2003 Coal Production",
-                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic2003.xls"
+                    "title": "2003 Coal Production"
                 }
             ],
+            "identifier": "DOE-019-4836445588",
+            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
             "keyword": [
                 "coal data",
                 "coal data file",
@@ -7967,53 +7959,53 @@
                 "coal production file",
                 "energy"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/data.cfm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2008-09-11",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_7a/form.pdf"
             ],
+            "spatial": "State and County",
+            "temporal": "2003-01-01/2003-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Average Number of Employees and Hours 2003"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Average Number of Employees and Hours 2002",
-            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, union status, labor hours, and employment data. Annual time series extend back to 1983. Based on EIA Form-7A data.",
-            "modified": "2008-09-11",
             "accessLevel": "public",
-            "identifier": "DOE-019-4837774433",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
-            "landingPage": "http://www.eia.gov/coal/data.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "State and County",
-            "temporal": "2002-01-01/2002-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
+            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, union status, labor hours, and employment data. Annual time series extend back to 1983. Based on EIA Form-7A data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic2002.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2002 Coal Production",
-                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic2002.xls"
+                    "title": "2002 Coal Production"
                 }
             ],
+            "identifier": "DOE-019-4837774433",
+            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
             "keyword": [
                 "coal data",
                 "coal data file",
@@ -8024,53 +8016,53 @@
                 "coal production file",
                 "energy"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/data.cfm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2008-09-11",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_7a/form.pdf"
             ],
+            "spatial": "State and County",
+            "temporal": "2002-01-01/2002-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Average Number of Employees and Hours 2002"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual Revenue from Retail Sales of Electricity by State by Provider From 1990 - Latest Year Available",
-            "description": "Annual data on the revenue from retail sales of electricity. Organized by state and by provider, i.e., total electric industry, full-service providers, restructured retail service providers, energy-only providers, and delivery-only service.  Annual time series extend back to 1990. Based on EIA Form-861 data.",
-            "modified": "2013-12-12",
             "accessLevel": "public",
-            "identifier": "DOE-019-5396453627",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/state/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1990/2012",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-AEPS-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Annual data on the revenue from retail sales of electricity. Organized by state and by provider, i.e., total electric industry, full-service providers, restructured retail service providers, energy-only providers, and delivery-only service.  Annual time series extend back to 1990. Based on EIA Form-861 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/state/revenue_annual.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Revenue from Retail Sales of Electricity From 1990 - Latest Year Available",
-                    "downloadURL": "https://www.eia.gov/electricity/data/state/revenue_annual.xls"
+                    "title": "Revenue from Retail Sales of Electricity From 1990 - Latest Year Available"
                 }
             ],
+            "identifier": "DOE-019-5396453627",
+            "isPartOf": "DOE-019-AEPS-COLLECTION1",
             "keyword": [
                 "commercial electricity revenue",
                 "commercial electricity sales",
@@ -8081,53 +8073,53 @@
                 "residential electricity revenue",
                 "residential electricity sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/state/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2013-12-12",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "1990/2012",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual Revenue from Retail Sales of Electricity by State by Provider From 1990 - Latest Year Available"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2001 Electric Power Industry Data",
-            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
-            "modified": "2007-03-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-3973434321",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001-01-01/2001-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-AEPID-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_861/form.pdf",
+            "description": "Historical U.S. electric utility data. Data on generation, electric purchases, peak load, sales, revenues, customer counts, demand-side management programs, green pricing, net metering programs, and distributed generation capacity. Based on EIA Form-861 data. Data contained in a zip file.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f86101.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2001 EPI Data EIA-861",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia861/zip/f86101.zip"
+                    "title": "2001 EPI Data EIA-861"
                 }
             ],
+            "identifier": "DOE-019-3973434321",
+            "isPartOf": "DOE-019-AEPID-Collection1",
             "keyword": [
                 "AMI",
                 "AMR",
@@ -8162,54 +8154,54 @@
                 "revenues",
                 "sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia861/index.html",
+            "language": [
+                "us-EN"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2007-03-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "us-EN"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_861/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2001-01-01/2001-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 2001 Electric Power Industry Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2006 Electric Generator Report",
-            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 data. Data contained in a zip file. The zip file contains generator-specific information such as initial date of commercial operation, prime movers, generating capacity, energy sources, status of existing and proposed generators, proposed changes to existing generators, county and State location (including power plant address), ownership, and FERC qualifying facility status. The file also includes data on the ability to use multiple fuels; specifically, data on co-firing and fuel switching are included.",
-            "modified": "2007-10-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-3971453859",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2006-01-01/2006-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-EIA-AEGR-COLL1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
+            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 data. Data contained in a zip file. The zip file contains generator-specific information such as initial date of commercial operation, prime movers, generating capacity, energy sources, status of existing and proposed generators, proposed changes to existing generators, county and State location (including power plant address), ownership, and FERC qualifying facility status. The file also includes data on the ability to use multiple fuels; specifically, data on co-firing and fuel switching are included.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia860/xls/eia8602006.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2006 EG Report EIA-860",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia860/xls/eia8602006.zip"
+                    "title": "2006 EG Report EIA-860"
                 }
             ],
+            "identifier": "DOE-019-3971453859",
+            "isPartOf": "DOE-019-EIA-AEGR-COLL1",
             "keyword": [
                 "EIA-860",
                 "annual data",
@@ -8236,54 +8228,54 @@
                 "winter capability",
                 "winter capacity"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2007-10-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_860/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2006-01-01/2006-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 2006 Electric Generator Report"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2008 Electric Generator Report",
-            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 data. Data contained in a zip file.                                                                                                                                                        The zip file contains generator-specific information such as initial date of commercial operation, prime movers, generating capacity, energy sources, status of existing and proposed generators, proposed changes to existing generators, county and State location (including power plant address), ownership, and FERC qualifying facility status. The file also includes data on the ability to use multiple fuels; specifically, data on co-firing and fuel switching are included.",
-            "modified": "2010-04-28",
             "accessLevel": "public",
-            "identifier": "DOE-019-4811111154",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2008-01-01/2008-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-EIA-AEGR-COLL1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
+            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 data. Data contained in a zip file.                                                                                                                                                        The zip file contains generator-specific information such as initial date of commercial operation, prime movers, generating capacity, energy sources, status of existing and proposed generators, proposed changes to existing generators, county and State location (including power plant address), ownership, and FERC qualifying facility status. The file also includes data on the ability to use multiple fuels; specifically, data on co-firing and fuel switching are included.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia860/xls/eia8602008.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2008 EG Report EIA-860",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia860/xls/eia8602008.zip"
+                    "title": "2008 EG Report EIA-860"
                 }
             ],
+            "identifier": "DOE-019-4811111154",
+            "isPartOf": "DOE-019-EIA-AEGR-COLL1",
             "keyword": [
                 "EIA-860",
                 "annual data",
@@ -8310,53 +8302,53 @@
                 "winter capability",
                 "winter capacity"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2010-04-28",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_860/form.pdf"
             ],
-            "theme": [
-                "energy"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Annual Summary Electricity Statistics for the U. S. From 2003 - Latest Year Available",
-            "description": "Annual data back to 2003 at the national level for electricity generation; capacity; consumption and cost of fossil fuels; sales, price and revenue; emissions; demand-side management; and operating revenues, expenses, and income. Based on Form EIA-860 and Form EIA-861 data.",
-            "modified": "2018-10-22",
-            "accessLevel": "public",
-            "identifier": "DOE-019-5403540322",
-            "dataQuality": true,
-            "describedBy": "https://www.eia.gov/electricity/annual/pdf/tech_notes.pdf",
-            "landingPage": "http://www.eia.gov/electricity/annual/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
             "spatial": "United States",
-            "temporal": "2000/2012",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
+            "temporal": "2008-01-01/2008-12-31",
+            "theme": [
+                "energy"
+            ],
+            "title": "Annual 2008 Electric Generator Report"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "https://www.eia.gov/electricity/annual/pdf/tech_notes.pdf",
+            "description": "Annual data back to 2003 at the national level for electricity generation; capacity; consumption and cost of fossil fuels; sales, price and revenue; emissions; demand-side management; and operating revenues, expenses, and income. Based on Form EIA-860 and Form EIA-861 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/annual/xls/epa_01_02.xlsx",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Summary Electricity Statistics",
-                    "downloadURL": "https://www.eia.gov/electricity/annual/xls/epa_01_02.xlsx"
+                    "title": "Summary Electricity Statistics"
                 }
             ],
+            "identifier": "DOE-019-5403540322",
             "keyword": [
                 "capacity",
                 "consumption and cost of fossil fuels",
@@ -8369,53 +8361,53 @@
                 "price and revenue",
                 "sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/annual/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2018-10-22",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/electricity/annual/pdf/tech_notes.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2000/2012",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual Summary Electricity Statistics for the U. S. From 2003 - Latest Year Available"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 1988",
-            "description": "Monthly 1988 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2005-11-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-2347234756",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1988-01-01/1988-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 1988 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/1988/data/impa88d.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "1998 Petroleum Imports",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/1988/data/impa88d.xls"
+                    "title": "1998 Petroleum Imports"
                 }
             ],
+            "identifier": "DOE-019-2347234756",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -8427,54 +8419,54 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2005-11-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "1988-01-01/1988-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports 1988"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 1990",
-            "description": "Monthly 1990 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2005-11-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-2349436726",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1990-01-01/1990-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 1990 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/1990/data/impa90d.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "1990 Petroleum Imports",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/1990/data/impa90d.xls"
+                    "title": "1990 Petroleum Imports"
                 }
             ],
+            "identifier": "DOE-019-2349436726",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -8486,54 +8478,54 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2005-11-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "1990-01-01/1990-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports 1990"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 1994",
-            "description": "Monthly 1994 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2005-11-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-2353482958",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1994-01-01/1994-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 1994 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/1994/data/impa94d.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "1994 Petroleum Imports",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/1994/data/impa94d.xls"
+                    "title": "1994 Petroleum Imports"
                 }
             ],
+            "identifier": "DOE-019-2353482958",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -8545,54 +8537,54 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2005-11-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "1994-01-01/1994-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports 1994"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 1996",
-            "description": "Monthly 1996 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2005-11-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-2355583355",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1996-01-01/1996-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 1996 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/1996/data/impa96d.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "1996 Petroleum Imports",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/1996/data/impa96d.xls"
+                    "title": "1996 Petroleum Imports"
                 }
             ],
+            "identifier": "DOE-019-2355583355",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -8604,54 +8596,54 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2005-11-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "1996-01-01/1996-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports 1996"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 2002",
-            "description": "Monthly 2002 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2005-11-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-2361482945",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2002-01-01/2002-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 2002 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2002/data/impa02d.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2002 Petroleum Imports",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2002/data/impa02d.xls"
+                    "title": "2002 Petroleum Imports"
                 }
             ],
+            "identifier": "DOE-019-2361482945",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -8663,46 +8655,44 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2005-11-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2002-01-01/2002-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports 2002"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data Application Programming Interface (API)",
-            "description": "Data on coal prices, reserves, production, imports and exports, stocks, consumption, receipts, and market sales. API also includes coal mine production, labor hours, average employees, and productivity.",
-            "modified": "2014-02-27T18:32:55.387907",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-6548765908",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "State",
-            "temporal": "2001/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on coal prices, reserves, production, imports and exports, stocks, consumption, receipts, and market sales. API also includes coal mine production, labor hours, average employees, and productivity.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -8717,6 +8707,8 @@
                     "title": "API Web Page"
                 }
             ],
+            "identifier": "DOE-019-6548765908",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "coal",
                 "coal consumption",
@@ -8727,53 +8719,53 @@
                 "coal reserves",
                 "coal stocks"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2014-02-27T18:32:55.387907",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "State",
+            "temporal": "2001/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Monthly Electric Utility Sales and Revenue Data 2010",
-            "description": "Utility level retail sales of electricity and associated revenue in 2010. Organized by reporting month, state, and by end-use sector, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 data.",
-            "modified": "2014-05-20",
             "accessLevel": "public",
-            "identifier": "DOE-019-4534785645",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_826/instructions.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia826/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2010-01-01/2010-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-MEUSR-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_826/instructions.pdf",
+            "description": "Utility level retail sales of electricity and associated revenue in 2010. Organized by reporting month, state, and by end-use sector, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia826/xls/f8262010.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Electricity Utility Sales 2010",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia826/xls/f8262010.xls"
+                    "title": "Electricity Utility Sales 2010"
                 }
             ],
+            "identifier": "DOE-019-4534785645",
+            "isPartOf": "DOE-019-MEUSR-COLLECTION1",
             "keyword": [
                 "cents per kWh",
                 "commercial electric prices",
@@ -8793,54 +8785,54 @@
                 "state electric prices",
                 "transportation electric prices"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia826/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2014-05-20",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_826/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2010-01-01/2010-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Monthly Electric Utility Sales and Revenue Data 2010"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Monthly Electric Utility Sales and Revenue Data 2011",
-            "description": "Utility level retail sales of electricity and associated revenue in 2011. Organized by reporting month, state, and by end-use sector, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 data.",
-            "modified": "2014-05-20",
             "accessLevel": "public",
-            "identifier": "DOE-019-5645676689",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_826/instructions.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia826/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2011-01-01/2011-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-MEUSR-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_826/instructions.pdf",
+            "description": "Utility level retail sales of electricity and associated revenue in 2011. Organized by reporting month, state, and by end-use sector, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia826/xls/f8262011.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Electricity Utility Sales 2011",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia826/xls/f8262011.xls"
+                    "title": "Electricity Utility Sales 2011"
                 }
             ],
+            "identifier": "DOE-019-5645676689",
+            "isPartOf": "DOE-019-MEUSR-COLLECTION1",
             "keyword": [
                 "cents per kWh",
                 "commercial electric prices",
@@ -8860,48 +8852,49 @@
                 "state electric prices",
                 "transportation electric prices"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia826/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2014-05-20",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_826/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2011-01-01/2011-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Monthly Electric Utility Sales and Revenue Data 2011"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Petroleum & Other Liquids Data and Statistics",
-            "description": "Weekly, monthly, and annual data on crude oil, gasoline, diesel, propane, jet fuel, ethanol, and other liquid fuels. Domestic and international data on petroleum prices, crude reserves and production, refining and processing, imports/exports, stocks, and consumption/sales.",
-            "modified": "2019-03-21",
             "accessLevel": "public",
-            "identifier": "DOE-019-4567349003",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/petroleum/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1W",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Weekly, monthly, and annual data on crude oil, gasoline, diesel, propane, jet fuel, ethanol, and other liquid fuels. Domestic and international data on petroleum prices, crude reserves and production, refining and processing, imports/exports, stocks, and consumption/sales.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/data.cfm",
                     "mediaType": "text/html",
-                    "title": "Petroleum & Other Liquids",
-                    "downloadURL": "https://www.eia.gov/petroleum/data.cfm"
+                    "title": "Petroleum & Other Liquids"
                 },
                 {
                     "@type": "dcat:Distribution",
@@ -8915,6 +8908,7 @@
                     "title": "API Web Page"
                 }
             ],
+            "identifier": "DOE-019-4567349003",
             "keyword": [
                 "aviation gasoline",
                 "biofuels",
@@ -8930,50 +8924,48 @@
                 "refinery",
                 "residual fuel oil"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2019-03-21",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Petroleum & Other Liquids Data and Statistics"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Monthly Electric Utility Sales and Revenue Data 2008",
-            "description": "Utility level retail sales of electricity and associated revenue in 2008. Organized by reporting month, state, and by end-use sector, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 data.",
-            "modified": "2009-04-24",
             "accessLevel": "public",
-            "identifier": "DOE-019-1138385926",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_826/instructions.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia826/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2008-01-01/2008-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-MEUSR-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_826/instructions.pdf",
+            "description": "Utility level retail sales of electricity and associated revenue in 2008. Organized by reporting month, state, and by end-use sector, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia826/xls/f8262008.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2008 Electric Sales and Revenue",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia826/xls/f8262008.xls"
+                    "title": "2008 Electric Sales and Revenue"
                 }
             ],
+            "identifier": "DOE-019-1138385926",
+            "isPartOf": "DOE-019-MEUSR-COLLECTION1",
             "keyword": [
                 "cents per kWh",
                 "commercial electric prices",
@@ -8993,53 +8985,53 @@
                 "state electric prices",
                 "transportation electric prices"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia826/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2009-04-24",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_826/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2008-01-01/2008-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Monthly Electric Utility Sales and Revenue Data 2008"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Monthly Electric Utility Sales and Revenue Data 2009",
-            "description": "Utility level retail sales of electricity and associated revenue in 2009. Organized by reporting month, state, and by end-use sector, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 data.",
-            "modified": "2011-02-15",
             "accessLevel": "public",
-            "identifier": "DOE-019-4846784523",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_826/instructions.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia826/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2009-01-01/2009-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-MEUSR-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_826/instructions.pdf",
+            "description": "Utility level retail sales of electricity and associated revenue in 2009. Organized by reporting month, state, and by end-use sector, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia826/xls/f8262009.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2009 Electric Sales and Revenue",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia826/xls/f8262009.xls"
+                    "title": "2009 Electric Sales and Revenue"
                 }
             ],
+            "identifier": "DOE-019-4846784523",
+            "isPartOf": "DOE-019-MEUSR-COLLECTION1",
             "keyword": [
                 "cents per kWh",
                 "commercial electric prices",
@@ -9059,44 +9051,43 @@
                 "state electric prices",
                 "transportation electric prices"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia826/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2011-02-15",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_826/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2009-01-01/2009-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Monthly Electric Utility Sales and Revenue Data 2009"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Nuclear & Uranium Data and Statistics",
-            "description": "Data on uranium and nuclear fuel, nuclear power plants and reactors, radioactive waste, and nuclear power generation. International data on nuclear generation also available. Monthly, quarterly, and annual data available.",
-            "modified": "2019-02-06",
             "accessLevel": "public",
-            "identifier": "DOE-019-5291681930",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/nuclear/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "2013/2040",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on uranium and nuclear fuel, nuclear power plants and reactors, radioactive waste, and nuclear power generation. International data on nuclear generation also available. Monthly, quarterly, and annual data available.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9104,6 +9095,7 @@
                     "title": "Nuclear and Uranium Data"
                 }
             ],
+            "identifier": "DOE-019-5291681930",
             "keyword": [
                 "capacity factor",
                 "nuclear electricity generation",
@@ -9118,42 +9110,40 @@
                 "uranium purchases",
                 "uranium reserves"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/nuclear/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2019-02-06",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "spatial": "Global",
+            "temporal": "2013/2040",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Nuclear & Uranium Data and Statistics"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Petroleum Data Application Programming Interface (API)",
-            "description": "Data on crude oil reserves and production; refining and processing; imports, exports, movements; stocks; prices; and consumption/sales are available in machine-readable format.                                                                Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2014-02-27T18:33:24.150177",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-3498237812",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/petroleum/data.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "rights": "The EIA API is offered as a free public service, although registration is required.",
-            "spatial": "Global",
-            "temporal": "2013/2040",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1W",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on crude oil reserves and production; refining and processing; imports, exports, movements; stocks; prices; and consumption/sales are available in machine-readable format.                                                                Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9168,6 +9158,7 @@
                     "title": "API Web Page"
                 }
             ],
+            "identifier": "DOE-019-3498237812",
             "keyword": [
                 "Aviation Gasoline",
                 "Kerosene",
@@ -9183,50 +9174,51 @@
                 "propane",
                 "refinery"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
-            "programCode": [
-                "019:022"
-            ],
+            "landingPage": "http://www.eia.gov/petroleum/data.cfm",
             "language": [
                 "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2014-02-27T18:33:24.150177",
+            "programCode": [
+                "019:022"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "rights": "The EIA API is offered as a free public service, although registration is required.",
+            "spatial": "Global",
+            "temporal": "2013/2040",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Petroleum Data Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Production by MSHA ID, Mine Operation, and Union Status, 1991",
-            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, and union status. Annual time series extend back to 1983. Based on EIA Form-7A data.",
-            "modified": "2008-09-11",
             "accessLevel": "public",
-            "identifier": "DOE-019-4824675689",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/data.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "State and County",
-            "temporal": "1991-01-01/1991-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, and union status. Annual time series extend back to 1983. Based on EIA Form-7A data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic1991.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "1991 Coal Production",
-                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic1991.xls"
+                    "title": "1991 Coal Production"
                 }
             ],
+            "identifier": "DOE-019-4824675689",
+            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
             "keyword": [
                 "coal data",
                 "coal data file",
@@ -9237,53 +9229,53 @@
                 "coal production file",
                 "energy"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/data.cfm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2008-09-11",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_7a/form.pdf"
             ],
+            "spatial": "State and County",
+            "temporal": "1991-01-01/1991-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Production by MSHA ID, Mine Operation, and Union Status, 1991"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 1989",
-            "description": "Monthly 1989 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2005-11-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-2348474945",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1989-01-01/1989-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 1989 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/1989/data/impa89d.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "1989 Petroleum Imports",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/1989/data/impa89d.xls"
+                    "title": "1989 Petroleum Imports"
                 }
             ],
+            "identifier": "DOE-019-2348474945",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -9295,54 +9287,54 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2005-11-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "1989-01-01/1989-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports 1989"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 1992",
-            "description": "Monthly 1992 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2005-11-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-2351783628",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1992-01-01/1992-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 1992 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/1992/data/impa92d.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "1992 Petroleum Imports",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/1992/data/impa92d.xls"
+                    "title": "1992 Petroleum Imports"
                 }
             ],
+            "identifier": "DOE-019-2351783628",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -9354,54 +9346,54 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2005-11-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "1992-01-01/1992-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports 1992"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 1998",
-            "description": "Monthly 1998 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2005-11-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-2357787878",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1998-01-01/1998-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 1998 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/1998/data/impa98d.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "1998 Petroleum Imports",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/1998/data/impa98d.xls"
+                    "title": "1998 Petroleum Imports"
                 }
             ],
+            "identifier": "DOE-019-2357787878",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -9413,54 +9405,54 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2005-11-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "1998-01-01/1998-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports 1998"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 2005",
-            "description": "Monthly 2005 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2006-10-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-2364583920",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2005-01-01/2005-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 2005 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2005/data/impa05d.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2005 Petroleum Imports",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2005/data/impa05d.xls"
+                    "title": "2005 Petroleum Imports"
                 }
             ],
+            "identifier": "DOE-019-2364583920",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -9472,54 +9464,54 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2006-10-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2005-01-01/2005-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports 2005"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 2010",
-            "description": "Monthly 2010 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2011-07-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-6359555888",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2010-01-01/2010-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 2010 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2010/data/impa10d.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2010 Petroleum Imports",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2010/data/impa10d.xls"
+                    "title": "2010 Petroleum Imports"
                 }
             ],
+            "identifier": "DOE-019-6359555888",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -9531,45 +9523,44 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
-            "programCode": [
-                "019:022"
-            ],
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
             "language": [
                 "en-US"
             ],
-            "references": [
-                "http://www.eia.gov/survey/form/eia_814/form.pdf",
-                "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
-            ],
-            "theme": [
-                "energy"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Electricity Data and Statistics Application Programming Interface (API)",
-            "description": "Monthly, quarterly, and annual data on electricity generation, consumption, retail sales, price, revenue from retail sales, useful thermal output, fossil fuel stocks, fossil fuel receipts, and quality of fossil fuel. Data organized by fuel type, i.e., coal petroleum, natural gas, nuclear, hydroelectric, wind, solar, geothermal, and wood. Also, data organized by sector, i.e., electric power, electric utility, independent power producers, commercial, and industrial.                                                                                                                                          Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2014-02-27T16:27:23.324514",
-            "accessLevel": "restricted public",
-            "identifier": "DOE-019-3299699499",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/beta/api/qb.cfm?category=0",
             "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1940/2014",
+            "modified": "2011-07-01",
+            "programCode": [
+                "019:022"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Energy Information Administration"
             },
+            "references": [
+                "http://www.eia.gov/survey/form/eia_814/form.pdf",
+                "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "2010-01-01/2010-12-31",
+            "theme": [
+                "energy"
+            ],
+            "title": "Company Level Petroleum Imports 2010"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Monthly, quarterly, and annual data on electricity generation, consumption, retail sales, price, revenue from retail sales, useful thermal output, fossil fuel stocks, fossil fuel receipts, and quality of fossil fuel. Data organized by fuel type, i.e., coal petroleum, natural gas, nuclear, hydroelectric, wind, solar, geothermal, and wood. Also, data organized by sector, i.e., electric power, electric utility, independent power producers, commercial, and industrial.                                                                                                                                          Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9589,6 +9580,7 @@
                     "title": "API Web Page"
                 }
             ],
+            "identifier": "DOE-019-3299699499",
             "keyword": [
                 "average revenue per kilowatthour",
                 "capacity",
@@ -9629,53 +9621,53 @@
                 "transmission capacity",
                 "wholesale power"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/api/qb.cfm?category=0",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2014-02-27T16:27:23.324514",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/#electricity"
             ],
+            "spatial": "United States",
+            "temporal": "1940/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Electricity Data and Statistics Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Monthly Electric Utility Sales and Revenue Data 2012",
-            "description": "Utility level retail sales of electricity and associated revenue in 2012. Organized by reporting month, state, and by end-use sector, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 data.",
-            "modified": "2013-12-18",
             "accessLevel": "public",
-            "identifier": "DOE-019-4567895645",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_826/instructions.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia826/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2013-01-01/2013-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-MEUSR-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_826/instructions.pdf",
+            "description": "Utility level retail sales of electricity and associated revenue in 2012. Organized by reporting month, state, and by end-use sector, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia826/xls/f8262012.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Electric Utility Sales 2012",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia826/xls/f8262012.xls"
+                    "title": "Electric Utility Sales 2012"
                 }
             ],
+            "identifier": "DOE-019-4567895645",
+            "isPartOf": "DOE-019-MEUSR-COLLECTION1",
             "keyword": [
                 "cents per kWh",
                 "commercial electric prices",
@@ -9695,54 +9687,54 @@
                 "state electric prices",
                 "transportation electric prices"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia826/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2013-12-18",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_826/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2013-01-01/2013-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Monthly Electric Utility Sales and Revenue Data 2012"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2004 Electric Generator Report",
-            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 data. Data contained in a zip file. The zip file contains generator-specific information such as initial date of commercial operation, prime movers, generating capacity, energy sources, status of existing and proposed generators, proposed changes to existing generators, county and State location (including power plant address), ownership, and FERC qualifying facility status. The file also includes data on the ability to use multiple fuels; specifically, data on co-firing and fuel switching are included.",
-            "modified": "2007-03-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-3969357595",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2004-01-01/2004-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-EIA-AEGR-COLL1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
+            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 data. Data contained in a zip file. The zip file contains generator-specific information such as initial date of commercial operation, prime movers, generating capacity, energy sources, status of existing and proposed generators, proposed changes to existing generators, county and State location (including power plant address), ownership, and FERC qualifying facility status. The file also includes data on the ability to use multiple fuels; specifically, data on co-firing and fuel switching are included.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia860/xls/eia8602004.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2004 EGR Data EIA-860",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia860/xls/eia8602004.zip"
+                    "title": "2004 EGR Data EIA-860"
                 }
             ],
+            "identifier": "DOE-019-3969357595",
+            "isPartOf": "DOE-019-EIA-AEGR-COLL1",
             "keyword": [
                 "EIA-860",
                 "annual data",
@@ -9769,53 +9761,53 @@
                 "winter capability",
                 "winter capacity"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2007-03-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_860m/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2004-01-01/2004-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual 2004 Electric Generator Report"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 2013",
-            "description": "Monthly 2013 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2014-05-12",
             "accessLevel": "public",
-            "identifier": "DOE-019-3456435465",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2013-01-01/2013-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 2013 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2013/data/impa13d.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "CLP Imports 2013",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2013/data/impa13d.xls"
+                    "title": "CLP Imports 2013"
                 }
             ],
+            "identifier": "DOE-019-3456435465",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -9827,44 +9819,43 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2014-05-12",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2013-01-01/2013-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports 2013"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Alternative Fuel Vehicle Data",
-            "description": "Annual data on the number of on-road alternative fuel vehicles and hybrid vehicles made available in the U.S. Data on the use of alternative fueled vehicles and the amount of fuel they consume is also available. Based on Form EIA-886 data and data extend back to 1994.",
-            "modified": "2019-05-22",
             "accessLevel": "public",
-            "identifier": "DOE-019-4536758345",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/renewable/afv/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "State",
-            "temporal": "2003/2017",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Annual data on the number of on-road alternative fuel vehicles and hybrid vehicles made available in the U.S. Data on the use of alternative fueled vehicles and the amount of fuel they consume is also available. Based on Form EIA-886 data and data extend back to 1994.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9872,6 +9863,7 @@
                     "title": "Alternative Fuel Vehicle"
                 }
             ],
+            "identifier": "DOE-019-4536758345",
             "keyword": [
                 "alternative fuel vehicles",
                 "alternative fuels",
@@ -9880,45 +9872,43 @@
                 "ethanol",
                 "hybrid vehiclels"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/renewable/afv/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2019-05-22",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/renewable/alternative_transport_vehicles/pdf/defs-sources-notes.pdf"
             ],
+            "spatial": "State",
+            "temporal": "2003/2017",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Alternative Fuel Vehicle Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "International Energy Outlook Table Browser",
-            "description": "The International Energy Outlook (IEO) presents EIA's long-term assessment of world energy markets. The IEO includes projections of world energy demand by region and primary energy source through 2040; electricity generation by fuel type; and energy-related carbon dioxide emissions.",
-            "modified": "2018-07-24",
             "accessLevel": "public",
-            "identifier": "DOE-019-5293333333",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/forecasts/ieo/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "2013/2040",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-IEDAD-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "The International Energy Outlook (IEO) presents EIA's long-term assessment of world energy markets. The IEO includes projections of world energy demand by region and primary energy source through 2040; electricity generation by fuel type; and energy-related carbon dioxide emissions.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -9926,6 +9916,8 @@
                     "title": "International Energy Outlook Table Browser"
                 }
             ],
+            "identifier": "DOE-019-5293333333",
+            "isPartOf": "DOE-019-IEDAD-COLLECTION1",
             "keyword": [
                 "carbon dioxide",
                 "climate",
@@ -9951,50 +9943,50 @@
                 "renewable energy",
                 "yearly projections"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/forecasts/ieo/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2018-07-24",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "spatial": "Global",
+            "temporal": "2013/2040",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Outlook Table Browser"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Average Number of Employees and Hours 2007",
-            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, union status, labor hours, and employment data. Annual time series extend back to 1983. Based on EIA Form-7A data.",
-            "modified": "1905-06-30",
             "accessLevel": "public",
-            "identifier": "DOE-019-1137456523",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
-            "landingPage": "http://www.eia.gov/coal/data.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "State and County",
-            "temporal": "2007-01-01/2007-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
+            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, union status, labor hours, and employment data. Annual time series extend back to 1983. Based on EIA Form-7A data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic2007.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Coal Production",
-                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic2007.xls"
+                    "title": "Coal Production"
                 }
             ],
+            "identifier": "DOE-019-1137456523",
+            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
             "keyword": [
                 "coal data",
                 "coal data file",
@@ -10005,53 +9997,53 @@
                 "coal production file",
                 "energy"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
-            "programCode": [
-                "019:022"
-            ],
+            "landingPage": "http://www.eia.gov/coal/data.cfm",
             "language": [
                 "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "1905-06-30",
+            "programCode": [
+                "019:022"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_7a/form.pdf"
             ],
+            "spatial": "State and County",
+            "temporal": "2007-01-01/2007-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Average Number of Employees and Hours 2007"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Average Number of Employees and Hours 2010",
-            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, union status, labor hours, and employment data. Annual time series extend back to 1983. Based on EIA Form-7A data.",
-            "modified": "2012-04-09",
             "accessLevel": "public",
-            "identifier": "DOE-019-6373482058",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
-            "landingPage": "http://www.eia.gov/coal/data.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2010-01-01/2010-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
+            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, union status, labor hours, and employment data. Annual time series extend back to 1983. Based on EIA Form-7A data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic2010.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2010 Coal Production",
-                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic2010.xls"
+                    "title": "2010 Coal Production"
                 }
             ],
+            "identifier": "DOE-019-6373482058",
+            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
             "keyword": [
                 "coal data",
                 "coal data file",
@@ -10062,53 +10054,53 @@
                 "coal production file",
                 "energy"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/data.cfm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2012-04-09",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_7a/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2010-01-01/2010-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Average Number of Employees and Hours 2010"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Average Number of Employees and Hours 2005",
-            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, union status, labor hours, and employment data. Annual time series extend back to 1983. Based on EIA Form-7A data.",
-            "modified": "2008-09-11",
             "accessLevel": "public",
-            "identifier": "DOE-019-4834447755",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
-            "landingPage": "http://www.eia.gov/coal/data.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "State and County",
-            "temporal": "2005-01-01/2005-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
+            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, union status, labor hours, and employment data. Annual time series extend back to 1983. Based on EIA Form-7A data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic2005.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2005 Coal Production",
-                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic2005.xls"
+                    "title": "2005 Coal Production"
                 }
             ],
+            "identifier": "DOE-019-4834447755",
+            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
             "keyword": [
                 "coal data",
                 "coal data file",
@@ -10119,53 +10111,53 @@
                 "coal production file",
                 "energy"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/data.cfm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2008-09-11",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_7a/form.pdf"
             ],
+            "spatial": "State and County",
+            "temporal": "2005-01-01/2005-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Average Number of Employees and Hours 2005"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Production by MSHA ID, Mine Operation, and Union Status, 1997",
-            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, and union status. Annual time series extend back to 1983. Based on EIA Form-7A data.",
-            "modified": "2008-09-11",
             "accessLevel": "public",
-            "identifier": "DOE-019-4818777745",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
-            "landingPage": "http://www.eia.gov/coal/data.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "State and County",
-            "temporal": "1997-01-01/1997-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
+            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, and union status. Annual time series extend back to 1983. Based on EIA Form-7A data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic1997.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "1997 Coal Production",
-                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic1997.xls"
+                    "title": "1997 Coal Production"
                 }
             ],
+            "identifier": "DOE-019-4818777745",
+            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
             "keyword": [
                 "coal data",
                 "coal data file",
@@ -10176,53 +10168,53 @@
                 "coal production file",
                 "energy"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/data.cfm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2008-09-11",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_7a/form.pdf"
             ],
+            "spatial": "State and County",
+            "temporal": "1997-01-01/1997-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Production by MSHA ID, Mine Operation, and Union Status, 1997"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Production by MSHA ID, Mine Operation, and Union Status, 1996",
-            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, and union status. Annual time series extend back to 1983. Based on EIA Form-7A data.",
-            "modified": "2008-09-11",
             "accessLevel": "public",
-            "identifier": "DOE-019-4819667667",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
-            "landingPage": "http://www.eia.gov/coal/data.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "State and County",
-            "temporal": "1996-01-01/1996-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
+            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, and union status. Annual time series extend back to 1983. Based on EIA Form-7A data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic1996.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "1996 Coal Production",
-                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic1996.xls"
+                    "title": "1996 Coal Production"
                 }
             ],
+            "identifier": "DOE-019-4819667667",
+            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
             "keyword": [
                 "coal data",
                 "coal data file",
@@ -10233,53 +10225,53 @@
                 "coal production file",
                 "energy"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/data.cfm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2008-09-11",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_7a/form.pdf"
             ],
+            "spatial": "State and County",
+            "temporal": "1996-01-01/1996-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Production by MSHA ID, Mine Operation, and Union Status, 1996"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Production by MSHA ID, Mine Operation, and Union Status, 1995",
-            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, and union status. Annual time series extend back to 1983. Based on EIA Form-7A data.",
-            "modified": "2008-09-11",
             "accessLevel": "public",
-            "identifier": "DOE-019-4820668367",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
-            "landingPage": "http://www.eia.gov/coal/data.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "State and County",
-            "temporal": "1995-01-01/1995-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
+            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, and union status. Annual time series extend back to 1983. Based on EIA Form-7A data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic1995.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "1995 Coal Production",
-                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic1995.xls"
+                    "title": "1995 Coal Production"
                 }
             ],
+            "identifier": "DOE-019-4820668367",
+            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
             "keyword": [
                 "coal data",
                 "coal data file",
@@ -10290,54 +10282,54 @@
                 "coal production file",
                 "energy"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/data.cfm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2008-09-11",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_7a/form.pdf"
             ],
+            "spatial": "State and County",
+            "temporal": "1995-01-01/1995-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Production by MSHA ID, Mine Operation, and Union Status, 1995"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual 2010 Electric Generator Report",
-            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 data. Data contained in a zip file.                                                                                                                                                        The zip file contains generator-specific information such as initial date of commercial operation, prime movers, generating capacity, energy sources, status of existing and proposed generators, proposed changes to existing generators, county and State location (including power plant address), ownership, and FERC qualifying facility status. The file also includes data on the ability to use multiple fuels; specifically, data on co-firing and fuel switching are included.",
-            "modified": "2011-11-30",
             "accessLevel": "public",
-            "identifier": "DOE-019-6358888888",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2010-01-01/2010-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-EIA-AEGR-COLL1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_860/form.pdf",
+            "description": "Annual U.S. generator level data about generators at electric power plants owned and operated by electric utilities and nonutilities (including independent power producers, combined heat and power producers, and other industrials). Based on EIA Form-860 data. Data contained in a zip file.                                                                                                                                                        The zip file contains generator-specific information such as initial date of commercial operation, prime movers, generating capacity, energy sources, status of existing and proposed generators, proposed changes to existing generators, county and State location (including power plant address), ownership, and FERC qualifying facility status. The file also includes data on the ability to use multiple fuels; specifically, data on co-firing and fuel switching are included.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia860/xls/eia8602010.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2010 EG Report EIA-860",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia860/xls/eia8602010.zip"
+                    "title": "2010 EG Report EIA-860"
                 }
             ],
+            "identifier": "DOE-019-6358888888",
+            "isPartOf": "DOE-019-EIA-AEGR-COLL1",
             "keyword": [
                 "EIA-860",
                 "annual data",
@@ -10364,54 +10356,54 @@
                 "winter capability",
                 "winter capacity"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
-            "programCode": [
-                "019:022"
-            ],
+            "landingPage": "http://www.eia.gov/electricity/data/eia860/index.html",
             "language": [
                 "en-US"
             ],
-            "references": [
-                "http://www.eia.gov/survey/form/eia_860/form.pdf"
-            ],
-            "theme": [
-                "energy"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 2000",
-            "description": "Monthly 2000 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2005-11-01",
-            "accessLevel": "public",
-            "identifier": "DOE-019-2359335484",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
             "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2000-01-01/2000-12-31",
+            "modified": "2011-11-30",
+            "programCode": [
+                "019:022"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Energy Information Administration"
             },
+            "references": [
+                "http://www.eia.gov/survey/form/eia_860/form.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "2010-01-01/2010-12-31",
+            "theme": [
+                "energy"
+            ],
+            "title": "Annual 2010 Electric Generator Report"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 2000 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2000/data/impa00d.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2000 Petroleum Imports",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2000/data/impa00d.xls"
+                    "title": "2000 Petroleum Imports"
                 }
             ],
+            "identifier": "DOE-019-2359335484",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -10423,54 +10415,54 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2005-11-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2000-01-01/2000-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports 2000"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 2004",
-            "description": "Monthly 2004 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2005-11-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-2363472849",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2004-01-01/2004-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 2004 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2004/data/impa04d.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2004 Petroleum Imports",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2004/data/impa04d.xls"
+                    "title": "2004 Petroleum Imports"
                 }
             ],
+            "identifier": "DOE-019-2363472849",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -10482,54 +10474,54 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2005-11-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2004-01-01/2004-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports 2004"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 2007",
-            "description": "Monthly 2007 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2008-11-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-2366482933",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2007-01-01/2007-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 2007 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2007/data/impa07d.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2007 Petroleum Imports",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2007/data/impa07d.xls"
+                    "title": "2007 Petroleum Imports"
                 }
             ],
+            "identifier": "DOE-019-2366482933",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -10541,46 +10533,44 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2008-11-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2007-01-01/2007-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports 2007"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Annual Energy Outlook Application Programming Interface (API)",
-            "description": "The Annual Energy Outlook API presents long-term annual projections of energy supply, demand, and prices through 2040. The projections, focused on U.S. energy markets, are based on results from EIA\u2019s National Energy Modeling System (NEMS). NEMS enables EIA to make projections under alternative, internally-consistent sets of assumptions, the results of which are presented as cases. The projections cover natural gas, petroleum, coal, electricity and renewable fuels by sector (residential, commercial, industrial, electric generation, and transportation) and by region (census). Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2014-05-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-6666665554",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/forecasts/aeo/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "rights": "The EIA API is offered as a free public service, although registration is required.",
-            "spatial": "United States",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-AEO-Collection1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "The Annual Energy Outlook API presents long-term annual projections of energy supply, demand, and prices through 2040. The projections, focused on U.S. energy markets, are based on results from EIA\u2019s National Energy Modeling System (NEMS). NEMS enables EIA to make projections under alternative, internally-consistent sets of assumptions, the results of which are presented as cases. The projections cover natural gas, petroleum, coal, electricity and renewable fuels by sector (residential, commercial, industrial, electric generation, and transportation) and by region (census). Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10594,6 +10584,8 @@
                     "title": "API Web Page"
                 }
             ],
+            "identifier": "DOE-019-6666665554",
+            "isPartOf": "DOE-019-AEO-Collection1",
             "keyword": [
                 "consumption",
                 "economy",
@@ -10614,41 +10606,40 @@
                 "refining",
                 "weather"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/forecasts/aeo/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2014-05-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "rights": "The EIA API is offered as a free public service, although registration is required.",
+            "spatial": "United States",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Annual Energy Outlook Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Bulk Download Facility",
-            "description": "The bulk download facility provides the entire contents of each major API data set in a single ZIP file. A small JSON formatted manifest file lists the bulk files and the update date of each file. The manifest is generally updated daily and can be downloaded from http://api.eia.gov/bulk/manifest.txt. The manifest contains information about the bulk files, including all required common core attributes.",
-            "modified": "2013-05-29",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-3334456781",
-            "dataQuality": true,
-            "describedBy": "http://api.eia.gov/bulk/manifest.txt",
-            "landingPage": "http://www.eia.gov/beta/api/bulkfiles.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1986/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://api.eia.gov/bulk/manifest.txt",
+            "description": "The bulk download facility provides the entire contents of each major API data set in a single ZIP file. A small JSON formatted manifest file lists the bulk files and the update date of each file. The manifest is generally updated daily and can be downloaded from http://api.eia.gov/bulk/manifest.txt. The manifest contains information about the bulk files, including all required common core attributes.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10657,6 +10648,7 @@
                     "title": "Bulk Download Facility"
                 }
             ],
+            "identifier": "DOE-019-3334456781",
             "keyword": [
                 "accessLevel",
                 "accessLevelComment",
@@ -10678,51 +10670,51 @@
                 "title",
                 "webService"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/beta/api/bulkfiles.cfm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2013-05-29",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "spatial": "Global",
+            "temporal": "1986/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Bulk Download Facility"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 2011",
-            "description": "Monthly 2011 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2013-09-27",
             "accessLevel": "public",
-            "identifier": "DOE-019-4565478845",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2011-01-01/2011-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/instructions.pdf",
+            "description": "Monthly 2011 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2011/data/impa11d.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "CLP Imports 2011",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2011/data/impa11d.xls"
+                    "title": "CLP Imports 2011"
                 }
             ],
+            "identifier": "DOE-019-4565478845",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company imports",
                 "crude oil imports",
@@ -10734,44 +10726,44 @@
                 "petroleum imports",
                 "residual fuel oil imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2013-09-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_814/form.pdf",
                 "http://www.eia.gov/survey/form/eia_814/instructions.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2011-01-01/2011-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Company Level Petroleum Imports 2011"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Natural Gas Data Application Programming Interface (API)",
-            "description": "EIA data on domestic natural gas prices, exploration and reserves, production, imports and exports, storage, pipelines, and consumption. Data released on a weekly, monthly and/or annual basis. The International Energy Data API provides international natural gas data: http://www.eia.gov/beta/api/qb.cfm?category=1505864                                                                                                  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2014-02-27T18:32:55.387909",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-4972990347",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/naturalgas/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1W",
-            "isPartOf": "DOE-019-NGD-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "EIA data on domestic natural gas prices, exploration and reserves, production, imports and exports, storage, pipelines, and consumption. Data released on a weekly, monthly and/or annual basis. The International Energy Data API provides international natural gas data: http://www.eia.gov/beta/api/qb.cfm?category=1505864                                                                                                  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -10786,6 +10778,8 @@
                     "title": "API Web Page"
                 }
             ],
+            "identifier": "DOE-019-4972990347",
+            "isPartOf": "DOE-019-NGD-COLLECTION1",
             "keyword": [
                 "base gas",
                 "citygate",
@@ -10808,53 +10802,51 @@
                 "vented and flared",
                 "working gas"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
-            "programCode": [
-                "019:022"
-            ],
+            "landingPage": "http://www.eia.gov/naturalgas/",
             "language": [
                 "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2014-02-27T18:32:55.387909",
+            "programCode": [
+                "019:022"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/#naturalgas"
             ],
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Natural Gas Data Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Employee Hours 1998",
-            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, and union status. Annual time series extend back to 1983. Based on EIA Form-7A data.",
-            "modified": "2008-09-12",
             "accessLevel": "public",
-            "identifier": "DOE-019-4841111111",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
-            "landingPage": "http://www.eia.gov/coal/data.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "State and County",
-            "temporal": "1998-01-01/1998-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
+            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, and union status. Annual time series extend back to 1983. Based on EIA Form-7A data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic1998.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "1998 Coal Production",
-                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic1998.xls"
+                    "title": "1998 Coal Production"
                 }
             ],
+            "identifier": "DOE-019-4841111111",
+            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
             "keyword": [
                 "coal data",
                 "coal data file",
@@ -10865,53 +10857,53 @@
                 "coal production file",
                 "energy"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/data.cfm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2008-09-12",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_7a/form.pdf"
             ],
+            "spatial": "State and County",
+            "temporal": "1998-01-01/1998-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Employee Hours 1998"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Average Number of Employees and Hours 2009",
-            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, union status, labor hours, and employment data. Annual time series extend back to 1983. Based on EIA Form-7A data.",
-            "modified": "2011-02-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-6356777666",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
-            "landingPage": "http://www.eia.gov/coal/data.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "State and County",
-            "temporal": "2009-01-01/2009-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
+            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, union status, labor hours, and employment data. Annual time series extend back to 1983. Based on EIA Form-7A data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic1999.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2009 Coal Production",
-                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic1999.xls"
+                    "title": "2009 Coal Production"
                 }
             ],
+            "identifier": "DOE-019-6356777666",
+            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
             "keyword": [
                 "coal data",
                 "coal data file",
@@ -10922,53 +10914,53 @@
                 "coal production file",
                 "energy"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/data.cfm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2011-02-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_7a/form.pdf"
             ],
+            "spatial": "State and County",
+            "temporal": "2009-01-01/2009-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Average Number of Employees and Hours 2009"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Average Number of Employees and Hours 2004",
-            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, union status, labor hours, and employment data. Annual time series extend back to 1983. Based on EIA Form-7A data.",
-            "modified": "2008-09-11",
             "accessLevel": "public",
-            "identifier": "DOE-019-4835657585",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
-            "landingPage": "http://www.eia.gov/coal/data.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "State and County",
-            "temporal": "2004-01-01/2004-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
+            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, union status, labor hours, and employment data. Annual time series extend back to 1983. Based on EIA Form-7A data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic2004.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2004 Coal Production",
-                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic2004.xls"
+                    "title": "2004 Coal Production"
                 }
             ],
+            "identifier": "DOE-019-4835657585",
+            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
             "keyword": [
                 "coal data",
                 "coal data file",
@@ -10979,53 +10971,53 @@
                 "coal production file",
                 "energy"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/data.cfm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2008-09-11",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_7a/form.pdf"
             ],
+            "spatial": "State and County",
+            "temporal": "2004-01-01/2004-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Average Number of Employees and Hours 2004"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Average Number of Employees and Hours 2001",
-            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, union status, labor hours, and employment data. Annual time series extend back to 1983. Based on EIA Form-7A data.",
-            "modified": "2008-09-11",
             "accessLevel": "public",
-            "identifier": "DOE-019-4838547654",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
-            "landingPage": "http://www.eia.gov/coal/data.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "State and County",
-            "temporal": "2001-01-01/2001-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
+            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, union status, labor hours, and employment data. Annual time series extend back to 1983. Based on EIA Form-7A data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic2001.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2001 Coal Production",
-                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic2001.xls"
+                    "title": "2001 Coal Production"
                 }
             ],
+            "identifier": "DOE-019-4838547654",
+            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
             "keyword": [
                 "coal data",
                 "coal data file",
@@ -11036,53 +11028,53 @@
                 "coal production file",
                 "energy"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/data.cfm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2008-09-11",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_7a/form.pdf"
             ],
+            "spatial": "State and County",
+            "temporal": "2001-01-01/2001-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Average Number of Employees and Hours 2001"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Average Number of Employees and Hours 2000",
-            "description": "Coal production data files contain information which identify the U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, union status, labor hours, and employment data. Annual time series extend back to 1983. Based on EIA Form-7A data.",
-            "modified": "2009-04-15",
             "accessLevel": "public",
-            "identifier": "DOE-019-4839767625",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
-            "landingPage": "http://www.eia.gov/coal/data.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "State and County",
-            "temporal": "2000-01-01/2000-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
+            "description": "Coal production data files contain information which identify the U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, union status, labor hours, and employment data. Annual time series extend back to 1983. Based on EIA Form-7A data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic2000.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2000 Coal Production",
-                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic2000.xls"
+                    "title": "2000 Coal Production"
                 }
             ],
+            "identifier": "DOE-019-4839767625",
+            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
             "keyword": [
                 "coal data",
                 "coal data file",
@@ -11093,53 +11085,53 @@
                 "coal production file",
                 "energy"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/data.cfm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2009-04-15",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_7a/form.pdf"
             ],
+            "spatial": "State and County",
+            "temporal": "2000-01-01/2000-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Average Number of Employees and Hours 2000"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Production by MSHA ID, Mine Operation, and Union Status, 1994",
-            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, and union status. Annual time series extend back to 1983. Based on EIA Form-7A data.",
-            "modified": "2008-09-11",
             "accessLevel": "public",
-            "identifier": "DOE-019-4821666642",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
-            "landingPage": "http://www.eia.gov/coal/data.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "County and State",
-            "temporal": "1994-01-01/1994-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
+            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, and union status. Annual time series extend back to 1983. Based on EIA Form-7A data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic1994.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "1994 Coal Production",
-                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic1994.xls"
+                    "title": "1994 Coal Production"
                 }
             ],
+            "identifier": "DOE-019-4821666642",
+            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
             "keyword": [
                 "coal data",
                 "coal data file",
@@ -11150,53 +11142,53 @@
                 "coal production file",
                 "energy"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
-            "programCode": [
-                "019:022"
-            ],
+            "landingPage": "http://www.eia.gov/coal/data.cfm",
             "language": [
                 "en-US"
             ],
-            "references": [
-                "http://www.eia.gov/survey/form/eia_7a/form.pdf"
-            ],
-            "theme": [
-                "energy"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Coal Production by MSHA ID, Mine Operation, and Union Status, 1993",
-            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, and union status. Annual time series extend back to 1983. Based on EIA Form-7A data.",
-            "modified": "2008-09-11",
-            "accessLevel": "public",
-            "identifier": "DOE-019-4822774598",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
-            "landingPage": "http://www.eia.gov/coal/data.cfm",
             "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "State and County",
-            "temporal": "1993-01-01/1993-12-31",
+            "modified": "2008-09-11",
+            "programCode": [
+                "019:022"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Energy Information Administration"
             },
-            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
+            "references": [
+                "http://www.eia.gov/survey/form/eia_7a/form.pdf"
+            ],
+            "spatial": "County and State",
+            "temporal": "1994-01-01/1994-12-31",
+            "theme": [
+                "energy"
+            ],
+            "title": "Coal Production by MSHA ID, Mine Operation, and Union Status, 1994"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
+            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, and union status. Annual time series extend back to 1983. Based on EIA Form-7A data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic1993.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "1993 Coal Production",
-                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic1993.xls"
+                    "title": "1993 Coal Production"
                 }
             ],
+            "identifier": "DOE-019-4822774598",
+            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
             "keyword": [
                 "coal data",
                 "coal data file",
@@ -11207,53 +11199,53 @@
                 "coal production file",
                 "energy"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/data.cfm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2008-09-11",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_7a/form.pdf"
             ],
+            "spatial": "State and County",
+            "temporal": "1993-01-01/1993-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Production by MSHA ID, Mine Operation, and Union Status, 1993"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Production by MSHA ID, Mine Operation, and Union Status, 1992",
-            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, and union status. Annual time series extend back to 1983. Based on EIA Form-7A data.",
-            "modified": "2008-09-11",
             "accessLevel": "public",
-            "identifier": "DOE-019-4823475923",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
-            "landingPage": "http://www.eia.gov/coal/data.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "State and County",
-            "temporal": "1992-01-01/1992-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
+            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, and union status. Annual time series extend back to 1983. Based on EIA Form-7A data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic1992.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "1992 Coal Production",
-                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic1992.xls"
+                    "title": "1992 Coal Production"
                 }
             ],
+            "identifier": "DOE-019-4823475923",
+            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
             "keyword": [
                 "coal data",
                 "coal data file",
@@ -11264,53 +11256,53 @@
                 "coal production file",
                 "energy"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/data.cfm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2008-09-11",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_7a/instructions.pdf"
             ],
+            "spatial": "State and County",
+            "temporal": "1992-01-01/1992-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Production by MSHA ID, Mine Operation, and Union Status, 1992"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Average Number of Employees and Hours 2012",
-            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, union status, labor hours, and employment data. Annual time series extend back to 1983. Based on EIA Form-7A data.",
-            "modified": "2013-12-16",
             "accessLevel": "public",
-            "identifier": "DOE-019-5438657634",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
-            "landingPage": "http://www.eia.gov/coal/data.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2012-01-01/2012-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_7a/instructions.pdf",
+            "description": "Data on U.S mining operation (i.e., operation name, mailing address, telephone number, State and county of operation, etc.), annual coal production, code definitions, union status, labor hours, and employment data. Annual time series extend back to 1983. Based on EIA Form-7A data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic2012.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Coal Production 2012",
-                    "downloadURL": "https://www.eia.gov/coal/data/public/xls/coalpublic2012.xls"
+                    "title": "Coal Production 2012"
                 }
             ],
+            "identifier": "DOE-019-5438657634",
+            "isPartOf": "DOE-019-CPMSHAID-COLLECTION1",
             "keyword": [
                 "coal data",
                 "coal data file",
@@ -11321,53 +11313,53 @@
                 "coal production file",
                 "energy"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/data.cfm",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2013-12-16",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_7a/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2012-01-01/2012-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Production by MSHA ID, Mine Operation, Union Status, and Average Number of Employees and Hours 2012"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Monthly 2002 Utility and Nonutility Fuel Receipts and Fuel Quality Data",
-            "description": "Monthly 2002 data on U.S. electric power generation, fuel consumption, stocks, and fuel heat content from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant-level.  Based on Form EIA-906 data. Monthly time series extend back to 2001.",
-            "modified": "2003-12-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-6355748392",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2002-01-01/2002-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-MUNF-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
+            "description": "Monthly 2002 data on U.S. electric power generation, fuel consumption, stocks, and fuel heat content from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant-level.  Based on Form EIA-906 data. Monthly time series extend back to 2001.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/xls/f906920_2002.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2002 Uility and Nonutility Fuel Data",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/xls/f906920_2002.zip"
+                    "title": "2002 Uility and Nonutility Fuel Data"
                 }
             ],
+            "identifier": "DOE-019-6355748392",
+            "isPartOf": "DOE-019-MUNF-COLLECTION1",
             "keyword": [
                 "coal receipts",
                 "electricity generating fuel",
@@ -11376,55 +11368,55 @@
                 "gas receipts",
                 "oil receipts"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2003-12-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_923/form.pdf",
                 "http://www.eia.gov/survey/form/eia_906/instructions_form.pdf",
                 "http://www.eia.gov/survey/form/eia_920/instructions_form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2002-01-01/2002-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Monthly 2002 Utility and Nonutility Fuel Receipts and Fuel Quality Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Monthly 2003 Utility and Nonutility Fuel Receipts and Fuel Quality Data",
-            "description": "Monthly 2003 data on U.S. electric power generation, fuel consumption, stocks, and fuel heat content from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant-level.  Based on Form EIA-906 data. Monthly time series extend back to 2001.",
-            "modified": "2004-12-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-6354456327",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2003-01-01/2003-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-MUNF-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
+            "description": "Monthly 2003 data on U.S. electric power generation, fuel consumption, stocks, and fuel heat content from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant-level.  Based on Form EIA-906 data. Monthly time series extend back to 2001.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/xls/f906920_2003.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2003 Utility and Nonutility Fuel Data",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/xls/f906920_2003.zip"
+                    "title": "2003 Utility and Nonutility Fuel Data"
                 }
             ],
+            "identifier": "DOE-019-6354456327",
+            "isPartOf": "DOE-019-MUNF-COLLECTION1",
             "keyword": [
                 "coal receipts",
                 "electricity generating fuel",
@@ -11433,55 +11425,55 @@
                 "gas receipts",
                 "oil receipts"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2004-12-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_923/form.pdf",
                 "http://www.eia.gov/survey/form/eia_906/instructions_form.pdf",
                 "http://www.eia.gov/survey/form/eia_920/instructions_form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2003-01-01/2003-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Monthly 2003 Utility and Nonutility Fuel Receipts and Fuel Quality Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Monthly 2004 Utility and Nonutility Fuel Receipts and Fuel Quality Data",
-            "description": "Monthly 2004 data on U.S. electric power generation, fuel consumption, stocks, and fuel heat content from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant-level.  Based on Form EIA-906 and Form EIA-920 data. Monthly time series extend back to 2001.",
-            "modified": "2005-11-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-6353362849",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2004-01-01/2004-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-MUNF-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
+            "description": "Monthly 2004 data on U.S. electric power generation, fuel consumption, stocks, and fuel heat content from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant-level.  Based on Form EIA-906 and Form EIA-920 data. Monthly time series extend back to 2001.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/xls/f906920_2004.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2004 Utility and Nonutility Fuel Data",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/xls/f906920_2004.zip"
+                    "title": "2004 Utility and Nonutility Fuel Data"
                 }
             ],
+            "identifier": "DOE-019-6353362849",
+            "isPartOf": "DOE-019-MUNF-COLLECTION1",
             "keyword": [
                 "coal receipts",
                 "electricity generating fuel",
@@ -11490,55 +11482,55 @@
                 "gas receipts",
                 "oil receipts"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2005-11-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_923/form.pdf",
                 "http://www.eia.gov/survey/form/eia_906/instructions_form.pdf",
                 "http://www.eia.gov/survey/form/eia_920/instructions_form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2004-01-01/2004-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Monthly 2004 Utility and Nonutility Fuel Receipts and Fuel Quality Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Monthly 2005 Utility and Nonutility Fuel Receipts and Fuel Quality Data",
-            "description": "Monthly 2005 data on U.S. electric power generation, fuel consumption, stocks, and fuel heat content from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant-level.  Based on Form EIA-906 and Form EIA-920 data. Monthly time series extend back to 2001.",
-            "modified": "2006-10-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-6352362860",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2005-01-01/2005-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-MUNF-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
+            "description": "Monthly 2005 data on U.S. electric power generation, fuel consumption, stocks, and fuel heat content from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant-level.  Based on Form EIA-906 and Form EIA-920 data. Monthly time series extend back to 2001.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/xls/f906920_2005.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2005 Utility and Nonutility Fuel Data",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/xls/f906920_2005.zip"
+                    "title": "2005 Utility and Nonutility Fuel Data"
                 }
             ],
+            "identifier": "DOE-019-6352362860",
+            "isPartOf": "DOE-019-MUNF-COLLECTION1",
             "keyword": [
                 "coal receipts",
                 "electricity generating fuel",
@@ -11547,55 +11539,55 @@
                 "gas receipts",
                 "oil receipts"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2006-10-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_923/form.pdf",
                 "http://www.eia.gov/survey/form/eia_906/instructions_form.pdf",
                 "http://www.eia.gov/survey/form/eia_920/instructions_form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2005-01-01/2005-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Monthly 2005 Utility and Nonutility Fuel Receipts and Fuel Quality Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Monthly 2006 Utility and Nonutility Fuel Receipts and Fuel Quality Data",
-            "description": "Monthly 2006 data on U.S. electric power generation, fuel consumption, stocks, and fuel heat content from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant-level.  Based on Form EIA-906 and Form EIA-920 data. Monthly time series extend back to 2001.",
-            "modified": "2008-07-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-6351583926",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2006-01-01/2006-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-MUNF-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
+            "description": "Monthly 2006 data on U.S. electric power generation, fuel consumption, stocks, and fuel heat content from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant-level.  Based on Form EIA-906 and Form EIA-920 data. Monthly time series extend back to 2001.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/xls/f906920_2006.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2006 Utility and Nonutility Fuel Data",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/xls/f906920_2006.zip"
+                    "title": "2006 Utility and Nonutility Fuel Data"
                 }
             ],
+            "identifier": "DOE-019-6351583926",
+            "isPartOf": "DOE-019-MUNF-COLLECTION1",
             "keyword": [
                 "coal receipts",
                 "electricity generating fuel",
@@ -11604,55 +11596,55 @@
                 "gas receipts",
                 "oil receipts"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2008-07-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_923/form.pdf",
                 "http://www.eia.gov/survey/form/eia_906/instructions_form.pdf",
                 "http://www.eia.gov/survey/form/eia_920/instructions_form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2006-01-01/2006-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Monthly 2006 Utility and Nonutility Fuel Receipts and Fuel Quality Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Monthly 2007 Utility and Nonutility Fuel Receipts and Fuel Quality Data",
-            "description": "Monthly 2007 data on U.S. electric power generation, fuel consumption, stocks, and fuel heat content from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant-level.  Based on Form EIA-906, Form EIA-920, and Form EIA-923 data. Monthly time series extend back to 2001.",
-            "modified": "2009-01-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-6350482940",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2007-01-01/2007-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-MUNF-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
+            "description": "Monthly 2007 data on U.S. electric power generation, fuel consumption, stocks, and fuel heat content from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant-level.  Based on Form EIA-906, Form EIA-920, and Form EIA-923 data. Monthly time series extend back to 2001.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/xls/f906920_2007.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2007 Utility and Nonutility Fuel Data",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/xls/f906920_2007.zip"
+                    "title": "2007 Utility and Nonutility Fuel Data"
                 }
             ],
+            "identifier": "DOE-019-6350482940",
+            "isPartOf": "DOE-019-MUNF-COLLECTION1",
             "keyword": [
                 "coal receipts",
                 "electricity generating fuel",
@@ -11661,55 +11653,55 @@
                 "gas receipts",
                 "oil receipts"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2009-01-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_923/form.pdf",
                 "http://www.eia.gov/survey/form/eia_906/instructions_form.pdf",
                 "http://www.eia.gov/survey/form/eia_920/instructions_form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2007-01-01/2007-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Monthly 2007 Utility and Nonutility Fuel Receipts and Fuel Quality Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Monthly 2008 Utility and Nonutility Fuel Receipts and Fuel Quality Data",
-            "description": "Monthly 2008 data on U.S. electric power generation and fuel consumption, stocks, receipts, quality, costs, fuel supplier, and coal mine source from utility power plants, nonutility power plans, and combined heat and power (CHP) plants. Data organized at the plant-level. Based on Form EIA-923 data. Monthly time series extend back to 2001.",
-            "modified": "2011-04-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-6349374921",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2008-01-01/2008-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-MUNF-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
+            "description": "Monthly 2008 data on U.S. electric power generation and fuel consumption, stocks, receipts, quality, costs, fuel supplier, and coal mine source from utility power plants, nonutility power plans, and combined heat and power (CHP) plants. Data organized at the plant-level. Based on Form EIA-923 data. Monthly time series extend back to 2001.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/xls/f923_2008.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2008 Utility and Nonutility Fuel Data",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/xls/f923_2008.zip"
+                    "title": "2008 Utility and Nonutility Fuel Data"
                 }
             ],
+            "identifier": "DOE-019-6349374921",
+            "isPartOf": "DOE-019-MUNF-COLLECTION1",
             "keyword": [
                 "coal receipts",
                 "electricity generating fuel",
@@ -11718,53 +11710,53 @@
                 "gas receipts",
                 "oil receipts"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2011-04-01",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_923/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2008-01-01/2008-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Monthly 2008 Utility and Nonutility Fuel Receipts and Fuel Quality Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Monthly 2009 Utility and Nonutility Fuel Receipts and Fuel Quality Data",
-            "description": "Monthly 2009 data on U.S. electric power generation and fuel consumption, stocks, receipts, quality, costs, fuel supplier, and coal mine source from utility power plants, nonutility power plans, and combined heat and power (CHP) plants. Data organized at the plant-level. Based on Form EIA-923 data. Monthly time series extend back to 2001.",
-            "modified": "2011-06-07",
             "accessLevel": "public",
-            "identifier": "DOE-019-7856486544",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2009-01-01/2009-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-MUNF-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
+            "description": "Monthly 2009 data on U.S. electric power generation and fuel consumption, stocks, receipts, quality, costs, fuel supplier, and coal mine source from utility power plants, nonutility power plans, and combined heat and power (CHP) plants. Data organized at the plant-level. Based on Form EIA-923 data. Monthly time series extend back to 2001.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/xls/923_2009.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Coal Production 2009",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/xls/923_2009.zip"
+                    "title": "Coal Production 2009"
                 }
             ],
+            "identifier": "DOE-019-7856486544",
+            "isPartOf": "DOE-019-MUNF-COLLECTION1",
             "keyword": [
                 "coal receipts",
                 "electricity generating fuel",
@@ -11773,53 +11765,53 @@
                 "gas receipts",
                 "oil receipts"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2011-06-07",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_923/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2009-01-01/2009-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Monthly 2009 Utility and Nonutility Fuel Receipts and Fuel Quality Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Monthly 2010 Utility and Nonutility Fuel Receipts and Fuel Quality Data",
-            "description": "Monthly 2010 data on U.S. electric power generation and fuel consumption, stocks, receipts, quality, costs, fuel supplier, and coal mine source from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant -level. Based on Form EIA-923 data. Monthly time series extend back to 2001.",
-            "modified": "2011-11-21",
             "accessLevel": "public",
-            "identifier": "DOE-019-6371472956",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2010-01-01/2010-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-MUNF-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
+            "description": "Monthly 2010 data on U.S. electric power generation and fuel consumption, stocks, receipts, quality, costs, fuel supplier, and coal mine source from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant -level. Based on Form EIA-923 data. Monthly time series extend back to 2001.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/xls/f923_2010.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "2010 Utility and Nonutility Fuel Data",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/xls/f923_2010.zip"
+                    "title": "2010 Utility and Nonutility Fuel Data"
                 }
             ],
+            "identifier": "DOE-019-6371472956",
+            "isPartOf": "DOE-019-MUNF-COLLECTION1",
             "keyword": [
                 "coal receipts",
                 "electricity generating fuel",
@@ -11828,53 +11820,53 @@
                 "gas receipts",
                 "oil receipts"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2011-11-21",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_923/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2010-01-01/2010-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Monthly 2010 Utility and Nonutility Fuel Receipts and Fuel Quality Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Monthly 2011 Utility and Nonutility Fuel Receipts and Fuel Quality Data",
-            "description": "Monthly 2011 data on U.S. electric power generation and fuel consumption, stocks, receipts, quality, costs, fuel supplier, and coal mine source from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant-level. Based on Form EIA-923 data. Monthly time series extend back to 2001.",
-            "modified": "2013-12-04",
             "accessLevel": "public",
-            "identifier": "DOE-019-4545454567",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2011-01-01/2011-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-MUNF-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
+            "description": "Monthly 2011 data on U.S. electric power generation and fuel consumption, stocks, receipts, quality, costs, fuel supplier, and coal mine source from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant-level. Based on Form EIA-923 data. Monthly time series extend back to 2001.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/xls/923_2011.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Utility/Nonutility Fuel Receipts 2011",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/xls/923_2011.zip"
+                    "title": "Utility/Nonutility Fuel Receipts 2011"
                 }
             ],
+            "identifier": "DOE-019-4545454567",
+            "isPartOf": "DOE-019-MUNF-COLLECTION1",
             "keyword": [
                 "coal receipts",
                 "electricity generating fuel",
@@ -11883,53 +11875,53 @@
                 "gas receipts",
                 "oil receipts"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
-            "programCode": [
-                "019:022"
-            ],
+            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
             "language": [
                 "en-US"
             ],
-            "references": [
-                "http://www.eia.gov/survey/form/eia_923/form.pdf"
-            ],
-            "theme": [
-                "energy"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Monthly 2012 Utility and Nonutility Fuel Receipts and Fuel Quality Data",
-            "description": "Monthly 2012 data on U.S. electric power generation and fuel consumption, stocks, receipts, quality, costs, fuel supplier, and coal mine source from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant-level.  Based on Form EIA-923 data. Monthly time series extend back to 2001.",
-            "modified": "2013-12-04",
-            "accessLevel": "public",
-            "identifier": "DOE-019-5463727477",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
-            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
             "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2012-01-01/2012-12-31",
+            "modified": "2013-12-04",
+            "programCode": [
+                "019:022"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Energy Information Administration"
             },
-            "isPartOf": "DOE-019-MUNF-COLLECTION1",
+            "references": [
+                "http://www.eia.gov/survey/form/eia_923/form.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "2011-01-01/2011-12-31",
+            "theme": [
+                "energy"
+            ],
+            "title": "Monthly 2011 Utility and Nonutility Fuel Receipts and Fuel Quality Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_923/form.pdf",
+            "description": "Monthly 2012 data on U.S. electric power generation and fuel consumption, stocks, receipts, quality, costs, fuel supplier, and coal mine source from utility power plants, nonutility power plants, and combined heat and power (CHP) plants. Data organized at the plant-level.  Based on Form EIA-923 data. Monthly time series extend back to 2001.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/xls/923_2012.zip",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Utility/Nonutility Fuel Receipts 2012",
-                    "downloadURL": "https://www.eia.gov/electricity/data/eia923/xls/923_2012.zip"
+                    "title": "Utility/Nonutility Fuel Receipts 2012"
                 }
             ],
+            "identifier": "DOE-019-5463727477",
+            "isPartOf": "DOE-019-MUNF-COLLECTION1",
             "keyword": [
                 "coal receipts",
                 "electricity generating fuels",
@@ -11938,53 +11930,53 @@
                 "gas receipts",
                 "oil receipts"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/data/eia923/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2013-12-04",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/form/eia_923/form.pdf"
             ],
+            "spatial": "United States",
+            "temporal": "2012-01-01/2012-12-31",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Monthly 2012 Utility and Nonutility Fuel Receipts and Fuel Quality Data"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Company Level Petroleum Imports 2008",
-            "description": "Monthly 2008 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
-            "modified": "2009-11-01",
             "accessLevel": "public",
-            "identifier": "DOE-019-540445800",
-            "dataQuality": true,
-            "describedBy": "http://www.eia.gov/survey/form/eia_814/form.pdf",
-            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States,",
-            "temporal": "2008-01-01/2008-12-31",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-CLPI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "describedBy": "http://www.eia.gov/survey/form/eia_814/form.pdf",
+            "description": "Monthly 2008 data at the company level on imports of crude oil and/or petroleum products into the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands other U.S. possessions, and Foreign Trade Zones located in the 50 States and DC by each importer of record. Based on Form EIA-814 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2008/data/impa08d.xls",
                     "mediaType": "application/vnd.ms-excel",
-                    "title": "Company Level Petroleum Imports 2008",
-                    "downloadURL": "https://www.eia.gov/petroleum/imports/companylevel/archive/2008/data/impa08d.xls"
+                    "title": "Company Level Petroleum Imports 2008"
                 }
             ],
+            "identifier": "DOE-019-540445800",
+            "isPartOf": "DOE-019-CLPI-COLLECTION1",
             "keyword": [
                 "company-imports",
                 "crude-oil-imports",
@@ -11996,36 +11988,34 @@
                 "petroleum-imports",
                 "residuel-fuel-oil-imports"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "http://www.eia.gov/petroleum/imports/companylevel/",
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2009-11-01",
             "programCode": [
                 "019:022"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Crude Oil Imports Application Programming Interface (API)",
-            "description": "Imports of all grades of crude oil, i.e., heavy sour, heavy sweet, light sour, light sweet,  and medium  crude oil. Monthly or annual data available. Data organized by country origin, by refinery, by refinery state, refinery PADD, by port, by port state, and by port PADD. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-01-29",
-            "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445798",
-            "dataQuality": true,
-            "landingPage": "https://www.eia.gov/developer/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "global",
-            "temporal": "2009/2014",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Energy Information Administration"
             },
+            "spatial": "United States,",
+            "temporal": "2008-01-01/2008-12-31",
+            "title": "Company Level Petroleum Imports 2008"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-COI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Imports of all grades of crude oil, i.e., heavy sour, heavy sweet, light sour, light sweet,  and medium  crude oil. Monthly or annual data available. Data organized by country origin, by refinery, by refinery state, refinery PADD, by port, by port state, and by port PADD. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12035,9 +12025,9 @@
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/beta/petroleum/imports/browser/#/?vs=PET_IMPORTS.WORLD-US-ALL.A",
                     "mediaType": "text/html",
-                    "title": "U.S. Crude Import Tracking Tool",
-                    "downloadURL": "https://www.eia.gov/beta/petroleum/imports/browser/#/?vs=PET_IMPORTS.WORLD-US-ALL.A"
+                    "title": "U.S. Crude Import Tracking Tool"
                 },
                 {
                     "@type": "dcat:Distribution",
@@ -12045,42 +12035,42 @@
                     "title": "API Web Page"
                 }
             ],
+            "identifier": "DOE-019-540445798",
+            "isPartOf": "DOE-019-COI-COLLECTION1",
             "keyword": [
                 "crude-oil-imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "https://www.eia.gov/developer/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-01-29",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "International Energy Statistics",
-            "description": "Country specific data by year, month and quarter. Most data are available back to 1980. Fuel production, consumption, imports, exports, capacity, stocks, emissions, heat contents, and conversion factors; as well as population, as available for all fuels and countries.",
-            "modified": "2020-01-20",
-            "accessLevel": "public",
-            "identifier": "DOE-019-8600473829",
-            "dataQuality": true,
-            "landingPage": "https://www.eia.gov/international/data/world",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "1980/2013",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Energy Information Administration"
             },
+            "spatial": "global",
+            "temporal": "2009/2014",
+            "title": "Crude Oil Imports Application Programming Interface (API)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-IEDAD-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Country specific data by year, month and quarter. Most data are available back to 1980. Fuel production, consumption, imports, exports, capacity, stocks, emissions, heat contents, and conversion factors; as well as population, as available for all fuels and countries.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12088,6 +12078,8 @@
                     "title": "International Energy Statistics"
                 }
             ],
+            "identifier": "DOE-019-8600473829",
+            "isPartOf": "DOE-019-IEDAD-COLLECTION1",
             "keyword": [
                 "CO2 emissions",
                 "DOE",
@@ -12117,42 +12109,40 @@
                 "renewable fuel",
                 "reserves"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "https://www.eia.gov/international/data/world",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2020-01-20",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "spatial": "Global",
+            "temporal": "1980/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "International Energy Statistics"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Crude Oil Imports: By Origin Application Programming Interface (API)",
-            "description": "Imports by origin of all grades of crude oil, i.e., heavy sour, heavy sweet, light sour, light sweet,  and medium  crude oil. View data by country, by world region, or by OPEC and non-OPEC status.  Data in monthly or annual time series.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-31",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445656",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/petroleum/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "2009/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-COI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Imports by origin of all grades of crude oil, i.e., heavy sour, heavy sweet, light sour, light sweet,  and medium  crude oil. View data by country, by world region, or by OPEC and non-OPEC status.  Data in monthly or annual time series.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12171,6 +12161,8 @@
                     "title": "U.S. Crude Import Tracking Tool"
                 }
             ],
+            "identifier": "DOE-019-540445656",
+            "isPartOf": "DOE-019-COI-COLLECTION1",
             "keyword": [
                 "API",
                 "OPEC",
@@ -12179,39 +12171,37 @@
                 "petroleum",
                 "petroleum imports"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "http://www.eia.gov/petroleum/",
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-31",
             "programCode": [
                 "019:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "spatial": "Global",
+            "temporal": "2009/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Crude Oil Imports: By Origin Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Crude Oil Imports: By Refinery Application Programming Interface (API)",
-            "description": "U.S. refinery imports of all grades of crude oil, i.e., heavy sour, heavy sweet, light sour, light sweet, and medium crude oil.  Data in monthly or annual time series.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-31",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445657",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/petroleum/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "2009/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-COI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "U.S. refinery imports of all grades of crude oil, i.e., heavy sour, heavy sweet, light sour, light sweet, and medium crude oil.  Data in monthly or annual time series.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12231,48 +12221,48 @@
                     "title": "U.S. Crude Import Tracking Tool"
                 }
             ],
+            "identifier": "DOE-019-540445657",
+            "isPartOf": "DOE-019-COI-COLLECTION1",
             "keyword": [
                 "API",
                 "crude oil imports",
                 "petroleum imports",
                 "refinery"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-31",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "spatial": "Global",
+            "temporal": "2009/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Crude Oil Imports: By Refinery Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Crude Oil Imports: By Refinery State Application Programming Interface (API)",
-            "description": "U.S. refinery imports of all grades of crude oil, i.e., heavy sour, heavy sweet, light sour, light sweet, and medium crude oil.  Data organized by refinery state. Data in monthly or annual time series.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-31",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445658",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/petroleum/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2009/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-COI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "U.S. refinery imports of all grades of crude oil, i.e., heavy sour, heavy sweet, light sour, light sweet, and medium crude oil.  Data organized by refinery state. Data in monthly or annual time series.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12291,45 +12281,45 @@
                     "title": "U.S. Crude Import Tracking Tool"
                 }
             ],
+            "identifier": "DOE-019-540445658",
+            "isPartOf": "DOE-019-COI-COLLECTION1",
             "keyword": [
                 "API",
                 "crude oil imports",
-                "petroleum imports",
-                "refinery"
-            ],
-            "bureauCode": [
-                "019:20"
-            ],
-            "programCode": [
-                "019:022"
-            ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Crude Oil Imports: By Refinery PADD Application Programming Interface (API)",
-            "description": "U.S. refinery imports of all grades of crude oil, i.e., heavy sour, heavy sweet, light sour, light sweet, and medium crude oil.  Data organized by refinery PADD, i.e., East Coast, Midwest, Gulf Coast, Rocky Mountain, West Coast, and Territories. Data in monthly or annual time series.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-31",
-            "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445659",
-            "dataQuality": true,
+                "petroleum imports",
+                "refinery"
+            ],
             "landingPage": "http://www.eia.gov/petroleum/",
+            "language": [
+                "en-US"
+            ],
             "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2009/2015",
+            "modified": "2015-07-31",
+            "programCode": [
+                "019:022"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Energy Information Administration"
             },
+            "spatial": "United States",
+            "temporal": "2009/2015",
+            "title": "Crude Oil Imports: By Refinery State Application Programming Interface (API)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-COI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "U.S. refinery imports of all grades of crude oil, i.e., heavy sour, heavy sweet, light sour, light sweet, and medium crude oil.  Data organized by refinery PADD, i.e., East Coast, Midwest, Gulf Coast, Rocky Mountain, West Coast, and Territories. Data in monthly or annual time series.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12348,47 +12338,47 @@
                     "title": "U.S. Crude Import Tracking Tool"
                 }
             ],
+            "identifier": "DOE-019-540445659",
+            "isPartOf": "DOE-019-COI-COLLECTION1",
             "keyword": [
                 "API",
                 "crude oil imports",
                 "petroleum imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-31",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "spatial": "United States",
+            "temporal": "2009/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Crude Oil Imports: By Refinery PADD Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Crude Oil Imports: By Port Application Programming Interface (API)",
-            "description": "U.S. imports of all grades of crude oil, i.e., heavy sour, heavy sweet, light sour, light sweet,  and medium  crude oil.  Data organized by ports of entry. Data in monthly or annual time series.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-31",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445660",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/petroleum/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2009/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-COI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "U.S. imports of all grades of crude oil, i.e., heavy sour, heavy sweet, light sour, light sweet,  and medium  crude oil.  Data organized by ports of entry. Data in monthly or annual time series.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12408,44 +12398,44 @@
                     "title": "Crude Oil Imports: By Port API"
                 }
             ],
+            "identifier": "DOE-019-540445660",
+            "isPartOf": "DOE-019-COI-COLLECTION1",
             "keyword": [
                 "API",
                 "crude oil imports",
                 "petroleum imports"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "http://www.eia.gov/petroleum/",
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-31",
             "programCode": [
                 "019:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "spatial": "United States",
+            "temporal": "2009/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Crude Oil Imports: By Port Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Crude Oil Imports: By Port PADD Application Programming Interface (API)",
-            "description": "U.S. refinery imports of all grades of crude oil, i.e., heavy sour, heavy sweet, light sour, light sweet,  and medium  crude oil.  Data organized by port of entry PADD, i.e., East Coast, Midwest, Gulf Coast, Rocky Mountain, West Coast, and Territories. Data in monthly or annual time series.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-31",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445662",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/petroleum/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2009/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-COI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "U.S. refinery imports of all grades of crude oil, i.e., heavy sour, heavy sweet, light sour, light sweet,  and medium  crude oil.  Data organized by port of entry PADD, i.e., East Coast, Midwest, Gulf Coast, Rocky Mountain, West Coast, and Territories. Data in monthly or annual time series.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12464,49 +12454,49 @@
                     "title": "Crude Oil Imports: By Port PADD API"
                 }
             ],
+            "identifier": "DOE-019-540445662",
+            "isPartOf": "DOE-019-COI-COLLECTION1",
             "keyword": [
                 "AAPI",
                 "crude oil imports",
                 "petroleum imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-31",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=petroleum"
             ],
+            "spatial": "United States",
+            "temporal": "2009/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Crude Oil Imports: By Port PADD Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Export Price Application Programming Interface (API)",
-            "description": "Data on coal, coke, metallurgical coal, and steam coal export prices in $/short ton. Data organized by country and by terminal. Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-08",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445689",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "2000/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on coal, coke, metallurgical coal, and steam coal export prices in $/short ton. Data organized by country and by terminal. Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12521,57 +12511,56 @@
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/beta/coal/data/browser/",
                     "mediaType": "text/html",
-                    "title": "Coal Data Browser",
-                    "downloadURL": "https://www.eia.gov/beta/coal/data/browser/"
+                    "title": "Coal Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445689",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
                 "coal export price",
                 "coal exports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-08",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "Global",
+            "temporal": "2000/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Export Price Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Import Quantity Application Programming Interface (API)",
-            "description": "Data on coal, coke, metallurgical coal, and steam coal import quantities in short ton. Data organized by country and by terminal. Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-08",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445690",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "rights": "The EIA API is offered as a free public service, although registration is required.",
-            "spatial": "Global",
-            "temporal": "2000/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on coal, coke, metallurgical coal, and steam coal import quantities in short ton. Data organized by country and by terminal. Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12590,48 +12579,49 @@
                     "title": "Coal Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445690",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
                 "coal imports"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "http://www.eia.gov/coal/",
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-08",
             "programCode": [
                 "019:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "rights": "The EIA API is offered as a free public service, although registration is required.",
+            "spatial": "Global",
+            "temporal": "2000/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Import Quantity Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Import Price Application Programming Interface (API)",
-            "description": "Data on coal, coke, metallurgical coal, and steam coal imports price in $/short ton. Data organized by country and by terminal. Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-08",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445691",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "2002/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on coal, coke, metallurgical coal, and steam coal imports price in $/short ton. Data organized by country and by terminal. Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12650,52 +12640,52 @@
                     "title": "Coal Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445691",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
                 "coal imports",
                 "coal prices"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-08",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "Global",
+            "temporal": "2002/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Import Price Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Crude Oil Imports: By Port State Application Programming Interface (API)",
-            "description": "U.S. imports of all grades of crude oil, i.e., heavy sour, heavy sweet, light sour, light sweet,  and medium  crude oil.  Data organized by port of entry state. Data in monthly or annual time series.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-31",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445661",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/petroleum/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2009/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-COI-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "U.S. imports of all grades of crude oil, i.e., heavy sour, heavy sweet, light sour, light sweet,  and medium  crude oil.  Data organized by port of entry state. Data in monthly or annual time series.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12714,46 +12704,47 @@
                     "title": "Crude Oil Imports: By Port State API"
                 }
             ],
+            "identifier": "DOE-019-540445661",
+            "isPartOf": "DOE-019-COI-COLLECTION1",
             "keyword": [
                 "API",
                 "crude oil imports",
                 "petroleum imports"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/petroleum/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-31",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
+            "spatial": "United States",
+            "temporal": "2009/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Crude Oil Imports: By Port State Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Electricity Data: Net Generation from Electricity Plants Application Programming Interface (API)",
-            "description": "This API provides data on U.S. electricity generation by fuel type, i.e., coal, petroleum, natural gas, nuclear, hydroelectric, wind, solar, geothermal, and wood. Data also organized by sector, i.e., electric power, electric utility, commerical and industrial. Annual, quarterly, and monthly data available. Based on Form EIA-906, Form EIA-920, and Form EIA-923 data.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445663",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/electricity/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides data on U.S. electricity generation by fuel type, i.e., coal, petroleum, natural gas, nuclear, hydroelectric, wind, solar, geothermal, and wood. Data also organized by sector, i.e., electric power, electric utility, commerical and industrial. Annual, quarterly, and monthly data available. Based on Form EIA-906, Form EIA-920, and Form EIA-923 data.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12772,52 +12763,51 @@
                     "title": "Electricity Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445663",
             "keyword": [
                 "API",
                 "electricity generation",
                 "electricity plants",
                 "net generation"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=electricity",
                 "http://www.eia.gov/survey/#eia-923"
             ],
+            "spatial": "United States",
+            "temporal": "2001/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Electricity Data: Net Generation from Electricity Plants Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Electricity Data: Total Consumption Application Programming Interface (API)",
-            "description": "This API provides data on U.S. total electricity consumption by fuel type, i.e., coal, petroleum liquids, petroleum coke, and  natural gas. Data also organized by sector, i.e., electric power, electric utility, commerical and industrial. Annual, quarterly, and monthly data available. Based on Form EIA-906, Form EIA-920, and Form EIA-923 data.  Users of the EIA API are required to obtain an API Key via this registration form:  http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445664",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/electricity/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-EDC-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides data on U.S. total electricity consumption by fuel type, i.e., coal, petroleum liquids, petroleum coke, and  natural gas. Data also organized by sector, i.e., electric power, electric utility, commerical and industrial. Annual, quarterly, and monthly data available. Based on Form EIA-906, Form EIA-920, and Form EIA-923 data.  Users of the EIA API are required to obtain an API Key via this registration form:  http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12836,51 +12826,51 @@
                     "title": "Electricity Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445664",
+            "isPartOf": "DOE-019-EDC-COLLECTION1",
             "keyword": [
                 "API",
                 "electricity consumption",
                 "total consumption"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=electricity",
                 "http://www.eia.gov/survey/#eia-923"
             ],
+            "spatial": "United States",
+            "temporal": "2001/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Electricity Data: Total Consumption Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Electricity Data: Total Consumption (Btu) Application Programming Interface (API)",
-            "description": "This API provides data on U.S. total consumption in Btu by fuel type, i.e., coal, petroleum liquids, petroleum coke, and  natural gas. Data also organized by sector, i.e., electric power, electric utility, commercial and industrial. Annual, quarterly, and monthly data available. Based on Form EIA-906, Form EIA-920, and Form EIA-923 data.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445665",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/electricity/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-EDC-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides data on U.S. total consumption in Btu by fuel type, i.e., coal, petroleum liquids, petroleum coke, and  natural gas. Data also organized by sector, i.e., electric power, electric utility, commercial and industrial. Annual, quarterly, and monthly data available. Based on Form EIA-906, Form EIA-920, and Form EIA-923 data.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12900,52 +12890,52 @@
                     "title": "Electricity Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445665",
+            "isPartOf": "DOE-019-EDC-COLLECTION1",
             "keyword": [
                 "API",
                 "Btu",
                 "electricity consumption",
                 "total consumption"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=electricity",
                 "http://www.eia.gov/survey/#eia-923"
             ],
+            "spatial": "United States",
+            "temporal": "2001/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Electricity Data: Total Consumption (Btu) Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Electricity Data: Consumption for Electricity Generation Application Programming Interface (API)",
-            "description": "This API provides  data on U.S. consumption for electricity generation. Data organized by fuel type, i.e., coal, petroleum liquids, petroleum coke, and  natural gas. Data also organized by sector, i.e., electric power, electric utility, commercial and industrial. Annual, quarterly, and monthly data available. Based on Form EIA-906, Form EIA-920, and Form EIA-923 data.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445666",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/electricity/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-EDC-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides  data on U.S. consumption for electricity generation. Data organized by fuel type, i.e., coal, petroleum liquids, petroleum coke, and  natural gas. Data also organized by sector, i.e., electric power, electric utility, commercial and industrial. Annual, quarterly, and monthly data available. Based on Form EIA-906, Form EIA-920, and Form EIA-923 data.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -12964,51 +12954,51 @@
                     "title": "Consumption for Electricity Generation API"
                 }
             ],
+            "identifier": "DOE-019-540445666",
+            "isPartOf": "DOE-019-EDC-COLLECTION1",
             "keyword": [
                 "API",
                 "conusumption",
                 "electricity generation"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=electricity",
                 "http://www.eia.gov/survey/#eia-923"
             ],
+            "spatial": "United States",
+            "temporal": "2001/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Electricity Data: Consumption for Electricity Generation Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Electricity Data: Consumption for Electricity Generation (Btu) Application Programming Interface (API)",
-            "description": "This API provides data on U.S. consumption for electricity generation in Btu. Data organized by fuel type, i.e., coal, petroleum liquids, petroleum coke, and  natural gas. Data also organized by sector, i.e., electric power, electric utility, commercial and industrial. Annual, quarterly, and monthly data available. Based on Form EIA-906, Form EIA-920, and Form EIA-923 data.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445667",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/electricity/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-EDC-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides data on U.S. consumption for electricity generation in Btu. Data organized by fuel type, i.e., coal, petroleum liquids, petroleum coke, and  natural gas. Data also organized by sector, i.e., electric power, electric utility, commercial and industrial. Annual, quarterly, and monthly data available. Based on Form EIA-906, Form EIA-920, and Form EIA-923 data.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13027,51 +13017,51 @@
                     "title": "Electricity Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445667",
+            "isPartOf": "DOE-019-EDC-COLLECTION1",
             "keyword": [
                 "API",
                 "conusumption",
                 "electricity generation"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=electricity",
                 "http://www.eia.gov/survey/#eia-923"
             ],
+            "spatial": "United States",
+            "temporal": "2001/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Electricity Data: Consumption for Electricity Generation (Btu) Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Electricity Data: Consumption for Useful Thermal Output Application Programming Interface (API)",
-            "description": "This API provides  data on U.S. consumption for useful thermal output. Data organized by fuel type, i.e., coal, petroleum liquids, petroleum coke, and  natural gas. Data also organized by sector, i.e., electric power, electric utility, commerical and industrial. Annual, quarterly, and monthly data available. Based on Form EIA-906, Form EIA-920, and Form EIA-923 data.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445668",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/electricity/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-EDC-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides  data on U.S. consumption for useful thermal output. Data organized by fuel type, i.e., coal, petroleum liquids, petroleum coke, and  natural gas. Data also organized by sector, i.e., electric power, electric utility, commerical and industrial. Annual, quarterly, and monthly data available. Based on Form EIA-906, Form EIA-920, and Form EIA-923 data.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13090,50 +13080,51 @@
                     "title": "Electricity Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445668",
+            "isPartOf": "DOE-019-EDC-COLLECTION1",
             "keyword": [
                 "API",
                 "electricity consumption",
                 "thermal output"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=electricity",
                 "http://www.eia.gov/survey/#eia-923"
             ],
+            "spatial": "United States",
+            "temporal": "2001/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Electricity Data: Consumption for Useful Thermal Output Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Electricity Data: Plant Level Data Application Programming Interface (API)",
-            "description": "This API provides data on electric fuel consumption, fuel consumption, and net generation at the plant level.  Annual, quarterly, and monthly data available. Based on Form EIA-906, Form EIA-920, and Form EIA-923 data.",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445670",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/electricity/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides data on electric fuel consumption, fuel consumption, and net generation at the plant level.  Annual, quarterly, and monthly data available. Based on Form EIA-906, Form EIA-920, and Form EIA-923 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13152,52 +13143,51 @@
                     "title": "Electricity Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445670",
             "keyword": [
                 "API",
                 "electricity generation",
                 "fuel consumption",
                 "power plants"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=electricity",
                 "http://www.eia.gov/survey/#eia-923"
             ],
+            "spatial": "United States",
+            "temporal": "2001/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Electricity Data: Plant Level Data Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Electricity Data: Retail Sales of Electricity Application Programming Interface (API)",
-            "description": "This API provides  data on retail sales of electricity by major end-use sectors, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 and Form EIA-861 data. Annual, quarterly, and monthly data available.",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445671",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/electricity/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-EDRP-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides  data on retail sales of electricity by major end-use sectors, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 and Form EIA-861 data. Annual, quarterly, and monthly data available.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13216,51 +13206,52 @@
                     "title": "Electricity Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445671",
+            "isPartOf": "DOE-019-EDRP-COLLECTION1",
             "keyword": [
                 "API",
                 "electricity sales",
                 "retail sales"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/#eia-826",
                 "http://www.eia.gov/tools/glossary/index.cfm?id=electricity",
                 "http://www.eia.gov/survey/#eia-861"
             ],
+            "spatial": "United States",
+            "temporal": "2001/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Electricity Data: Retail Sales of Electricity Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Electricity Data: Average Retail Price of Electricity Application Programming Interface (API)",
-            "description": "This API provides data on average retail price of electricity by major end-use sectors, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 and Form EIA-861 data. Annual, quarterly, and monthly data available.",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445673",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/electricity/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides data on average retail price of electricity by major end-use sectors, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 and Form EIA-861 data. Annual, quarterly, and monthly data available.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13279,52 +13270,51 @@
                     "title": "Electricity Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445673",
             "keyword": [
                 "API",
                 "electricity prices",
                 "retail price"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/#eia-826",
                 "http://www.eia.gov/tools/glossary/index.cfm?id=electricity",
                 "http://www.eia.gov/survey/#eia-861"
             ],
+            "spatial": "United States",
+            "temporal": "2001/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Electricity Data: Average Retail Price of Electricity Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Electricity Data: Revenue from Retail Sales of Electricity Application Programming Interface (API)",
-            "description": "This API provides data on revenue from retail sales of electricity by major end-use sectors, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 and Form EIA- 861 data. Annual, quarterly, and monthly data available.",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445672",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/electricity/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-EDRP-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides data on revenue from retail sales of electricity by major end-use sectors, i.e., residential, commercial, industrial, and transportation. Based on Form EIA-826 and Form EIA- 861 data. Annual, quarterly, and monthly data available.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13343,53 +13333,53 @@
                     "title": "Electricity Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445672",
+            "isPartOf": "DOE-019-EDRP-COLLECTION1",
             "keyword": [
                 "API",
                 "electricity revenue",
                 "electricity sales",
                 "retail price"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/#eia-826",
                 "http://www.eia.gov/tools/glossary/index.cfm?id=electricity",
                 "http://www.eia.gov/survey/#eia-861"
             ],
+            "spatial": "United States",
+            "temporal": "2001/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Electricity Data: Revenue from Retail Sales of Electricity Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Electricity Data: Consumption for Useful Thermal Output (Btu) Application Programming Interface (API)",
-            "description": "This API provides  data on U.S. consumption for useful thermal output in British thermal units (Btu). Data organized by fuel type, i.e., coal, petroleum liquids, petroleum coke, and  natural gas. Data also organized by sector, i.e., electric power, electric utility, commercial and industrial. Annual, quarterly, and monthly data available. Based on Form EIA-906, Form EIA-920, and Form EIA-923 data.",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445669",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/electricity/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-EDC-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides  data on U.S. consumption for useful thermal output in British thermal units (Btu). Data organized by fuel type, i.e., coal, petroleum liquids, petroleum coke, and  natural gas. Data also organized by sector, i.e., electric power, electric utility, commercial and industrial. Annual, quarterly, and monthly data available. Based on Form EIA-906, Form EIA-920, and Form EIA-923 data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13408,51 +13398,51 @@
                     "title": "Electricity Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445669",
+            "isPartOf": "DOE-019-EDC-COLLECTION1",
             "keyword": [
                 "API",
                 "electricity consumption",
                 "thermal output"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=electricity",
                 "http://www.eia.gov/survey/#eia-923"
             ],
+            "spatial": "United States",
+            "temporal": "2001/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Electricity Data: Consumption for Useful Thermal Output (Btu) Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Electricity Data: Fossil-fuel Stocks for Electricity Generation Application Programming Interface (API)",
-            "description": "This API provides data on fossil fuel stocks for electricity generation. Data organized by fuel type, i.e., coal, bituminous coal, subbituminous coal, lignite coal, petroleum liquids, and petroleum coke. Also by sector, i.e., electric power, electric utility, and independent power producers. Annual, quarterly, and monthly data available.  Based on Form EIA-423 and Form EIA-923 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445674",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/electricity/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2008/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-EDFF-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides data on fossil fuel stocks for electricity generation. Data organized by fuel type, i.e., coal, bituminous coal, subbituminous coal, lignite coal, petroleum liquids, and petroleum coke. Also by sector, i.e., electric power, electric utility, and independent power producers. Annual, quarterly, and monthly data available.  Based on Form EIA-423 and Form EIA-923 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13471,6 +13461,8 @@
                     "title": "Electricity Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445674",
+            "isPartOf": "DOE-019-EDFF-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
@@ -13479,48 +13471,45 @@
                 "petroleum coke",
                 "petroleum liquids"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/#eia-423",
                 "http://www.eia.gov/tools/glossary/index.cfm?id=electricity",
                 "http://www.eia.gov/survey/#eia-923"
             ],
+            "spatial": "United States",
+            "temporal": "2008/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Electricity Data: Fossil-fuel Stocks for Electricity Generation Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Electricity Data: Quality Fossil Fuels in Electricity Generation: Ash Content Application Programming Interface (API)",
-            "description": "This API provides data on ash content in fossil fuels. Data organized by fuel type, i.e., coal, bituminous coal, subbituminous coal, lignite coal, and petroleum coke. Also by sector, i.e., electric power, electric utility, independent power producers, commercial, and industrial. Annual, quarterly, and monthly data available.  Based on Form EIA-423 and Form EIA-923 data.   Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-54044567680",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/electricity/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "rights": "The EIA API is offered as a free public service, although registration is required.",
-            "spatial": "United States",
-            "temporal": "2008/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-EDFF-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides data on ash content in fossil fuels. Data organized by fuel type, i.e., coal, bituminous coal, subbituminous coal, lignite coal, and petroleum coke. Also by sector, i.e., electric power, electric utility, independent power producers, commercial, and industrial. Annual, quarterly, and monthly data available.  Based on Form EIA-423 and Form EIA-923 data.   Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13539,6 +13528,8 @@
                     "title": "Quality of Fossil Fuels in Electricity Generation: Ash Content API"
                 }
             ],
+            "identifier": "DOE-019-54044567680",
+            "isPartOf": "DOE-019-EDFF-COLLECTION1",
             "keyword": [
                 "API",
                 "ash content",
@@ -13548,47 +13539,46 @@
                 "petroleum coke",
                 "petroleum liquids"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/#eia-423",
                 "http://www.eia.gov/tools/glossary/index.cfm?id=electricity",
                 "http://www.eia.gov/survey/#eia-923"
             ],
+            "rights": "The EIA API is offered as a free public service, although registration is required.",
+            "spatial": "United States",
+            "temporal": "2008/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Electricity Data: Quality Fossil Fuels in Electricity Generation: Ash Content Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Market Sales Application Programming Interface (API)",
-            "description": "Data on the amount of coal sold in the open market and captive market. Annual data available. Based on Form EIA-7 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-04-23",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445703",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on the amount of coal sold in the open market and captive market. Annual data available. Based on Form EIA-7 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13607,6 +13597,8 @@
                     "title": "Coal Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445703",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "captive market",
@@ -13614,46 +13606,44 @@
                 "coal market sales",
                 "open market"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
-            "programCode": [
-                "019:022"
-            ],
+            "landingPage": "http://www.eia.gov/coal/",
             "language": [
                 "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-04-23",
+            "programCode": [
+                "019:022"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "United States",
+            "temporal": "2001/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Market Sales Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Heat Content Application Programming Interface (API)",
-            "description": "Data on the heat content of coal. Data organized by electric power sector, i.e., electric utility, independent power producers, commercial and institutional, and coke plants. Quarterly and annual data available. Based on Form EIA-3 and Form EIA-923 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445704",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2008/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on the heat content of coal. Data organized by electric power sector, i.e., electric utility, independent power producers, commercial and institutional, and coke plants. Quarterly and annual data available. Based on Form EIA-3 and Form EIA-923 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13672,51 +13662,51 @@
                     "title": "Coal Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445704",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
                 "coal heat content"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "United States",
+            "temporal": "2008/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Heat Content Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Market Average Price Application Programming Interface (API)",
-            "description": "Data on the average price of coal sold in the open market and captive market. Annual data available. Based on Form EIA-7 data.Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-04-23",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445705",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on the average price of coal sold in the open market and captive market. Annual data available. Based on Form EIA-7 data.Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13731,57 +13721,57 @@
                 },
                 {
                     "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.eia.gov/beta/coal/data/browser/",
                     "mediaType": "text/html",
-                    "title": "Coal Data Browser",
-                    "downloadURL": "https://www.eia.gov/beta/coal/data/browser/"
+                    "title": "Coal Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445705",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
                 "coal market",
                 "coal prices"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-04-23",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "United States",
+            "temporal": "2001/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Market Average Price Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Average Price by Rank Application Programming Interface (API)",
-            "description": "Data on the average price of coal by rank, i.e., lignite, anthracite, subbituminous, and bituminous coal. Annual data available. Based on Form EIA-7 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-04-23",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445706",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on the average price of coal by rank, i.e., lignite, anthracite, subbituminous, and bituminous coal. Annual data available. Based on Form EIA-7 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13800,51 +13790,51 @@
                     "title": "Coal Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445706",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
                 "coal price"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-04-23",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "United States",
+            "temporal": "2001/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Average Price by Rank Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Productive Capacity Application Programming Interface (API)",
-            "description": "Data on the maximum amount of coal that a mining operation can produce or process.  Annual data available. Based on Form EIA-7 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-04-23",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445707",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on the maximum amount of coal that a mining operation can produce or process.  Annual data available. Based on Form EIA-7 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13863,52 +13853,52 @@
                     "title": "Coal Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445707",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
                 "coal production",
                 "coal productive capacity"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-04-23",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "United States",
+            "temporal": "2001/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Productive Capacity Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Recoverable Reserves at Producing Mines Application Programming Interface (API)",
-            "description": "Data on estimated coal reserves based on a demonstrated reserve base, adjusted for assumed accessibility and recovery factors, and does not include any specific economic feasibility criteria. Annual data available. Based on Form EIA-7 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-04-23",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445708",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on estimated coal reserves based on a demonstrated reserve base, adjusted for assumed accessibility and recovery factors, and does not include any specific economic feasibility criteria. Annual data available. Based on Form EIA-7 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13927,52 +13917,52 @@
                     "title": "Coal Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445708",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
                 "coal mines",
                 "coal reserves"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-04-23",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "United States",
+            "temporal": "2001/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Recoverable Reserves at Producing Mines Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Coal Mine Ending Stocks Application Programming Interface (API)",
-            "description": "Data on coal mine ending stocks. Annual data available. Based on Form EIA-7 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-04-23",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445709",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2008/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on coal mine ending stocks. Annual data available. Based on Form EIA-7 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -13991,52 +13981,52 @@
                     "title": "Coal Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445709",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
                 "coal mine",
                 "coal stocks"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-04-23",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "United States",
+            "temporal": "2008/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Coal Mine Ending Stocks Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Coal shipments to the electric power sector: quantity, by plant state Application Programming Interface (API)",
-            "description": "Data on coal shipments to the electric power sector. Data organized by plant state and by coal, i.e., lignite, anthracite, subbituminous, bituminous, waste coal, and synfuel coal. Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445710",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2008/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on coal shipments to the electric power sector. Data organized by plant state and by coal, i.e., lignite, anthracite, subbituminous, bituminous, waste coal, and synfuel coal. Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14055,6 +14045,8 @@
                     "title": "Coal Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445710",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
@@ -14062,46 +14054,44 @@
                 "coal shipments",
                 "electric power sector"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "United States",
+            "temporal": "2008/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Coal shipments to the electric power sector: quantity, by plant state Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Coal shipments to the electric power sector: price, by plant state Application Programming Interface (API)",
-            "description": "Data on the price of coal that is shipped to the electric power sector. Data organized by plant state and by coal, i.e., lignite, anthracite, subbituminous, bituminous, waste coal, and synfuel coal. Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445711",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2008/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on the price of coal that is shipped to the electric power sector. Data organized by plant state and by coal, i.e., lignite, anthracite, subbituminous, bituminous, waste coal, and synfuel coal. Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14121,6 +14111,8 @@
                     "title": "Coal Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445711",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
@@ -14128,46 +14120,44 @@
                 "coal shipments",
                 "electric power sector"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "United States",
+            "temporal": "2008/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Coal shipments to the electric power sector: price, by plant state Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Coal shipments to the electric power sector: heat content, by plant state Application Programming Interface (API)",
-            "description": "Data on the heat content of coal that is shipped to the electric power sector. Data organized by plant state and by coal, i.e., lignite, anthracite, subbituminous, bituminous, waste coal, and synfuel coal. Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445712",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2008/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on the heat content of coal that is shipped to the electric power sector. Data organized by plant state and by coal, i.e., lignite, anthracite, subbituminous, bituminous, waste coal, and synfuel coal. Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14186,6 +14176,8 @@
                     "title": "Coal shipments to the electric power sector: heat content, by plant state API"
                 }
             ],
+            "identifier": "DOE-019-540445712",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
@@ -14194,46 +14186,44 @@
                 "electric power sector",
                 "heat content"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "United States",
+            "temporal": "2008/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Coal shipments to the electric power sector: heat content, by plant state Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Coal shipments to the electric power sector: ash content, by plant state Application Programming Interface (API)",
-            "description": "Data on the ash content of coal that is shipped to the electric power sector. Data organized by plant state and by coal, i.e., lignite, anthracite, subbituminous, bituminous, waste coal, and synfuel coal. Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445713",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2008/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on the ash content of coal that is shipped to the electric power sector. Data organized by plant state and by coal, i.e., lignite, anthracite, subbituminous, bituminous, waste coal, and synfuel coal. Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14252,6 +14242,8 @@
                     "title": "Coal Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445713",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "ash content",
@@ -14260,45 +14252,43 @@
                 "coal shipments",
                 "electric power sector"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "United States",
+            "temporal": "2008/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Coal shipments to the electric power sector: ash content, by plant state Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Coal shipments to the electric power sector: sulfur content, by plant state Application Programming Interface (API)",
-            "description": "Data on the sulfur content of coal that is shipped to the electric power sector. Data organized by plant state and by coal, i.e., lignite, anthracite, subbituminous, bituminous, waste coal, and synfuel coal. Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445714",
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2008/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "description": "Data on the sulfur content of coal that is shipped to the electric power sector. Data organized by plant state and by coal, i.e., lignite, anthracite, subbituminous, bituminous, waste coal, and synfuel coal. Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14317,6 +14307,8 @@
                     "title": "Coal shipments to the electric power sector: sulfur content, by plant state API"
                 }
             ],
+            "identifier": "DOE-019-540445714",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
@@ -14324,46 +14316,44 @@
                 "electric power sector",
                 "sulfur content"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "United States",
+            "temporal": "2008/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Coal shipments to the electric power sector: sulfur content, by plant state Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Coal shipments to the electric power sector: price, by mine state Application Programming Interface (API)",
-            "description": "Data on the price of coal that is shipped to the electric power sector. Data organized by mine state and by coal (i.e., lignite, anthracite, subbituminous, bituminous, waste coal, and synfuel coal). Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445715",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2008/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on the price of coal that is shipped to the electric power sector. Data organized by mine state and by coal (i.e., lignite, anthracite, subbituminous, bituminous, waste coal, and synfuel coal). Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14382,6 +14372,8 @@
                     "title": "Coal shipments to the electric power sector: price, by mine state API"
                 }
             ],
+            "identifier": "DOE-019-540445715",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
@@ -14389,44 +14381,43 @@
                 "coal shipments",
                 "electric power sector"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "United States",
+            "temporal": "2008/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Coal shipments to the electric power sector: price, by mine state Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Short-Term Energy Outlook: U.S. Renewable Energy Application Programming Interface (API)",
-            "description": "This API provides data back to 1990 and projections annually, monthly, and quarterly for 18 months.  Summarizes the outlook for renewable energy consumption and renewable generation capacity. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445735",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/forecasts/steo/index.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1990/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides data back to 1990 and projections annually, monthly, and quarterly for 18 months.  Summarizes the outlook for renewable energy consumption and renewable generation capacity. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14445,6 +14436,7 @@
                     "title": "STEO Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445735",
             "keyword": [
                 "STEO",
                 "forecasts",
@@ -14453,42 +14445,40 @@
                 "renewable energy consumption",
                 "renewable energy generation"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "http://www.eia.gov/forecasts/steo/index.cfm",
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/"
             ],
+            "spatial": "United States",
+            "temporal": "1990/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Short-Term Energy Outlook: U.S. Renewable Energy Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Electricity Data: Receipts of Fossil Fuels (Btu) Application Programming Interface (API)",
-            "description": "This API provides data on receipts of fossil fuels by electricity plants in British thermal units (Btu). Data organized by fuel type, i.e., coal, bituminous coal, subbituminous coal, lignite coal, petroleum liquids, and petroleum coke. Also by sector, i.e., electric power, electric utility, and independent power producers. Annual, quarterly, and monthly data available.  Based on Form EIA-423 and Form EIA-923 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445676",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/electricity/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2008/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-EDFF-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides data on receipts of fossil fuels by electricity plants in British thermal units (Btu). Data organized by fuel type, i.e., coal, bituminous coal, subbituminous coal, lignite coal, petroleum liquids, and petroleum coke. Also by sector, i.e., electric power, electric utility, and independent power producers. Annual, quarterly, and monthly data available.  Based on Form EIA-423 and Form EIA-923 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14507,6 +14497,8 @@
                     "title": "Electricity Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445676",
+            "isPartOf": "DOE-019-EDFF-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
@@ -14515,48 +14507,45 @@
                 "petroleum coke",
                 "petroleum liquids"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/#eia-423",
                 "http://www.eia.gov/tools/glossary/index.cfm?id=electricity",
                 "http://www.eia.gov/survey/#eia-923"
             ],
+            "spatial": "United States",
+            "temporal": "2008/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Electricity Data: Receipts of Fossil Fuels (Btu) Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Electricity Data: Average Cost of Fossil Fuels for Electricity Generation Application Programming Interface (API)",
-            "description": "This API provides data on the average cost of fossil fuels. Data organized by fuel type, i.e., coal, bituminous coal, subbituminous coal, lignite coal, petroleum liquids, petroleum coke, and natural gas. Also by sector, i.e., electric power, electric utility, independent power producers, commercial, and industrial. Annual, quarterly, and monthly data available.  Based on Form EIA-423 and Form EIA-923 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-54044567677",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/electricity/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "rights": "The EIA API is offered as a free public service, although registration is required.",
-            "spatial": "United States",
-            "temporal": "2008/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-EDFF-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides data on the average cost of fossil fuels. Data organized by fuel type, i.e., coal, bituminous coal, subbituminous coal, lignite coal, petroleum liquids, petroleum coke, and natural gas. Also by sector, i.e., electric power, electric utility, independent power producers, commercial, and industrial. Annual, quarterly, and monthly data available.  Based on Form EIA-423 and Form EIA-923 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14575,6 +14564,8 @@
                     "title": "Electricity Data Browser"
                 }
             ],
+            "identifier": "DOE-019-54044567677",
+            "isPartOf": "DOE-019-EDFF-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
@@ -14583,47 +14574,46 @@
                 "petroleum coke",
                 "petroleum liquids"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/#eia-423",
                 "http://www.eia.gov/tools/glossary/index.cfm?id=electricity",
                 "http://www.eia.gov/survey/#eia-923"
             ],
+            "rights": "The EIA API is offered as a free public service, although registration is required.",
+            "spatial": "United States",
+            "temporal": "2008/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Electricity Data: Average Cost of Fossil Fuels for Electricity Generation Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Electricity Data: Average Cost of Fossil Fuels For Electricity Generation (per Btu) Application Programming Interface (API)",
-            "description": "This API provides data on the average cost of fossil fuels per Btu. Data organized by fuel type, i.e., coal, bituminous coal, subbituminous coal, lignite coal, petroleum liquids, petroleum coke, and natural gas. Also by sector, i.e., electric power, electric utility, independent power producers, commercial, and industrial. Annual, quarterly, and monthly data available.  Based on Form EIA-423 and Form EIA-923 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-54044567678",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/electricity/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2008/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-EDFF-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides data on the average cost of fossil fuels per Btu. Data organized by fuel type, i.e., coal, bituminous coal, subbituminous coal, lignite coal, petroleum liquids, petroleum coke, and natural gas. Also by sector, i.e., electric power, electric utility, independent power producers, commercial, and industrial. Annual, quarterly, and monthly data available.  Based on Form EIA-423 and Form EIA-923 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14642,6 +14632,8 @@
                     "title": "Electricity Data Browser"
                 }
             ],
+            "identifier": "DOE-019-54044567678",
+            "isPartOf": "DOE-019-EDFF-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
@@ -14651,47 +14643,45 @@
                 "petroleum coke",
                 "petroleum liquids"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/#eia-423",
                 "http://www.eia.gov/tools/glossary/index.cfm?id=electricity",
                 "http://www.eia.gov/survey/#eia-923"
             ],
+            "spatial": "United States",
+            "temporal": "2008/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Electricity Data: Average Cost of Fossil Fuels For Electricity Generation (per Btu) Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Electricity Data: Quality of Fossil Fuels in Electricity Generation: Sulfur Content API",
-            "description": "This API provides  data on sulfur content in fossil fuels. Data organized by fuel type, i.e., coal, bituminous coal, subbituminous coal, lignite coal, petroleum liquids, and petroleum coke. Also by sector, i.e., electric power, electric utility, independent power producers, commercial, and industrial. Annual, quarterly, and monthly data available.  Based on Form EIA-423 and Form EIA-923 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-54044567679",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/electricity/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2008/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-EDFF-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "This API provides  data on sulfur content in fossil fuels. Data organized by fuel type, i.e., coal, bituminous coal, subbituminous coal, lignite coal, petroleum liquids, and petroleum coke. Also by sector, i.e., electric power, electric utility, independent power producers, commercial, and industrial. Annual, quarterly, and monthly data available.  Based on Form EIA-423 and Form EIA-923 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14710,6 +14700,8 @@
                     "title": "Electricity Data Browser"
                 }
             ],
+            "identifier": "DOE-019-54044567679",
+            "isPartOf": "DOE-019-EDFF-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
@@ -14719,47 +14711,45 @@
                 "petroleum liquids",
                 "sulfer content"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/electricity/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/#eia-423",
                 "http://www.eia.gov/tools/glossary/index.cfm?id=electricity",
                 "http://www.eia.gov/survey/#eia-923"
             ],
+            "spatial": "United States",
+            "temporal": "2008/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Electricity Data: Quality of Fossil Fuels in Electricity Generation: Sulfur Content API"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Natural Gas Data: Summary Application Programming Interface (API)",
-            "description": "Data on natural gas prices, production, reserves, gross withdrawals, imports and exports, underground storage, deliveries, and consumption. Annual and monthly data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-31",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445681",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/naturalgas",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1973/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-NGD-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on natural gas prices, production, reserves, gross withdrawals, imports and exports, underground storage, deliveries, and consumption. Annual and monthly data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14774,6 +14764,8 @@
                     "title": "Natural Gas Data: Summary API"
                 }
             ],
+            "identifier": "DOE-019-540445681",
+            "isPartOf": "DOE-019-NGD-COLLECTION1",
             "keyword": [
                 "API",
                 "natural gas",
@@ -14786,43 +14778,41 @@
                 "natural gas production",
                 "natural gas reserves"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "http://www.eia.gov/naturalgas",
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-31",
             "programCode": [
                 "019:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=natural%20gas",
                 "http://www.eia.gov/survey/#naturalgas"
             ],
+            "spatial": "United States",
+            "temporal": "1973/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Natural Gas Data: Summary Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Natural Gas Data: Prices Application Programming Interface (API)",
-            "description": "Data on natural gas prices. Annual and monthly data available. Users of the EIA API are required to obtain an API Key via this registration form:  http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445682",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/naturalgas",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1987/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-NGD-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on natural gas prices. Annual and monthly data available. Users of the EIA API are required to obtain an API Key via this registration form:  http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14837,6 +14827,8 @@
                     "title": "Natural Gas Data: Prices API"
                 }
             ],
+            "identifier": "DOE-019-540445682",
+            "isPartOf": "DOE-019-NGD-COLLECTION1",
             "keyword": [
                 "API",
                 "natural gas",
@@ -14845,46 +14837,44 @@
                 "natural gas prices",
                 "natural gas wellhead"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/naturalgas",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=natural%20gas",
                 "http://www.eia.gov/survey/#naturalgas"
             ],
+            "spatial": "United States",
+            "temporal": "1987/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Natural Gas Data: Prices Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Natural Gas Data: Exploration and Reserves Application Programming Interface (API)",
-            "description": "Data on natural gas reserves, acquisitions, sales, new field discoveries, estimated production, proved reserves, proved reserves adjustment, and proved reserves extensions. Also data on natural gas wells. Monthly and annual data available.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-31",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445683",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/naturalgas",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1979/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-NGD-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on natural gas reserves, acquisitions, sales, new field discoveries, estimated production, proved reserves, proved reserves adjustment, and proved reserves extensions. Also data on natural gas wells. Monthly and annual data available.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14898,6 +14888,8 @@
                     "title": "Natural Gas Data: Exploration and Reserves API"
                 }
             ],
+            "identifier": "DOE-019-540445683",
+            "isPartOf": "DOE-019-NGD-COLLECTION1",
             "keyword": [
                 "API",
                 "natural gas",
@@ -14907,43 +14899,41 @@
                 "natural gas reserves",
                 "natural gas wells"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "http://www.eia.gov/naturalgas",
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-31",
             "programCode": [
                 "019:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=natural%20gas",
                 "http://www.eia.gov/survey/#naturalgas"
             ],
+            "spatial": "United States",
+            "temporal": "1979/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Natural Gas Data: Exploration and Reserves Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Natural Gas Data: Production Application Programming Interface (API)",
-            "description": "Data on natural gas production, gross withdrawals, lease condensate production, coalbed methane production, shale gas production, and offshore production. Monthly and Annual data available.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-31",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445684",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/naturalgas",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1993/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-NGD-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on natural gas production, gross withdrawals, lease condensate production, coalbed methane production, shale gas production, and offshore production. Monthly and Annual data available.  Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -14957,6 +14947,8 @@
                     "title": "Natural Gas Data: Production API"
                 }
             ],
+            "identifier": "DOE-019-540445684",
+            "isPartOf": "DOE-019-NGD-COLLECTION1",
             "keyword": [
                 "API",
                 "natural gas",
@@ -14966,43 +14958,41 @@
                 "natural gas reserves",
                 "natural gas wells"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "http://www.eia.gov/naturalgas",
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-31",
             "programCode": [
                 "019:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=natural%20gas",
                 "http://www.eia.gov/survey/#naturalgas"
             ],
+            "spatial": "United States",
+            "temporal": "1993/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Natural Gas Data: Production Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Natural Gas Data: Storage Application Programming Interface (API)",
-            "description": "Data on natural gas storage, withdrawals, and capacity. Weekly, monthly, and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-31",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445686",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/naturalgas",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1973/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-NGD-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on natural gas storage, withdrawals, and capacity. Weekly, monthly, and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15016,6 +15006,8 @@
                     "title": "Natural Gas Data: Storage API"
                 }
             ],
+            "identifier": "DOE-019-540445686",
+            "isPartOf": "DOE-019-NGD-COLLECTION1",
             "keyword": [
                 "API",
                 "natural gas",
@@ -15023,43 +15015,41 @@
                 "natural gas storage",
                 "natural gas withdrawals"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "http://www.eia.gov/naturalgas",
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-31",
             "programCode": [
                 "019:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/index.cfm?id=natural%20gas",
                 "http://www.eia.gov/survey/#naturalgas"
             ],
+            "spatial": "United States",
+            "temporal": "1973/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Natural Gas Data: Storage Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Natural Gas Data: Consumption/End Use Application Programming Interface (API)",
-            "description": "Data on natural gas consumption, deliveries, and number of consumers. Monthly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-31",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445687",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/naturalgas/data.cfm",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "1949/2015",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1M",
-            "isPartOf": "DOE-019-NGD-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on natural gas consumption, deliveries, and number of consumers. Monthly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15073,48 +15063,48 @@
                     "title": "Natural Gas Data: Consumption/End Use API"
                 }
             ],
+            "identifier": "DOE-019-540445687",
+            "isPartOf": "DOE-019-NGD-COLLECTION1",
             "keyword": [
                 "API",
                 "natural gas consumption",
                 "natural gas deliveries"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "http://www.eia.gov/naturalgas/data.cfm",
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-31",
             "programCode": [
                 "019:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/survey/#naturalgas",
                 "http://www.eia.gov/tools/glossary/index.cfm?id=natural%20gas"
             ],
+            "spatial": "United States",
+            "temporal": "1949/2015",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Natural Gas Data: Consumption/End Use Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Export Quantity Application Programming Interface (API)",
-            "description": "Data on all coal, coke, metallurgical, and steam coal export quantities. Data organized by country and by terminal. Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-08",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445688",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "Global",
-            "temporal": "2002/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on all coal, coke, metallurgical, and steam coal export quantities. Data organized by country and by terminal. Quarterly and annual data available. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15134,48 +15124,48 @@
                     "title": "Coal Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445688",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
                 "coal exports"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "http://www.eia.gov/coal/",
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-08",
             "programCode": [
                 "019:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/coal/",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "Global",
+            "temporal": "2002/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Export Quantity Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Aggregate Coal Mine Production Application Programming Interface (API)",
-            "description": "Annual data on coal mine production. Data organized by coal rank (lignite, anthracite, subbituminous, bituminous) and by mine type (surface, underground, refuse). Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-04-23",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445692",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Annual data on coal mine production. Data organized by coal rank (lignite, anthracite, subbituminous, bituminous) and by mine type (surface, underground, refuse). Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15194,52 +15184,52 @@
                     "title": "Coal Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445692",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
                 "coal mine",
                 "coal mine production"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-04-23",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "United States",
+            "temporal": "2001/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Aggregate Coal Mine Production Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Aggregate Coal Mine Labor Hours Application Programming Interface (API)",
-            "description": "Annual data on coal mine labor hours. Data organized by mine type (surface, underground, refuse). Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-04-23",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445693",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Annual data on coal mine labor hours. Data organized by mine type (surface, underground, refuse). Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15258,52 +15248,52 @@
                     "title": "Coal Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445693",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
                 "coal mine",
                 "coal mine production"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-04-23",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "United States",
+            "temporal": "2001/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Aggregate Coal Mine Labor Hours Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Aggregate Coal Mine Average Employees Application Programming Interface (API)",
-            "description": "Annual data on the number of employees in coal mines. Data organized by mine type (total, surface, underground, refuse mining). Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-04-23",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445694",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Annual data on the number of employees in coal mines. Data organized by mine type (total, surface, underground, refuse mining). Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15322,46 +15312,47 @@
                     "title": "Coal Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445694",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
                 "coal mine"
             ],
-            "bureauCode": [
-                "019:20"
-            ],
+            "landingPage": "http://www.eia.gov/coal/",
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-04-23",
             "programCode": [
                 "019:022"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "United States",
+            "temporal": "2001/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Aggregate Coal Mine Average Employees Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Aggregate Coal Mine Productivity Application Programming Interface (API)",
-            "description": "Annual data on coal mine productivity in short tons per labor hour. Data organized by mine type (total, surface, underground, refuse). Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-04-23",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445695",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Annual data on coal mine productivity in short tons per labor hour. Data organized by mine type (total, surface, underground, refuse). Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15380,52 +15371,51 @@
                     "title": "Coal Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445695",
             "keyword": [
                 "API",
                 "coal",
                 "coal mine",
                 "coal mine productivity"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-04-23",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "United States",
+            "temporal": "2001/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Aggregate Coal Mine Productivity Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Mine Level Data Application Programming Interface (API)",
-            "description": "Coal mine level data on the number of employees, labor hours, and production. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-04-23",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445696",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001/2013",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P1Y",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Coal mine level data on the number of employees, labor hours, and production. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15444,51 +15434,51 @@
                     "title": "Coal Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445696",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
                 "coal mine"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-04-23",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "United States",
+            "temporal": "2001/2013",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Mine Level Data Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Total Consumption Application Programming Interface (API)",
-            "description": "Data on coal consumption. Data organized by electric power sector, i.e., electric utility, independent power producers, commercial and institutional, and coke plants. Quarterly and annual data available. Based on Form EIA-3 and Form EIA-923 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445697",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2001/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on coal consumption. Data organized by electric power sector, i.e., electric utility, independent power producers, commercial and institutional, and coke plants. Quarterly and annual data available. Based on Form EIA-3 and Form EIA-923 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15507,51 +15497,51 @@
                     "title": "Total Coal Consumption API"
                 }
             ],
+            "identifier": "DOE-019-540445697",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
                 "coal consumption"
             ],
-            "bureauCode": [
-                "019:20"
+            "landingPage": "http://www.eia.gov/coal/",
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "spatial": "United States",
+            "temporal": "2001/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Total Consumption Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Price Application Programming Interface (API)",
-            "description": "Data on coal prices in $/short ton. Data organized by electric power sector, i.e., electric utility, independent power producers, commercial and institutional, and coke plants. Quarterly and annual data available. Based on Form EIA-3 and Form EIA-923 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445698",
-            "dataQuality": true,
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "rights": "The EIA API is offered as a free public service, although registration is required.",
-            "spatial": "United States",
-            "temporal": "2008/2014",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "U.S. Energy Information Administration"
-            },
             "accrualPeriodicity": "R/P3M",
-            "isPartOf": "DOE-019-COAL-COLLECTION1",
+            "bureauCode": [
+                "019:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "William Jeffers",
                 "hasEmail": "mailto:data@eia.gov"
             },
+            "dataQuality": true,
+            "description": "Data on coal prices in $/short ton. Data organized by electric power sector, i.e., electric utility, independent power producers, commercial and institutional, and coke plants. Quarterly and annual data available. Based on Form EIA-3 and Form EIA-923 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -15570,51 +15560,51 @@
                     "title": "Coal Data Browser"
                 }
             ],
+            "identifier": "DOE-019-540445698",
+            "isPartOf": "DOE-019-COAL-COLLECTION1",
             "keyword": [
                 "API",
                 "coal",
                 "coal price"
             ],
-            "bureauCode": [
-                "019:20"
+            "language": [
+                "en-US"
             ],
+            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
+            "modified": "2015-07-27",
             "programCode": [
                 "019:022"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Energy Information Administration"
+            },
             "references": [
                 "http://www.eia.gov/tools/glossary/?id=coal",
                 "http://www.eia.gov/survey/#coal"
             ],
+            "rights": "The EIA API is offered as a free public service, although registration is required.",
+            "spatial": "United States",
+            "temporal": "2008/2014",
             "theme": [
                 "energy"
-            ]
+            ],
+            "title": "Coal Data: Price Application Programming Interface (API)"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "Coal Data: Receipts Application Programming Interface (API)",
-            "description": "Data on coal receipts in short tons. Data organized by electric power sector, i.e., electric utility, independent power producers, commercial and institutional, and coke plants. Quarterly and annual data available. Based on Form EIA-3 and Form EIA-923 data. Users of the EIA API are required to obtain an API Key via this registration form: http://www.eia.gov/beta/api/register.cfm",
-            "modified": "2015-07-27",
             "accessLevel": "restricted public",
-            "identifier": "DOE-019-540445699",
-            "dataQuality": true,
-            "landingPage": "http://www.eia.gov/coal/",
-            "license": "http://creativecommons.org/publicdomain/mark/1.0/other-pd",
-            "spatial": "United States",
-            "temporal": "2008/2014",
-            "publisher": {
-                "@type": "org:Organization",
```

