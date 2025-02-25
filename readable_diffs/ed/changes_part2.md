# Change History for ed.json (Part 2)

### Changes from 31606f9 to dd2190f (Part 2/13)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/1c004a108b18460bba1ddb29ec1f7982/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/1c004a108b18460bba1ddb29ec1f7982/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "d80ca738-e107-4584-87e2-ce7ff8f27e9a",
+            "issued": "2020-03-25T21:20:39.000Z",
             "keyword": [
                 "edge",
                 "education-demographic-and-geographic-estimates-program",
@@ -9385,25 +9364,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:11.180862",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Private School Locations 2021-22",
-            "description": "<div style='text-align:Left;'><p>The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimates (EDGE) program develops bi-annually updated point locations (latitude and longitude) for private schools included in the NCES Private School Survey (PSS). The PSS is conducted to provide a biennial count of the total number of private schools, teachers, and students. The PSS school location and associated geographic area assignments are derived from reported information about the physical location of private schools. The school geocode file includes supplemental geographic information for the universe of schools reported in the 2021-2022 PSS school collection, and they can be integrated with the survey files through use of institutional identifiers included in both sources. For more information about NCES school point data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' style='color:rgb(0, 121, 193); font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px; text-decoration-line:none;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>\u00a0and\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries' style='color:rgb(0, 121, 193); font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px; text-decoration-line:none;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries</a>.</p><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></p></div>",
-            "modified": "2024-10-19T12:48:10.220479",
-            "accessLevel": "public",
-            "identifier": "9eaca271-3952-4a23-90ff-4900474ff82b",
-            "issued": "2023-12-21T17:02:54.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -9424,63 +9389,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Private School Locations - Current"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><p>The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimates (EDGE) program develops bi-annually updated point locations (latitude and longitude) for private schools included in the NCES Private School Survey (PSS). The PSS is conducted to provide a biennial count of the total number of private schools, teachers, and students. The PSS school location and associated geographic area assignments are derived from reported information about the physical location of private schools. The school geocode file includes supplemental geographic information for the universe of schools reported in the 2021-2022 PSS school collection, and they can be integrated with the survey files through use of institutional identifiers included in both sources. For more information about NCES school point data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' style='color:rgb(0, 121, 193); font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px; text-decoration-line:none;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>\u00a0and\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries' style='color:rgb(0, 121, 193); font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px; text-decoration-line:none;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries</a>.</p><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></p></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/5ebacc8bd42e4d85a66d0661fd5fb29e/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/5ebacc8bd42e4d85a66d0661fd5fb29e/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::private-school-locations-2021-22",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::private-school-locations-2021-22"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PRIVATESCH_2122/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PRIVATESCH_2122/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/5ebacc8bd42e4d85a66d0661fd5fb29e/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/5ebacc8bd42e4d85a66d0661fd5fb29e/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/5ebacc8bd42e4d85a66d0661fd5fb29e/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/5ebacc8bd42e4d85a66d0661fd5fb29e/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/5ebacc8bd42e4d85a66d0661fd5fb29e/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/5ebacc8bd42e4d85a66d0661fd5fb29e/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/5ebacc8bd42e4d85a66d0661fd5fb29e/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/5ebacc8bd42e4d85a66d0661fd5fb29e/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "9eaca271-3952-4a23-90ff-4900474ff82b",
+            "issued": "2023-12-21T17:02:54.000Z",
             "keyword": [
                 "edge",
                 "education-demographic-and-geographic-estimates-program",
@@ -9495,25 +9474,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:10.220479",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Private School Locations 2019-20",
-            "description": "The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimate (EDGE) program develops bi-annually updated point locations (latitude and longitude) for private schools included in the NCES Private School Survey (PSS). The PSS is conducted to provide a biennial count of the total number of private schools, teachers, and students.\u00a0The PSS school location and associated geographic area assignments are derived from reported information about the physical location of private schools. The school geocode file includes supplemental geographic information for the universe of schools reported in the 2019-2020 PSS school collection, and they can be integrated with the survey files through use of institutional identifiers included in both sources. For more information about NCES school point data,\u00a0 see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>\u00a0and\u00a0</span><a href='https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries</a><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>.</span><div><p><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif;'><br /></span></p><p><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</span><br /></p><p><span></span></p></div>",
-            "modified": "2024-10-19T12:48:08.759520",
-            "accessLevel": "public",
-            "identifier": "bd6becee-8372-41ca-a37e-627143c1e76d",
-            "issued": "2021-10-25T19:11:17.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -9534,77 +9499,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Private School Locations 2021-22"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimate (EDGE) program develops bi-annually updated point locations (latitude and longitude) for private schools included in the NCES Private School Survey (PSS). The PSS is conducted to provide a biennial count of the total number of private schools, teachers, and students.\u00a0The PSS school location and associated geographic area assignments are derived from reported information about the physical location of private schools. The school geocode file includes supplemental geographic information for the universe of schools reported in the 2019-2020 PSS school collection, and they can be integrated with the survey files through use of institutional identifiers included in both sources. For more information about NCES school point data,\u00a0 see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>\u00a0and\u00a0</span><a href='https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries</a><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>.</span><div><p><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif;'><br /></span></p><p><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</span><br /></p><p><span></span></p></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/18cd70b6f5424bbaa05dd4086a29d63b/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/18cd70b6f5424bbaa05dd4086a29d63b/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::private-school-locations-2019-20",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::private-school-locations-2019-20"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PRIVATESCH_1920/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PRIVATESCH_1920/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Geocodes: Private Schools",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_GEOCODE_PRIVATESCH_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Private Schools"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Geocodes: Private Schools",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PRIVATESCH_1920.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Private Schools"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/18cd70b6f5424bbaa05dd4086a29d63b/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/18cd70b6f5424bbaa05dd4086a29d63b/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/18cd70b6f5424bbaa05dd4086a29d63b/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/18cd70b6f5424bbaa05dd4086a29d63b/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/18cd70b6f5424bbaa05dd4086a29d63b/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/18cd70b6f5424bbaa05dd4086a29d63b/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/18cd70b6f5424bbaa05dd4086a29d63b/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/18cd70b6f5424bbaa05dd4086a29d63b/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "bd6becee-8372-41ca-a37e-627143c1e76d",
+            "issued": "2021-10-25T19:11:17.000Z",
             "keyword": [
                 "edge",
                 "education-demographic-and-geographic-estimates-program",
@@ -9619,25 +9598,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:08.759520",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Private School Locations 2017-18",
-            "description": "The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimate (EDGE) program develops bi-annually updated point locations (latitude and longitude) for private schools included in the NCES Private School Survey (PSS). The PSS is conducted to generate biennial data on the total number of private schools, teachers, and students, and to build an accurate and complete list of private schools to serve as a sampling frame for NCES surveys. The PSS school location and associated geographic area assignments are derived from reported information about the physical location of private schools. The school geocode file includes supplemental geographic information for the universe of schools reported in the 2017-2018 PSS school sample, and they can be integrated with the survey files through use of institutional identifiers included in both sources. For more information about NCES school point data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>\u00a0and\u00a0</span><a href='https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries</a><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>.</span><p><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif;'><br /></span></p><p><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</span><br /></p>",
-            "modified": "2024-10-19T12:48:07.715928",
-            "accessLevel": "public",
-            "identifier": "1f32eb3d-dfc7-4d20-a71f-b3a453728dfc",
-            "issued": "2020-03-20T23:42:45.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -9658,77 +9623,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Private School Locations 2019-20"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimate (EDGE) program develops bi-annually updated point locations (latitude and longitude) for private schools included in the NCES Private School Survey (PSS). The PSS is conducted to generate biennial data on the total number of private schools, teachers, and students, and to build an accurate and complete list of private schools to serve as a sampling frame for NCES surveys. The PSS school location and associated geographic area assignments are derived from reported information about the physical location of private schools. The school geocode file includes supplemental geographic information for the universe of schools reported in the 2017-2018 PSS school sample, and they can be integrated with the survey files through use of institutional identifiers included in both sources. For more information about NCES school point data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>\u00a0and\u00a0</span><a href='https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries</a><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>.</span><p><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif;'><br /></span></p><p><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</span><br /></p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/b3c70b83d725438292cce259a0fc1d08/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/b3c70b83d725438292cce259a0fc1d08/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::private-school-locations-2017-18",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::private-school-locations-2017-18"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PRIVATESCH_1718/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PRIVATESCH_1718/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Geocodes: Private Schools",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_GEOCODE_PRIVATESCH_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Private Schools"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Geocodes: Private Schools",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PRIVATESCH_17_18.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Private Schools"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b3c70b83d725438292cce259a0fc1d08/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b3c70b83d725438292cce259a0fc1d08/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b3c70b83d725438292cce259a0fc1d08/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b3c70b83d725438292cce259a0fc1d08/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b3c70b83d725438292cce259a0fc1d08/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b3c70b83d725438292cce259a0fc1d08/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b3c70b83d725438292cce259a0fc1d08/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b3c70b83d725438292cce259a0fc1d08/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "1f32eb3d-dfc7-4d20-a71f-b3a453728dfc",
+            "issued": "2020-03-20T23:42:45.000Z",
             "keyword": [
                 "edge",
                 "education-demographic-and-geographic-estimates-program",
@@ -9743,25 +9722,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:07.715928",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Private School Locations 2015-16",
-            "description": "The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimate (EDGE) program develops bi-annually updated point locations (latitude and longitude) for private schools included in the NCES Private School Survey (PSS). The PSS is conducted to generate biennial data on the total number of private schools, teachers, and students, and to build an accurate and complete list of private schools to serve as a sampling frame for NCES surveys. The PSS school location and associated geographic area assignments are derived from reported information about the physical location of private schools. The school geocode file includes supplemental geographic information for the universe of schools reported in the 2015-2016 PSS school sample, and they can be integrated with the survey files through use of institutional identifiers included in both sources. For more information about NCES school point data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>\u00a0and\u00a0</span><a href='https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries</a><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>.</span><div><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></span></div><div><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></span></div>",
-            "modified": "2024-10-19T12:48:06.719586",
-            "accessLevel": "public",
-            "identifier": "ebdf989c-45fc-48a4-b8e7-28e9085aecfd",
-            "issued": "2020-03-20T23:20:20.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -9782,77 +9747,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Private School Locations 2017-18"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimate (EDGE) program develops bi-annually updated point locations (latitude and longitude) for private schools included in the NCES Private School Survey (PSS). The PSS is conducted to generate biennial data on the total number of private schools, teachers, and students, and to build an accurate and complete list of private schools to serve as a sampling frame for NCES surveys. The PSS school location and associated geographic area assignments are derived from reported information about the physical location of private schools. The school geocode file includes supplemental geographic information for the universe of schools reported in the 2015-2016 PSS school sample, and they can be integrated with the survey files through use of institutional identifiers included in both sources. For more information about NCES school point data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>\u00a0and\u00a0</span><a href='https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries</a><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>.</span><div><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></span></div><div><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></span></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/528953aa81b24f6f8ec071302c550401/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/528953aa81b24f6f8ec071302c550401/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::private-school-locations-2015-16",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::private-school-locations-2015-16"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PRIVATESCH_15_16/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PRIVATESCH_15_16/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Geocodes: Private Schools",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_GEOCODE_PRIVATESCH_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Private Schools"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Geocodes: Private Schools",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PRIVATESCH_15_16.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Private Schools"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/528953aa81b24f6f8ec071302c550401/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/528953aa81b24f6f8ec071302c550401/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/528953aa81b24f6f8ec071302c550401/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/528953aa81b24f6f8ec071302c550401/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/528953aa81b24f6f8ec071302c550401/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/528953aa81b24f6f8ec071302c550401/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/528953aa81b24f6f8ec071302c550401/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/528953aa81b24f6f8ec071302c550401/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "ebdf989c-45fc-48a4-b8e7-28e9085aecfd",
+            "issued": "2020-03-20T23:20:20.000Z",
             "keyword": [
                 "edge",
                 "education-demographic-and-geographic-estimates-program",
@@ -9867,25 +9846,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:06.719586",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Public School Characteristics 2021-22",
-            "description": "<p style='margin:12pt 0in; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>The National Center for\nEducation Statistics' (NCES) Education Demographic and Geographic Estimate\n(EDGE) program develops annually updated point locations (latitude and\nlongitude) for public elementary and secondary schools included in the NCES\nCommon Core of Data (CCD). The CCD program annually collects administrative and\nfiscal data about all public schools, school districts, and state education\nagencies in the United States. The data are supplied by state education agency\nofficials and include basic directory and contact information for schools and\nschool districts, as well as characteristics about student demographics, number\nof teachers, school grade span, and various other administrative conditions.\nCCD school and agency point locations are derived from reported information\nabout the physical location of schools and agency administrative offices.\u00a0<span>The point locations and administrative\nattributes in this data layer were developed from the 2021-2022 CCD collection.</span>\u00a0For more information about NCES school point data,\nsee:\u00a0<font size='3'><span style='color:black;'><a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' target='_blank' rel='nofollow ugc noopener noreferrer'><span style='font-family:Calibri, sans-serif;'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</span></a></span><span style='font-family:Calibri, sans-serif;'>.</span><span style='font-family:Calibri, sans-serif; color:black;'> </span></font>For more information about\nthese CCD attributes, as well as additional attributes not included, see:<font size='3'><span style='font-family:Calibri, sans-serif;'>\u00a0</span><span style='color:black;'><a href='https://nces.ed.gov/ccd/files.asp' target='_blank' rel='nofollow ugc noopener noreferrer'><span style='font-family:Calibri, sans-serif;'>https://nces.ed.gov/ccd/files.asp</span></a></span><span style='font-family:Calibri, sans-serif;'>.</span></font></p><div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Notes:</div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><table border='1' cellpadding='0' cellspacing='0' style='margin-bottom:1.5rem; width:1004px; border-collapse:collapse; border-spacing:0px; border:none; font-size:0.875rem;'><tbody><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border:1pt solid windowtext; padding:0in 5.4pt; width:71.75pt;' valign='top' width='96'><p style='margin-top:0px; margin-bottom:0in;'><span style='font-family:inherit; font-size:12pt;'>-1 or M</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:233.75pt; border-top:1pt solid windowtext; border-bottom:1pt solid windowtext; border-image:initial;' valign='top' width='312'><p style='margin-top:0px; margin-bottom:0in;'><span style='font-family:inherit; font-size:12pt;'>Indicates that the data are missing.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:71.75pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='96'><p style='margin-top:0px; margin-bottom:0in;'><span style='font-family:inherit; font-size:12pt;'>-2 or N</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:233.75pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='312'><p style='margin-top:0px; margin-bottom:0in;'><span style='font-family:inherit; font-size:12pt;'>Indicates that the data are not applicable.</span></p></td></tr><tr style='border-bottom:none;'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:71.75pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='96'><p style='margin-top:0px; margin-bottom:0in;'><span style='font-family:inherit; font-size:12pt;'>-9</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:233.75pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='312'><p style='margin-top:0px; margin-bottom:0in;'><span style='font-family:inherit; font-size:12pt;'>Indicates that the data do not meet NCES data quality standards.</span></p></td></tr></tbody></table></div><div><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></span></div><div><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</span><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></span></div></div>",
-            "modified": "2024-10-19T12:48:05.915970",
-            "accessLevel": "public",
-            "identifier": "4af10df6-bd8b-417a-9914-507bfd45d544",
-            "issued": "2023-04-04T11:49:51.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -9906,63 +9871,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Private School Locations 2015-16"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<p style='margin:12pt 0in; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>The National Center for\nEducation Statistics' (NCES) Education Demographic and Geographic Estimate\n(EDGE) program develops annually updated point locations (latitude and\nlongitude) for public elementary and secondary schools included in the NCES\nCommon Core of Data (CCD). The CCD program annually collects administrative and\nfiscal data about all public schools, school districts, and state education\nagencies in the United States. The data are supplied by state education agency\nofficials and include basic directory and contact information for schools and\nschool districts, as well as characteristics about student demographics, number\nof teachers, school grade span, and various other administrative conditions.\nCCD school and agency point locations are derived from reported information\nabout the physical location of schools and agency administrative offices.\u00a0<span>The point locations and administrative\nattributes in this data layer were developed from the 2021-2022 CCD collection.</span>\u00a0For more information about NCES school point data,\nsee:\u00a0<font size='3'><span style='color:black;'><a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' target='_blank' rel='nofollow ugc noopener noreferrer'><span style='font-family:Calibri, sans-serif;'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</span></a></span><span style='font-family:Calibri, sans-serif;'>.</span><span style='font-family:Calibri, sans-serif; color:black;'> </span></font>For more information about\nthese CCD attributes, as well as additional attributes not included, see:<font size='3'><span style='font-family:Calibri, sans-serif;'>\u00a0</span><span style='color:black;'><a href='https://nces.ed.gov/ccd/files.asp' target='_blank' rel='nofollow ugc noopener noreferrer'><span style='font-family:Calibri, sans-serif;'>https://nces.ed.gov/ccd/files.asp</span></a></span><span style='font-family:Calibri, sans-serif;'>.</span></font></p><div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Notes:</div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><table border='1' cellpadding='0' cellspacing='0' style='margin-bottom:1.5rem; width:1004px; border-collapse:collapse; border-spacing:0px; border:none; font-size:0.875rem;'><tbody><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border:1pt solid windowtext; padding:0in 5.4pt; width:71.75pt;' valign='top' width='96'><p style='margin-top:0px; margin-bottom:0in;'><span style='font-family:inherit; font-size:12pt;'>-1 or M</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:233.75pt; border-top:1pt solid windowtext; border-bottom:1pt solid windowtext; border-image:initial;' valign='top' width='312'><p style='margin-top:0px; margin-bottom:0in;'><span style='font-family:inherit; font-size:12pt;'>Indicates that the data are missing.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:71.75pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='96'><p style='margin-top:0px; margin-bottom:0in;'><span style='font-family:inherit; font-size:12pt;'>-2 or N</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:233.75pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='312'><p style='margin-top:0px; margin-bottom:0in;'><span style='font-family:inherit; font-size:12pt;'>Indicates that the data are not applicable.</span></p></td></tr><tr style='border-bottom:none;'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:71.75pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='96'><p style='margin-top:0px; margin-bottom:0in;'><span style='font-family:inherit; font-size:12pt;'>-9</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:233.75pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='312'><p style='margin-top:0px; margin-bottom:0in;'><span style='font-family:inherit; font-size:12pt;'>Indicates that the data do not meet NCES data quality standards.</span></p></td></tr></tbody></table></div><div><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></span></div><div><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</span><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></span></div></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/b480c30aa8654d23be9b79a0feb436e3/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/b480c30aa8654d23be9b79a0feb436e3/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::public-school-characteristics-2021-22",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::public-school-characteristics-2021-22"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_ADMINDATA_PUBLICSCH_2122/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_ADMINDATA_PUBLICSCH_2122/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b480c30aa8654d23be9b79a0feb436e3/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b480c30aa8654d23be9b79a0feb436e3/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b480c30aa8654d23be9b79a0feb436e3/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b480c30aa8654d23be9b79a0feb436e3/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b480c30aa8654d23be9b79a0feb436e3/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b480c30aa8654d23be9b79a0feb436e3/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b480c30aa8654d23be9b79a0feb436e3/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b480c30aa8654d23be9b79a0feb436e3/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "4af10df6-bd8b-417a-9914-507bfd45d544",
+            "issued": "2023-04-04T11:49:51.000Z",
             "keyword": [
                 "ccd",
                 "common-core-of-data",
@@ -9977,25 +9956,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:05.915970",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Public School Characteristics 2020-21",
-            "description": "<div style='text-align:Left;'><p>The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary and secondary schools included in the NCES Common Core of Data (CCD). The CCD program annually collects administrative and fiscal data about all public schools, school districts, and state education agencies in the United States. The data are supplied by state education agency officials and include basic directory and contact information for schools and school districts, as well as characteristics about student demographics, number of teachers, school grade span, and various other administrative conditions. CCD school and agency point locations are derived from reported information about the physical location of schools and agency administrative offices.\u00a0<span>The point locations and administrative\nattributes in this data layer were developed from the 2020-2021 CCD collection.</span>\u00a0For more information about NCES school point data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>. For more information about these CCD attributes, as well as additional attributes not included, see:\u00a0<a href='https://nces.ed.gov/ccd/files.asp' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/ccd/files.asp</a>.<br /></p><div>Notes:</div><div><table border='1' cellpadding='0' cellspacing='0' style='border-collapse:collapse; border:none;'>\n <tbody><tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-1 or M</span></p>\n  </td>\n  <td style='width:233.75pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are missing.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-2 or N</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are not applicable.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-9</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data do not meet NCES data quality standards.</span></p>\n  </td>\n </tr>\n</tbody></table></div><p>All information contained in this file is in the public domain. Data \nusers are advised to review NCES program documentation and feature class\n metadata to understand the limitations and appropriate use of these \ndata.<br /></p><p><span></span></p></div>",
-            "modified": "2024-10-19T12:48:04.909889",
-            "accessLevel": "public",
-            "identifier": "3ab9e035-8482-4908-8e4b-0bfd37738454",
-            "issued": "2022-06-13T14:57:00.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -10016,77 +9981,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Public School Characteristics 2021-22"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><p>The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary and secondary schools included in the NCES Common Core of Data (CCD). The CCD program annually collects administrative and fiscal data about all public schools, school districts, and state education agencies in the United States. The data are supplied by state education agency officials and include basic directory and contact information for schools and school districts, as well as characteristics about student demographics, number of teachers, school grade span, and various other administrative conditions. CCD school and agency point locations are derived from reported information about the physical location of schools and agency administrative offices.\u00a0<span>The point locations and administrative\nattributes in this data layer were developed from the 2020-2021 CCD collection.</span>\u00a0For more information about NCES school point data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>. For more information about these CCD attributes, as well as additional attributes not included, see:\u00a0<a href='https://nces.ed.gov/ccd/files.asp' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/ccd/files.asp</a>.<br /></p><div>Notes:</div><div><table border='1' cellpadding='0' cellspacing='0' style='border-collapse:collapse; border:none;'>\n <tbody><tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-1 or M</span></p>\n  </td>\n  <td style='width:233.75pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are missing.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-2 or N</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are not applicable.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-9</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data do not meet NCES data quality standards.</span></p>\n  </td>\n </tr>\n</tbody></table></div><p>All information contained in this file is in the public domain. Data \nusers are advised to review NCES program documentation and feature class\n metadata to understand the limitations and appropriate use of these \ndata.<br /></p><p><span></span></p></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/e3cbd4087f144ec5ac3b31094ec84199/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/e3cbd4087f144ec5ac3b31094ec84199/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::public-school-characteristics-2020-21",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::public-school-characteristics-2020-21"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_ADMINDATA_PUBLICSCH_2021/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_ADMINDATA_PUBLICSCH_2021/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Public School Documentation",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_GEOCODE_PUBLIC_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Public School Documentation"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Public School Characteristics 2020-21",
                     "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::public-school-characteristics-2020-21.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Public School Characteristics 2020-21"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/e3cbd4087f144ec5ac3b31094ec84199/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/e3cbd4087f144ec5ac3b31094ec84199/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/e3cbd4087f144ec5ac3b31094ec84199/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/e3cbd4087f144ec5ac3b31094ec84199/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/e3cbd4087f144ec5ac3b31094ec84199/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/e3cbd4087f144ec5ac3b31094ec84199/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/e3cbd4087f144ec5ac3b31094ec84199/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/e3cbd4087f144ec5ac3b31094ec84199/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "3ab9e035-8482-4908-8e4b-0bfd37738454",
+            "issued": "2022-06-13T14:57:00.000Z",
             "keyword": [
                 "ccd",
                 "common-core-of-data",
@@ -10101,25 +10080,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:04.909889",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Public School Characteristics 2019-20",
-            "description": "<div style='text-align:Left;'><p><span>The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary and secondary schools included in the NCES Common Core of Data (CCD). The NCES EDGE program collaborates with the U.S. Census Bureau's Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for schools reported in the annual CCD directory file. The CCD program annually collects administrative and fiscal data about all public schools, school districts, and state education agencies in the United States. The data are supplied by state education agency officials and include basic directory and contact information for schools and school districts, as well as characteristics about student demographics, number of teachers, school grade span, and various other administrative conditions. CCD school and agency point locations are derived from reported information about the physical location of schools and agency administrative offices. The point locations and administrative attributes in this data layer were developed from the 2019-2020 CCD collection. For more information about NCES school point data, see: <a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>. For more information about these CCD attributes, as well as additional attributes not included, see: <a href='https://nces.ed.gov/ccd/files.asp' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/ccd/files.asp</a>.</span></p><div>Notes:</div><div><table border='1' cellpadding='0' cellspacing='0' style='border-collapse:collapse; border:none;'>\n <tbody><tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-1 or M</span></p>\n  </td>\n  <td style='width:233.75pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are missing.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-2 or N</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are not applicable.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-9</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data do not meet NCES data quality standards.</span></p>\n  </td>\n </tr>\n</tbody></table></div><p>All information contained in this file is in the public domain. Data \nusers are advised to review NCES program documentation and feature class\n metadata to understand the limitations and appropriate use of these \ndata.<br /></p><p><span></span></p></div>",
-            "modified": "2024-10-19T12:48:03.826891",
-            "accessLevel": "public",
-            "identifier": "cdf064a4-a167-4341-b065-9f52b901db29",
-            "issued": "2021-08-24T18:18:48.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -10140,77 +10105,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Public School Characteristics 2020-21"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><p><span>The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary and secondary schools included in the NCES Common Core of Data (CCD). The NCES EDGE program collaborates with the U.S. Census Bureau's Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for schools reported in the annual CCD directory file. The CCD program annually collects administrative and fiscal data about all public schools, school districts, and state education agencies in the United States. The data are supplied by state education agency officials and include basic directory and contact information for schools and school districts, as well as characteristics about student demographics, number of teachers, school grade span, and various other administrative conditions. CCD school and agency point locations are derived from reported information about the physical location of schools and agency administrative offices. The point locations and administrative attributes in this data layer were developed from the 2019-2020 CCD collection. For more information about NCES school point data, see: <a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>. For more information about these CCD attributes, as well as additional attributes not included, see: <a href='https://nces.ed.gov/ccd/files.asp' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/ccd/files.asp</a>.</span></p><div>Notes:</div><div><table border='1' cellpadding='0' cellspacing='0' style='border-collapse:collapse; border:none;'>\n <tbody><tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-1 or M</span></p>\n  </td>\n  <td style='width:233.75pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are missing.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-2 or N</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are not applicable.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-9</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data do not meet NCES data quality standards.</span></p>\n  </td>\n </tr>\n</tbody></table></div><p>All information contained in this file is in the public domain. Data \nusers are advised to review NCES program documentation and feature class\n metadata to understand the limitations and appropriate use of these \ndata.<br /></p><p><span></span></p></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/39ba5e0393174f5da3772ca48f6273bf/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/39ba5e0393174f5da3772ca48f6273bf/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::public-school-characteristics-2019-20",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::public-school-characteristics-2019-20"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_ADMINDATA_PUBLICSCH_1920/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_ADMINDATA_PUBLICSCH_1920/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Public School Documentation",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_GEOCODE_PUBLIC_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Public School Documentation"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Public School Characteristics 2019-20",
                     "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::public-school-characteristics-2019-20.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Public School Characteristics 2019-20"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/39ba5e0393174f5da3772ca48f6273bf/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/39ba5e0393174f5da3772ca48f6273bf/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/39ba5e0393174f5da3772ca48f6273bf/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/39ba5e0393174f5da3772ca48f6273bf/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/39ba5e0393174f5da3772ca48f6273bf/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/39ba5e0393174f5da3772ca48f6273bf/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/39ba5e0393174f5da3772ca48f6273bf/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/39ba5e0393174f5da3772ca48f6273bf/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "cdf064a4-a167-4341-b065-9f52b901db29",
+            "issued": "2021-08-24T18:18:48.000Z",
             "keyword": [
                 "ccd",
                 "common-core-of-data",
@@ -10225,25 +10204,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:03.826891",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Public School Characteristics 2018-19",
-            "description": "<div style='text-align:Left;'><div><div><p><span>The National Center for\n Education Statistics' (NCES) Education Demographic and Geographic \nEstimate (EDGE) program develops annually updated point locations \n(latitude and longitude) for public elementary and secondary schools \nincluded in the NCES Common Core of Data (CCD). The NCES EDGE program \ncollaborates with the U.S. Census Bureau's Education Demographic, \nGeographic, and Economic Statistics (EDGE) Branch to develop point \nlocations for schools reported in the annual CCD directory file. The CCD\n program annually collects administrative and fiscal data about all \npublic schools, school districts, and state education agencies in the \nUnited States. The data are supplied by state education agency officials\n and include basic directory and contact information for schools and \nschool districts, as well as characteristics about student demographics,\n number of teachers, school grade span, and various other administrative\n conditions. CCD school and agency point locations are derived from \nreported information about the physical location of schools and agency \nadministrative offices. The point locations and administrative \nattributes in this data layer were developed from the 2018-2019 CCD \ncollection. For more information about NCES school point data, see: <a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>. For more information about these CCD attributes, as well as additional attributes not included, see: <a href='https://nces.ed.gov/ccd/files.asp' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/ccd/files.asp</a>.</span></p><div>Notes:</div><div><table border='1' cellpadding='0' cellspacing='0' style='border-collapse:collapse; border:none;'>\n <tbody><tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-1 or M</span></p>\n  </td>\n  <td style='width:233.75pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are missing.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-2 or N</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are not applicable.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-9</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data do not meet NCES data quality standards.</span></p>\n  </td>\n </tr>\n</tbody></table></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><p><span></span></p><p><span>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></span></p></div></div></div>",
-            "modified": "2024-10-19T12:48:02.838318",
-            "accessLevel": "public",
-            "identifier": "2cd9c703-6893-4ce2-b8d2-c437bc9d4050",
-            "issued": "2020-08-10T20:56:41.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -10264,77 +10229,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Public School Characteristics 2019-20"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><div><div><p><span>The National Center for\n Education Statistics' (NCES) Education Demographic and Geographic \nEstimate (EDGE) program develops annually updated point locations \n(latitude and longitude) for public elementary and secondary schools \nincluded in the NCES Common Core of Data (CCD). The NCES EDGE program \ncollaborates with the U.S. Census Bureau's Education Demographic, \nGeographic, and Economic Statistics (EDGE) Branch to develop point \nlocations for schools reported in the annual CCD directory file. The CCD\n program annually collects administrative and fiscal data about all \npublic schools, school districts, and state education agencies in the \nUnited States. The data are supplied by state education agency officials\n and include basic directory and contact information for schools and \nschool districts, as well as characteristics about student demographics,\n number of teachers, school grade span, and various other administrative\n conditions. CCD school and agency point locations are derived from \nreported information about the physical location of schools and agency \nadministrative offices. The point locations and administrative \nattributes in this data layer were developed from the 2018-2019 CCD \ncollection. For more information about NCES school point data, see: <a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>. For more information about these CCD attributes, as well as additional attributes not included, see: <a href='https://nces.ed.gov/ccd/files.asp' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/ccd/files.asp</a>.</span></p><div>Notes:</div><div><table border='1' cellpadding='0' cellspacing='0' style='border-collapse:collapse; border:none;'>\n <tbody><tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-1 or M</span></p>\n  </td>\n  <td style='width:233.75pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are missing.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-2 or N</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are not applicable.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-9</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data do not meet NCES data quality standards.</span></p>\n  </td>\n </tr>\n</tbody></table></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><p><span></span></p><p><span>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></span></p></div></div></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/146f28635d01435e978c6d2d5ccf6ea9/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/146f28635d01435e978c6d2d5ccf6ea9/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::public-school-characteristics-2018-19",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::public-school-characteristics-2018-19"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_ADMINDATA_PUBLICSCH_1819/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_ADMINDATA_PUBLICSCH_1819/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Public School Documentation",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_GEOCODE_PUBLIC_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Public School Documentation"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Public School Characteristics 2018-19",
                     "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::public-school-characteristics-2018-19.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Public School Characteristics 2018-19"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/146f28635d01435e978c6d2d5ccf6ea9/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/146f28635d01435e978c6d2d5ccf6ea9/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/146f28635d01435e978c6d2d5ccf6ea9/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/146f28635d01435e978c6d2d5ccf6ea9/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/146f28635d01435e978c6d2d5ccf6ea9/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/146f28635d01435e978c6d2d5ccf6ea9/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/146f28635d01435e978c6d2d5ccf6ea9/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/146f28635d01435e978c6d2d5ccf6ea9/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "2cd9c703-6893-4ce2-b8d2-c437bc9d4050",
+            "issued": "2020-08-10T20:56:41.000Z",
             "keyword": [
                 "ccd",
                 "common-core-of-data",
@@ -10349,25 +10328,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:02.838318",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Public School Characteristics 2017-18",
-            "description": "<div style='text-align:Left;'><p></p><div style='text-align:Left;'><div><div><p><span>The National Center for\n Education Statistics' (NCES) Education Demographic and Geographic \nEstimate (EDGE) program develops annually updated point locations \n(latitude and longitude) for public elementary and secondary schools \nincluded in the NCES Common Core of Data (CCD). The NCES EDGE program \ncollaborates with the U.S. Census Bureau's Education Demographic, \nGeographic, and Economic Statistics (EDGE) Branch to develop point \nlocations for schools reported in the annual CCD directory file. The CCD\n program annually collects administrative and fiscal data about all \npublic schools, school districts, and state education agencies in the \nUnited States. The data are supplied by state education agency officials\n and include basic directory and contact information for schools and \nschool districts, as well as characteristics about student demographics,\n number of teachers, school grade span, and various other administrative\n conditions. CCD school and agency point locations are derived from \nreported information about the physical location of schools and agency \nadministrative offices. The point locations and administrative \nattributes in this data layer were developed from the 2017-2018 CCD \ncollection. For more information about NCES school point data, see: <a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>. For more information about these CCD attributes, as well as additional attributes not included, see: <a href='https://nces.ed.gov/ccd/files.asp' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/ccd/files.asp</a>.</span></p><div>Notes:</div><div><table border='1' cellpadding='0' cellspacing='0' style='border-collapse:collapse; border:none;'>\n <tbody><tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-1 or M</span></p>\n  </td>\n  <td style='width:233.75pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are missing.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-2 or N</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are not applicable.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-9</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data do not meet NCES data quality standards.</span></p>\n  </td>\n </tr>\n</tbody></table></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><p><span></span></p><p><span>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></span></p></div></div></div><p></p></div>",
-            "modified": "2024-10-19T12:48:01.806528",
-            "accessLevel": "public",
-            "identifier": "58488bcb-1a7c-45fd-bf20-1b3adaf0b3d3",
-            "issued": "2020-04-27T14:10:09.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -10388,77 +10353,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Public School Characteristics 2018-19"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><p></p><div style='text-align:Left;'><div><div><p><span>The National Center for\n Education Statistics' (NCES) Education Demographic and Geographic \nEstimate (EDGE) program develops annually updated point locations \n(latitude and longitude) for public elementary and secondary schools \nincluded in the NCES Common Core of Data (CCD). The NCES EDGE program \ncollaborates with the U.S. Census Bureau's Education Demographic, \nGeographic, and Economic Statistics (EDGE) Branch to develop point \nlocations for schools reported in the annual CCD directory file. The CCD\n program annually collects administrative and fiscal data about all \npublic schools, school districts, and state education agencies in the \nUnited States. The data are supplied by state education agency officials\n and include basic directory and contact information for schools and \nschool districts, as well as characteristics about student demographics,\n number of teachers, school grade span, and various other administrative\n conditions. CCD school and agency point locations are derived from \nreported information about the physical location of schools and agency \nadministrative offices. The point locations and administrative \nattributes in this data layer were developed from the 2017-2018 CCD \ncollection. For more information about NCES school point data, see: <a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>. For more information about these CCD attributes, as well as additional attributes not included, see: <a href='https://nces.ed.gov/ccd/files.asp' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/ccd/files.asp</a>.</span></p><div>Notes:</div><div><table border='1' cellpadding='0' cellspacing='0' style='border-collapse:collapse; border:none;'>\n <tbody><tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-1 or M</span></p>\n  </td>\n  <td style='width:233.75pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are missing.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-2 or N</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are not applicable.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-9</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data do not meet NCES data quality standards.</span></p>\n  </td>\n </tr>\n</tbody></table></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><p><span></span></p><p><span>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></span></p></div></div></div><p></p></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/075dafd36b3443abb45332f1ef396f09/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/075dafd36b3443abb45332f1ef396f09/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::public-school-characteristics-2017-18",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::public-school-characteristics-2017-18"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_ADMINDATA_PUBLICSCH_1718/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_ADMINDATA_PUBLICSCH_1718/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Public School Documentation",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_GEOCODE_PUBLIC_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Public School Documentation"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Public School Characteristics 2017-18",
                     "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::public-school-characteristics-2017-18.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Public School Characteristics 2017-18"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/075dafd36b3443abb45332f1ef396f09/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/075dafd36b3443abb45332f1ef396f09/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/075dafd36b3443abb45332f1ef396f09/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/075dafd36b3443abb45332f1ef396f09/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/075dafd36b3443abb45332f1ef396f09/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/075dafd36b3443abb45332f1ef396f09/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/075dafd36b3443abb45332f1ef396f09/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/075dafd36b3443abb45332f1ef396f09/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "58488bcb-1a7c-45fd-bf20-1b3adaf0b3d3",
+            "issued": "2020-04-27T14:10:09.000Z",
             "keyword": [
                 "ccd",
                 "common-core-of-data",
@@ -10473,25 +10452,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:01.806528",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School Neighborhood Poverty Estimates - Current",
-            "description": "The 2020-2021 School Neighborhood Poverty Estimates are based on school locations from the 2020-2021 Common Core of Data (CCD) school file and income data from families with children ages 5 to 18 in the U.S. Census Bureau\u2019s 2017-2021 American Community Survey (ACS) 5-year collection. The ACS is a continuous household survey that collects social, demographic, economic, and housing information from the population in the United States each month. The Census Bureau calculates the income-to-poverty ratio (IPR) based on money income reported for families relative to the poverty thresholds, which are determined based on the family size and structure. Noncash benefits (such as food stamps and housing subsidies) are excluded, as are capital gains and losses. The IPR is the percentage of family income that is above or below the federal poverty level. The IPR indicator ranges from 0 to a top-coded value of 999. A family with income at the poverty threshold has an IPR value of 100. The estimates in this file reflect the IPR for the neighborhoods around schools which may be different from the neighborhood conditions of students enrolled in schools.<p style='margin:12pt 0in; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif; color:black;'>Collections are available for\nthe following years:</span></p><p>\n\n</p><ul>\n <li><a href='https://nces.maps.arcgis.com/home/item.html?id=10bd90462ec14a53bab1827bc8f533c9' target='_blank' rel='nofollow ugc noopener noreferrer'>School Neighborhood Poverty Estimates, 2020-2021</a><br /></li><li><span style='color:#4C4C4C;'><a href='https://nces.maps.arcgis.com/home/item.html?id=bded6baaf81e43d190946fd1f0469e51' target='_blank' rel='nofollow ugc noopener noreferrer'>School Neighborhood Poverty Estimates, 2019-2020</a></span></li>\n <li><span style='color:black;'><a href='https://nces.maps.arcgis.com/home/item.html?id=8c7c4af648174dc1ad08bcb09303591e' target='_blank' rel='nofollow ugc noopener noreferrer'>School Neighborhood Poverty Estimates, 2018-2019</a></span></li>\n <li><span style='color:black;'><a href='https://nces.maps.arcgis.com/home/item.html?id=82561a1eb6914fa1ac7581520b97bd42' target='_blank' rel='nofollow ugc noopener noreferrer'>School Neighborhood Poverty Estimates, 2017-2018</a></span></li>\n <li><span style='color:black;'><a href='https://nces.maps.arcgis.com/home/item.html?id=eafacbb8ed48433ebdcb2fd9cf93eb82' target='_blank' rel='nofollow ugc noopener noreferrer'>School Neighborhood Poverty Estimates, 2016-2017</a></span></li>\n <li><span style='color:black;'><a href='https://nces.maps.arcgis.com/home/item.html?id=9bed2f9afd86406c88dea2f40e73a658' target='_blank' rel='nofollow ugc noopener noreferrer'>School Neighborhood Poverty Estimates, 2015-2016</a></span></li>\n</ul><p><span>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</span></p>",
-            "modified": "2024-10-19T12:48:00.802784",
-            "accessLevel": "public",
-            "identifier": "464130c3-0031-4393-b88c-8b58dcb8867f",
-            "issued": "2022-04-15T17:34:34.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -10512,78 +10477,92 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Public School Characteristics 2017-18"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "The 2020-2021 School Neighborhood Poverty Estimates are based on school locations from the 2020-2021 Common Core of Data (CCD) school file and income data from families with children ages 5 to 18 in the U.S. Census Bureau\u2019s 2017-2021 American Community Survey (ACS) 5-year collection. The ACS is a continuous household survey that collects social, demographic, economic, and housing information from the population in the United States each month. The Census Bureau calculates the income-to-poverty ratio (IPR) based on money income reported for families relative to the poverty thresholds, which are determined based on the family size and structure. Noncash benefits (such as food stamps and housing subsidies) are excluded, as are capital gains and losses. The IPR is the percentage of family income that is above or below the federal poverty level. The IPR indicator ranges from 0 to a top-coded value of 999. A family with income at the poverty threshold has an IPR value of 100. The estimates in this file reflect the IPR for the neighborhoods around schools which may be different from the neighborhood conditions of students enrolled in schools.<p style='margin:12pt 0in; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'><span style='font-size:11.0pt; font-family:&quot;Calibri&quot;,sans-serif; color:black;'>Collections are available for\nthe following years:</span></p><p>\n\n</p><ul>\n <li><a href='https://nces.maps.arcgis.com/home/item.html?id=10bd90462ec14a53bab1827bc8f533c9' target='_blank' rel='nofollow ugc noopener noreferrer'>School Neighborhood Poverty Estimates, 2020-2021</a><br /></li><li><span style='color:#4C4C4C;'><a href='https://nces.maps.arcgis.com/home/item.html?id=bded6baaf81e43d190946fd1f0469e51' target='_blank' rel='nofollow ugc noopener noreferrer'>School Neighborhood Poverty Estimates, 2019-2020</a></span></li>\n <li><span style='color:black;'><a href='https://nces.maps.arcgis.com/home/item.html?id=8c7c4af648174dc1ad08bcb09303591e' target='_blank' rel='nofollow ugc noopener noreferrer'>School Neighborhood Poverty Estimates, 2018-2019</a></span></li>\n <li><span style='color:black;'><a href='https://nces.maps.arcgis.com/home/item.html?id=82561a1eb6914fa1ac7581520b97bd42' target='_blank' rel='nofollow ugc noopener noreferrer'>School Neighborhood Poverty Estimates, 2017-2018</a></span></li>\n <li><span style='color:black;'><a href='https://nces.maps.arcgis.com/home/item.html?id=eafacbb8ed48433ebdcb2fd9cf93eb82' target='_blank' rel='nofollow ugc noopener noreferrer'>School Neighborhood Poverty Estimates, 2016-2017</a></span></li>\n <li><span style='color:black;'><a href='https://nces.maps.arcgis.com/home/item.html?id=9bed2f9afd86406c88dea2f40e73a658' target='_blank' rel='nofollow ugc noopener noreferrer'>School Neighborhood Poverty Estimates, 2015-2016</a></span></li>\n</ul><p><span>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</span></p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/45baf5309f384bb98cb50d31526be680/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/45baf5309f384bb98cb50d31526be680/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-neighborhood-poverty-estimates-current",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-neighborhood-poverty-estimates-current"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://services1.arcgis.com/Ua5sjt3LWTPigjyD/arcgis/rest/services/School_Neighborhood_Poverty_Estimates_Current/FeatureServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://services1.arcgis.com/Ua5sjt3LWTPigjyD/arcgis/rest/services/School_Neighborhood_Poverty_Estimates_Current/FeatureServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "School Neighborhood Poverty Estimates",
                     "description": "Technical Documentation",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_SIDE_PUBSCH_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "School Neighborhood Poverty Estimates"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "School Neighborhood Poverty Estimates",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_SIDE1721_PUBSCHS2021.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "School Neighborhood Poverty Estimates"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/45baf5309f384bb98cb50d31526be680/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/45baf5309f384bb98cb50d31526be680/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/45baf5309f384bb98cb50d31526be680/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/45baf5309f384bb98cb50d31526be680/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/45baf5309f384bb98cb50d31526be680/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/45baf5309f384bb98cb50d31526be680/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/45baf5309f384bb98cb50d31526be680/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/45baf5309f384bb98cb50d31526be680/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "464130c3-0031-4393-b88c-8b58dcb8867f",
+            "issued": "2022-04-15T17:34:34.000Z",
             "keyword": [
                 "ccd",
                 "common-core-of-data",
@@ -10593,25 +10572,11 @@
                 "side",
                 "spatially-interpolated-demographic-estimates"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:48:00.802784",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Postsecondary School Locations 2022-23",
-            "description": "<div style='text-align:Left;'><p>The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimates (EDGE) program develops annually updated point locations (latitude and longitude) for postsecondary institutions included in the NCES Integrated Postsecondary Education Data System (IPEDS). The IPEDS program annually collects information about enrollments, program completions, graduation rates, faculty and staff, finances, institutional prices, and student financial aid from colleges, universities, and technical and vocational institutions that participate in federal student financial aid programs under the Higher Education Act of 1965 (as amended). The NCES EDGE program uses address information reported in the annually updated IPEDS directory file to develop point locations for all institutions reported in IPEDS. The point locations in this data layer were developed from the 2022-2023 IPEDS collection. For more information about NCES school point data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>.</p><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</p></div>",
-            "modified": "2024-10-19T12:47:59.878749",
-            "accessLevel": "public",
-            "identifier": "f6e1f582-a28c-4680-a896-ed09f0762d59",
-            "issued": "2023-12-21T16:44:12.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -10632,63 +10597,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "School Neighborhood Poverty Estimates - Current"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><p>The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimates (EDGE) program develops annually updated point locations (latitude and longitude) for postsecondary institutions included in the NCES Integrated Postsecondary Education Data System (IPEDS). The IPEDS program annually collects information about enrollments, program completions, graduation rates, faculty and staff, finances, institutional prices, and student financial aid from colleges, universities, and technical and vocational institutions that participate in federal student financial aid programs under the Higher Education Act of 1965 (as amended). The NCES EDGE program uses address information reported in the annually updated IPEDS directory file to develop point locations for all institutions reported in IPEDS. The point locations in this data layer were developed from the 2022-2023 IPEDS collection. For more information about NCES school point data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>.</p><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</p></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/92e4b742b59f4b90b3af85e444a912f7/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/92e4b742b59f4b90b3af85e444a912f7/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::postsecondary-school-locations-2022-23",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::postsecondary-school-locations-2022-23"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Postsecondary_School_Locations/EDGE_GEOCODE_POSTSECONDARYSCH_2223/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Postsecondary_School_Locations/EDGE_GEOCODE_POSTSECONDARYSCH_2223/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/92e4b742b59f4b90b3af85e444a912f7/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/92e4b742b59f4b90b3af85e444a912f7/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/92e4b742b59f4b90b3af85e444a912f7/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/92e4b742b59f4b90b3af85e444a912f7/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/92e4b742b59f4b90b3af85e444a912f7/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/92e4b742b59f4b90b3af85e444a912f7/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/92e4b742b59f4b90b3af85e444a912f7/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/92e4b742b59f4b90b3af85e444a912f7/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "f6e1f582-a28c-4680-a896-ed09f0762d59",
+            "issued": "2023-12-21T16:44:12.000Z",
             "keyword": [
                 "edge",
                 "education",
@@ -10704,25 +10683,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:59.878749",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Postsecondary School Locations 2021-22",
-            "description": "<div style='text-align:Left;'><p>The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimates (EDGE) program develops annually updated point locations (latitude and longitude) for postsecondary institutions included in the NCES Integrated Postsecondary Education Data System (IPEDS). The IPEDS program annually collects information about enrollments, program completions, graduation rates, faculty and staff, finances, institutional prices, and student financial aid from colleges, universities, and technical and vocational institutions that participate in federal student financial aid programs under the Higher Education Act of 1965 (as amended). The NCES EDGE program uses address information reported in the annually updated IPEDS directory file to develop point locations for all institutions reported in IPEDS.\u00a0<span>The point locations in this data layer were developed from the 2021-2022 IPEDS collection. For more information about NCES school point data, see: <a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>.</span></p><p><span><span>All information contained in this file is in the public \ndomain. Data users are advised to review NCES program documentation and \nfeature class metadata to understand the limitations and appropriate use\n of these data.</span></span><span></span></p></div>",
-            "modified": "2024-10-19T12:47:58.972931",
-            "accessLevel": "public",
-            "identifier": "93d2622b-73dd-445e-96f7-6ecaba24fd24",
-            "issued": "2022-05-05T14:45:05.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -10743,77 +10708,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Postsecondary School Locations 2022-23"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><p>The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimates (EDGE) program develops annually updated point locations (latitude and longitude) for postsecondary institutions included in the NCES Integrated Postsecondary Education Data System (IPEDS). The IPEDS program annually collects information about enrollments, program completions, graduation rates, faculty and staff, finances, institutional prices, and student financial aid from colleges, universities, and technical and vocational institutions that participate in federal student financial aid programs under the Higher Education Act of 1965 (as amended). The NCES EDGE program uses address information reported in the annually updated IPEDS directory file to develop point locations for all institutions reported in IPEDS.\u00a0<span>The point locations in this data layer were developed from the 2021-2022 IPEDS collection. For more information about NCES school point data, see: <a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>.</span></p><p><span><span>All information contained in this file is in the public \ndomain. Data users are advised to review NCES program documentation and \nfeature class metadata to understand the limitations and appropriate use\n of these data.</span></span><span></span></p></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/49cd0352fe2546a99cbeb8ec332d9354/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/49cd0352fe2546a99cbeb8ec332d9354/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::postsecondary-school-locations-2021-22",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::postsecondary-school-locations-2021-22"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Postsecondary_School_Locations/EDGE_GEOCODE_POSTSECONDARYSCH_2122/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Postsecondary_School_Locations/EDGE_GEOCODE_POSTSECONDARYSCH_2122/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Geocodes: Postsecondary Schools",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_GEOCODE_POSTSEC_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Postsecondary Schools"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Geocodes: Postsecondary Schools",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_POSTSECONDARYSCH_2122.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Postsecondary Schools"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/49cd0352fe2546a99cbeb8ec332d9354/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/49cd0352fe2546a99cbeb8ec332d9354/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/49cd0352fe2546a99cbeb8ec332d9354/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/49cd0352fe2546a99cbeb8ec332d9354/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/49cd0352fe2546a99cbeb8ec332d9354/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/49cd0352fe2546a99cbeb8ec332d9354/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/49cd0352fe2546a99cbeb8ec332d9354/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/49cd0352fe2546a99cbeb8ec332d9354/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "93d2622b-73dd-445e-96f7-6ecaba24fd24",
+            "issued": "2022-05-05T14:45:05.000Z",
             "keyword": [
                 "edge",
                 "education",
@@ -10829,25 +10808,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:58.972931",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Postsecondary School Locations 2018-19",
-            "description": "<div>The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for postsecondary institutions included in the NCES Integrated Postsecondary Education Data System (IPEDS). The IPEDS program annually collects information about enrollments, program completions, graduation rates, faculty and staff, finances, institutional prices, and student financial aid from every college, university, and technical and vocational institution that participates in federal student financial aid programs under the Higher Education Act of 1965 (as amended). IPEDS school point locations are derived from reported information about the physical location of schools. The NCES EDGE program collaborates with the U.S. Census Bureau's Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for schools reported in the annual IPEDS file. The point locations in this data layer were developed from the 2018-2019 IPEDS collection. For more information about NCES school point data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>.</div><div><br />All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div>",
-            "modified": "2024-10-19T12:47:57.601684",
-            "accessLevel": "public",
-            "identifier": "50bc41a3-0eb9-448e-9756-dd811b242eb9",
-            "issued": "2020-03-17T20:54:29.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -10868,77 +10833,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Postsecondary School Locations 2021-22"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div>The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for postsecondary institutions included in the NCES Integrated Postsecondary Education Data System (IPEDS). The IPEDS program annually collects information about enrollments, program completions, graduation rates, faculty and staff, finances, institutional prices, and student financial aid from every college, university, and technical and vocational institution that participates in federal student financial aid programs under the Higher Education Act of 1965 (as amended). IPEDS school point locations are derived from reported information about the physical location of schools. The NCES EDGE program collaborates with the U.S. Census Bureau's Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for schools reported in the annual IPEDS file. The point locations in this data layer were developed from the 2018-2019 IPEDS collection. For more information about NCES school point data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>.</div><div><br />All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/6aa17db388b34c6c9d6ae040993cd99d/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/6aa17db388b34c6c9d6ae040993cd99d/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::postsecondary-school-locations-2018-19",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::postsecondary-school-locations-2018-19"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Postsecondary_School_Locations/EDGE_GEOCODE_POSTSECONDARYSCH_1819/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Postsecondary_School_Locations/EDGE_GEOCODE_POSTSECONDARYSCH_1819/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Geocodes: Postsecondary Schools",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_GEOCODE_POSTSEC_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Postsecondary Schools"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "EDGE_GEOCODE_POSTSECONDARYSCH_1819",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_POSTSECONDARYSCH_1819.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "EDGE_GEOCODE_POSTSECONDARYSCH_1819"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6aa17db388b34c6c9d6ae040993cd99d/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6aa17db388b34c6c9d6ae040993cd99d/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6aa17db388b34c6c9d6ae040993cd99d/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6aa17db388b34c6c9d6ae040993cd99d/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6aa17db388b34c6c9d6ae040993cd99d/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6aa17db388b34c6c9d6ae040993cd99d/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6aa17db388b34c6c9d6ae040993cd99d/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6aa17db388b34c6c9d6ae040993cd99d/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "50bc41a3-0eb9-448e-9756-dd811b242eb9",
+            "issued": "2020-03-17T20:54:29.000Z",
             "keyword": [
                 "department-of-education",
                 "edge",
@@ -10950,25 +10929,11 @@
                 "postsecondary",
                 "schools"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:57.601684",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Postsecondary School Locations 2017-18",
-            "description": "<div style='text-align:Left;'><div><div><p><span>The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for postsecondary institutions included in the NCES Integrated Postsecondary Education Data System (IPEDS). The IPEDS program annually collects information about enrollments, program completions, graduation rates, faculty and staff, finances, institutional prices, and student financial aid from every college, university, and technical and vocational institution that participates in federal student financial aid programs under the Higher Education Act of 1965 (as amended). IPEDS school point locations are derived from reported information about the physical location of schools. The NCES EDGE program collaborates with the U.S. Census Bureau's Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for schools reported in the annual IPEDS file. The point locations in this data layer were developed from the 2017-2018 IPEDS collection. For more information about NCES school point data, see:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a><span>. <br /></span></p><p><span>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></span></p></div></div></div>",
-            "modified": "2024-10-19T12:47:56.747744",
-            "accessLevel": "public",
-            "identifier": "a3c3cab5-f3a6-48d4-8aac-762faaee266b",
-            "issued": "2020-03-20T20:55:59.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -10989,77 +10954,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Postsecondary School Locations 2018-19"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><div><div><p><span>The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for postsecondary institutions included in the NCES Integrated Postsecondary Education Data System (IPEDS). The IPEDS program annually collects information about enrollments, program completions, graduation rates, faculty and staff, finances, institutional prices, and student financial aid from every college, university, and technical and vocational institution that participates in federal student financial aid programs under the Higher Education Act of 1965 (as amended). IPEDS school point locations are derived from reported information about the physical location of schools. The NCES EDGE program collaborates with the U.S. Census Bureau's Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for schools reported in the annual IPEDS file. The point locations in this data layer were developed from the 2017-2018 IPEDS collection. For more information about NCES school point data, see:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a><span>. <br /></span></p><p><span>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></span></p></div></div></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/adc0c93f5b004246b186e90f4b43830f/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/adc0c93f5b004246b186e90f4b43830f/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::postsecondary-school-locations-2017-18",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::postsecondary-school-locations-2017-18"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Postsecondary_School_Locations/EDGE_GEOCODE_POSTSECONDARYSCH_1718/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Postsecondary_School_Locations/EDGE_GEOCODE_POSTSECONDARYSCH_1718/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Geocodes: Postsecondary Schools",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_GEOCODE_POSTSEC_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Postsecondary Schools"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Geocodes: Postsecondary Schools",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_POSTSECONDARYSCH_1718.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Postsecondary Schools"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/adc0c93f5b004246b186e90f4b43830f/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/adc0c93f5b004246b186e90f4b43830f/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/adc0c93f5b004246b186e90f4b43830f/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/adc0c93f5b004246b186e90f4b43830f/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/adc0c93f5b004246b186e90f4b43830f/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/adc0c93f5b004246b186e90f4b43830f/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/adc0c93f5b004246b186e90f4b43830f/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/adc0c93f5b004246b186e90f4b43830f/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "a3c3cab5-f3a6-48d4-8aac-762faaee266b",
+            "issued": "2020-03-20T20:55:59.000Z",
             "keyword": [
                 "edge",
                 "education",
@@ -11075,25 +11054,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:56.747744",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Postsecondary School Locations 2016-17",
-            "description": "<div style='text-align:Left;'><p>The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations\u00a0<span style='background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>(latitude and longitude)\u00a0</span>for postsecondary institutions included in the NCES\u00a0<span style='background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>Integrated Postsecondary Education Data System (IPEDS)</span>. The IPEDS program annually collects information about enrollments, program completions, graduation rates, faculty and staff, finances, institutional prices, and student financial aid from every college, university, and technical and vocational institution that participates in federal student financial aid programs under the Higher Education Act of 1965 (as amended).\u00a0\u00a0The NCES EDGE program uses address information reported in the annually updated IPEDS directory file and collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for all institutions reported in IPEDS. The point locations in this data layer were developed from the 2016-2017 IPEDS collection. For more information about NCES school point data, see:\u00a0\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' rel='nofollow ugc'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>. <br /></p><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></p></div>",
-            "modified": "2024-10-19T12:47:55.926772",
-            "accessLevel": "public",
-            "identifier": "0865a36f-cfcc-4037-8c8a-34a6bbec8c6a",
-            "issued": "2020-03-20T21:08:00.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -11114,77 +11079,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Postsecondary School Locations 2017-18"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><p>The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations\u00a0<span style='background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>(latitude and longitude)\u00a0</span>for postsecondary institutions included in the NCES\u00a0<span style='background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>Integrated Postsecondary Education Data System (IPEDS)</span>. The IPEDS program annually collects information about enrollments, program completions, graduation rates, faculty and staff, finances, institutional prices, and student financial aid from every college, university, and technical and vocational institution that participates in federal student financial aid programs under the Higher Education Act of 1965 (as amended).\u00a0\u00a0The NCES EDGE program uses address information reported in the annually updated IPEDS directory file and collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for all institutions reported in IPEDS. The point locations in this data layer were developed from the 2016-2017 IPEDS collection. For more information about NCES school point data, see:\u00a0\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' rel='nofollow ugc'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>. <br /></p><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></p></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/72d9d1167cad4b619fa23f36f05e8766/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/72d9d1167cad4b619fa23f36f05e8766/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::postsecondary-school-locations-2016-17",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::postsecondary-school-locations-2016-17"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Postsecondary_School_Locations/EDGE_GEOCODE_POSTSECONDARYSCH_1617/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Postsecondary_School_Locations/EDGE_GEOCODE_POSTSECONDARYSCH_1617/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Geocodes: Postsecondary Schools",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_GEOCODE_POSTSEC_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Postsecondary Schools"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Geocodes: Postsecondary Schools",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_POSTSECONDARYSCH_1617.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Postsecondary Schools"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/72d9d1167cad4b619fa23f36f05e8766/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/72d9d1167cad4b619fa23f36f05e8766/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/72d9d1167cad4b619fa23f36f05e8766/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/72d9d1167cad4b619fa23f36f05e8766/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/72d9d1167cad4b619fa23f36f05e8766/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/72d9d1167cad4b619fa23f36f05e8766/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/72d9d1167cad4b619fa23f36f05e8766/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/72d9d1167cad4b619fa23f36f05e8766/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "0865a36f-cfcc-4037-8c8a-34a6bbec8c6a",
+            "issued": "2020-03-20T21:08:00.000Z",
             "keyword": [
                 "edge",
                 "education",
@@ -11200,25 +11179,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:55.926772",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Postsecondary School Locations 2015-16",
-            "description": "<div>The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations\u00a0<span style='background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>(latitude and longitude)\u00a0</span>for postsecondary institutions included in the NCES\u00a0<span style='background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>Integrated Postsecondary Education Data System (IPEDS)</span>. The IPEDS program annually collects information about enrollments, program completions, graduation rates, faculty and staff, finances, institutional prices, and student financial aid from every college, university, and technical and vocational institution that participates in federal student financial aid programs under the Higher Education Act of 1965 (as amended).\u00a0\u00a0The NCES EDGE program uses address information reported in the annually updated IPEDS directory file and collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for all institutions reported in IPEDS. The point locations in this data layer were developed from the 2015-2016 IPEDS collection. For more information about NCES school point data, see:\u00a0\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' rel='nofollow ugc'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>.</div><div><br /></div><div>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div>",
-            "modified": "2024-10-19T12:47:55.077465",
-            "accessLevel": "public",
-            "identifier": "13522779-db95-4800-adba-5b7476ac776d",
-            "issued": "2020-03-20T21:12:40.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -11239,77 +11204,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Postsecondary School Locations 2016-17"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div>The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations\u00a0<span style='background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>(latitude and longitude)\u00a0</span>for postsecondary institutions included in the NCES\u00a0<span style='background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>Integrated Postsecondary Education Data System (IPEDS)</span>. The IPEDS program annually collects information about enrollments, program completions, graduation rates, faculty and staff, finances, institutional prices, and student financial aid from every college, university, and technical and vocational institution that participates in federal student financial aid programs under the Higher Education Act of 1965 (as amended).\u00a0\u00a0The NCES EDGE program uses address information reported in the annually updated IPEDS directory file and collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for all institutions reported in IPEDS. The point locations in this data layer were developed from the 2015-2016 IPEDS collection. For more information about NCES school point data, see:\u00a0\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' rel='nofollow ugc'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>.</div><div><br /></div><div>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/809cc7caddf34d3692970c9a781dac03/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/809cc7caddf34d3692970c9a781dac03/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::postsecondary-school-locations-2015-16",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::postsecondary-school-locations-2015-16"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Postsecondary_School_Locations/EDGE_GEOCODE_POSTSECONDARYSCH_1516/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Postsecondary_School_Locations/EDGE_GEOCODE_POSTSECONDARYSCH_1516/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Geocodes: Postsecondary Schools",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_GEOCODE_POSTSEC_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Postsecondary Schools"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Geocodes: Postsecondary Schools",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_POSTSECONDARYSCH_1516.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Postsecondary Schools"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/809cc7caddf34d3692970c9a781dac03/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/809cc7caddf34d3692970c9a781dac03/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/809cc7caddf34d3692970c9a781dac03/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/809cc7caddf34d3692970c9a781dac03/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/809cc7caddf34d3692970c9a781dac03/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/809cc7caddf34d3692970c9a781dac03/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/809cc7caddf34d3692970c9a781dac03/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/809cc7caddf34d3692970c9a781dac03/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "13522779-db95-4800-adba-5b7476ac776d",
+            "issued": "2020-03-20T21:12:40.000Z",
             "keyword": [
                 "edge",
                 "education-demographic-and-geographic-estimates-program",
@@ -11320,25 +11299,11 @@
                 "nces",
                 "postsecondary"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:55.077465",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School District Characteristics 2021-22",
-            "description": "<p style='margin-bottom:0in;'></p><p style='margin-bottom:0in;'>The\nNational Center for Education Statistics\u2019 (NCES) Education Demographic and\nGeographic Estimate (EDGE) program develops annually updated school district\nboundary composite files that include public elementary, secondary, and unified\nschool district boundaries clipped to the U.S. shoreline. School districts are\nspecial-purpose governments and administrative units designed by state and\nlocal officials to provide public education for local residents. District\nboundaries are collected for NCES by the U.S. Census Bureau to develop\ndemographic estimates and to support educational research and program\nadministration. The NCES Common Core of Data (CCD) program is an annual\ncollection of basic administrative characteristics for all public schools,\nschool districts, and state education agencies in the United States. These\ncharacteristics are reported by state education officials and include directory\ninformation, number of students, number of teachers, grade span, and other\nconditions. The administrative attributes in this layer were developed from the\n2021-2022 CCD collection. For more information about NCES school district\nboundaries, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries' rel='nofollow ugc'>https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries</a>.\nFor more information about CCD school district attributes, see:\u00a0<a href='https://nces.ed.gov/ccd/files.asp' rel='nofollow ugc'>https://nces.ed.gov/ccd/files.asp</a>.</p><p style='margin-bottom:0in;'><br /></p>\n\n<p style='margin-bottom:0in;'><span>Notes:</span></p>\n\n<table border='0' cellpadding='0' cellspacing='0' style='border-collapse:collapse;'>\n <tbody><tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin:0in;'>-1 or M</p></td><td style='width:337.25pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='450'><p style='margin:0in;'>Indicates that the data are missing.</p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin:0in;'>-2 or N</p>\n  </td>\n  <td style='width:337.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='450'>\n  <p style='margin:0in;'>Indicates that the data are not applicable.</p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin:0in;'>-9</p>\n  </td>\n  <td style='width:337.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='450'>\n  <p style='margin:0in;'>Indicates that the data do not meet NCES data quality standards.</p>\n  </td>\n </tr>\n</tbody></table>\n\n<p>All\ninformation contained in this file is in the public domain. Data users are\nadvised to review NCES program documentation and feature class metadata to\nunderstand the limitations and appropriate use of these data.</p>",
-            "modified": "2024-10-19T12:47:54.252104",
-            "accessLevel": "public",
-            "identifier": "f9a5b5b9-59ec-43d0-87f2-a7fe1666bcc7",
-            "issued": "2023-04-04T11:23:53.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -11359,63 +11324,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Postsecondary School Locations 2015-16"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<p style='margin-bottom:0in;'></p><p style='margin-bottom:0in;'>The\nNational Center for Education Statistics\u2019 (NCES) Education Demographic and\nGeographic Estimate (EDGE) program develops annually updated school district\nboundary composite files that include public elementary, secondary, and unified\nschool district boundaries clipped to the U.S. shoreline. School districts are\nspecial-purpose governments and administrative units designed by state and\nlocal officials to provide public education for local residents. District\nboundaries are collected for NCES by the U.S. Census Bureau to develop\ndemographic estimates and to support educational research and program\nadministration. The NCES Common Core of Data (CCD) program is an annual\ncollection of basic administrative characteristics for all public schools,\nschool districts, and state education agencies in the United States. These\ncharacteristics are reported by state education officials and include directory\ninformation, number of students, number of teachers, grade span, and other\nconditions. The administrative attributes in this layer were developed from the\n2021-2022 CCD collection. For more information about NCES school district\nboundaries, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries' rel='nofollow ugc'>https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries</a>.\nFor more information about CCD school district attributes, see:\u00a0<a href='https://nces.ed.gov/ccd/files.asp' rel='nofollow ugc'>https://nces.ed.gov/ccd/files.asp</a>.</p><p style='margin-bottom:0in;'><br /></p>\n\n<p style='margin-bottom:0in;'><span>Notes:</span></p>\n\n<table border='0' cellpadding='0' cellspacing='0' style='border-collapse:collapse;'>\n <tbody><tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin:0in;'>-1 or M</p></td><td style='width:337.25pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='450'><p style='margin:0in;'>Indicates that the data are missing.</p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin:0in;'>-2 or N</p>\n  </td>\n  <td style='width:337.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='450'>\n  <p style='margin:0in;'>Indicates that the data are not applicable.</p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin:0in;'>-9</p>\n  </td>\n  <td style='width:337.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='450'>\n  <p style='margin:0in;'>Indicates that the data do not meet NCES data quality standards.</p>\n  </td>\n </tr>\n</tbody></table>\n\n<p>All\ninformation contained in this file is in the public domain. Data users are\nadvised to review NCES program documentation and feature class metadata to\nunderstand the limitations and appropriate use of these data.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/71710fd5ae9a43768f221c89e8ff7bb0/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/71710fd5ae9a43768f221c89e8ff7bb0/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-characteristics-2021-22",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-characteristics-2021-22"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/School_District_Boundaries/EDGE_ADMINDATA_SCHOOLDISTRICTS_SY2122/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/School_District_Boundaries/EDGE_ADMINDATA_SCHOOLDISTRICTS_SY2122/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/71710fd5ae9a43768f221c89e8ff7bb0/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/71710fd5ae9a43768f221c89e8ff7bb0/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/71710fd5ae9a43768f221c89e8ff7bb0/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/71710fd5ae9a43768f221c89e8ff7bb0/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/71710fd5ae9a43768f221c89e8ff7bb0/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/71710fd5ae9a43768f221c89e8ff7bb0/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/71710fd5ae9a43768f221c89e8ff7bb0/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/71710fd5ae9a43768f221c89e8ff7bb0/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "f9a5b5b9-59ec-43d0-87f2-a7fe1666bcc7",
+            "issued": "2023-04-04T11:23:53.000Z",
             "keyword": [
                 "ccd",
                 "common-core-of-data",
@@ -11429,25 +11408,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:54.252104",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School District Characteristics 2018-19",
-            "description": "<div style='text-align:Left;'><p>The National Center for Education Statistics\u2019 (NCES) Education \nDemographic and Geographic Estimate (EDGE) program develops annually \nupdated school district boundary composite files that include public \nelementary, secondary, and unified school district boundaries clipped to\n the U.S. shoreline. School districts are special-purpose administrative\n units designed by state and local officials to provide public education\n for local residents. District boundaries are collected for NCES by the \nU.S. Census Bureau to develop demographic estimates and to support \neducational research and program administration. The NCES Common Core of\n Data (CCD) program is an annual collection of basic administrative \ncharacteristics for all public schools, school districts, and state \neducation agencies in the United States. These characteristics are \nreported by state education officials and include directory information,\n number of students, number of teachers, grade span, and other \nconditions. The administrative attributes in this layer were developed \nfrom the 2018-2019 CCD collection. For more information about NCES \nschool district boundaries, see: <a href='https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries</a>. For more information about CCD school district attributes, see: <a href='https://nces.ed.gov/ccd/files.asp' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/ccd/files.asp</a>.</p><div>Notes:</div><div><table border='1' cellpadding='0' cellspacing='0' style='border-collapse:collapse; border:none;'>\n <tbody><tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-1 or M</span></p>\n  </td>\n  <td style='width:233.75pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are missing.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-2 or N</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are not applicable.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-9</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data do not meet NCES data quality standards.</span></p>\n  </td>\n </tr>\n</tbody></table></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><p></p><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></p></div>",
-            "modified": "2024-10-19T12:47:53.292469",
-            "accessLevel": "public",
-            "identifier": "05b61761-b000-4423-8e92-1bbcf262b80b",
-            "issued": "2020-08-10T21:09:03.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -11468,77 +11433,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "School District Characteristics 2021-22"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><p>The National Center for Education Statistics\u2019 (NCES) Education \nDemographic and Geographic Estimate (EDGE) program develops annually \nupdated school district boundary composite files that include public \nelementary, secondary, and unified school district boundaries clipped to\n the U.S. shoreline. School districts are special-purpose administrative\n units designed by state and local officials to provide public education\n for local residents. District boundaries are collected for NCES by the \nU.S. Census Bureau to develop demographic estimates and to support \neducational research and program administration. The NCES Common Core of\n Data (CCD) program is an annual collection of basic administrative \ncharacteristics for all public schools, school districts, and state \neducation agencies in the United States. These characteristics are \nreported by state education officials and include directory information,\n number of students, number of teachers, grade span, and other \nconditions. The administrative attributes in this layer were developed \nfrom the 2018-2019 CCD collection. For more information about NCES \nschool district boundaries, see: <a href='https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries</a>. For more information about CCD school district attributes, see: <a href='https://nces.ed.gov/ccd/files.asp' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/ccd/files.asp</a>.</p><div>Notes:</div><div><table border='1' cellpadding='0' cellspacing='0' style='border-collapse:collapse; border:none;'>\n <tbody><tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-1 or M</span></p>\n  </td>\n  <td style='width:233.75pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are missing.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-2 or N</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are not applicable.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-9</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data do not meet NCES data quality standards.</span></p>\n  </td>\n </tr>\n</tbody></table></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><p></p><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></p></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/be3f7956f07849369e75f7008b2899d3/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/be3f7956f07849369e75f7008b2899d3/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-characteristics-2018-19",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-characteristics-2018-19"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/School_District_Boundaries/EDGE_ADMINDATA_SCHOOLDISTRICTS_SY1819/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/School_District_Boundaries/EDGE_ADMINDATA_SCHOOLDISTRICTS_SY1819/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "School District Documentation",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_SDBOUNDARIES_COMPOSITE_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "School District Documentation"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "School District Characteristics 2018-19",
                     "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-characteristics-2018-19.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "School District Characteristics 2018-19"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/be3f7956f07849369e75f7008b2899d3/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/be3f7956f07849369e75f7008b2899d3/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/be3f7956f07849369e75f7008b2899d3/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/be3f7956f07849369e75f7008b2899d3/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/be3f7956f07849369e75f7008b2899d3/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/be3f7956f07849369e75f7008b2899d3/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/be3f7956f07849369e75f7008b2899d3/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/be3f7956f07849369e75f7008b2899d3/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "05b61761-b000-4423-8e92-1bbcf262b80b",
+            "issued": "2020-08-10T21:09:03.000Z",
             "keyword": [
                 "ccd",
                 "common-core-of-data",
@@ -11553,25 +11532,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:53.292469",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School District Boundaries - Current",
-            "description": "<p></p><p></p><p></p><p>The National Center for Education Statistics\u2019 (NCES)\nEducation Demographic and Geographic Estimate (EDGE) program develops annually\nupdated school district boundary composite files that include public\nelementary, secondary, and unified school district boundaries clipped to the\nU.S. shoreline. School districts are special-purpose governments and\nadministrative units designed by state and local officials to organize and\nprovide public education for local residents. District boundaries are collected\nfor NCES by the U.S. Census Bureau to support educational research and program\nadministration, and the boundaries are essential for constructing\ndistrict-level estimates of the number of children in poverty.</p>\n\n<p>The Census Bureau\u2019s School District Boundary Review program\n(SDRP) (https://www.census.gov/programs-surveys/sdrp.html) obtains the\nboundaries, names, and grade ranges from state officials, and integrates these\nupdates into Census TIGER. Census TIGER boundaries include legal maritime\nbuffers for coastal areas by default, but the NCES composite file removes these\nbuffers to facilitate broader use and cleaner cartographic representation. For\nmore information about NCES school district boundary data, see: <a href='https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries' rel='nofollow ugc'>https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries</a>.</p>\n\n<p>Collections are available for the following years:<br /></p><ul><li><a href='https://nces.maps.arcgis.com/home/item.html?id=10ea737b49f149f084a64e221f487c99' rel='nofollow ugc'>SY\n2022-23 TL 23</a></li><li><a href='https://nces.maps.arcgis.com/home/item.html?id=6afefd8dda8048d18444b8f06fad6930' rel='nofollow ugc'>SY\n2021-22 TL 22</a></li><li><a href='https://nces.maps.arcgis.com/home/item.html?id=57648a58b8e74acb80225485c18c4f63' rel='nofollow ugc'>SY\n2020-21 TL 21</a></li><li><a href='https://nces.maps.arcgis.com/home/item.html?id=a55870b7904848f793590998559f86bb' rel='nofollow ugc'>SY\n2019-20 TL 20</a></li><li><a href='https://nces.maps.arcgis.com/home/item.html?id=fc0aaa02bb72455aa276e8c4efa07e1b' rel='nofollow ugc'>SY\n2018-19 TL 19</a></li><li><a href='https://nces.maps.arcgis.com/home/item.html?id=29ccd69e8d0b438195cbf9e1f317ea60' rel='nofollow ugc'>SY\n2017-18 TL 18</a></li><li><a href='https://nces.maps.arcgis.com/home/item.html?id=cdde8df963b44233a20aedc495fdb20b' rel='nofollow ugc'>SY\n2015-16 TL 17</a></li><li><a href='https://nces.maps.arcgis.com/home/item.html?id=37e60391180e47639445e11c67d9e990' rel='nofollow ugc'>SY\n2015-16 TL 16</a></li><li><a href='https://nces.maps.arcgis.com/home/item.html?id=acb0e63f84b6437c88a05c62e7b4aa4f' rel='nofollow ugc'>SY\n2013-14 TL 15</a></li><li><a href='https://nces.maps.arcgis.com/home/item.html?id=9e3cbc1863d64545ad1936f49374927e' rel='nofollow ugc'>SY\n2013-14 TL 14</a></li></ul><p>All information contained in this file is in the public\ndomain. Data users are advised to review NCES program documentation and feature\nclass metadata to understand the limitations and appropriate use of these data.</p>",
-            "modified": "2024-10-19T12:47:52.112866",
-            "accessLevel": "public",
-            "identifier": "f42fb273-8624-4835-9fd0-960346cdd0d7",
-            "issued": "2020-03-16T13:18:41.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -11592,63 +11557,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "School District Characteristics 2018-19"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<p></p><p></p><p></p><p>The National Center for Education Statistics\u2019 (NCES)\nEducation Demographic and Geographic Estimate (EDGE) program develops annually\nupdated school district boundary composite files that include public\nelementary, secondary, and unified school district boundaries clipped to the\nU.S. shoreline. School districts are special-purpose governments and\nadministrative units designed by state and local officials to organize and\nprovide public education for local residents. District boundaries are collected\nfor NCES by the U.S. Census Bureau to support educational research and program\nadministration, and the boundaries are essential for constructing\ndistrict-level estimates of the number of children in poverty.</p>\n\n<p>The Census Bureau\u2019s School District Boundary Review program\n(SDRP) (https://www.census.gov/programs-surveys/sdrp.html) obtains the\nboundaries, names, and grade ranges from state officials, and integrates these\nupdates into Census TIGER. Census TIGER boundaries include legal maritime\nbuffers for coastal areas by default, but the NCES composite file removes these\nbuffers to facilitate broader use and cleaner cartographic representation. For\nmore information about NCES school district boundary data, see: <a href='https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries' rel='nofollow ugc'>https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries</a>.</p>\n\n<p>Collections are available for the following years:<br /></p><ul><li><a href='https://nces.maps.arcgis.com/home/item.html?id=10ea737b49f149f084a64e221f487c99' rel='nofollow ugc'>SY\n2022-23 TL 23</a></li><li><a href='https://nces.maps.arcgis.com/home/item.html?id=6afefd8dda8048d18444b8f06fad6930' rel='nofollow ugc'>SY\n2021-22 TL 22</a></li><li><a href='https://nces.maps.arcgis.com/home/item.html?id=57648a58b8e74acb80225485c18c4f63' rel='nofollow ugc'>SY\n2020-21 TL 21</a></li><li><a href='https://nces.maps.arcgis.com/home/item.html?id=a55870b7904848f793590998559f86bb' rel='nofollow ugc'>SY\n2019-20 TL 20</a></li><li><a href='https://nces.maps.arcgis.com/home/item.html?id=fc0aaa02bb72455aa276e8c4efa07e1b' rel='nofollow ugc'>SY\n2018-19 TL 19</a></li><li><a href='https://nces.maps.arcgis.com/home/item.html?id=29ccd69e8d0b438195cbf9e1f317ea60' rel='nofollow ugc'>SY\n2017-18 TL 18</a></li><li><a href='https://nces.maps.arcgis.com/home/item.html?id=cdde8df963b44233a20aedc495fdb20b' rel='nofollow ugc'>SY\n2015-16 TL 17</a></li><li><a href='https://nces.maps.arcgis.com/home/item.html?id=37e60391180e47639445e11c67d9e990' rel='nofollow ugc'>SY\n2015-16 TL 16</a></li><li><a href='https://nces.maps.arcgis.com/home/item.html?id=acb0e63f84b6437c88a05c62e7b4aa4f' rel='nofollow ugc'>SY\n2013-14 TL 15</a></li><li><a href='https://nces.maps.arcgis.com/home/item.html?id=9e3cbc1863d64545ad1936f49374927e' rel='nofollow ugc'>SY\n2013-14 TL 14</a></li></ul><p>All information contained in this file is in the public\ndomain. Data users are advised to review NCES program documentation and feature\nclass metadata to understand the limitations and appropriate use of these data.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/95738ddb2b784336a60aff23312ff480/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/95738ddb2b784336a60aff23312ff480/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-boundaries-current",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-boundaries-current"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://services1.arcgis.com/Ua5sjt3LWTPigjyD/arcgis/rest/services/School_Districts_Current/FeatureServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://services1.arcgis.com/Ua5sjt3LWTPigjyD/arcgis/rest/services/School_Districts_Current/FeatureServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/95738ddb2b784336a60aff23312ff480/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/95738ddb2b784336a60aff23312ff480/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/95738ddb2b784336a60aff23312ff480/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/95738ddb2b784336a60aff23312ff480/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/95738ddb2b784336a60aff23312ff480/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/95738ddb2b784336a60aff23312ff480/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/95738ddb2b784336a60aff23312ff480/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/95738ddb2b784336a60aff23312ff480/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "f42fb273-8624-4835-9fd0-960346cdd0d7",
+            "issued": "2020-03-16T13:18:41.000Z",
             "keyword": [
                 "administrative-school-district",
                 "boundaries",
@@ -11661,25 +11640,11 @@
                 "united-states",
                 "us"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:52.112866",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School District Composites SY 2022-23 TL 23",
-            "description": "<p>The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimates (EDGE) program develops annually updated school district boundary composite files that include public elementary, secondary, and unified school district boundaries clipped to the U.S. shoreline. School districts are special-purpose governments and administrative units designed by state and local officials to organize and provide public education for local residents. District boundaries are collected for NCES by the U.S. Census Bureau to support educational research and program administration, and the boundaries are essential for constructing district-level estimates of the number of children in poverty.</p><p>The Census Bureau\u2019s School District Boundary Review Program (SDRP) (<a href='https://www.census.gov/programs-surveys/sdrp.html' target='_blank' rel='nofollow ugc noopener noreferrer'>https://www.census.gov/programs-surveys/sdrp.html</a>) obtains the boundaries, names, and grade ranges from state officials, and integrates these updates into Census TIGER. Census TIGER boundaries include legal maritime buffers for coastal areas by default, but the NCES composite file removes these buffers to facilitate broader use and cleaner cartographic representation. The inputs for this data layer were developed from Census TIGER/Line 2023 and represent boundaries reported for the 2022-2023 school year. For more information about NCES school district boundary data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries</a>.</p><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</p>",
-            "modified": "2024-10-19T12:47:51.142755",
-            "accessLevel": "public",
-            "identifier": "69dc5eff-7486-4a4c-9ef2-ec9ba2d0ea3a",
-            "issued": "2024-02-09T13:46:14.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -11700,63 +11665,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "School District Boundaries - Current"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<p>The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimates (EDGE) program develops annually updated school district boundary composite files that include public elementary, secondary, and unified school district boundaries clipped to the U.S. shoreline. School districts are special-purpose governments and administrative units designed by state and local officials to organize and provide public education for local residents. District boundaries are collected for NCES by the U.S. Census Bureau to support educational research and program administration, and the boundaries are essential for constructing district-level estimates of the number of children in poverty.</p><p>The Census Bureau\u2019s School District Boundary Review Program (SDRP) (<a href='https://www.census.gov/programs-surveys/sdrp.html' target='_blank' rel='nofollow ugc noopener noreferrer'>https://www.census.gov/programs-surveys/sdrp.html</a>) obtains the boundaries, names, and grade ranges from state officials, and integrates these updates into Census TIGER. Census TIGER boundaries include legal maritime buffers for coastal areas by default, but the NCES composite file removes these buffers to facilitate broader use and cleaner cartographic representation. The inputs for this data layer were developed from Census TIGER/Line 2023 and represent boundaries reported for the 2022-2023 school year. For more information about NCES school district boundary data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries</a>.</p><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/10ea737b49f149f084a64e221f487c99/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/10ea737b49f149f084a64e221f487c99/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-composites-sy-2022-23-tl-23",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-composites-sy-2022-23-tl-23"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/School_District_Boundaries/EDGE_SCHOOLDISTRICT_TL23_SY2223/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/School_District_Boundaries/EDGE_SCHOOLDISTRICT_TL23_SY2223/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/10ea737b49f149f084a64e221f487c99/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/10ea737b49f149f084a64e221f487c99/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/10ea737b49f149f084a64e221f487c99/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/10ea737b49f149f084a64e221f487c99/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/10ea737b49f149f084a64e221f487c99/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/10ea737b49f149f084a64e221f487c99/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/10ea737b49f149f084a64e221f487c99/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/10ea737b49f149f084a64e221f487c99/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "69dc5eff-7486-4a4c-9ef2-ec9ba2d0ea3a",
+            "issued": "2024-02-09T13:46:14.000Z",
             "keyword": [
                 "administrative-school-district",
                 "boundaries",
@@ -11769,25 +11748,11 @@
                 "united-states",
                 "us"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:51.142755",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School District Composites SY 2021-22 TL 22",
-            "description": "<div style='text-align:Left;'><p>\u00a0The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimates (EDGE) program develops annually updated school district boundary composite files that include public elementary, secondary, and unified school district boundaries clipped to the U.S. shoreline. School districts are special-purpose governments and administrative units designed by state and local officials to organize and provide public education for local residents. District boundaries are collected for NCES by the U.S. Census Bureau to support educational research and program administration, and the boundaries are essential for constructing district-level estimates of the number of children in poverty.\u00a0</p><p>The Census Bureau\u2019s School District Boundary Review program (SDRP) (<a href='https://www.census.gov/programs-surveys/sdrp.html' target='_blank' rel='nofollow ugc noopener noreferrer'>https://www.census.gov/programs-surveys/sdrp.html</a>) obtains the boundaries, names, and grade ranges from state officials, and integrates these updates into Census TIGER. Census TIGER boundaries include legal maritime buffers for coastal areas by default, but the NCES composite file removes these buffers to facilitate broader use and cleaner cartographic representation. The inputs for this data layer were developed from Census TIGER/Line 2022 and represent boundaries reported for the 2021-2022 school year. For more information about NCES school district boundary data, see: <a href='https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries' rel='nofollow ugc'>https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries</a>.</p><p><span><span>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></span></span></p><p><span></span></p></div>",
-            "modified": "2024-10-19T12:47:49.978338",
-            "accessLevel": "public",
-            "identifier": "c42e1216-fc0d-4022-b485-3917466f11fa",
-            "issued": "2022-11-30T19:14:48.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -11808,77 +11773,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "School District Composites SY 2022-23 TL 23"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><p>\u00a0The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimates (EDGE) program develops annually updated school district boundary composite files that include public elementary, secondary, and unified school district boundaries clipped to the U.S. shoreline. School districts are special-purpose governments and administrative units designed by state and local officials to organize and provide public education for local residents. District boundaries are collected for NCES by the U.S. Census Bureau to support educational research and program administration, and the boundaries are essential for constructing district-level estimates of the number of children in poverty.\u00a0</p><p>The Census Bureau\u2019s School District Boundary Review program (SDRP) (<a href='https://www.census.gov/programs-surveys/sdrp.html' target='_blank' rel='nofollow ugc noopener noreferrer'>https://www.census.gov/programs-surveys/sdrp.html</a>) obtains the boundaries, names, and grade ranges from state officials, and integrates these updates into Census TIGER. Census TIGER boundaries include legal maritime buffers for coastal areas by default, but the NCES composite file removes these buffers to facilitate broader use and cleaner cartographic representation. The inputs for this data layer were developed from Census TIGER/Line 2022 and represent boundaries reported for the 2021-2022 school year. For more information about NCES school district boundary data, see: <a href='https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries' rel='nofollow ugc'>https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries</a>.</p><p><span><span>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></span></span></p><p><span></span></p></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/6afefd8dda8048d18444b8f06fad6930/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/6afefd8dda8048d18444b8f06fad6930/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-composites-sy-2021-22-tl-22",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-composites-sy-2021-22-tl-22"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/School_District_Boundaries/EDGE_SCHOOLDISTRICT_TL22_SY2122/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/School_District_Boundaries/EDGE_SCHOOLDISTRICT_TL22_SY2122/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "School District Documentation",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_SDBOUNDARIES_COMPOSITE_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "School District Documentation"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Single Composite File",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_SCHOOLDISTRICT_TL22_SY2122.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Single Composite File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6afefd8dda8048d18444b8f06fad6930/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6afefd8dda8048d18444b8f06fad6930/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6afefd8dda8048d18444b8f06fad6930/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6afefd8dda8048d18444b8f06fad6930/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6afefd8dda8048d18444b8f06fad6930/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6afefd8dda8048d18444b8f06fad6930/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6afefd8dda8048d18444b8f06fad6930/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6afefd8dda8048d18444b8f06fad6930/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "c42e1216-fc0d-4022-b485-3917466f11fa",
+            "issued": "2022-11-30T19:14:48.000Z",
             "keyword": [
                 "administrative-school-district",
                 "boundaries",
@@ -11891,25 +11870,11 @@
                 "united-states",
                 "us"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:49.978338",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School District Composites SY 2020-21 TL 21",
-            "description": "<div style='text-align:Left;'><div><div><p><span><span>The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated school district boundary composite files that include public elementary, secondary, and unified school district boundaries clipped to the U.S. shoreline. School districts are single-purpose administrative units designed by state and local officials to organize and provide public education for local residents. District boundaries are collected for NCES by the U.S. Census Bureau to support educational research and program administration, and the boundaries are essential for constructing district-level estimates of the number of children in poverty. </span></span></p><p><span><span>The Census Bureau\u2019s School District Boundary Review program (SDBR) (</span></span><a href='https://www.census.gov/programs-surveys/sdrp.html' style='text-decoration:underline;' rel='nofollow ugc'><span><span>https://www.census.gov/programs-surveys/sdrp.html</span></span></a><span>) obtains the boundaries, names, and grade ranges from state officials, and integrates these updates into Census TIGER. Census TIGER boundaries include legal maritime buffers for coastal areas by default, but the NCES composite file removes these buffers to facilitate broader use and cleaner cartographic representation. The NCES EDGE program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop the composite school district files. The inputs for this data layer were developed from Census TIGER/Line 2021 and represent boundaries reported for the 2020-2021 school year. For more information about NCES school district boundary data, see </span><a href='https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries' style='text-decoration:underline;' rel='nofollow ugc'><span><span>https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries</span></span></a><span><span>. </span></span></p><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<span><span><br /></span></span></p></div></div></div>",
-            "modified": "2024-10-19T12:47:48.989807",
-            "accessLevel": "public",
-            "identifier": "dc85a374-3759-4685-8db4-6194d0b5d09c",
-            "issued": "2021-11-29T14:18:45.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -11930,77 +11895,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "School District Composites SY 2021-22 TL 22"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><div><div><p><span><span>The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated school district boundary composite files that include public elementary, secondary, and unified school district boundaries clipped to the U.S. shoreline. School districts are single-purpose administrative units designed by state and local officials to organize and provide public education for local residents. District boundaries are collected for NCES by the U.S. Census Bureau to support educational research and program administration, and the boundaries are essential for constructing district-level estimates of the number of children in poverty. </span></span></p><p><span><span>The Census Bureau\u2019s School District Boundary Review program (SDBR) (</span></span><a href='https://www.census.gov/programs-surveys/sdrp.html' style='text-decoration:underline;' rel='nofollow ugc'><span><span>https://www.census.gov/programs-surveys/sdrp.html</span></span></a><span>) obtains the boundaries, names, and grade ranges from state officials, and integrates these updates into Census TIGER. Census TIGER boundaries include legal maritime buffers for coastal areas by default, but the NCES composite file removes these buffers to facilitate broader use and cleaner cartographic representation. The NCES EDGE program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop the composite school district files. The inputs for this data layer were developed from Census TIGER/Line 2021 and represent boundaries reported for the 2020-2021 school year. For more information about NCES school district boundary data, see </span><a href='https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries' style='text-decoration:underline;' rel='nofollow ugc'><span><span>https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries</span></span></a><span><span>. </span></span></p><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<span><span><br /></span></span></p></div></div></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/57648a58b8e74acb80225485c18c4f63/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/57648a58b8e74acb80225485c18c4f63/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-composites-sy-2020-21-tl-21",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-composites-sy-2020-21-tl-21"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/School_District_Boundaries/EDGE_SCHOOLDISTRICT_TL21_SY2021/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/School_District_Boundaries/EDGE_SCHOOLDISTRICT_TL21_SY2021/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "School District Documentation",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_SDBOUNDARIES_COMPOSITE_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "School District Documentation"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Single Composite File",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGESCHOOLDISTRICT_TL21_SY2021.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Single Composite File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/57648a58b8e74acb80225485c18c4f63/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/57648a58b8e74acb80225485c18c4f63/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/57648a58b8e74acb80225485c18c4f63/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/57648a58b8e74acb80225485c18c4f63/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/57648a58b8e74acb80225485c18c4f63/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/57648a58b8e74acb80225485c18c4f63/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/57648a58b8e74acb80225485c18c4f63/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/57648a58b8e74acb80225485c18c4f63/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "dc85a374-3759-4685-8db4-6194d0b5d09c",
+            "issued": "2021-11-29T14:18:45.000Z",
             "keyword": [
                 "boundaries",
                 "elementary-school-district",
@@ -12012,25 +11991,11 @@
                 "united-states",
                 "us"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:48.989807",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School District Composites SY 2019-20 TL 20",
-            "description": "<div style='text-align:Left;'><div><div><p><span><span>The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated school district boundary composite files that include public elementary, secondary, and unified school district boundaries clipped to the U.S. shoreline. School districts are single-purpose administrative units designed by state and local officials to organize and provide public education for local residents. District boundaries are collected for NCES by the U.S. Census Bureau to support educational research and program administration, and the boundaries are essential for constructing district-level estimates of the number of children in poverty. </span></span></p><p><span><span>The Census Bureau\u2019s School District Boundary Review program (SDBR) (</span></span><a href='https://www.census.gov/programs-surveys/sdrp.html' style='text-decoration:underline;' rel='nofollow ugc'><span><span>https://www.census.gov/programs-surveys/sdrp.html</span></span></a><span>) obtains the boundaries, names, and grade ranges from state officials, and integrates these updates into Census TIGER. Census TIGER boundaries include legal maritime buffers for coastal areas by default, but the NCES composite file removes these buffers to facilitate broader use and cleaner cartographic representation. The NCES EDGE program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop the composite school district files. The inputs for this data layer were developed from Census TIGER/Line 2020 and represent boundaries reported for the 2019-2020 school year. For more information about NCES school district boundary data, see </span><a href='https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries' style='text-decoration:underline;' rel='nofollow ugc'><span><span>https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries</span></span></a><span><span>. </span></span></p><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<span><span><br /></span></span></p></div></div></div>",
-            "modified": "2024-10-19T12:47:48.162919",
-            "accessLevel": "public",
-            "identifier": "a985da24-60ae-44e7-b8df-54423b5f1a7d",
-            "issued": "2021-03-29T22:52:03.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -12051,77 +12016,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "School District Composites SY 2020-21 TL 21"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><div><div><p><span><span>The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated school district boundary composite files that include public elementary, secondary, and unified school district boundaries clipped to the U.S. shoreline. School districts are single-purpose administrative units designed by state and local officials to organize and provide public education for local residents. District boundaries are collected for NCES by the U.S. Census Bureau to support educational research and program administration, and the boundaries are essential for constructing district-level estimates of the number of children in poverty. </span></span></p><p><span><span>The Census Bureau\u2019s School District Boundary Review program (SDBR) (</span></span><a href='https://www.census.gov/programs-surveys/sdrp.html' style='text-decoration:underline;' rel='nofollow ugc'><span><span>https://www.census.gov/programs-surveys/sdrp.html</span></span></a><span>) obtains the boundaries, names, and grade ranges from state officials, and integrates these updates into Census TIGER. Census TIGER boundaries include legal maritime buffers for coastal areas by default, but the NCES composite file removes these buffers to facilitate broader use and cleaner cartographic representation. The NCES EDGE program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop the composite school district files. The inputs for this data layer were developed from Census TIGER/Line 2020 and represent boundaries reported for the 2019-2020 school year. For more information about NCES school district boundary data, see </span><a href='https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries' style='text-decoration:underline;' rel='nofollow ugc'><span><span>https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries</span></span></a><span><span>. </span></span></p><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<span><span><br /></span></span></p></div></div></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/a55870b7904848f793590998559f86bb/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/a55870b7904848f793590998559f86bb/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-composites-sy-2019-20-tl-20",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-composites-sy-2019-20-tl-20"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/School_District_Boundaries/EDGE_SCHOOLDISTRICT_TL20_SY1920/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/School_District_Boundaries/EDGE_SCHOOLDISTRICT_TL20_SY1920/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "School District Documentation",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_SDBOUNDARIES_COMPOSITE_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "School District Documentation"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Single Composite File",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_SCHOOLDISTRICT_TL20_SY1920.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Single Composite File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a55870b7904848f793590998559f86bb/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a55870b7904848f793590998559f86bb/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a55870b7904848f793590998559f86bb/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a55870b7904848f793590998559f86bb/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a55870b7904848f793590998559f86bb/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a55870b7904848f793590998559f86bb/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a55870b7904848f793590998559f86bb/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a55870b7904848f793590998559f86bb/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "a985da24-60ae-44e7-b8df-54423b5f1a7d",
+            "issued": "2021-03-29T22:52:03.000Z",
             "keyword": [
                 "boundaries",
                 "elementary-school-district",
@@ -12133,25 +12112,11 @@
                 "united-states",
                 "us"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:48.162919",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School District Composites SY 2018-19 TL 19",
-            "description": "<div style='text-align:Left;'><div><div><p><span><span>The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated school district boundary composite files that include public elementary, secondary, and unified school district boundaries clipped to the U.S. shoreline. School districts are single-purpose administrative units designed by state and local officials to organize and provide public education for local residents. District boundaries are collected for NCES by the U.S. Census Bureau to support educational research and program administration, and the boundaries are essential for constructing district-level estimates of the number of children in poverty. </span></span></p><p><span><span>The Census Bureau\u2019s School District Boundary Review program (SDBR) (</span></span><a href='https://www.census.gov/programs-surveys/sdrp.html' style='text-decoration:underline;' rel='nofollow ugc'><span><span>https://www.census.gov/programs-surveys/sdrp.html</span></span></a><span>) obtains the boundaries, names, and grade ranges from state officials, and integrates these updates into Census TIGER. Census TIGER boundaries include legal maritime buffers for coastal areas by default, but the NCES composite file removes these buffers to facilitate broader use and cleaner cartographic representation. The NCES EDGE program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop the composite school district files. The inputs for this data layer were developed from Census TIGER/Line 2019 and represent boundaries reported for the 2018-2019 school year. For more information about NCES school district boundary data, see </span><a href='https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries' style='text-decoration:underline;' rel='nofollow ugc'><span><span>https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries</span></span></a><span><span>.\u00a0</span></span></p><p><span><span>All information contained in this file is in the public domain. Data users\u00a0are advised to review NCES program documentation and feature class metadata to understand the limitations\u00a0and appropriate use\u00a0of the data.</span></span></p></div></div></div>",
-            "modified": "2024-10-19T12:47:47.190877",
-            "accessLevel": "public",
-            "identifier": "fa4f6482-b3e7-4801-80ef-f0efa3442874",
-            "issued": "2020-03-13T19:02:13.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -12172,77 +12137,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "School District Composites SY 2019-20 TL 20"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><div><div><p><span><span>The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated school district boundary composite files that include public elementary, secondary, and unified school district boundaries clipped to the U.S. shoreline. School districts are single-purpose administrative units designed by state and local officials to organize and provide public education for local residents. District boundaries are collected for NCES by the U.S. Census Bureau to support educational research and program administration, and the boundaries are essential for constructing district-level estimates of the number of children in poverty. </span></span></p><p><span><span>The Census Bureau\u2019s School District Boundary Review program (SDBR) (</span></span><a href='https://www.census.gov/programs-surveys/sdrp.html' style='text-decoration:underline;' rel='nofollow ugc'><span><span>https://www.census.gov/programs-surveys/sdrp.html</span></span></a><span>) obtains the boundaries, names, and grade ranges from state officials, and integrates these updates into Census TIGER. Census TIGER boundaries include legal maritime buffers for coastal areas by default, but the NCES composite file removes these buffers to facilitate broader use and cleaner cartographic representation. The NCES EDGE program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop the composite school district files. The inputs for this data layer were developed from Census TIGER/Line 2019 and represent boundaries reported for the 2018-2019 school year. For more information about NCES school district boundary data, see </span><a href='https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries' style='text-decoration:underline;' rel='nofollow ugc'><span><span>https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries</span></span></a><span><span>.\u00a0</span></span></p><p><span><span>All information contained in this file is in the public domain. Data users\u00a0are advised to review NCES program documentation and feature class metadata to understand the limitations\u00a0and appropriate use\u00a0of the data.</span></span></p></div></div></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/fc0aaa02bb72455aa276e8c4efa07e1b/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/fc0aaa02bb72455aa276e8c4efa07e1b/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-composites-sy-2018-19-tl-19",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-composites-sy-2018-19-tl-19"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/School_District_Boundaries/EDGE_SCHOOLDISTRICT_TL19_SY1819/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/School_District_Boundaries/EDGE_SCHOOLDISTRICT_TL19_SY1819/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "School District Documentation",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_SDBOUNDARIES_COMPOSITE_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "School District Documentation"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Single Composite File",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_SCHOOLDISTRICT_TL19_SY1819.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Single Composite File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/fc0aaa02bb72455aa276e8c4efa07e1b/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/fc0aaa02bb72455aa276e8c4efa07e1b/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/fc0aaa02bb72455aa276e8c4efa07e1b/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/fc0aaa02bb72455aa276e8c4efa07e1b/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/fc0aaa02bb72455aa276e8c4efa07e1b/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/fc0aaa02bb72455aa276e8c4efa07e1b/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/fc0aaa02bb72455aa276e8c4efa07e1b/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/fc0aaa02bb72455aa276e8c4efa07e1b/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "fa4f6482-b3e7-4801-80ef-f0efa3442874",
+            "issued": "2020-03-13T19:02:13.000Z",
             "keyword": [
                 "boundaries",
                 "elementary-school-district",
@@ -12254,25 +12233,11 @@
                 "united-states",
                 "us"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:47.190877",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School District Composites SY 2017-18 TL 18",
-            "description": "<div style='text-align:Left;'><div><div><p><span><span>The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated school district boundary composite files that include public elementary, secondary, and unified school district boundaries clipped to the U.S. shoreline. School districts are single-purpose administrative units designed by state and local officials to organize and provide public education for local residents. District boundaries are collected for NCES by the U.S. Census Bureau to support educational research and program administration, and the boundaries are essential for constructing district-level estimates of the number of children in poverty. </span></span></p><p><span><span>The Census Bureau\u2019s School District Boundary Review program (SDBR) (</span></span><a href='https://www.census.gov/programs-surveys/sdrp.html' style='text-decoration:underline;' rel='nofollow ugc'><span><span>https://www.census.gov/programs-surveys/sdrp.html</span></span></a><span><span>) obtains the boundaries, names, and grade ranges from state officials, and integrates these updates into Census TIGER. Census TIGER boundaries include legal maritime buffers for coastal areas by default, but the NCES composite file removes these buffers to facilitate broader use and cleaner cartographic representation. The NCES EDGE program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop the composite school district files. The inputs for this data layer were developed from Census TIGER/Line 2018 and represent boundaries reported for the 2017-2018 school year. For more information about NCES school district boundary data, see </span></span><a href='https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries' style='text-decoration:underline;' rel='nofollow ugc'><span><span>https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries</span></span></a><span><span>. </span></span></p><p><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</span><span><span><br /></span></span></p><p><span></span></p><p><span></span></p></div></div></div>",
-            "modified": "2024-10-19T12:47:46.226189",
-            "accessLevel": "public",
-            "identifier": "1b5b59e2-b486-4d2a-8da3-083710dfce8b",
-            "issued": "2020-03-20T22:07:51.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -12293,63 +12258,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "School District Composites SY 2018-19 TL 19"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><div><div><p><span><span>The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated school district boundary composite files that include public elementary, secondary, and unified school district boundaries clipped to the U.S. shoreline. School districts are single-purpose administrative units designed by state and local officials to organize and provide public education for local residents. District boundaries are collected for NCES by the U.S. Census Bureau to support educational research and program administration, and the boundaries are essential for constructing district-level estimates of the number of children in poverty. </span></span></p><p><span><span>The Census Bureau\u2019s School District Boundary Review program (SDBR) (</span></span><a href='https://www.census.gov/programs-surveys/sdrp.html' style='text-decoration:underline;' rel='nofollow ugc'><span><span>https://www.census.gov/programs-surveys/sdrp.html</span></span></a><span><span>) obtains the boundaries, names, and grade ranges from state officials, and integrates these updates into Census TIGER. Census TIGER boundaries include legal maritime buffers for coastal areas by default, but the NCES composite file removes these buffers to facilitate broader use and cleaner cartographic representation. The NCES EDGE program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop the composite school district files. The inputs for this data layer were developed from Census TIGER/Line 2018 and represent boundaries reported for the 2017-2018 school year. For more information about NCES school district boundary data, see </span></span><a href='https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries' style='text-decoration:underline;' rel='nofollow ugc'><span><span>https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries</span></span></a><span><span>. </span></span></p><p><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</span><span><span><br /></span></span></p><p><span></span></p><p><span></span></p></div></div></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/29ccd69e8d0b438195cbf9e1f317ea60/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/29ccd69e8d0b438195cbf9e1f317ea60/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-composites-sy-2017-18-tl-18",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-composites-sy-2017-18-tl-18"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/School_District_Boundaries/EDGE_SCHOOLDISTRICT_TL18_SY1718/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/School_District_Boundaries/EDGE_SCHOOLDISTRICT_TL18_SY1718/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/29ccd69e8d0b438195cbf9e1f317ea60/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/29ccd69e8d0b438195cbf9e1f317ea60/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/29ccd69e8d0b438195cbf9e1f317ea60/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/29ccd69e8d0b438195cbf9e1f317ea60/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/29ccd69e8d0b438195cbf9e1f317ea60/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/29ccd69e8d0b438195cbf9e1f317ea60/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/29ccd69e8d0b438195cbf9e1f317ea60/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/29ccd69e8d0b438195cbf9e1f317ea60/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "1b5b59e2-b486-4d2a-8da3-083710dfce8b",
+            "issued": "2020-03-20T22:07:51.000Z",
             "keyword": [
                 "boundaries",
                 "elementary-school-district",
@@ -12361,25 +12340,11 @@
                 "united-states",
                 "us"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:46.226189",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School District Office Locations - Current",
-            "description": "<div style='text-align:Left;'><p></p><p style='margin-top:12.0pt; margin-right:0in; margin-bottom:12.0pt; margin-left:0in; background:white;'><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C;'>The\nNational Center for Education Statistics' (NCES) Education Demographic and\nGeographic Estimate (EDGE) program develops annually updated point locations\n(latitude and longitude) for public elementary, secondary, unified, and\nsupervisory school district administrative offices included in the NCES Common\nCore of Data (CCD).\u00a0The CCD is an annual collection of basic\nadministrative characteristics that includes the physical address for all\npublic schools, school districts, and state education agencies in the United\nStates. For more information about NCES school point data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' rel='nofollow ugc'><span style='color:blue;'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</span></a>.</span></p>\n\n<p style='margin-top:12.0pt; margin-right:0in; margin-bottom:12.0pt; margin-left:0in; background:white;'><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C;'>Collections\nare available for the following years:</span></p>\n\n<ul>\n <li><a href='https://nces.maps.arcgis.com/home/item.html?id=482d5c0c09c44c5994758c04b256da6d' target='_blank' rel='nofollow ugc noopener noreferrer'>2022-23</a><br /></li><li><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif; color:black;'><a href='https://nces.maps.arcgis.com/home/item.html?id=0bd897b60c08482b88ef5555993d42b8' rel='nofollow ugc'><span style='color:blue;'>2021-22</span></a></span></li>\n <li><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif; color:black;'><a href='https://nces.maps.arcgis.com/home/item.html?id=01078406d89245ebae606eeceb7b3657' target='_blank' rel='nofollow ugc noopener noreferrer'><span style='color:blue;'>2020-21</span></a></span></li>\n <li><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif; color:black;'><a href='https://nces.maps.arcgis.com/home/item.html?id=dfa2adbe5c854024b506ecd908268fbb' target='_blank' rel='nofollow ugc noopener noreferrer'><span style='color:blue;'>2019-20</span></a></span></li>\n <li><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif; color:black;'><a href='https://nces.maps.arcgis.com/home/item.html?id=2cf893e8f3304db18ea9dd239acc74a3v' target='_blank' rel='nofollow ugc noopener noreferrer'><span style='color:blue;'>2018-19</span></a></span></li>\n <li><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif; color:black;'><a href='https://nces.maps.arcgis.com/home/item.html?id=0b7f9ab695be4f7285bf1c51461a1c40' target='_blank' rel='nofollow ugc noopener noreferrer'><span style='color:blue;'>2017-18</span></a></span></li>\n <li><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif; color:black;'><a href='https://nces.maps.arcgis.com/home/item.html?id=f42d690035cb4e35b8247886a495305c' target='_blank' rel='nofollow ugc noopener noreferrer'><span style='color:blue;'>2016-17</span></a></span></li>\n <li><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif; color:black;'><a href='https://nces.maps.arcgis.com/home/item.html?id=9f7c5c08e2df46eebbff76717effe2dd' target='_blank' rel='nofollow ugc noopener noreferrer'><span style='color:blue;'>2015-16</span></a></span></li>\n</ul>\n\n<p style='margin-top:12.0pt; margin-right:0in; margin-bottom:0in; margin-left:0in; background:white;'><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif; color:black;'>All\ninformation contained in this file is in the public domain. Data users are\nadvised to review NCES program documentation and feature class metadata to\nunderstand the limitations and appropriate use of these data.</span></p><p></p></div>",
-            "modified": "2024-10-19T12:47:45.134180",
-            "accessLevel": "public",
-            "identifier": "c1f38238-2434-4fe3-abd2-39901d47fe62",
-            "issued": "2020-03-26T21:59:37.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -12400,63 +12365,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "School District Composites SY 2017-18 TL 18"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><p></p><p style='margin-top:12.0pt; margin-right:0in; margin-bottom:12.0pt; margin-left:0in; background:white;'><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C;'>The\nNational Center for Education Statistics' (NCES) Education Demographic and\nGeographic Estimate (EDGE) program develops annually updated point locations\n(latitude and longitude) for public elementary, secondary, unified, and\nsupervisory school district administrative offices included in the NCES Common\nCore of Data (CCD).\u00a0The CCD is an annual collection of basic\nadministrative characteristics that includes the physical address for all\npublic schools, school districts, and state education agencies in the United\nStates. For more information about NCES school point data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' rel='nofollow ugc'><span style='color:blue;'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</span></a>.</span></p>\n\n<p style='margin-top:12.0pt; margin-right:0in; margin-bottom:12.0pt; margin-left:0in; background:white;'><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C;'>Collections\nare available for the following years:</span></p>\n\n<ul>\n <li><a href='https://nces.maps.arcgis.com/home/item.html?id=482d5c0c09c44c5994758c04b256da6d' target='_blank' rel='nofollow ugc noopener noreferrer'>2022-23</a><br /></li><li><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif; color:black;'><a href='https://nces.maps.arcgis.com/home/item.html?id=0bd897b60c08482b88ef5555993d42b8' rel='nofollow ugc'><span style='color:blue;'>2021-22</span></a></span></li>\n <li><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif; color:black;'><a href='https://nces.maps.arcgis.com/home/item.html?id=01078406d89245ebae606eeceb7b3657' target='_blank' rel='nofollow ugc noopener noreferrer'><span style='color:blue;'>2020-21</span></a></span></li>\n <li><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif; color:black;'><a href='https://nces.maps.arcgis.com/home/item.html?id=dfa2adbe5c854024b506ecd908268fbb' target='_blank' rel='nofollow ugc noopener noreferrer'><span style='color:blue;'>2019-20</span></a></span></li>\n <li><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif; color:black;'><a href='https://nces.maps.arcgis.com/home/item.html?id=2cf893e8f3304db18ea9dd239acc74a3v' target='_blank' rel='nofollow ugc noopener noreferrer'><span style='color:blue;'>2018-19</span></a></span></li>\n <li><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif; color:black;'><a href='https://nces.maps.arcgis.com/home/item.html?id=0b7f9ab695be4f7285bf1c51461a1c40' target='_blank' rel='nofollow ugc noopener noreferrer'><span style='color:blue;'>2017-18</span></a></span></li>\n <li><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif; color:black;'><a href='https://nces.maps.arcgis.com/home/item.html?id=f42d690035cb4e35b8247886a495305c' target='_blank' rel='nofollow ugc noopener noreferrer'><span style='color:blue;'>2016-17</span></a></span></li>\n <li><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif; color:black;'><a href='https://nces.maps.arcgis.com/home/item.html?id=9f7c5c08e2df46eebbff76717effe2dd' target='_blank' rel='nofollow ugc noopener noreferrer'><span style='color:blue;'>2015-16</span></a></span></li>\n</ul>\n\n<p style='margin-top:12.0pt; margin-right:0in; margin-bottom:0in; margin-left:0in; background:white;'><span style='font-size:11.5pt; font-family:&quot;Helvetica&quot;,sans-serif; color:black;'>All\ninformation contained in this file is in the public domain. Data users are\nadvised to review NCES program documentation and feature class metadata to\nunderstand the limitations and appropriate use of these data.</span></p><p></p></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/4b545c5ef1494b439bc4c4ce888f8b7d/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/4b545c5ef1494b439bc4c4ce888f8b7d/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-office-locations-current-1",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-office-locations-current-1"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://services1.arcgis.com/Ua5sjt3LWTPigjyD/arcgis/rest/services/School_District_Office_Locations_Current/FeatureServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://services1.arcgis.com/Ua5sjt3LWTPigjyD/arcgis/rest/services/School_District_Office_Locations_Current/FeatureServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/4b545c5ef1494b439bc4c4ce888f8b7d/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/4b545c5ef1494b439bc4c4ce888f8b7d/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/4b545c5ef1494b439bc4c4ce888f8b7d/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/4b545c5ef1494b439bc4c4ce888f8b7d/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/4b545c5ef1494b439bc4c4ce888f8b7d/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/4b545c5ef1494b439bc4c4ce888f8b7d/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/4b545c5ef1494b439bc4c4ce888f8b7d/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/4b545c5ef1494b439bc4c4ce888f8b7d/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "c1f38238-2434-4fe3-abd2-39901d47fe62",
+            "issued": "2020-03-26T21:59:37.000Z",
             "keyword": [
                 "ccd",
                 "common-core-of-data",
@@ -12471,25 +12450,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:45.134180",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School District Office Locations 2022-23",
-            "description": "<div style='text-align:Left;'><div><div><p>The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimates (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary, secondary, unified, and supervisory school district administrative offices included in the NCES Common Core of Data (CCD). The CCD is an annual collection of basic administrative characteristics that includes the physical address for all public schools, school districts, and state education agencies in the United States. The point locations in this data layer were developed from the 2022-2023 CCD collection. For more information about NCES school point data, see:<a style='color:rgb(0, 121, 193);font-family:inherit;font-size:16px;text-decoration-line:none;' target='_blank' href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>.</p><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</p></div></div></div>",
-            "modified": "2024-10-19T12:47:44.141502",
-            "accessLevel": "public",
-            "identifier": "d3c656fb-addd-4acc-908e-9a093587c6b0",
-            "issued": "2024-02-09T15:03:41.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -12510,63 +12475,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "School District Office Locations - Current"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><div><div><p>The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimates (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary, secondary, unified, and supervisory school district administrative offices included in the NCES Common Core of Data (CCD). The CCD is an annual collection of basic administrative characteristics that includes the physical address for all public schools, school districts, and state education agencies in the United States. The point locations in this data layer were developed from the 2022-2023 CCD collection. For more information about NCES school point data, see:<a style='color:rgb(0, 121, 193);font-family:inherit;font-size:16px;text-decoration-line:none;' target='_blank' href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>.</p><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</p></div></div></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/482d5c0c09c44c5994758c04b256da6d/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/482d5c0c09c44c5994758c04b256da6d/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-office-locations-2022-23-",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-office-locations-2022-23-"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICLEA_2223/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICLEA_2223/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/482d5c0c09c44c5994758c04b256da6d/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/482d5c0c09c44c5994758c04b256da6d/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/482d5c0c09c44c5994758c04b256da6d/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/482d5c0c09c44c5994758c04b256da6d/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/482d5c0c09c44c5994758c04b256da6d/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/482d5c0c09c44c5994758c04b256da6d/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/482d5c0c09c44c5994758c04b256da6d/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/482d5c0c09c44c5994758c04b256da6d/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "d3c656fb-addd-4acc-908e-9a093587c6b0",
+            "issued": "2024-02-09T15:03:41.000Z",
             "keyword": [
                 "ccd",
                 "common-core-of-data",
@@ -12582,25 +12561,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:44.141502",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School District Office Locations 2021-22",
-            "description": "<div style='text-align:Left;'><p style='margin-top:0px; margin-bottom:1.5rem; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><span style='font-family:inherit;'>The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimates (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary, secondary, unified, and supervisory school district administrative offices included in the NCES Common Core of Data (CCD). The CCD is an annual collection of basic administrative characteristics that includes the physical address for all public schools, school districts, and state education agencies in the United States.\u00a0 The point locations in this data layer were developed from the 2021-2022 CCD collection. For more information about NCES school point data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:inherit;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>.<br /></span></p><p style='margin-top:0px; margin-bottom:1.5rem; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><span style='font-family:inherit;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</span></p></div>",
-            "modified": "2024-10-19T12:47:43.194746",
-            "accessLevel": "public",
-            "identifier": "a462e230-5f39-406a-a5ca-eda5edc84f9a",
-            "issued": "2023-03-10T15:17:23.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -12621,77 +12586,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "School District Office Locations 2022-23"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><p style='margin-top:0px; margin-bottom:1.5rem; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><span style='font-family:inherit;'>The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimates (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary, secondary, unified, and supervisory school district administrative offices included in the NCES Common Core of Data (CCD). The CCD is an annual collection of basic administrative characteristics that includes the physical address for all public schools, school districts, and state education agencies in the United States.\u00a0 The point locations in this data layer were developed from the 2021-2022 CCD collection. For more information about NCES school point data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:inherit;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>.<br /></span></p><p style='margin-top:0px; margin-bottom:1.5rem; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><span style='font-family:inherit;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</span></p></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/0bd897b60c08482b88ef5555993d42b8/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/0bd897b60c08482b88ef5555993d42b8/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-office-locations-2021-22",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-office-locations-2021-22"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICLEA_2122/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICLEA_2122/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Geocodes: Public Schools and Local Education Agencies",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_GEOCODE_PUBLIC_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Public Schools and Local Education Agencies"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Geocodes: Public Schools and Local Education Agencies",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PUBLICLEA_2122.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Public Schools and Local Education Agencies"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/0bd897b60c08482b88ef5555993d42b8/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/0bd897b60c08482b88ef5555993d42b8/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/0bd897b60c08482b88ef5555993d42b8/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/0bd897b60c08482b88ef5555993d42b8/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/0bd897b60c08482b88ef5555993d42b8/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/0bd897b60c08482b88ef5555993d42b8/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/0bd897b60c08482b88ef5555993d42b8/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/0bd897b60c08482b88ef5555993d42b8/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "a462e230-5f39-406a-a5ca-eda5edc84f9a",
+            "issued": "2023-03-10T15:17:23.000Z",
             "keyword": [
                 "ccd",
                 "common-core-of-data",
@@ -12707,25 +12686,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:43.194746",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School District Office Locations 2020-21",
-            "description": "<div style='text-align:Left;'><p style='margin-top:0px; margin-bottom:1.5rem; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><span style='font-family:inherit;'>The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary, secondary, unified, and supervisory school district administrative offices included in the NCES Common Core of Data (CCD). The CCD is an annual collection of basic administrative characteristics that includes the physical address for all public schools, school districts, and state education agencies in the United States.\u00a0 The point locations in this data layer were developed from the 2022-2021 CCD collection. For more information about NCES school point data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:inherit;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>.<br /></span></p><p style='margin-top:0px; margin-bottom:1.5rem; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><span style='font-family:inherit;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</span></p></div>",
-            "modified": "2024-10-19T12:47:42.102540",
-            "accessLevel": "public",
-            "identifier": "af44916b-9474-47d5-8a68-36c3894b322c",
-            "issued": "2022-03-03T19:47:14.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -12746,77 +12711,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "School District Office Locations 2021-22"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><p style='margin-top:0px; margin-bottom:1.5rem; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><span style='font-family:inherit;'>The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary, secondary, unified, and supervisory school district administrative offices included in the NCES Common Core of Data (CCD). The CCD is an annual collection of basic administrative characteristics that includes the physical address for all public schools, school districts, and state education agencies in the United States.\u00a0 The point locations in this data layer were developed from the 2022-2021 CCD collection. For more information about NCES school point data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:inherit;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>.<br /></span></p><p style='margin-top:0px; margin-bottom:1.5rem; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><span style='font-family:inherit;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</span></p></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/01078406d89245ebae606eeceb7b3657/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/01078406d89245ebae606eeceb7b3657/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-office-locations-2020-21",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-office-locations-2020-21"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICLEA_2021/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICLEA_2021/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Geocodes: Public Schools and Local Education Agencies",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_GEOCODE_PUBLIC_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Public Schools and Local Education Agencies"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Geocodes: Public Schools and Local Education Agencies",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PUBLICLEA_2021.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Public Schools and Local Education Agencies"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/01078406d89245ebae606eeceb7b3657/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/01078406d89245ebae606eeceb7b3657/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/01078406d89245ebae606eeceb7b3657/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/01078406d89245ebae606eeceb7b3657/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/01078406d89245ebae606eeceb7b3657/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/01078406d89245ebae606eeceb7b3657/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/01078406d89245ebae606eeceb7b3657/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/01078406d89245ebae606eeceb7b3657/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "af44916b-9474-47d5-8a68-36c3894b322c",
+            "issued": "2022-03-03T19:47:14.000Z",
             "keyword": [
                 "ccd",
                 "common-core-of-data",
@@ -12832,25 +12811,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:42.102540",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School District Office Locations 2019-20",
-            "description": "<div style='text-align:Left;'><p><span>The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary, secondary, and unified school district administrative offices included in the NCES Common Core of Data (CCD).\u00a0</span><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The CCD is an annual collection of basic administrative characteristics that includes the physical address for all public schools, school districts, and state education agencies in the United States. The NCES EDGE program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for schools and school district administrative offices based on these addresses. The point locations in this data layer were developed from the 2019-2020 CCD collection. For more information about NCES school point data, see:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' rel='nofollow ugc'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>.\u00a0</span></p><p><span>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></span></p></div>",
-            "modified": "2024-10-19T12:47:41.155254",
-            "accessLevel": "public",
-            "identifier": "e94b3d64-4876-45e5-9878-76280bbe4627",
-            "issued": "2021-03-25T17:40:17.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -12871,77 +12836,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "School District Office Locations 2020-21"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><p><span>The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary, secondary, and unified school district administrative offices included in the NCES Common Core of Data (CCD).\u00a0</span><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The CCD is an annual collection of basic administrative characteristics that includes the physical address for all public schools, school districts, and state education agencies in the United States. The NCES EDGE program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for schools and school district administrative offices based on these addresses. The point locations in this data layer were developed from the 2019-2020 CCD collection. For more information about NCES school point data, see:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' rel='nofollow ugc'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>.\u00a0</span></p><p><span>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></span></p></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/dfa2adbe5c854024b506ecd908268fbb/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/dfa2adbe5c854024b506ecd908268fbb/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-office-locations-2019-20",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-office-locations-2019-20"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICLEA_1920/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICLEA_1920/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Geocodes: Public Schools and Local Education Agencies",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_GEOCODE_PUBLIC_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Public Schools and Local Education Agencies"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Geocodes: Public Schools and Local Education Agencies",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PUBLICLEA_1920.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Public Schools and Local Education Agencies"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/dfa2adbe5c854024b506ecd908268fbb/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/dfa2adbe5c854024b506ecd908268fbb/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/dfa2adbe5c854024b506ecd908268fbb/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/dfa2adbe5c854024b506ecd908268fbb/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/dfa2adbe5c854024b506ecd908268fbb/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/dfa2adbe5c854024b506ecd908268fbb/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/dfa2adbe5c854024b506ecd908268fbb/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/dfa2adbe5c854024b506ecd908268fbb/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "e94b3d64-4876-45e5-9878-76280bbe4627",
+            "issued": "2021-03-25T17:40:17.000Z",
             "keyword": [
                 "ccd",
                 "common-core-of-data",
@@ -12957,25 +12936,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:41.155254",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School District Office Locations 2017-18",
-            "description": "<div style='text-align:Left;'><p>The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary, secondary, and unified school district administrative offices included in the NCES Common Core of Data (CCD).\u00a0<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The CCD is an annual collection of basic administrative characteristics that includes the physical address for all public schools, school districts, and state education agencies in the United States. The NCES EDGE program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for schools and school district administrative offices based on these addresses. The point locations in this data layer were developed from the 2017-2018 CCD collection. For more information about NCES school point data, see:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' rel='nofollow ugc'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>.</span></p><p><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</span><br /></p></div>",
-            "modified": "2024-10-19T12:47:40.217051",
-            "accessLevel": "public",
-            "identifier": "f9742a3c-9089-4d7f-9248-93b4b2ccba2f",
-            "issued": "2020-03-24T12:33:57.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -12996,77 +12961,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "School District Office Locations 2019-20"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><p>The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary, secondary, and unified school district administrative offices included in the NCES Common Core of Data (CCD).\u00a0<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The CCD is an annual collection of basic administrative characteristics that includes the physical address for all public schools, school districts, and state education agencies in the United States. The NCES EDGE program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for schools and school district administrative offices based on these addresses. The point locations in this data layer were developed from the 2017-2018 CCD collection. For more information about NCES school point data, see:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' rel='nofollow ugc'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>.</span></p><p><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</span><br /></p></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/0b7f9ab695be4f7285bf1c51461a1c40/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/0b7f9ab695be4f7285bf1c51461a1c40/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-office-locations-2017-18",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-office-locations-2017-18"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICLEA_1718/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICLEA_1718/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Geocodes: Public Schools and Local Education Agencies",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_GEOCODE_PUBLIC_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Public Schools and Local Education Agencies"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Geocodes: Public Schools and Local Education Agencies",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PUBLICLEA_1718.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Public Schools and Local Education Agencies"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/0b7f9ab695be4f7285bf1c51461a1c40/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/0b7f9ab695be4f7285bf1c51461a1c40/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/0b7f9ab695be4f7285bf1c51461a1c40/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/0b7f9ab695be4f7285bf1c51461a1c40/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/0b7f9ab695be4f7285bf1c51461a1c40/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/0b7f9ab695be4f7285bf1c51461a1c40/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/0b7f9ab695be4f7285bf1c51461a1c40/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/0b7f9ab695be4f7285bf1c51461a1c40/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "f9742a3c-9089-4d7f-9248-93b4b2ccba2f",
+            "issued": "2020-03-24T12:33:57.000Z",
             "keyword": [
                 "ccd",
                 "common-core-of-data",
@@ -13083,25 +13062,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:40.217051",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School District Office Locations 2016-17",
-            "description": "<div style='text-align:Left;'><p>The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary, secondary, and unified school district administrative offices included in the NCES Common Core of Data (CCD).\u00a0<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The CCD is an annual collection of basic administrative characteristics that includes the physical address for all public schools, school districts, and state education agencies in the United States. The NCES EDGE program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for schools and school district administrative offices based on these addresses. The point locations in this data layer were developed from the 2016-2017 CCD collection. For more information about NCES school point data, see:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' rel='nofollow ugc'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>.</span></p><p><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</span><br /></p></div>",
-            "modified": "2024-10-19T12:47:39.201486",
-            "accessLevel": "public",
-            "identifier": "fbd8f838-c7a7-4df0-bbc9-62b6d8271bf9",
-            "issued": "2020-03-24T12:41:33.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -13122,77 +13087,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "School District Office Locations 2017-18"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><p>The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary, secondary, and unified school district administrative offices included in the NCES Common Core of Data (CCD).\u00a0<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The CCD is an annual collection of basic administrative characteristics that includes the physical address for all public schools, school districts, and state education agencies in the United States. The NCES EDGE program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for schools and school district administrative offices based on these addresses. The point locations in this data layer were developed from the 2016-2017 CCD collection. For more information about NCES school point data, see:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' rel='nofollow ugc'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>.</span></p><p><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</span><br /></p></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/f42d690035cb4e35b8247886a495305c/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/f42d690035cb4e35b8247886a495305c/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-office-locations-2016-17",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-office-locations-2016-17"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICLEA_1617/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICLEA_1617/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Geocodes: Public Schools and Local Education Agencies",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_GEOCODE_PUBLIC_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Public Schools and Local Education Agencies"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Geocodes: Public Schools and Local Education Agencies",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PUBLICLEA_1617.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Public Schools and Local Education Agencies"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/f42d690035cb4e35b8247886a495305c/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/f42d690035cb4e35b8247886a495305c/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/f42d690035cb4e35b8247886a495305c/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/f42d690035cb4e35b8247886a495305c/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/f42d690035cb4e35b8247886a495305c/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/f42d690035cb4e35b8247886a495305c/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/f42d690035cb4e35b8247886a495305c/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/f42d690035cb4e35b8247886a495305c/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "fbd8f838-c7a7-4df0-bbc9-62b6d8271bf9",
+            "issued": "2020-03-24T12:41:33.000Z",
             "keyword": [
                 "ccd",
                 "common-core-of-data",
@@ -13209,25 +13188,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:39.201486",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School District Office Locations 2015-16",
-            "description": "<div style='text-align:Left;'><p>The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary, secondary, and unified school district administrative offices included in the NCES Common Core of Data (CCD).\u00a0<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The CCD is an annual collection of basic administrative characteristics that includes the physical address for all public schools, school districts, and state education agencies in the United States. The NCES EDGE program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for schools and school district administrative offices based on these addresses. The point locations in this data layer were developed from the 2015-2016 CCD collection. For more information about NCES school point data, see:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' rel='nofollow ugc'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>.</span></p><p><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</span><br /></p></div>",
-            "modified": "2024-10-19T12:47:38.311128",
-            "accessLevel": "public",
-            "identifier": "b4f1b4f6-5538-4bfb-b2a6-b159ad20c143",
-            "issued": "2020-03-24T12:49:28.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -13248,77 +13213,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "School District Office Locations 2016-17"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><p>The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary, secondary, and unified school district administrative offices included in the NCES Common Core of Data (CCD).\u00a0<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The CCD is an annual collection of basic administrative characteristics that includes the physical address for all public schools, school districts, and state education agencies in the United States. The NCES EDGE program collaborates with the U.S. Census Bureau\u2019s Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for schools and school district administrative offices based on these addresses. The point locations in this data layer were developed from the 2015-2016 CCD collection. For more information about NCES school point data, see:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' rel='nofollow ugc'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>.</span></p><p><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</span><br /></p></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/9f7c5c08e2df46eebbff76717effe2dd/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/9f7c5c08e2df46eebbff76717effe2dd/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-office-locations-2015-16",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-office-locations-2015-16"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICLEA_1516/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICLEA_1516/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Geocodes: Public Schools and Local Education Agencies",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_GEOCODE_PUBLIC_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Public Schools and Local Education Agencies"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Geocodes: Public Schools and Local Education Agencies",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PUBLICLEA_1516.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Public Schools and Local Education Agencies"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9f7c5c08e2df46eebbff76717effe2dd/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9f7c5c08e2df46eebbff76717effe2dd/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9f7c5c08e2df46eebbff76717effe2dd/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9f7c5c08e2df46eebbff76717effe2dd/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9f7c5c08e2df46eebbff76717effe2dd/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9f7c5c08e2df46eebbff76717effe2dd/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9f7c5c08e2df46eebbff76717effe2dd/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9f7c5c08e2df46eebbff76717effe2dd/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "b4f1b4f6-5538-4bfb-b2a6-b159ad20c143",
+            "issued": "2020-03-24T12:49:28.000Z",
             "keyword": [
                 "ccd",
                 "common-core-of-data",
@@ -13335,25 +13314,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:38.311128",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Locale - Current",
-            "description": "<div style='text-align:Left;'><p>This data layer produced by the National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimates (EDGE) program provides a geographic locale framework that classifies all U.S. territory into twelve categories ranging from Large Cities to Remote Rural areas. NCES uses this framework to describe the type of geographic area where schools and school districts are located. The criteria for these classifications are defined by NCES and rely on standard geographic areas developed and maintained by the U.S. Census Bureau. The NCES Locale boundaries are based on geographic areas represented in Census TIGER/Line. For more information about the NCES locale framework, and to download the data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries</a>. The classifications include:</p><div><ul><li>City - Large (11): Territory inside an Urban Area with a population of 50,000 or more and inside a Principal City with population of 250,000 or more.</li><li>City - Midsize (12): Territory inside an Urban Area with a population of 50,000 or more and inside a Principal City with population less than 250,000 and greater than or equal to 100,000.</li><li>City - Small (13): Territory inside an Urban Area with a population of 50,000 or more and inside a Principal City with population less than 100,000.</li><li>Suburb \u2013 Large (21): Territory outside a Principal City and inside an Urban Area with population of 250,000 or more.</li><li>Suburb - Midsize (22): Territory outside a Principal City and inside an Urban Area with population less than 250,000 and greater than or equal to 100,000.</li><li>Suburb - Small (23): Territory outside a Principal City and inside an Urban Area with population less than 100,000.\u00a0</li><li>Town - Fringe (31): Territory inside an Urban Area with a population less than 50,000 that is less than or equal to 10 miles from an Urban Area with a population of 50,000 or more.</li><li>Town - Distant (32): Territory inside an Urban Area with a population less than 50,000 that is more than 10 miles and less than or equal to 35 miles from an Urban Area with a population of 50,000 or more.</li><li>Town - Remote (33): Territory inside an Urban Area with a population less than 50,000 that is more than 35 miles of an Urban Area with a population of 50,000 or more.</li><li>Rural - Fringe (41): Census-defined rural territory that is less than or equal to 5 miles from an Urban Area of 50,000 or more, as well as rural territory that is less than or equal to 2.5 miles from an Urban Area with a population less than 50,000.</li><li>Rural - Distant (42): Census-defined rural territory that is more than 5 miles but less than or equal to 25 miles from an Urban Area with a population of 50,000 or more, as well as rural territory that is more than 2.5 miles but less than or equal to 10 miles from an Urban Area with a population less than 50,000.</li><li>Rural - Remote (43): Census-defined rural territory that is more than 25 miles from an Urban Area with a population of 50,000 or more and is also more than 10 miles from an Urban Area with a population less than 50,000.</li></ul></div><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></p><p></p></div>",
-            "modified": "2024-10-19T12:47:37.569995",
-            "accessLevel": "public",
-            "identifier": "a2b57585-e027-4895-a93d-c47b03cfe950",
-            "issued": "2020-03-30T13:33:51.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -13374,77 +13339,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "School District Office Locations 2015-16"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><p>This data layer produced by the National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimates (EDGE) program provides a geographic locale framework that classifies all U.S. territory into twelve categories ranging from Large Cities to Remote Rural areas. NCES uses this framework to describe the type of geographic area where schools and school districts are located. The criteria for these classifications are defined by NCES and rely on standard geographic areas developed and maintained by the U.S. Census Bureau. The NCES Locale boundaries are based on geographic areas represented in Census TIGER/Line. For more information about the NCES locale framework, and to download the data, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/LocaleBoundaries</a>. The classifications include:</p><div><ul><li>City - Large (11): Territory inside an Urban Area with a population of 50,000 or more and inside a Principal City with population of 250,000 or more.</li><li>City - Midsize (12): Territory inside an Urban Area with a population of 50,000 or more and inside a Principal City with population less than 250,000 and greater than or equal to 100,000.</li><li>City - Small (13): Territory inside an Urban Area with a population of 50,000 or more and inside a Principal City with population less than 100,000.</li><li>Suburb \u2013 Large (21): Territory outside a Principal City and inside an Urban Area with population of 250,000 or more.</li><li>Suburb - Midsize (22): Territory outside a Principal City and inside an Urban Area with population less than 250,000 and greater than or equal to 100,000.</li><li>Suburb - Small (23): Territory outside a Principal City and inside an Urban Area with population less than 100,000.\u00a0</li><li>Town - Fringe (31): Territory inside an Urban Area with a population less than 50,000 that is less than or equal to 10 miles from an Urban Area with a population of 50,000 or more.</li><li>Town - Distant (32): Territory inside an Urban Area with a population less than 50,000 that is more than 10 miles and less than or equal to 35 miles from an Urban Area with a population of 50,000 or more.</li><li>Town - Remote (33): Territory inside an Urban Area with a population less than 50,000 that is more than 35 miles of an Urban Area with a population of 50,000 or more.</li><li>Rural - Fringe (41): Census-defined rural territory that is less than or equal to 5 miles from an Urban Area of 50,000 or more, as well as rural territory that is less than or equal to 2.5 miles from an Urban Area with a population less than 50,000.</li><li>Rural - Distant (42): Census-defined rural territory that is more than 5 miles but less than or equal to 25 miles from an Urban Area with a population of 50,000 or more, as well as rural territory that is more than 2.5 miles but less than or equal to 10 miles from an Urban Area with a population less than 50,000.</li><li>Rural - Remote (43): Census-defined rural territory that is more than 25 miles from an Urban Area with a population of 50,000 or more and is also more than 10 miles from an Urban Area with a population less than 50,000.</li></ul></div><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></p><p></p></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/943b5ef4f7b241e397f06d5822f060ec/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/943b5ef4f7b241e397f06d5822f060ec/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::locale-current-1",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::locale-current-1"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://services1.arcgis.com/Ua5sjt3LWTPigjyD/arcgis/rest/services/Locale_Current/FeatureServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://services1.arcgis.com/Ua5sjt3LWTPigjyD/arcgis/rest/services/Locale_Current/FeatureServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Locale Boundaries File Documentation",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_NCES_LOCALE.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Locale Boundaries File Documentation"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Entire US",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_Locale21_US.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Entire US"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/943b5ef4f7b241e397f06d5822f060ec/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/943b5ef4f7b241e397f06d5822f060ec/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/943b5ef4f7b241e397f06d5822f060ec/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/943b5ef4f7b241e397f06d5822f060ec/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/943b5ef4f7b241e397f06d5822f060ec/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/943b5ef4f7b241e397f06d5822f060ec/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/943b5ef4f7b241e397f06d5822f060ec/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/943b5ef4f7b241e397f06d5822f060ec/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "a2b57585-e027-4895-a93d-c47b03cfe950",
+            "issued": "2020-03-30T13:33:51.000Z",
             "keyword": [
                 "city",
                 "distant",
@@ -13460,25 +13439,11 @@
                 "suburb",
                 "town"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:37.569995",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ACS-ED 2013-2017 Children-Enrolled Public: Social Characteristics (CDP02)",
-            "description": "<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The American Community Survey Education Tabulation (ACS-ED) is a custom tabulation of the ACS produced for the National Center of Education Statistics (NCES) by the U.S. Census Bureau. The ACS-ED provides a rich collection of social, economic, demographic, and housing characteristics for school systems, school-age children, and the parents of school-age children. In addition to focusing on school-age children, the ACS-ED provides enrollment iterations for children enrolled in public school. The data profiles include percentages (along with associated margins of error) that allow for comparison of school district-level conditions across the U.S. For more information about the NCES ACS-ED collection, visit the NCES Education Demographic and Geographic Estimates (EDGE) program at:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Demographic/ACS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Demographic/ACS</a><div><br /></div><div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Annotation values are negative value representations of estimates and have values when non-integer information needs to be represented. See the table below for a list of common Estimate/Margin of Error (E/M) values and their corresponding Annotation (EA/MA) values.</div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><table border='0' cellpadding='0' cellspacing='0' style='margin-bottom:1.5rem; width:467.5pt; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial; border-collapse:collapse; border-spacing:0px; border:1px solid rgb(204, 204, 204); font-size:0.875rem;' width='623'><tbody><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-9</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:1pt solid windowtext; border-bottom:1pt solid windowtext; border-image:initial;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-9' entry in the estimate and margin of error columns indicates that data for this geographic area cannot be displayed because the number of sample cases is too small.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-8</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-8' means that the estimate is not applicable or not available.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-6</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-6' entry in the estimate column indicates that either no sample observations or too few sample observations were available to compute an\u00a0 \u00a0estimate, or a ratio of medians cannot be calculated because one or both of the median estimates falls in the lowest interval or upper interval of an open-ended distribution.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-5</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-5' entry in the margin of error column indicates that the estimate is controlled. A statistical test for sampling variability is not appropriate.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-3</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-3' entry in the margin of error column indicates that the median falls in the lowest interval or upper interval of an open-ended distribution. A statistical test is not appropriate.</span></p></td></tr><tr style='border-bottom:none;'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-2</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-2' entry in the margin of error column indicates that either no sample observations or too few sample observations were available to compute a standard error and thus the margin of error. A statistical test is not appropriate.</span></p></td></tr></tbody></table></div></div>",
-            "modified": "2024-10-19T12:47:36.580221",
-            "accessLevel": "public",
-            "identifier": "dadc0dd5-c806-4a9d-88b9-a5707bdd4ced",
-            "issued": "2020-12-15T00:00:15.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -13499,63 +13464,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Locale - Current"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The American Community Survey Education Tabulation (ACS-ED) is a custom tabulation of the ACS produced for the National Center of Education Statistics (NCES) by the U.S. Census Bureau. The ACS-ED provides a rich collection of social, economic, demographic, and housing characteristics for school systems, school-age children, and the parents of school-age children. In addition to focusing on school-age children, the ACS-ED provides enrollment iterations for children enrolled in public school. The data profiles include percentages (along with associated margins of error) that allow for comparison of school district-level conditions across the U.S. For more information about the NCES ACS-ED collection, visit the NCES Education Demographic and Geographic Estimates (EDGE) program at:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Demographic/ACS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Demographic/ACS</a><div><br /></div><div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Annotation values are negative value representations of estimates and have values when non-integer information needs to be represented. See the table below for a list of common Estimate/Margin of Error (E/M) values and their corresponding Annotation (EA/MA) values.</div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><table border='0' cellpadding='0' cellspacing='0' style='margin-bottom:1.5rem; width:467.5pt; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial; border-collapse:collapse; border-spacing:0px; border:1px solid rgb(204, 204, 204); font-size:0.875rem;' width='623'><tbody><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-9</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:1pt solid windowtext; border-bottom:1pt solid windowtext; border-image:initial;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-9' entry in the estimate and margin of error columns indicates that data for this geographic area cannot be displayed because the number of sample cases is too small.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-8</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-8' means that the estimate is not applicable or not available.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-6</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-6' entry in the estimate column indicates that either no sample observations or too few sample observations were available to compute an\u00a0 \u00a0estimate, or a ratio of medians cannot be calculated because one or both of the median estimates falls in the lowest interval or upper interval of an open-ended distribution.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-5</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-5' entry in the margin of error column indicates that the estimate is controlled. A statistical test for sampling variability is not appropriate.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-3</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-3' entry in the margin of error column indicates that the median falls in the lowest interval or upper interval of an open-ended distribution. A statistical test is not appropriate.</span></p></td></tr><tr style='border-bottom:none;'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-2</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-2' entry in the margin of error column indicates that either no sample observations or too few sample observations were available to compute a standard error and thus the margin of error. A statistical test is not appropriate.</span></p></td></tr></tbody></table></div></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/e46b2d31d4bc48f19a8362ddf613355e/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/e46b2d31d4bc48f19a8362ddf613355e/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::acs-ed-2013-2017-children-enrolled-public-social-characteristics-cdp02",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::acs-ed-2013-2017-children-enrolled-public-social-characteristics-cdp02"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Social_Economic/ACS_OpenData_1317/MapServer/1",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Social_Economic/ACS_OpenData_1317/MapServer/1"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/e46b2d31d4bc48f19a8362ddf613355e/csv?layers=1",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/e46b2d31d4bc48f19a8362ddf613355e/csv?layers=1"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/e46b2d31d4bc48f19a8362ddf613355e/geojson?layers=1",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/e46b2d31d4bc48f19a8362ddf613355e/geojson?layers=1"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/e46b2d31d4bc48f19a8362ddf613355e/shapefile?layers=1",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/e46b2d31d4bc48f19a8362ddf613355e/shapefile?layers=1"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/e46b2d31d4bc48f19a8362ddf613355e/kml?layers=1",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/e46b2d31d4bc48f19a8362ddf613355e/kml?layers=1"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "dadc0dd5-c806-4a9d-88b9-a5707bdd4ced",
+            "issued": "2020-12-15T00:00:15.000Z",
             "keyword": [
                 "acs",
                 "acs-ed",
@@ -13569,25 +13548,11 @@
                 "u-s-census-bureau",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:36.580221",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ACS-ED 2013-2017 Children-Enrolled Public: Demographic Characteristics (CDP05)",
-            "description": "<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The American Community Survey Education Tabulation (ACS-ED) is a custom tabulation of the ACS produced for the National Center of Education Statistics (NCES) by the U.S. Census Bureau. The ACS-ED provides a rich collection of social, economic, demographic, and housing characteristics for school systems, school-age children, and the parents of school-age children. In addition to focusing on school-age children, the ACS-ED provides enrollment iterations for children enrolled in public school. The data profiles include percentages (along with associated margins of error) that allow for comparison of school district-level conditions across the U.S. For more information about the NCES ACS-ED collection, visit the NCES Education Demographic and Geographic Estimates (EDGE) program at:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Demographic/ACS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Demographic/ACS</a><div><br /></div><div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Annotation values are negative value representations of estimates and have values when non-integer information needs to be represented. See the table below for a list of common Estimate/Margin of Error (E/M) values and their corresponding Annotation (EA/MA) values.</div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><table border='0' cellpadding='0' cellspacing='0' style='margin-bottom:1.5rem; width:467.5pt; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial; border-collapse:collapse; border-spacing:0px; border:1px solid rgb(204, 204, 204); font-size:0.875rem;' width='623'><tbody><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-9</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:1pt solid windowtext; border-bottom:1pt solid windowtext; border-image:initial;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-9' entry in the estimate and margin of error columns indicates that data for this geographic area cannot be displayed because the number of sample cases is too small.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-8</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-8' means that the estimate is not applicable or not available.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-6</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-6' entry in the estimate column indicates that either no sample observations or too few sample observations were available to compute an\u00a0 \u00a0estimate, or a ratio of medians cannot be calculated because one or both of the median estimates falls in the lowest interval or upper interval of an open-ended distribution.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-5</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-5' entry in the margin of error column indicates that the estimate is controlled. A statistical test for sampling variability is not appropriate.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-3</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-3' entry in the margin of error column indicates that the median falls in the lowest interval or upper interval of an open-ended distribution. A statistical test is not appropriate.</span></p></td></tr><tr style='border-bottom:none;'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-2</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-2' entry in the margin of error column indicates that either no sample observations or too few sample observations were available to compute a standard error and thus the margin of error. A statistical test is not appropriate.</span></p></td></tr></tbody></table></div></div>",
-            "modified": "2024-10-19T12:47:35.526962",
-            "accessLevel": "public",
-            "identifier": "9e8b658c-25f2-4e75-aac0-3b9d8ad1fdba",
-            "issued": "2020-12-15T00:09:49.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -13608,63 +13573,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "ACS-ED 2013-2017 Children-Enrolled Public: Social Characteristics (CDP02)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The American Community Survey Education Tabulation (ACS-ED) is a custom tabulation of the ACS produced for the National Center of Education Statistics (NCES) by the U.S. Census Bureau. The ACS-ED provides a rich collection of social, economic, demographic, and housing characteristics for school systems, school-age children, and the parents of school-age children. In addition to focusing on school-age children, the ACS-ED provides enrollment iterations for children enrolled in public school. The data profiles include percentages (along with associated margins of error) that allow for comparison of school district-level conditions across the U.S. For more information about the NCES ACS-ED collection, visit the NCES Education Demographic and Geographic Estimates (EDGE) program at:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Demographic/ACS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Demographic/ACS</a><div><br /></div><div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Annotation values are negative value representations of estimates and have values when non-integer information needs to be represented. See the table below for a list of common Estimate/Margin of Error (E/M) values and their corresponding Annotation (EA/MA) values.</div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><table border='0' cellpadding='0' cellspacing='0' style='margin-bottom:1.5rem; width:467.5pt; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial; border-collapse:collapse; border-spacing:0px; border:1px solid rgb(204, 204, 204); font-size:0.875rem;' width='623'><tbody><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-9</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:1pt solid windowtext; border-bottom:1pt solid windowtext; border-image:initial;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-9' entry in the estimate and margin of error columns indicates that data for this geographic area cannot be displayed because the number of sample cases is too small.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-8</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-8' means that the estimate is not applicable or not available.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-6</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-6' entry in the estimate column indicates that either no sample observations or too few sample observations were available to compute an\u00a0 \u00a0estimate, or a ratio of medians cannot be calculated because one or both of the median estimates falls in the lowest interval or upper interval of an open-ended distribution.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-5</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-5' entry in the margin of error column indicates that the estimate is controlled. A statistical test for sampling variability is not appropriate.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-3</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-3' entry in the margin of error column indicates that the median falls in the lowest interval or upper interval of an open-ended distribution. A statistical test is not appropriate.</span></p></td></tr><tr style='border-bottom:none;'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-2</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-2' entry in the margin of error column indicates that either no sample observations or too few sample observations were available to compute a standard error and thus the margin of error. A statistical test is not appropriate.</span></p></td></tr></tbody></table></div></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/b05fb5f490484ea5840cc67e3379e764/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/b05fb5f490484ea5840cc67e3379e764/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::acs-ed-2013-2017-children-enrolled-public-demographic-characteristics-cdp05",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::acs-ed-2013-2017-children-enrolled-public-demographic-characteristics-cdp05"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Social_Economic/ACS_OpenData_1317/MapServer/7",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Social_Economic/ACS_OpenData_1317/MapServer/7"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b05fb5f490484ea5840cc67e3379e764/csv?layers=7",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b05fb5f490484ea5840cc67e3379e764/csv?layers=7"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b05fb5f490484ea5840cc67e3379e764/geojson?layers=7",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b05fb5f490484ea5840cc67e3379e764/geojson?layers=7"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b05fb5f490484ea5840cc67e3379e764/shapefile?layers=7",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b05fb5f490484ea5840cc67e3379e764/shapefile?layers=7"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b05fb5f490484ea5840cc67e3379e764/kml?layers=7",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b05fb5f490484ea5840cc67e3379e764/kml?layers=7"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "9e8b658c-25f2-4e75-aac0-3b9d8ad1fdba",
+            "issued": "2020-12-15T00:09:49.000Z",
             "keyword": [
                 "acs",
                 "acs-ed",
@@ -13679,25 +13658,11 @@
                 "u-s-census-bureau",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:35.526962",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ACS-ED 2013-2017 Children-Enrolled Public: Economic Characteristics (CDP03)",
-            "description": "<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The American Community Survey Education Tabulation (ACS-ED) is a custom tabulation of the ACS produced for the National Center of Education Statistics (NCES) by the U.S. Census Bureau. The ACS-ED provides a rich collection of social, economic, demographic, and housing characteristics for school systems, school-age children, and the parents of school-age children. In addition to focusing on school-age children, the ACS-ED provides enrollment iterations for children enrolled in public school. The data profiles include percentages (along with associated margins of error) that allow for comparison of school district-level conditions across the U.S. For more information about the NCES ACS-ED collection, visit the NCES Education Demographic and Geographic Estimates (EDGE) program at:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Demographic/ACS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Demographic/ACS</a><div><br /></div><div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Annotation values are negative value representations of estimates and have values when non-integer information needs to be represented. See the table below for a list of common Estimate/Margin of Error (E/M) values and their corresponding Annotation (EA/MA) values.</div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><table border='0' cellpadding='0' cellspacing='0' style='margin-bottom:1.5rem; width:467.5pt; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial; border-collapse:collapse; border-spacing:0px; border:1px solid rgb(204, 204, 204); font-size:0.875rem;' width='623'><tbody><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-9</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:1pt solid windowtext; border-bottom:1pt solid windowtext; border-image:initial;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-9' entry in the estimate and margin of error columns indicates that data for this geographic area cannot be displayed because the number of sample cases is too small.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-8</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-8' means that the estimate is not applicable or not available.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-6</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-6' entry in the estimate column indicates that either no sample observations or too few sample observations were available to compute an\u00a0 \u00a0estimate, or a ratio of medians cannot be calculated because one or both of the median estimates falls in the lowest interval or upper interval of an open-ended distribution.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-5</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-5' entry in the margin of error column indicates that the estimate is controlled. A statistical test for sampling variability is not appropriate.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-3</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-3' entry in the margin of error column indicates that the median falls in the lowest interval or upper interval of an open-ended distribution. A statistical test is not appropriate.</span></p></td></tr><tr style='border-bottom:none;'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-2</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-2' entry in the margin of error column indicates that either no sample observations or too few sample observations were available to compute a standard error and thus the margin of error. A statistical test is not appropriate.</span></p></td></tr></tbody></table></div></div>",
-            "modified": "2024-10-19T12:47:34.299390",
-            "accessLevel": "public",
-            "identifier": "60623339-008b-4b38-924e-3097911969f4",
-            "issued": "2020-12-15T00:13:00.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -13718,63 +13683,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "ACS-ED 2013-2017 Children-Enrolled Public: Demographic Characteristics (CDP05)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The American Community Survey Education Tabulation (ACS-ED) is a custom tabulation of the ACS produced for the National Center of Education Statistics (NCES) by the U.S. Census Bureau. The ACS-ED provides a rich collection of social, economic, demographic, and housing characteristics for school systems, school-age children, and the parents of school-age children. In addition to focusing on school-age children, the ACS-ED provides enrollment iterations for children enrolled in public school. The data profiles include percentages (along with associated margins of error) that allow for comparison of school district-level conditions across the U.S. For more information about the NCES ACS-ED collection, visit the NCES Education Demographic and Geographic Estimates (EDGE) program at:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Demographic/ACS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Demographic/ACS</a><div><br /></div><div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Annotation values are negative value representations of estimates and have values when non-integer information needs to be represented. See the table below for a list of common Estimate/Margin of Error (E/M) values and their corresponding Annotation (EA/MA) values.</div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><table border='0' cellpadding='0' cellspacing='0' style='margin-bottom:1.5rem; width:467.5pt; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial; border-collapse:collapse; border-spacing:0px; border:1px solid rgb(204, 204, 204); font-size:0.875rem;' width='623'><tbody><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-9</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:1pt solid windowtext; border-bottom:1pt solid windowtext; border-image:initial;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-9' entry in the estimate and margin of error columns indicates that data for this geographic area cannot be displayed because the number of sample cases is too small.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-8</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-8' means that the estimate is not applicable or not available.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-6</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-6' entry in the estimate column indicates that either no sample observations or too few sample observations were available to compute an\u00a0 \u00a0estimate, or a ratio of medians cannot be calculated because one or both of the median estimates falls in the lowest interval or upper interval of an open-ended distribution.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-5</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-5' entry in the margin of error column indicates that the estimate is controlled. A statistical test for sampling variability is not appropriate.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-3</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-3' entry in the margin of error column indicates that the median falls in the lowest interval or upper interval of an open-ended distribution. A statistical test is not appropriate.</span></p></td></tr><tr style='border-bottom:none;'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-2</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-2' entry in the margin of error column indicates that either no sample observations or too few sample observations were available to compute a standard error and thus the margin of error. A statistical test is not appropriate.</span></p></td></tr></tbody></table></div></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/7d9645640d1a432db836cb5ce9dcc3f4/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/7d9645640d1a432db836cb5ce9dcc3f4/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::acs-ed-2013-2017-children-enrolled-public-economic-characteristics-cdp03",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::acs-ed-2013-2017-children-enrolled-public-economic-characteristics-cdp03"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Social_Economic/ACS_OpenData_1317/MapServer/3",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Social_Economic/ACS_OpenData_1317/MapServer/3"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/7d9645640d1a432db836cb5ce9dcc3f4/csv?layers=3",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/7d9645640d1a432db836cb5ce9dcc3f4/csv?layers=3"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/7d9645640d1a432db836cb5ce9dcc3f4/geojson?layers=3",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/7d9645640d1a432db836cb5ce9dcc3f4/geojson?layers=3"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/7d9645640d1a432db836cb5ce9dcc3f4/shapefile?layers=3",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/7d9645640d1a432db836cb5ce9dcc3f4/shapefile?layers=3"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/7d9645640d1a432db836cb5ce9dcc3f4/kml?layers=3",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/7d9645640d1a432db836cb5ce9dcc3f4/kml?layers=3"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "60623339-008b-4b38-924e-3097911969f4",
+            "issued": "2020-12-15T00:13:00.000Z",
             "keyword": [
                 "acs",
                 "acs-ed",
@@ -13788,25 +13767,11 @@
                 "u-s-census-bureau",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:34.299390",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ACS-ED 2013-2017 Total Population: Housing Characteristics (DP04)",
-            "description": "<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The American Community Survey Education Tabulation (ACS-ED) is a custom tabulation of the ACS produced for the National Center of Education Statistics (NCES) by the U.S. Census Bureau. The ACS-ED provides a rich collection of social, economic, demographic, and housing characteristics for school systems, school-age children, and the parents of school-age children. In addition to focusing on school-age children, the ACS-ED provides enrollment iterations for children enrolled in public school. The data profiles include percentages (along with associated margins of error) that allow for comparison of school district-level conditions across the U.S. For more information about the NCES ACS-ED collection, visit the NCES Education Demographic and Geographic Estimates (EDGE) program at:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Demographic/ACS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Demographic/ACS</a><div><br /></div><div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Annotation values are negative value representations of estimates and have values when non-integer information needs to be represented. See the table below for a list of common Estimate/Margin of Error (E/M) values and their corresponding Annotation (EA/MA) values.</div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><table border='0' cellpadding='0' cellspacing='0' style='margin-bottom:1.5rem; width:467.5pt; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial; border-collapse:collapse; border-spacing:0px; border:1px solid rgb(204, 204, 204); font-size:0.875rem;' width='623'><tbody><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-9</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:1pt solid windowtext; border-bottom:1pt solid windowtext; border-image:initial;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-9' entry in the estimate and margin of error columns indicates that data for this geographic area cannot be displayed because the number of sample cases is too small.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-8</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-8' means that the estimate is not applicable or not available.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-6</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-6' entry in the estimate column indicates that either no sample observations or too few sample observations were available to compute an\u00a0 \u00a0estimate, or a ratio of medians cannot be calculated because one or both of the median estimates falls in the lowest interval or upper interval of an open-ended distribution.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-5</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-5' entry in the margin of error column indicates that the estimate is controlled. A statistical test for sampling variability is not appropriate.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-3</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-3' entry in the margin of error column indicates that the median falls in the lowest interval or upper interval of an open-ended distribution. A statistical test is not appropriate.</span></p></td></tr><tr style='border-bottom:none;'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-2</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-2' entry in the margin of error column indicates that either no sample observations or too few sample observations were available to compute a standard error and thus the margin of error. A statistical test is not appropriate.</span></p></td></tr></tbody></table></div></div>",
-            "modified": "2024-10-19T12:47:33.363857",
-            "accessLevel": "public",
-            "identifier": "dd0e8bb5-e4ea-41f9-9bd6-c517fbdbd835",
-            "issued": "2020-12-14T23:30:02.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -13827,63 +13792,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "ACS-ED 2013-2017 Children-Enrolled Public: Economic Characteristics (CDP03)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The American Community Survey Education Tabulation (ACS-ED) is a custom tabulation of the ACS produced for the National Center of Education Statistics (NCES) by the U.S. Census Bureau. The ACS-ED provides a rich collection of social, economic, demographic, and housing characteristics for school systems, school-age children, and the parents of school-age children. In addition to focusing on school-age children, the ACS-ED provides enrollment iterations for children enrolled in public school. The data profiles include percentages (along with associated margins of error) that allow for comparison of school district-level conditions across the U.S. For more information about the NCES ACS-ED collection, visit the NCES Education Demographic and Geographic Estimates (EDGE) program at:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Demographic/ACS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Demographic/ACS</a><div><br /></div><div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Annotation values are negative value representations of estimates and have values when non-integer information needs to be represented. See the table below for a list of common Estimate/Margin of Error (E/M) values and their corresponding Annotation (EA/MA) values.</div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><table border='0' cellpadding='0' cellspacing='0' style='margin-bottom:1.5rem; width:467.5pt; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial; border-collapse:collapse; border-spacing:0px; border:1px solid rgb(204, 204, 204); font-size:0.875rem;' width='623'><tbody><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-9</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:1pt solid windowtext; border-bottom:1pt solid windowtext; border-image:initial;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-9' entry in the estimate and margin of error columns indicates that data for this geographic area cannot be displayed because the number of sample cases is too small.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-8</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-8' means that the estimate is not applicable or not available.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-6</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-6' entry in the estimate column indicates that either no sample observations or too few sample observations were available to compute an\u00a0 \u00a0estimate, or a ratio of medians cannot be calculated because one or both of the median estimates falls in the lowest interval or upper interval of an open-ended distribution.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-5</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-5' entry in the margin of error column indicates that the estimate is controlled. A statistical test for sampling variability is not appropriate.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-3</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-3' entry in the margin of error column indicates that the median falls in the lowest interval or upper interval of an open-ended distribution. A statistical test is not appropriate.</span></p></td></tr><tr style='border-bottom:none;'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-2</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-2' entry in the margin of error column indicates that either no sample observations or too few sample observations were available to compute a standard error and thus the margin of error. A statistical test is not appropriate.</span></p></td></tr></tbody></table></div></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/500ff4afc04045258e5eeeb36452ce71/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/500ff4afc04045258e5eeeb36452ce71/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::acs-ed-2013-2017-total-population-housing-characteristics-dp04",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::acs-ed-2013-2017-total-population-housing-characteristics-dp04"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Social_Economic/ACS_OpenData_1317/MapServer/10",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Social_Economic/ACS_OpenData_1317/MapServer/10"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/500ff4afc04045258e5eeeb36452ce71/csv?layers=10",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/500ff4afc04045258e5eeeb36452ce71/csv?layers=10"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/500ff4afc04045258e5eeeb36452ce71/geojson?layers=10",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/500ff4afc04045258e5eeeb36452ce71/geojson?layers=10"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/500ff4afc04045258e5eeeb36452ce71/shapefile?layers=10",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/500ff4afc04045258e5eeeb36452ce71/shapefile?layers=10"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/500ff4afc04045258e5eeeb36452ce71/kml?layers=10",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/500ff4afc04045258e5eeeb36452ce71/kml?layers=10"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "dd0e8bb5-e4ea-41f9-9bd6-c517fbdbd835",
+            "issued": "2020-12-14T23:30:02.000Z",
             "keyword": [
                 "acs",
                 "acs-ed",
@@ -13898,25 +13877,11 @@
                 "u-s-census-bureau",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:33.363857",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ACS-ED 2013-2017 Children-Enrolled Public: Housing Characteristics (CDP04)",
-            "description": "<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The American Community Survey Education Tabulation (ACS-ED) is a custom tabulation of the ACS produced for the National Center of Education Statistics (NCES) by the U.S. Census Bureau. The ACS-ED provides a rich collection of social, economic, demographic, and housing characteristics for school systems, school-age children, and the parents of school-age children. In addition to focusing on school-age children, the ACS-ED provides enrollment iterations for children enrolled in public school. The data profiles include percentages (along with associated margins of error) that allow for comparison of school district-level conditions across the U.S. For more information about the NCES ACS-ED collection, visit the NCES Education Demographic and Geographic Estimates (EDGE) program at:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Demographic/ACS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Demographic/ACS</a><div><br /></div><div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Annotation values are negative value representations of estimates and have values when non-integer information needs to be represented. See the table below for a list of common Estimate/Margin of Error (E/M) values and their corresponding Annotation (EA/MA) values.</div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><table border='0' cellpadding='0' cellspacing='0' style='margin-bottom:1.5rem; width:467.5pt; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial; border-collapse:collapse; border-spacing:0px; border:1px solid rgb(204, 204, 204); font-size:0.875rem;' width='623'><tbody><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-9</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:1pt solid windowtext; border-bottom:1pt solid windowtext; border-image:initial;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-9' entry in the estimate and margin of error columns indicates that data for this geographic area cannot be displayed because the number of sample cases is too small.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-8</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-8' means that the estimate is not applicable or not available.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-6</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-6' entry in the estimate column indicates that either no sample observations or too few sample observations were available to compute an\u00a0 \u00a0estimate, or a ratio of medians cannot be calculated because one or both of the median estimates falls in the lowest interval or upper interval of an open-ended distribution.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-5</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-5' entry in the margin of error column indicates that the estimate is controlled. A statistical test for sampling variability is not appropriate.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-3</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-3' entry in the margin of error column indicates that the median falls in the lowest interval or upper interval of an open-ended distribution. A statistical test is not appropriate.</span></p></td></tr><tr style='border-bottom:none;'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-2</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-2' entry in the margin of error column indicates that either no sample observations or too few sample observations were available to compute a standard error and thus the margin of error. A statistical test is not appropriate.</span></p></td></tr></tbody></table></div></div>",
-            "modified": "2024-10-19T12:47:32.227630",
-            "accessLevel": "public",
-            "identifier": "5799eeb4-d3a5-47fd-99b9-84af2f103887",
-            "issued": "2020-12-15T00:03:54.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -13937,63 +13902,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "ACS-ED 2013-2017 Total Population: Housing Characteristics (DP04)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The American Community Survey Education Tabulation (ACS-ED) is a custom tabulation of the ACS produced for the National Center of Education Statistics (NCES) by the U.S. Census Bureau. The ACS-ED provides a rich collection of social, economic, demographic, and housing characteristics for school systems, school-age children, and the parents of school-age children. In addition to focusing on school-age children, the ACS-ED provides enrollment iterations for children enrolled in public school. The data profiles include percentages (along with associated margins of error) that allow for comparison of school district-level conditions across the U.S. For more information about the NCES ACS-ED collection, visit the NCES Education Demographic and Geographic Estimates (EDGE) program at:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Demographic/ACS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Demographic/ACS</a><div><br /></div><div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Annotation values are negative value representations of estimates and have values when non-integer information needs to be represented. See the table below for a list of common Estimate/Margin of Error (E/M) values and their corresponding Annotation (EA/MA) values.</div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><table border='0' cellpadding='0' cellspacing='0' style='margin-bottom:1.5rem; width:467.5pt; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial; border-collapse:collapse; border-spacing:0px; border:1px solid rgb(204, 204, 204); font-size:0.875rem;' width='623'><tbody><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-9</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:1pt solid windowtext; border-bottom:1pt solid windowtext; border-image:initial;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-9' entry in the estimate and margin of error columns indicates that data for this geographic area cannot be displayed because the number of sample cases is too small.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-8</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-8' means that the estimate is not applicable or not available.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-6</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-6' entry in the estimate column indicates that either no sample observations or too few sample observations were available to compute an\u00a0 \u00a0estimate, or a ratio of medians cannot be calculated because one or both of the median estimates falls in the lowest interval or upper interval of an open-ended distribution.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-5</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-5' entry in the margin of error column indicates that the estimate is controlled. A statistical test for sampling variability is not appropriate.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-3</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-3' entry in the margin of error column indicates that the median falls in the lowest interval or upper interval of an open-ended distribution. A statistical test is not appropriate.</span></p></td></tr><tr style='border-bottom:none;'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-2</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-2' entry in the margin of error column indicates that either no sample observations or too few sample observations were available to compute a standard error and thus the margin of error. A statistical test is not appropriate.</span></p></td></tr></tbody></table></div></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/b91c0ab6a41847ff994a9f0a7441c1ab/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/b91c0ab6a41847ff994a9f0a7441c1ab/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::acs-ed-2013-2017-children-enrolled-public-housing-characteristics-cdp04",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::acs-ed-2013-2017-children-enrolled-public-housing-characteristics-cdp04"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Social_Economic/ACS_OpenData_1317/MapServer/5",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Social_Economic/ACS_OpenData_1317/MapServer/5"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b91c0ab6a41847ff994a9f0a7441c1ab/csv?layers=5",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b91c0ab6a41847ff994a9f0a7441c1ab/csv?layers=5"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b91c0ab6a41847ff994a9f0a7441c1ab/geojson?layers=5",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b91c0ab6a41847ff994a9f0a7441c1ab/geojson?layers=5"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b91c0ab6a41847ff994a9f0a7441c1ab/shapefile?layers=5",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b91c0ab6a41847ff994a9f0a7441c1ab/shapefile?layers=5"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b91c0ab6a41847ff994a9f0a7441c1ab/kml?layers=5",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/b91c0ab6a41847ff994a9f0a7441c1ab/kml?layers=5"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "5799eeb4-d3a5-47fd-99b9-84af2f103887",
+            "issued": "2020-12-15T00:03:54.000Z",
             "keyword": [
                 "acs",
                 "acs-ed",
@@ -14007,25 +13986,11 @@
                 "u-s-census-bureau",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:32.227630",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ACS-ED 2013-2017 Total Population: Demographic Characteristics (DP05)",
-            "description": "<div><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The American Community Survey Education Tabulation (ACS-ED) is a custom tabulation of the ACS produced for the National Center of Education Statistics (NCES) by the U.S. Census Bureau. The ACS-ED provides a rich collection of social, economic, demographic, and housing characteristics for school systems, school-age children, and the parents of school-age children. In addition to focusing on school-age children, the ACS-ED provides enrollment iterations for children enrolled in public school. The data profiles include percentages (along with associated margins of error) that allow for comparison of school district-level conditions across the U.S. For more information about the NCES ACS-ED collection, visit the NCES Education Demographic and Geographic Estimates (EDGE) program at:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Demographic/ACS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Demographic/ACS</a></div><div><br /></div><div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Annotation values are negative value representations of estimates and have values when non-integer information needs to be represented. See the table below for a list of common Estimate/Margin of Error (E/M) values and their corresponding Annotation (EA/MA) values.</div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. \nData users are advised to review NCES program documentation and feature \nclass metadata to understand the limitations and appropriate use of \nthese data.<br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><table border='0' cellpadding='0' cellspacing='0' style='margin-bottom:1.5rem; width:467.5pt; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial; border-collapse:collapse; border-spacing:0px; border:1px solid rgb(204, 204, 204); font-size:0.875rem;' width='623'><tbody><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-9</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:1pt solid windowtext; border-bottom:1pt solid windowtext; border-image:initial;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-9' entry in the estimate and margin of error columns indicates that data for this geographic area cannot be displayed because the number of sample cases is too small.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-8</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-8' means that the estimate is not applicable or not available.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-6</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-6' entry in the estimate column indicates that either no sample observations or too few sample observations were available to compute an\u00a0 \u00a0estimate, or a ratio of medians cannot be calculated because one or both of the median estimates falls in the lowest interval or upper interval of an open-ended distribution.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-5</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-5' entry in the margin of error column indicates that the estimate is controlled. A statistical test for sampling variability is not appropriate.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-3</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-3' entry in the margin of error column indicates that the median falls in the lowest interval or upper interval of an open-ended distribution. A statistical test is not appropriate.</span></p></td></tr><tr style='border-bottom:none;'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-2</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-2' entry in the margin of error column indicates that either no sample observations or too few sample observations were available to compute a standard error and thus the margin of error. A statistical test is not appropriate.</span></p></td></tr></tbody></table></div></div>",
-            "modified": "2024-10-19T12:47:31.349444",
-            "accessLevel": "public",
-            "identifier": "585ccec8-1ec5-4023-990a-908e0a7819e2",
-            "issued": "2020-12-14T23:42:34.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -14046,63 +14011,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "ACS-ED 2013-2017 Children-Enrolled Public: Housing Characteristics (CDP04)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The American Community Survey Education Tabulation (ACS-ED) is a custom tabulation of the ACS produced for the National Center of Education Statistics (NCES) by the U.S. Census Bureau. The ACS-ED provides a rich collection of social, economic, demographic, and housing characteristics for school systems, school-age children, and the parents of school-age children. In addition to focusing on school-age children, the ACS-ED provides enrollment iterations for children enrolled in public school. The data profiles include percentages (along with associated margins of error) that allow for comparison of school district-level conditions across the U.S. For more information about the NCES ACS-ED collection, visit the NCES Education Demographic and Geographic Estimates (EDGE) program at:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Demographic/ACS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Demographic/ACS</a></div><div><br /></div><div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Annotation values are negative value representations of estimates and have values when non-integer information needs to be represented. See the table below for a list of common Estimate/Margin of Error (E/M) values and their corresponding Annotation (EA/MA) values.</div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. \nData users are advised to review NCES program documentation and feature \nclass metadata to understand the limitations and appropriate use of \nthese data.<br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><table border='0' cellpadding='0' cellspacing='0' style='margin-bottom:1.5rem; width:467.5pt; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial; border-collapse:collapse; border-spacing:0px; border:1px solid rgb(204, 204, 204); font-size:0.875rem;' width='623'><tbody><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-9</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:1pt solid windowtext; border-bottom:1pt solid windowtext; border-image:initial;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-9' entry in the estimate and margin of error columns indicates that data for this geographic area cannot be displayed because the number of sample cases is too small.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-8</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-8' means that the estimate is not applicable or not available.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-6</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-6' entry in the estimate column indicates that either no sample observations or too few sample observations were available to compute an\u00a0 \u00a0estimate, or a ratio of medians cannot be calculated because one or both of the median estimates falls in the lowest interval or upper interval of an open-ended distribution.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-5</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-5' entry in the margin of error column indicates that the estimate is controlled. A statistical test for sampling variability is not appropriate.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-3</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-3' entry in the margin of error column indicates that the median falls in the lowest interval or upper interval of an open-ended distribution. A statistical test is not appropriate.</span></p></td></tr><tr style='border-bottom:none;'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-2</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-2' entry in the margin of error column indicates that either no sample observations or too few sample observations were available to compute a standard error and thus the margin of error. A statistical test is not appropriate.</span></p></td></tr></tbody></table></div></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/a8c1a92f266f43508d1cd36568c199e9/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/a8c1a92f266f43508d1cd36568c199e9/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::acs-ed-2013-2017-total-population-demographic-characteristics-dp05",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::acs-ed-2013-2017-total-population-demographic-characteristics-dp05"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Social_Economic/ACS_OpenData_1317/MapServer/11",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Social_Economic/ACS_OpenData_1317/MapServer/11"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a8c1a92f266f43508d1cd36568c199e9/csv?layers=11",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a8c1a92f266f43508d1cd36568c199e9/csv?layers=11"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a8c1a92f266f43508d1cd36568c199e9/geojson?layers=11",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a8c1a92f266f43508d1cd36568c199e9/geojson?layers=11"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a8c1a92f266f43508d1cd36568c199e9/shapefile?layers=11",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a8c1a92f266f43508d1cd36568c199e9/shapefile?layers=11"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a8c1a92f266f43508d1cd36568c199e9/kml?layers=11",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a8c1a92f266f43508d1cd36568c199e9/kml?layers=11"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "585ccec8-1ec5-4023-990a-908e0a7819e2",
+            "issued": "2020-12-14T23:42:34.000Z",
             "keyword": [
                 "acs",
                 "acs-ed",
@@ -14117,25 +14096,11 @@
                 "u-s-census-bureau",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:31.349444",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ACS-ED 2013-2017 Total Population: Economic Characteristics (DP03)",
-            "description": "<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The American Community Survey Education Tabulation (ACS-ED) is a custom tabulation of the ACS produced for the National Center of Education Statistics (NCES) by the U.S. Census Bureau. The ACS-ED provides a rich collection of social, economic, demographic, and housing characteristics for school systems, school-age children, and the parents of school-age children. In addition to focusing on school-age children, the ACS-ED provides enrollment iterations for children enrolled in public school. The data profiles include percentages (along with associated margins of error) that allow for comparison of school district-level conditions across the U.S. For more information about the NCES ACS-ED collection, visit the NCES Education Demographic and Geographic Estimates (EDGE) program at:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Demographic/ACS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Demographic/ACS</a><div><br /></div><div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Annotation values are negative value representations of estimates and have values when non-integer information needs to be represented. See the table below for a list of common Estimate/Margin of Error (E/M) values and their corresponding Annotation (EA/MA) values.</div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><table border='0' cellpadding='0' cellspacing='0' style='margin-bottom:1.5rem; width:467.5pt; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial; border-collapse:collapse; border-spacing:0px; border:1px solid rgb(204, 204, 204); font-size:0.875rem;' width='623'><tbody><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-9</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:1pt solid windowtext; border-bottom:1pt solid windowtext; border-image:initial;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-9' entry in the estimate and margin of error columns indicates that data for this geographic area cannot be displayed because the number of sample cases is too small.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-8</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-8' means that the estimate is not applicable or not available.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-6</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-6' entry in the estimate column indicates that either no sample observations or too few sample observations were available to compute an\u00a0 \u00a0estimate, or a ratio of medians cannot be calculated because one or both of the median estimates falls in the lowest interval or upper interval of an open-ended distribution.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-5</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-5' entry in the margin of error column indicates that the estimate is controlled. A statistical test for sampling variability is not appropriate.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-3</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-3' entry in the margin of error column indicates that the median falls in the lowest interval or upper interval of an open-ended distribution. A statistical test is not appropriate.</span></p></td></tr><tr style='border-bottom:none;'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-2</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-2' entry in the margin of error column indicates that either no sample observations or too few sample observations were available to compute a standard error and thus the margin of error. A statistical test is not appropriate.</span></p></td></tr></tbody></table></div></div>",
-            "modified": "2024-10-19T12:47:30.441968",
-            "accessLevel": "public",
-            "identifier": "e200c728-9d16-4ec9-b94f-8a22d9dd7f7f",
-            "issued": "2020-12-14T23:38:09.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -14156,63 +14121,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "ACS-ED 2013-2017 Total Population: Demographic Characteristics (DP05)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The American Community Survey Education Tabulation (ACS-ED) is a custom tabulation of the ACS produced for the National Center of Education Statistics (NCES) by the U.S. Census Bureau. The ACS-ED provides a rich collection of social, economic, demographic, and housing characteristics for school systems, school-age children, and the parents of school-age children. In addition to focusing on school-age children, the ACS-ED provides enrollment iterations for children enrolled in public school. The data profiles include percentages (along with associated margins of error) that allow for comparison of school district-level conditions across the U.S. For more information about the NCES ACS-ED collection, visit the NCES Education Demographic and Geographic Estimates (EDGE) program at:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Demographic/ACS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Demographic/ACS</a><div><br /></div><div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Annotation values are negative value representations of estimates and have values when non-integer information needs to be represented. See the table below for a list of common Estimate/Margin of Error (E/M) values and their corresponding Annotation (EA/MA) values.</div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><table border='0' cellpadding='0' cellspacing='0' style='margin-bottom:1.5rem; width:467.5pt; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial; border-collapse:collapse; border-spacing:0px; border:1px solid rgb(204, 204, 204); font-size:0.875rem;' width='623'><tbody><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-9</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:1pt solid windowtext; border-bottom:1pt solid windowtext; border-image:initial;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-9' entry in the estimate and margin of error columns indicates that data for this geographic area cannot be displayed because the number of sample cases is too small.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-8</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-8' means that the estimate is not applicable or not available.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-6</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-6' entry in the estimate column indicates that either no sample observations or too few sample observations were available to compute an\u00a0 \u00a0estimate, or a ratio of medians cannot be calculated because one or both of the median estimates falls in the lowest interval or upper interval of an open-ended distribution.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-5</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-5' entry in the margin of error column indicates that the estimate is controlled. A statistical test for sampling variability is not appropriate.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-3</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-3' entry in the margin of error column indicates that the median falls in the lowest interval or upper interval of an open-ended distribution. A statistical test is not appropriate.</span></p></td></tr><tr style='border-bottom:none;'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-2</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-2' entry in the margin of error column indicates that either no sample observations or too few sample observations were available to compute a standard error and thus the margin of error. A statistical test is not appropriate.</span></p></td></tr></tbody></table></div></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/a84043b72e8c43aab8fa9d9a1f400d5c/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/a84043b72e8c43aab8fa9d9a1f400d5c/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::acs-ed-2013-2017-total-population-economic-characteristics-dp03",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::acs-ed-2013-2017-total-population-economic-characteristics-dp03"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Social_Economic/ACS_OpenData_1317/MapServer/9",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Social_Economic/ACS_OpenData_1317/MapServer/9"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a84043b72e8c43aab8fa9d9a1f400d5c/csv?layers=9",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a84043b72e8c43aab8fa9d9a1f400d5c/csv?layers=9"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a84043b72e8c43aab8fa9d9a1f400d5c/geojson?layers=9",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a84043b72e8c43aab8fa9d9a1f400d5c/geojson?layers=9"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a84043b72e8c43aab8fa9d9a1f400d5c/shapefile?layers=9",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a84043b72e8c43aab8fa9d9a1f400d5c/shapefile?layers=9"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a84043b72e8c43aab8fa9d9a1f400d5c/kml?layers=9",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a84043b72e8c43aab8fa9d9a1f400d5c/kml?layers=9"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "e200c728-9d16-4ec9-b94f-8a22d9dd7f7f",
+            "issued": "2020-12-14T23:38:09.000Z",
             "keyword": [
                 "acs",
                 "acs-ed",
@@ -14227,25 +14206,11 @@
                 "u-s-census-bureau",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:30.441968",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ACS-ED 2014-2018 Children-Enrolled Public: Economic Characteristics (CDP03)",
-            "description": "<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The American Community Survey Education Tabulation (ACS-ED) is a custom tabulation of the ACS produced for the National Center of Education Statistics (NCES) by the U.S. Census Bureau. The ACS-ED provides a rich collection of social, economic, demographic, and housing characteristics for school systems, school-age children, and the parents of school-age children. In addition to focusing on school-age children, the ACS-ED provides enrollment iterations for children enrolled in public school. The data profiles include percentages (along with associated margins of error) that allow for comparison of school district-level conditions across the U.S. For more information about the NCES ACS-ED collection, visit the NCES Education Demographic and Geographic Estimates (EDGE) program at:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Demographic/ACS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Demographic/ACS</a><div><br /></div><div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Annotation values are negative value representations of estimates and have values when non-integer information needs to be represented. See the table below for a list of common Estimate/Margin of Error (E/M) values and their corresponding Annotation (EA/MA) values.</div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><table border='0' cellpadding='0' cellspacing='0' style='width:467.5pt; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial; border-collapse:collapse;' width='623'>\n <tbody><tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-9</span></p>\n  </td>\n  <td style='width:418.25pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-9' entry in the estimate and margin of\n  error columns indicates that data for this geographic area cannot be\n  displayed because the number of sample cases is too small.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-8</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-8' means that the estimate is not\n  applicable or not available.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-6</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-6' entry in the estimate column indicates\n  that either no sample observations or too few sample observations were\n  available to compute an\u00a0 \u00a0estimate, or a ratio of medians cannot be\n  calculated because one or both of the median estimates falls in the lowest\n  interval or upper interval of an open-ended distribution.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-5</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-5' entry in the margin of error column\n  indicates that the estimate is controlled. A statistical test for sampling\n  variability is not appropriate.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-3</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-3' entry in the margin of error column indicates\n  that the median falls in the lowest interval or upper interval of an\n  open-ended distribution. A statistical test is not appropriate.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-2</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-2' entry in the margin of error column\n  indicates that either no sample observations or too few sample observations\n  were available to compute a standard error and thus the margin of error. A\n  statistical test is not appropriate.</span></p>\n  </td>\n </tr>\n</tbody></table><br /></div></div>",
-            "modified": "2024-10-19T12:47:29.634164",
-            "accessLevel": "public",
-            "identifier": "f3374ede-f347-4db4-9058-8c3128d55865",
-            "issued": "2020-09-08T23:06:46.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -14266,63 +14231,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "ACS-ED 2013-2017 Total Population: Economic Characteristics (DP03)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The American Community Survey Education Tabulation (ACS-ED) is a custom tabulation of the ACS produced for the National Center of Education Statistics (NCES) by the U.S. Census Bureau. The ACS-ED provides a rich collection of social, economic, demographic, and housing characteristics for school systems, school-age children, and the parents of school-age children. In addition to focusing on school-age children, the ACS-ED provides enrollment iterations for children enrolled in public school. The data profiles include percentages (along with associated margins of error) that allow for comparison of school district-level conditions across the U.S. For more information about the NCES ACS-ED collection, visit the NCES Education Demographic and Geographic Estimates (EDGE) program at:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Demographic/ACS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Demographic/ACS</a><div><br /></div><div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Annotation values are negative value representations of estimates and have values when non-integer information needs to be represented. See the table below for a list of common Estimate/Margin of Error (E/M) values and their corresponding Annotation (EA/MA) values.</div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><table border='0' cellpadding='0' cellspacing='0' style='width:467.5pt; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial; border-collapse:collapse;' width='623'>\n <tbody><tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-9</span></p>\n  </td>\n  <td style='width:418.25pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-9' entry in the estimate and margin of\n  error columns indicates that data for this geographic area cannot be\n  displayed because the number of sample cases is too small.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-8</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-8' means that the estimate is not\n  applicable or not available.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-6</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-6' entry in the estimate column indicates\n  that either no sample observations or too few sample observations were\n  available to compute an\u00a0 \u00a0estimate, or a ratio of medians cannot be\n  calculated because one or both of the median estimates falls in the lowest\n  interval or upper interval of an open-ended distribution.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-5</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-5' entry in the margin of error column\n  indicates that the estimate is controlled. A statistical test for sampling\n  variability is not appropriate.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-3</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-3' entry in the margin of error column indicates\n  that the median falls in the lowest interval or upper interval of an\n  open-ended distribution. A statistical test is not appropriate.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-2</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-2' entry in the margin of error column\n  indicates that either no sample observations or too few sample observations\n  were available to compute a standard error and thus the margin of error. A\n  statistical test is not appropriate.</span></p>\n  </td>\n </tr>\n</tbody></table><br /></div></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/ad0155bf000744cd8821467e4e0bbea7/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/ad0155bf000744cd8821467e4e0bbea7/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::acs-ed-2014-2018-children-enrolled-public-economic-characteristics-cdp03",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::acs-ed-2014-2018-children-enrolled-public-economic-characteristics-cdp03"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Social_Economic/ACS_OpenData_1418/MapServer/3",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Social_Economic/ACS_OpenData_1418/MapServer/3"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ad0155bf000744cd8821467e4e0bbea7/csv?layers=3",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ad0155bf000744cd8821467e4e0bbea7/csv?layers=3"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ad0155bf000744cd8821467e4e0bbea7/geojson?layers=3",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ad0155bf000744cd8821467e4e0bbea7/geojson?layers=3"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ad0155bf000744cd8821467e4e0bbea7/shapefile?layers=3",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ad0155bf000744cd8821467e4e0bbea7/shapefile?layers=3"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ad0155bf000744cd8821467e4e0bbea7/kml?layers=3",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ad0155bf000744cd8821467e4e0bbea7/kml?layers=3"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "f3374ede-f347-4db4-9058-8c3128d55865",
+            "issued": "2020-09-08T23:06:46.000Z",
             "keyword": [
                 "acs",
                 "american-community-survey",
@@ -14336,25 +14315,11 @@
                 "u-s-census-bureau",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:29.634164",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ACS-ED 2014-2018 Children-Enrolled Public: Demographic Characteristics (CDP05)",
-            "description": "<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The American Community Survey Education Tabulation (ACS-ED) is a custom tabulation of the ACS produced for the National Center of Education Statistics (NCES) by the U.S. Census Bureau. The ACS-ED provides a rich collection of social, economic, demographic, and housing characteristics for school systems, school-age children, and the parents of school-age children. In addition to focusing on school-age children, the ACS-ED provides enrollment iterations for children enrolled in public school. The data profiles include percentages (along with associated margins of error) that allow for comparison of school district-level conditions across the U.S. For more information about the NCES ACS-ED collection, visit the NCES Education Demographic and Geographic Estimates (EDGE) program at:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Demographic/ACS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Demographic/ACS</a><div><br /></div><div><div><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Annotation values are negative value representations of estimates and have values when non-integer information needs to be represented. See the table below for a list of common Estimate/Margin of Error (E/M) values and their corresponding Annotation (EA/MA) values.</span></div><div><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></span></div><div><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></span></div><div><br /></div><div><table border='0' cellpadding='0' cellspacing='0' style='width:467.5pt; background:white; border-collapse:collapse;' width='623'>\n <tbody><tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-9</span></p>\n  </td>\n  <td style='width:418.25pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>An '-9' entry in the estimate and margin of\n  error columns indicates that data for this geographic area cannot be\n  displayed because the number of sample cases is too small.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-8</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>An '-8' means that the estimate is not\n  applicable or not available.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-6</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-6' entry in the estimate column indicates\n  that either no sample observations or too few sample observations were\n  available to compute an\u00a0 \u00a0estimate, or a ratio of medians cannot be\n  calculated because one or both of the median estimates falls in the lowest\n  interval or upper interval of an open-ended distribution.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-5</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-5' entry in the margin of error column\n  indicates that the estimate is controlled. A statistical test for sampling\n  variability is not appropriate.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-3</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-3' entry in the margin of error column indicates\n  that the median falls in the lowest interval or upper interval of an\n  open-ended distribution. A statistical test is not appropriate.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-2</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-2' entry in the margin of error column\n  indicates that either no sample observations or too few sample observations\n  were available to compute a standard error and thus the margin of error. A\n  statistical test is not appropriate.</span></p>\n  </td>\n </tr>\n</tbody></table></div></div>",
-            "modified": "2024-10-19T12:47:28.838243",
-            "accessLevel": "public",
-            "identifier": "308f66b3-ffd6-4b70-8a22-9e6a98af6c8e",
-            "issued": "2020-09-08T20:12:21.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -14375,63 +14340,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "ACS-ED 2014-2018 Children-Enrolled Public: Economic Characteristics (CDP03)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The American Community Survey Education Tabulation (ACS-ED) is a custom tabulation of the ACS produced for the National Center of Education Statistics (NCES) by the U.S. Census Bureau. The ACS-ED provides a rich collection of social, economic, demographic, and housing characteristics for school systems, school-age children, and the parents of school-age children. In addition to focusing on school-age children, the ACS-ED provides enrollment iterations for children enrolled in public school. The data profiles include percentages (along with associated margins of error) that allow for comparison of school district-level conditions across the U.S. For more information about the NCES ACS-ED collection, visit the NCES Education Demographic and Geographic Estimates (EDGE) program at:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Demographic/ACS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Demographic/ACS</a><div><br /></div><div><div><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Annotation values are negative value representations of estimates and have values when non-integer information needs to be represented. See the table below for a list of common Estimate/Margin of Error (E/M) values and their corresponding Annotation (EA/MA) values.</span></div><div><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></span></div><div><span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></span></div><div><br /></div><div><table border='0' cellpadding='0' cellspacing='0' style='width:467.5pt; background:white; border-collapse:collapse;' width='623'>\n <tbody><tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-9</span></p>\n  </td>\n  <td style='width:418.25pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>An '-9' entry in the estimate and margin of\n  error columns indicates that data for this geographic area cannot be\n  displayed because the number of sample cases is too small.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-8</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>An '-8' means that the estimate is not\n  applicable or not available.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-6</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-6' entry in the estimate column indicates\n  that either no sample observations or too few sample observations were\n  available to compute an\u00a0 \u00a0estimate, or a ratio of medians cannot be\n  calculated because one or both of the median estimates falls in the lowest\n  interval or upper interval of an open-ended distribution.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-5</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-5' entry in the margin of error column\n  indicates that the estimate is controlled. A statistical test for sampling\n  variability is not appropriate.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-3</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-3' entry in the margin of error column indicates\n  that the median falls in the lowest interval or upper interval of an\n  open-ended distribution. A statistical test is not appropriate.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-2</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-2' entry in the margin of error column\n  indicates that either no sample observations or too few sample observations\n  were available to compute a standard error and thus the margin of error. A\n  statistical test is not appropriate.</span></p>\n  </td>\n </tr>\n</tbody></table></div></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/a1dd89e8fd204b6ba5fc055c9774dc45/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/a1dd89e8fd204b6ba5fc055c9774dc45/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::acs-ed-2014-2018-children-enrolled-public-demographic-characteristics-cdp05",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::acs-ed-2014-2018-children-enrolled-public-demographic-characteristics-cdp05"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Social_Economic/ACS_OpenData_1418/MapServer/7",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Social_Economic/ACS_OpenData_1418/MapServer/7"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a1dd89e8fd204b6ba5fc055c9774dc45/csv?layers=7",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a1dd89e8fd204b6ba5fc055c9774dc45/csv?layers=7"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a1dd89e8fd204b6ba5fc055c9774dc45/geojson?layers=7",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a1dd89e8fd204b6ba5fc055c9774dc45/geojson?layers=7"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a1dd89e8fd204b6ba5fc055c9774dc45/shapefile?layers=7",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a1dd89e8fd204b6ba5fc055c9774dc45/shapefile?layers=7"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a1dd89e8fd204b6ba5fc055c9774dc45/kml?layers=7",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a1dd89e8fd204b6ba5fc055c9774dc45/kml?layers=7"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "308f66b3-ffd6-4b70-8a22-9e6a98af6c8e",
+            "issued": "2020-09-08T20:12:21.000Z",
             "keyword": [
                 "acs",
                 "acs-ed",
@@ -14447,25 +14426,11 @@
                 "u-s-census-bureau",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:28.838243",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ACS-ED 2014-2018 Total Population: Housing Characteristics (DP04)",
-            "description": "<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The American Community Survey Education Tabulation (ACS-ED) is a custom tabulation of the ACS produced for the National Center of Education Statistics (NCES) by the U.S. Census Bureau. The ACS-ED provides a rich collection of social, economic, demographic, and housing characteristics for school systems, school-age children, and the parents of school-age children. In addition to focusing on school-age children, the ACS-ED provides enrollment iterations for children enrolled in public school. The data profiles include percentages (along with associated margins of error) that allow for comparison of school district-level conditions across the U.S. For more information about the NCES ACS-ED collection, visit the NCES Education Demographic and Geographic Estimates (EDGE) program at:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Demographic/ACS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Demographic/ACS</a><div><br /></div><div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Annotation values are negative value representations of estimates and have values when non-integer information needs to be represented. See the table below for a list of common Estimate/Margin of Error (E/M) values and their corresponding Annotation (EA/MA) values.</div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><table border='0' cellpadding='0' cellspacing='0' style='width:467.5pt; background:white; border-collapse:collapse;' width='623'>\n <tbody><tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Arial&quot;,sans-serif; color:#4C4C4C; background:white;'>-9</span></p>\n  </td>\n  <td style='width:418.25pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Arial&quot;,sans-serif; color:#4C4C4C; background:white;'>An '-9' entry in the estimate and margin of\n  error columns indicates that data for this geographic area cannot be\n  displayed because the number of sample cases is too small.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Arial&quot;,sans-serif; color:#4C4C4C; background:white;'>-8</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Arial&quot;,sans-serif; color:#4C4C4C; background:white;'>An '-8' means that the estimate is not\n  applicable or not available.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Arial&quot;,sans-serif; color:#4C4C4C; background:white;'>-6</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Arial&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-6' entry in the estimate column indicates\n  that either no sample observations or too few sample observations were\n  available to compute an\u00a0 \u00a0estimate, or a ratio of medians cannot be\n  calculated because one or both of the median estimates falls in the lowest\n  interval or upper interval of an open-ended distribution.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Arial&quot;,sans-serif; color:#4C4C4C; background:white;'>-5</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Arial&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-5' entry in the margin of error column\n  indicates that the estimate is controlled. A statistical test for sampling\n  variability is not appropriate.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Arial&quot;,sans-serif; color:#4C4C4C; background:white;'>-3</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Arial&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-3' entry in the margin of error column indicates\n  that the median falls in the lowest interval or upper interval of an\n  open-ended distribution. A statistical test is not appropriate.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Arial&quot;,sans-serif; color:#4C4C4C; background:white;'>-2</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Arial&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-2' entry in the margin of error column\n  indicates that either no sample observations or too few sample observations\n  were available to compute a standard error and thus the margin of error. A\n  statistical test is not appropriate.</span></p>\n  </td>\n </tr>\n</tbody></table><br /></div></div>",
-            "modified": "2024-10-19T12:47:28.061889",
-            "accessLevel": "public",
-            "identifier": "fdddc7b2-6a94-4642-9daa-bf2e987595d1",
-            "issued": "2020-09-08T20:40:04.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -14486,63 +14451,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "ACS-ED 2014-2018 Children-Enrolled Public: Demographic Characteristics (CDP05)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The American Community Survey Education Tabulation (ACS-ED) is a custom tabulation of the ACS produced for the National Center of Education Statistics (NCES) by the U.S. Census Bureau. The ACS-ED provides a rich collection of social, economic, demographic, and housing characteristics for school systems, school-age children, and the parents of school-age children. In addition to focusing on school-age children, the ACS-ED provides enrollment iterations for children enrolled in public school. The data profiles include percentages (along with associated margins of error) that allow for comparison of school district-level conditions across the U.S. For more information about the NCES ACS-ED collection, visit the NCES Education Demographic and Geographic Estimates (EDGE) program at:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Demographic/ACS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Demographic/ACS</a><div><br /></div><div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Annotation values are negative value representations of estimates and have values when non-integer information needs to be represented. See the table below for a list of common Estimate/Margin of Error (E/M) values and their corresponding Annotation (EA/MA) values.</div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><table border='0' cellpadding='0' cellspacing='0' style='width:467.5pt; background:white; border-collapse:collapse;' width='623'>\n <tbody><tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Arial&quot;,sans-serif; color:#4C4C4C; background:white;'>-9</span></p>\n  </td>\n  <td style='width:418.25pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Arial&quot;,sans-serif; color:#4C4C4C; background:white;'>An '-9' entry in the estimate and margin of\n  error columns indicates that data for this geographic area cannot be\n  displayed because the number of sample cases is too small.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Arial&quot;,sans-serif; color:#4C4C4C; background:white;'>-8</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Arial&quot;,sans-serif; color:#4C4C4C; background:white;'>An '-8' means that the estimate is not\n  applicable or not available.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Arial&quot;,sans-serif; color:#4C4C4C; background:white;'>-6</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Arial&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-6' entry in the estimate column indicates\n  that either no sample observations or too few sample observations were\n  available to compute an\u00a0 \u00a0estimate, or a ratio of medians cannot be\n  calculated because one or both of the median estimates falls in the lowest\n  interval or upper interval of an open-ended distribution.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Arial&quot;,sans-serif; color:#4C4C4C; background:white;'>-5</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Arial&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-5' entry in the margin of error column\n  indicates that the estimate is controlled. A statistical test for sampling\n  variability is not appropriate.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Arial&quot;,sans-serif; color:#4C4C4C; background:white;'>-3</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Arial&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-3' entry in the margin of error column indicates\n  that the median falls in the lowest interval or upper interval of an\n  open-ended distribution. A statistical test is not appropriate.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Arial&quot;,sans-serif; color:#4C4C4C; background:white;'>-2</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Arial&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-2' entry in the margin of error column\n  indicates that either no sample observations or too few sample observations\n  were available to compute a standard error and thus the margin of error. A\n  statistical test is not appropriate.</span></p>\n  </td>\n </tr>\n</tbody></table><br /></div></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/2fea121976014abfad30ec3dd1021fc4/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/2fea121976014abfad30ec3dd1021fc4/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::acs-ed-2014-2018-total-population-housing-characteristics-dp04",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::acs-ed-2014-2018-total-population-housing-characteristics-dp04"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Social_Economic/ACS_OpenData_1418/MapServer/10",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Social_Economic/ACS_OpenData_1418/MapServer/10"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/2fea121976014abfad30ec3dd1021fc4/csv?layers=10",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/2fea121976014abfad30ec3dd1021fc4/csv?layers=10"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/2fea121976014abfad30ec3dd1021fc4/geojson?layers=10",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/2fea121976014abfad30ec3dd1021fc4/geojson?layers=10"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/2fea121976014abfad30ec3dd1021fc4/shapefile?layers=10",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/2fea121976014abfad30ec3dd1021fc4/shapefile?layers=10"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/2fea121976014abfad30ec3dd1021fc4/kml?layers=10",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/2fea121976014abfad30ec3dd1021fc4/kml?layers=10"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "fdddc7b2-6a94-4642-9daa-bf2e987595d1",
+            "issued": "2020-09-08T20:40:04.000Z",
             "keyword": [
                 "acs",
                 "acs-ed",
@@ -14557,25 +14536,11 @@
                 "u-s-census-bureau",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:28.061889",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ACS-ED 2014-2018 Total Population: Economic Characteristics (DP03)",
-            "description": "<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The American Community Survey Education Tabulation (ACS-ED) is a custom tabulation of the ACS produced for the National Center of Education Statistics (NCES) by the U.S. Census Bureau. The ACS-ED provides a rich collection of social, economic, demographic, and housing characteristics for school systems, school-age children, and the parents of school-age children. In addition to focusing on school-age children, the ACS-ED provides enrollment iterations for children enrolled in public school. The data profiles include percentages (along with associated margins of error) that allow for comparison of school district-level conditions across the U.S. For more information about the NCES ACS-ED collection, visit the NCES Education Demographic and Geographic Estimates (EDGE) program at:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Demographic/ACS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Demographic/ACS</a><div><br /></div><div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Annotation values are negative value representations of estimates and have values when non-integer information needs to be represented. See the table below for a list of common Estimate/Margin of Error (E/M) values and their corresponding Annotation (EA/MA) values.</div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><table border='0' cellpadding='0' cellspacing='0' style='width:467.5pt; background:white; border-collapse:collapse;' width='623'>\n <tbody><tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-9</span></p>\n  </td>\n  <td style='width:418.25pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>An '-9' entry in the estimate and margin of\n  error columns indicates that data for this geographic area cannot be\n  displayed because the number of sample cases is too small.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-8</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>An '-8' means that the estimate is not\n  applicable or not available.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-6</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-6' entry in the estimate column indicates\n  that either no sample observations or too few sample observations were\n  available to compute an\u00a0 \u00a0estimate, or a ratio of medians cannot be\n  calculated because one or both of the median estimates falls in the lowest\n  interval or upper interval of an open-ended distribution.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-5</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-5' entry in the margin of error column\n  indicates that the estimate is controlled. A statistical test for sampling\n  variability is not appropriate.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-3</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-3' entry in the margin of error column indicates\n  that the median falls in the lowest interval or upper interval of an\n  open-ended distribution. A statistical test is not appropriate.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-2</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-2' entry in the margin of error column\n  indicates that either no sample observations or too few sample observations\n  were available to compute a standard error and thus the margin of error. A\n  statistical test is not appropriate.</span></p>\n  </td>\n </tr>\n</tbody></table><br /></div>",
-            "modified": "2024-10-19T12:47:27.130335",
-            "accessLevel": "public",
-            "identifier": "8d56228f-f01e-4a29-b50b-0bb3294a64df",
-            "issued": "2020-09-08T20:45:43.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -14596,63 +14561,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "ACS-ED 2014-2018 Total Population: Housing Characteristics (DP04)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The American Community Survey Education Tabulation (ACS-ED) is a custom tabulation of the ACS produced for the National Center of Education Statistics (NCES) by the U.S. Census Bureau. The ACS-ED provides a rich collection of social, economic, demographic, and housing characteristics for school systems, school-age children, and the parents of school-age children. In addition to focusing on school-age children, the ACS-ED provides enrollment iterations for children enrolled in public school. The data profiles include percentages (along with associated margins of error) that allow for comparison of school district-level conditions across the U.S. For more information about the NCES ACS-ED collection, visit the NCES Education Demographic and Geographic Estimates (EDGE) program at:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Demographic/ACS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Demographic/ACS</a><div><br /></div><div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Annotation values are negative value representations of estimates and have values when non-integer information needs to be represented. See the table below for a list of common Estimate/Margin of Error (E/M) values and their corresponding Annotation (EA/MA) values.</div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><table border='0' cellpadding='0' cellspacing='0' style='width:467.5pt; background:white; border-collapse:collapse;' width='623'>\n <tbody><tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-9</span></p>\n  </td>\n  <td style='width:418.25pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>An '-9' entry in the estimate and margin of\n  error columns indicates that data for this geographic area cannot be\n  displayed because the number of sample cases is too small.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-8</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>An '-8' means that the estimate is not\n  applicable or not available.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-6</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-6' entry in the estimate column indicates\n  that either no sample observations or too few sample observations were\n  available to compute an\u00a0 \u00a0estimate, or a ratio of medians cannot be\n  calculated because one or both of the median estimates falls in the lowest\n  interval or upper interval of an open-ended distribution.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-5</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-5' entry in the margin of error column\n  indicates that the estimate is controlled. A statistical test for sampling\n  variability is not appropriate.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-3</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-3' entry in the margin of error column indicates\n  that the median falls in the lowest interval or upper interval of an\n  open-ended distribution. A statistical test is not appropriate.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-2</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-2' entry in the margin of error column\n  indicates that either no sample observations or too few sample observations\n  were available to compute a standard error and thus the margin of error. A\n  statistical test is not appropriate.</span></p>\n  </td>\n </tr>\n</tbody></table><br /></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/de3da5068f334fbca9c876786062b6ef/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/de3da5068f334fbca9c876786062b6ef/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::acs-ed-2014-2018-total-population-economic-characteristics-dp03",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::acs-ed-2014-2018-total-population-economic-characteristics-dp03"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Social_Economic/ACS_OpenData_1418/MapServer/9",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Social_Economic/ACS_OpenData_1418/MapServer/9"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/de3da5068f334fbca9c876786062b6ef/csv?layers=9",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/de3da5068f334fbca9c876786062b6ef/csv?layers=9"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/de3da5068f334fbca9c876786062b6ef/geojson?layers=9",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/de3da5068f334fbca9c876786062b6ef/geojson?layers=9"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/de3da5068f334fbca9c876786062b6ef/shapefile?layers=9",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/de3da5068f334fbca9c876786062b6ef/shapefile?layers=9"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/de3da5068f334fbca9c876786062b6ef/kml?layers=9",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/de3da5068f334fbca9c876786062b6ef/kml?layers=9"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "8d56228f-f01e-4a29-b50b-0bb3294a64df",
+            "issued": "2020-09-08T20:45:43.000Z",
             "keyword": [
                 "acs",
                 "acs-ed",
@@ -14667,25 +14646,11 @@
                 "u-s-census-bureau",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:27.130335",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ACS-ED 2014-2018 Total Population: Demographic Characteristics (DP05)",
-            "description": "<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The American Community Survey Education Tabulation (ACS-ED) is a custom tabulation of the ACS produced for the National Center of Education Statistics (NCES) by the U.S. Census Bureau. The ACS-ED provides a rich collection of social, economic, demographic, and housing characteristics for school systems, school-age children, and the parents of school-age children. In addition to focusing on school-age children, the ACS-ED provides enrollment iterations for children enrolled in public school. The data profiles include percentages (along with associated margins of error) that allow for comparison of school district-level conditions across the U.S. For more information about the NCES ACS-ED collection, visit the NCES Education Demographic and Geographic Estimates (EDGE) program at:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Demographic/ACS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Demographic/ACS</a><div><br /></div><div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Annotation values are negative value representations of estimates and have values when non-integer information needs to be represented. See the table below for a list of common Estimate/Margin of Error (E/M) values and their corresponding Annotation (EA/MA) values.</div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><table border='0' cellpadding='0' cellspacing='0' style='width:467.5pt; background:white; border-collapse:collapse;' width='623'>\n <tbody><tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-9</span></p>\n  </td>\n  <td style='width:418.25pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>An '-9' entry in the estimate and margin of\n  error columns indicates that data for this geographic area cannot be\n  displayed because the number of sample cases is too small.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-8</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>An '-8' means that the estimate is not\n  applicable or not available.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-6</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-6' entry in the estimate column indicates\n  that either no sample observations or too few sample observations were\n  available to compute an\u00a0 \u00a0estimate, or a ratio of medians cannot be\n  calculated because one or both of the median estimates falls in the lowest\n  interval or upper interval of an open-ended distribution.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-5</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-5' entry in the margin of error column\n  indicates that the estimate is controlled. A statistical test for sampling\n  variability is not appropriate.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-3</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-3' entry in the margin of error column indicates\n  that the median falls in the lowest interval or upper interval of an\n  open-ended distribution. A statistical test is not appropriate.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-2</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-2' entry in the margin of error column\n  indicates that either no sample observations or too few sample observations\n  were available to compute a standard error and thus the margin of error. A\n  statistical test is not appropriate.</span></p>\n  </td>\n </tr>\n</tbody></table><br /></div></div>",
-            "modified": "2024-10-19T12:47:26.219568",
-            "accessLevel": "public",
-            "identifier": "b9cf18de-de3b-4624-a9e5-f036bca2caf5",
-            "issued": "2020-09-08T20:56:48.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -14706,63 +14671,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "ACS-ED 2014-2018 Total Population: Economic Characteristics (DP03)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The American Community Survey Education Tabulation (ACS-ED) is a custom tabulation of the ACS produced for the National Center of Education Statistics (NCES) by the U.S. Census Bureau. The ACS-ED provides a rich collection of social, economic, demographic, and housing characteristics for school systems, school-age children, and the parents of school-age children. In addition to focusing on school-age children, the ACS-ED provides enrollment iterations for children enrolled in public school. The data profiles include percentages (along with associated margins of error) that allow for comparison of school district-level conditions across the U.S. For more information about the NCES ACS-ED collection, visit the NCES Education Demographic and Geographic Estimates (EDGE) program at:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Demographic/ACS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Demographic/ACS</a><div><br /></div><div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Annotation values are negative value representations of estimates and have values when non-integer information needs to be represented. See the table below for a list of common Estimate/Margin of Error (E/M) values and their corresponding Annotation (EA/MA) values.</div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><table border='0' cellpadding='0' cellspacing='0' style='width:467.5pt; background:white; border-collapse:collapse;' width='623'>\n <tbody><tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-9</span></p>\n  </td>\n  <td style='width:418.25pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>An '-9' entry in the estimate and margin of\n  error columns indicates that data for this geographic area cannot be\n  displayed because the number of sample cases is too small.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-8</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>An '-8' means that the estimate is not\n  applicable or not available.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-6</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-6' entry in the estimate column indicates\n  that either no sample observations or too few sample observations were\n  available to compute an\u00a0 \u00a0estimate, or a ratio of medians cannot be\n  calculated because one or both of the median estimates falls in the lowest\n  interval or upper interval of an open-ended distribution.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-5</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-5' entry in the margin of error column\n  indicates that the estimate is controlled. A statistical test for sampling\n  variability is not appropriate.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-3</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-3' entry in the margin of error column indicates\n  that the median falls in the lowest interval or upper interval of an\n  open-ended distribution. A statistical test is not appropriate.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-2</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-2' entry in the margin of error column\n  indicates that either no sample observations or too few sample observations\n  were available to compute a standard error and thus the margin of error. A\n  statistical test is not appropriate.</span></p>\n  </td>\n </tr>\n</tbody></table><br /></div></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/1f97febd50f64c178a72872f7d5dfcd8/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/1f97febd50f64c178a72872f7d5dfcd8/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::acs-ed-2014-2018-total-population-demographic-characteristics-dp05",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::acs-ed-2014-2018-total-population-demographic-characteristics-dp05"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Social_Economic/ACS_OpenData_1418/MapServer/11",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Social_Economic/ACS_OpenData_1418/MapServer/11"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/1f97febd50f64c178a72872f7d5dfcd8/csv?layers=11",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/1f97febd50f64c178a72872f7d5dfcd8/csv?layers=11"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/1f97febd50f64c178a72872f7d5dfcd8/geojson?layers=11",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/1f97febd50f64c178a72872f7d5dfcd8/geojson?layers=11"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/1f97febd50f64c178a72872f7d5dfcd8/shapefile?layers=11",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/1f97febd50f64c178a72872f7d5dfcd8/shapefile?layers=11"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/1f97febd50f64c178a72872f7d5dfcd8/kml?layers=11",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/1f97febd50f64c178a72872f7d5dfcd8/kml?layers=11"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "b9cf18de-de3b-4624-a9e5-f036bca2caf5",
+            "issued": "2020-09-08T20:56:48.000Z",
             "keyword": [
                 "acs",
                 "acs-ed",
@@ -14777,25 +14756,11 @@
                 "u-s-census-bureau",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:26.219568",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ACS-ED 2014-2018 Children-Enrolled Public: Housing Characteristics (CDP04)",
-            "description": "<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The American Community Survey Education Tabulation (ACS-ED) is a custom tabulation of the ACS produced for the National Center of Education Statistics (NCES) by the U.S. Census Bureau. The ACS-ED provides a rich collection of social, economic, demographic, and housing characteristics for school systems, school-age children, and the parents of school-age children. In addition to focusing on school-age children, the ACS-ED provides enrollment iterations for children enrolled in public school. The data profiles include percentages (along with associated margins of error) that allow for comparison of school district-level conditions across the U.S. For more information about the NCES ACS-ED collection, visit the NCES Education Demographic and Geographic Estimates (EDGE) program at:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Demographic/ACS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Demographic/ACS</a><div><br /></div><div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Annotation values are negative value representations of estimates and have values when non-integer information needs to be represented. See the table below for a list of common Estimate/Margin of Error (E/M) values and their corresponding Annotation (EA/MA) values.</div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><table border='0' cellpadding='0' cellspacing='0' style='width:467.5pt; background:white; border-collapse:collapse;' width='623'>\n <tbody><tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-9</span></p>\n  </td>\n  <td style='width:418.25pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>An '-9' entry in the estimate and margin of\n  error columns indicates that data for this geographic area cannot be\n  displayed because the number of sample cases is too small.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-8</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>An '-8' means that the estimate is not\n  applicable or not available.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-6</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-6' entry in the estimate column indicates\n  that either no sample observations or too few sample observations were\n  available to compute an\u00a0 \u00a0estimate, or a ratio of medians cannot be\n  calculated because one or both of the median estimates falls in the lowest\n  interval or upper interval of an open-ended distribution.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-5</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-5' entry in the margin of error column\n  indicates that the estimate is controlled. A statistical test for sampling\n  variability is not appropriate.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-3</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-3' entry in the margin of error column indicates\n  that the median falls in the lowest interval or upper interval of an\n  open-ended distribution. A statistical test is not appropriate.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-2</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-2' entry in the margin of error column\n  indicates that either no sample observations or too few sample observations\n  were available to compute a standard error and thus the margin of error. A\n  statistical test is not appropriate.</span></p>\n  </td>\n </tr>\n</tbody></table><br /></div>",
-            "modified": "2024-10-19T12:47:25.477081",
-            "accessLevel": "public",
-            "identifier": "0fdc623e-d36d-42b7-87bc-df0c7c9b5276",
-            "issued": "2020-09-08T23:13:01.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -14816,63 +14781,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "ACS-ED 2014-2018 Total Population: Demographic Characteristics (DP05)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The American Community Survey Education Tabulation (ACS-ED) is a custom tabulation of the ACS produced for the National Center of Education Statistics (NCES) by the U.S. Census Bureau. The ACS-ED provides a rich collection of social, economic, demographic, and housing characteristics for school systems, school-age children, and the parents of school-age children. In addition to focusing on school-age children, the ACS-ED provides enrollment iterations for children enrolled in public school. The data profiles include percentages (along with associated margins of error) that allow for comparison of school district-level conditions across the U.S. For more information about the NCES ACS-ED collection, visit the NCES Education Demographic and Geographic Estimates (EDGE) program at:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Demographic/ACS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Demographic/ACS</a><div><br /></div><div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Annotation values are negative value representations of estimates and have values when non-integer information needs to be represented. See the table below for a list of common Estimate/Margin of Error (E/M) values and their corresponding Annotation (EA/MA) values.</div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><table border='0' cellpadding='0' cellspacing='0' style='width:467.5pt; background:white; border-collapse:collapse;' width='623'>\n <tbody><tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-9</span></p>\n  </td>\n  <td style='width:418.25pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>An '-9' entry in the estimate and margin of\n  error columns indicates that data for this geographic area cannot be\n  displayed because the number of sample cases is too small.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-8</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>An '-8' means that the estimate is not\n  applicable or not available.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-6</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-6' entry in the estimate column indicates\n  that either no sample observations or too few sample observations were\n  available to compute an\u00a0 \u00a0estimate, or a ratio of medians cannot be\n  calculated because one or both of the median estimates falls in the lowest\n  interval or upper interval of an open-ended distribution.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-5</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-5' entry in the margin of error column\n  indicates that the estimate is controlled. A statistical test for sampling\n  variability is not appropriate.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-3</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-3' entry in the margin of error column indicates\n  that the median falls in the lowest interval or upper interval of an\n  open-ended distribution. A statistical test is not appropriate.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-2</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-2' entry in the margin of error column\n  indicates that either no sample observations or too few sample observations\n  were available to compute a standard error and thus the margin of error. A\n  statistical test is not appropriate.</span></p>\n  </td>\n </tr>\n</tbody></table><br /></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/0db311af55a349688de83884c09e7c1d/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/0db311af55a349688de83884c09e7c1d/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::acs-ed-2014-2018-children-enrolled-public-housing-characteristics-cdp04",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::acs-ed-2014-2018-children-enrolled-public-housing-characteristics-cdp04"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Social_Economic/ACS_OpenData_1418/MapServer/5",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Social_Economic/ACS_OpenData_1418/MapServer/5"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/0db311af55a349688de83884c09e7c1d/csv?layers=5",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/0db311af55a349688de83884c09e7c1d/csv?layers=5"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/0db311af55a349688de83884c09e7c1d/geojson?layers=5",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/0db311af55a349688de83884c09e7c1d/geojson?layers=5"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/0db311af55a349688de83884c09e7c1d/shapefile?layers=5",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/0db311af55a349688de83884c09e7c1d/shapefile?layers=5"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/0db311af55a349688de83884c09e7c1d/kml?layers=5",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/0db311af55a349688de83884c09e7c1d/kml?layers=5"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "0fdc623e-d36d-42b7-87bc-df0c7c9b5276",
+            "issued": "2020-09-08T23:13:01.000Z",
             "keyword": [
                 "acs",
                 "acs-ed",
@@ -14887,25 +14866,11 @@
                 "u-s-census-bureau",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:25.477081",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ACS-ED 2014-2018 Children-Enrolled Public: Social Characteristics (CDP02)",
-            "description": "<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The American Community Survey Education Tabulation (ACS-ED) is a custom tabulation of the ACS produced for the National Center of Education Statistics (NCES) by the U.S. Census Bureau. The ACS-ED provides a rich collection of social, economic, demographic, and housing characteristics for school systems, school-age children, and the parents of school-age children. In addition to focusing on school-age children, the ACS-ED provides enrollment iterations for children enrolled in public school. The data profiles include percentages (along with associated margins of error) that allow for comparison of school district-level conditions across the U.S. For more information about the NCES ACS-ED collection, visit the NCES Education Demographic and Geographic Estimates (EDGE) program at:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Demographic/ACS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Demographic/ACS</a><div><br /></div><div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Annotation values are negative value representations of estimates and have values when non-integer information needs to be represented. See the table below for a list of common Estimate/Margin of Error (E/M) values and their corresponding Annotation (EA/MA) values.</div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><table border='0' cellpadding='0' cellspacing='0' style='width:467.5pt; background:white; border-collapse:collapse;' width='623'>\n <tbody><tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-9</span></p>\n  </td>\n  <td style='width:418.25pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>An '-9' entry in the estimate and margin of\n  error columns indicates that data for this geographic area cannot be\n  displayed because the number of sample cases is too small.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-8</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>An '-8' means that the estimate is not\n  applicable or not available.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-6</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-6' entry in the estimate column indicates\n  that either no sample observations or too few sample observations were\n  available to compute an\u00a0 \u00a0estimate, or a ratio of medians cannot be\n  calculated because one or both of the median estimates falls in the lowest\n  interval or upper interval of an open-ended distribution.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-5</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-5' entry in the margin of error column\n  indicates that the estimate is controlled. A statistical test for sampling\n  variability is not appropriate.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-3</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-3' entry in the margin of error column indicates\n  that the median falls in the lowest interval or upper interval of an\n  open-ended distribution. A statistical test is not appropriate.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-2</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-2' entry in the margin of error column\n  indicates that either no sample observations or too few sample observations\n  were available to compute a standard error and thus the margin of error. A\n  statistical test is not appropriate.</span></p>\n  </td>\n </tr>\n</tbody></table><br /></div>",
-            "modified": "2024-10-19T12:47:24.522016",
-            "accessLevel": "public",
-            "identifier": "c3b14f47-18fb-4ca7-b605-d288488b6909",
-            "issued": "2020-09-08T23:30:56.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -14926,63 +14891,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "ACS-ED 2014-2018 Children-Enrolled Public: Housing Characteristics (CDP04)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The American Community Survey Education Tabulation (ACS-ED) is a custom tabulation of the ACS produced for the National Center of Education Statistics (NCES) by the U.S. Census Bureau. The ACS-ED provides a rich collection of social, economic, demographic, and housing characteristics for school systems, school-age children, and the parents of school-age children. In addition to focusing on school-age children, the ACS-ED provides enrollment iterations for children enrolled in public school. The data profiles include percentages (along with associated margins of error) that allow for comparison of school district-level conditions across the U.S. For more information about the NCES ACS-ED collection, visit the NCES Education Demographic and Geographic Estimates (EDGE) program at:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Demographic/ACS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Demographic/ACS</a><div><br /></div><div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Annotation values are negative value representations of estimates and have values when non-integer information needs to be represented. See the table below for a list of common Estimate/Margin of Error (E/M) values and their corresponding Annotation (EA/MA) values.</div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><table border='0' cellpadding='0' cellspacing='0' style='width:467.5pt; background:white; border-collapse:collapse;' width='623'>\n <tbody><tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-9</span></p>\n  </td>\n  <td style='width:418.25pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>An '-9' entry in the estimate and margin of\n  error columns indicates that data for this geographic area cannot be\n  displayed because the number of sample cases is too small.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-8</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>An '-8' means that the estimate is not\n  applicable or not available.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-6</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-6' entry in the estimate column indicates\n  that either no sample observations or too few sample observations were\n  available to compute an\u00a0 \u00a0estimate, or a ratio of medians cannot be\n  calculated because one or both of the median estimates falls in the lowest\n  interval or upper interval of an open-ended distribution.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-5</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-5' entry in the margin of error column\n  indicates that the estimate is controlled. A statistical test for sampling\n  variability is not appropriate.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-3</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-3' entry in the margin of error column indicates\n  that the median falls in the lowest interval or upper interval of an\n  open-ended distribution. A statistical test is not appropriate.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:49.25pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='66'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in; text-align:center;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>-2</span></p>\n  </td>\n  <td style='width:418.25pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='558'>\n  <p style='margin-top:3.0pt; margin-right:0in; margin-bottom:3.0pt; margin-left:0in;'><span style='font-family:&quot;Helvetica&quot;,sans-serif; color:#4C4C4C; background:white;'>A '-2' entry in the margin of error column\n  indicates that either no sample observations or too few sample observations\n  were available to compute a standard error and thus the margin of error. A\n  statistical test is not appropriate.</span></p>\n  </td>\n </tr>\n</tbody></table><br /></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/50609a329cc74f02b4ddca6b251df6be/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/50609a329cc74f02b4ddca6b251df6be/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::acs-ed-2014-2018-children-enrolled-public-social-characteristics-cdp02",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::acs-ed-2014-2018-children-enrolled-public-social-characteristics-cdp02"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Social_Economic/ACS_OpenData_1418/MapServer/1",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Social_Economic/ACS_OpenData_1418/MapServer/1"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/50609a329cc74f02b4ddca6b251df6be/csv?layers=1",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/50609a329cc74f02b4ddca6b251df6be/csv?layers=1"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/50609a329cc74f02b4ddca6b251df6be/geojson?layers=1",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/50609a329cc74f02b4ddca6b251df6be/geojson?layers=1"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/50609a329cc74f02b4ddca6b251df6be/shapefile?layers=1",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/50609a329cc74f02b4ddca6b251df6be/shapefile?layers=1"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/50609a329cc74f02b4ddca6b251df6be/kml?layers=1",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/50609a329cc74f02b4ddca6b251df6be/kml?layers=1"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "c3b14f47-18fb-4ca7-b605-d288488b6909",
+            "issued": "2020-09-08T23:30:56.000Z",
             "keyword": [
                 "acs",
                 "acs-ed",
@@ -14997,25 +14976,11 @@
                 "u-s-census-bureau",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:24.522016",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School District Office Locations 2018-19",
-            "description": "<div style='text-align:Left;'><div><div><p><span>The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary, secondary, and unified school district offices included in the NCES Common Core of Data (CCD). The CCD program annually collects administrative and fiscal data about all public schools, school districts, and state education agencies in the United States. The data are supplied by state education agency officials and include basic directory and contact information for schools and school districts, as well as characteristics about student demographics, number of teachers, school grade span, and various other administrative conditions. The CCD program also provides fiscal data about school district revenues and expenditures. CCD school and agency point locations are derived from reported information about the physical location of schools and agency administrative offices. The NCES EDGE program collaborates with the U.S. Census Bureau's Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for schools reported in the annual CCD directory file. The point locations in this data layer were developed from the 2018-2019 CCD collection. For more information about NCES school point data, see: https://nces.ed.gov/programs/edge/Geographic/SchoolLocations.</span></p></div></div></div>",
-            "modified": "2024-10-19T12:47:23.564531",
-            "accessLevel": "public",
-            "identifier": "797b1c5a-69e9-4866-8b82-e7f9f05d0e64",
-            "issued": "2020-03-17T17:02:17.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -15036,77 +15001,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "ACS-ED 2014-2018 Children-Enrolled Public: Social Characteristics (CDP02)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><div><div><p><span>The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for public elementary, secondary, and unified school district offices included in the NCES Common Core of Data (CCD). The CCD program annually collects administrative and fiscal data about all public schools, school districts, and state education agencies in the United States. The data are supplied by state education agency officials and include basic directory and contact information for schools and school districts, as well as characteristics about student demographics, number of teachers, school grade span, and various other administrative conditions. The CCD program also provides fiscal data about school district revenues and expenditures. CCD school and agency point locations are derived from reported information about the physical location of schools and agency administrative offices. The NCES EDGE program collaborates with the U.S. Census Bureau's Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for schools reported in the annual CCD directory file. The point locations in this data layer were developed from the 2018-2019 CCD collection. For more information about NCES school point data, see: https://nces.ed.gov/programs/edge/Geographic/SchoolLocations.</span></p></div></div></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/2cf893e8f3304db18ea9dd239acc74a3/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/2cf893e8f3304db18ea9dd239acc74a3/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-office-locations-2018-19",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-office-locations-2018-19"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICLEA_1819/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_GEOCODE_PUBLICLEA_1819/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Geocodes: Public Schools and Local Education Agencies",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_GEOCODE_PUBLIC_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Public Schools and Local Education Agencies"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Geocodes: Public Schools and Local Education Agencies",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PUBLICLEA_1819.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Public Schools and Local Education Agencies"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/2cf893e8f3304db18ea9dd239acc74a3/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/2cf893e8f3304db18ea9dd239acc74a3/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/2cf893e8f3304db18ea9dd239acc74a3/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/2cf893e8f3304db18ea9dd239acc74a3/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/2cf893e8f3304db18ea9dd239acc74a3/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/2cf893e8f3304db18ea9dd239acc74a3/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/2cf893e8f3304db18ea9dd239acc74a3/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/2cf893e8f3304db18ea9dd239acc74a3/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "797b1c5a-69e9-4866-8b82-e7f9f05d0e64",
+            "issued": "2020-03-17T17:02:17.000Z",
             "keyword": [
                 "ccd",
                 "common-core-of-data",
@@ -15124,25 +15103,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:23.564531",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School Attendance Boundary Survey 2015-2016",
-            "description": "<div style='text-align:Left;'><p style='margin-top:0px; margin-bottom:1.5rem; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><span style='font-family:inherit;'>This polygon files contains 2015-2016 school-year data delineating school attendance boundaries. These data were collected and processed as part of the School Attendance Boundary Survey (SABS) project which was funded by NCES to create geography delineating school attendance boundaries. Original source information that was used to create these boundary files were collected\u00a0</span><span style='font-family:inherit;'>were collected over a web-based self-reporting system, through e-mail, and mailed paper maps. The web application provided instructions and assistance to users via a user guide, a frequently asked questions document, and instructional videos. Boundaries supplied outside of the online reporting system typically fell into one of six categories: a digital geographic file, such as a shapefile or KML file; digital image files, such as jpegs and pdfs; narrative descriptions; an interactive web map; Excel or pdf address lists; and paper maps. 2</span><span style='font-family:inherit;'>015 TIGER/line features (that consist of streets, hydrography, railways, etc.) were used to digitize school attendance boundaries and was the primary source of information used to digitize analog information. This practice works well as most school attendance boundaries align with streets, railways, water bodies and similar line features included in the 2015 TIGER/line &quot;edges&quot; files. In those few cases in which a portion of a school attendance boundary serves both sides of a street contractor staff used Esri\u2019s Imagery base map to estimate the property lines of parcels. The data digitized from analog maps and verbal descriptions do not conform to cadastral data (and many of the original GIS files created by school districts do not conform with cadastral or parcel data).</span></p><p style='margin-top:0px; margin-bottom:1.5rem; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><span style='font-family:inherit;'>The SABS 2015-2016 file uses the WGS 1984 Web Mercator Auxiliary Sphere coordinate system.</span></p><p style='margin-top:0px; margin-bottom:1.5rem; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Additional information about SABS can be found on the\u00a0<a href='https://nces.ed.gov/programs/edge/SABS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:inherit;' target='_blank' rel='nofollow ugc noopener noreferrer'>EDGE website</a>.</p><p style='margin-top:0px; margin-bottom:1.5rem; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><span>The SABS dataset is intended for research purposes only and \nreflects a single snapshot in time. School boundaries frequently change \nfrom year to year. To verify legal descriptions of boundaries, users \nmust contact the school district directly.</span></p><p style='margin-top:0px; margin-bottom:1.5rem; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><span>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></span></p></div>",
-            "modified": "2024-10-19T12:47:22.648365",
-            "accessLevel": "public",
-            "identifier": "97613a80-63e6-454b-a078-eef7852fea24",
-            "issued": "2020-03-21T13:49:19.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -15163,63 +15128,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "School District Office Locations 2018-19"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><p style='margin-top:0px; margin-bottom:1.5rem; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><span style='font-family:inherit;'>This polygon files contains 2015-2016 school-year data delineating school attendance boundaries. These data were collected and processed as part of the School Attendance Boundary Survey (SABS) project which was funded by NCES to create geography delineating school attendance boundaries. Original source information that was used to create these boundary files were collected\u00a0</span><span style='font-family:inherit;'>were collected over a web-based self-reporting system, through e-mail, and mailed paper maps. The web application provided instructions and assistance to users via a user guide, a frequently asked questions document, and instructional videos. Boundaries supplied outside of the online reporting system typically fell into one of six categories: a digital geographic file, such as a shapefile or KML file; digital image files, such as jpegs and pdfs; narrative descriptions; an interactive web map; Excel or pdf address lists; and paper maps. 2</span><span style='font-family:inherit;'>015 TIGER/line features (that consist of streets, hydrography, railways, etc.) were used to digitize school attendance boundaries and was the primary source of information used to digitize analog information. This practice works well as most school attendance boundaries align with streets, railways, water bodies and similar line features included in the 2015 TIGER/line &quot;edges&quot; files. In those few cases in which a portion of a school attendance boundary serves both sides of a street contractor staff used Esri\u2019s Imagery base map to estimate the property lines of parcels. The data digitized from analog maps and verbal descriptions do not conform to cadastral data (and many of the original GIS files created by school districts do not conform with cadastral or parcel data).</span></p><p style='margin-top:0px; margin-bottom:1.5rem; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><span style='font-family:inherit;'>The SABS 2015-2016 file uses the WGS 1984 Web Mercator Auxiliary Sphere coordinate system.</span></p><p style='margin-top:0px; margin-bottom:1.5rem; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Additional information about SABS can be found on the\u00a0<a href='https://nces.ed.gov/programs/edge/SABS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:inherit;' target='_blank' rel='nofollow ugc noopener noreferrer'>EDGE website</a>.</p><p style='margin-top:0px; margin-bottom:1.5rem; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><span>The SABS dataset is intended for research purposes only and \nreflects a single snapshot in time. School boundaries frequently change \nfrom year to year. To verify legal descriptions of boundaries, users \nmust contact the school district directly.</span></p><p style='margin-top:0px; margin-bottom:1.5rem; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><span>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></span></p></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/9171e7ed24bb4362be8e388dc8dddf5a/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/9171e7ed24bb4362be8e388dc8dddf5a/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-attendance-boundary-survey-2015-2016",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-attendance-boundary-survey-2015-2016"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/SABS_1516/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/SABS_1516/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9171e7ed24bb4362be8e388dc8dddf5a/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9171e7ed24bb4362be8e388dc8dddf5a/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9171e7ed24bb4362be8e388dc8dddf5a/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9171e7ed24bb4362be8e388dc8dddf5a/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9171e7ed24bb4362be8e388dc8dddf5a/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9171e7ed24bb4362be8e388dc8dddf5a/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9171e7ed24bb4362be8e388dc8dddf5a/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9171e7ed24bb4362be8e388dc8dddf5a/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "97613a80-63e6-454b-a078-eef7852fea24",
+            "issued": "2020-03-21T13:49:19.000Z",
             "keyword": [
                 "attendance-zones",
                 "ccd",
@@ -15240,25 +15219,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:22.648365",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ACS-ED 2013-2017 Total Population: Social Characteristics (DP02)",
-            "description": "<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The American Community Survey Education Tabulation (ACS-ED) is a custom tabulation of the ACS produced for the National Center of Education Statistics (NCES) by the U.S. Census Bureau. The ACS-ED provides a rich collection of social, economic, demographic, and housing characteristics for school systems, school-age children, and the parents of school-age children. In addition to focusing on school-age children, the ACS-ED provides enrollment iterations for children enrolled in public school. The data profiles include percentages (along with associated margins of error) that allow for comparison of school district-level conditions across the U.S. For more information about the NCES ACS-ED collection, visit the NCES Education Demographic and Geographic Estimates (EDGE) program at:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Demographic/ACS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Demographic/ACS</a><div><br /></div><div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Annotation values are negative value representations of estimates and have values when non-integer information needs to be represented. See the table below for a list of common Estimate/Margin of Error (E/M) values and their corresponding Annotation (EA/MA) values.</div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><table border='0' cellpadding='0' cellspacing='0' style='margin-bottom:1.5rem; width:467.5pt; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial; border-collapse:collapse; border-spacing:0px; border:1px solid rgb(204, 204, 204); font-size:0.875rem;' width='623'><tbody><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-9</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:1pt solid windowtext; border-bottom:1pt solid windowtext; border-image:initial;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-9' entry in the estimate and margin of error columns indicates that data for this geographic area cannot be displayed because the number of sample cases is too small.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-8</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-8' means that the estimate is not applicable or not available.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-6</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-6' entry in the estimate column indicates that either no sample observations or too few sample observations were available to compute an\u00a0 \u00a0estimate, or a ratio of medians cannot be calculated because one or both of the median estimates falls in the lowest interval or upper interval of an open-ended distribution.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-5</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-5' entry in the margin of error column indicates that the estimate is controlled. A statistical test for sampling variability is not appropriate.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-3</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-3' entry in the margin of error column indicates that the median falls in the lowest interval or upper interval of an open-ended distribution. A statistical test is not appropriate.</span></p></td></tr><tr style='border-bottom:none;'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-2</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-2' entry in the margin of error column indicates that either no sample observations or too few sample observations were available to compute a standard error and thus the margin of error. A statistical test is not appropriate.</span></p></td></tr></tbody></table></div></div>",
-            "modified": "2024-10-19T12:47:21.645749",
-            "accessLevel": "public",
-            "identifier": "767a9a15-c3f8-43d2-bc41-96e2641828b6",
-            "issued": "2020-12-14T23:20:05.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -15279,63 +15244,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "School Attendance Boundary Survey 2015-2016"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<span style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>The American Community Survey Education Tabulation (ACS-ED) is a custom tabulation of the ACS produced for the National Center of Education Statistics (NCES) by the U.S. Census Bureau. The ACS-ED provides a rich collection of social, economic, demographic, and housing characteristics for school systems, school-age children, and the parents of school-age children. In addition to focusing on school-age children, the ACS-ED provides enrollment iterations for children enrolled in public school. The data profiles include percentages (along with associated margins of error) that allow for comparison of school district-level conditions across the U.S. For more information about the NCES ACS-ED collection, visit the NCES Education Demographic and Geographic Estimates (EDGE) program at:\u00a0</span><a href='https://nces.ed.gov/programs/edge/Demographic/ACS' style='color:rgb(0, 121, 193); text-decoration-line:none; font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Demographic/ACS</a><div><br /></div><div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>Annotation values are negative value representations of estimates and have values when non-integer information needs to be represented. See the table below for a list of common Estimate/Margin of Error (E/M) values and their corresponding Annotation (EA/MA) values.</div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><table border='0' cellpadding='0' cellspacing='0' style='margin-bottom:1.5rem; width:467.5pt; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial; border-collapse:collapse; border-spacing:0px; border:1px solid rgb(204, 204, 204); font-size:0.875rem;' width='623'><tbody><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-9</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:1pt solid windowtext; border-bottom:1pt solid windowtext; border-image:initial;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-9' entry in the estimate and margin of error columns indicates that data for this geographic area cannot be displayed because the number of sample cases is too small.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-8</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>An '-8' means that the estimate is not applicable or not available.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-6</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-6' entry in the estimate column indicates that either no sample observations or too few sample observations were available to compute an\u00a0 \u00a0estimate, or a ratio of medians cannot be calculated because one or both of the median estimates falls in the lowest interval or upper interval of an open-ended distribution.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-5</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-5' entry in the margin of error column indicates that the estimate is controlled. A statistical test for sampling variability is not appropriate.</span></p></td></tr><tr style='border-bottom:1px solid rgb(204, 204, 204);'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-3</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-3' entry in the margin of error column indicates that the median falls in the lowest interval or upper interval of an open-ended distribution. A statistical test is not appropriate.</span></p></td></tr><tr style='border-bottom:none;'><td style='border-left:1pt solid windowtext; border-right:1pt solid windowtext; padding:0in 5.4pt; width:49.25pt; border-bottom:1pt solid windowtext; border-image:initial; border-top:none;' valign='top' width='66'><p style='margin:3pt 0in; text-align:center;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>-2</span></p></td><td style='border-left:none; border-right:1pt solid windowtext; padding:0in 5.4pt; width:418.25pt; border-top:none; border-bottom:1pt solid windowtext;' valign='top' width='558'><p style='margin:3pt 0in;'><span style='font-family:Arial, sans-serif; background-image:initial; background-position:initial; background-size:initial; background-repeat:initial; background-attachment:initial; background-origin:initial; background-clip:initial;'>A '-2' entry in the margin of error column indicates that either no sample observations or too few sample observations were available to compute a standard error and thus the margin of error. A statistical test is not appropriate.</span></p></td></tr></tbody></table></div></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/cab3accd8ca541f68f988b3fe3278e7c/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/cab3accd8ca541f68f988b3fe3278e7c/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::acs-ed-2013-2017-total-population-social-characteristics-dp02",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::acs-ed-2013-2017-total-population-social-characteristics-dp02"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Social_Economic/ACS_OpenData_1317/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Social_Economic/ACS_OpenData_1317/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/cab3accd8ca541f68f988b3fe3278e7c/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/cab3accd8ca541f68f988b3fe3278e7c/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/cab3accd8ca541f68f988b3fe3278e7c/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/cab3accd8ca541f68f988b3fe3278e7c/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/cab3accd8ca541f68f988b3fe3278e7c/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/cab3accd8ca541f68f988b3fe3278e7c/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/cab3accd8ca541f68f988b3fe3278e7c/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/cab3accd8ca541f68f988b3fe3278e7c/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "767a9a15-c3f8-43d2-bc41-96e2641828b6",
+            "issued": "2020-12-14T23:20:05.000Z",
             "keyword": [
                 "acs",
                 "acs-ed",
@@ -15350,25 +15329,11 @@
                 "u-s-census-bureau",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:21.645749",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Postsecondary School Locations - Current",
-            "description": "<p style='margin-bottom:0in;'>The National Center for Education Statistics\u2019 (NCES)\nEducation Demographic and Geographic Estimates (EDGE) program develops annually\nupdated point locations (latitude and longitude) for postsecondary institutions\nincluded in the NCES Integrated Postsecondary Education Data System (IPEDS).\nThe IPEDS program annually collects information about enrollments, program\ncompletions, graduation rates, faculty and staff, finances, institutional\nprices, and student financial aid from colleges, universities, and technical\nand vocational institutions that participate in federal student financial aid\nprograms under the Higher Education Act of 1965 (as amended). The NCES EDGE\nprogram uses address information reported in the annually updated IPEDS\ndirectory file to develop point locations for all institutions reported in\nIPEDS. The point locations in this data layer represent the most current IPEDS\ncollection available. For more information about NCES school point data,\nsee:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>.</p>\n\n<p style='margin-bottom:0in;'>Collections are available for the following years:</p>\n\n<ul>\n <li><a href='https://nces.maps.arcgis.com/home/item.html?id=92e4b742b59f4b90b3af85e444a912f7' target='_blank' rel='nofollow ugc noopener noreferrer'>2022-23</a></li>\n <li><a href='https://nces.maps.arcgis.com/home/item.html?id=49cd0352fe2546a99cbeb8ec332d9354' target='_blank' rel='nofollow ugc noopener noreferrer'>2021-22</a></li>\n <li><a href='https://nces.maps.arcgis.com/home/item.html?id=296839772bf14df29c290202f8547ff1' target='_blank' rel='nofollow ugc noopener noreferrer'>2020-21</a></li>\n <li><a href='https://nces.maps.arcgis.com/home/item.html?id=6a2b95d345d8452ca527b30490096391' target='_blank' rel='nofollow ugc noopener noreferrer'>2019-20</a></li>\n <li><a href='https://nces.maps.arcgis.com/home/item.html?id=6aa17db388b34c6c9d6ae040993cd99d' target='_blank' rel='nofollow ugc noopener noreferrer'>2018-19</a></li>\n <li><a href='https://nces.maps.arcgis.com/home/item.html?id=adc0c93f5b004246b186e90f4b43830f' target='_blank' rel='nofollow ugc noopener noreferrer'>2017-18</a></li>\n <li><a href='https://nces.maps.arcgis.com/home/item.html?id=72d9d1167cad4b619fa23f36f05e8766' target='_blank' rel='nofollow ugc noopener noreferrer'>2016-17</a></li>\n <li><a href='https://nces.maps.arcgis.com/home/item.html?id=809cc7caddf34d3692970c9a781dac03' target='_blank' rel='nofollow ugc noopener noreferrer'>2015-16</a></li>\n</ul>\n\n<p style='margin-bottom:0in;'>All information contained in this file is in the public\ndomain. Data users are ad\u00a0vised to review NCES program documentation and feature\nclass metadata to understand the limitations and appropriate use of these data.</p>",
-            "modified": "2024-10-19T12:47:20.761379",
-            "accessLevel": "public",
-            "identifier": "318ff24e-8a33-4e98-8943-6f7330cc5858",
-            "issued": "2020-03-13T21:07:34.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -15389,63 +15354,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "ACS-ED 2013-2017 Total Population: Social Characteristics (DP02)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<p style='margin-bottom:0in;'>The National Center for Education Statistics\u2019 (NCES)\nEducation Demographic and Geographic Estimates (EDGE) program develops annually\nupdated point locations (latitude and longitude) for postsecondary institutions\nincluded in the NCES Integrated Postsecondary Education Data System (IPEDS).\nThe IPEDS program annually collects information about enrollments, program\ncompletions, graduation rates, faculty and staff, finances, institutional\nprices, and student financial aid from colleges, universities, and technical\nand vocational institutions that participate in federal student financial aid\nprograms under the Higher Education Act of 1965 (as amended). The NCES EDGE\nprogram uses address information reported in the annually updated IPEDS\ndirectory file to develop point locations for all institutions reported in\nIPEDS. The point locations in this data layer represent the most current IPEDS\ncollection available. For more information about NCES school point data,\nsee:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>.</p>\n\n<p style='margin-bottom:0in;'>Collections are available for the following years:</p>\n\n<ul>\n <li><a href='https://nces.maps.arcgis.com/home/item.html?id=92e4b742b59f4b90b3af85e444a912f7' target='_blank' rel='nofollow ugc noopener noreferrer'>2022-23</a></li>\n <li><a href='https://nces.maps.arcgis.com/home/item.html?id=49cd0352fe2546a99cbeb8ec332d9354' target='_blank' rel='nofollow ugc noopener noreferrer'>2021-22</a></li>\n <li><a href='https://nces.maps.arcgis.com/home/item.html?id=296839772bf14df29c290202f8547ff1' target='_blank' rel='nofollow ugc noopener noreferrer'>2020-21</a></li>\n <li><a href='https://nces.maps.arcgis.com/home/item.html?id=6a2b95d345d8452ca527b30490096391' target='_blank' rel='nofollow ugc noopener noreferrer'>2019-20</a></li>\n <li><a href='https://nces.maps.arcgis.com/home/item.html?id=6aa17db388b34c6c9d6ae040993cd99d' target='_blank' rel='nofollow ugc noopener noreferrer'>2018-19</a></li>\n <li><a href='https://nces.maps.arcgis.com/home/item.html?id=adc0c93f5b004246b186e90f4b43830f' target='_blank' rel='nofollow ugc noopener noreferrer'>2017-18</a></li>\n <li><a href='https://nces.maps.arcgis.com/home/item.html?id=72d9d1167cad4b619fa23f36f05e8766' target='_blank' rel='nofollow ugc noopener noreferrer'>2016-17</a></li>\n <li><a href='https://nces.maps.arcgis.com/home/item.html?id=809cc7caddf34d3692970c9a781dac03' target='_blank' rel='nofollow ugc noopener noreferrer'>2015-16</a></li>\n</ul>\n\n<p style='margin-bottom:0in;'>All information contained in this file is in the public\ndomain. Data users are ad\u00a0vised to review NCES program documentation and feature\nclass metadata to understand the limitations and appropriate use of these data.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/a15e8731a17a46aabc452ea607f172c0/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/a15e8731a17a46aabc452ea607f172c0/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::postsecondary-school-locations-current-1",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::postsecondary-school-locations-current-1"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://services1.arcgis.com/Ua5sjt3LWTPigjyD/arcgis/rest/services/Postsecondary_School_Locations_Current/FeatureServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://services1.arcgis.com/Ua5sjt3LWTPigjyD/arcgis/rest/services/Postsecondary_School_Locations_Current/FeatureServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a15e8731a17a46aabc452ea607f172c0/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a15e8731a17a46aabc452ea607f172c0/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a15e8731a17a46aabc452ea607f172c0/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a15e8731a17a46aabc452ea607f172c0/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a15e8731a17a46aabc452ea607f172c0/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a15e8731a17a46aabc452ea607f172c0/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a15e8731a17a46aabc452ea607f172c0/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/a15e8731a17a46aabc452ea607f172c0/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "318ff24e-8a33-4e98-8943-6f7330cc5858",
+            "issued": "2020-03-13T21:07:34.000Z",
             "keyword": [
                 "edge",
                 "education",
@@ -15461,25 +15440,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:20.761379",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Postsecondary School Locations 2020-21",
-            "description": "<div style='text-align:Left;'><div><div><p><span><span>The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for postsecondary institutions included in the NCES Integrated Postsecondary Education Data System (IPEDS). The IPEDS program annually collects information about enrollments, program completions, graduation rates, faculty and staff, finances, institutional prices, and student financial aid from every college, university, and technical and vocational institution that participates in federal student financial aid programs under the Higher Education Act of 1965 (as amended). IPEDS school point locations are derived from reported information about the physical location of schools. The NCES EDGE program collaborates with the U.S. Census Bureau's Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for schools reported in the annual IPEDS file. The point locations in this data layer were developed from the 2020-2021 IPEDS collection. For more information about NCES school point data, see: <a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>.</span></span></p><p><span><span>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></span></span></p></div></div></div>",
-            "modified": "2024-10-19T12:47:19.317515",
-            "accessLevel": "public",
-            "identifier": "7133e891-4d35-436b-a51a-1c72d8fc19c4",
-            "issued": "2021-04-30T15:29:07.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -15500,77 +15465,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Postsecondary School Locations - Current"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><div><div><p><span><span>The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for postsecondary institutions included in the NCES Integrated Postsecondary Education Data System (IPEDS). The IPEDS program annually collects information about enrollments, program completions, graduation rates, faculty and staff, finances, institutional prices, and student financial aid from every college, university, and technical and vocational institution that participates in federal student financial aid programs under the Higher Education Act of 1965 (as amended). IPEDS school point locations are derived from reported information about the physical location of schools. The NCES EDGE program collaborates with the U.S. Census Bureau's Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for schools reported in the annual IPEDS file. The point locations in this data layer were developed from the 2020-2021 IPEDS collection. For more information about NCES school point data, see: <a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a>.</span></span></p><p><span><span>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></span></span></p></div></div></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/296839772bf14df29c290202f8547ff1/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/296839772bf14df29c290202f8547ff1/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::postsecondary-school-locations-2020-21",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::postsecondary-school-locations-2020-21"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Postsecondary_School_Locations/EDGE_GEOCODE_POSTSECONDARYSCH_2021/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Postsecondary_School_Locations/EDGE_GEOCODE_POSTSECONDARYSCH_2021/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "EDGE Postsecondary File Documentation",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_GEOCODE_PUBLIC_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "EDGE Postsecondary File Documentation"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "EDGE Geocode Postsecondary",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_POSTSECONDARYSCH_2021.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "EDGE Geocode Postsecondary"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/296839772bf14df29c290202f8547ff1/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/296839772bf14df29c290202f8547ff1/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/296839772bf14df29c290202f8547ff1/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/296839772bf14df29c290202f8547ff1/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/296839772bf14df29c290202f8547ff1/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/296839772bf14df29c290202f8547ff1/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/296839772bf14df29c290202f8547ff1/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/296839772bf14df29c290202f8547ff1/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "7133e891-4d35-436b-a51a-1c72d8fc19c4",
+            "issued": "2021-04-30T15:29:07.000Z",
             "keyword": [
                 "edge",
                 "education",
@@ -15586,25 +15565,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:19.317515",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Postsecondary School Locations 2019-20",
-            "description": "<div style='text-align:Left;'><div><div><p><span><span>The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for postsecondary institutions included in the NCES Integrated Postsecondary Education Data System (IPEDS). The IPEDS program annually collects information about enrollments, program completions, graduation rates, faculty and staff, finances, institutional prices, and student financial aid from every college, university, and technical and vocational institution that participates in federal student financial aid programs under the Higher Education Act of 1965 (as amended). IPEDS school point locations are derived from reported information about the physical location of schools. The NCES EDGE program collaborates with the U.S. Census Bureau's Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for schools reported in the annual IPEDS file. The point locations in this data layer were developed from the 2019-2020 IPEDS collection. For more information about NCES school point data, see:\u00a0</span></span><a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a><span><span>.</span></span></p><p><span><span>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></span></span></p><p><span></span></p></div></div></div>",
-            "modified": "2024-10-19T12:47:18.319295",
-            "accessLevel": "public",
-            "identifier": "3d63f36c-744a-4d86-aabc-98f27ef34acc",
-            "issued": "2020-03-31T21:16:45.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -15625,77 +15590,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Postsecondary School Locations 2020-21"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><div><div><p><span><span>The National Center for Education Statistics' (NCES) Education Demographic and Geographic Estimate (EDGE) program develops annually updated point locations (latitude and longitude) for postsecondary institutions included in the NCES Integrated Postsecondary Education Data System (IPEDS). The IPEDS program annually collects information about enrollments, program completions, graduation rates, faculty and staff, finances, institutional prices, and student financial aid from every college, university, and technical and vocational institution that participates in federal student financial aid programs under the Higher Education Act of 1965 (as amended). IPEDS school point locations are derived from reported information about the physical location of schools. The NCES EDGE program collaborates with the U.S. Census Bureau's Education Demographic, Geographic, and Economic Statistics (EDGE) Branch to develop point locations for schools reported in the annual IPEDS file. The point locations in this data layer were developed from the 2019-2020 IPEDS collection. For more information about NCES school point data, see:\u00a0</span></span><a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a><span><span>.</span></span></p><p><span><span>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></span></span></p><p><span></span></p></div></div></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/6a2b95d345d8452ca527b30490096391/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/6a2b95d345d8452ca527b30490096391/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::postsecondary-school-locations-2019-20",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::postsecondary-school-locations-2019-20"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Postsecondary_School_Locations/EDGE_GEOCODE_POSTSECONDARYSCH_1920/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/Postsecondary_School_Locations/EDGE_GEOCODE_POSTSECONDARYSCH_1920/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "Geocodes: Postsecondary Schools",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_GEOCODE_POSTSEC_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Postsecondary Schools"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "Geocodes: Postsecondary Schools",
                     "downloadURL": "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_POSTSEC_1920.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "Geocodes: Postsecondary Schools"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6a2b95d345d8452ca527b30490096391/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6a2b95d345d8452ca527b30490096391/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6a2b95d345d8452ca527b30490096391/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6a2b95d345d8452ca527b30490096391/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6a2b95d345d8452ca527b30490096391/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6a2b95d345d8452ca527b30490096391/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6a2b95d345d8452ca527b30490096391/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6a2b95d345d8452ca527b30490096391/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "3d63f36c-744a-4d86-aabc-98f27ef34acc",
+            "issued": "2020-03-31T21:16:45.000Z",
             "keyword": [
                 "edge",
                 "education",
@@ -15711,25 +15690,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:18.319295",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School District Characteristics 2022-23",
-            "description": "<div style='text-align:Left;'><div><div><p>The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimates (EDGE) program develops annually updated school district boundary composite files that include public elementary, secondary, and unified school district boundaries clipped to the U.S. shoreline. School districts are special-purpose governments and administrative units designed by state and local officials to provide public education for local residents. District boundaries are collected for NCES by the U.S. Census Bureau to develop demographic estimates and to support educational research and program administration. The NCES Common Core of Data (CCD) program is an annual collection of basic administrative characteristics for all public schools, school districts, and state education agencies in the United States. These characteristics are reported by state education officials and include directory information, number of students, number of teachers, grade span, and other conditions. The administrative attributes in this layer were developed from the 2022-2023 CCD collection. For more information about NCES school district boundaries, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries</a>. For more information about CCD school district attributes, see:\u00a0<a href='https://nces.ed.gov/ccd/files.asp' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/ccd/files.asp</a>.</p><p style='margin-bottom:0in;'>Notes:</p><figure><table border='0' cellpadding='0' cellspacing='0' style='border-collapse:collapse;'><tbody><tr><td style='border:1pt solid windowtext; padding:0in 5.4pt; width:71.75pt;' width='96'><p style='margin:0in;'>-1 or M</p></td><td style='border-bottom:1pt solid windowtext; border-image:initial; border-left-style:none; border-right:1pt solid windowtext; border-top:1pt solid windowtext; padding:0in 5.4pt; width:337.25pt;' width='450'><p style='margin:0in;'>Indicates that the data are missing.</p></td></tr><tr><td style='border-bottom:1pt solid windowtext; border-image:initial; border-left:1pt solid windowtext; border-right:1pt solid windowtext; border-top-style:none; padding:0in 5.4pt; width:71.75pt;' width='96'><p style='margin:0in;'>-2 or N</p></td><td style='border-bottom:1pt solid windowtext; border-left-style:none; border-right:1pt solid windowtext; border-top-style:none; padding:0in 5.4pt; width:337.25pt;' width='450'><p style='margin:0in;'>Indicates that the data are not applicable.</p></td></tr><tr><td style='border-bottom:1pt solid windowtext; border-image:initial; border-left:1pt solid windowtext; border-right:1pt solid windowtext; border-top-style:none; padding:0in 5.4pt; width:71.75pt;' width='96'><p style='margin:0in;'>-9</p></td><td style='border-bottom:1pt solid windowtext; border-left-style:none; border-right:1pt solid windowtext; border-top-style:none; padding:0in 5.4pt; width:337.25pt;' width='450'><p style='margin:0in;'>Indicates that the data do not meet NCES data quality standards.</p></td></tr></tbody></table></figure><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</p></div></div></div>",
-            "modified": "2024-10-19T12:47:14.674568",
-            "accessLevel": "public",
-            "identifier": "402ef1e2-765c-4228-8b68-a4808c0a177f",
-            "issued": "2024-06-11T18:01:46.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -15750,63 +15715,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Postsecondary School Locations 2019-20"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><div><div><p>The National Center for Education Statistics\u2019 (NCES) Education Demographic and Geographic Estimates (EDGE) program develops annually updated school district boundary composite files that include public elementary, secondary, and unified school district boundaries clipped to the U.S. shoreline. School districts are special-purpose governments and administrative units designed by state and local officials to provide public education for local residents. District boundaries are collected for NCES by the U.S. Census Bureau to develop demographic estimates and to support educational research and program administration. The NCES Common Core of Data (CCD) program is an annual collection of basic administrative characteristics for all public schools, school districts, and state education agencies in the United States. These characteristics are reported by state education officials and include directory information, number of students, number of teachers, grade span, and other conditions. The administrative attributes in this layer were developed from the 2022-2023 CCD collection. For more information about NCES school district boundaries, see:\u00a0<a href='https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries</a>. For more information about CCD school district attributes, see:\u00a0<a href='https://nces.ed.gov/ccd/files.asp' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/ccd/files.asp</a>.</p><p style='margin-bottom:0in;'>Notes:</p><figure><table border='0' cellpadding='0' cellspacing='0' style='border-collapse:collapse;'><tbody><tr><td style='border:1pt solid windowtext; padding:0in 5.4pt; width:71.75pt;' width='96'><p style='margin:0in;'>-1 or M</p></td><td style='border-bottom:1pt solid windowtext; border-image:initial; border-left-style:none; border-right:1pt solid windowtext; border-top:1pt solid windowtext; padding:0in 5.4pt; width:337.25pt;' width='450'><p style='margin:0in;'>Indicates that the data are missing.</p></td></tr><tr><td style='border-bottom:1pt solid windowtext; border-image:initial; border-left:1pt solid windowtext; border-right:1pt solid windowtext; border-top-style:none; padding:0in 5.4pt; width:71.75pt;' width='96'><p style='margin:0in;'>-2 or N</p></td><td style='border-bottom:1pt solid windowtext; border-left-style:none; border-right:1pt solid windowtext; border-top-style:none; padding:0in 5.4pt; width:337.25pt;' width='450'><p style='margin:0in;'>Indicates that the data are not applicable.</p></td></tr><tr><td style='border-bottom:1pt solid windowtext; border-image:initial; border-left:1pt solid windowtext; border-right:1pt solid windowtext; border-top-style:none; padding:0in 5.4pt; width:71.75pt;' width='96'><p style='margin:0in;'>-9</p></td><td style='border-bottom:1pt solid windowtext; border-left-style:none; border-right:1pt solid windowtext; border-top-style:none; padding:0in 5.4pt; width:337.25pt;' width='450'><p style='margin:0in;'>Indicates that the data do not meet NCES data quality standards.</p></td></tr></tbody></table></figure><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.</p></div></div></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/ce8c3991435c425986c2fdb334e90093/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/ce8c3991435c425986c2fdb334e90093/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-characteristics-2022-23",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-characteristics-2022-23"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/School_District_Boundaries/EDGE_ADMINDATA_SCHOOLDISTRICTS_SY2223/MapServer/1",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/School_District_Boundaries/EDGE_ADMINDATA_SCHOOLDISTRICTS_SY2223/MapServer/1"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ce8c3991435c425986c2fdb334e90093/csv?layers=1",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ce8c3991435c425986c2fdb334e90093/csv?layers=1"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ce8c3991435c425986c2fdb334e90093/geojson?layers=1",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ce8c3991435c425986c2fdb334e90093/geojson?layers=1"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ce8c3991435c425986c2fdb334e90093/shapefile?layers=1",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ce8c3991435c425986c2fdb334e90093/shapefile?layers=1"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ce8c3991435c425986c2fdb334e90093/kml?layers=1",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ce8c3991435c425986c2fdb334e90093/kml?layers=1"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "402ef1e2-765c-4228-8b68-a4808c0a177f",
+            "issued": "2024-06-11T18:01:46.000Z",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "ccd",
@@ -15821,25 +15800,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:14.674568",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Public School Characteristics 2022-23",
-            "description": "<div style='text-align:Left;'><p></p><p style='margin-top:12.0pt; margin-right:0in; margin-bottom:12.0pt; margin-left:0in; background:white;'><span style='font-family:&quot;Calibri&quot;,sans-serif; color:#4C4C4C;'>The National Center for\nEducation Statistics' (NCES) Education Demographic and Geographic Estimates\n(EDGE) program develops annually updated point locations (latitude and\nlongitude) for public elementary and secondary schools included in the NCES\nCommon Core of Data (CCD). The CCD program annually collects administrative and\nfiscal data about all public schools, school districts, and state education\nagencies in the United States. The data are supplied by state education agency\nofficials and include basic directory and contact information for schools and\nschool districts, as well as characteristics about student demographics, number\nof teachers, school grade span, and various other administrative conditions.\nCCD school and agency point locations are derived from reported information\nabout the physical location of schools and agency administrative offices. The\npoint locations and administrative attributes in this data layer were developed\nfrom the 2022-2023 CCD collection. For more information about NCES school point\ndata, see:\u00a0</span><u><span style='font-family:&quot;Calibri&quot;,sans-serif; color:blue;'><a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a></span></u><span style='font-family:&quot;Calibri&quot;,sans-serif; color:#4C4C4C;'>. For more information\nabout these CCD attributes, as well as additional attributes not included, see:\n</span><u><span style='font-family:&quot;Calibri&quot;,sans-serif; color:blue;'><a href='https://nces.ed.gov/ccd/files.asp' rel='nofollow ugc'>https://nces.ed.gov/ccd/files.asp</a></span></u><span style='font-family:&quot;Calibri&quot;,sans-serif; color:#4C4C4C;'>.</span></p>\n\n<p style='margin-bottom:0in; background:white;'><span style='font-family:&quot;Calibri&quot;,sans-serif; color:#4C4C4C;'>Notes:</span></p>\n\n<table border='1' cellpadding='0' cellspacing='0' style='border-collapse:collapse;'>\n <tbody><tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-family:&quot;Calibri&quot;,sans-serif;'>-1 or M</span></p>\n  </td>\n  <td style='width:233.75pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-family:&quot;Calibri&quot;,sans-serif;'>Indicates that the data are missing.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-family:&quot;Calibri&quot;,sans-serif;'>-2 or N</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-family:&quot;Calibri&quot;,sans-serif;'>Indicates that the data are not\n  applicable.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-family:&quot;Calibri&quot;,sans-serif;'>-9</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-family:&quot;Calibri&quot;,sans-serif;'>Indicates that the data do not meet\n  NCES data quality standards.</span></p>\n  </td>\n </tr>\n</tbody></table>\n\n<p style='margin-top:12.0pt; margin-right:0in; margin-bottom:12.0pt; margin-left:0in; background:white;'><span style='font-family:&quot;Calibri&quot;,sans-serif; color:#4C4C4C;'>All information\ncontained in this file is in the public domain. Data users are advised to\nreview NCES program documentation and feature class metadata to understand the\nlimitations and appropriate use of these data.</span></p><br /><p></p></div>",
-            "modified": "2024-10-19T12:47:10.315787",
-            "accessLevel": "public",
-            "identifier": "8aa75aa1-d594-44eb-bcfc-ac47157fa5d5",
-            "issued": "2024-06-11T19:48:40.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -15860,63 +15825,77 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "School District Characteristics 2022-23"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<div style='text-align:Left;'><p></p><p style='margin-top:12.0pt; margin-right:0in; margin-bottom:12.0pt; margin-left:0in; background:white;'><span style='font-family:&quot;Calibri&quot;,sans-serif; color:#4C4C4C;'>The National Center for\nEducation Statistics' (NCES) Education Demographic and Geographic Estimates\n(EDGE) program develops annually updated point locations (latitude and\nlongitude) for public elementary and secondary schools included in the NCES\nCommon Core of Data (CCD). The CCD program annually collects administrative and\nfiscal data about all public schools, school districts, and state education\nagencies in the United States. The data are supplied by state education agency\nofficials and include basic directory and contact information for schools and\nschool districts, as well as characteristics about student demographics, number\nof teachers, school grade span, and various other administrative conditions.\nCCD school and agency point locations are derived from reported information\nabout the physical location of schools and agency administrative offices. The\npoint locations and administrative attributes in this data layer were developed\nfrom the 2022-2023 CCD collection. For more information about NCES school point\ndata, see:\u00a0</span><u><span style='font-family:&quot;Calibri&quot;,sans-serif; color:blue;'><a href='https://nces.ed.gov/programs/edge/Geographic/SchoolLocations' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/SchoolLocations</a></span></u><span style='font-family:&quot;Calibri&quot;,sans-serif; color:#4C4C4C;'>. For more information\nabout these CCD attributes, as well as additional attributes not included, see:\n</span><u><span style='font-family:&quot;Calibri&quot;,sans-serif; color:blue;'><a href='https://nces.ed.gov/ccd/files.asp' rel='nofollow ugc'>https://nces.ed.gov/ccd/files.asp</a></span></u><span style='font-family:&quot;Calibri&quot;,sans-serif; color:#4C4C4C;'>.</span></p>\n\n<p style='margin-bottom:0in; background:white;'><span style='font-family:&quot;Calibri&quot;,sans-serif; color:#4C4C4C;'>Notes:</span></p>\n\n<table border='1' cellpadding='0' cellspacing='0' style='border-collapse:collapse;'>\n <tbody><tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-family:&quot;Calibri&quot;,sans-serif;'>-1 or M</span></p>\n  </td>\n  <td style='width:233.75pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-family:&quot;Calibri&quot;,sans-serif;'>Indicates that the data are missing.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-family:&quot;Calibri&quot;,sans-serif;'>-2 or N</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-family:&quot;Calibri&quot;,sans-serif;'>Indicates that the data are not\n  applicable.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-family:&quot;Calibri&quot;,sans-serif;'>-9</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-family:&quot;Calibri&quot;,sans-serif;'>Indicates that the data do not meet\n  NCES data quality standards.</span></p>\n  </td>\n </tr>\n</tbody></table>\n\n<p style='margin-top:12.0pt; margin-right:0in; margin-bottom:12.0pt; margin-left:0in; background:white;'><span style='font-family:&quot;Calibri&quot;,sans-serif; color:#4C4C4C;'>All information\ncontained in this file is in the public domain. Data users are advised to\nreview NCES program documentation and feature class metadata to understand the\nlimitations and appropriate use of these data.</span></p><br /><p></p></div>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/6a4fa1b0434e4688b5d60c2e5c1dcaaa/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/6a4fa1b0434e4688b5d60c2e5c1dcaaa/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::public-school-characteristics-2022-23",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::public-school-characteristics-2022-23"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_ADMINDATA_PUBLICSCH_2223/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/K12_School_Locations/EDGE_ADMINDATA_PUBLICSCH_2223/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6a4fa1b0434e4688b5d60c2e5c1dcaaa/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6a4fa1b0434e4688b5d60c2e5c1dcaaa/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6a4fa1b0434e4688b5d60c2e5c1dcaaa/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6a4fa1b0434e4688b5d60c2e5c1dcaaa/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6a4fa1b0434e4688b5d60c2e5c1dcaaa/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6a4fa1b0434e4688b5d60c2e5c1dcaaa/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6a4fa1b0434e4688b5d60c2e5c1dcaaa/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/6a4fa1b0434e4688b5d60c2e5c1dcaaa/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "8aa75aa1-d594-44eb-bcfc-ac47157fa5d5",
+            "issued": "2024-06-11T19:48:40.000Z",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "ccd",
@@ -15932,25 +15911,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:10.315787",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School District Characteristics 2017-18",
-            "description": "<p></p><p>The National Center for Education Statistics\u2019 (NCES) Education \nDemographic and Geographic Estimate (EDGE) program develops annually \nupdated school district boundary composite files that include public \nelementary, secondary, and unified school district boundaries clipped to\n the U.S. shoreline. School districts are special-purpose administrative\n units designed by state and local officials to provide public education\n for local residents. District boundaries are collected for NCES by the \nU.S. Census Bureau to develop demographic estimates and to support \neducational research and program administration. The NCES Common Core of\n Data (CCD) program is an annual collection of basic administrative \ncharacteristics for all public schools, school districts, and state \neducation agencies in the United States. These characteristics are \nreported by state education officials and include directory information,\n number of students, number of teachers, grade span, and other \nconditions. The administrative attributes in this layer were developed \nfrom the 2017-2018 CCD collection. For more information about NCES \nschool district boundaries, see: <a href='https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries</a>. For more information about CCD school district attributes, see: <a href='https://nces.ed.gov/ccd/files.asp' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/ccd/files.asp</a>.</p><div>Notes:</div><div><table border='1' cellpadding='0' cellspacing='0' style='border-collapse:collapse; border:none;'>\n <tbody><tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-1 or M</span></p>\n  </td>\n  <td style='width:233.75pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are missing.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-2 or N</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are not applicable.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-9</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data do not meet NCES data quality standards.</span></p>\n  </td>\n </tr>\n</tbody></table></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><p></p><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></p>",
-            "modified": "2024-10-19T12:47:09.318500",
-            "accessLevel": "public",
-            "identifier": "9d11931a-642b-457b-86ee-e07b41bdba9c",
-            "issued": "2020-04-27T14:14:04.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -15971,77 +15936,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "Public School Characteristics 2022-23"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<p></p><p>The National Center for Education Statistics\u2019 (NCES) Education \nDemographic and Geographic Estimate (EDGE) program develops annually \nupdated school district boundary composite files that include public \nelementary, secondary, and unified school district boundaries clipped to\n the U.S. shoreline. School districts are special-purpose administrative\n units designed by state and local officials to provide public education\n for local residents. District boundaries are collected for NCES by the \nU.S. Census Bureau to develop demographic estimates and to support \neducational research and program administration. The NCES Common Core of\n Data (CCD) program is an annual collection of basic administrative \ncharacteristics for all public schools, school districts, and state \neducation agencies in the United States. These characteristics are \nreported by state education officials and include directory information,\n number of students, number of teachers, grade span, and other \nconditions. The administrative attributes in this layer were developed \nfrom the 2017-2018 CCD collection. For more information about NCES \nschool district boundaries, see: <a href='https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries</a>. For more information about CCD school district attributes, see: <a href='https://nces.ed.gov/ccd/files.asp' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/ccd/files.asp</a>.</p><div>Notes:</div><div><table border='1' cellpadding='0' cellspacing='0' style='border-collapse:collapse; border:none;'>\n <tbody><tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-1 or M</span></p>\n  </td>\n  <td style='width:233.75pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are missing.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-2 or N</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are not applicable.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-9</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data do not meet NCES data quality standards.</span></p>\n  </td>\n </tr>\n</tbody></table></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><p></p><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/9c46f665e0ec499a8a06e2f31f5831fd/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/9c46f665e0ec499a8a06e2f31f5831fd/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-characteristics-2017-18",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-characteristics-2017-18"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/School_District_Boundaries/EDGE_ADD_SchoolDistricts_SY1718/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/School_District_Boundaries/EDGE_ADD_SchoolDistricts_SY1718/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "School District Documentation",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_SDBOUNDARIES_COMPOSITE_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "School District Documentation"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "School District Characteristics 2017-18",
                     "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-characteristics-2017-18.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "School District Characteristics 2017-18"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9c46f665e0ec499a8a06e2f31f5831fd/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9c46f665e0ec499a8a06e2f31f5831fd/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9c46f665e0ec499a8a06e2f31f5831fd/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9c46f665e0ec499a8a06e2f31f5831fd/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9c46f665e0ec499a8a06e2f31f5831fd/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9c46f665e0ec499a8a06e2f31f5831fd/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9c46f665e0ec499a8a06e2f31f5831fd/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/9c46f665e0ec499a8a06e2f31f5831fd/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "9d11931a-642b-457b-86ee-e07b41bdba9c",
+            "issued": "2020-04-27T14:14:04.000Z",
             "keyword": [
                 "ccd",
                 "common-core-of-data",
@@ -16055,25 +16034,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:09.318500",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School District Characteristics 2020-21",
-            "description": "<p></p><p>The National Center for Education Statistics\u2019 (NCES) Education \nDemographic and Geographic Estimate (EDGE) program develops annually \nupdated school district boundary composite files that include public \nelementary, secondary, and unified school district boundaries clipped to\n the U.S. shoreline. School districts are special-purpose governments and administrative\n units designed by state and local officials to provide public education\n for local residents. District boundaries are collected for NCES by the \nU.S. Census Bureau to develop demographic estimates and to support \neducational research and program administration. The NCES Common Core of\n Data (CCD) program is an annual collection of basic administrative \ncharacteristics for all public schools, school districts, and state \neducation agencies in the United States. These characteristics are \nreported by state education officials and include directory information,\n number of students, number of teachers, grade span, and other \nconditions. The administrative attributes in this layer were developed \nfrom the 2020-2021 CCD collection. For more information about NCES \nschool district boundaries, see: <a href='https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries</a>. For more information about CCD school district attributes, see: <a href='https://nces.ed.gov/ccd/files.asp' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/ccd/files.asp</a>.</p><div>Notes:</div><div><table border='1' cellpadding='0' cellspacing='0' style='border-collapse:collapse; border:none;'>\n <tbody><tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-1 or M</span></p>\n  </td>\n  <td style='width:233.75pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are missing.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-2 or N</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are not applicable.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-9</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data do not meet NCES data quality standards.</span></p>\n  </td>\n </tr>\n</tbody></table></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><p></p><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></p>",
-            "modified": "2024-10-19T12:47:08.556663",
-            "accessLevel": "public",
-            "identifier": "8895030b-331a-4b35-8975-2346c6492b37",
-            "issued": "2022-06-13T14:58:38.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -16094,77 +16059,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "School District Characteristics 2017-18"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<p></p><p>The National Center for Education Statistics\u2019 (NCES) Education \nDemographic and Geographic Estimate (EDGE) program develops annually \nupdated school district boundary composite files that include public \nelementary, secondary, and unified school district boundaries clipped to\n the U.S. shoreline. School districts are special-purpose governments and administrative\n units designed by state and local officials to provide public education\n for local residents. District boundaries are collected for NCES by the \nU.S. Census Bureau to develop demographic estimates and to support \neducational research and program administration. The NCES Common Core of\n Data (CCD) program is an annual collection of basic administrative \ncharacteristics for all public schools, school districts, and state \neducation agencies in the United States. These characteristics are \nreported by state education officials and include directory information,\n number of students, number of teachers, grade span, and other \nconditions. The administrative attributes in this layer were developed \nfrom the 2020-2021 CCD collection. For more information about NCES \nschool district boundaries, see: <a href='https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries</a>. For more information about CCD school district attributes, see: <a href='https://nces.ed.gov/ccd/files.asp' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/ccd/files.asp</a>.</p><div>Notes:</div><div><table border='1' cellpadding='0' cellspacing='0' style='border-collapse:collapse; border:none;'>\n <tbody><tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-1 or M</span></p>\n  </td>\n  <td style='width:233.75pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are missing.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-2 or N</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are not applicable.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-9</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data do not meet NCES data quality standards.</span></p>\n  </td>\n </tr>\n</tbody></table></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><p></p><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/ca8a6ea2361049fdb48de07988f953ff/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/ca8a6ea2361049fdb48de07988f953ff/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-characteristics-2020-21",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-characteristics-2020-21"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/School_District_Boundaries/EDGE_ADMINDATA_SCHOOLDISTRICTS_SY2021/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/School_District_Boundaries/EDGE_ADMINDATA_SCHOOLDISTRICTS_SY2021/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "School District Documentation",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_SDBOUNDARIES_COMPOSITE_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "School District Documentation"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "School District Characteristics 2020-21",
                     "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-characteristics-2020-21.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "School District Characteristics 2020-21"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ca8a6ea2361049fdb48de07988f953ff/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ca8a6ea2361049fdb48de07988f953ff/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ca8a6ea2361049fdb48de07988f953ff/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ca8a6ea2361049fdb48de07988f953ff/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ca8a6ea2361049fdb48de07988f953ff/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ca8a6ea2361049fdb48de07988f953ff/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ca8a6ea2361049fdb48de07988f953ff/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/ca8a6ea2361049fdb48de07988f953ff/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "8895030b-331a-4b35-8975-2346c6492b37",
+            "issued": "2022-06-13T14:58:38.000Z",
             "keyword": [
                 "ccd",
                 "common-core-of-data",
@@ -16178,25 +16157,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:08.556663",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School District Characteristics 2019-20",
-            "description": "<p></p><p>The National Center for Education Statistics\u2019 (NCES) Education \nDemographic and Geographic Estimate (EDGE) program develops annually \nupdated school district boundary composite files that include public \nelementary, secondary, and unified school district boundaries clipped to\n the U.S. shoreline. School districts are special-purpose administrative\n units designed by state and local officials to provide public education\n for local residents. District boundaries are collected for NCES by the \nU.S. Census Bureau to develop demographic estimates and to support \neducational research and program administration. The NCES Common Core of\n Data (CCD) program is an annual collection of basic administrative \ncharacteristics for all public schools, school districts, and state \neducation agencies in the United States. These characteristics are \nreported by state education officials and include directory information,\n number of students, number of teachers, grade span, and other \nconditions. The administrative attributes in this layer were developed \nfrom the 2019-2020 CCD collection. For more information about NCES \nschool district boundaries, see: <a href='https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries</a>. For more information about CCD school district attributes, see: <a href='https://nces.ed.gov/ccd/files.asp' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/ccd/files.asp</a>.</p><div>Notes:</div><div><table border='1' cellpadding='0' cellspacing='0' style='border-collapse:collapse; border:none;'>\n <tbody><tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-1 or M</span></p>\n  </td>\n  <td style='width:233.75pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are missing.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-2 or N</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are not applicable.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-9</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data do not meet NCES data quality standards.</span></p>\n  </td>\n </tr>\n</tbody></table></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><p></p><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></p>",
-            "modified": "2024-10-19T12:47:07.606024",
-            "accessLevel": "public",
-            "identifier": "36e0a1c7-ae20-4fbb-9e16-8cea1148d6f0",
-            "issued": "2021-08-24T19:05:42.000Z",
-            "license": "https://resources.data.gov/open-licenses/",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -16217,77 +16182,91 @@
                     }
                 }
             },
+            "theme": [
+                "geospatial"
+            ],
+            "title": "School District Characteristics 2020-21"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "nces",
                 "hasEmail": "mailto:nces@ed.gov"
             },
+            "description": "<p></p><p>The National Center for Education Statistics\u2019 (NCES) Education \nDemographic and Geographic Estimate (EDGE) program develops annually \nupdated school district boundary composite files that include public \nelementary, secondary, and unified school district boundaries clipped to\n the U.S. shoreline. School districts are special-purpose administrative\n units designed by state and local officials to provide public education\n for local residents. District boundaries are collected for NCES by the \nU.S. Census Bureau to develop demographic estimates and to support \neducational research and program administration. The NCES Common Core of\n Data (CCD) program is an annual collection of basic administrative \ncharacteristics for all public schools, school districts, and state \neducation agencies in the United States. These characteristics are \nreported by state education officials and include directory information,\n number of students, number of teachers, grade span, and other \nconditions. The administrative attributes in this layer were developed \nfrom the 2019-2020 CCD collection. For more information about NCES \nschool district boundaries, see: <a href='https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/programs/edge/Geographic/DistrictBoundaries</a>. For more information about CCD school district attributes, see: <a href='https://nces.ed.gov/ccd/files.asp' target='_blank' rel='nofollow ugc noopener noreferrer'>https://nces.ed.gov/ccd/files.asp</a>.</p><div>Notes:</div><div><table border='1' cellpadding='0' cellspacing='0' style='border-collapse:collapse; border:none;'>\n <tbody><tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-1 or M</span></p>\n  </td>\n  <td style='width:233.75pt; border:solid windowtext 1.0pt; border-left:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are missing.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-2 or N</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data are not applicable.</span></p>\n  </td>\n </tr>\n <tr>\n  <td style='width:71.75pt; border:solid windowtext 1.0pt; border-top:none; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='96'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>-9</span></p>\n  </td>\n  <td style='width:233.75pt; border-top:none; border-left:none; border-bottom:solid windowtext 1.0pt; border-right:solid windowtext 1.0pt; padding:0in 5.4pt 0in 5.4pt;' valign='top' width='312'>\n  <p style='margin-bottom:0in;'><span style='font-size:12.0pt;'>Indicates that the data do not meet NCES data quality standards.</span></p>\n  </td>\n </tr>\n</tbody></table></div><div style='font-family:&quot;Avenir Next W01&quot;, &quot;Avenir Next W00&quot;, &quot;Avenir Next&quot;, Avenir, &quot;Helvetica Neue&quot;, sans-serif; font-size:16px;'><br /></div><p></p><p>All information contained in this file is in the public domain. Data users are advised to review NCES program documentation and feature class metadata to understand the limitations and appropriate use of these data.<br /></p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/xml",
-                    "format": "XML",
-                    "title": "Original ISO-19139 metadata",
                     "conformsTo": "https://www.isotc211.org/2005/gmi",
-                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/43b42be85c4749e48267f83f1f6ffa60/info/metadata/metadata.xml?format=iso19139"
+                    "downloadURL": "https://www.arcgis.com/sharing/rest/content/items/43b42be85c4749e48267f83f1f6ffa60/info/metadata/metadata.xml?format=iso19139",
+                    "format": "XML",
+                    "mediaType": "text/xml",
+                    "title": "Original ISO-19139 metadata"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-characteristics-2019-20",
                     "format": "HTML",
-                    "title": "ArcGIS Hub Dataset",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-characteristics-2019-20"
+                    "mediaType": "text/html",
+                    "title": "ArcGIS Hub Dataset"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/json",
+                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/School_District_Boundaries/EDGE_ADMINDATA_SCHOOLDISTRICTS_SY1920/MapServer/0",
                     "format": "ArcGIS GeoServices REST API",
-                    "title": "ArcGIS GeoService",
-                    "downloadURL": "https://nces.ed.gov/opengis/rest/services/School_District_Boundaries/EDGE_ADMINDATA_SCHOOLDISTRICTS_SY1920/MapServer/0"
+                    "mediaType": "application/json",
+                    "title": "ArcGIS GeoService"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "PDF",
-                    "title": "School District Documentation",
                     "downloadURL": "https://nces.ed.gov/programs/edge/docs/EDGE_SDBOUNDARIES_COMPOSITE_FILEDOC.pdf",
-                    "mediaType": "text/plain"
+                    "format": "PDF",
+                    "mediaType": "text/plain",
+                    "title": "School District Documentation"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "ZIP",
-                    "title": "School District Characteristics 2019-20",
                     "downloadURL": "https://data-nces.opendata.arcgis.com/datasets/nces::school-district-characteristics-2019-20.zip",
-                    "mediaType": "text/plain"
+                    "format": "ZIP",
+                    "mediaType": "text/plain",
+                    "title": "School District Characteristics 2019-20"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/43b42be85c4749e48267f83f1f6ffa60/csv?layers=0",
                     "format": "CSV",
-                    "title": "CSV",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/43b42be85c4749e48267f83f1f6ffa60/csv?layers=0"
+                    "mediaType": "text/csv",
+                    "title": "CSV"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.geo+json",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/43b42be85c4749e48267f83f1f6ffa60/geojson?layers=0",
                     "format": "GeoJSON",
-                    "title": "GeoJSON",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/43b42be85c4749e48267f83f1f6ffa60/geojson?layers=0"
+                    "mediaType": "application/vnd.geo+json",
+                    "title": "GeoJSON"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/43b42be85c4749e48267f83f1f6ffa60/shapefile?layers=0",
                     "format": "ZIP",
-                    "title": "Shapefile",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/43b42be85c4749e48267f83f1f6ffa60/shapefile?layers=0"
+                    "mediaType": "application/zip",
+                    "title": "Shapefile"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/43b42be85c4749e48267f83f1f6ffa60/kml?layers=0",
                     "format": "KML",
-                    "title": "KML",
-                    "downloadURL": "https://data-nces.opendata.arcgis.com/api/download/v1/items/43b42be85c4749e48267f83f1f6ffa60/kml?layers=0"
+                    "mediaType": "application/vnd.google-earth.kml+xml",
+                    "title": "KML"
                 }
             ],
+            "identifier": "36e0a1c7-ae20-4fbb-9e16-8cea1148d6f0",
+            "issued": "2021-08-24T19:05:42.000Z",
             "keyword": [
                 "ccd",
                 "common-core-of-data",
@@ -16301,25 +16280,11 @@
                 "united-states",
                 "us-census-bureau"
             ],
-            "bureauCode": [
-                "018:15"
-            ],
+            "license": "https://resources.data.gov/open-licenses/",
+            "modified": "2024-10-19T12:47:07.606024",
             "programCode": [
                 "018:000"
             ],
-            "theme": [
-                "geospatial"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School District Characteristics - Current",
```

