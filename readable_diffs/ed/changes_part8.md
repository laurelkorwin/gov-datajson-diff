# Change History for ed.json (Part 8)

### Changes from 31606f9 to dd2190f (Part 8/13)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -69312,30 +69271,48 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/surveys/frss/download/data/f68doc.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/sorn/18-13-01_060499.pdf",
+            "temporal": "1998/1999",
+            "title": "Advanced Telecommunications in U.S. Private Schools, 1998-99"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "Vocational Programs in Secondary Schools, 1999 (FRSS 72), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at https://nces.ed.gov/surveys/frss/downloads.asp. FRSS 72 https://nces.ed.gov/surveys/frss/index.asp is a cross-sectional survey that collected information from secondary schools in the United States about availability of vocational education programs and courses. This study was conducted using surveys of secondary school principals. 1,150 secondary schools in the United States were sampled. The study's unweighted response rate was 94 percent. The weighted response rate was 95 percent. Key statistics produced from FRSS 72 are on program offerings, relevant job skills, skill competency lists, and credentialing process.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "f72data.zip",
                     "description": "Vocational Programs in Secondary Schools, 1999 data as a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f72data.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f72data.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "f72data.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "f72sas.zip",
                     "description": "Vocational Programs in Secondary Schools, 1999 data as a zipped SAS file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f72sas.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f72sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "f72sas.zip"
                 }
             ],
+            "identifier": "b0631b9f-3f93-46e3-bb57-14fda5a6236b",
+            "issued": "2003-05-06",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "comprehensive-schools",
@@ -69352,32 +69329,14 @@
                 "vocational-programs",
                 "vocational-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/surveys/frss/download/data/f72doc.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Service-Learning and Community Service in K-12 Public Schools, 1999",
-            "description": "Service-Learning and Community Service in K-12 Public Schools, 1999 (FRSS 71), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at https://nces.ed.gov/surveys/frss/downloads.asp. FRSS 71 https://nces.ed.gov/surveys/frss/index.asp is a cross-sectional study that was designed to assess the prevalence and support for service-learning programs in K-12 schools across the nation. This study was conducted using surveys of elementary, middle, and secondary/combined school principals. Public elementary schools (200), middle schools (500), and secondary/combined schools (1,300) were sampled. The study's unweighted response rate was 92 percent and the weighted response rate was 93 percent. Key statistics produced from FRSS 71 were on the prevalence of service-learning activities in K-12 schools.",
-            "modified": "2023-06-27T18:01:54.473784",
-            "accessLevel": "public",
-            "identifier": "0667d3a8-f4c1-4171-86ca-253f41a7fe57",
-            "dataQuality": true,
-            "issued": "2003-05-06",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/sorn/18-13-01_060499.pdf",
-            "temporal": "1998/1999",
+            "modified": "2023-06-27T18:02:42.159955",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -69398,30 +69357,48 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/surveys/frss/download/data/f72doc.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/sorn/18-13-01_060499.pdf",
+            "temporal": "1998/1999",
+            "title": "Vocational Programs in Secondary Schools, 1999"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "Service-Learning and Community Service in K-12 Public Schools, 1999 (FRSS 71), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at https://nces.ed.gov/surveys/frss/downloads.asp. FRSS 71 https://nces.ed.gov/surveys/frss/index.asp is a cross-sectional study that was designed to assess the prevalence and support for service-learning programs in K-12 schools across the nation. This study was conducted using surveys of elementary, middle, and secondary/combined school principals. Public elementary schools (200), middle schools (500), and secondary/combined schools (1,300) were sampled. The study's unweighted response rate was 92 percent and the weighted response rate was 93 percent. Key statistics produced from FRSS 71 were on the prevalence of service-learning activities in K-12 schools.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "f71data.zip",
                     "description": "Service-Learning and Community Service in K-12 Public Schools, 1999 data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f71data.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f71data.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "f71data.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "f71sas.zip",
                     "description": "Service-Learning and Community Service in K-12 Public Schools, 1999 data in a zipped SAS file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f71sas.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f71sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "f71sas.zip"
                 }
             ],
+            "identifier": "0667d3a8-f4c1-4171-86ca-253f41a7fe57",
+            "issued": "2003-05-06",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "community-service",
@@ -69440,32 +69417,14 @@
                 "secondarycombined-schools",
                 "service-learning"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/surveys/frss/download/data/f71doc.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Condition of America's Public School Facilities, 1999",
-            "description": "The Condition of America's Public School Facilities, 1999 (FRSS 73), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 73 (https://nces.ed.gov/surveys/frss/) is a cross-sectional survey that collects and report data on key issues at public elementary and secondary schools in the United States. The sample for FRSS 73 included approximately 1000 public elementary, middle, and high schools. District personnel who were familiar with the condition of schools completed questionnaires for each sampled school in their districts. The study's weighted response rate was 91 percent. Key statistics produced from FRSS 73 provide information on the pervasiveness of air conditioning, the number of temporary classrooms, the number of days particular public schools were closed for repairs, planned construction, repairs, and additions, long range facilities plans, the age of public schools, overcrowding and practices used to address overcrowding, estimated costs for bringing facilities to a satisfactory condition, and the overall condition of roofs, floors, walls, plumbing, heating, electric facilities, and safety features.",
-            "modified": "2023-06-27T17:59:39.411236",
-            "accessLevel": "public",
-            "identifier": "efb4af0b-50e6-4248-9ae9-5e478d37422f",
-            "dataQuality": true,
-            "issued": "2003-05-06",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "1999/P1Y",
+            "modified": "2023-06-27T18:01:54.473784",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -69486,30 +69445,48 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/surveys/frss/download/data/f71doc.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/sorn/18-13-01_060499.pdf",
+            "temporal": "1998/1999",
+            "title": "Service-Learning and Community Service in K-12 Public Schools, 1999"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Condition of America's Public School Facilities, 1999 (FRSS 73), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 73 (https://nces.ed.gov/surveys/frss/) is a cross-sectional survey that collects and report data on key issues at public elementary and secondary schools in the United States. The sample for FRSS 73 included approximately 1000 public elementary, middle, and high schools. District personnel who were familiar with the condition of schools completed questionnaires for each sampled school in their districts. The study's weighted response rate was 91 percent. Key statistics produced from FRSS 73 provide information on the pervasiveness of air conditioning, the number of temporary classrooms, the number of days particular public schools were closed for repairs, planned construction, repairs, and additions, long range facilities plans, the age of public schools, overcrowding and practices used to address overcrowding, estimated costs for bringing facilities to a satisfactory condition, and the overall condition of roofs, floors, walls, plumbing, heating, electric facilities, and safety features.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "f73data.zip",
                     "description": "Condition of America's Public School Facilities, 1999 data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f73data.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f73data.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "f73data.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "f73sas.zip",
                     "description": "Condition of America's Public School Facilities, 1999 data in a zipped SAS file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f73sas.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f73sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "f73sas.zip"
                 }
             ],
+            "identifier": "efb4af0b-50e6-4248-9ae9-5e478d37422f",
+            "issued": "2003-05-06",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "conditions",
@@ -69520,32 +69497,14 @@
                 "public-schools",
                 "schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/surveys/frss/download/data/f73doc.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Distance Education Courses for Public Elementary and Secondary School Students, 2003",
-            "description": "Distance Education Courses for Public Elementary and Secondary School Students, 2003 (FRSS 84), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 84 (https://nces.ed.gov/surveys/frss/) is a cross-sectional survey that provides national estimates on distance education courses in public school districts, including enrollment in distance education courses, how districts monitor these courses, the motivations for providing distance education, and the technologies used for delivering distance education. Superintendents of sampled public school districts received a paper questionnaire in the mail and were instructed that the staff member most knowledgeable about the district's distance education practices should complete it. The study's weighted response rate was 96 percent. Key statistics produced from FRSS 84 are information on the prevalence of technology-based distance education courses, enrollments of public elementary and secondary school students in distance education courses, the types of technologies most commonly used for delivering distance education courses, districts' reasons for having distance education courses, and factors districts report that prevent their expansion of distance education course offerings.",
-            "modified": "2023-06-27T17:57:50.993643",
-            "accessLevel": "public",
-            "identifier": "5009b303-eb2f-43e9-a499-a3b6c4b0cfeb",
-            "dataQuality": true,
-            "issued": "2007-04-04",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2003/2004",
+            "modified": "2023-06-27T17:59:39.411236",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -69566,30 +69525,48 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/surveys/frss/download/data/f73doc.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "1999/P1Y",
+            "title": "Condition of America's Public School Facilities, 1999"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "Distance Education Courses for Public Elementary and Secondary School Students, 2003 (FRSS 84), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 84 (https://nces.ed.gov/surveys/frss/) is a cross-sectional survey that provides national estimates on distance education courses in public school districts, including enrollment in distance education courses, how districts monitor these courses, the motivations for providing distance education, and the technologies used for delivering distance education. Superintendents of sampled public school districts received a paper questionnaire in the mail and were instructed that the staff member most knowledgeable about the district's distance education practices should complete it. The study's weighted response rate was 96 percent. Key statistics produced from FRSS 84 are information on the prevalence of technology-based distance education courses, enrollments of public elementary and secondary school students in distance education courses, the types of technologies most commonly used for delivering distance education courses, districts' reasons for having distance education courses, and factors districts report that prevent their expansion of distance education course offerings.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "f84data.zip",
                     "description": "Distance Education Courses for Public Elementary and Secondary School Students, 2003 data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f84data.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f84data.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "f84data.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "f84sas.zip",
                     "description": "Distance Education Courses for Public Elementary and Secondary School Students, 2003 data in a zipped SAS file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f84sas.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f84sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "f84sas.zip"
                 }
             ],
+            "identifier": "5009b303-eb2f-43e9-a499-a3b6c4b0cfeb",
+            "issued": "2007-04-04",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "courses-offerings",
@@ -69602,32 +69579,14 @@
                 "secondary",
                 "telecommunications"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/surveys/frss/download/data/f84doc.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Internet Access in U.S. Public Schools, 2003",
-            "description": "Internet Access in U.S. Public Schools, 2003 (FRSS 86), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at https://nces.ed.gov/surveys/frss/downloads.asp. FRSS 86 (https://nces.ed.gov/surveys/frss/) is a cross-sectional survey that collects and reports data on key education issues at the elementary and secondary levels. The study was conducted using questionnaires of principals. Schools in September 2003 were sampled. The study's response rate was 91 percent. Key statistics produced from FRSS 86 will gauge the progress that public schools have made since 1994 in internet accessibility and connectivity, and to explore continuing challenges in incorporating the internet as an educational tool.",
-            "modified": "2023-06-27T17:57:08.452684",
-            "accessLevel": "public",
-            "identifier": "c6d53b23-62ea-4fe5-b7a0-25cd1c7bfbbb",
-            "dataQuality": true,
-            "issued": "2007-06-06",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2003/2004",
+            "modified": "2023-06-27T17:57:50.993643",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -69648,30 +69607,48 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/surveys/frss/download/data/f84doc.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2003/2004",
+            "title": "Distance Education Courses for Public Elementary and Secondary School Students, 2003"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "Internet Access in U.S. Public Schools, 2003 (FRSS 86), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at https://nces.ed.gov/surveys/frss/downloads.asp. FRSS 86 (https://nces.ed.gov/surveys/frss/) is a cross-sectional survey that collects and reports data on key education issues at the elementary and secondary levels. The study was conducted using questionnaires of principals. Schools in September 2003 were sampled. The study's response rate was 91 percent. Key statistics produced from FRSS 86 will gauge the progress that public schools have made since 1994 in internet accessibility and connectivity, and to explore continuing challenges in incorporating the internet as an educational tool.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "f86data.zip",
                     "description": "Internet Access in U.S. Public Schools, 2003 data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f86data.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f86data.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "f86data.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "f86sas.zip",
                     "description": "Internet Access in U.S. Public Schools, 2003 data in a zipped SAS file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f86sas.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f86sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "f86sas.zip"
                 }
             ],
+            "identifier": "c6d53b23-62ea-4fe5-b7a0-25cd1c7bfbbb",
+            "issued": "2007-06-06",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "computers",
@@ -69683,32 +69660,14 @@
                 "teachers",
                 "technology"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/surveys/frss/download/data/f86doc.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Dual-Credit and Exam-Based Courses, 2003",
-            "description": "The Dual-Credit and Exam-Based Courses, 2003 (FRSS 85), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at https://nces.ed.gov/surveys/frss/downloads.asp. FRSS 85 (https://nces.ed.gov/surveys/frss/) is a cross-sectional survey that collects and reports data on key education issues at the secondary level. The study was conducted using questionnaires of principals. Schools in September 2003 were sampled. The study's response rate was 92 percent. Key statistics produced from FRSS 85 will provide education policymakers with important baseline information about the prevalence and characteristics of dual credit courses.",
-            "modified": "2023-06-27T17:56:10.639212",
-            "accessLevel": "public",
-            "identifier": "d3cce408-869e-417b-9ab9-f58e848dd07d",
-            "dataQuality": true,
-            "issued": "2009-02-10",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2002/2003",
+            "modified": "2023-06-27T17:57:08.452684",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -69729,30 +69688,48 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/surveys/frss/download/data/f86doc.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2003/2004",
+            "title": "Internet Access in U.S. Public Schools, 2003"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Dual-Credit and Exam-Based Courses, 2003 (FRSS 85), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at https://nces.ed.gov/surveys/frss/downloads.asp. FRSS 85 (https://nces.ed.gov/surveys/frss/) is a cross-sectional survey that collects and reports data on key education issues at the secondary level. The study was conducted using questionnaires of principals. Schools in September 2003 were sampled. The study's response rate was 92 percent. Key statistics produced from FRSS 85 will provide education policymakers with important baseline information about the prevalence and characteristics of dual credit courses.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "f85dat.zip",
                     "description": "Dual-Credit and Exam-Based Courses, 2003 data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f85dat.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f85dat.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "f85dat.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "f85sas.zip",
                     "description": "Dual-Credit and Exam-Based Courses, 2003 data in a zipped SAS file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f85sas.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f85sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "f85sas.zip"
                 }
             ],
+            "identifier": "d3cce408-869e-417b-9ab9-f58e848dd07d",
+            "issued": "2009-02-10",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "college-credit",
@@ -69764,32 +69741,14 @@
                 "high-school",
                 "postsecondary"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/surveys/frss/download/data/f85doc.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Foods and Physical Activity in Public Elementary Schools, 2005",
-            "description": "The Foods and Physical Activity in Public Elementary Schools, 2005 (FRSS 87), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 87 (https://nces.ed.gov/surveys/frss/) is a sample survey that was designed to obtain current national information on availability of foods and opportunities for exercise in public elementary schools. Questionnaires were mailed to the principals of each sampled school.  Respondents had the option of completing paper-and-pencil or web-based questionnaires. The study's weighted response rate was 91 percent. Key statistics produced from the study were  types of food sold at one or more locations in their schools and in their cafeterias or lunchrooms; the types of food sold at vending machines and school stores or snack bars, and times when foods were available at those locations; food service operations and contracts with companies to sell foods at schools; scheduled recess, including the days per week, times per day, and minutes per day of recess; scheduled physical education, including the days per week, class length, and average minutes per week of physical education; activities to encourage physical activity among elementary students; and the physical assessment of students.",
-            "modified": "2023-06-27T17:55:01.728544",
-            "accessLevel": "public",
-            "identifier": "2bd232a3-5fcc-4136-a63b-0a2d6d5a9b5e",
-            "dataQuality": true,
-            "issued": "2007-01-04",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2004/2005",
+            "modified": "2023-06-27T17:56:10.639212",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -69810,30 +69769,48 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/surveys/frss/download/data/f85doc.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2002/2003",
+            "title": "Dual-Credit and Exam-Based Courses, 2003"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Foods and Physical Activity in Public Elementary Schools, 2005 (FRSS 87), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 87 (https://nces.ed.gov/surveys/frss/) is a sample survey that was designed to obtain current national information on availability of foods and opportunities for exercise in public elementary schools. Questionnaires were mailed to the principals of each sampled school.  Respondents had the option of completing paper-and-pencil or web-based questionnaires. The study's weighted response rate was 91 percent. Key statistics produced from the study were  types of food sold at one or more locations in their schools and in their cafeterias or lunchrooms; the types of food sold at vending machines and school stores or snack bars, and times when foods were available at those locations; food service operations and contracts with companies to sell foods at schools; scheduled recess, including the days per week, times per day, and minutes per day of recess; scheduled physical education, including the days per week, class length, and average minutes per week of physical education; activities to encourage physical activity among elementary students; and the physical assessment of students.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "f87data.zip",
                     "description": "Foods and Physical Activity in Public Elementary Schools, 2005 data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f87data.zip"
-                },
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f87data.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "f87data.zip"
+                },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "f87sas.zip",
                     "description": "Foods and Physical Activity in Public Elementary Schools, 2005 data in a zipped SAS file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f87sas.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f87sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "f87sas.zip"
                 }
             ],
+            "identifier": "2bd232a3-5fcc-4136-a63b-0a2d6d5a9b5e",
+            "issued": "2007-01-04",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "elementary-schools",
@@ -69842,32 +69819,14 @@
                 "nutrition",
                 "physical-education"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/surveys/frss/download/data/f87doc.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Public School Principals' Perceptions of Their School Facilities, 2005",
-            "description": "The Public School Principals' Perceptions of Their School Facilities, Fall 2005 (FRSS 88), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 88 (https://nces.ed.gov/surveys/frss/) is a cross-sectional survey that collects and report data on principals' perceptions of their school facilities at the elementary and secondary levels. Principals in sampled schools received questionnaires regarding the condition of their school facilities. Respondents had the option of completing paper or web-based questionnaires. The study's response weighted rate was 91 percent. Key statistics produced from FRSS 88 will provide current information about principals' satisfaction with various environmental factors in their schools and the extent to which they perceive those factors as interfering with the ability of the school to deliver instruction.",
-            "modified": "2023-06-27T17:50:18.233055",
-            "accessLevel": "public",
-            "identifier": "9c12d206-b55e-40be-ba0f-dc82a0de743a",
-            "dataQuality": true,
-            "issued": "2008-03-26",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2005/2006",
+            "modified": "2023-06-27T17:55:01.728544",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -69888,30 +69847,48 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/surveys/frss/download/data/f87doc.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2004/2005",
+            "title": "Foods and Physical Activity in Public Elementary Schools, 2005"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Public School Principals' Perceptions of Their School Facilities, Fall 2005 (FRSS 88), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 88 (https://nces.ed.gov/surveys/frss/) is a cross-sectional survey that collects and report data on principals' perceptions of their school facilities at the elementary and secondary levels. Principals in sampled schools received questionnaires regarding the condition of their school facilities. Respondents had the option of completing paper or web-based questionnaires. The study's response weighted rate was 91 percent. Key statistics produced from FRSS 88 will provide current information about principals' satisfaction with various environmental factors in their schools and the extent to which they perceive those factors as interfering with the ability of the school to deliver instruction.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "f88dat.zip",
                     "description": "Public School Principals' Perceptions of Their School Facilities, 2005 data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f88dat.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f88dat.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "f88dat.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "f88sas.zip",
                     "description": "Public School Principals' Perceptions of Their School Facilities, 2005 data in a zipped SAS file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f88sas.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f88sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "f88sas.zip"
                 }
             ],
+            "identifier": "9c12d206-b55e-40be-ba0f-dc82a0de743a",
+            "issued": "2008-03-26",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "elementary-schools",
@@ -69922,32 +69899,14 @@
                 "school-overcrowding",
                 "secondary-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/surveys/frss/download/data/f88doc.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "After-School Programs at Public Elementary Schools, 2008",
-            "description": "The After-School Programs at Public Elementary Schools, 2008 (FRSS 91), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 91 (https://nces.ed.gov/surveys/frss/) is a sample survey that provides a national profile of various types of formal after-school programs physically located at public elementary schools in 2008. These programs include stand-alone programs that focus primarily on a single type of service (e.g., only day care) and broad-based programs that provide a combination of services such as academic enrichment and cultural activities. The study was conducted using surveys via web or by mail. Principals of public elementary schools were sampled. The study's weighted response rate was 91 percent. Key statistics produced from FRSS 91 were program focus (if applicable), number of students enrolled, hours per week the program operates, availability of transportation for students, whether students from other schools attend the program, and factors that may hinder students from participating in the program.",
-            "modified": "2023-06-27T17:47:08.598390",
-            "accessLevel": "public",
-            "identifier": "1a5494ab-de44-448b-be2b-548c07628082",
-            "dataQuality": true,
-            "issued": "2009-08-04",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2007/2008",
+            "modified": "2023-06-27T17:50:18.233055",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -69968,30 +69927,48 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/surveys/frss/download/data/f88doc.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2005/2006",
+            "title": "Public School Principals' Perceptions of Their School Facilities, 2005"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The After-School Programs at Public Elementary Schools, 2008 (FRSS 91), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 91 (https://nces.ed.gov/surveys/frss/) is a sample survey that provides a national profile of various types of formal after-school programs physically located at public elementary schools in 2008. These programs include stand-alone programs that focus primarily on a single type of service (e.g., only day care) and broad-based programs that provide a combination of services such as academic enrichment and cultural activities. The study was conducted using surveys via web or by mail. Principals of public elementary schools were sampled. The study's weighted response rate was 91 percent. Key statistics produced from FRSS 91 were program focus (if applicable), number of students enrolled, hours per week the program operates, availability of transportation for students, whether students from other schools attend the program, and factors that may hinder students from participating in the program.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "f91data.zip",
                     "description": "After-School Programs at Public Elementary Schools, 2008 data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f91data.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f91data.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "f91data.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "f91sas.zip",
                     "description": "After-School Programs at Public Elementary Schools, 2008 data in a zipped SAS file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f91sas.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f91sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "f91sas.zip"
                 }
             ],
+            "identifier": "1a5494ab-de44-448b-be2b-548c07628082",
+            "issued": "2009-08-04",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "21st-century-community-learning-centers",
@@ -70001,32 +69978,14 @@
                 "fast-response-survey-system",
                 "frss"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/surveys/frss/download/data/f91doc.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Internet Access in U.S. Public Schools, 2005",
-            "description": "Internet Access in U.S. Public Schools, 2005 (FRSS 90), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 90 (https://nces.ed.gov/surveys/frss/) is a sample survey that provides trend analysis on the percent of public schools and instructional rooms with internet access and on the ratio of students to instructional computers with Internet access. The study was conducted using mailed questionnaires or the option of completing the survey via the web. Principals of various public schools were sampled. The study's response rate was 86 percent. Key statistics produced from FRSS 90 were the number of instructional computers with access to the internet, the types of internet connections, technologies and procedures used to prevent student access to inappropriate material on the internet, and the availability of hand-held and laptop computers for students and teachers. Respondents also provided information on teacher professional development on how to integrate the use of the internet into the curriculum and on the use of the internet to provide opportunities and information for teaching and learning.",
-            "modified": "2023-06-27T17:46:02.866251",
-            "accessLevel": "public",
-            "identifier": "1796faad-bfa6-420f-8df0-3f481c391259",
-            "dataQuality": true,
-            "issued": "2007-04-04",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2005/2006",
+            "modified": "2023-06-27T17:47:08.598390",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -70047,30 +70006,48 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/surveys/frss/download/data/f91doc.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2007/2008",
+            "title": "After-School Programs at Public Elementary Schools, 2008"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "Internet Access in U.S. Public Schools, 2005 (FRSS 90), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 90 (https://nces.ed.gov/surveys/frss/) is a sample survey that provides trend analysis on the percent of public schools and instructional rooms with internet access and on the ratio of students to instructional computers with Internet access. The study was conducted using mailed questionnaires or the option of completing the survey via the web. Principals of various public schools were sampled. The study's response rate was 86 percent. Key statistics produced from FRSS 90 were the number of instructional computers with access to the internet, the types of internet connections, technologies and procedures used to prevent student access to inappropriate material on the internet, and the availability of hand-held and laptop computers for students and teachers. Respondents also provided information on teacher professional development on how to integrate the use of the internet into the curriculum and on the use of the internet to provide opportunities and information for teaching and learning.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "f90data.zip",
                     "description": "Internet Access in U.S. Public Schools, 2005 data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f90data.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f90data.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "f90data.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "f90sas.zip",
                     "description": "Internet Access in U.S. Public Schools, 2005 data in a zipped SAS file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f90sas.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f90sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "f90sas.zip"
                 }
             ],
+            "identifier": "1796faad-bfa6-420f-8df0-3f481c391259",
+            "issued": "2007-04-04",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "computers",
@@ -70081,32 +70058,14 @@
                 "professional-development",
                 "secondary-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/surveys/frss/download/data/f90doc.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Educational Technology in Public Schools, 2008",
-            "description": "Educational Technology in Public Schools, 2008 (FRSS 92), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 92 (https://nces.ed.gov/surveys/frss/) is a sample survey that provides national estimates on the availability and use of educational technology in public elementary and secondary schools during fall 2008. This is one of a set of three surveys (at the district, school, and teacher levels) that collected data on a range of educational technology resources. The study was conducted using mailed questionnaires and respondents had the option of completing the survey via the web. Schools were sampled. The study's weighted response rate was 79 percent. Key statistics produced from FRSS 92 were information on computer hardware and internet access, availability of staff to help integrate technology into instruction and provide timely technical support, and perceptions of educational technology issues at the school and district levels. Respondents reported the number of instructional computers within their schools, by type, mobility, and location. The survey also asked respondents about the types of operating systems or platforms used on instructional computers. Data on the number of handheld devices provided to school personnel and students, and the number of other technology devices provided for instructional purposes were also collected. Respondents indicated the extent to which technology staff provided assistance with technology support and integration and the response times for obtaining such support. Respondents gave opinions on statements related to using educational technology in their schools.",
-            "modified": "2023-06-27T17:44:58.749372",
-            "accessLevel": "public",
-            "identifier": "c3c0ea47-b951-4a98-aace-b00bf0e58774",
-            "dataQuality": true,
-            "issued": "2010-05-06",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2008/2009",
+            "modified": "2023-06-27T17:46:02.866251",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -70127,30 +70086,48 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/surveys/frss/download/data/f90doc.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2005/2006",
+            "title": "Internet Access in U.S. Public Schools, 2005"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "Educational Technology in Public Schools, 2008 (FRSS 92), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 92 (https://nces.ed.gov/surveys/frss/) is a sample survey that provides national estimates on the availability and use of educational technology in public elementary and secondary schools during fall 2008. This is one of a set of three surveys (at the district, school, and teacher levels) that collected data on a range of educational technology resources. The study was conducted using mailed questionnaires and respondents had the option of completing the survey via the web. Schools were sampled. The study's weighted response rate was 79 percent. Key statistics produced from FRSS 92 were information on computer hardware and internet access, availability of staff to help integrate technology into instruction and provide timely technical support, and perceptions of educational technology issues at the school and district levels. Respondents reported the number of instructional computers within their schools, by type, mobility, and location. The survey also asked respondents about the types of operating systems or platforms used on instructional computers. Data on the number of handheld devices provided to school personnel and students, and the number of other technology devices provided for instructional purposes were also collected. Respondents indicated the extent to which technology staff provided assistance with technology support and integration and the response times for obtaining such support. Respondents gave opinions on statements related to using educational technology in their schools.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "f92data.zip",
                     "description": "Educational Technology in Public Schools, 2008 data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f92data.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f92data.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "f92data.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "f92sas.zip",
                     "description": "Educational Technology in Public Schools, 2008 data in a zipped SAS file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f92sas.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f92sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "f92sas.zip"
                 }
             ],
+            "identifier": "c3c0ea47-b951-4a98-aace-b00bf0e58774",
+            "issued": "2010-05-06",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "computer-networks",
@@ -70160,32 +70137,14 @@
                 "frss",
                 "teacher-professional-development"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/surveys/frss/download/data/f92doc.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Teachers' Use of Educational Technology in U.S. Public Schools, 2009",
-            "description": "Teachers' Use of Educational Technology in U.S. Public Schools, 2009 (FRSS 95), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 95 (https://nces.ed.gov/surveys/frss/) is a sample survey that provides national estimates on the availability and use of educational technology among teachers in public elementary and secondary schools during 2009. This is one of a set of three surveys (at the district, school, and teacher levels) that collected data on a range of educational technology resources. The study was conducted using surveys via the web or by mail. Telephone follow-up for survey non-response and data clarification was also used. Questionnaires and cover letters for the teacher survey were mailed to sampled teachers at their schools. Public schools and teachers within those schools were sampled. The weighted response rate for schools providing lists of teachers for sampling was 81 percent, and the weighted response rate for sampled teachers completing questionnaires was 79 percent. Key statistics produced from FRSS 95 were information on the use of computers and internet access in the classroom; availability and use of computing devices, software, and school or district networks (including remote access) by teachers; students' use of educational technology; teachers' preparation to use educational technology for instruction; and technology-related professional development activities.",
-            "modified": "2023-06-27T17:43:43.264214",
-            "accessLevel": "public",
-            "identifier": "f6dccc8f-448d-4189-a5ee-e432f23bd720",
-            "dataQuality": true,
-            "issued": "2010-05-06",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2008/2009",
+            "modified": "2023-06-27T17:44:58.749372",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -70206,62 +70165,62 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/surveys/frss/download/data/f92doc.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2008/2009",
+            "title": "Educational Technology in Public Schools, 2008"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "Teachers' Use of Educational Technology in U.S. Public Schools, 2009 (FRSS 95), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 95 (https://nces.ed.gov/surveys/frss/) is a sample survey that provides national estimates on the availability and use of educational technology among teachers in public elementary and secondary schools during 2009. This is one of a set of three surveys (at the district, school, and teacher levels) that collected data on a range of educational technology resources. The study was conducted using surveys via the web or by mail. Telephone follow-up for survey non-response and data clarification was also used. Questionnaires and cover letters for the teacher survey were mailed to sampled teachers at their schools. Public schools and teachers within those schools were sampled. The weighted response rate for schools providing lists of teachers for sampling was 81 percent, and the weighted response rate for sampled teachers completing questionnaires was 79 percent. Key statistics produced from FRSS 95 were information on the use of computers and internet access in the classroom; availability and use of computing devices, software, and school or district networks (including remote access) by teachers; students' use of educational technology; teachers' preparation to use educational technology for instruction; and technology-related professional development activities.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "f95data.zip",
                     "description": "Teachers' Use of Educational Technology in U.S. Public Schools, 2009 data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f95data.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f95data.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "f95data.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "f95sas.zip",
                     "description": "Teachers' Use of Educational Technology in U.S. Public Schools, 2009 data in a zipped SAS file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f95sas.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f95sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "f95sas.zip"
                 }
             ],
+            "identifier": "f6dccc8f-448d-4189-a5ee-e432f23bd720",
+            "issued": "2010-05-06",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "computers",
                 "information-technology",
                 "internet"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/surveys/frss/download/data/f95doc.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Educational Technology in Public School Districts, 2008",
-            "description": "Educational Technology in Public School Districts, 2008 (FRSS 93), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 93 (https://nces.ed.gov/surveys/frss/) is a sample survey that provides national estimates on the availability and use of educational technology in public school districts during Fall 2008. This is one of a set of three surveys (at the district, school, and teacher levels) that collected data on a range of educational technology resources. The study was conducted by having school superintendents fill out surveys via the web or by mail. Public school districts were sampled. The study's weighted response rate was 90 percent. Key statistics produced from FRSS 93 were information on networks and internet capacity, technology policies, district-provided resources, teacher professional development, and district-level leadership for technology. Respondents reported the number of schools in the district with a local area network and the number of schools with each type of district network connection. The survey collected information on written district policies on acceptable student use of various technologies. Other survey topics included employment of staff responsible for educational technology leadership and the type of teacher professional development offered or required by districts for educational technology. Respondents gave their opinions on statements related to the use of educational technology in the instructional programs in their districts.",
-            "modified": "2023-06-27T17:42:46.695546",
-            "accessLevel": "public",
-            "identifier": "af461675-00f7-4f0f-8f1e-22083bd8a643",
-            "dataQuality": true,
-            "issued": "2010-03-29",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2008/2009",
+            "modified": "2023-06-27T17:43:43.264214",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -70282,30 +70241,48 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/surveys/frss/download/data/f95doc.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2008/2009",
+            "title": "Teachers' Use of Educational Technology in U.S. Public Schools, 2009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "Educational Technology in Public School Districts, 2008 (FRSS 93), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 93 (https://nces.ed.gov/surveys/frss/) is a sample survey that provides national estimates on the availability and use of educational technology in public school districts during Fall 2008. This is one of a set of three surveys (at the district, school, and teacher levels) that collected data on a range of educational technology resources. The study was conducted by having school superintendents fill out surveys via the web or by mail. Public school districts were sampled. The study's weighted response rate was 90 percent. Key statistics produced from FRSS 93 were information on networks and internet capacity, technology policies, district-provided resources, teacher professional development, and district-level leadership for technology. Respondents reported the number of schools in the district with a local area network and the number of schools with each type of district network connection. The survey collected information on written district policies on acceptable student use of various technologies. Other survey topics included employment of staff responsible for educational technology leadership and the type of teacher professional development offered or required by districts for educational technology. Respondents gave their opinions on statements related to the use of educational technology in the instructional programs in their districts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "f93data.zip",
                     "description": "Educational Technology in Public School Districts, 2008 data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f93data.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f93data.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "f93data.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "f93sas.zip",
                     "description": "Educational Technology in Public School Districts, 2008 data in a zipped SAS file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f93sas.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f93sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "f93sas.zip"
                 }
             ],
+            "identifier": "af461675-00f7-4f0f-8f1e-22083bd8a643",
+            "issued": "2010-03-29",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "computer-networks",
@@ -70315,32 +70292,14 @@
                 "frss",
                 "teacher-professional-development"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/surveys/frss/download/data/f93doc.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "District Survey of Alternative Schools and Programs, 2007-08",
-            "description": "The District Survey of Alternative Schools and Programs, 2007-08 (FRSS 96), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 96 (https://nces.ed.gov/surveys/frss/) is a sample survey that provides national estimates on the availability of alternative schools and programs for students at risk of educational failure in public school districts during the 2007-08 school year. The study was conducted using mailed paper questionnaires. Superintendents were sampled. The study's response rate was 96 percent. Key statistics produced from FRSS 96 were that students who attend alternative schools and programs are typically at risk of educational failure (as indicated by poor grades, truancy, disruptive behavior, pregnancy, or similar factors associated with temporary or permanent withdrawal from school).",
-            "modified": "2023-06-27T17:41:34.527611",
-            "accessLevel": "public",
-            "identifier": "ec4f230a-9dc0-45fd-9440-ec729eb9ad2b",
-            "dataQuality": true,
-            "issued": "2010-03-29",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2007/2010",
+            "modified": "2023-06-27T17:42:46.695546",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -70361,30 +70320,48 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/surveys/frss/download/data/f93doc.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2008/2009",
+            "title": "Educational Technology in Public School Districts, 2008"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The District Survey of Alternative Schools and Programs, 2007-08 (FRSS 96), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 96 (https://nces.ed.gov/surveys/frss/) is a sample survey that provides national estimates on the availability of alternative schools and programs for students at risk of educational failure in public school districts during the 2007-08 school year. The study was conducted using mailed paper questionnaires. Superintendents were sampled. The study's response rate was 96 percent. Key statistics produced from FRSS 96 were that students who attend alternative schools and programs are typically at risk of educational failure (as indicated by poor grades, truancy, disruptive behavior, pregnancy, or similar factors associated with temporary or permanent withdrawal from school).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "f96data.zip",
                     "description": "District Survey of Alternative Schools and Programs, 2007-08 data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f96data.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f96data.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "f96data.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "f96sas.zip",
                     "description": "District Survey of Alternative Schools and Programs, 2007-08 data in a zipped SAS file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f96sas.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f96sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "f96sas.zip"
                 }
             ],
+            "identifier": "ec4f230a-9dc0-45fd-9440-ec729eb9ad2b",
+            "issued": "2010-03-29",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "alternative-programs",
@@ -70392,32 +70369,14 @@
                 "district-survey",
                 "students-at-risk"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/surveys/frss/download/data/f96doc.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Distance Education Courses for Public Elementary and Secondary School Students, 2009-10",
-            "description": "The Distance Education Courses for Public Elementary and Secondary School Students, 2009-10 (FRSS 98), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 98 (https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2012009) is a sample survey that provides national estimates on distance education courses in public school districts, including enrollment in distance education courses, how districts monitor these courses, the motivations for providing distance education, and the technologies used for delivering distance education. The study was conducted using surveys via the web or by mail. District superintendents were sampled. The study's weighted response rate was 95%. Key statistics produced from FRSS 98 include the types of distance education courses taken by students, whether the district plans to expand the number of distance education courses, and the technologies used for delivering distance education.",
-            "modified": "2023-06-27T17:40:18.662472",
-            "accessLevel": "public",
-            "identifier": "bdd9959b-0f3b-40ab-8569-ad2f670102a6",
-            "dataQuality": true,
-            "issued": "2011-12-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2009/2010",
+            "modified": "2023-06-27T17:41:34.527611",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -70438,30 +70397,48 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/surveys/frss/download/data/f96doc.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2007/2010",
+            "title": "District Survey of Alternative Schools and Programs, 2007-08"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Distance Education Courses for Public Elementary and Secondary School Students, 2009-10 (FRSS 98), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 98 (https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2012009) is a sample survey that provides national estimates on distance education courses in public school districts, including enrollment in distance education courses, how districts monitor these courses, the motivations for providing distance education, and the technologies used for delivering distance education. The study was conducted using surveys via the web or by mail. District superintendents were sampled. The study's weighted response rate was 95%. Key statistics produced from FRSS 98 include the types of distance education courses taken by students, whether the district plans to expand the number of distance education courses, and the technologies used for delivering distance education.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "f98data.zip",
                     "description": "Distance Education Courses for Public Elementary and Secondary School Students, 2009-10 data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f98data.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f98data.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "f98data.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "f98sas.zip",
                     "description": "Distance Education Courses for Public Elementary and Secondary School Students, 2009-10 data in a zipped SAS file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f98sas.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f98sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "f98sas.zip"
                 }
             ],
+            "identifier": "bdd9959b-0f3b-40ab-8569-ad2f670102a6",
+            "issued": "2011-12-01",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "distance-education",
@@ -70470,31 +70447,14 @@
                 "public-elementary-students",
                 "public-secondary-school-students"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/surveys/frss/download/data/f98doc.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Elementary School Arts Education Survey, 2009",
-            "description": "The Elementary School Arts Education Survey, 2009 (FRSS 100), is a study that is part of the Quick Response Information System. FRSS 100 (https://nces.ed.gov/surveys/frss/) is a sample survey that provides national estimates on student access to arts education and resources available for such instruction in public elementary schools during fall 2009. The study was conducted using mailed questionnaires that could be completed via web or by mail. Follow-up telephone interviews were also conducted. Principals of elementary schools were sampled. The study's response rate was 85 percent. Key statistics produced from FRSS 100 are availability and characteristics of music, visual arts, dance, and drama/theatre instruction; the type of space used for arts instruction; the availability of curriculum guides for arts teachers to follow; and whether those teaching the subject are arts specialists.",
-            "modified": "2023-06-27T16:24:33.029416",
-            "accessLevel": "public",
-            "identifier": "661c567f-cf7b-46cb-97f7-3f80fd1e879f",
-            "dataQuality": true,
-            "issued": "2012-04-02",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2009/2010",
+            "modified": "2023-06-27T17:40:18.662472",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -70515,30 +70475,48 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/surveys/frss/download/data/f98doc.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2009/2010",
+            "title": "Distance Education Courses for Public Elementary and Secondary School Students, 2009-10"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Elementary School Arts Education Survey, 2009 (FRSS 100), is a study that is part of the Quick Response Information System. FRSS 100 (https://nces.ed.gov/surveys/frss/) is a sample survey that provides national estimates on student access to arts education and resources available for such instruction in public elementary schools during fall 2009. The study was conducted using mailed questionnaires that could be completed via web or by mail. Follow-up telephone interviews were also conducted. Principals of elementary schools were sampled. The study's response rate was 85 percent. Key statistics produced from FRSS 100 are availability and characteristics of music, visual arts, dance, and drama/theatre instruction; the type of space used for arts instruction; the availability of curriculum guides for arts teachers to follow; and whether those teaching the subject are arts specialists.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "f100data.zip",
                     "description": "Elementary School Arts Education Survey, 2009 data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f100data.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f100data.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "f100data.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "f100sas.zip",
                     "description": "Elementary School Arts Education Survey, 2009 data in a zipped SAS file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f100sas.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f100sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "f100sas.zip"
                 }
             ],
+            "identifier": "661c567f-cf7b-46cb-97f7-3f80fd1e879f",
+            "issued": "2012-04-02",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "arts-specialists",
@@ -70548,32 +70526,14 @@
                 "music",
                 "visual-arts"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/surveys/frss/download/data/f100doc.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Dropout Prevention Services and Programs",
-            "description": "Dropout Prevention Services and Programs (FRSS 99), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 99 (https://nces.ed.gov/surveys/frss/index.asp) is a sample survey that provides national estimates on how public school districts identify students at risk of dropping out, programs used specifically to address the needs of students at risk of dropping out of school, the use of mentors for at-risk students, and efforts to encourage dropouts to return to school. The study was conducted using mail, surveys via the web, and telephone follow-up for survey nonresponse and data clarification. Superintendents of public school districts were sampled. The study's weighted response rate was 89 percent. Key statistics produced from FRSS 99 were information on various services or programs offered by districts specifically to address the needs of students at risk of dropping out of school, and types of transition support services used to help all students transition from a school at one instructional level to a school at a higher instructional level. Data on the various factors used to identify students who were at risk of dropping out were also collected.",
-            "modified": "2023-06-27T16:23:58.139632",
-            "accessLevel": "public",
-            "identifier": "b5e8682a-9db4-41fc-9d8c-9549a66ef657",
-            "dataQuality": true,
-            "issued": "2011-10-12",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2010/2011",
+            "modified": "2023-06-27T16:24:33.029416",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -70594,30 +70554,47 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/surveys/frss/download/data/f100doc.zip"
+            ],
+            "spatial": "United States",
+            "temporal": "2009/2010",
+            "title": "Elementary School Arts Education Survey, 2009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "Dropout Prevention Services and Programs (FRSS 99), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 99 (https://nces.ed.gov/surveys/frss/index.asp) is a sample survey that provides national estimates on how public school districts identify students at risk of dropping out, programs used specifically to address the needs of students at risk of dropping out of school, the use of mentors for at-risk students, and efforts to encourage dropouts to return to school. The study was conducted using mail, surveys via the web, and telephone follow-up for survey nonresponse and data clarification. Superintendents of public school districts were sampled. The study's weighted response rate was 89 percent. Key statistics produced from FRSS 99 were information on various services or programs offered by districts specifically to address the needs of students at risk of dropping out of school, and types of transition support services used to help all students transition from a school at one instructional level to a school at a higher instructional level. Data on the various factors used to identify students who were at risk of dropping out were also collected.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "f99data.zip",
                     "description": "Dropout Prevention Services and Programs data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f99data.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f99data.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "f99data.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "f99sas.zip",
                     "description": "Dropout Prevention Services and Programs data in a zipped SAS file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f99sas.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f99sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "f99sas.zip"
                 }
             ],
+            "identifier": "b5e8682a-9db4-41fc-9d8c-9549a66ef657",
+            "issued": "2011-10-12",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "district-services",
@@ -70627,31 +70604,14 @@
                 "programs",
                 "students-at-risk-of-dropping-out"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-27T16:23:58.139632",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://nces.ed.gov/surveys/frss/download/data/f99doc.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Secondary School Arts Education Survey, 2009",
-            "description": "Secondary School Arts and Education Survey, 2009 (FRSS 101), is a study that is part of the Quick Response Information System. FRSS 101 (https://nces.ed.gov/surveys/frss/) is a sample survey that provides national estimates on student access to arts education and the resources available for such instruction in public secondary schools during fall 2009. The study was conducted using mailed questionnaires that could be completed via mail or the web. Follow-up telephone interviews were also conducted. School principals were sampled. The study's response rate was 87 percent. Key statistics produced from FRSS 101 are availability of music, visual arts, dance, and drama/theatre instruction; enrollment in these courses, the type of space used for arts instruction, the availability of curriculum guides for arts teachers to follow, and the number of arts teachers who are specialists in the subject.",
-            "modified": "2023-06-27T16:23:01.541206",
-            "accessLevel": "public",
-            "identifier": "5ef4ee3e-301f-4b03-b274-42d87910073a",
-            "dataQuality": true,
-            "issued": "2012-04-02",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2009/2010",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -70672,22 +70632,40 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/surveys/frss/download/data/f99doc.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2010/2011",
+            "title": "Dropout Prevention Services and Programs"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "Secondary School Arts and Education Survey, 2009 (FRSS 101), is a study that is part of the Quick Response Information System. FRSS 101 (https://nces.ed.gov/surveys/frss/) is a sample survey that provides national estimates on student access to arts education and the resources available for such instruction in public secondary schools during fall 2009. The study was conducted using mailed questionnaires that could be completed via mail or the web. Follow-up telephone interviews were also conducted. School principals were sampled. The study's response rate was 87 percent. Key statistics produced from FRSS 101 are availability of music, visual arts, dance, and drama/theatre instruction; enrollment in these courses, the type of space used for arts instruction, the availability of curriculum guides for arts teachers to follow, and the number of arts teachers who are specialists in the subject.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped ASCII",
-                    "title": "f101data.zip",
                     "description": "Secondary School Arts Education Survey, 2009 data in a zipped ASCII file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f101data.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f101data.zip",
+                    "format": "Zipped ASCII",
+                    "mediaType": "application/zip",
+                    "title": "f101data.zip"
                 }
             ],
+            "identifier": "5ef4ee3e-301f-4b03-b274-42d87910073a",
+            "issued": "2012-04-02",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "educational-achievement",
@@ -70696,28 +70674,14 @@
                 "mathematics",
                 "science"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-27T16:23:01.541206",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Arts Education Surveys of Elementary School Teachers, 2009",
-            "description": "Arts Education Surveys of Elementary School Teachers, 2009 (FRSS 102), is a study that is part of the Quick Response Information System. FRSS 102 (https://nces.ed.gov/surveys/frss/) is a sample survey that provides national estimates on arts education and arts instructors in public elementary schools during the 2009-10 school year. The study was conducted using mailed questionnaires that could be completed via mail or the web. Follow-up telephone interviews were also conducted. Elementary school teachers were sampled. The response rate for each of the three surveys was 86.5 percent for the music specialist survey, 87.6 percent for the visual arts specialist survey, and 81.5 percent for the classroom teacher survey. Key statistics produced from FRSS 102 were data on the teaching load of music and visual arts specialists in elementary schools; teacher participation in various professional development activities; the ways in which self-contained classroom teachers teach arts education as part of their instructional program; and teachers' use of formal methods of assessment of students' achievement in the arts.",
-            "modified": "2023-06-27T16:22:14.882085",
-            "accessLevel": "public",
-            "identifier": "d5d0e1a7-fe05-4f1f-aae8-848f067785c8",
-            "dataQuality": true,
-            "issued": "2012-04-24",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2009/2010",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -70738,30 +70702,44 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2009/2010",
+            "title": "Secondary School Arts Education Survey, 2009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "Arts Education Surveys of Elementary School Teachers, 2009 (FRSS 102), is a study that is part of the Quick Response Information System. FRSS 102 (https://nces.ed.gov/surveys/frss/) is a sample survey that provides national estimates on arts education and arts instructors in public elementary schools during the 2009-10 school year. The study was conducted using mailed questionnaires that could be completed via mail or the web. Follow-up telephone interviews were also conducted. Elementary school teachers were sampled. The response rate for each of the three surveys was 86.5 percent for the music specialist survey, 87.6 percent for the visual arts specialist survey, and 81.5 percent for the classroom teacher survey. Key statistics produced from FRSS 102 were data on the teaching load of music and visual arts specialists in elementary schools; teacher participation in various professional development activities; the ways in which self-contained classroom teachers teach arts education as part of their instructional program; and teachers' use of formal methods of assessment of students' achievement in the arts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "f102data.zip",
                     "description": "Arts Education Surveys of Elementary School Teachers, 2009 data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f102data.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f102data.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "f102data.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "f102sas.zip",
                     "description": "Arts Education Surveys of Elementary School Teachers, 2009 data in a zipped SAS file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f102sas.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f102sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "f102sas.zip"
                 }
             ],
+            "identifier": "d5d0e1a7-fe05-4f1f-aae8-848f067785c8",
+            "issued": "2012-04-24",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "arts-specialists",
@@ -70771,31 +70749,14 @@
                 "music",
                 "visual-arts"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/surveys/frss/download/data/f102doc.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Arts Education Surveys of Secondary School Teachers, 2009",
-            "description": "Arts Education Surveys of Secondary School Teachers, 2009 (FRSS 103), is a study that is part of the Quick Response Information System. FRSS 103 (https://nces.ed.gov/surveys/frss/) is a sample survey that provides national estimates on arts education and arts instructors in public secondary schools during the 2009-10 school year. The study was conducted using mailed questionnaires that could be completed via web or by mail. Follow-up telephone interviews were also conducted. Teachers were sampled. The study's response rate was 81.8 percent. Key statistics produced from FRSS 103 were data on the teaching load of music and visual arts specialists in secondary schools; teacher participation in various professional development activities and the perceived impact of such participation on teaching; and teachers' use of formal methods of assessment of students' progress and achievement in the arts.",
-            "modified": "2023-06-27T16:21:16.821109",
-            "accessLevel": "public",
-            "identifier": "7350d362-8133-4d25-ae6f-540983471e48",
-            "dataQuality": true,
-            "issued": "2012-04-02",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2009/2010",
+            "modified": "2023-06-27T16:22:14.882085",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -70816,46 +70777,63 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/surveys/frss/download/data/f102doc.zip"
+            ],
+            "spatial": "United States",
+            "temporal": "2009/2010",
+            "title": "Arts Education Surveys of Elementary School Teachers, 2009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "Arts Education Surveys of Secondary School Teachers, 2009 (FRSS 103), is a study that is part of the Quick Response Information System. FRSS 103 (https://nces.ed.gov/surveys/frss/) is a sample survey that provides national estimates on arts education and arts instructors in public secondary schools during the 2009-10 school year. The study was conducted using mailed questionnaires that could be completed via web or by mail. Follow-up telephone interviews were also conducted. Teachers were sampled. The study's response rate was 81.8 percent. Key statistics produced from FRSS 103 were data on the teaching load of music and visual arts specialists in secondary schools; teacher participation in various professional development activities and the perceived impact of such participation on teaching; and teachers' use of formal methods of assessment of students' progress and achievement in the arts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "f103data_1.zip",
                     "description": "Arts Education Surveys of Secondary School Teachers, 2009 music data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f103data_1.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f103data_1.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "f103data_1.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "f103data_2.zip",
                     "description": "Arts Education Surveys of Secondary School Teachers, 2009 visual arts data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f103data_2.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f103data_2.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "f103data_2.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "f103sas_1.zip",
                     "description": "Arts Education Surveys of Secondary School Teachers, 2009 music data in a zipped SAS file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f103sas_1.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f103sas_1.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "f103sas_1.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "f103sas_2.zip",
                     "description": "Arts Education Surveys of Secondary School Teachers, 2009 visual arts data in a zipped SAS file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f103sas_2.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f103sas_2.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "f103sas_2.zip"
                 }
             ],
+            "identifier": "7350d362-8133-4d25-ae6f-540983471e48",
+            "issued": "2012-04-02",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "arts-specialists",
@@ -70864,32 +70842,14 @@
                 "music",
                 "visual-arts"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/surveys/frss/download/data/f103doc_1.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Dual Credit and Exam-Based Courses, 2010-11",
-            "description": "The Dual Credit and Exam-Based Courses, 2010-11 (FRSS 104), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 104 is a study that provides nationally representative data on prevalence and enrollment of dual credit and exam-based courses in public high schools. The study was conducted using paper surveys, telephones, and email. In this study school personnel were sampled. The unweighted survey response rate was 91 percent and the weighted response rate using the initial base weights was also 91 percent. Key statistics produced from FRSS 104 were whether students could earn both high school and postsecondary credits for the same courses, and if so, the total number of enrollments in these courses and the methods of implementation (distance education, at school or at college campus and by high school instructor or postsecondary instructor).",
-            "modified": "2023-06-27T16:10:53.570259",
-            "accessLevel": "public",
-            "identifier": "28db6f75-7118-404f-a630-a6434127cd17",
-            "dataQuality": true,
-            "issued": "2013-06-14",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2010/2011",
+            "modified": "2023-06-27T16:21:16.821109",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -70910,30 +70870,47 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/surveys/frss/download/data/f103doc_1.zip"
+            ],
+            "spatial": "United States",
+            "temporal": "2009/2010",
+            "title": "Arts Education Surveys of Secondary School Teachers, 2009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Dual Credit and Exam-Based Courses, 2010-11 (FRSS 104), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 104 is a study that provides nationally representative data on prevalence and enrollment of dual credit and exam-based courses in public high schools. The study was conducted using paper surveys, telephones, and email. In this study school personnel were sampled. The unweighted survey response rate was 91 percent and the weighted response rate using the initial base weights was also 91 percent. Key statistics produced from FRSS 104 were whether students could earn both high school and postsecondary credits for the same courses, and if so, the total number of enrollments in these courses and the methods of implementation (distance education, at school or at college campus and by high school instructor or postsecondary instructor).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "f104data.zip",
                     "description": "Dual Credit and Exam-Based Courses, 2010-11 data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f104data.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f104data.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "f104data.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "f104sas.zip",
                     "description": "Dual Credit and Exam-Based Courses, 2010-11 data in a zipped SAS file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f104sas.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f104sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "f104sas.zip"
                 }
             ],
+            "identifier": "28db6f75-7118-404f-a630-a6434127cd17",
+            "issued": "2013-06-14",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "dual-credit",
@@ -70948,32 +70925,14 @@
                 "prevalence-and-enrollment-of-dual-credit-and-exam-based-courses-in-public-high-schools",
                 "prevalence-of-college-course-taking-by-high-school-students"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/surveys/frss/download/data/f104doc.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Condition of Public School Facilities, 2012-13",
-            "description": "Condition of Public School Facilities, 2012-13 (FRSS 105), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at https://nces.ed.gov/surveys/frss/downloads.asp that will provide national data about the condition of public schools in 2012 based on a survey conducted by NCES. FRSS 105 (https://nces.ed.gov/surveys/frss/index.asp) is a cross-sectional survey that collects and report data on key education issues at the elementary and secondary levels. The study was conducted using questionnaires of principals. Schools in September 2012 were sampled. The study's weighted response rate was 90 percent. Key statistics produced from FRSS 105 will provide information about the condition of school facilities and the costs to bring them into good condition; school plans for repairs, renovations, and replacements; the age of public schools; and school improvements to increase energy efficiency.",
-            "modified": "2023-06-27T16:10:08.633408",
-            "accessLevel": "public",
-            "identifier": "9e8fa916-0208-49c3-83cf-ff43b1cadfad",
-            "dataQuality": true,
-            "issued": "2014-03-25",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2012/2013",
+            "modified": "2023-06-27T16:10:53.570259",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -70994,30 +70953,48 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/surveys/frss/download/data/f104doc.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2010/2011",
+            "title": "Dual Credit and Exam-Based Courses, 2010-11"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "Condition of Public School Facilities, 2012-13 (FRSS 105), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at https://nces.ed.gov/surveys/frss/downloads.asp that will provide national data about the condition of public schools in 2012 based on a survey conducted by NCES. FRSS 105 (https://nces.ed.gov/surveys/frss/index.asp) is a cross-sectional survey that collects and report data on key education issues at the elementary and secondary levels. The study was conducted using questionnaires of principals. Schools in September 2012 were sampled. The study's weighted response rate was 90 percent. Key statistics produced from FRSS 105 will provide information about the condition of school facilities and the costs to bring them into good condition; school plans for repairs, renovations, and replacements; the age of public schools; and school improvements to increase energy efficiency.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "f105data.zip",
                     "description": "Condition of Public School Facilities, 2012-13 data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f105data.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f105data.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "f105data.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "f105sas.zip",
                     "description": "Condition of Public School Facilities, 2012-13 data in a zipped SAS file",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f105sas.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f105sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "f105sas.zip"
                 }
             ],
+            "identifier": "9e8fa916-0208-49c3-83cf-ff43b1cadfad",
+            "issued": "2014-03-25",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "conditions",
@@ -71028,31 +71005,14 @@
                 "pretest",
                 "public-school"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/surveys/frss/download/data/f105doc.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School Safety and Discipline, 2013-14",
-            "description": "School Safety and Discipline, 2013-14 (FRSS 106), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 106 (https://nces.ed.gov/surveys/frss/index.asp) is a study that provides nationally representative data on safety and discipline in public schools. The study was conducted using mailed questionnaires that could be completed on paper or online. Public schools in each level (elementary, middle, high school, and combined) were sampled. The study's weighted response rate was 85%. Key statistics produced from FRSS 106 will provide information on specific safety and discipline plans and practices; training for teachers and aides related to school safety and discipline issues; use of law enforcement or security personnel on school grounds; frequency of specific discipline problems; and the number of incidents of various crimes that occurred during the 2013-14 school year.",
-            "modified": "2023-06-27T16:08:39.005368",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "0812ff45-0577-44b6-8bfb-076dcd2ac7fe",
-            "dataQuality": true,
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2013/2014",
+            "modified": "2023-06-27T16:10:08.633408",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -71073,36 +71033,53 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/surveys/frss/download/data/f105doc.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2012/2013",
+            "title": "Condition of Public School Facilities, 2012-13"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "School Safety and Discipline, 2013-14 (FRSS 106), is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 106 (https://nces.ed.gov/surveys/frss/index.asp) is a study that provides nationally representative data on safety and discipline in public schools. The study was conducted using mailed questionnaires that could be completed on paper or online. Public schools in each level (elementary, middle, high school, and combined) were sampled. The study's weighted response rate was 85%. Key statistics produced from FRSS 106 will provide information on specific safety and discipline plans and practices; training for teachers and aides related to school safety and discipline issues; use of law enforcement or security personnel on school grounds; frequency of specific discipline problems; and the number of incidents of various crimes that occurred during the 2013-14 school year.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped CSV",
-                    "title": "f106data.zip",
                     "description": "Public-Use Data Files and Documentation (FRSS 106): School Safety and Discipline: 2013-14",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f106data.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f106data.zip",
+                    "format": "Zipped CSV",
+                    "mediaType": "application/zip",
+                    "title": "f106data.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "f106sas.zip",
                     "description": "Public-Use Data Files and Documentation (FRSS 106): School Safety and Discipline: 2013-14",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f106sas.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f106sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "f106sas.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "(FRSS 106): School Safety and Discipline: 2013-14 Restricted-Use Data Files",
                     "description": "Restricted-use data file for (FRSS 106): School Safety and Discipline: 2013-14",
                     "downloadURL": "https://nces.ed.gov/statprog/instruct.asp",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "(FRSS 106): School Safety and Discipline: 2013-14 Restricted-Use Data Files"
                 }
             ],
+            "identifier": "0812ff45-0577-44b6-8bfb-076dcd2ac7fe",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "crime",
@@ -71112,25 +71089,11 @@
                 "public-school",
                 "safety"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-27T16:08:39.005368",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Programs and Services for High School English Learners, 2015-16",
-            "description": "Programs and Services for High School English Learners, 2015-16 (FRSS 107) is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 107 (https://nces.ed.gov/surveys/frss/index.asp) is a study that provides nationally representative data on programs and services for high-school English learners (Els), including instructional approaches, newcomer programs, online or computer-based programs, and programs or services (e.g., tutoring) designed specifically for high school Els. The study was conducted using mailed questionnaires that could be completed on paper or online. Public local education agencies (LEAs) instructing either of Grades 11 or 12 in the 50 United States and the District of Columbia were sampled. The study's weighted response rate was 89 percent. Key statistics produced from FRSS 107 include data on the use of native language(s) for content instruction, instructional support, materials, and services; information that LEAs provide about educational programs or services to Els aged 18 to 21 years-old seeking to newly enroll in the LEA; and factors LEAs consider when providing information about these programs and services to Els in this group.",
-            "modified": "2023-06-27T16:07:55.671845",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "fe4a935f-a4b8-4fe3-a20a-e057a71cac20",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2015/2016",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -71151,36 +71114,50 @@
                     }
                 }
             },
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "temporal": "2013/2014",
+            "title": "School Safety and Discipline, 2013-14"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "Programs and Services for High School English Learners, 2015-16 (FRSS 107) is a study that is part of the Fast Response Survey System (FRSS) program; program data is available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 107 (https://nces.ed.gov/surveys/frss/index.asp) is a study that provides nationally representative data on programs and services for high-school English learners (Els), including instructional approaches, newcomer programs, online or computer-based programs, and programs or services (e.g., tutoring) designed specifically for high school Els. The study was conducted using mailed questionnaires that could be completed on paper or online. Public local education agencies (LEAs) instructing either of Grades 11 or 12 in the 50 United States and the District of Columbia were sampled. The study's weighted response rate was 89 percent. Key statistics produced from FRSS 107 include data on the use of native language(s) for content instruction, instructional support, materials, and services; information that LEAs provide about educational programs or services to Els aged 18 to 21 years-old seeking to newly enroll in the LEA; and factors LEAs consider when providing information about these programs and services to Els in this group.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped CSV",
-                    "title": "f107data.zip",
                     "description": "Public-Use Data Files and Documentation (FRSS 107): Programs and Services for High School English Learners",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f107data.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f107data.zip",
+                    "format": "Zipped CSV",
+                    "mediaType": "application/zip",
+                    "title": "f107data.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "f107sas.zip",
                     "description": "Public-Use Data Files and Documentation (FRSS 107): Programs and Services for High School English Learners",
-                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f107sas.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/frss/download/data/f107sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "f107sas.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "(FRSS 107): Programs and Services for High School English Learners Restricted-Use Data Files",
                     "description": "Restricted-use data file for (FRSS 107): Programs and Services for High School English Learners",
                     "downloadURL": "https://nces.ed.gov/statprog/instruct.asp",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "(FRSS 107): Programs and Services for High School English Learners Restricted-Use Data Files"
                 }
             ],
+            "identifier": "fe4a935f-a4b8-4fe3-a20a-e057a71cac20",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "district-programs-and-services",
@@ -71196,24 +71173,11 @@
                 "local-education-agencies",
                 "public-school-districts"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-27T16:07:55.671845",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Career and Technical Education Programs in Public School Districts, 2016-17",
-            "description": "Career and Technical Education Programs in Public School Districts, 2016-17 (FRSS 108) is a data collection that is part of the Fast Response Survey System (FRSS) program; program data are available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 108 (https://nces.ed.gov/surveys/frss/index.asp) is a cross-sectional data collection that provides nationally representative data on career and technical education (CTE) programs. Public local education agencies (LEAs) instructing either grades 11 or 12 in the 50 United States and the District of Columbia were sampled. The study was conducted using mailed questionnaires that could be completed on paper or online. The data collection's response rate was 86 percent. Key statistics produced from FRSS 108 include data on the entities that provide the CTE programs, the locations at which the CTE programs are offered, work-based learning activities and employer involvement in CTE programs, barriers to the district offering CTE programs, barriers to student participation in CTE programs, and the extent to which various factors influence the district's decisions on whether to add or phase out CTE programs.",
-            "modified": "2023-06-27T16:06:58.978519",
-            "accessLevel": "public",
-            "identifier": "1ccd201b-01cc-4adc-b04b-699736981add",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2016/2017",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -71234,29 +71198,43 @@
                     }
                 }
             },
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "temporal": "2015/2016",
+            "title": "Programs and Services for High School English Learners, 2015-16"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "Career and Technical Education Programs in Public School Districts, 2016-17 (FRSS 108) is a data collection that is part of the Fast Response Survey System (FRSS) program; program data are available since 1998-99 at <https://nces.ed.gov/surveys/frss/downloads.asp>. FRSS 108 (https://nces.ed.gov/surveys/frss/index.asp) is a cross-sectional data collection that provides nationally representative data on career and technical education (CTE) programs. Public local education agencies (LEAs) instructing either grades 11 or 12 in the 50 United States and the District of Columbia were sampled. The study was conducted using mailed questionnaires that could be completed on paper or online. The data collection's response rate was 86 percent. Key statistics produced from FRSS 108 include data on the entities that provide the CTE programs, the locations at which the CTE programs are offered, work-based learning activities and employer involvement in CTE programs, barriers to the district offering CTE programs, barriers to student participation in CTE programs, and the extent to which various factors influence the district's decisions on whether to add or phase out CTE programs.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/ascii",
-                    "format": "Zipped ascii",
-                    "title": "2018029_ascii.zip",
                     "description": "Public-Use Data Files (FRSS 108): Career and Technical Education Programs in Public School Districts",
-                    "downloadURL": "https://nces.ed.gov/pubs2018/data/2018029_ascii.zip"
+                    "downloadURL": "https://nces.ed.gov/pubs2018/data/2018029_ascii.zip",
+                    "format": "Zipped ascii",
+                    "mediaType": "application/ascii",
+                    "title": "2018029_ascii.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "2018029_sas.zip",
                     "description": "Public-Use Data Files (FRSS 108): Career and Technical Education Programs in Public School Districts",
-                    "downloadURL": "https://nces.ed.gov/pubs2018/data/2018029_sas.zip"
+                    "downloadURL": "https://nces.ed.gov/pubs2018/data/2018029_sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "2018029_sas.zip"
                 }
             ],
+            "identifier": "1ccd201b-01cc-4adc-b04b-699736981add",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "career-and-technical-education-programs",
@@ -71265,30 +71243,17 @@
                 "high-school",
                 "work-based-learning"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-27T16:06:58.978519",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Federal Pell Grant Reporting, 2012-13",
-            "description": "Federal Pell Grant Reporting, 2012-13 (Pell Grant Reporting 2012-13), is a part of the Federal Pell Grant Reporting (Pell Grant Reporting) program. Pell Grant Reporting 2012-13 (https://www2.ed.gov/programs/fpg/index.html) is a compilation of quantitative program data assembled to offer insights into the changes to the Title IV applicant universe and the Pell Grant program. The information provides a basis for program planning and development and can also be used to estimate the potential impact of actual or proposed policies on Pell Grant recipients and federal aid applicants. In addition, it can assist researchers, students, higher education officials, and financial aid administrators to better understand current patterns of Federal Pell Grant disbursements and Title IV applicant activity.",
-            "modified": "2023-06-27T16:04:35.142876",
-            "accessLevel": "public",
-            "identifier": "4a08dd77-e1bd-4f49-878d-37f24c793a9f",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2012/2013",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Postsecondary Education (OPE)",
+                "name": "National Center for Education Statistics (NCES)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of the Under Secretary (OUS)",
+                    "name": "Institute of Education Sciences (IES)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -71303,68 +71268,68 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2016/2017",
+            "title": "Career and Technical Education Programs in Public School Districts, 2016-17"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Anthony Hales, Jr.",
                 "hasEmail": "mailto:anthony.hales@ed.gov"
             },
+            "dataQuality": true,
+            "description": "Federal Pell Grant Reporting, 2012-13 (Pell Grant Reporting 2012-13), is a part of the Federal Pell Grant Reporting (Pell Grant Reporting) program. Pell Grant Reporting 2012-13 (https://www2.ed.gov/programs/fpg/index.html) is a compilation of quantitative program data assembled to offer insights into the changes to the Title IV applicant universe and the Pell Grant program. The information provides a basis for program planning and development and can also be used to estimate the potential impact of actual or proposed policies on Pell Grant recipients and federal aid applicants. In addition, it can assist researchers, students, higher education officials, and financial aid administrators to better understand current patterns of Federal Pell Grant disbursements and Title IV applicant activity.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "pell-inst-12-13.xls",
                     "description": "Distribution of Federal Pell Grant Recipients by Type and Control of Institution: Award Year 2012-2013",
-                    "downloadURL": "https://www2.ed.gov/finaid/prof/resources/data/pell-inst-12-13.xls"
+                    "downloadURL": "https://www2.ed.gov/finaid/prof/resources/data/pell-inst-12-13.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "pell-inst-12-13.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/pdf",
-                    "format": "PDF",
-                    "title": "pell-eoy-2012-13.pdf",
                     "description": "2012-2013 Federal Pell Grant Program End-of-Year Report",
-                    "downloadURL": "https://www2.ed.gov/finaid/prof/resources/data/pell-2012-13/pell-eoy-2012-13.pdf"
+                    "downloadURL": "https://www2.ed.gov/finaid/prof/resources/data/pell-2012-13/pell-eoy-2012-13.pdf",
+                    "format": "PDF",
+                    "mediaType": "application/pdf",
+                    "title": "pell-eoy-2012-13.pdf"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "ZIP",
-                    "title": "pell-eoy-2012-13.zip",
                     "description": "2012-2013 Federal Pell Grant Program End-of-Year Report",
-                    "downloadURL": "https://www2.ed.gov/finaid/prof/resources/data/pell-2012-13/pell-eoy-2012-13.zip"
+                    "downloadURL": "https://www2.ed.gov/finaid/prof/resources/data/pell-2012-13/pell-eoy-2012-13.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip",
+                    "title": "pell-eoy-2012-13.zip"
                 }
             ],
+            "identifier": "4a08dd77-e1bd-4f49-878d-37f24c793a9f",
             "keyword": [
                 "c1e7a143-9bfc-4eeb-8df8-720605a12e1a",
                 "federal-pell-grant",
                 "financial-aid",
                 "postsecondary-education"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-27T16:04:35.142876",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Gainful Employment Informational Rates, 2011",
-            "description": "The Gainful Employment Informational Rates, 2011 (GE2011), is a collection that is part of the Gainful Employment (GE) program; program data is available since 2011 at <https://studentaid.ed.gov/sa/about/data-center/school/ge/data>. GE2011 (https://studentaid.ed.gov/sa/about/data-center/school/ge) is a universe data collection regarding repayment rate and debt-to-earnings ratios, as in order to be eligible for Title IV student assistance programs under the Higher Education Act (HEA), postsecondary institutions' educational programs must be proven to lead to a degree or to prepare students for gainful employment in a recognized occupation. With very few exceptions, all educational programs offered at for-profit institutions must lead to gainful employment in a recognized occupation. The GE2011 rates are for informational purposes only and, as such, do not invoke any regulatory requirements, sanctions, or other adverse action. These informational rates were prepared in advance of the July 1, 2012 effective date of the applicable regulations for the years in which programs that fail the debt measures will be required to provide debt warnings and may lose eligibility after failing three out of four consecutive years. Key statistics produced from GE2011 were information on repayment rates and debt-to-earnings ratios.",
-            "modified": "2023-06-27T15:56:04.359149",
-            "accessLevel": "public",
-            "identifier": "6724d1a6-27e4-4bdb-ab26-853b13e5575b",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2011/2012",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Federal Student Aid (FSA)",
+                "name": "Office of Postsecondary Education (OPE)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Office of the Under Secretary (OUS)",
@@ -71382,22 +71347,35 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2012/2013",
+            "title": "Federal Pell Grant Reporting, 2012-13"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:45"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tara Marini",
                 "hasEmail": "mailto:tara.marini@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Gainful Employment Informational Rates, 2011 (GE2011), is a collection that is part of the Gainful Employment (GE) program; program data is available since 2011 at <https://studentaid.ed.gov/sa/about/data-center/school/ge/data>. GE2011 (https://studentaid.ed.gov/sa/about/data-center/school/ge) is a universe data collection regarding repayment rate and debt-to-earnings ratios, as in order to be eligible for Title IV student assistance programs under the Higher Education Act (HEA), postsecondary institutions' educational programs must be proven to lead to a degree or to prepare students for gainful employment in a recognized occupation. With very few exceptions, all educational programs offered at for-profit institutions must lead to gainful employment in a recognized occupation. The GE2011 rates are for informational purposes only and, as such, do not invoke any regulatory requirements, sanctions, or other adverse action. These informational rates were prepared in advance of the July 1, 2012 effective date of the applicable regulations for the years in which programs that fail the debt measures will be required to provide debt warnings and may lose eligibility after failing three out of four consecutive years. Key statistics produced from GE2011 were information on repayment rates and debt-to-earnings ratios.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "apploication/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "GE2011InformationalRates102512_0.XLS",
                     "description": "2011 Gainful Employment Informational Rates",
-                    "downloadURL": "https://studentaid.ed.gov/sa/sites/default/files/GE2011InformationalRates102512_0.XLS"
+                    "downloadURL": "https://studentaid.ed.gov/sa/sites/default/files/GE2011InformationalRates102512_0.XLS",
+                    "format": "XLS",
+                    "mediaType": "apploication/vnd.ms-excel",
+                    "title": "GE2011InformationalRates102512_0.XLS"
                 }
             ],
+            "identifier": "6724d1a6-27e4-4bdb-ab26-853b13e5575b",
             "keyword": [
                 "5474ef49-ba39-40d2-8f39-47bf2a766902",
                 "annual-loan-payments",
@@ -71409,35 +71387,20 @@
                 "recognized-occupation",
                 "repayment-rate"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:45"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-27T15:56:04.359149",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Impact Evaluation of Teacher and Leader Performance Evaluation Systems",
-            "description": "The Impact Evaluation of Teacher and Leader Performance Evaluation Systems (TLES Study) is a data collection that is part of the NCEE Evaluation Studies program. The TLES Study (https://ies.ed.gov/ncee/projects/evaluation/tq_performance.asp) is a cross-sectional data collection that evaluates  the implementation of teacher and principal performance measures, as well as the impact of providing feedback based on these measures. Eight districts participated in the study; about 15 schools within each district were sampled. The data collection consisted of attendance lists, data from online systems, surveys of teachers and principals, ratings, classroom observations, student test scores, and district administrative records. Key findings produced from the TLES Study include: (1) the study's performance measures were implemented generally as planned, (2) the study's measures provided some information to identify educators who needed support, but provided limited information to indicate the areas of practice educators most needed to improve, (3) as intended, educators in treatment schools received more frequent feedback with ratings than did those in control schools, and (4)feedback from the study's measures had some positive impacts on teachers' classroom practice, principals' leadership, and student achievement.",
-            "modified": "2023-06-27T15:55:00.655598",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "bef5ce25-f4a0-46e5-9c6e-191d9eef5861",
-            "issued": "9999-12-31",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-10-12/pdf/2012-25186.pdf",
-            "temporal": "2011/2017",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "National Center for Education Evaluation and Regional Assistance (NCEERA)",
+                "name": "Office of Federal Student Aid (FSA)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Institute of Education Sciences (IES)",
+                    "name": "Office of the Under Secretary (OUS)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -71452,24 +71415,37 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2011/2012",
+            "title": "Gainful Employment Informational Rates, 2011"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Melanie Ali",
                 "hasEmail": "mailto:Melanie.Ali@ed.gov"
             },
+            "description": "The Impact Evaluation of Teacher and Leader Performance Evaluation Systems (TLES Study) is a data collection that is part of the NCEE Evaluation Studies program. The TLES Study (https://ies.ed.gov/ncee/projects/evaluation/tq_performance.asp) is a cross-sectional data collection that evaluates  the implementation of teacher and principal performance measures, as well as the impact of providing feedback based on these measures. Eight districts participated in the study; about 15 schools within each district were sampled. The data collection consisted of attendance lists, data from online systems, surveys of teachers and principals, ratings, classroom observations, student test scores, and district administrative records. Key findings produced from the TLES Study include: (1) the study's performance measures were implemented generally as planned, (2) the study's measures provided some information to identify educators who needed support, but provided limited information to indicate the areas of practice educators most needed to improve, (3) as intended, educators in treatment schools received more frequent feedback with ratings than did those in control schools, and (4)feedback from the study's measures had some positive impacts on teachers' classroom practice, principals' leadership, and student achievement.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
-                    "format": "Restricted Use CD-ROM",
-                    "title": "Impact Evaluation of Teacher and Performance Evaluation Systems (TLES Study)",
-                    "description": "TLES Study data as a restricted-use file",
                     "describedBy": "https://datainventory.ed.gov/Search?txtMenuSearchTerm=&txtSearchTerm=&searchTerm=Impact%20Evaluation%20of%20Teacher%20and%20Leader%20Performance%20Evaluation%20System%20TLES&advanced_search=&rdSearchType=Exact&seriesID=8382&studyID=18831&studyType=study&seriesVar=&seriesVarTerm=&seriesVarType=Exact&studyVar=&studyVarTerm=&studyVarType=Exact&currentSearch=",
                     "describedByType": "text/html",
-                    "downloadURL": "https://nces.ed.gov/pubsearch/licenses.asp"
+                    "description": "TLES Study data as a restricted-use file",
+                    "downloadURL": "https://nces.ed.gov/pubsearch/licenses.asp",
+                    "format": "Restricted Use CD-ROM",
+                    "mediaType": "text/html",
+                    "title": "Impact Evaluation of Teacher and Performance Evaluation Systems (TLES Study)"
                 }
             ],
+            "identifier": "bef5ce25-f4a0-46e5-9c6e-191d9eef5861",
+            "issued": "9999-12-31",
             "keyword": [
                 "34621008-400b-4c5c-b37f-2af6fec112e8",
                 "administrators",
@@ -71479,31 +71455,17 @@
                 "teacher-feedback",
                 "teachers"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-27T15:55:00.655598",
             "programCode": [
                 "018:006"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Integrated Postsecondary Education Data System, 2004-05",
-            "description": "The Integrated Postsecondary Education Data System, 2004-05 (IPEDS 2004-05), was a study that was part of the Integrated Postsecondary Education Data System (IPEDS) program; program data is available since 1980 at <https://nces.ed.gov/ipeds/>. IPEDS 2004-05 (https://nces.ed.gov/ipeds/) was a cross-sectional survey designed to collect basic data from all postsecondary institutions in the United States and the other jurisdictions. Key statistics produced from IPEDS 2004-05 allowed the National Center for Education Statistics (NCES) to describe the size of one of the nation's largest enterprises--postsecondary education-- in terms of students enrolled, degrees and other awards earned, dollars expended, and staff employed. All Title IV institutions were required to respond to IPEDS (see Section 490 of the Higher Education Amendments of 1992 [P.L. 102-325; 20 U.S.C. 1070 et seq.]). IPEDS allowed other, non-Title IV institutions to participate on a voluntary basis, but only about 200 elected to respond.",
-            "modified": "2023-06-27T15:52:01.027324",
-            "accessLevel": "public",
-            "identifier": "998ef5a6-6922-4ff5-970b-8a211db81c97",
-            "dataQuality": true,
-            "issued": "2005-09-29",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2004/2005",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "National Center for Education Statistics (NCES)",
+                "name": "National Center for Education Evaluation and Regional Assistance (NCEERA)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Institute of Education Sciences (IES)",
@@ -71521,28 +71483,44 @@
                     }
                 }
             },
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-10-12/pdf/2012-25186.pdf",
+            "temporal": "2011/2017",
+            "title": "Impact Evaluation of Teacher and Leader Performance Evaluation Systems"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sam Barbett",
                 "hasEmail": "mailto:samuel.barbett@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Integrated Postsecondary Education Data System, 2004-05 (IPEDS 2004-05), was a study that was part of the Integrated Postsecondary Education Data System (IPEDS) program; program data is available since 1980 at <https://nces.ed.gov/ipeds/>. IPEDS 2004-05 (https://nces.ed.gov/ipeds/) was a cross-sectional survey designed to collect basic data from all postsecondary institutions in the United States and the other jurisdictions. Key statistics produced from IPEDS 2004-05 allowed the National Center for Education Statistics (NCES) to describe the size of one of the nation's largest enterprises--postsecondary education-- in terms of students enrolled, degrees and other awards earned, dollars expended, and staff employed. All Title IV institutions were required to respond to IPEDS (see Section 490 of the Higher Education Amendments of 1992 [P.L. 102-325; 20 U.S.C. 1070 et seq.]). IPEDS allowed other, non-Title IV institutions to participate on a voluntary basis, but only about 200 elected to respond.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "IPEDS Data Center",
                     "description": "The IPEDS Data Center allows users to retrieve IPEDS data using a series of predefined and custom functions",
                     "downloadURL": "https://nces.ed.gov/ipeds/use-the-data",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "IPEDS Data Center"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "IPEDS Trend Generator",
                     "description": "The IPEDS Trend Generator is a quick and easy way to see IPEDS data over time",
                     "downloadURL": "https://nces.ed.gov/ipeds/trendgenerator/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "IPEDS Trend Generator"
                 }
             ],
+            "identifier": "998ef5a6-6922-4ff5-970b-8a211db81c97",
+            "issued": "2005-09-29",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "college-enrollment",
@@ -71568,28 +71546,14 @@
                 "student-financial-aid",
                 "title-iv"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-27T15:52:01.027324",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Integrated Postsecondary Education Data System, 2003-04",
-            "description": "The Integrated Postsecondary Education Data System, 2003-04 (IPEDS 2003-04), was a study that was part of the Integrated Postsecondary Education Data System (IPEDS) program; program data is available since 1980 at <https://nces.ed.gov/ipeds/>. IPEDS 2003-04 (https://nces.ed.gov/ipeds/) was a cross-sectional survey designed to collect basic data from all postsecondary institutions in the United States and the other jurisdictions. Key statistics produced from IPEDS 2003-04 allowed the National Center for Education Statistics (NCES) to describe the size of one of the nation's largest enterprises--postsecondary education-- in terms of students enrolled, degrees and other awards earned, dollars expended, and staff employed. All Title IV institutions were required to respond to IPEDS (see Section 490 of the Higher Education Amendments of 1992 [P.L. 102-325; 20 U.S.C.  1070 et seq.]). IPEDS allowed other, non-Title IV institutions to participate on a voluntary basis, but only about 200 elected to respond.",
-            "modified": "2023-06-27T15:51:23.642126",
-            "accessLevel": "public",
-            "identifier": "0ae40fa9-40f7-4658-ba6a-98f4b7f69e79",
-            "dataQuality": true,
-            "issued": "2013-03-14",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2003/2004",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -71610,28 +71574,42 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2004/2005",
+            "title": "Integrated Postsecondary Education Data System, 2004-05"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sam Barbett",
                 "hasEmail": "mailto:samuel.barbett@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Integrated Postsecondary Education Data System, 2003-04 (IPEDS 2003-04), was a study that was part of the Integrated Postsecondary Education Data System (IPEDS) program; program data is available since 1980 at <https://nces.ed.gov/ipeds/>. IPEDS 2003-04 (https://nces.ed.gov/ipeds/) was a cross-sectional survey designed to collect basic data from all postsecondary institutions in the United States and the other jurisdictions. Key statistics produced from IPEDS 2003-04 allowed the National Center for Education Statistics (NCES) to describe the size of one of the nation's largest enterprises--postsecondary education-- in terms of students enrolled, degrees and other awards earned, dollars expended, and staff employed. All Title IV institutions were required to respond to IPEDS (see Section 490 of the Higher Education Amendments of 1992 [P.L. 102-325; 20 U.S.C.  1070 et seq.]). IPEDS allowed other, non-Title IV institutions to participate on a voluntary basis, but only about 200 elected to respond.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "IPEDS Data Center",
                     "description": "The IPEDS Data Center allows users to retrieve IPEDS data using a series of predefined and custom functions",
                     "downloadURL": "https://nces.ed.gov/ipeds/use-the-data",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "IPEDS Data Center"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "IPEDS Trend Generator",
                     "description": "The IPEDS Trend Generator is a quick and easy way to see IPEDS data over time",
                     "downloadURL": "https://nces.ed.gov/ipeds/trendgenerator/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "IPEDS Trend Generator"
                 }
             ],
+            "identifier": "0ae40fa9-40f7-4658-ba6a-98f4b7f69e79",
+            "issued": "2013-03-14",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "college-enrollment",
@@ -71657,28 +71635,14 @@
                 "student-financial-aid",
                 "title-iv"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-27T15:51:23.642126",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Integrated Postsecondary Education Data System, 2006-07",
-            "description": "The Integrated Postsecondary Education Data System, 2006-07 (IPEDS 2006-07), was a study that was part of the Integrated Postsecondary Education Data System (IPEDS) program; program data is available since 1980 at <https://nces.ed.gov/ipeds/>. IPEDS 2006-07 (https://nces.ed.gov/ipeds/) was a cross-sectional survey designed to collect basic data from all postsecondary institutions in the United States and the other jurisdictions. Key statistics produced from IPEDS 2006-07 allowed the National Center for Education Statistics (NCES) to describe the size of one of the nation's largest enterprises--postsecondary education-- in terms of students enrolled, degrees and other awards earned, dollars expended, and staff employed. All Title IV institutions were required to respond to IPEDS (see Section 490 of the Higher Education Amendments of 1992 [P.L. 102-325;1070 et seq.]). IPEDS allowed other, non-Title IV institutions to participate on a voluntary basis, but only about 200 elected to respond.",
-            "modified": "2023-06-27T15:50:49.645746",
-            "accessLevel": "public",
-            "identifier": "0712bac0-2c63-4238-890d-7610599bae77",
-            "dataQuality": true,
-            "issued": "2007-09-11",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2006/2007",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -71699,28 +71663,42 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2003/2004",
+            "title": "Integrated Postsecondary Education Data System, 2003-04"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sam Barbett",
                 "hasEmail": "mailto:samuel.barbett@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Integrated Postsecondary Education Data System, 2006-07 (IPEDS 2006-07), was a study that was part of the Integrated Postsecondary Education Data System (IPEDS) program; program data is available since 1980 at <https://nces.ed.gov/ipeds/>. IPEDS 2006-07 (https://nces.ed.gov/ipeds/) was a cross-sectional survey designed to collect basic data from all postsecondary institutions in the United States and the other jurisdictions. Key statistics produced from IPEDS 2006-07 allowed the National Center for Education Statistics (NCES) to describe the size of one of the nation's largest enterprises--postsecondary education-- in terms of students enrolled, degrees and other awards earned, dollars expended, and staff employed. All Title IV institutions were required to respond to IPEDS (see Section 490 of the Higher Education Amendments of 1992 [P.L. 102-325;1070 et seq.]). IPEDS allowed other, non-Title IV institutions to participate on a voluntary basis, but only about 200 elected to respond.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "IPEDS Data Center",
                     "description": "The IPEDS Data Center allows users to retrieve IPEDS data using a series of predefined and custom functions",
                     "downloadURL": "https://nces.ed.gov/ipeds/use-the-data",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "IPEDS Data Center"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "IPEDS Trend Generator",
                     "description": "The IPEDS Trend Generator is a quick and easy way to see IPEDS data over time",
                     "downloadURL": "https://nces.ed.gov/ipeds/trendgenerator/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "IPEDS Trend Generator"
                 }
             ],
+            "identifier": "0712bac0-2c63-4238-890d-7610599bae77",
+            "issued": "2007-09-11",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "college-enrollment",
@@ -71746,28 +71724,14 @@
                 "student-financial-aid",
                 "title-iv"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-27T15:50:49.645746",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Integrated Postsecondary Education Data System, 2005-06",
-            "description": "The Integrated Postsecondary Education Data System, 2005-06 (IPEDS 2005-06), was a study that was part of the Integrated Postsecondary Education Data System (IPEDS) program; program data is available since 1980 at <https://nces.ed.gov/ipeds/>. IPEDS 2005-06 (https://nces.ed.gov/ipeds/) was a cross-sectional survey designed to collect basic data from all postsecondary institutions in the United States and the other jurisdictions. Key statistics produced from IPEDS 2005-06 allowed the National Center for Education Statistics (NCES) to describe the size of one of the nation's largest enterprises--postsecondary education-- in terms of students enrolled, degrees and other awards earned, dollars expended, and staff employed. All Title IV institutions were required to respond to IPEDS (see Section 490 of the Higher Education Amendments of 1992 [P.L. 102-325; 20 U.S.C. 1070 et seq.]). IPEDS allowed other, non-Title IV institutions to participate on a voluntary basis, but only about 200 elected to respond.",
-            "modified": "2023-06-27T15:50:16.767101",
-            "accessLevel": "public",
-            "identifier": "901b93c5-bc72-4683-a88a-f949804c046a",
-            "dataQuality": true,
-            "issued": "2006-12-27",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2005/2006",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -71788,28 +71752,42 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2006/2007",
+            "title": "Integrated Postsecondary Education Data System, 2006-07"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sam Barbett",
                 "hasEmail": "mailto:samuel.barbett@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Integrated Postsecondary Education Data System, 2005-06 (IPEDS 2005-06), was a study that was part of the Integrated Postsecondary Education Data System (IPEDS) program; program data is available since 1980 at <https://nces.ed.gov/ipeds/>. IPEDS 2005-06 (https://nces.ed.gov/ipeds/) was a cross-sectional survey designed to collect basic data from all postsecondary institutions in the United States and the other jurisdictions. Key statistics produced from IPEDS 2005-06 allowed the National Center for Education Statistics (NCES) to describe the size of one of the nation's largest enterprises--postsecondary education-- in terms of students enrolled, degrees and other awards earned, dollars expended, and staff employed. All Title IV institutions were required to respond to IPEDS (see Section 490 of the Higher Education Amendments of 1992 [P.L. 102-325; 20 U.S.C. 1070 et seq.]). IPEDS allowed other, non-Title IV institutions to participate on a voluntary basis, but only about 200 elected to respond.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "IPEDS Data Center",
                     "description": "The IPEDS Data Center allows users to retrieve IPEDS data using a series of predefined and custom functions",
                     "downloadURL": "https://nces.ed.gov/ipeds/use-the-data",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "IPEDS Data Center"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "IPEDS Trend Generator",
                     "description": "The IPEDS Trend Generator is a quick and easy way to see IPEDS data over time",
                     "downloadURL": "https://nces.ed.gov/ipeds/trendgenerator/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "IPEDS Trend Generator"
                 }
             ],
+            "identifier": "901b93c5-bc72-4683-a88a-f949804c046a",
+            "issued": "2006-12-27",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "college-enrollment",
@@ -71835,28 +71813,14 @@
                 "student-financial-aid",
                 "title-iv"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-27T15:50:16.767101",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Integrated Postsecondary Education Data System, 2007-08",
-            "description": "The Integrated Postsecondary Education Data System, 2007-08 (IPEDS 2007-08), was a study that was part of the Integrated Postsecondary Education Data System (IPEDS) program; program data is available since 1980 at <https://nces.ed.gov/ipeds/>. IPEDS 2007-08 (https://nces.ed.gov/ipeds/) was a cross-sectional survey designed to collect basic data from all postsecondary institutions in the United States and the other jurisdictions. Key statistics produced from IPEDS 2007-08 allowed the National Center for Education Statistics (NCES) to describe the size of one of the nation's largest enterprises--postsecondary education-- in terms of students enrolled, degrees and other awards earned, dollars expended, and staff employed. All Title IV institutions were required to respond to IPEDS (see Section 490 of the Higher Education Amendments of 1992 [P.L. 102-325; 20 U.S.C. 1070 et seq.]). IPEDS allowed other, non-Title IV institutions to participate on a voluntary basis, but only about 200 elected to respond.",
-            "modified": "2023-06-27T15:45:49.557791",
-            "accessLevel": "public",
-            "identifier": "59b9a7b9-5b80-4145-88cf-acb46e719577",
-            "dataQuality": true,
-            "issued": "2008-10-15",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2007/2008",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -71877,28 +71841,42 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2005/2006",
+            "title": "Integrated Postsecondary Education Data System, 2005-06"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sam Barbett",
                 "hasEmail": "mailto:samuel.barbett@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Integrated Postsecondary Education Data System, 2007-08 (IPEDS 2007-08), was a study that was part of the Integrated Postsecondary Education Data System (IPEDS) program; program data is available since 1980 at <https://nces.ed.gov/ipeds/>. IPEDS 2007-08 (https://nces.ed.gov/ipeds/) was a cross-sectional survey designed to collect basic data from all postsecondary institutions in the United States and the other jurisdictions. Key statistics produced from IPEDS 2007-08 allowed the National Center for Education Statistics (NCES) to describe the size of one of the nation's largest enterprises--postsecondary education-- in terms of students enrolled, degrees and other awards earned, dollars expended, and staff employed. All Title IV institutions were required to respond to IPEDS (see Section 490 of the Higher Education Amendments of 1992 [P.L. 102-325; 20 U.S.C. 1070 et seq.]). IPEDS allowed other, non-Title IV institutions to participate on a voluntary basis, but only about 200 elected to respond.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "IPEDS Data Center",
                     "description": "The IPEDS Data Center allows users to retrieve IPEDS data using a series of predefined and custom functions",
                     "downloadURL": "https://nces.ed.gov/ipeds/use-the-data",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "IPEDS Data Center"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "IPEDS Trend Generator",
                     "description": "The IPEDS Trend Generator is a quick and easy way to see IPEDS data over time",
                     "downloadURL": "https://nces.ed.gov/ipeds/trendgenerator/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "IPEDS Trend Generator"
                 }
             ],
+            "identifier": "59b9a7b9-5b80-4145-88cf-acb46e719577",
+            "issued": "2008-10-15",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "college-enrollment",
@@ -71924,28 +71902,14 @@
                 "student-financial-aid",
                 "title-iv"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-27T15:45:49.557791",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Integrated Postsecondary Education Data System, 2008-09",
-            "description": "The Integrated Postsecondary Education Data System, 2008-09 (IPEDS 2008-09), was a study that was part of the Integrated Postsecondary Education Data System (IPEDS) program; program data is available since 1980 at <https://nces.ed.gov/ipeds/>. IPEDS 2008-09 (https://nces.ed.gov/ipeds/) was a cross-sectional survey designed to collect basic data from all postsecondary institutions in the United States and the other jurisdictions. Key statistics produced from IPEDS 2008-09 allowed the National Center for Education Statistics (NCES) to describe the size of one of the nation's largest enterprises--postsecondary education-- in terms of students enrolled, degrees and other awards earned, dollars expended, and staff employed. All Title IV institutions were required to respond to IPEDS (see Section 490 of the Higher Education Amendments of 1992 [P.L. 102-325; 20 U.S.C. 1070 et seq.]). IPEDS allowed other, non-Title IV institutions to participate on a voluntary basis, but only about 200 elected to respond.",
-            "modified": "2023-06-27T15:45:12.883816",
-            "accessLevel": "public",
-            "identifier": "3bc0bf6f-a38c-49b7-8f37-36c9853683fb",
-            "dataQuality": true,
-            "issued": "2009-10-13",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2008/2009",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -71966,28 +71930,42 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2007/2008",
+            "title": "Integrated Postsecondary Education Data System, 2007-08"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sam Barbett",
                 "hasEmail": "mailto:samuel.barbett@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Integrated Postsecondary Education Data System, 2008-09 (IPEDS 2008-09), was a study that was part of the Integrated Postsecondary Education Data System (IPEDS) program; program data is available since 1980 at <https://nces.ed.gov/ipeds/>. IPEDS 2008-09 (https://nces.ed.gov/ipeds/) was a cross-sectional survey designed to collect basic data from all postsecondary institutions in the United States and the other jurisdictions. Key statistics produced from IPEDS 2008-09 allowed the National Center for Education Statistics (NCES) to describe the size of one of the nation's largest enterprises--postsecondary education-- in terms of students enrolled, degrees and other awards earned, dollars expended, and staff employed. All Title IV institutions were required to respond to IPEDS (see Section 490 of the Higher Education Amendments of 1992 [P.L. 102-325; 20 U.S.C. 1070 et seq.]). IPEDS allowed other, non-Title IV institutions to participate on a voluntary basis, but only about 200 elected to respond.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "IPEDS Data Center",
                     "description": "The IPEDS Data Center allows users to retrieve IPEDS data using a series of predefined and custom functions",
                     "downloadURL": "https://nces.ed.gov/ipeds/use-the-data",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "IPEDS Data Center"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "IPEDS Trend Generator",
                     "description": "The IPEDS Trend Generator is a quick and easy way to see IPEDS data over time",
                     "downloadURL": "https://nces.ed.gov/ipeds/trendgenerator/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "IPEDS Trend Generator"
                 }
             ],
+            "identifier": "3bc0bf6f-a38c-49b7-8f37-36c9853683fb",
+            "issued": "2009-10-13",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "college-enrollment",
@@ -72014,28 +71992,14 @@
                 "student-financial-aid",
                 "title-iv"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-27T15:45:12.883816",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Integrated Postsecondary Education Data System, 2009-10",
-            "description": "The Integrated Postsecondary Education Data System, 2009-10 (IPEDS 2009-10), was a study that was part of the Integrated Postsecondary Education Data System (IPEDS) program; program data is available since 1980 at <https://nces.ed.gov/ipeds/>. IPEDS 2009-10 (https://nces.ed.gov/ipeds/) was a cross-sectional survey designed to collect basic data from all postsecondary institutions in the United States and the other jurisdictions. Key statistics produced from IPEDS 2009-10 allowed the National Center for Education Statistics (NCES) to describe the size of one of the nation's largest enterprises--postsecondary education-- in terms of students enrolled, degrees and other awards earned, dollars expended, and staff employed. All Title IV institutions were required to respond to IPEDS (see Section 490 of the Higher Education Amendments of 1992 [P.L. 102-325; 20 U.S.C. 1070 et seq.]). IPEDS allowed other, non-Title IV institutions to participate on a voluntary basis, but only about 200 elected to respond.",
-            "modified": "2023-06-27T15:42:23.954668",
-            "accessLevel": "public",
-            "identifier": "04d7fd13-3edf-4771-9d6b-75625e49dc50",
-            "dataQuality": true,
-            "issued": "2010-08-25",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2009/2010",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -72056,28 +72020,42 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2008/2009",
+            "title": "Integrated Postsecondary Education Data System, 2008-09"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sam Barbett",
                 "hasEmail": "mailto:samuel.barbett@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Integrated Postsecondary Education Data System, 2009-10 (IPEDS 2009-10), was a study that was part of the Integrated Postsecondary Education Data System (IPEDS) program; program data is available since 1980 at <https://nces.ed.gov/ipeds/>. IPEDS 2009-10 (https://nces.ed.gov/ipeds/) was a cross-sectional survey designed to collect basic data from all postsecondary institutions in the United States and the other jurisdictions. Key statistics produced from IPEDS 2009-10 allowed the National Center for Education Statistics (NCES) to describe the size of one of the nation's largest enterprises--postsecondary education-- in terms of students enrolled, degrees and other awards earned, dollars expended, and staff employed. All Title IV institutions were required to respond to IPEDS (see Section 490 of the Higher Education Amendments of 1992 [P.L. 102-325; 20 U.S.C. 1070 et seq.]). IPEDS allowed other, non-Title IV institutions to participate on a voluntary basis, but only about 200 elected to respond.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "IPEDS Data Center",
                     "description": "The IPEDS Data Center allows users to retrieve IPEDS data using a series of predefined and custom functions",
                     "downloadURL": "https://nces.ed.gov/ipeds/use-the-data",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "IPEDS Data Center"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "IPEDS Trend Generator",
                     "description": "The IPEDS Trend Generator is a quick and easy way to see IPEDS data over time",
                     "downloadURL": "https://nces.ed.gov/ipeds/trendgenerator/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "IPEDS Trend Generator"
                 }
             ],
+            "identifier": "04d7fd13-3edf-4771-9d6b-75625e49dc50",
+            "issued": "2010-08-25",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "college-enrollment",
@@ -72104,28 +72082,14 @@
                 "student-financial-aid",
                 "title-iv"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-27T15:42:23.954668",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Integrated Postsecondary Education Data System, 2011-12",
-            "description": "The Integrated Postsecondary Education Data System, 2011-12 (IPEDS 2011-12), was a study that was part of the Integrated Postsecondary Education Data System (IPEDS) program; program data is available since 1980 at <https://nces.ed.gov/ipeds/>. IPEDS 2011-12 (https://nces.ed.gov/ipeds/) was a web-based system designed to collect basic data from all postsecondary institutions in the United States and the other jurisdictions. Key statistics produced from IPEDS 2011-12 allowed the National Center for Education Statistics (NCES) to describe the size of one of the nation's largest enterprises--postsecondary education-- in terms of students enrolled, degrees and other awards earned, dollars expended, and staff employed. All Title IV institutions were required to respond to IPEDS (see Section 490 of the Higher Education Amendments of 1992 [P.L. 102-325; 20 U.S.C. 1070 et seq.]). IPEDS allowed other, non-Title IV institutions to participate on a voluntary basis, but only about 200 elected to respond.",
-            "modified": "2023-06-27T15:41:49.698765",
-            "accessLevel": "public",
-            "identifier": "8564fd9f-0f05-4662-a35c-8fb8ca0db453",
-            "dataQuality": true,
-            "issued": "2012-09-25",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2011/2012",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -72146,28 +72110,42 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2009/2010",
+            "title": "Integrated Postsecondary Education Data System, 2009-10"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sam Barbett",
                 "hasEmail": "mailto:samuel.barbett@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Integrated Postsecondary Education Data System, 2011-12 (IPEDS 2011-12), was a study that was part of the Integrated Postsecondary Education Data System (IPEDS) program; program data is available since 1980 at <https://nces.ed.gov/ipeds/>. IPEDS 2011-12 (https://nces.ed.gov/ipeds/) was a web-based system designed to collect basic data from all postsecondary institutions in the United States and the other jurisdictions. Key statistics produced from IPEDS 2011-12 allowed the National Center for Education Statistics (NCES) to describe the size of one of the nation's largest enterprises--postsecondary education-- in terms of students enrolled, degrees and other awards earned, dollars expended, and staff employed. All Title IV institutions were required to respond to IPEDS (see Section 490 of the Higher Education Amendments of 1992 [P.L. 102-325; 20 U.S.C. 1070 et seq.]). IPEDS allowed other, non-Title IV institutions to participate on a voluntary basis, but only about 200 elected to respond.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "IPEDS Data Center",
                     "description": "The IPEDS Data Center allows users to retrieve IPEDS data using a series of predefined and custom functions",
                     "downloadURL": "https://nces.ed.gov/ipeds/use-the-data",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "IPEDS Data Center"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "IPEDS Trend Generator",
                     "description": "The IPEDS Trend Generator is a quick and easy way to see IPEDS data over time",
                     "downloadURL": "https://nces.ed.gov/ipeds/trendgenerator/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "IPEDS Trend Generator"
                 }
             ],
+            "identifier": "8564fd9f-0f05-4662-a35c-8fb8ca0db453",
+            "issued": "2012-09-25",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "college-enrollment",
@@ -72194,28 +72172,14 @@
                 "student-financial-aid",
                 "title-iv"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-27T15:41:49.698765",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Integrated Postsecondary Education Data System, 2010-11",
-            "description": "The Integrated Postsecondary Education Data System, 2010-11 (IPEDS 2010-11), was a study that was part of the Integrated Postsecondary Education Data System (IPEDS) program; program data is available since 1980 at <https://nces.ed.gov/ipeds/>. IPEDS 2010-11 (https://nces.ed.gov/ipeds/) was a cross-sectional survey designed to collect basic data from all postsecondary institutions in the United States and the other jurisdictions. Key statistics produced from IPEDS 2010-11 allowed the National Center for Education Statistics (NCES) to describe the size of one of the nation's largest enterprises--postsecondary education-- in terms of students enrolled, degrees and other awards earned, dollars expended, and staff employed. All Title IV institutions were required to respond to IPEDS (see Section 490 of the Higher Education Amendments of 1992 [P.L. 102-325; 20 U.S.C. 1070 et seq.]). IPEDS allowed other, non-Title IV institutions to participate on a voluntary basis, but only about 200 elected to respond.",
-            "modified": "2023-06-27T15:41:11.970350",
-            "accessLevel": "public",
-            "identifier": "f76d60e9-a6b1-4703-93df-7633445f49d7",
-            "dataQuality": true,
-            "issued": "2011-09-15",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2010/2011",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -72236,28 +72200,42 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2011/2012",
+            "title": "Integrated Postsecondary Education Data System, 2011-12"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sam Barbett",
                 "hasEmail": "mailto:samuel.barbett@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Integrated Postsecondary Education Data System, 2010-11 (IPEDS 2010-11), was a study that was part of the Integrated Postsecondary Education Data System (IPEDS) program; program data is available since 1980 at <https://nces.ed.gov/ipeds/>. IPEDS 2010-11 (https://nces.ed.gov/ipeds/) was a cross-sectional survey designed to collect basic data from all postsecondary institutions in the United States and the other jurisdictions. Key statistics produced from IPEDS 2010-11 allowed the National Center for Education Statistics (NCES) to describe the size of one of the nation's largest enterprises--postsecondary education-- in terms of students enrolled, degrees and other awards earned, dollars expended, and staff employed. All Title IV institutions were required to respond to IPEDS (see Section 490 of the Higher Education Amendments of 1992 [P.L. 102-325; 20 U.S.C. 1070 et seq.]). IPEDS allowed other, non-Title IV institutions to participate on a voluntary basis, but only about 200 elected to respond.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "IPEDS Data Center",
                     "description": "The IPEDS Data Center allows users to retrieve IPEDS data using a series of predefined and custom functions",
                     "downloadURL": "https://nces.ed.gov/ipeds/use-the-data",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "IPEDS Data Center"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "IPEDS Trend Generator",
                     "description": "The IPEDS Trend Generator is a quick and easy way to see IPEDS data over time",
                     "downloadURL": "https://nces.ed.gov/ipeds/trendgenerator/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "IPEDS Trend Generator"
                 }
             ],
+            "identifier": "f76d60e9-a6b1-4703-93df-7633445f49d7",
+            "issued": "2011-09-15",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "college-enrollment",
@@ -72284,28 +72262,14 @@
                 "student-financial-aid",
                 "title-iv"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-27T15:41:11.970350",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Integrated Postsecondary Education Data System, 2012-13",
-            "description": "The Integrated Postsecondary Education Data System, 2012-13 (IPEDS 2012-13), was a study that was part of the Integrated Postsecondary Education Data System (IPEDS) program; program data is available since 1980 at <https://nces.ed.gov/ipeds/>. IPEDS 2012-13 (https://nces.ed.gov/ipeds/) was a web-based system designed to collect basic data from all postsecondary institutions in the United States and the other jurisdictions. Key statistics produced from IPEDS 2012-13 allowed the National Center for Education Statistics (NCES) to describe the size of one of the nation's largest enterprises--postsecondary education-- in terms of students enrolled, degrees and other awards earned, dollars expended, and staff employed. All Title IV institutions were required to respond to IPEDS (see Section 490 of the Higher Education Amendments of 1992 [P.L. 102-325; 20 U.S.C. 1070 et seq.]). IPEDS allowed other, non-Title IV institutions to participate on a voluntary basis, but only about 200 elected to respond.",
-            "modified": "2023-06-27T15:39:16.855168",
-            "accessLevel": "public",
-            "identifier": "ce8c01a1-4ade-4ac2-9e4f-20b59ae00535",
-            "dataQuality": true,
-            "issued": "2013-05-23",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2012/2013",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -72326,28 +72290,42 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2010/2011",
+            "title": "Integrated Postsecondary Education Data System, 2010-11"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sam Barbett",
                 "hasEmail": "mailto:samuel.barbett@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Integrated Postsecondary Education Data System, 2012-13 (IPEDS 2012-13), was a study that was part of the Integrated Postsecondary Education Data System (IPEDS) program; program data is available since 1980 at <https://nces.ed.gov/ipeds/>. IPEDS 2012-13 (https://nces.ed.gov/ipeds/) was a web-based system designed to collect basic data from all postsecondary institutions in the United States and the other jurisdictions. Key statistics produced from IPEDS 2012-13 allowed the National Center for Education Statistics (NCES) to describe the size of one of the nation's largest enterprises--postsecondary education-- in terms of students enrolled, degrees and other awards earned, dollars expended, and staff employed. All Title IV institutions were required to respond to IPEDS (see Section 490 of the Higher Education Amendments of 1992 [P.L. 102-325; 20 U.S.C. 1070 et seq.]). IPEDS allowed other, non-Title IV institutions to participate on a voluntary basis, but only about 200 elected to respond.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "IPEDS Data Center",
                     "description": "The IPEDS Data Center allows users to retrieve IPEDS data using a series of predefined and custom functions",
                     "downloadURL": "https://nces.ed.gov/ipeds/use-the-data",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "IPEDS Data Center"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "IPEDS Trend Generator",
                     "description": "The IPEDS Trend Generator is a quick and easy way to see IPEDS data over time",
                     "downloadURL": "https://nces.ed.gov/ipeds/trendgenerator/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "IPEDS Trend Generator"
                 }
             ],
+            "identifier": "ce8c01a1-4ade-4ac2-9e4f-20b59ae00535",
+            "issued": "2013-05-23",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "college-enrollment",
@@ -72374,28 +72352,14 @@
                 "student-financial-aid",
                 "title-iv"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-27T15:39:16.855168",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Integrated Postsecondary Education Data System, 2013-14",
-            "description": "The Integrated Postsecondary Education Data System, 2013-14 (IPEDS 2013-14), was a study that was part of the Integrated Postsecondary Education Data System (IPEDS) program; program data is available since 1980 at6 <https://nces.ed.gov/ipeds/>. IPEDS 2013-14 (https://nces.ed.gov/ipeds/) was a web-based system designed to collect basic data from all postsecondary institutions in the United States and the other jurisdictions. Key statistics produced from IPEDS 2013-14 allowed the National Center for Education Statistics (NCES) to describe the size of one of the nation's largest enterprises--postsecondary education-- in terms of students enrolled, degrees and other awards earned, dollars expended, and staff employed. All Title IV institutions were required to respond to IPEDS (see Section 490 of the Higher Education Amendments of 1992 [P.L. 102-325; 20 U.S.C. 1070 et seq.]). IPEDS allowed other, non-Title IV institutions to participate on a voluntary basis, but only about 200 elected to respond.",
-            "modified": "2023-06-27T15:38:06.345066",
-            "accessLevel": "public",
-            "identifier": "12f5c5c1-15d0-4e4e-8e6a-4781cb9d367a",
-            "dataQuality": true,
-            "issued": "2014-06-04",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2013/2014",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -72416,35 +72380,49 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2012/2013",
+            "title": "Integrated Postsecondary Education Data System, 2012-13"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sam Barbett",
                 "hasEmail": "mailto:samuel.barbett@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Integrated Postsecondary Education Data System, 2013-14 (IPEDS 2013-14), was a study that was part of the Integrated Postsecondary Education Data System (IPEDS) program; program data is available since 1980 at6 <https://nces.ed.gov/ipeds/>. IPEDS 2013-14 (https://nces.ed.gov/ipeds/) was a web-based system designed to collect basic data from all postsecondary institutions in the United States and the other jurisdictions. Key statistics produced from IPEDS 2013-14 allowed the National Center for Education Statistics (NCES) to describe the size of one of the nation's largest enterprises--postsecondary education-- in terms of students enrolled, degrees and other awards earned, dollars expended, and staff employed. All Title IV institutions were required to respond to IPEDS (see Section 490 of the Higher Education Amendments of 1992 [P.L. 102-325; 20 U.S.C. 1070 et seq.]). IPEDS allowed other, non-Title IV institutions to participate on a voluntary basis, but only about 200 elected to respond.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "College Navigator",
                     "description": "College Navigator consists primarily of the latest data from the Integrated Postsecondary Education Data System (IPEDS), the core postsecondary education data collection program for NCES--the National Center for Education Statistics",
                     "downloadURL": "https://nces.ed.gov/collegenavigator/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "College Navigator"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "IPEDS Data Center",
                     "description": "The IPEDS Data Center allows users to retrieve IPEDS data using a series of predefined and custom functions",
                     "downloadURL": "https://nces.ed.gov/ipeds/use-the-data",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "IPEDS Data Center"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "IPEDS Trend Generator",
                     "description": "The IPEDS Trend Generator is a quick and easy way to see IPEDS data over time",
                     "downloadURL": "https://nces.ed.gov/ipeds/trendgenerator/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "IPEDS Trend Generator"
                 }
             ],
+            "identifier": "12f5c5c1-15d0-4e4e-8e6a-4781cb9d367a",
+            "issued": "2014-06-04",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "college-enrollment",
@@ -72471,30 +72449,14 @@
                 "student-financial-aid",
                 "title-iv"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-27T15:38:06.345066",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Adult Literacy and Lifeskills Survey, 2003",
-            "description": "The Adult Literacy and Lifeskills Survey, 2003 (ALL), is an international comparative study designed to provide participating countries, including the United States, with information about the skills of their adult populations. ALL measured the literacy and numeracy skills of a nationally representative sample from each participating country.",
-            "modified": "2023-06-27T15:33:13.341619",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "f74692f8-b1ab-4a02-8dcd-d20d5c94f21d",
-            "dataQuality": true,
-            "issued": "2010-05-03",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2002/2003",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -72515,21 +72477,35 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2013/2014",
+            "title": "Integrated Postsecondary Education Data System, 2013-14"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Holly Xie",
                 "hasEmail": "mailto:holly.xie@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Adult Literacy and Lifeskills Survey, 2003 (ALL), is an international comparative study designed to provide participating countries, including the United States, with information about the skills of their adult populations. ALL measured the literacy and numeracy skills of a nationally representative sample from each participating country.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Adult Literacy and Lifeskills Survey Restricted-Use Data File and User's Guide: 2003",
                     "description": "Restricted-Use Data File and User's Guide for the 2003 Adult Literacy and Lifeskills Survey.",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2009071",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Adult Literacy and Lifeskills Survey Restricted-Use Data File and User's Guide: 2003"
                 }
             ],
+            "identifier": "f74692f8-b1ab-4a02-8dcd-d20d5c94f21d",
+            "issued": "2010-05-03",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "adult-education",
@@ -72537,29 +72513,14 @@
                 "assessment",
                 "international-comparisons"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-27T15:33:13.341619",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Education Longitudinal Study of 2002",
-            "description": "The Education Longitudinal Study of 2002 (ELS:2002; https://nces.ed.gov/surveys/els2002/) is a study that is a part of the Education Longitudinal Study program. It is a longitudinal survey that monitors the transitions of a national sample of young people as they progress from tenth grade to, eventually, the world of work. In 2004, the sample was augmented to make it representative of seniors as well. The study was conducted using self-administered questionnaires and cognitive tests of students, parents, teachers, librarians, and school administrators. Students and their high school administrators, library media coordinators, mathematics and English teachers, and parents in the spring term of the 2002 school year were sampled. The study's base year weighted response rate was 87.3 percent for students, 98.5 percent for school administrators, 95.9 percent for library media coordinators, 91.6 percent for both mathematics and English teachers, 87.5 percent for parents, and 67.8 percent for schools. Key statistics produced from ELS:2002 focus on the changes taking place in the lives of students which can be understood by life achievements, aspirations, and experiences.",
-            "modified": "2023-06-27T15:32:19.485319",
-            "accessLevel": "public",
-            "identifier": "b9d2c00c-aeca-40a2-9210-84028bc6e2e2",
-            "dataQuality": true,
-            "issued": "2004-11-12",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2002/2013",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -72580,18 +72541,32 @@
                     }
                 }
             },
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2002/2003",
+            "title": "Adult Literacy and Lifeskills Survey, 2003"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elise Christopher",
                 "hasEmail": "mailto:elise.christopher@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Education Longitudinal Study of 2002 (ELS:2002; https://nces.ed.gov/surveys/els2002/) is a study that is a part of the Education Longitudinal Study program. It is a longitudinal survey that monitors the transitions of a national sample of young people as they progress from tenth grade to, eventually, the world of work. In 2004, the sample was augmented to make it representative of seniors as well. The study was conducted using self-administered questionnaires and cognitive tests of students, parents, teachers, librarians, and school administrators. Students and their high school administrators, library media coordinators, mathematics and English teachers, and parents in the spring term of the 2002 school year were sampled. The study's base year weighted response rate was 87.3 percent for students, 98.5 percent for school administrators, 95.9 percent for library media coordinators, 91.6 percent for both mathematics and English teachers, 87.5 percent for parents, and 67.8 percent for schools. Key statistics produced from ELS:2002 focus on the changes taking place in the lives of students which can be understood by life achievements, aspirations, and experiences.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Education Longitudinal Study: 2002 Data Files and Electronic Codebook System",
                     "description": "Education Longitudinal Study of 2002 data files and electronic codebook",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2015035",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Education Longitudinal Study: 2002 Data Files and Electronic Codebook System"
                 },
                 {
                     "@type": "dcat:Distribution",
@@ -72600,6 +72575,8 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "b9d2c00c-aeca-40a2-9210-84028bc6e2e2",
+            "issued": "2004-11-12",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "dropouts",
@@ -72611,30 +72588,14 @@
                 "students",
                 "teachers"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-27T15:32:19.485319",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "High School and Beyond",
-            "description": "High School and Beyond (HS&B) is a study that is part of the Longitudinal Studies Branch (LSB) program; program data is available since 1980 at https://nces.ed.gov/pubsearch/getpubcats.asp?sid=022. HS&B (https://nces.ed.gov/surveys/hsb/) is a longitudinal survey. HS&B survey included two cohorts: the 1980 senior class, and the 1980 sophomore class. Both cohorts were surveyed every two years through 1986, and the 1980 sophomore class was also surveyed again in 1992.",
-            "modified": "2023-06-27T15:29:04.892415",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "1fdf85a6-0f4d-40d7-9012-0807a603120f",
-            "dataQuality": true,
-            "issued": "1995-06-15",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/sorn/18-13-01_060499.pdf",
-            "temporal": "1980/1992",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -72655,29 +72616,44 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2002/2013",
+            "title": "Education Longitudinal Study of 2002"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elise Christopher",
                 "hasEmail": "mailto:elise.christopher@ed.gov"
             },
+            "dataQuality": true,
+            "description": "High School and Beyond (HS&B) is a study that is part of the Longitudinal Studies Branch (LSB) program; program data is available since 1980 at https://nces.ed.gov/pubsearch/getpubcats.asp?sid=022. HS&B (https://nces.ed.gov/surveys/hsb/) is a longitudinal survey. HS&B survey included two cohorts: the 1980 senior class, and the 1980 sophomore class. Both cohorts were surveyed every two years through 1986, and the 1980 sophomore class was also surveyed again in 1992.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "Data Analysis System (DAS)",
                     "description": "High School and Beyond study sophomore cohort data available on the Data Analysis System",
                     "downloadURL": "https://nces.ed.gov/dasolv2/tables/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "Data Analysis System (DAS)"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "CD-ROM: High School & Beyond: 1992 (Restricted) Data File",
                     "description": "Restricted-use data file for all follow-ups of the High School and Beyond study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=95361",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "CD-ROM: High School & Beyond: 1992 (Restricted) Data File"
                 }
             ],
+            "identifier": "1fdf85a6-0f4d-40d7-9012-0807a603120f",
+            "issued": "1995-06-15",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "academic-achievement",
@@ -72688,33 +72664,14 @@
                 "occupation",
                 "postsecondary-education"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/dasolv2/help/guide_1.asp"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "High School Longitudinal Study of 2009",
-            "description": "The High School Longitudinal Study of 2009 (HSLS:09) is part of the High School Longitudinal Study (HSLS) program. HSLS:09 (https://nces.ed.gov/surveys/hsls09/) is a longitudinal survey that follows more than 21,000 9th graders in 944 schools throughout their secondary and postsecondary years. The study focuses on understanding students' trajectories from the beginning of high school into postsecondary education, the workforce, and beyond. Key statistics produced from the HSLS:09 are what students decide to pursue when, why, and how.",
-            "modified": "2023-06-27T15:27:24.241017",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "d2487e2b-74e5-463c-bbfc-4a2a7f3ce164",
-            "dataQuality": true,
-            "issued": "2011-08-24",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2009/2014",
+            "modified": "2023-06-27T15:29:04.892415",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -72735,112 +72692,116 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/dasolv2/help/guide_1.asp"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/sorn/18-13-01_060499.pdf",
+            "temporal": "1980/1992",
+            "title": "High School and Beyond"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elise Christopher",
                 "hasEmail": "mailto:elise.christopher@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The High School Longitudinal Study of 2009 (HSLS:09) is part of the High School Longitudinal Study (HSLS) program. HSLS:09 (https://nces.ed.gov/surveys/hsls09/) is a longitudinal survey that follows more than 21,000 9th graders in 944 schools throughout their secondary and postsecondary years. The study focuses on understanding students' trajectories from the beginning of high school into postsecondary education, the workforce, and beyond. Key statistics produced from the HSLS:09 are what students decide to pursue when, why, and how.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "High School Longitudinal Study of 2009 (HSLS:09): Public-Use Data File",
                     "description": "High School Longitudinal Study of 2009 public-use data",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2011334",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "High School Longitudinal Study of 2009 (HSLS:09): Public-Use Data File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "High School Longitudinal Study of 2009 (HSLS:09): Restricted-Use Data File",
                     "description": "High School Longitudinal Study of 2009 restricted-use data",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2011333",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "High School Longitudinal Study of 2009 (HSLS:09): Restricted-Use Data File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "High School Longitudinal Study of 2009 (HSLS:09): 2013 Update and High School Transcripts Restricted-Use Data File",
                     "description": "High School Longitudinal Study of 2009 (HSLS:09) 2013 Update and High School Transcripts Restricted-use Data File",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2015038",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "High School Longitudinal Study of 2009 (HSLS:09): 2013 Update and High School Transcripts Restricted-Use Data File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "High School Longitudinal Study of 2009 (HSLS:09): 2013 Updated and High School Transcripts Public-Use Data File",
                     "description": "High School Longitudinal Study of 2009 (HSLS:09) 2013 Update and High School Transcripts Public-use Data File",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2015315",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "High School Longitudinal Study of 2009 (HSLS:09): 2013 Updated and High School Transcripts Public-Use Data File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Zipped SPSS",
                     "description": "High School Longitudinal Study of 2009 (HSLS:09) Base-Year to Second Follow-Up Public-Use Data File",
                     "downloadURL": "https://nces.ed.gov/EDAT/Data/Zip/HSLS_2016_v1_0_SPSS_Datasets.zip",
+                    "format": "Zipped SPSS",
                     "mediaType": "text/plain"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Zipped SAS",
                     "description": "High School Longitudinal Study of 2009 (HSLS:09) Base-Year to Second Follow-Up Public-Use Data File",
                     "downloadURL": "https://nces.ed.gov/EDAT/Data/Zip/HSLS_2016_v1_0_SAS_Datasets.zip",
+                    "format": "Zipped SAS",
                     "mediaType": "text/plain"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Zipped Stata",
                     "description": "High School Longitudinal Study of 2009 (HSLS:09) Base-Year to Second Follow-Up Public-Use Data File",
                     "downloadURL": "https://nces.ed.gov/EDAT/Data/Zip/HSLS_2016_v1_0_Stata_Datasets.zip",
+                    "format": "Zipped Stata",
                     "mediaType": "text/plain"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Zipped R",
                     "description": "High School Longitudinal Study of 2009 (HSLS:09) Base-Year to Second Follow-Up Public-Use Data File",
                     "downloadURL": "https://nces.ed.gov/EDAT/Data/Zip/HSLS_2016_v1_0_R_Datasets.zip",
+                    "format": "Zipped R",
                     "mediaType": "text/plain"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Zipped ASCII",
                     "description": "High School Longitudinal Study of 2009 (HSLS:09) Base-Year to Second Follow-Up Public-Use Data File",
                     "downloadURL": "https://nces.ed.gov/EDAT/Data/Zip/HSLS_2016_v1_0_ASCII_Datasets.zip",
+                    "format": "Zipped ASCII",
                     "mediaType": "text/plain"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Zipped CSV",
                     "description": "High School Longitudinal Study of 2009 (HSLS:09) Base-Year to Second Follow-Up Public-Use Data File",
                     "downloadURL": "https://nces.ed.gov/EDAT/Data/Zip/HSLS_2016_v1_0_CSV_Datasets.zip",
+                    "format": "Zipped CSV",
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "d2487e2b-74e5-463c-bbfc-4a2a7f3ce164",
+            "issued": "2011-08-24",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "assessments",
                 "educational-attainment",
                 "secondary-school"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-27T15:27:24.241017",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Education Longitudinal Study of 1988",
-            "description": "The National Education Longitudinal Study of 1988 (NELS:88) is a study that is part of the Longitudinal Studies Branch (LSB) program; program data is available since 1988 at <https://nces.ed.gov/surveys/nels88/data_products.asp>. NELS:88 (https://nces.ed.gov/surveys/nels88/) is a longitudinal study that is designed to provide trend data about critical transitions experienced by students as they leave middle or junior high school, and progress through high school and into postsecondary institutions or the work force. A nationally representative sample of eighth-graders were first surveyed in the spring of 1988. A sample of these respondents were then resurveyed through four follow-ups in 1990, 1992, 1994, and 2000. Overall weighted response rate was unavailable as of December 2014. Key statistics produced from NELS:88 data can be used for policy-relevant research about educational processes and outcomes, for example: student learning; early and late predictors of dropping out; and school effects on students' access to programs and equal opportunity to learn.",
-            "modified": "2023-06-27T15:26:32.184383",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "517e5849-1a10-4dcb-a2eb-d84278a8403e",
-            "dataQuality": true,
-            "issued": "1996-03-12",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "1987/2001",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -72861,57 +72822,73 @@
                     }
                 }
             },
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2009/2014",
+            "title": "High School Longitudinal Study of 2009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elise Christopher",
                 "hasEmail": "mailto:elise.christopher@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Education Longitudinal Study of 1988 (NELS:88) is a study that is part of the Longitudinal Studies Branch (LSB) program; program data is available since 1988 at <https://nces.ed.gov/surveys/nels88/data_products.asp>. NELS:88 (https://nces.ed.gov/surveys/nels88/) is a longitudinal study that is designed to provide trend data about critical transitions experienced by students as they leave middle or junior high school, and progress through high school and into postsecondary institutions or the work force. A nationally representative sample of eighth-graders were first surveyed in the spring of 1988. A sample of these respondents were then resurveyed through four follow-ups in 1990, 1992, 1994, and 2000. Overall weighted response rate was unavailable as of December 2014. Key statistics produced from NELS:88 data can be used for policy-relevant research about educational processes and outcomes, for example: student learning; early and late predictors of dropping out; and school effects on students' access to programs and equal opportunity to learn.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "Data Analysis System (DAS)",
                     "description": "National Education Longitudinal Study of 1988 year 2000 follow-up data available on the Data Analysis System",
                     "downloadURL": "https://nces.ed.gov/dasolv2/tables/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "Data Analysis System (DAS)"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "CD-ROM: NELS:88/94 Restricted Use",
                     "description": "Restricted-use data for the National Education Longitudinal Study of 1988 base year through third follow-up (1994)",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=96130",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "CD-ROM: NELS:88/94 Restricted Use"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "CD-ROM: NELS:88/94 Data Analysis System, with Additional Systems for High School and Beyond and the National Longitudinal Study of 1972",
                     "description": "Data Analysis System for the 1994 follow-up to the National Education Longitudinal Study of 1988",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=96127",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "CD-ROM: NELS:88/94 Data Analysis System, with Additional Systems for High School and Beyond and the National Longitudinal Study of 1972"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "CD-ROM: NELS:88/94 Public Use Data Files and Electronic Codebook - Base Year through Third Follow-up",
                     "description": "CD-ROM containing public use data files and electronic codebook for the National Education Longitudinal Study of 1988 base year through third follow-up (1994)",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2000328rev",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "CD-ROM: NELS:88/94 Public Use Data Files and Electronic Codebook - Base Year through Third Follow-up"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "CD-ROM: NELS:88/2000 Public Use Data Files and Electronic Codebook - Base Year through Fourth Follow-up",
                     "description": "CD-ROM containing public use data files and electronic codebook for the National Education Longitudinal Study of 1988 base year through fourth follow-up (2000)",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2002322rev",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "CD-ROM: NELS:88/2000 Public Use Data Files and Electronic Codebook - Base Year through Fourth Follow-up"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "CD-ROM: NELS:88/2000 Restricted Use Data Files and Electronic Codebook",
                     "description": "Restricted-use data file and electronic codebook for the National Education Longitudinal Study of 1988 base year through fourth follow-up (2000)",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2003348",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "CD-ROM: NELS:88/2000 Restricted Use Data Files and Electronic Codebook"
                 }
             ],
+            "identifier": "517e5849-1a10-4dcb-a2eb-d84278a8403e",
+            "issued": "1996-03-12",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "assessments",
@@ -72928,33 +72905,14 @@
                 "the-role-in-education-of-their-parents-and-peers",
                 "work"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2000193"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "The National Longitudinal Study of the High School Class of 1972",
-            "description": "The National Longitudinal Study of the High School Class of 1972 (NLS-72) is part of the Secondary Longitudinal Studies (SLS) program; program data is available since 1972 at https://nces.ed.gov/pubsearch/getpubcats.asp?sid=021. The National Longitudinal Study of the High School Class of 1972 (NLS-72) (https://nces.ed.gov/surveys/nls72/index.asp) is a longitudinal survey that follows high school seniors through 5 follow-ups in 1973, 1974, 1976, 1979, and 1986.  The study was conducted using a national representative sample of 1972 high school seniors. Key statistics produced from the National Longitudinal Study of High School Class of 1972 are student's educational aspirations and attainment, family formation, and occupations.",
-            "modified": "2023-06-27T15:25:44.847247",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "f0f28b73-254f-453e-9c76-ee0953954e5b",
-            "dataQuality": true,
-            "issued": "1994-03-18",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/sorn/18-13-01_060499.pdf",
-            "temporal": "1971/1986",
+            "modified": "2023-06-27T15:26:32.184383",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -72975,21 +72933,39 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2000193"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "temporal": "1987/2001",
+            "title": "National Education Longitudinal Study of 1988"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Elise Christopher",
                 "hasEmail": "mailto:elise.christopher@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Longitudinal Study of the High School Class of 1972 (NLS-72) is part of the Secondary Longitudinal Studies (SLS) program; program data is available since 1972 at https://nces.ed.gov/pubsearch/getpubcats.asp?sid=021. The National Longitudinal Study of the High School Class of 1972 (NLS-72) (https://nces.ed.gov/surveys/nls72/index.asp) is a longitudinal survey that follows high school seniors through 5 follow-ups in 1973, 1974, 1976, 1979, and 1986.  The study was conducted using a national representative sample of 1972 high school seniors. Key statistics produced from the National Longitudinal Study of High School Class of 1972 are student's educational aspirations and attainment, family formation, and occupations.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NLS-72 Restricted-Use Data File",
                     "description": "Restricted-use data file for the National Longitudinal Study of the High School Class of 1972 longitudinal data collections.",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=1994487rev",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NLS-72 Restricted-Use Data File"
                 }
             ],
+            "identifier": "f0f28b73-254f-453e-9c76-ee0953954e5b",
+            "issued": "1994-03-18",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "background-characteristics",
@@ -73004,28 +72980,14 @@
                 "secondary-education",
                 "vocational-activities"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-27T15:25:44.847247",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Assessment of Adult Literacy, 2003",
-            "description": "National Assessment of Adult Literacy, 2003 (NAAL:2003), is a study that is part of the National Assessment of Adult Literacy program. NAAL:2003 (https://nces.ed.gov/naal/) is a cross-sectional assessment that collected information about English literacy among American adults age 16 and older. The study was conducted using direct assessment from 19,000 adults 16 or older, in their homes and some in prisons from the 50 states and District of Columbia. Households and prison inmates were sampled in 2003. The weighted response rate was 62.1 percent for households and 88.3 percent for prison inmates. Key statistics produced from NAAL:2003 include reading skills, general literacy, relationships, demographics, and background characteristics.",
-            "modified": "2023-06-27T15:24:59.794843",
-            "accessLevel": "public",
-            "identifier": "ea330636-edd4-4edb-99e3-70f6b7b48195",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf ",
-            "temporal": "2002/2003",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -73046,59 +73008,58 @@
                     }
                 }
             },
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/sorn/18-13-01_060499.pdf",
+            "temporal": "1971/1986",
+            "title": "The National Longitudinal Study of the High School Class of 1972"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jing Chen",
                 "hasEmail": "mailto:jing.chen@ed.gov"
             },
+            "dataQuality": true,
+            "description": "National Assessment of Adult Literacy, 2003 (NAAL:2003), is a study that is part of the National Assessment of Adult Literacy program. NAAL:2003 (https://nces.ed.gov/naal/) is a cross-sectional assessment that collected information about English literacy among American adults age 16 and older. The study was conducted using direct assessment from 19,000 adults 16 or older, in their homes and some in prisons from the 50 states and District of Columbia. Households and prison inmates were sampled in 2003. The weighted response rate was 62.1 percent for households and 88.3 percent for prison inmates. Key statistics produced from NAAL:2003 include reading skills, general literacy, relationships, demographics, and background characteristics.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped TSV",
-                    "title": "NAAL_2003_PDQ.zip",
                     "description": "The 2003 combined household-prison public use file",
-                    "downloadURL": "https://nces.ed.gov/naal/data/NAAL_2003_PDQ.zip"
+                    "downloadURL": "https://nces.ed.gov/naal/data/NAAL_2003_PDQ.zip",
+                    "format": "Zipped TSV",
+                    "mediaType": "application/zip",
+                    "title": "NAAL_2003_PDQ.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped TSV",
-                    "title": "NAAL_2003_Health.zip",
                     "description": "A separate 2003 public-use file Zip File (5.3 MB) permits estimates of proficiency on the health literacy scale.",
-                    "downloadURL": "https://nces.ed.gov/naal/data/NAAL_2003_Health.zip"
+                    "downloadURL": "https://nces.ed.gov/naal/data/NAAL_2003_Health.zip",
+                    "format": "Zipped TSV",
+                    "mediaType": "application/zip",
+                    "title": "NAAL_2003_Health.zip"
                 }
             ],
+            "identifier": "ea330636-edd4-4edb-99e3-70f6b7b48195",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "adult-literacy",
                 "assessment"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-27T15:24:59.794843",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Assessment of Educational Progress, 2003",
-            "description": "The National Assessment of Educational Progress, 2003 (NAEP 2003), is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data is available since 1990 at https://nces.ed.gov/nationsreportcard/naepdata/. NAEP 2003 (https://nces.ed.gov/nationsreportcard/) is a cross-sectional survey that assesses what America's students know and can do in various subject areas. The study was conducted using computer-based assessment of students. Students in grades 4, 8, and 12 were sampled. The study's response rate was between 90 and 92 percent. Key statistics produced from NAEP 2003 are results on subject-matter achievement, instructional experiences, and school environment for populations of students (e.g., all fourth-graders) and groups within those populations (e.g., female students, Hispanic students).",
-            "modified": "2023-06-27T15:24:10.650282",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "fa41622a-03dc-4ca7-9c9d-bfcc4d18c13e",
-            "dataQuality": true,
-            "issued": "2006-08-22",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
-            "temporal": "2002/2003",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -73119,50 +73080,65 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf ",
+            "temporal": "2002/2003",
+            "title": "National Assessment of Adult Literacy, 2003"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Linda Hamilton",
                 "hasEmail": "mailto:linda.hamilton@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Assessment of Educational Progress, 2003 (NAEP 2003), is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data is available since 1990 at https://nces.ed.gov/nationsreportcard/naepdata/. NAEP 2003 (https://nces.ed.gov/nationsreportcard/) is a cross-sectional survey that assesses what America's students know and can do in various subject areas. The study was conducted using computer-based assessment of students. Students in grades 4, 8, and 12 were sampled. The study's response rate was between 90 and 92 percent. Key statistics produced from NAEP 2003 are results on subject-matter achievement, instructional experiences, and school environment for populations of students (e.g., all fourth-graders) and groups within those populations (e.g., female students, Hispanic students).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "NAEP Data Explorer",
                     "description": "2003 National Assessment of Educational Progress data available through the NAEP Data Explorer",
                     "downloadURL": "https://nces.ed.gov/nationsreportcard/naepdata/dataset.aspx",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "NAEP Data Explorer"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2003 National and State Mathematics Assessments (Grade 4): Restricted-Use Data Files",
                     "description": "Restricted-use data file for Grade 4 mathematics assessments from the 2003 National Assessment of Educational Progress study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2004562rev",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2003 National and State Mathematics Assessments (Grade 4): Restricted-Use Data Files"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2003 National and State Mathematics Assessments (Grade 8): Restricted-Use Data Files",
                     "description": "Restricted-use data file for Grade 8 mathematics assessments from the 2003 National Assessment of Educational Progress study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2004563rev",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2003 National and State Mathematics Assessments (Grade 8): Restricted-Use Data Files"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2003 National and State Reading Assessments (Grade 4): Restricted-Use Data Files",
                     "description": "Restricted-use data file for Grade 4 reading assessments from the 2003 National Assessment of Educational Progress study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2004564rev",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2003 National and State Reading Assessments (Grade 4): Restricted-Use Data Files"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2003 National and State Reading Assessments (Grade 8): Restricted-Use Data Files",
                     "description": "Restricted-use data file for Grade 8 reading assessments from the 2003 National Assessment of Educational Progress study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2004565rev",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2003 National and State Reading Assessments (Grade 8): Restricted-Use Data Files"
                 }
             ],
+            "identifier": "fa41622a-03dc-4ca7-9c9d-bfcc4d18c13e",
+            "issued": "2006-08-22",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "assessment",
@@ -73171,33 +73147,14 @@
                 "reading",
                 "students"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Assessment of Educational Progress, 2004 Long-Term Trend Study",
-            "description": "The National Assessment of Educational Progress, 2004 Long-Term Trend Study (NAEP 2004 LTT), is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data is available since 1971 at https://nces.ed.gov/nationsreportcard/naepdata/. NAEP 2004 LTT (https://nces.ed.gov/nationsreportcard/ltt) is a cross-sectional survey that assesses what America's students know and can do in reading and mathematics. NAEP 2004 LTT was administered to students aged 9, 13, and 17 who were enrolled in public and private elementary and secondary schools throughout the nation.",
-            "modified": "2023-06-27T15:21:04.518207",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "68759445-d239-4c1d-a4bb-b5e6efe60cd5",
-            "dataQuality": true,
-            "issued": "2008-05-21",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
-            "temporal": "2003/2004",
+            "modified": "2023-06-27T15:24:10.650282",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -73218,82 +73175,82 @@
                     }
                 }
             },
-            "accrualPeriodicity": "R/P4Y",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Linda Hamilton",
-                "hasEmail": "mailto:linda.hamilton@ed.gov"
-            },
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "NAEP Data Explorer",
+            "references": [
+                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
+            "temporal": "2002/2003",
+            "title": "National Assessment of Educational Progress, 2003"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "accrualPeriodicity": "R/P4Y",
+            "bureauCode": [
+                "018:50"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Linda Hamilton",
+                "hasEmail": "mailto:linda.hamilton@ed.gov"
+            },
+            "dataQuality": true,
+            "description": "The National Assessment of Educational Progress, 2004 Long-Term Trend Study (NAEP 2004 LTT), is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data is available since 1971 at https://nces.ed.gov/nationsreportcard/naepdata/. NAEP 2004 LTT (https://nces.ed.gov/nationsreportcard/ltt) is a cross-sectional survey that assesses what America's students know and can do in reading and mathematics. NAEP 2004 LTT was administered to students aged 9, 13, and 17 who were enrolled in public and private elementary and secondary schools throughout the nation.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
                     "description": "National Assessment of Educational Progress, 2004 Long-Term Trend study data available through the NAEP Data Explorer",
                     "downloadURL": "https://nces.ed.gov/nationsreportcard/lttdata/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "NAEP Data Explorer"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 1978-2004 Mathematics Long-Term Trend Restricted-Use Data File",
                     "description": "Restricted-use data file for mathematics for the National Assessment of Education Progress, 2004 Long-Term Trend study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2008486",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 1978-2004 Mathematics Long-Term Trend Restricted-Use Data File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 1978-2004 Reading Long-Term Trend Restricted-Use Data File",
                     "description": "Restricted-use data file for reading for the National Assessment of Education Progress, 2004 Long-Term Trend study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2008479",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 1978-2004 Reading Long-Term Trend Restricted-Use Data File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP Mathematics Long-Term Trend Restricted Use Data File: 1978-2008",
                     "description": "Restricted-use data file for mathematics for the National Assessment of Education Progress, 2004 Long-Term Trend study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2012462",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP Mathematics Long-Term Trend Restricted Use Data File: 1978-2008"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP Reading Long-Term Trend Restricted Use Data File: 1971-2008",
                     "description": "Restricted-use data file for reading for the National Assessment of Education Progress, 2004 Long-Term Trend study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2012463",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP Reading Long-Term Trend Restricted Use Data File: 1971-2008"
                 }
             ],
+            "identifier": "68759445-d239-4c1d-a4bb-b5e6efe60cd5",
+            "issued": "2008-05-21",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "mathematics-assessment",
                 "reading-assessment"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Assessment of Educational Progress, 2005 High School Transcript Study",
-            "description": "The National Assessment of Educational Progress, 2005 High School Transcript Study (HSTS 2005), is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data available since 1990 at <https://nces.ed.gov/nationsreportcard/naepdata/>. HSTS 2005 (https://nces.ed.gov/nationsreportcard/hsts/) is a cross-sectional survey that periodically surveys the curricula being followed in our nation's high schools and the coursetaking patterns of high school students through a collection of transcripts. For public schools, the HSTS sample included every eligible sampled NAEP 2005 twelfth-grade public school that was contacted for the HSTS, whether or not they actually participated in the NAEP assessments. For private schools, the HSTS sample was a subsample from the NAEP 2005 twelfth-grade private school sample for the mathematics and science assessments. The study was conducted using a survey of school administrative personnel and collection of students' transcripts. Schools participating in the 12th-grade NAEP math and science assessments in 2005 were sampled. The study's weighted response rate was 84.2 percent. HSTS 2005 also offers information on the relationship of student coursetaking patterns to achievement at grade 12 as measured by NAEP. Key statistics produced from HSTS 2005 are information about the types of courses that graduates took, how many credits they earned, their grade point averages, and the relationship between coursetaking patterns and achievement, as measured by NAEP.",
-            "modified": "2023-06-27T15:20:32.527824",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "15a835b6-3496-4bbf-a7d9-a2dfa2dfb2e7",
-            "dataQuality": true,
-            "issued": "2008-08-19",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
-            "temporal": "2004/2005",
+            "modified": "2023-06-27T15:21:04.518207",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -73314,29 +73271,48 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
+            "temporal": "2003/2004",
+            "title": "National Assessment of Educational Progress, 2004 Long-Term Trend Study"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P4Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Linda Hamilton",
                 "hasEmail": "mailto:linda.hamilton@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Assessment of Educational Progress, 2005 High School Transcript Study (HSTS 2005), is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data available since 1990 at <https://nces.ed.gov/nationsreportcard/naepdata/>. HSTS 2005 (https://nces.ed.gov/nationsreportcard/hsts/) is a cross-sectional survey that periodically surveys the curricula being followed in our nation's high schools and the coursetaking patterns of high school students through a collection of transcripts. For public schools, the HSTS sample included every eligible sampled NAEP 2005 twelfth-grade public school that was contacted for the HSTS, whether or not they actually participated in the NAEP assessments. For private schools, the HSTS sample was a subsample from the NAEP 2005 twelfth-grade private school sample for the mathematics and science assessments. The study was conducted using a survey of school administrative personnel and collection of students' transcripts. Schools participating in the 12th-grade NAEP math and science assessments in 2005 were sampled. The study's weighted response rate was 84.2 percent. HSTS 2005 also offers information on the relationship of student coursetaking patterns to achievement at grade 12 as measured by NAEP. Key statistics produced from HSTS 2005 are information about the types of courses that graduates took, how many credits they earned, their grade point averages, and the relationship between coursetaking patterns and achievement, as measured by NAEP.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "NAEP Data Explorer",
                     "description": "National Assessment of Educational Progress, 2005 High School Transcript Study data available through the NAEP Data Explorer",
                     "downloadURL": "https://nces.ed.gov/nationsreportcard/hstsdata/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "NAEP Data Explorer"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP High School Transcript Study 2005 Restricted-Use Data File",
                     "description": "Restricted-use data file for the National Assessment of Educational Progress, 2005 High School Transcript Study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2008483",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP High School Transcript Study 2005 Restricted-Use Data File"
                 }
             ],
+            "identifier": "15a835b6-3496-4bbf-a7d9-a2dfa2dfb2e7",
+            "issued": "2008-08-19",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "achievement",
@@ -73351,33 +73327,14 @@
                 "progress-in-education",
                 "secondary-education"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Assessment of Educational Progress, 2005",
-            "description": "The National Assessment of Educational Progress, 2005 (NAEP 2005), is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data is available since 1990 at https://nces.ed.gov/nationsreportcard/naepdata/. NAEP 2005 (https://nces.ed.gov/nationsreportcard/) is a cross-sectional survey that assesses what America's students know and can do in various subject areas. The study was conducted using computer-based assessment of students. Students in grade 4, 8, and 12 were sampled. NAEP 2005 assessments consist of national and state assessments in mathematics, reading, and science. The study's response rate was between 84 and 99 percent. Key statistics produced from NAEP 2005 are results on subject-matter achievement, instructional experiences, and school environment for populations of students (e.g., all fourth-graders) and groups within those populations (e.g., female students, Hispanic students).",
-            "modified": "2023-06-27T15:19:53.898765",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "988da1e7-2ba7-44e8-8592-8e052c7c90bb",
-            "dataQuality": true,
-            "issued": "2007-07-19",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
-            "temporal": "2004/2005",
+            "modified": "2023-06-27T15:20:32.527824",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -73398,71 +73355,90 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
+            "temporal": "2004/2005",
+            "title": "National Assessment of Educational Progress, 2005 High School Transcript Study"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Linda Hamilton",
                 "hasEmail": "mailto:linda.hamilton@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Assessment of Educational Progress, 2005 (NAEP 2005), is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data is available since 1990 at https://nces.ed.gov/nationsreportcard/naepdata/. NAEP 2005 (https://nces.ed.gov/nationsreportcard/) is a cross-sectional survey that assesses what America's students know and can do in various subject areas. The study was conducted using computer-based assessment of students. Students in grade 4, 8, and 12 were sampled. NAEP 2005 assessments consist of national and state assessments in mathematics, reading, and science. The study's response rate was between 84 and 99 percent. Key statistics produced from NAEP 2005 are results on subject-matter achievement, instructional experiences, and school environment for populations of students (e.g., all fourth-graders) and groups within those populations (e.g., female students, Hispanic students).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "NAEP Data Explorer",
                     "description": "2005 National Assessment of Educational Progress data available through the NAEP Data Explorer",
                     "downloadURL": "https://nces.ed.gov/nationsreportcard/naepdata/dataset.aspx",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "NAEP Data Explorer"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2005 National Grade 12 Assessments (Mathematics, Reading, and Science) Restricted-Use Data Files",
                     "description": "Restricted-use data file for Grade 12 mathematics, reading, and science assessments from the 2005 National Assessment of Educational Progress study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2007484",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2005 National Grade 12 Assessments (Mathematics, Reading, and Science) Restricted-Use Data Files"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2005 National and State Mathematics Assessments (Grade 4) Restricted-Use Data Files",
                     "description": "Restricted-use data file for Grade 4 mathematics assessments from the 2005 National Assessment of Educational Progress study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2007485",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2005 National and State Mathematics Assessments (Grade 4) Restricted-Use Data Files"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2005 National and State Mathematics Assessments (Grade 8) Restricted-Use Data Files",
                     "description": "Restricted-use data file for Grade 8 mathematics assessments from the 2005 National Assessment of Educational Progress study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2007486",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2005 National and State Mathematics Assessments (Grade 8) Restricted-Use Data Files"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2005 National and State Reading Assessments (Grade 4) Restricted-Use Data Files",
                     "description": "Restricted-use data file for Grade 4 reading assessments from the 2005 National Assessment of Educational Progress study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2007487",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2005 National and State Reading Assessments (Grade 4) Restricted-Use Data Files"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2005 National and State Reading Assessments (Grade 8) Restricted-Use Data Files",
                     "description": "Restricted-use data file for Grade 8 reading assessments from the 2005 National Assessment of Educational Progress study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2007488",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2005 National and State Reading Assessments (Grade 8) Restricted-Use Data Files"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2005 National and State Science Assessments (Grade 4) Restricted-Use Data Files",
                     "description": "Restricted-use data file for Grade 4 science assessments from the 2005 National Assessment of Educational Progress study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2007489",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2005 National and State Science Assessments (Grade 4) Restricted-Use Data Files"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2005 National and State Science Assessments (Grade 8) Restricted-Use Data Files",
                     "description": "Restricted-use data file for Grade 8 science assessments from the 2005 National Assessment of Educational Progress study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2007490",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2005 National and State Science Assessments (Grade 8) Restricted-Use Data Files"
                 }
             ],
+            "identifier": "988da1e7-2ba7-44e8-8592-8e052c7c90bb",
+            "issued": "2007-07-19",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "math",
@@ -73471,33 +73447,14 @@
                 "science",
                 "students"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Assessment of Educational Progress, 2007",
-            "description": "The National Assessment of Educational Progress, 2007 (NAEP 2007), is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data is available since 1990 at https://nces.ed.gov/nationsreportcard/naepdata/. NAEP 2007 (https://nces.ed.gov/nationsreportcard/) is a cross-sectional survey that assesses what America's students know and can do in various subject areas. The study was conducted using computer-based assessment of students. Students in grade 4, 8, and 12 were sampled. NAEP 2007 assessments consist of national and state assessments in reading and mathematics, at grades 4 and 8; a national and state sample in writing at grade 8; and a national only writing sample at grade 12.",
-            "modified": "2023-06-27T15:19:11.516234",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "2521aaff-63e5-481c-8e6f-a5f981cd9d79",
-            "dataQuality": true,
-            "issued": "2008-09-10",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
-            "temporal": "2006/2007",
+            "modified": "2023-06-27T15:19:53.898765",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -73518,57 +73475,76 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
+            "temporal": "2004/2005",
+            "title": "National Assessment of Educational Progress, 2005"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Linda Hamilton",
                 "hasEmail": "mailto:linda.hamilton@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Assessment of Educational Progress, 2007 (NAEP 2007), is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data is available since 1990 at https://nces.ed.gov/nationsreportcard/naepdata/. NAEP 2007 (https://nces.ed.gov/nationsreportcard/) is a cross-sectional survey that assesses what America's students know and can do in various subject areas. The study was conducted using computer-based assessment of students. Students in grade 4, 8, and 12 were sampled. NAEP 2007 assessments consist of national and state assessments in reading and mathematics, at grades 4 and 8; a national and state sample in writing at grade 8; and a national only writing sample at grade 12.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "NAEP Data Explorer",
                     "description": "2007 National Assessment of Educational Progress data available through the NAEP Data Explorer",
                     "downloadURL": "https://nces.ed.gov/nationsreportcard/naepdata/dataset.aspx",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "NAEP Data Explorer"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2007 National and State Writing Assessments (Grades 8 and 12) Restricted-Use Data Files",
                     "description": "Restricted-use data file for Grades 8 and 12 writing assessments from the 2007 National Assessment of Educational Progress study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2009478",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2007 National and State Writing Assessments (Grades 8 and 12) Restricted-Use Data Files"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2007 National and State Mathematics Assessments (Grade 4) Restricted-Use Data Files",
                     "description": "Restricted-use data file for Grade 4 mathematics assessments from the 2007 National Assessment of Educational Progress study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2008491",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2007 National and State Mathematics Assessments (Grade 4) Restricted-Use Data Files"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2007 National and State Mathematics Assessments (Grade 8) Restricted-Use Data Files",
                     "description": "Restricted-use data file for Grade 8 mathematics assessments from the 2007 National Assessment of Educational Progress study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2008492",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2007 National and State Mathematics Assessments (Grade 8) Restricted-Use Data Files"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2007 National and State Reading Assessments (Grade 4) Restricted-Use Data Files",
                     "description": "Restricted-use data file for Grade 4 reading assessments from the 2007 National Assessment of Educational Progress study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2008493",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2007 National and State Reading Assessments (Grade 4) Restricted-Use Data Files"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2007 National and State Reading Assessments (Grade 8) Restricted-Use Data Files",
                     "description": "Restricted-use data file for Grade 8 reading assessments from the 2007 National Assessment of Educational Progress study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2008494",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2007 National and State Reading Assessments (Grade 8) Restricted-Use Data Files"
                 }
             ],
+            "identifier": "2521aaff-63e5-481c-8e6f-a5f981cd9d79",
+            "issued": "2008-09-10",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "math",
@@ -73577,33 +73553,14 @@
                 "students",
                 "writing"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Assessment of Educational Progress, 2006",
-            "description": "The National Assessment of Educational Progress, 2006 (NAEP 2006), is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data is available since 1990 at https://nces.ed.gov/nationsreportcard/naepdata/. NAEP 2006 (https://nces.ed.gov/nationsreportcard/) is a cross-sectional survey that assesses what America's students know and can do in various subject areas. The study was conducted using computer-based assessment of students. Students in grade 4, 8, and 12 were sampled. NAEP 2006 assessments consist of national assessments in civics and U.S. history at grades 4, 8, and 12, and economics at grade 12. The study's response rate was between 78 and 86 percent. Key statistics produced from NAEP 2006 are results on subject-matter achievement, instructional experiences, and school environment for populations of students (e.g., all fourth-graders) and groups within those populations (e.g., female students, Hispanic students).",
-            "modified": "2023-06-27T15:17:19.591616",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "e146a9e2-f5a3-4f75-836a-0042b463bd03",
-            "dataQuality": true,
-            "issued": "2008-02-20",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
-            "temporal": "2005/2006",
+            "modified": "2023-06-27T15:19:11.516234",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -73624,29 +73581,48 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
+            "temporal": "2006/2007",
+            "title": "National Assessment of Educational Progress, 2007"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Linda Hamilton",
                 "hasEmail": "mailto:linda.hamilton@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Assessment of Educational Progress, 2006 (NAEP 2006), is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data is available since 1990 at https://nces.ed.gov/nationsreportcard/naepdata/. NAEP 2006 (https://nces.ed.gov/nationsreportcard/) is a cross-sectional survey that assesses what America's students know and can do in various subject areas. The study was conducted using computer-based assessment of students. Students in grade 4, 8, and 12 were sampled. NAEP 2006 assessments consist of national assessments in civics and U.S. history at grades 4, 8, and 12, and economics at grade 12. The study's response rate was between 78 and 86 percent. Key statistics produced from NAEP 2006 are results on subject-matter achievement, instructional experiences, and school environment for populations of students (e.g., all fourth-graders) and groups within those populations (e.g., female students, Hispanic students).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "NAEP Data Explorer",
                     "description": "2006 National Assessment of Educational Progress data available through the NAEP Data Explorer",
                     "downloadURL": "https://nces.ed.gov/nationsreportcard/naepdata/dataset.aspx",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "NAEP Data Explorer"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2006 National Civics, Economics, and U.S. History Restricted Use Data File",
                     "description": "Restricted-use data file for Grades 4, 8, and 12 civics, economics, and U.S. history assessments from the 2007 National Assessment of Educational Progress study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2008472",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2006 National Civics, Economics, and U.S. History Restricted Use Data File"
                 }
             ],
+            "identifier": "e146a9e2-f5a3-4f75-836a-0042b463bd03",
+            "issued": "2008-02-20",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "civics",
@@ -73656,33 +73632,14 @@
                 "u-s-history",
                 "us-history"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Assessment of Educational Progress, 2008",
-            "description": "The National Assessment of Educational Progress, 2008 (NAEP 2008), is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data is available since 1990 at https://nces.ed.gov/nationsreportcard/naepdata/. NAEP 2008 (https://nces.ed.gov/nationsreportcard/) is a cross-sectional survey that assesses what America's students know and can do in arts. The study was conducted using computer-based assessment of students. Students in grade 8 were sampled. Key statistics produced from NAEP 2008 are results on subject-matter achievement, instructional experiences, and school environment for populations of students (e.g., all eighth-graders) and groups within those populations (e.g., female students, Hispanic students).",
-            "modified": "2023-06-27T15:16:31.957080",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "7906bf57-f4c4-4135-ae7d-689b3b9d996a",
-            "dataQuality": true,
-            "issued": "2011-03-11",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
-            "temporal": "2007/2008",
+            "modified": "2023-06-27T15:17:19.591616",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -73703,29 +73660,48 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
+            "temporal": "2005/2006",
+            "title": "National Assessment of Educational Progress, 2006"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Linda Hamilton",
                 "hasEmail": "mailto:linda.hamilton@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Assessment of Educational Progress, 2008 (NAEP 2008), is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data is available since 1990 at https://nces.ed.gov/nationsreportcard/naepdata/. NAEP 2008 (https://nces.ed.gov/nationsreportcard/) is a cross-sectional survey that assesses what America's students know and can do in arts. The study was conducted using computer-based assessment of students. Students in grade 8 were sampled. Key statistics produced from NAEP 2008 are results on subject-matter achievement, instructional experiences, and school environment for populations of students (e.g., all eighth-graders) and groups within those populations (e.g., female students, Hispanic students).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "NAEP Data Explorer",
                     "description": "2008 National Assessment of Educational Progress data available through the NAEP Data Explorer",
                     "downloadURL": "https://nces.ed.gov/nationsreportcard/naepdata/dataset.aspx",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "NAEP Data Explorer"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "2008 Arts restricted-use data CD-ROM",
                     "description": "Restricted-use data file for Grade 8 arts assessments from the 2008 National Assessment of Educational Progress study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2011469",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "2008 Arts restricted-use data CD-ROM"
                 }
             ],
+            "identifier": "7906bf57-f4c4-4135-ae7d-689b3b9d996a",
+            "issued": "2011-03-11",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "arts-education",
@@ -73734,33 +73710,14 @@
                 "on-line-assessment",
                 "students"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Assessment of Educational Progress, 2008 Long-Term Trend Study",
-            "description": "The National Assessment of Educational Progress, 2008 Long-Term Trend Study (NAEP 2008 LTT), is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data available since 1971 at <https://nces.ed.gov/nationsreportcard/naepdata/>. NAEP 2008 LTT (https://nces.ed.gov/nationsreportcard/ltt) is a cross-sectional survey that assesses what America's students know and can do in reading and mathematics. NAEP 2008 LTT assessments were administered to students aged 9, 13, and 17 who were enrolled in public and non-public elementary and secondary schools throughout the nation.",
-            "modified": "2023-06-27T15:15:54.435055",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "039d6a58-bba1-46ad-aed2-b421620e6173",
-            "dataQuality": true,
-            "issued": "2012-02-23",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
-            "temporal": "2007/2008",
+            "modified": "2023-06-27T15:16:31.957080",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -73781,36 +73738,55 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
+            "temporal": "2007/2008",
+            "title": "National Assessment of Educational Progress, 2008"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P4Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Linda Hamilton",
                 "hasEmail": "mailto:linda.hamilton@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Assessment of Educational Progress, 2008 Long-Term Trend Study (NAEP 2008 LTT), is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data available since 1971 at <https://nces.ed.gov/nationsreportcard/naepdata/>. NAEP 2008 LTT (https://nces.ed.gov/nationsreportcard/ltt) is a cross-sectional survey that assesses what America's students know and can do in reading and mathematics. NAEP 2008 LTT assessments were administered to students aged 9, 13, and 17 who were enrolled in public and non-public elementary and secondary schools throughout the nation.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "NAEP Data Explorer",
                     "description": "National Assessment of Educational Progress, 2008 Long-Term Trend Study data available through the NAEP Data Explorer",
                     "downloadURL": "https://nces.ed.gov/nationsreportcard/lttdata/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "NAEP Data Explorer"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP Mathematics Long-Term Trend Restricted Use Data File: 1978-2008",
                     "description": "Restricted-use data file for mathematics for the National Assessment of Educational Progress, 2008 Long-Term Trend Study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2012462",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP Mathematics Long-Term Trend Restricted Use Data File: 1978-2008"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP Reading Long-Term Trend Restricted Use Data File: 1971-2008",
                     "description": "Restricted-use data file for reading for the National Assessment of Educational Progress, 2008 Long-Term Trend Study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2012463",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP Reading Long-Term Trend Restricted Use Data File: 1971-2008"
                 }
             ],
+            "identifier": "039d6a58-bba1-46ad-aed2-b421620e6173",
+            "issued": "2012-02-23",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "long-term-trends",
@@ -73819,33 +73795,14 @@
                 "national-assessment-of-educational-progress",
                 "reading-assessment"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Assessment of Educational Progress, 2009",
-            "description": "The National Assessment of Educational Progress, 2009 (NAEP 2009) is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data is available since 1990 at <https://nces.ed.gov/nationsreportcard/naepdata/>. NAEP 2009 (https://nces.ed.gov/nationsreportcard/) is a cross-sectional survey that assesses what America's students know and can do in various subject areas. The study was conducted using computer-based assessment of students. Students in grades 4, 8, and 12 were sampled. NAEP 2009 assessments consist of national and state assessments in reading and math, at grades 4 and 8; a national and state sample in writing at grade 8; and a national only writing sample at grade 12. The study's response rates were between 83 and 100 percent. Key statistics produced from NAEP 2009 are results on subject-matter achievement, instructional experiences, and school environment for populations of students (e.g., all fourth-graders) and groups within those populations (e.g., female students, Hispanic students).",
-            "modified": "2023-06-27T15:15:13.682934",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "ee5c9bdd-2f6b-4dcb-b4e0-329fa6b99e18",
-            "dataQuality": true,
-            "issued": "2011-08-04",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
-            "temporal": "2008/2009",
+            "modified": "2023-06-27T15:15:54.435055",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -73866,50 +73823,69 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
+            "temporal": "2007/2008",
+            "title": "National Assessment of Educational Progress, 2008 Long-Term Trend Study"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Linda Hamilton",
                 "hasEmail": "mailto:linda.hamilton@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Assessment of Educational Progress, 2009 (NAEP 2009) is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data is available since 1990 at <https://nces.ed.gov/nationsreportcard/naepdata/>. NAEP 2009 (https://nces.ed.gov/nationsreportcard/) is a cross-sectional survey that assesses what America's students know and can do in various subject areas. The study was conducted using computer-based assessment of students. Students in grades 4, 8, and 12 were sampled. NAEP 2009 assessments consist of national and state assessments in reading and math, at grades 4 and 8; a national and state sample in writing at grade 8; and a national only writing sample at grade 12. The study's response rates were between 83 and 100 percent. Key statistics produced from NAEP 2009 are results on subject-matter achievement, instructional experiences, and school environment for populations of students (e.g., all fourth-graders) and groups within those populations (e.g., female students, Hispanic students).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "NAEP Data Explorer",
                     "description": "2009 National Assessment of Educational Progress data available through the NAEP Data Explorer",
                     "downloadURL": "https://nces.ed.gov/nationsreportcard/naepdata/dataset.aspx",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "NAEP Data Explorer"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2009 National and State Mathematics Assessments (Grades 4 and 8) Restricted-Use Data Files",
                     "description": "Restricted-use data file for Grades 4 and 8 mathematics assessments from the 2009 National Assessment of Educational Progress study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2011478",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2009 National and State Mathematics Assessments (Grades 4 and 8) Restricted-Use Data Files"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2009 National and State Science Assessments (Grades 4, 8 and 12) Restricted-Use Data Files",
                     "description": "Restricted-use data file for Grades 4, 8, and 12 science assessments from the 2009 National Assessment of Educational Progress study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2011492rev",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2009 National and State Science Assessments (Grades 4, 8 and 12) Restricted-Use Data Files"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2009 National and State Reading Assessments (Grades 4 and 8) Restricted-Use Data Files",
                     "description": "Restricted-use data file for Grades 4 and 8 reading assessments from the 2009 National Assessment of Educational Progress study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2011474",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2009 National and State Reading Assessments (Grades 4 and 8) Restricted-Use Data Files"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2009 National Grade 12 Assessments in Mathematics and Reading Restricted-Use Data Files",
                     "description": "Restricted-use data file for Grade 12 mathematics and reading assessments from the 2009 National Assessment of Educational Progress study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2011491",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2009 National Grade 12 Assessments in Mathematics and Reading Restricted-Use Data Files"
                 }
             ],
+            "identifier": "ee5c9bdd-2f6b-4dcb-b4e0-329fa6b99e18",
+            "issued": "2011-08-04",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "computer-assessment",
@@ -73918,33 +73894,14 @@
                 "science",
                 "students"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Assessment of Educational Progress, 2010",
-            "description": "The National Assessment of Educational Progress, 2010 (NAEP 2010), is part of the National Assessment of Educational Progress (NAEP) program; program data available since 1971 at <https://nces.ed.gov/nationsreportcard/naepdata/>. NAEP (https://nces.ed.gov/nationsreportcard/) is a cross-sectional survey that assesses what America's students know and can do in various subject areas. The 2010 study was conducted using a computer-based assessment of students. Students in grades 4, 8, and 12 were sampled. NAEP 2010 assessments consist of national and state assessments in geography, civics, U.S. history, and writing. The study's response rates were between 83 and 96 percent. Key statistics produced from NAEP 2010 are results on subject-matter achievement, instructional experiences, and school environment for populations of students (e.g., all fourth-graders) and groups within those populations (e.g. female students, Hispanic students).",
-            "modified": "2023-06-27T15:14:18.800833",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "e8692d82-4925-4a06-a1f2-dd385c66e58b",
-            "dataQuality": true,
-            "issued": "2012-07-31",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
-            "temporal": "2009/2010",
+            "modified": "2023-06-27T15:15:13.682934",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -73965,29 +73922,48 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
+            "temporal": "2008/2009",
+            "title": "National Assessment of Educational Progress, 2009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Linda Hamilton",
                 "hasEmail": "mailto:linda.hamilton@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Assessment of Educational Progress, 2010 (NAEP 2010), is part of the National Assessment of Educational Progress (NAEP) program; program data available since 1971 at <https://nces.ed.gov/nationsreportcard/naepdata/>. NAEP (https://nces.ed.gov/nationsreportcard/) is a cross-sectional survey that assesses what America's students know and can do in various subject areas. The 2010 study was conducted using a computer-based assessment of students. Students in grades 4, 8, and 12 were sampled. NAEP 2010 assessments consist of national and state assessments in geography, civics, U.S. history, and writing. The study's response rates were between 83 and 96 percent. Key statistics produced from NAEP 2010 are results on subject-matter achievement, instructional experiences, and school environment for populations of students (e.g., all fourth-graders) and groups within those populations (e.g. female students, Hispanic students).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "NAEP Data Explorer",
                     "description": "2010 National Assessment of Educational Progress data available through the NAEP Data Explorer",
                     "downloadURL": "https://nces.ed.gov/nationsreportcard/naepdata/dataset.aspx",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "NAEP Data Explorer"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2010 Restricted-Use Data File",
                     "description": "Restricted-use data file for the National Assessment of Educational Progress, 2010",
                     "downloadURL": "https://nces.ed.gov/statprog/instruct.asp",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2010 Restricted-Use Data File"
                 }
             ],
+            "identifier": "e8692d82-4925-4a06-a1f2-dd385c66e58b",
+            "issued": "2012-07-31",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "assessment",
@@ -73998,33 +73974,14 @@
                 "u-s-history",
                 "us-history"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Assessment of Educational Progress, 2011",
-            "description": "The National Assessment of Educational Progress, 2011 (NAEP 2011), is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data available since 1971 at <https://nces.ed.gov/nationsreportcard/naepdata/>. NAEP 2011 (https://nces.ed.gov/nationsreportcard/) is a cross-sectional survey that assesses what America's students know and can do in various subject areas. The study was conducted using computer-based assessments of students. Students in grades 4, 8, and 12 were sampled. NAEP 2011 assessments consist of national and state assessments in mathematics, reading, and writing. The study's response rates were between 87 and 98 percent. Key statistics produced from NAEP 2011 are results on subject-matter achievement, instructional experiences, and school environment for populations of students (e.g., all fourth-graders) and groups within those populations (e.g. female students, Hispanic students).",
-            "modified": "2023-06-27T15:13:16.999891",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "7a29d444-9c60-4313-86e0-ed3c82e50110",
-            "dataQuality": true,
-            "issued": "2013-04-02",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
-            "temporal": "2010/2011",
+            "modified": "2023-06-27T15:14:18.800833",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -74045,51 +74002,70 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
+            "temporal": "2009/2010",
+            "title": "National Assessment of Educational Progress, 2010"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Linda Hamilton",
                 "hasEmail": "mailto:linda.hamilton@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Assessment of Educational Progress, 2011 (NAEP 2011), is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data available since 1971 at <https://nces.ed.gov/nationsreportcard/naepdata/>. NAEP 2011 (https://nces.ed.gov/nationsreportcard/) is a cross-sectional survey that assesses what America's students know and can do in various subject areas. The study was conducted using computer-based assessments of students. Students in grades 4, 8, and 12 were sampled. NAEP 2011 assessments consist of national and state assessments in mathematics, reading, and writing. The study's response rates were between 87 and 98 percent. Key statistics produced from NAEP 2011 are results on subject-matter achievement, instructional experiences, and school environment for populations of students (e.g., all fourth-graders) and groups within those populations (e.g. female students, Hispanic students).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "NAEP Data Explorer",
                     "description": "2011 National Assessment of Educational Progress data available through the NAEP Data Explorer",
                     "downloadURL": "https://nces.ed.gov/nationsreportcard/naepdata/dataset.aspx",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "NAEP Data Explorer"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2011 National and State Mathematics Assessments (Grades 4 and 8) Restricted-Use Data Files",
                     "description": "Restricted-use data file for Grades 4 and 8 mathematics assessments from the 2011 National Assessment of Educational Progress study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2014473",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2011 National and State Mathematics Assessments (Grades 4 and 8) Restricted-Use Data Files"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2011 National and State Reading Assessments (Grades 4 & 8) Restricted Use Data Files",
                     "description": "Restricted-use data file for Grades 4, and 8 reading assessments from the 2011 National Assessment of Educational Progress study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2014474",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2011 National and State Reading Assessments (Grades 4 & 8) Restricted Use Data Files"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2011 National Science Assessments (Grade 8) Restricted Use Data Files",
                     "description": "Restricted-use data file for Grade 8 science assessments from the 2011 National Assessment of Educational Progress study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2014475",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2011 National Science Assessments (Grade 8) Restricted Use Data Files"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2011 National Writing Assessment (Grades 8 &12) Restricted Use Data Files",
                     "description": "Restricted-use data file for Grade 8, and 12 writing assessments from the 2011 National Assessment of Educational Progress study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2014477",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2011 National Writing Assessment (Grades 8 &12) Restricted Use Data Files"
                 }
             ],
-            "keyword": [
+            "identifier": "7a29d444-9c60-4313-86e0-ed3c82e50110",
+            "issued": "2013-04-02",
+            "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "assessment",
                 "math",
@@ -74099,32 +74075,14 @@
                 "students",
                 "writing"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Assessment of Educational Progress, 2012",
-            "description": "The National Assessment of Educational Progress, 2012 (NAEP 2012), is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data is available since 1990 at https://nces.ed.gov/nationsreportcard/naepdata/. NAEP 2012 (https://nces.ed.gov/nationsreportcard/) is a cross-sectional survey that assesses what America's students know and can do in economics. Students in grade 12 were sampled. NAEP 2012 assessments consist of national assessment in economics. Key statistics produced from NAEP 2012 are results on subject-matter achievement, instructional experiences, and school environment for populations of students (e.g., all fourth-graders) and groups within those populations (e.g. female students, Hispanic students).",
-            "modified": "2023-06-27T15:12:39.115458",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "dcdcdb00-2c4d-4dd1-9366-9b57777cf8d3",
-            "dataQuality": true,
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
-            "temporal": "2011/2012",
+            "modified": "2023-06-27T15:13:16.999891",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -74145,62 +74103,61 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
+            "temporal": "2010/2011",
+            "title": "National Assessment of Educational Progress, 2011"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Linda Hamilton",
                 "hasEmail": "mailto:linda.hamilton@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Assessment of Educational Progress, 2012 (NAEP 2012), is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data is available since 1990 at https://nces.ed.gov/nationsreportcard/naepdata/. NAEP 2012 (https://nces.ed.gov/nationsreportcard/) is a cross-sectional survey that assesses what America's students know and can do in economics. Students in grade 12 were sampled. NAEP 2012 assessments consist of national assessment in economics. Key statistics produced from NAEP 2012 are results on subject-matter achievement, instructional experiences, and school environment for populations of students (e.g., all fourth-graders) and groups within those populations (e.g. female students, Hispanic students).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "NAEP Data Explorer",
                     "description": "2012 National Assessment of Educational Progress data available through the NAEP Data Explorer",
                     "downloadURL": "https://nces.ed.gov/nationsreportcard/naepdata/dataset.aspx",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "NAEP Data Explorer"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2012 Restricted-Use Data File",
                     "description": "Restricted-use data file for the National Assessment of Educational Progress, 2012",
                     "downloadURL": "https://nces.ed.gov/statprog/instruct.asp",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2012 Restricted-Use Data File"
                 }
             ],
+            "identifier": "dcdcdb00-2c4d-4dd1-9366-9b57777cf8d3",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "economics",
                 "national-assessment-of-educational-progress",
                 "students"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Assessment of Educational Progress, 2012 Long-Term Trend",
-            "description": "The National Assessment of Educational Progress, 2012 Long-Term Trend (NAEP 2012 LTT), is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data is available since 1971 at https://nces.ed.gov/nationsreportcard/naepdata/. NAEP 2012 LTT (https://nces.ed.gov/nationsreportcard/ltt) is a cross-sectional survey that assesses what America's students know and can do in reading and mathematics. NAEP 2012 Long-Term Trend assessment was administered to students aged 9, 13, and 17 who were enrolled in public and non-public elementary and secondary schools throughout the nation.",
-            "modified": "2023-06-27T15:11:56.130695",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "e6abeac2-6f70-4166-925a-4523d97b27d5",
-            "dataQuality": true,
-            "issued": "2013-05-16",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
-            "temporal": "2011/2012",
+            "modified": "2023-06-27T15:12:39.115458",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -74221,29 +74178,48 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
+            "temporal": "2011/2012",
+            "title": "National Assessment of Educational Progress, 2012"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P4Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Linda Hamilton",
                 "hasEmail": "mailto:linda.hamilton@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Assessment of Educational Progress, 2012 Long-Term Trend (NAEP 2012 LTT), is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data is available since 1971 at https://nces.ed.gov/nationsreportcard/naepdata/. NAEP 2012 LTT (https://nces.ed.gov/nationsreportcard/ltt) is a cross-sectional survey that assesses what America's students know and can do in reading and mathematics. NAEP 2012 Long-Term Trend assessment was administered to students aged 9, 13, and 17 who were enrolled in public and non-public elementary and secondary schools throughout the nation.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "NAEP Data Explorer",
                     "description": "National Assessment of Educational Progress, 2012 Long-Term Trend study data available through the NAEP Data Explorer",
                     "downloadURL": "https://nces.ed.gov/nationsreportcard/lttdata/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "NAEP Data Explorer"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2012 LTT Restricted-Use Data File",
                     "description": "Restricted-use data file for National Assessment of Educational Progress, 2012 Long-Term Trend",
                     "downloadURL": "https://nces.ed.gov/statprog/instruct.asp",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2012 LTT Restricted-Use Data File"
                 }
             ],
+            "identifier": "e6abeac2-6f70-4166-925a-4523d97b27d5",
+            "issued": "2013-05-16",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "education",
@@ -74254,32 +74230,14 @@
                 "sd-student-with-disabilities",
                 "secondary-education"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Assessment of Educational Progress, 2014",
-            "description": "The 2014 National Assessment of Educational Progress (NAEP 2014) is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data is available since 1990 at <https://nces.ed.gov/nationsreportcard/naepdata/>. NAEP 2014 (https://nces.ed.gov/nationsreportcard/) is a cross-sectional survey that assesses what America's students know and can do in various subject areas. The study is conducted using computer-based assessment of students. Students in grade 4, 8, and 12 are sampled. NAEP 2014 assessments consist of national assessments in civics, geography, U.S. history, and technology and engineering literacy for 8th-grade students. Key statistics produced from NAEP 2014 are results on subject-matter achievement, instructional experiences, and school environment for populations of students (e.g., all fourth-graders) and groups within those populations (e.g. female students, Hispanic students).",
-            "modified": "2023-06-27T15:10:19.342920",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "63e09c04-30fc-4f2c-95cb-f21f194ee5bd",
-            "dataQuality": true,
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
-            "temporal": "2013/2014",
+            "modified": "2023-06-27T15:11:56.130695",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -74300,29 +74258,47 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
+            "temporal": "2011/2012",
+            "title": "National Assessment of Educational Progress, 2012 Long-Term Trend"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Linda Hamilton",
                 "hasEmail": "mailto:linda.hamilton@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The 2014 National Assessment of Educational Progress (NAEP 2014) is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data is available since 1990 at <https://nces.ed.gov/nationsreportcard/naepdata/>. NAEP 2014 (https://nces.ed.gov/nationsreportcard/) is a cross-sectional survey that assesses what America's students know and can do in various subject areas. The study is conducted using computer-based assessment of students. Students in grade 4, 8, and 12 are sampled. NAEP 2014 assessments consist of national assessments in civics, geography, U.S. history, and technology and engineering literacy for 8th-grade students. Key statistics produced from NAEP 2014 are results on subject-matter achievement, instructional experiences, and school environment for populations of students (e.g., all fourth-graders) and groups within those populations (e.g. female students, Hispanic students).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "NAEP Data Explorer",
                     "description": "2014 National Assessment of Educational Progress data available through the NAEP Data Explorer",
                     "downloadURL": "https://nces.ed.gov/nationsreportcard/naepdata/dataset.aspx",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "NAEP Data Explorer"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2014 Restricted-Use Data File",
                     "description": "Restricted-use data file for the National Assessment of Educational Progress, 2014",
                     "downloadURL": "https://nces.ed.gov/statprog/instruct.asp",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2014 Restricted-Use Data File"
                 }
             ],
+            "identifier": "63e09c04-30fc-4f2c-95cb-f21f194ee5bd",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "civics",
@@ -74333,32 +74309,14 @@
                 "u-s-history",
                 "us-history"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Assessment of Educational Progress, 2013",
-            "description": "The National Assessment of Educational Progress, 2013 (NAEP 2013), is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data is available since 1990 at https://nces.ed.gov/nationsreportcard/naepdata/. NAEP 2013 (https://nces.ed.gov/nationsreportcard/) is a cross-sectional survey that assesses what America's students know and can do in various subject areas. Students in grade 4, 8, and 12 were sampled. NAEP 2013 assessments consist of national and state assessments in mathematics and reading. Key statistics produced from the NAEP 2013 are results on subject-matter achievement, instructional experiences, and school environment for populations of students (e.g., all fourth-graders) and groups within those populations (e.g., female students, Hispanic students).",
-            "modified": "2023-06-27T15:09:44.874107",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "e4b94e4b-7ac6-4dfc-8354-1867bdb569b7",
-            "dataQuality": true,
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
-            "temporal": "2012/2013",
+            "modified": "2023-06-27T15:10:19.342920",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -74379,29 +74337,47 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
+            "temporal": "2013/2014",
+            "title": "National Assessment of Educational Progress, 2014"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Linda Hamilton",
                 "hasEmail": "mailto:linda.hamilton@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Assessment of Educational Progress, 2013 (NAEP 2013), is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data is available since 1990 at https://nces.ed.gov/nationsreportcard/naepdata/. NAEP 2013 (https://nces.ed.gov/nationsreportcard/) is a cross-sectional survey that assesses what America's students know and can do in various subject areas. Students in grade 4, 8, and 12 were sampled. NAEP 2013 assessments consist of national and state assessments in mathematics and reading. Key statistics produced from the NAEP 2013 are results on subject-matter achievement, instructional experiences, and school environment for populations of students (e.g., all fourth-graders) and groups within those populations (e.g., female students, Hispanic students).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "NAEP Data Explorer",
                     "description": "2013 National Assessment of Educational Progress data available through the NAEP Data Explorer",
                     "downloadURL": "https://nces.ed.gov/nationsreportcard/naepdata/dataset.aspx",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "NAEP Data Explorer"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2013 Restricted-Use Data File",
                     "description": "Restricted-use data file for the National Assessment of Educational Progress, 2013",
                     "downloadURL": "https://nces.ed.gov/statprog/instruct.asp",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2013 Restricted-Use Data File"
                 }
             ],
+            "identifier": "e4b94e4b-7ac6-4dfc-8354-1867bdb569b7",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "math",
@@ -74409,32 +74385,14 @@
                 "reading",
                 "students"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Assessment of Educational Progress, 2015",
-            "description": "The National Assessment of Educational Progress, 2015 (NAEP 2015) is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data is available since 1990 at <https://nces.ed.gov/nationsreportcard/naepdata/>. NAEP 2015 (https://nces.ed.gov/nationsreportcard/) is a cross-sectional survey that assesses what America's students know and can do in various subject areas. The study is conducted using computer-based assessment of students. Students in grade 4, 8, and 12 are sampled. NAEP 2015 assessments consist of national and state assessments in mathematics, reading, and science. Key statistics produced from NAEP 2015 are results on subject-matter achievement, instructional experiences, and school environment for populations of students (e.g., all fourth-graders) and groups within those populations (e.g. female students, Hispanic students).",
-            "modified": "2023-06-27T15:09:03.918149",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "f6d1e252-b3e2-4725-9005-b1447d8be789",
-            "dataQuality": true,
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
-            "temporal": "2014/2015",
+            "modified": "2023-06-27T15:09:44.874107",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -74455,29 +74413,47 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
+            "temporal": "2012/2013",
+            "title": "National Assessment of Educational Progress, 2013"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Linda Hamilton",
                 "hasEmail": "mailto:linda.hamilton@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Assessment of Educational Progress, 2015 (NAEP 2015) is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data is available since 1990 at <https://nces.ed.gov/nationsreportcard/naepdata/>. NAEP 2015 (https://nces.ed.gov/nationsreportcard/) is a cross-sectional survey that assesses what America's students know and can do in various subject areas. The study is conducted using computer-based assessment of students. Students in grade 4, 8, and 12 are sampled. NAEP 2015 assessments consist of national and state assessments in mathematics, reading, and science. Key statistics produced from NAEP 2015 are results on subject-matter achievement, instructional experiences, and school environment for populations of students (e.g., all fourth-graders) and groups within those populations (e.g. female students, Hispanic students).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "NAEP Data Explorer",
                     "description": "2015 National Assessment of Educational Progress data available through the NAEP Data Explorer",
                     "downloadURL": "https://nces.ed.gov/nationsreportcard/naepdata/dataset.aspx",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "NAEP Data Explorer"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2015 Restricted-Use Data File",
                     "description": "Restricted-use data file for the National Assessment of Educational Progress, 2015",
                     "downloadURL": "https://nces.ed.gov/statprog/instruct.asp",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2015 Restricted-Use Data File"
                 }
             ],
+            "identifier": "f6d1e252-b3e2-4725-9005-b1447d8be789",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "assessments",
@@ -74489,33 +74465,14 @@
                 "secondary-education",
                 "students-with-disabilities-sd"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Indian Education Study, 2005",
-            "description": "The National Indian Education Study, 2005 (NIES 2005), is a study that is part of the National Indian Education Study (NIES), which is a part of National Assessment of Educational Progress (NAEP) program; program data is available since 2005 at https://nces.ed.gov/nationsreportcard/nies/. NIES 2005 (https://nces.ed.gov/nationsreportcard/nies/) is a cross-sectional survey that is designed to describe the condition of education for American Indian and Alaska Native (AI/AN) students in the United States. Students in public, private, Department of Defense, and Bureau of Indian Education-funded schools were sampled using paper-and-pencil assessment in April and May of 2005. Overall weighted response rate for 4th grade reading was 83 percent. Overall weighted response rate for 8th grade reading was 85 percent. Overall weighted response rate for 4th grade math was 86 percent. Overall weighted response rate for 8th grade math was 87 percent. Key statistics produced from NIES 2005 provides educators, policymakers, and the public with information about the academic performance in reading and mathematics of AI/AN fourth- and eighth-graders as well as their exposure to Native American culture.",
-            "modified": "2023-06-27T15:08:14.770395",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "155938f4-a110-4b84-b799-536b2f46f1ab",
-            "dataQuality": true,
-            "issued": "2007-09-04",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
-            "temporal": "2004/2005",
+            "modified": "2023-06-27T15:09:03.918149",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -74536,29 +74493,48 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
+            "temporal": "2014/2015",
+            "title": "National Assessment of Educational Progress, 2015"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P2Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Linda Hamilton",
                 "hasEmail": "mailto:linda.hamilton@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Indian Education Study, 2005 (NIES 2005), is a study that is part of the National Indian Education Study (NIES), which is a part of National Assessment of Educational Progress (NAEP) program; program data is available since 2005 at https://nces.ed.gov/nationsreportcard/nies/. NIES 2005 (https://nces.ed.gov/nationsreportcard/nies/) is a cross-sectional survey that is designed to describe the condition of education for American Indian and Alaska Native (AI/AN) students in the United States. Students in public, private, Department of Defense, and Bureau of Indian Education-funded schools were sampled using paper-and-pencil assessment in April and May of 2005. Overall weighted response rate for 4th grade reading was 83 percent. Overall weighted response rate for 8th grade reading was 85 percent. Overall weighted response rate for 4th grade math was 86 percent. Overall weighted response rate for 8th grade math was 87 percent. Key statistics produced from NIES 2005 provides educators, policymakers, and the public with information about the academic performance in reading and mathematics of AI/AN fourth- and eighth-graders as well as their exposure to Native American culture.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "NAEP Data Explorer",
                     "description": "2005 National Indian Education Study data available through the NAEP Data Explorer",
                     "downloadURL": "https://nces.ed.gov/nationsreportcard/niesdata/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "NAEP Data Explorer"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "2005 National Indian Education Study, Parts I and II Restricted-Use Data Files",
                     "description": "Restricted-use data file for the 2005 National Indian Education Study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2007491",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "2005 National Indian Education Study, Parts I and II Restricted-Use Data Files"
                 }
             ],
+            "identifier": "155938f4-a110-4b84-b799-536b2f46f1ab",
+            "issued": "2007-09-04",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "achievement-and-education-experiences",
@@ -74568,41 +74544,14 @@
                 "mathematics",
                 "reading"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf",
-                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2005_NIES_Part_I_Variables.xls",
-                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2005_NIES_Part_II_Variables.xls",
-                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2005_NIES_Part_I_Variables_School.csv",
-                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2005_NIES_Part_I_Variables_SDLEP.csv",
-                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2005_NIES_Part_I_Variables_Student.csv",
-                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2005_NIES_Part_I_Variables_Teacher.csv",
-                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2005_NIES_Part_II_Variables_School.csv",
-                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2005_NIES_Part_II_Variables_Student.csv",
-                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2005_NIES_Part_II_Variables_Teacher.csv"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Household Education Surveys Program, 2012 Parent and Family Involvement in Education Survey",
-            "description": "The National Household Education Survey Program, 2012 Parent and Family Involvement in Education Survey (PFI-NHES:2012), is a study that is part of the National Household Education Survey (NHES) program. PFI-NHES:2012 (https://nces.ed.gov/nhes/) is a cross-sectional survey that collects data directly from households on educational issues. This study was conducted using address based sample, self-administered questionnaires of households. Households in 2012 were sampled. Key statistics produced from PFI-NHES:2012 are early childhood care and education, children's readiness for school, parent perceptions of school safety and discipline, before- and after-school activities of school-age children, participation in adult and continuing education, parent involvement in education, school choice, homeschooling, and civic involvement.",
-            "modified": "2023-06-27T15:07:25.599277",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "bdf82c61-0027-4d50-9505-44fc57f2fd12",
-            "dataQuality": true,
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2012/P1Y",
+            "modified": "2023-06-27T15:08:14.770395",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -74623,32 +74572,59 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf",
+                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2005_NIES_Part_I_Variables.xls",
+                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2005_NIES_Part_II_Variables.xls",
+                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2005_NIES_Part_I_Variables_School.csv",
+                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2005_NIES_Part_I_Variables_SDLEP.csv",
+                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2005_NIES_Part_I_Variables_Student.csv",
+                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2005_NIES_Part_I_Variables_Teacher.csv",
+                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2005_NIES_Part_II_Variables_School.csv",
+                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2005_NIES_Part_II_Variables_Student.csv",
+                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2005_NIES_Part_II_Variables_Teacher.csv"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
+            "temporal": "2004/2005",
+            "title": "National Indian Education Study, 2005"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sarah Grady",
                 "hasEmail": "mailto:sarah.grady@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Household Education Survey Program, 2012 Parent and Family Involvement in Education Survey (PFI-NHES:2012), is a study that is part of the National Household Education Survey (NHES) program. PFI-NHES:2012 (https://nces.ed.gov/nhes/) is a cross-sectional survey that collects data directly from households on educational issues. This study was conducted using address based sample, self-administered questionnaires of households. Households in 2012 were sampled. Key statistics produced from PFI-NHES:2012 are early childhood care and education, children's readiness for school, parent perceptions of school safety and discipline, before- and after-school activities of school-age children, participation in adult and continuing education, parent involvement in education, school choice, homeschooling, and civic involvement.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "2012PFIascii.zip",
                     "describedBy": "https://nces.ed.gov/nhes/pdf/userman/NHES_2012_pfi_codebook.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/nhes/data/2012PFIascii.zip"
+                    "downloadURL": "https://nces.ed.gov/nhes/data/2012PFIascii.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "2012PFIascii.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "National Household Education Surveys Program (NHES):2012 Restricted-Use Data Files",
-                    "description": "Restricted-use data files for the 2012 National Household Education Surveys Program (NHES:2012), including the Early Childhood Program Participation (ECPP) and Parent and Family Involvement in Education (PFI) files",
                     "describedBy": "https://nces.ed.gov/nhes/pdf/userman/NHES_2012_UsersManual.pdf",
                     "describedByType": "application/pdf",
+                    "description": "Restricted-use data files for the 2012 National Household Education Surveys Program (NHES:2012), including the Early Childhood Program Participation (ECPP) and Parent and Family Involvement in Education (PFI) files",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2016097",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "National Household Education Surveys Program (NHES):2012 Restricted-Use Data Files"
                 }
             ],
+            "identifier": "bdf82c61-0027-4d50-9505-44fc57f2fd12",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "education",
@@ -74659,30 +74635,14 @@
                 "parental-involvement-in-education",
                 "public-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-27T15:07:25.599277",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Indian Education Study, 2007",
-            "description": "The National Indian Education Study, 2007 (NIES 2007), is a study that is part of the National Indian Education Study (NIES), which is a part of National Assessment of Educational Progress (NAEP) program; program data is available since 2005 at https://nces.ed.gov/nationsreportcard/nies/. NIES 2007 (https://nces.ed.gov/nationsreportcard/nies/) is a cross-sectional survey that is designed to describe the condition of education for American Indian and Alaska Native (AI/AN) students in the United States. Students in public, private, Department of Defense, and Bureau of Indian Education-funded schools were sampled using paper-and-pencil assessment. Overall weighted response rate for 4th grade was 75 percent. Overall weighted response rate for 8th grade was 74 percent. Key statistics produced from NIES 2007 provides educators, policymakers, and the public with information about the academic performance in reading and mathematics of AI/AN fourth- and eighth-graders as well as their exposure to Native American culture.",
-            "modified": "2023-06-27T14:50:56.020729",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "df6dc78d-e091-4af1-92d8-bb337694c237",
-            "dataQuality": true,
-            "issued": "2009-02-13",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
-            "temporal": "2006/2007",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -74703,29 +74663,45 @@
                     }
                 }
             },
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2012/P1Y",
+            "title": "National Household Education Surveys Program, 2012 Parent and Family Involvement in Education Survey"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P2Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Linda Hamilton",
                 "hasEmail": "mailto:linda.hamilton@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Indian Education Study, 2007 (NIES 2007), is a study that is part of the National Indian Education Study (NIES), which is a part of National Assessment of Educational Progress (NAEP) program; program data is available since 2005 at https://nces.ed.gov/nationsreportcard/nies/. NIES 2007 (https://nces.ed.gov/nationsreportcard/nies/) is a cross-sectional survey that is designed to describe the condition of education for American Indian and Alaska Native (AI/AN) students in the United States. Students in public, private, Department of Defense, and Bureau of Indian Education-funded schools were sampled using paper-and-pencil assessment. Overall weighted response rate for 4th grade was 75 percent. Overall weighted response rate for 8th grade was 74 percent. Key statistics produced from NIES 2007 provides educators, policymakers, and the public with information about the academic performance in reading and mathematics of AI/AN fourth- and eighth-graders as well as their exposure to Native American culture.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "NAEP Data Explorer",
                     "description": "2007 National Indian Education Study data available through the NAEP Data Explorer",
                     "downloadURL": "https://nces.ed.gov/nationsreportcard/niesdata/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "NAEP Data Explorer"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "2007 National Indian Education Study, Parts I and II Restricted-Use Data Files",
                     "description": "Restricted-use data file for the 2007 National Indian Education Study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2009489",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "2007 National Indian Education Study, Parts I and II Restricted-Use Data Files"
                 }
             ],
+            "identifier": "df6dc78d-e091-4af1-92d8-bb337694c237",
+            "issued": "2009-02-13",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "focus-groups",
@@ -74735,41 +74711,14 @@
                 "nies",
                 "report"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf",
-                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2007_NIES_Part_I_Variables.xls",
-                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2007_NIES_Part_II_Variables.xls",
-                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2007_NIES_Part_I_Variables_School.csv",
-                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2007_NIES_Part_I_Variables_SDELL.csv",
-                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2007_NIES_Part_I_Variables_Student.csv",
-                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2007_NIES_Part_I_Variables_Teacher.csv",
-                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2007_NIES_Part_II_Variables_School.csv",
-                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2007_NIES_Part_II_Variables_Student.csv",
-                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2007_NIES_Part_II_Variables_Teacher.csv"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Household Education Surveys Program, 2012 Early Childhood Program Participation Survey",
-            "description": "The National Household Education Survey Program, 2012 Early Childhood Program Participation Survey (ECPP-NHES:2012), is a study that is part of the National Household Education Survey (NHES) program. ECPP-NHES:2012 (https://nces.ed.gov/nhes/) is a cross-sectional survey that collects data directly from households on educational issues. This study was conducted using address based sample, self-administered questionnaires of households. Households in 2012 were sampled. Key statistics produced from ECPP-NHES:2012 are early childhood care and education.",
-            "modified": "2023-06-27T14:41:50.056862",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "1d8b500d-428c-4ef8-9e67-bac707845fc5",
-            "dataQuality": true,
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2012/P1Y",
+            "modified": "2023-06-27T14:50:56.020729",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -74790,32 +74739,59 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf",
+                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2007_NIES_Part_I_Variables.xls",
+                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2007_NIES_Part_II_Variables.xls",
+                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2007_NIES_Part_I_Variables_School.csv",
+                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2007_NIES_Part_I_Variables_SDELL.csv",
+                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2007_NIES_Part_I_Variables_Student.csv",
+                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2007_NIES_Part_I_Variables_Teacher.csv",
+                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2007_NIES_Part_II_Variables_School.csv",
+                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2007_NIES_Part_II_Variables_Student.csv",
+                "https://nces.ed.gov/nationsreportcard/data/researchcenter/QData/2007_NIES_Part_II_Variables_Teacher.csv"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
+            "temporal": "2006/2007",
+            "title": "National Indian Education Study, 2007"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sarah Grady",
                 "hasEmail": "mailto:sarah.grady@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Household Education Survey Program, 2012 Early Childhood Program Participation Survey (ECPP-NHES:2012), is a study that is part of the National Household Education Survey (NHES) program. ECPP-NHES:2012 (https://nces.ed.gov/nhes/) is a cross-sectional survey that collects data directly from households on educational issues. This study was conducted using address based sample, self-administered questionnaires of households. Households in 2012 were sampled. Key statistics produced from ECPP-NHES:2012 are early childhood care and education.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "2012ECPPascii.zip",
                     "describedBy": "https://nces.ed.gov/nhes/pdf/userman/NHES_2012_ecpp_codebook.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/nhes/data/2012ECPPascii.zip"
+                    "downloadURL": "https://nces.ed.gov/nhes/data/2012ECPPascii.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "2012ECPPascii.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "National Household Education Surveys Program (NHES):2012 Restricted-Use Data Files",
-                    "description": "Restricted-use data files for the 2012 National Household Education Surveys Program (NHES:2012), including the Early Childhood Program Participation (ECPP) and Parent and Family Involvement in Education (PFI) files",
                     "describedBy": "https://nces.ed.gov/nhes/pdf/userman/NHES_2012_UsersManual.pdf",
                     "describedByType": "application/pdf",
+                    "description": "Restricted-use data files for the 2012 National Household Education Surveys Program (NHES:2012), including the Early Childhood Program Participation (ECPP) and Parent and Family Involvement in Education (PFI) files",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2016097",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "National Household Education Surveys Program (NHES):2012 Restricted-Use Data Files"
                 }
             ],
+            "identifier": "1d8b500d-428c-4ef8-9e67-bac707845fc5",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "early-childhood-care",
@@ -74827,30 +74803,14 @@
                 "national-household-education-survey-nhes",
                 "public-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-27T14:41:50.056862",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Indian Education Study, 2009",
-            "description": "The National Indian Education Study, 2009 (NIES 2009), is a study that is part of the National Indian Education Study (NIES), which is a part of National Assessment of Educational Progress (NAEP) program; program data is available since 2005 at https://nces.ed.gov/nationsreportcard/nies/. NIES 2009 (https://nces.ed.gov/nationsreportcard/nies/) is a cross-sectional survey that is designed to describe the condition of education for American Indian and Alaska Native (AI/AN) students in the United States. Students in public, private, Department of Defense, and Bureau of Indian Education-funded schools were sampled using paper-and-pencil assessment. Key statistics produced from NIES 2009 provides educators, policymakers, and the public with information about the academic performance in reading and mathematics of AI/AN fourth- and eighth-graders as well as their exposure to Native American culture.",
-            "modified": "2023-06-23T18:31:45.499569",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".)",
-            "identifier": "e58c792b-3ddd-4b32-9e5a-7e4e8306b3db",
-            "dataQuality": true,
-            "issued": "2011-08-04",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
-            "temporal": "2008/2009",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -74871,36 +74831,52 @@
                     }
                 }
             },
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2012/P1Y",
+            "title": "National Household Education Surveys Program, 2012 Early Childhood Program Participation Survey"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P2Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Linda Hamilton",
                 "hasEmail": "mailto:linda.hamilton@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Indian Education Study, 2009 (NIES 2009), is a study that is part of the National Indian Education Study (NIES), which is a part of National Assessment of Educational Progress (NAEP) program; program data is available since 2005 at https://nces.ed.gov/nationsreportcard/nies/. NIES 2009 (https://nces.ed.gov/nationsreportcard/nies/) is a cross-sectional survey that is designed to describe the condition of education for American Indian and Alaska Native (AI/AN) students in the United States. Students in public, private, Department of Defense, and Bureau of Indian Education-funded schools were sampled using paper-and-pencil assessment. Key statistics produced from NIES 2009 provides educators, policymakers, and the public with information about the academic performance in reading and mathematics of AI/AN fourth- and eighth-graders as well as their exposure to Native American culture.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "2009 National Indian Education Study, Parts I and II Restricted-Use Data Files",
                     "description": "Restricted-use data file for the 2009 National Indian Education Study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2011486",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "2009 National Indian Education Study, Parts I and II Restricted-Use Data Files"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "2009 National Indian Education Study, Parts I and II Restricted-Use Data Files (Data Companion)",
                     "description": "Restricted-use data file Data Companion for the 2009 National Indian Education Study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2011487",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "2009 National Indian Education Study, Parts I and II Restricted-Use Data Files (Data Companion)"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "NAEP Data Explorer",
                     "description": "2009 National Indian Education Study data available through the NAEP Data Explorer",
                     "downloadURL": "https://nces.ed.gov/nationsreportcard/niesdata/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "NAEP Data Explorer"
                 }
             ],
+            "identifier": "e58c792b-3ddd-4b32-9e5a-7e4e8306b3db",
+            "issued": "2011-08-04",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "focus-groups",
@@ -74910,40 +74886,14 @@
                 "nies",
                 "report"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/nationsreportcard/data/researchcenter/qdata_post_04012011/2009_NIES_Part1_Variables.xls",
-                "https://nces.ed.gov/nationsreportcard/data/researchcenter/qdata_post_04012011/2009_NIES_Part2_Variables.xls",
-                "https://nces.ed.gov/nationsreportcard/data/researchcenter/qdata_post_04012011/2009_NIES_Part1_School_Variables.csv",
-                "https://nces.ed.gov/nationsreportcard/data/researchcenter/qdata_post_04012011/2009_NIES_Part1_SDELL_Variables.csv",
-                "https://nces.ed.gov/nationsreportcard/data/researchcenter/qdata_post_04012011/2009_NIES_Part1_Student_Variables.csv",
-                "https://nces.ed.gov/nationsreportcard/data/researchcenter/qdata_post_04012011/2009_NIES_Part1_Teacher_Variables.csv",
-                "https://nces.ed.gov/nationsreportcard/data/researchcenter/qdata_post_04012011/2009_NIES_Part2_School_Variables.csv",
-                "https://nces.ed.gov/nationsreportcard/data/researchcenter/qdata_post_04012011/2009_NIES_Part2_Student_Variables.csv",
-                "https://nces.ed.gov/nationsreportcard/data/researchcenter/qdata_post_04012011/2009_NIES_Part2_Teacher_Variables.csv",
-                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Household Education Surveys Program, 2005 After-School Programs And Activities Survey",
-            "description": "The National Household Education Survey, 2005 After-School Programs and Activities (ASPA-NHES:2005), is a study that is part of the National Household Education Survey (NHES) program. ASPA-NHES:2005 (https://nces.ed.gov/nhes/) is a cross-sectional survey that collects data directly from households on educational issues. This study was conducted using address based sample, self-administered questionnaires of households. Households in 2005 were sampled. The study response rate was 67.5 percent. Key statistics produced from ASPA-NHES:2005 are participation in after-school programs and activities.",
-            "modified": "2023-06-23T18:30:17.153581",
-            "accessLevel": "public",
-            "identifier": "9b5db297-29b4-460f-a153-a360076e33ec",
-            "dataQuality": true,
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2004/2005",
+            "modified": "2023-06-23T18:31:45.499569",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -74964,60 +74914,66 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/nationsreportcard/data/researchcenter/qdata_post_04012011/2009_NIES_Part1_Variables.xls",
+                "https://nces.ed.gov/nationsreportcard/data/researchcenter/qdata_post_04012011/2009_NIES_Part2_Variables.xls",
+                "https://nces.ed.gov/nationsreportcard/data/researchcenter/qdata_post_04012011/2009_NIES_Part1_School_Variables.csv",
+                "https://nces.ed.gov/nationsreportcard/data/researchcenter/qdata_post_04012011/2009_NIES_Part1_SDELL_Variables.csv",
+                "https://nces.ed.gov/nationsreportcard/data/researchcenter/qdata_post_04012011/2009_NIES_Part1_Student_Variables.csv",
+                "https://nces.ed.gov/nationsreportcard/data/researchcenter/qdata_post_04012011/2009_NIES_Part1_Teacher_Variables.csv",
+                "https://nces.ed.gov/nationsreportcard/data/researchcenter/qdata_post_04012011/2009_NIES_Part2_School_Variables.csv",
+                "https://nces.ed.gov/nationsreportcard/data/researchcenter/qdata_post_04012011/2009_NIES_Part2_Student_Variables.csv",
+                "https://nces.ed.gov/nationsreportcard/data/researchcenter/qdata_post_04012011/2009_NIES_Part2_Teacher_Variables.csv",
+                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".)",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
+            "temporal": "2008/2009",
+            "title": "National Indian Education Study, 2009"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sarah Grady",
                 "hasEmail": "mailto:sarah.grady@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Household Education Survey, 2005 After-School Programs and Activities (ASPA-NHES:2005), is a study that is part of the National Household Education Survey (NHES) program. ASPA-NHES:2005 (https://nces.ed.gov/nhes/) is a cross-sectional survey that collects data directly from households on educational issues. This study was conducted using address based sample, self-administered questionnaires of households. Households in 2005 were sampled. The study response rate was 67.5 percent. Key statistics produced from ASPA-NHES:2005 are participation in after-school programs and activities.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "aspa05asc.zip",
                     "description": "National Household Education Surveys Program, 2005 After-School Programs And Activities Survey, data as a zipped data file",
-                    "downloadURL": "https://nces.ed.gov/nhes/data/aspa05asc.zip"
+                    "downloadURL": "https://nces.ed.gov/nhes/data/aspa05asc.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "aspa05asc.zip"
                 }
             ],
+            "identifier": "9b5db297-29b4-460f-a153-a360076e33ec",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "after-school-programs-and-activities",
                 "education-and-care",
                 "households"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/nhes/pdf/userman/NHES_2005_Vol_I.pdf",
-                "https://nces.ed.gov/nhes/pdf/userman/NHES_2005_Vol_IV_AE.pdf",
-                "https://nces.ed.gov/nhes/pdf/adulted/2005_ae.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Longitudinal Transition Study-2",
-            "description": "The National Longitudinal Transition Study-2 (NLTS2) is a study that is part of the National Longitudinal Transition Study (NLTS) program; program data is available since 2000 at <https://ies.ed.gov/ncser/pubs/index.asp#nlts2>. NLTS2 (https://ies.ed.gov/ncser/projects/nlts2) is a longitudinal survey that was designed to provide a national picture of the experiences and achievements of students in special education during high school and as they transition from high school to adult life. NLTS2 involved five waves of data collection using three main data collection components: (1) telephone interviews with parents and youth who are capable of completing a phone interview; (2) direct assessments and in-person interviews with youth while they are in secondary school; and (3) the collection of school data (e.g., surveys of teachers, special education teachers, principals). A nationally representative sample of students who were 13 to 16 years old and receiving special education services in December 2000 when the study began were sampled, and these students were followed until 2010. Key statistics produced from NLTS2 are characteristics of secondary school students in special education and their households; secondary school experiences of students in special education, including their schools, school programs, related services, and extracurricular activities; experiences of students once they leave secondary school, including adult programs and services, social activities, etc.; and measurement of the secondary school and postschool outcomes of students in the education, employment, social, and residential domains.",
-            "modified": "2023-06-23T18:25:24.443054",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".)",
-            "identifier": "5ebf0612-c423-42f1-9044-eba5cb036f27",
-            "dataQuality": true,
-            "issued": "2012-03-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-23.pdf",
-            "temporal": "2001/2010",
+            "modified": "2023-06-23T18:30:17.153581",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "National Center for Special Education Research (NCSER)",
+                "name": "National Center for Education Statistics (NCES)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Institute of Education Sciences (IES)",
@@ -75035,20 +74991,40 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/nhes/pdf/userman/NHES_2005_Vol_I.pdf",
+                "https://nces.ed.gov/nhes/pdf/userman/NHES_2005_Vol_IV_AE.pdf",
+                "https://nces.ed.gov/nhes/pdf/adulted/2005_ae.pdf"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2004/2005",
+            "title": "National Household Education Surveys Program, 2005 After-School Programs And Activities Survey"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jacquelyn Buckley",
                 "hasEmail": "mailto:jacquelyn.buckley@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Longitudinal Transition Study-2 (NLTS2) is a study that is part of the National Longitudinal Transition Study (NLTS) program; program data is available since 2000 at <https://ies.ed.gov/ncser/pubs/index.asp#nlts2>. NLTS2 (https://ies.ed.gov/ncser/projects/nlts2) is a longitudinal survey that was designed to provide a national picture of the experiences and achievements of students in special education during high school and as they transition from high school to adult life. NLTS2 involved five waves of data collection using three main data collection components: (1) telephone interviews with parents and youth who are capable of completing a phone interview; (2) direct assessments and in-person interviews with youth while they are in secondary school; and (3) the collection of school data (e.g., surveys of teachers, special education teachers, principals). A nationally representative sample of students who were 13 to 16 years old and receiving special education services in December 2000 when the study began were sampled, and these students were followed until 2010. Key statistics produced from NLTS2 are characteristics of secondary school students in special education and their households; secondary school experiences of students in special education, including their schools, school programs, related services, and extracurricular activities; experiences of students once they leave secondary school, including adult programs and services, social activities, etc.; and measurement of the secondary school and postschool outcomes of students in the education, employment, social, and residential domains.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "National Longitudinal Transition Study-2 (NLTS2) restricted-use data",
                     "description": "All-wave restricted-use National Longitudinal Transition Study-2 (NLTS2) data",
                     "downloadURL": "https://ies.ed.gov/ncser/projects/datasets_nlts2.asp",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "National Longitudinal Transition Study-2 (NLTS2) restricted-use data"
                 }
             ],
+            "identifier": "5ebf0612-c423-42f1-9044-eba5cb036f27",
+            "issued": "2012-03-01",
             "keyword": [
                 "7e5b5019-7b00-43b5-917a-4c7c776296f2",
                 "absenteeism-school-attendance-and-completion-status",
@@ -75112,32 +75088,17 @@
                 "youths-household",
                 "youths-household-characteristics"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-23T18:25:24.443054",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Postsecondary Student Aid Study, 2007-08",
-            "description": "The National Postsecondary Student Aid Study, 2007-08 (NPSAS:08), is a study that is part of the National Postsecondary Student Aid Study (NPSAS) program. NPSAS:08 [https://nces.ed.gov/surveys/npsas/about.asp]is a cross-sectional survey that is designed to compile a comprehensive research dataset, based on student-level records, on financial aid provided by the federal government, the states, postsecondary institutions, employers, and private agencies, along with student demographic and enrollment data. The study was conducted using multiple sources, including institutional records, government databases, and student interviews. NPSAS:08 contains the data on a sample of 114,000 undergraduate students and 14,000 graduate students. These students were enrolled between July 1, 2007 and June 30, 2008 in about 1,730 postsecondary institutions. The data are representative of all undergraduate and graduate students enrolled in postsecondary institutions in the 50 United States, the District of Columbia, and Puerto Rico that were eligible to participate in the federal financial aid programs in Title IV of the Higher Education Act. Statistics produced from the NPSAS:08 provide reliable national estimates of characteristics related to financial aid for postsecondary students.",
-            "modified": "2023-06-23T18:23:46.915092",
-            "accessLevel": "public",
-            "identifier": "613922f7-1325-426e-a086-e836184a7939",
-            "dataQuality": true,
-            "issued": "2009-11-06",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2007/2008",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "National Center for Education Statistics (NCES)",
+                "name": "National Center for Special Education Research (NCSER)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Institute of Education Sciences (IES)",
@@ -75155,36 +75116,52 @@
                     }
                 }
             },
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".)",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-23.pdf",
+            "temporal": "2001/2010",
+            "title": "National Longitudinal Transition Study-2"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P4Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tracy Hunt-White",
                 "hasEmail": "mailto:tracy.hunt-white@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Postsecondary Student Aid Study, 2007-08 (NPSAS:08), is a study that is part of the National Postsecondary Student Aid Study (NPSAS) program. NPSAS:08 [https://nces.ed.gov/surveys/npsas/about.asp]is a cross-sectional survey that is designed to compile a comprehensive research dataset, based on student-level records, on financial aid provided by the federal government, the states, postsecondary institutions, employers, and private agencies, along with student demographic and enrollment data. The study was conducted using multiple sources, including institutional records, government databases, and student interviews. NPSAS:08 contains the data on a sample of 114,000 undergraduate students and 14,000 graduate students. These students were enrolled between July 1, 2007 and June 30, 2008 in about 1,730 postsecondary institutions. The data are representative of all undergraduate and graduate students enrolled in postsecondary institutions in the 50 United States, the District of Columbia, and Puerto Rico that were eligible to participate in the federal financial aid programs in Title IV of the Higher Education Act. Statistics produced from the NPSAS:08 provide reliable national estimates of characteristics related to financial aid for postsecondary students.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Datalab for Postsecondary Education",
                     "downloadURL": "https://nces.ed.gov/datalab/postsecondary/index.aspx",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Datalab for Postsecondary Education"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
-                    "format": "ASCII",
-                    "title": "np08gr",
                     "description": "NPSAS:08 Graduate Derived File",
-                    "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2010171rev2"
+                    "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2010171rev2",
+                    "format": "ASCII",
+                    "mediaType": "text/html",
+                    "title": "np08gr"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/html",
-                    "format": "ASCII",
-                    "title": "np08ug",
                     "description": "NPSAS:08 Undergraduate Derived File",
-                    "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2010171rev2"
+                    "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2010171rev2",
+                    "format": "ASCII",
+                    "mediaType": "text/html",
+                    "title": "np08ug"
                 }
             ],
+            "identifier": "613922f7-1325-426e-a086-e836184a7939",
+            "issued": "2009-11-06",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "cost-of-higher-education",
@@ -75193,30 +75170,14 @@
                 "postsecondary-education",
                 "student-record"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-23T18:23:46.915092",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Indian Education Study, 2011",
-            "description": "The National Indian Education Study, 2011 (NIES 2011), is a study that is part of the National Indian Education Study (NIES) within the National Assessment of Educational Progress (NAEP) program. NIES 2011 (https://nces.ed.gov/nationsreportcard/nies/) is a cross-sectional survey that is designed to describe the condition of education for American Indian and Alaska Native (AI/AN) students in the United States. Students in public, private, Department of Defense, and Bureau of Indian Education-funded schools were sampled and then assessed using a paper-and-pencil assessment instrument. The weighted response rates ranged from 80 to 92 percent. Key statistics produced from NIES 2011 provides educators, policymakers, and the public with information about the academic performance in reading and mathematics of AI/AN fourth- and eighth-graders, as well as information about their exposure to Native American culture.",
-            "modified": "2023-06-23T18:22:50.900187",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".)",
-            "identifier": "c1656d48-00b8-44c1-8f62-7b31013512c6",
-            "dataQuality": true,
-            "issued": "2012-07-03",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
-            "temporal": "2010/2011",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -75237,29 +75198,44 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2007/2008",
+            "title": "National Postsecondary Student Aid Study, 2007-08"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Linda Hamilton",
                 "hasEmail": "mailto:linda.hamilton@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Indian Education Study, 2011 (NIES 2011), is a study that is part of the National Indian Education Study (NIES) within the National Assessment of Educational Progress (NAEP) program. NIES 2011 (https://nces.ed.gov/nationsreportcard/nies/) is a cross-sectional survey that is designed to describe the condition of education for American Indian and Alaska Native (AI/AN) students in the United States. Students in public, private, Department of Defense, and Bureau of Indian Education-funded schools were sampled and then assessed using a paper-and-pencil assessment instrument. The weighted response rates ranged from 80 to 92 percent. Key statistics produced from NIES 2011 provides educators, policymakers, and the public with information about the academic performance in reading and mathematics of AI/AN fourth- and eighth-graders, as well as information about their exposure to Native American culture.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "NAEP Data Explorer",
                     "description": "2011 National Indian Education Study data available through the NAEP Data Explorer",
                     "downloadURL": "https://nces.ed.gov/nationsreportcard/niesdata",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "NAEP Data Explorer"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP 2011 National Indian Education Study (NIES) Restricted Use Data Files",
                     "description": "Restricted-use data file for the NAEP 2011 National Indian Education Study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2014473",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP 2011 National Indian Education Study (NIES) Restricted Use Data Files"
                 }
             ],
+            "identifier": "c1656d48-00b8-44c1-8f62-7b31013512c6",
+            "issued": "2012-07-03",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "focus-groups",
@@ -75269,33 +75245,14 @@
                 "nies",
                 "report"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Study of Postsecondary Faculty, 2004",
-            "description": "The National Study of Postsecondary Faculty, 2004 (NSOPF:04), is the last iteration in a series of studies that form the National Study of Postsecondary Faculty (NSOPF) program. NSOPF:04 (https://nces.ed.gov/surveys/nsopf/) is a cross-sectional survey that provides a national profile of postsecondary faculty and instructional staff: their professional backgrounds, responsibilities, workloads, salaries, benefits, and attitudes. The study was conducted using self-administered web-based questionnaires and a computer-assisted telephone interview (CATI) of postsecondary faculty and instructional staff. Postsecondary faculty and instructional staff in the academic term of Fall 2003 were sampled. The study weighted response rate was 76 percent for postsecondary faculty and 84 percent for institutions. Key statistics produced from NSOPF:04 are counts of faculty, faculty hires and departures, tenure of faculty, tenure policies, retirement and other benefits of faculty, faculty characteristics, employment history, current employment status including rank and tenure, workload, courses taught, publications, job satisfaction and attitudes, career and retirement plans, and benefits and compensation.",
-            "modified": "2023-06-23T18:19:45.231375",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".)",
-            "identifier": "6de62baf-4d69-4213-886e-994fd87e0a0e",
-            "dataQuality": true,
-            "issued": "2005-05-15",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2003/2004",
+            "modified": "2023-06-23T18:22:50.900187",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -75316,53 +75273,58 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".)",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
+            "temporal": "2010/2011",
+            "title": "National Indian Education Study, 2011"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Aurora D'Amico",
                 "hasEmail": "mailto:aurora.damico@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Study of Postsecondary Faculty, 2004 (NSOPF:04), is the last iteration in a series of studies that form the National Study of Postsecondary Faculty (NSOPF) program. NSOPF:04 (https://nces.ed.gov/surveys/nsopf/) is a cross-sectional survey that provides a national profile of postsecondary faculty and instructional staff: their professional backgrounds, responsibilities, workloads, salaries, benefits, and attitudes. The study was conducted using self-administered web-based questionnaires and a computer-assisted telephone interview (CATI) of postsecondary faculty and instructional staff. Postsecondary faculty and instructional staff in the academic term of Fall 2003 were sampled. The study weighted response rate was 76 percent for postsecondary faculty and 84 percent for institutions. Key statistics produced from NSOPF:04 are counts of faculty, faculty hires and departures, tenure of faculty, tenure policies, retirement and other benefits of faculty, faculty characteristics, employment history, current employment status including rank and tenure, workload, courses taught, publications, job satisfaction and attitudes, career and retirement plans, and benefits and compensation.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "datalab",
-                    "title": "NCES Datalab",
                     "description": "National Center for Education Statistics PowerStats for National Study of Postsecondary Faculty, 2004. Users may carry out tabular and regression-based analysis of NSOPF data without a restricted-use license through PowerStats",
                     "downloadURL": "https://nces.ed.gov/datalab/",
-                    "mediaType": "text/plain"
+                    "format": "datalab",
+                    "mediaType": "text/plain",
+                    "title": "NCES Datalab"
                 }
             ],
+            "identifier": "6de62baf-4d69-4213-886e-994fd87e0a0e",
+            "issued": "2005-05-15",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "faculty-careers",
                 "faculty-research",
                 "postsecondary-education"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-23T18:19:45.231375",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Pre-Elementary Education Longitudinal Study",
-            "description": "PEELS is a study that is part of the Pre-Elementary Education Longitudinal Study. PEELS (https://ies.ed.gov/ncser/projects/peels/) is a longitudinal survey that is designed to describe the characteristics of children receiving preschool special education, their educational programs and services, and their transitions from preschool programs to elementary schools. The study was conducted using CATI, paper questionnaires, and child assessments. The study followed a nationally representative sample of children with disabilities who were 3 to 5 years old at the start of the study in 2003 through 2009, examining the achievement of students with disabilities in preschool, kindergarten, and elementary school and determining the factors associated with this achievement. Key statistics produced from PEELS are characteristics of children and their families; characteristics of educational services and providers; transitions from early intervention to preschool, and preschool to elementary school; and school-related readiness and behavior.",
-            "modified": "2023-06-23T18:13:33.257116",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "c9c99c3c-ad4a-47e3-9ce4-f90a7aec65ed",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2003/2004",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "National Center for Special Education Research (NCSER)",
+                "name": "National Center for Education Statistics (NCES)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Institute of Education Sciences (IES)",
@@ -75380,27 +75342,42 @@
                     }
                 }
             },
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".)",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2003/2004",
+            "title": "National Study of Postsecondary Faculty, 2004"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Amy Sussman",
                 "hasEmail": "mailto:amy.sussman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "PEELS is a study that is part of the Pre-Elementary Education Longitudinal Study. PEELS (https://ies.ed.gov/ncser/projects/peels/) is a longitudinal survey that is designed to describe the characteristics of children receiving preschool special education, their educational programs and services, and their transitions from preschool programs to elementary schools. The study was conducted using CATI, paper questionnaires, and child assessments. The study followed a nationally representative sample of children with disabilities who were 3 to 5 years old at the start of the study in 2003 through 2009, examining the achievement of students with disabilities in preschool, kindergarten, and elementary school and determining the factors associated with this achievement. Key statistics produced from PEELS are characteristics of children and their families; characteristics of educational services and providers; transitions from early intervention to preschool, and preschool to elementary school; and school-related readiness and behavior.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "datalab",
-                    "title": "NCES Datalab",
                     "description": "National Center for Education Statistics PowerStats for Pre-Elementary Education Longitudinal Study (PEELS), Waves 1-5. Users may carry out tabular and regression-based analysis of PEELS data without a restricted-use license through PowerStats",
                     "downloadURL": "https://nces.ed.gov/datalab/",
-                    "mediaType": "text/plain"
+                    "format": "datalab",
+                    "mediaType": "text/plain",
+                    "title": "NCES Datalab"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Restricted-Use Data Files Pre-Elementary Education Longitudinal Study",
                     "downloadURL": "https://ies.ed.gov/ncser/projects/peels/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Restricted-Use Data Files Pre-Elementary Education Longitudinal Study"
                 }
             ],
+            "identifier": "c9c99c3c-ad4a-47e3-9ce4-f90a7aec65ed",
             "keyword": [
                 "7e5b5019-7b00-43b5-917a-4c7c776296f2",
                 "early-childhood",
@@ -75410,35 +75387,17 @@
                 "medical-information",
                 "preschoolers"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://ies.ed.gov/ncser/projects/datasets_peels.asp"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Household Education Surveys Program, 2007 School Readiness Survey",
-            "description": "The National Household Education Survey, 2007 School Readiness (SR-NHES:2007), is a study that is part of the National Household Education Survey (NHES) program. SR-NHES:2007 (https://nces.ed.gov/nhes/) is a cross-sectional survey that collects data directly from households on educational issues. This study was conducted using address based sample, self-administered questionnaires of households. Households in 2007 were sampled. The study's response rate was 53.2 percent. Key statistics produced from SR-NHES:2007 are children's readiness for school.",
-            "modified": "2023-06-23T18:11:36.938138",
-            "accessLevel": "public",
-            "identifier": "91b5cf0b-150f-45a5-a7dc-e6931911848f",
-            "dataQuality": true,
-            "issued": "2008-10-27",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2006/2007",
+            "modified": "2023-06-23T18:13:33.257116",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "National Center for Education Statistics (NCES)",
+                "name": "National Center for Special Education Research (NCSER)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Institute of Education Sciences (IES)",
@@ -75456,53 +75415,55 @@
                     }
                 }
             },
+            "references": [
+                "https://ies.ed.gov/ncser/projects/datasets_peels.asp"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "temporal": "2003/2004",
+            "title": "Pre-Elementary Education Longitudinal Study"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sarah Grady",
                 "hasEmail": "mailto:sarah.grady@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Household Education Survey, 2007 School Readiness (SR-NHES:2007), is a study that is part of the National Household Education Survey (NHES) program. SR-NHES:2007 (https://nces.ed.gov/nhes/) is a cross-sectional survey that collects data directly from households on educational issues. This study was conducted using address based sample, self-administered questionnaires of households. Households in 2007 were sampled. The study's response rate was 53.2 percent. Key statistics produced from SR-NHES:2007 are children's readiness for school.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped CSV",
-                    "title": "SR07Asc.zip",
-                    "description": "School Readiness public-use data",
                     "describedBy": "https://nces.ed.gov/nhes/pdf/userman/NHES_2007_SR_Codebook.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/nhes/data/SR07Asc.zip"
+                    "description": "School Readiness public-use data",
+                    "downloadURL": "https://nces.ed.gov/nhes/data/SR07Asc.zip",
+                    "format": "Zipped CSV",
+                    "mediaType": "application/zip",
+                    "title": "SR07Asc.zip"
                 }
             ],
+            "identifier": "91b5cf0b-150f-45a5-a7dc-e6931911848f",
+            "issued": "2008-10-27",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "households",
                 "school-readiness"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-23T18:11:36.938138",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Assessment of Educational Progress, 2009 High School Transcript Study",
-            "description": "The National Assessment of Educational Progress, 2009 High School Transcript Study (HSTS 2009), is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data available since 1990 at <https://nces.ed.gov/nationsreportcard/naepdata/>. HSTS 2009 (https://nces.ed.gov/nationsreportcard/hsts/) is a cross-sectional survey that periodically surveys the curricula being followed in our nation's high schools and the coursetaking patterns of high school students through a collection of transcripts. The study was conducted using survey of school administrative personnel and collection of students' transcripts. For public schools, the HSTS sample was a subsample of the NAEP 2009 twelfth-grade public school sample for the operational mathematics and science assessments. For private schools, the HSTS sample was the NAEP 2009 twelfth-grade private school sample for the operational mathematics and science assessments. The study weighted response rate was 83 percent. HSTS 2009 also offers information on the relationship of student coursetaking patterns to achievement at grade 12 as measured by NAEP. Key statistics produced from HSTS 2009 are information about the types of courses that graduates take, how many credits they earn, their grade point averages, and the relationship between coursetaking patterns and achievement, as measured by NAEP.",
-            "modified": "2023-06-23T17:21:53.416834",
-            "accessLevel": "restricted public",
-            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
-            "identifier": "e3a3586c-7533-490f-9e95-ebadc007dcf4",
-            "dataQuality": true,
-            "issued": "2011-07-19",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
-            "temporal": "2008/2009",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -75523,29 +75484,44 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2006/2007",
+            "title": "National Household Education Surveys Program, 2007 School Readiness Survey"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "restricted public",
             "accrualPeriodicity": "R/P4Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Linda Hamilton",
                 "hasEmail": "mailto:linda.hamilton@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Assessment of Educational Progress, 2009 High School Transcript Study (HSTS 2009), is a study that is part of the National Assessment of Educational Progress (NAEP) program; program data available since 1990 at <https://nces.ed.gov/nationsreportcard/naepdata/>. HSTS 2009 (https://nces.ed.gov/nationsreportcard/hsts/) is a cross-sectional survey that periodically surveys the curricula being followed in our nation's high schools and the coursetaking patterns of high school students through a collection of transcripts. The study was conducted using survey of school administrative personnel and collection of students' transcripts. For public schools, the HSTS sample was a subsample of the NAEP 2009 twelfth-grade public school sample for the operational mathematics and science assessments. For private schools, the HSTS sample was the NAEP 2009 twelfth-grade private school sample for the operational mathematics and science assessments. The study weighted response rate was 83 percent. HSTS 2009 also offers information on the relationship of student coursetaking patterns to achievement at grade 12 as measured by NAEP. Key statistics produced from HSTS 2009 are information about the types of courses that graduates take, how many credits they earn, their grade point averages, and the relationship between coursetaking patterns and achievement, as measured by NAEP.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "NAEP Data Explorer",
                     "description": "National Assessment of Educational Progress, 2009 High School Transcript Study data available through the NAEP Data Explorer",
                     "downloadURL": "https://nces.ed.gov/nationsreportcard/hstsdata/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "NAEP Data Explorer"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "NAEP High School Transcript Study 2009 Restricted-Use Data File",
                     "description": "Restricted-use data file for the National Assessment of Educational Progress, 2009 High School Transcript Study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2011490",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "NAEP High School Transcript Study 2009 Restricted-Use Data File"
                 }
             ],
+            "identifier": "e3a3586c-7533-490f-9e95-ebadc007dcf4",
+            "issued": "2011-07-19",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "achievement",
@@ -75560,36 +75536,20 @@
                 "progress-in-education",
                 "secondary-education"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EDFacts Migrant Education Program, 2010-11",
-            "description": "EDFacts Migrant Education Program, 2010-11 (EDFacts MEP:2010-11), is one of 17 'topics' identified in the EDFacts documentation (in this database, each 'topic' is entered as a separate study); program data is available since 2005 at <ed.gov/about/inits/ed/edfacts>. EDFacts MEP:2010-11 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states to support oversight and reporting of the Migrant Education Program (MEP) about students eligible for funding and students served under the migrant student program at the school, LEA, and state levels. EDFacts MEP:2010-11 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts MEP:2010-11 are from 10 data groups on Consolidated MEP Funds Status, MEP Personnel (FTE), MEP Personnel (Headcount), MEP Services, MEP Students Eligible and Served -Summer/Intersession, MEP Students Served - 12 - Month, MEP Students Served - Regular School Year, MEP Students Served - Summer/Intersession, Migrant Students Eligible - 12 - Month, and Migrant Students Eligible - Regular School Year. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
-            "modified": "2023-06-22T20:41:53.733817",
-            "accessLevel": "public",
-            "identifier": "8cfe677e-9b88-4f12-b907-1b74eee8c78c",
-            "dataQuality": true,
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2011/2012",
+            "modified": "2023-06-23T17:21:53.416834",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Migrant Education (MEP)",
+                "name": "National Center for Education Statistics (NCES)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of Elementary and Secondary Education (OESE)",
+                    "name": "Institute of Education Sciences (IES)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -75604,22 +75564,40 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/nationsreportcard/pdf/NDEQuickReferenceGuideWebVersion05.18.09.pdf"
+            ],
+            "rights": "IES uses Restricted-data Licenses as a mechanism for making more detailed data available to qualified researchers. Please request license to access data by submitting an application via the link in \"Resources\".",
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-03.pdf",
+            "temporal": "2008/2009",
+            "title": "National Assessment of Educational Progress, 2009 High School Transcript Study"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "EDFacts Migrant Education Program, 2010-11 (EDFacts MEP:2010-11), is one of 17 'topics' identified in the EDFacts documentation (in this database, each 'topic' is entered as a separate study); program data is available since 2005 at <ed.gov/about/inits/ed/edfacts>. EDFacts MEP:2010-11 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states to support oversight and reporting of the Migrant Education Program (MEP) about students eligible for funding and students served under the migrant student program at the school, LEA, and state levels. EDFacts MEP:2010-11 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts MEP:2010-11 are from 10 data groups on Consolidated MEP Funds Status, MEP Personnel (FTE), MEP Personnel (Headcount), MEP Services, MEP Students Eligible and Served -Summer/Intersession, MEP Students Served - 12 - Month, MEP Students Served - Regular School Year, MEP Students Served - Summer/Intersession, Migrant Students Eligible - 12 - Month, and Migrant Students Eligible - Regular School Year. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "ED Data Express",
                     "description": "EDFacts Migrant Education Program 2010-11 data available through ED Data Express",
                     "downloadURL": "https://eddataexpress.ed.gov/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "ED Data Express"
                 }
             ],
+            "identifier": "8cfe677e-9b88-4f12-b907-1b74eee8c78c",
             "keyword": [
                 "252a4986-4fc5-46d1-ae78-5c89bfb43b9a",
                 "adult-education",
@@ -75639,32 +75617,14 @@
                 "students",
                 "title-i"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:10"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://eddataexpress.ed.gov/faqs.cfm",
-                "https://eddataexpress.ed.gov/definitions.cfm"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EDFacts Migrant Education Program, 2012-13",
-            "description": "EDFacts Migrant Education Program, 2012-13 (EDFacts MEP:2012-13) is one of 17 topics identified in the EDFacts documentation (in this database, each topic is entered as a separate study). EDFacts MEP:2012-13 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states to support oversight and reporting of the Migrant Education Program (MEP) about students eligible for funding and students served under the migrant student program at the school, Local Education Agency, and state levels. EDFacts MEP:2012-13 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts MEP:2012-13 are from ten data groups on Consolidated MEP Funds Status, MEP Personnel (FTE), MEP Personnel (Headcount), MEP Services, MEP Students Eligible and Served-Summer/Intersession, MEP Students Served-12-Month, MEP Students Served-Regular School Year, MEP Students Served-Summer/Intersession, Migrant Students Eligible-12-Month, and Migrant Students Eligible-Regular School Year. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
-            "modified": "2023-06-22T20:40:46.691529",
-            "accessLevel": "public",
-            "identifier": "22d2dbd4-19a3-44a6-bcdd-6231f6d2ca30",
-            "dataQuality": true,
-            "issued": "2013-06-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2013/2014",
+            "modified": "2023-06-22T20:41:53.733817",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Migrant Education (MEP)",
@@ -75685,22 +75645,40 @@
                     }
                 }
             },
+            "references": [
+                "https://eddataexpress.ed.gov/faqs.cfm",
+                "https://eddataexpress.ed.gov/definitions.cfm"
+            ],
+            "spatial": "United States",
+            "temporal": "2011/2012",
+            "title": "EDFacts Migrant Education Program, 2010-11"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "EDFacts Migrant Education Program, 2012-13 (EDFacts MEP:2012-13) is one of 17 topics identified in the EDFacts documentation (in this database, each topic is entered as a separate study). EDFacts MEP:2012-13 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states to support oversight and reporting of the Migrant Education Program (MEP) about students eligible for funding and students served under the migrant student program at the school, Local Education Agency, and state levels. EDFacts MEP:2012-13 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts MEP:2012-13 are from ten data groups on Consolidated MEP Funds Status, MEP Personnel (FTE), MEP Personnel (Headcount), MEP Services, MEP Students Eligible and Served-Summer/Intersession, MEP Students Served-12-Month, MEP Students Served-Regular School Year, MEP Students Served-Summer/Intersession, Migrant Students Eligible-12-Month, and Migrant Students Eligible-Regular School Year. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "ED Data Express",
                     "description": "EDFacts Migrant Education Program 2012-13 data available through ED Data Express",
                     "downloadURL": "https://eddataexpress.ed.gov/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "ED Data Express"
                 }
             ],
+            "identifier": "22d2dbd4-19a3-44a6-bcdd-6231f6d2ca30",
+            "issued": "2013-06-01",
             "keyword": [
                 "252a4986-4fc5-46d1-ae78-5c89bfb43b9a",
                 "adult-education",
@@ -75720,32 +75698,14 @@
                 "students",
                 "title-i"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:10"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://eddataexpress.ed.gov/faqs.cfm",
-                "https://eddataexpress.ed.gov/definitions.cfm"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EDFacts Migrant Education Program, 2013-14",
-            "description": "EDFacts Migrant Education Program, 2013-14 (EDFacts MEP:2013-14) is one of 17 topics identified in the EDFacts documentation (in this database, each topic is entered as a separate study). EDFacts MEP:2013-14 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states to support oversight and reporting of the Migrant Education Program (MEP) about students eligible for funding and students served under the migrant student program at the school, Local Education Agency, and state levels. EDFacts MEP:2013-14 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts MEP:2013-14 are from ten data groups on Consolidated MEP Funds Status, MEP Personnel (FTE), MEP Personnel (Headcount), MEP Services, MEP Students Eligible and Served-Summer/Intersession, MEP Students Served-12-Month, MEP Students Served-Regular School Year, MEP Students Served-Summer/Intersession, Migrant Students Eligible-12-Month, and Migrant Students Eligible-Regular School Year. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
-            "modified": "2023-06-22T20:39:07.602271",
-            "accessLevel": "public",
-            "identifier": "f1c35942-25cc-42bc-9ace-80f2615d93a9",
-            "dataQuality": true,
-            "issued": "2013-06-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2014/2015",
+            "modified": "2023-06-22T20:40:46.691529",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Migrant Education (MEP)",
@@ -75766,22 +75726,40 @@
                     }
                 }
             },
+            "references": [
+                "https://eddataexpress.ed.gov/faqs.cfm",
+                "https://eddataexpress.ed.gov/definitions.cfm"
+            ],
+            "spatial": "United States",
+            "temporal": "2013/2014",
+            "title": "EDFacts Migrant Education Program, 2012-13"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "EDFacts Migrant Education Program, 2013-14 (EDFacts MEP:2013-14) is one of 17 topics identified in the EDFacts documentation (in this database, each topic is entered as a separate study). EDFacts MEP:2013-14 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states to support oversight and reporting of the Migrant Education Program (MEP) about students eligible for funding and students served under the migrant student program at the school, Local Education Agency, and state levels. EDFacts MEP:2013-14 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts MEP:2013-14 are from ten data groups on Consolidated MEP Funds Status, MEP Personnel (FTE), MEP Personnel (Headcount), MEP Services, MEP Students Eligible and Served-Summer/Intersession, MEP Students Served-12-Month, MEP Students Served-Regular School Year, MEP Students Served-Summer/Intersession, Migrant Students Eligible-12-Month, and Migrant Students Eligible-Regular School Year. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "ED Data Express",
                     "description": "EDFacts Migrant Education Program 2013-14 data available through ED Data Express",
                     "downloadURL": "https://eddataexpress.ed.gov/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "ED Data Express"
                 }
             ],
+            "identifier": "f1c35942-25cc-42bc-9ace-80f2615d93a9",
+            "issued": "2013-06-01",
             "keyword": [
                 "252a4986-4fc5-46d1-ae78-5c89bfb43b9a",
                 "adult-education",
@@ -75801,32 +75779,14 @@
                 "students",
                 "title-i"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:10"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://eddataexpress.ed.gov/faqs.cfm",
-                "https://eddataexpress.ed.gov/definitions.cfm"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EDFacts Migrant Education Program, 2016-17",
-            "description": "EDFacts Migrant Education Program, 2016-17 (EDFacts MEP:2016-17) is one of 17 topics identified in the EDFacts documentation (in this database, each topic is entered as a separate study). EDFacts MEP:2016-17 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states to support oversight and reporting of the Migrant Education Program (MEP) about students eligible for funding and students served under the migrant student program at the school, Local Education Agency, and state levels. EDFacts MEP:2016-17 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts MEP:2016-17 are from ten data groups on Consolidated MEP Funds Status, MEP Personnel (FTE), MEP Personnel (Headcount), MEP Services, MEP Students Eligible and Served-Summer/Intersession, MEP Students Served-12-Month, MEP Students Served-Regular School Year, MEP Students Served-Summer/Intersession, Migrant Students Eligible-12-Month, and Migrant Students Eligible-Regular School Year. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
-            "modified": "2023-06-22T20:37:14.826461",
-            "accessLevel": "public",
-            "identifier": "ee495b37-aa97-486e-a0c8-a14c8d0c2f79",
-            "dataQuality": true,
-            "issued": "2013-06-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2017/2018",
+            "modified": "2023-06-22T20:39:07.602271",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Migrant Education (MEP)",
@@ -75847,22 +75807,40 @@
                     }
                 }
             },
+            "references": [
+                "https://eddataexpress.ed.gov/faqs.cfm",
+                "https://eddataexpress.ed.gov/definitions.cfm"
+            ],
+            "spatial": "United States",
+            "temporal": "2014/2015",
+            "title": "EDFacts Migrant Education Program, 2013-14"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "EDFacts Migrant Education Program, 2016-17 (EDFacts MEP:2016-17) is one of 17 topics identified in the EDFacts documentation (in this database, each topic is entered as a separate study). EDFacts MEP:2016-17 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states to support oversight and reporting of the Migrant Education Program (MEP) about students eligible for funding and students served under the migrant student program at the school, Local Education Agency, and state levels. EDFacts MEP:2016-17 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts MEP:2016-17 are from ten data groups on Consolidated MEP Funds Status, MEP Personnel (FTE), MEP Personnel (Headcount), MEP Services, MEP Students Eligible and Served-Summer/Intersession, MEP Students Served-12-Month, MEP Students Served-Regular School Year, MEP Students Served-Summer/Intersession, Migrant Students Eligible-12-Month, and Migrant Students Eligible-Regular School Year. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "ED Data Express",
                     "description": "EDFacts Migrant Education Program 2016-17 data available through ED Data Express",
                     "downloadURL": "https://eddataexpress.ed.gov/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "ED Data Express"
                 }
             ],
+            "identifier": "ee495b37-aa97-486e-a0c8-a14c8d0c2f79",
+            "issued": "2013-06-01",
             "keyword": [
                 "252a4986-4fc5-46d1-ae78-5c89bfb43b9a",
                 "adult-education",
@@ -75882,32 +75860,14 @@
                 "students",
                 "title-i"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:10"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://eddataexpress.ed.gov/faqs.cfm",
-                "https://eddataexpress.ed.gov/definitions.cfm"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EDFacts Migrant Education Program, 2015-16",
-            "description": "EDFacts Migrant Education Program, 2015-16 (EDFacts MEP:2015-16) is one of 17 topics identified in the EDFacts documentation (in this database, each topic is entered as a separate study). EDFacts MEP:2015-16 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states to support oversight and reporting of the Migrant Education Program (MEP) about students eligible for funding and students served under the migrant student program at the school, Local Education Agency, and state levels. EDFacts MEP:2015-16 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts MEP:2015-16 are from ten data groups on Consolidated MEP Funds Status, MEP Personnel (FTE), MEP Personnel (Headcount), MEP Services, MEP Students Eligible and Served-Summer/Intersession, MEP Students Served-12-Month, MEP Students Served-Regular School Year, MEP Students Served-Summer/Intersession, Migrant Students Eligible-12-Month, and Migrant Students Eligible-Regular School Year. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
-            "modified": "2023-06-22T20:35:19.493912",
-            "accessLevel": "public",
-            "identifier": "88cb09ad-62ba-464d-ac25-8daf6bd0c80b",
-            "dataQuality": true,
-            "issued": "2013-06-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2016/2017",
+            "modified": "2023-06-22T20:37:14.826461",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Migrant Education (MEP)",
@@ -75928,22 +75888,40 @@
                     }
                 }
             },
+            "references": [
+                "https://eddataexpress.ed.gov/faqs.cfm",
+                "https://eddataexpress.ed.gov/definitions.cfm"
+            ],
+            "spatial": "United States",
+            "temporal": "2017/2018",
+            "title": "EDFacts Migrant Education Program, 2016-17"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "EDFacts Migrant Education Program, 2015-16 (EDFacts MEP:2015-16) is one of 17 topics identified in the EDFacts documentation (in this database, each topic is entered as a separate study). EDFacts MEP:2015-16 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states to support oversight and reporting of the Migrant Education Program (MEP) about students eligible for funding and students served under the migrant student program at the school, Local Education Agency, and state levels. EDFacts MEP:2015-16 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts MEP:2015-16 are from ten data groups on Consolidated MEP Funds Status, MEP Personnel (FTE), MEP Personnel (Headcount), MEP Services, MEP Students Eligible and Served-Summer/Intersession, MEP Students Served-12-Month, MEP Students Served-Regular School Year, MEP Students Served-Summer/Intersession, Migrant Students Eligible-12-Month, and Migrant Students Eligible-Regular School Year. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "ED Data Express",
                     "description": "EDFacts Migrant Education Program 2015-16 data available through ED Data Express",
                     "downloadURL": "https://eddataexpress.ed.gov/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "ED Data Express"
                 }
             ],
+            "identifier": "88cb09ad-62ba-464d-ac25-8daf6bd0c80b",
+            "issued": "2013-06-01",
             "keyword": [
                 "252a4986-4fc5-46d1-ae78-5c89bfb43b9a",
                 "adult-education",
@@ -75963,32 +75941,14 @@
                 "students",
                 "title-i"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:10"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://eddataexpress.ed.gov/faqs.cfm",
-                "https://eddataexpress.ed.gov/definitions.cfm"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EDFacts Migrant Education Program, 2014-15",
-            "description": "EDFacts Migrant Education Program, 2014-15 (EDFacts MEP:2014-15) is one of 17 topics identified in the EDFacts documentation (in this database, each topic is entered as a separate study). EDFacts MEP:2014-15 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states to support oversight and reporting of the Migrant Education Program (MEP) about students eligible for funding and students served under the migrant student program at the school, Local Education Agency, and state levels. EDFacts MEP:2014-15 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts MEP:2014-15 are from ten data groups on Consolidated MEP Funds Status, MEP Personnel (FTE), MEP Personnel (Headcount), MEP Services, MEP Students Eligible and Served-Summer/Intersession, MEP Students Served-12-Month, MEP Students Served-Regular School Year, MEP Students Served-Summer/Intersession, Migrant Students Eligible-12-Month, and Migrant Students Eligible-Regular School Year. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
-            "modified": "2023-06-22T20:32:40.653834",
-            "accessLevel": "public",
-            "identifier": "9cb7ebbc-6d48-4056-8a98-9ff2f6630fdb",
-            "dataQuality": true,
-            "issued": "2013-06-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2015/2016",
+            "modified": "2023-06-22T20:35:19.493912",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of Migrant Education (MEP)",
@@ -76009,22 +75969,40 @@
                     }
                 }
             },
+            "references": [
+                "https://eddataexpress.ed.gov/faqs.cfm",
+                "https://eddataexpress.ed.gov/definitions.cfm"
+            ],
+            "spatial": "United States",
+            "temporal": "2016/2017",
+            "title": "EDFacts Migrant Education Program, 2015-16"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "EDFacts Migrant Education Program, 2014-15 (EDFacts MEP:2014-15) is one of 17 topics identified in the EDFacts documentation (in this database, each topic is entered as a separate study). EDFacts MEP:2014-15 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states to support oversight and reporting of the Migrant Education Program (MEP) about students eligible for funding and students served under the migrant student program at the school, Local Education Agency, and state levels. EDFacts MEP:2014-15 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts MEP:2014-15 are from ten data groups on Consolidated MEP Funds Status, MEP Personnel (FTE), MEP Personnel (Headcount), MEP Services, MEP Students Eligible and Served-Summer/Intersession, MEP Students Served-12-Month, MEP Students Served-Regular School Year, MEP Students Served-Summer/Intersession, Migrant Students Eligible-12-Month, and Migrant Students Eligible-Regular School Year. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "ED Data Express",
                     "description": "EDFacts Migrant Education Program 2014-15 data available through ED Data Express",
                     "downloadURL": "https://eddataexpress.ed.gov/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "ED Data Express"
                 }
             ],
+            "identifier": "9cb7ebbc-6d48-4056-8a98-9ff2f6630fdb",
+            "issued": "2013-06-01",
             "keyword": [
                 "252a4986-4fc5-46d1-ae78-5c89bfb43b9a",
                 "adult-education",
@@ -76044,55 +76022,67 @@
                 "students",
                 "title-i"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:10"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://eddataexpress.ed.gov/faqs.cfm",
-                "https://eddataexpress.ed.gov/definitions.cfm"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EDFacts Title I, 2010-11",
-            "description": "EDFacts Title I, 2010-11 (EDFacts T1:2010-11), is one of 17 'topics' identified in the EDFacts documentation (in this database, each 'topic' is entered as a separate study); program data is available since 2005 at <ed.gov/about/inits/ed/edfacts>. EDFacts T1:2010-11 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states about student participants and staff of Title I, Part A of the Elementary and Secondary Act (ESEA), as amended, at the school, LEA, and state levels. EDFacts T1:2010-11 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts T1:2010-11 are from 18 data groups with information on Economically Disadvantaged Students, School Poverty Indicator, Public School Choice - Eligible, Public School Choice - Applied for Transfer, Public School Choice - Transferred, Public School Choice - Implementation, Public School Choice - 20% Transportation Reservation, Public School Choice - Funds Spent, SES - Applied to Receive Services, SES - Eligible to Receive Services, SES - Funds Spent, SES - Per Pupil Expenditure, SES - Received Services, Title I Part A Participation, Title I Status, Title I Part A SWP/TAS Participation, Title I TAS Staff Funded (FTE), Title I Part A TAS. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
-            "modified": "2023-06-22T20:28:25.209424",
-            "accessLevel": "public",
-            "identifier": "331369e8-d055-4b95-9af2-962f4324556e",
-            "dataQuality": true,
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2011/2012",
+            "modified": "2023-06-22T20:32:40.653834",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of Migrant Education (MEP)",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of Elementary and Secondary Education (OESE)",
+                    "subOrganizationOf": {
+                        "@type": "org:Organization",
+                        "name": "Office of the Secretary (OS)",
+                        "subOrganizationOf": {
                             "@type": "org:Organization",
                             "name": "U.S. Department of Education",
                             "subOrganizationOf": {
                                 "@type": "org:Organization",
                                 "name": "U.S. Government"
                             }
+                        }
+                    }
+                }
             },
+            "references": [
+                "https://eddataexpress.ed.gov/faqs.cfm",
+                "https://eddataexpress.ed.gov/definitions.cfm"
+            ],
+            "spatial": "United States",
+            "temporal": "2015/2016",
+            "title": "EDFacts Migrant Education Program, 2014-15"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "EDFacts Title I, 2010-11 (EDFacts T1:2010-11), is one of 17 'topics' identified in the EDFacts documentation (in this database, each 'topic' is entered as a separate study); program data is available since 2005 at <ed.gov/about/inits/ed/edfacts>. EDFacts T1:2010-11 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states about student participants and staff of Title I, Part A of the Elementary and Secondary Act (ESEA), as amended, at the school, LEA, and state levels. EDFacts T1:2010-11 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts T1:2010-11 are from 18 data groups with information on Economically Disadvantaged Students, School Poverty Indicator, Public School Choice - Eligible, Public School Choice - Applied for Transfer, Public School Choice - Transferred, Public School Choice - Implementation, Public School Choice - 20% Transportation Reservation, Public School Choice - Funds Spent, SES - Applied to Receive Services, SES - Eligible to Receive Services, SES - Funds Spent, SES - Per Pupil Expenditure, SES - Received Services, Title I Part A Participation, Title I Status, Title I Part A SWP/TAS Participation, Title I TAS Staff Funded (FTE), Title I Part A TAS. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "ED Data Express",
                     "description": "EDFacts Title I 2010-11 data available through ED Data Express",
                     "downloadURL": "https://eddataexpress.ed.gov/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "ED Data Express"
                 }
             ],
+            "identifier": "331369e8-d055-4b95-9af2-962f4324556e",
             "keyword": [
                 "7c15ea20-6617-4989-aa89-4f48c8a5517a",
                 "edfacts",
@@ -76121,100 +76111,77 @@
                 "tas",
                 "title-i"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://eddataexpress.ed.gov/faqs.cfm",
-                "https://eddataexpress.ed.gov/definitions.cfm"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Household Education Surveys Program, 2007 Parent and Family Involvement in Education Survey",
-            "description": "The National Household Education Survey, 2007 Parent and Family Involvement in Education (PFI-NHES:2007), is a study that is part of the National Household Education Survey (NHES) program. PFI-NHES:2007 (https://nces.ed.gov/nhes/) is a cross-sectional survey that collects data directly from households on educational issues. This study was conducted using address based sample, self-administered questionnaires of households. Households in 2007 were sampled. The study's response rate was 53.2 percent. Key statistics produced from PFI-NHES:2007 are parent involvement in education.",
-            "modified": "2023-06-22T20:27:47.971406",
-            "accessLevel": "public",
-            "identifier": "451c09e0-9c35-4d9e-a232-73615c73215a",
-            "dataQuality": true,
-            "issued": "2008-10-27",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2006/2007",
+            "modified": "2023-06-22T20:28:25.209424",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Education Statistics (NCES)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Institute of Education Sciences (IES)",
-                    "subOrganizationOf": {
-                        "@type": "org:Organization",
-                        "name": "Office of the Secretary (OS)",
-                        "subOrganizationOf": {
                 "@type": "org:Organization",
                 "name": "U.S. Department of Education",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "U.S. Government"
                 }
-                        }
-                    }
-                }
             },
+            "references": [
+                "https://eddataexpress.ed.gov/faqs.cfm",
+                "https://eddataexpress.ed.gov/definitions.cfm"
+            ],
+            "spatial": "United States",
+            "temporal": "2011/2012",
+            "title": "EDFacts Title I, 2010-11"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sarah Grady",
                 "hasEmail": "mailto:sarah.grady@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Household Education Survey, 2007 Parent and Family Involvement in Education (PFI-NHES:2007), is a study that is part of the National Household Education Survey (NHES) program. PFI-NHES:2007 (https://nces.ed.gov/nhes/) is a cross-sectional survey that collects data directly from households on educational issues. This study was conducted using address based sample, self-administered questionnaires of households. Households in 2007 were sampled. The study's response rate was 53.2 percent. Key statistics produced from PFI-NHES:2007 are parent involvement in education.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped CSV",
-                    "title": "PFI07Asc.zip",
-                    "description": "Parent and Family Involvement in Education public-use data",
                     "describedBy": "https://nces.ed.gov/nhes/pdf/userman/NHES_2007_PFI_Codebook.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/nhes/data/PFI07Asc.zip"
+                    "description": "Parent and Family Involvement in Education public-use data",
+                    "downloadURL": "https://nces.ed.gov/nhes/data/PFI07Asc.zip",
+                    "format": "Zipped CSV",
+                    "mediaType": "application/zip",
+                    "title": "PFI07Asc.zip"
                 }
             ],
+            "identifier": "451c09e0-9c35-4d9e-a232-73615c73215a",
+            "issued": "2008-10-27",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "homeschooling",
                 "parental-involvement-in-education"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-22T20:27:47.971406",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EDFacts Title III/Limited English Proficiency, 2010-11",
-            "description": "EDFacts Title III/Limited English Proficiency, 2010-11 (EDFacts T3/LEP:2010-11), is one of 17 'topics' identified in the EDFacts documentation (in this database, each 'topic' is entered as a separate study); program data is available since 2005 at <ed.gov/about/inits/ed/edfacts>. EDFacts T3/LEP:2010-11 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states to support oversight and reporting of programs for the education of limited English proficient students as contained in Title I and Title III of the Elementary and Secondary Education Act (ESEA), as amended. Title III also provides programs for students who are immigrants at the SEA and LEA levels. EDFacts T3/LEP:2010-11 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts T3/LEP:2010-11 are from 13 data groups: AMAO I LEP Making Progress, AMAO II LEP English Attainment, AMAO III AYP for LEP, Immigrant, LEP Enrolled, LEP Students in LEP Program, LEP English Language Proficiency Results, LEP English Language Proficiency Test, Title III Teachers, Title III LEP English Language Proficiency Results, Title III LEP English Language Proficiency Test, Title III LEP Students Served, and Title III Former LEP Students. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
-            "modified": "2023-06-22T20:26:52.618603",
-            "accessLevel": "public",
-            "identifier": "313fb450-8b70-441c-93cd-10096b4213b1",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2011/2012",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of English Language Acquisition (OELA)",
+                "name": "National Center for Education Statistics (NCES)",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Institute of Education Sciences (IES)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -76227,23 +76194,38 @@
                             }
                         }
                     }
+                }
+            },
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2006/2007",
+            "title": "National Household Education Surveys Program, 2007 Parent and Family Involvement in Education Survey"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "EDFacts Title III/Limited English Proficiency, 2010-11 (EDFacts T3/LEP:2010-11), is one of 17 'topics' identified in the EDFacts documentation (in this database, each 'topic' is entered as a separate study); program data is available since 2005 at <ed.gov/about/inits/ed/edfacts>. EDFacts T3/LEP:2010-11 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states to support oversight and reporting of programs for the education of limited English proficient students as contained in Title I and Title III of the Elementary and Secondary Education Act (ESEA), as amended. Title III also provides programs for students who are immigrants at the SEA and LEA levels. EDFacts T3/LEP:2010-11 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts T3/LEP:2010-11 are from 13 data groups: AMAO I LEP Making Progress, AMAO II LEP English Attainment, AMAO III AYP for LEP, Immigrant, LEP Enrolled, LEP Students in LEP Program, LEP English Language Proficiency Results, LEP English Language Proficiency Test, Title III Teachers, Title III LEP English Language Proficiency Results, Title III LEP English Language Proficiency Test, Title III LEP Students Served, and Title III Former LEP Students. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "ED Data Express",
                     "description": "EDFacts Title III/Limited English Proficiency 2010-11 data available through ED Data Express",
                     "downloadURL": "https://eddataexpress.ed.gov/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "ED Data Express"
                 }
             ],
+            "identifier": "313fb450-8b70-441c-93cd-10096b4213b1",
             "keyword": [
                 "6c548925-1c84-490a-b972-9ef7c1ca1183",
                 "amao",
@@ -76263,39 +76245,17 @@
                 "title-iii-lep",
                 "title-iiilep"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:15"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://eddataexpress.ed.gov/faqs.cfm",
-                "https://eddataexpress.ed.gov/definitions.cfm"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Household Education Surveys Program, 2005 Early Childhood Program Participation Survey",
-            "description": "The National Household Education Survey, 2005 Early Childhood Program Participation (ECPP-NHES:2005), is a study that is part of the National Household Education Survey (NHES) program. ECPP-NHES:2005 (https://nces.ed.gov/nhes/) is a cross-sectional survey that collects data directly from households on educational issues. This study was conducted using address based sample, self-administered questionnaires of households. Households in 2005 were sampled. The study's response rate was 67.5 percent. Key statistics produced from ECPP-NHES:2005 are participation in early childhood education and care programs.",
-            "modified": "2023-06-22T20:26:24.222535",
-            "accessLevel": "public",
-            "identifier": "10578759-1178-4dac-9ad2-e337daf402e3",
-            "dataQuality": true,
-            "issued": "2006-07-07",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2004/2005",
+            "modified": "2023-06-22T20:26:52.618603",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "National Center for Education Statistics (NCES)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Institute of Education Sciences (IES)",
+                "name": "Office of English Language Acquisition (OELA)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Office of the Secretary (OS)",
@@ -76308,54 +76268,56 @@
                         }
                     }
                 }
-                }
             },
+            "references": [
+                "https://eddataexpress.ed.gov/faqs.cfm",
+                "https://eddataexpress.ed.gov/definitions.cfm"
+            ],
+            "spatial": "United States",
+            "temporal": "2011/2012",
+            "title": "EDFacts Title III/Limited English Proficiency, 2010-11"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sarah Grady",
                 "hasEmail": "mailto:sarah.grady@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Household Education Survey, 2005 Early Childhood Program Participation (ECPP-NHES:2005), is a study that is part of the National Household Education Survey (NHES) program. ECPP-NHES:2005 (https://nces.ed.gov/nhes/) is a cross-sectional survey that collects data directly from households on educational issues. This study was conducted using address based sample, self-administered questionnaires of households. Households in 2005 were sampled. The study's response rate was 67.5 percent. Key statistics produced from ECPP-NHES:2005 are participation in early childhood education and care programs.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped CSV",
-                    "title": "ecpp05asc.zip",
-                    "description": "Early Childhood Program Participation public-use data",
                     "describedBy": "https://nces.ed.gov/nhes/pdf/userman/NHES_2005_ECPP_Codebook.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/nhes/data/ecpp05asc.zip"
+                    "description": "Early Childhood Program Participation public-use data",
+                    "downloadURL": "https://nces.ed.gov/nhes/data/ecpp05asc.zip",
+                    "format": "Zipped CSV",
+                    "mediaType": "application/zip",
+                    "title": "ecpp05asc.zip"
                 }
             ],
+            "identifier": "10578759-1178-4dac-9ad2-e337daf402e3",
+            "issued": "2006-07-07",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "early-childhood-care",
                 "early-childhood-education"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-22T20:26:24.222535",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Household Education Surveys Program, 2005 Adult Education Survey",
-            "description": "The National Household Education Survey, 2005 Adult Education (AE-NHES:2005), is a study that is part of the National Household Education Survey (NHES) program. AE-NHES:2005 (https://nces.ed.gov/nhes/) is a cross-sectional survey that collects data directly from households on educational issues. This study was conducted using address based sample, self-administered questionnaires of households. Households in 2005 were sampled. The study's response rate was 67.5 percent. Key statistics produced from AE-NHES:2005 are participation in adult and continuing education and lifelong learning.",
-            "modified": "2023-06-22T20:25:39.652070",
-            "accessLevel": "public",
-            "identifier": "1661d277-822b-4e38-aa67-fd1a56343402",
-            "dataQuality": true,
-            "issued": "2006-05-31",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2004/2005",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -76376,81 +76338,109 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2004/2005",
+            "title": "National Household Education Surveys Program, 2005 Early Childhood Program Participation Survey"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sarah Grady",
                 "hasEmail": "mailto:sarah.grady@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Household Education Survey, 2005 Adult Education (AE-NHES:2005), is a study that is part of the National Household Education Survey (NHES) program. AE-NHES:2005 (https://nces.ed.gov/nhes/) is a cross-sectional survey that collects data directly from households on educational issues. This study was conducted using address based sample, self-administered questionnaires of households. Households in 2005 were sampled. The study's response rate was 67.5 percent. Key statistics produced from AE-NHES:2005 are participation in adult and continuing education and lifelong learning.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "ae05asc.zip",
-                    "description": "National Household Education Surveys Program, 2005 Adult Education Survey, data as a zipped ASCII data file",
                     "describedBy": "https://nces.ed.gov/nhes/pdf/userman/NHES_2005_AE_Codebook.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/nhes/data/ae05asc.zip"
+                    "description": "National Household Education Surveys Program, 2005 Adult Education Survey, data as a zipped ASCII data file",
+                    "downloadURL": "https://nces.ed.gov/nhes/data/ae05asc.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "ae05asc.zip"
                 }
             ],
+            "identifier": "1661d277-822b-4e38-aa67-fd1a56343402",
+            "issued": "2006-05-31",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "adult-education",
                 "continuing-education",
                 "lifelong-learning"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/nhes/pdf/userman/NHES_2005_Vol_I.pdf",
-                "https://nces.ed.gov/nhes/pdf/userman/NHES_2005_Vol_IV_AE.pdf",
-                "https://nces.ed.gov/nhes/pdf/adulted/2005_ae.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "EDFacts Title I, 2011-12",
-            "description": "EDFacts Title I, 2011-12 (EDFacts T1:2011-12), is one of 17 'topics' identified in the EDFacts documentation (in this database, each 'topic' is entered as a separate study); program data is available since 2005 at <ed.gov/about/inits/ed/edfacts>. EDFacts T1:2011-12 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states about student participants and staff of Title I, Part A of the Elementary and Secondary Act (ESEA), as amended, at the school, LEA, and state levels. EDFacts T1:2011-12 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts T1:2011-12 are from 18 data groups with information on Economically Disadvantaged Students, School Poverty Indicator, Public School Choice - Eligible, Public School Choice - Applied for Transfer, Public School Choice - Transferred, Public School Choice - Implementation, Public School Choice - 20% Transportation Reservation, Public School Choice - Funds Spent, SES - Applied to Receive Services, SES - Eligible to Receive Services, SES - Funds Spent, SES - Per Pupil Expenditure, SES - Received Services, Title I Part A Participation, Title I Status, Title I Part A SWP/TAS Participation, Title I TAS Staff Funded (FTE), Title I Part A TAS. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
-            "modified": "2023-06-22T20:24:23.866468",
-            "accessLevel": "public",
-            "identifier": "80ba0e83-4959-43a0-975a-eb5762d62e73",
-            "dataQuality": true,
-            "issued": "2013-06-01",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2012/2013",
+            "modified": "2023-06-22T20:25:39.652070",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Education Statistics (NCES)",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Institute of Education Sciences (IES)",
+                    "subOrganizationOf": {
+                        "@type": "org:Organization",
+                        "name": "Office of the Secretary (OS)",
+                        "subOrganizationOf": {
                             "@type": "org:Organization",
                             "name": "U.S. Department of Education",
                             "subOrganizationOf": {
                                 "@type": "org:Organization",
                                 "name": "U.S. Government"
                             }
+                        }
+                    }
+                }
+            },
+            "references": [
+                "https://nces.ed.gov/nhes/pdf/userman/NHES_2005_Vol_I.pdf",
+                "https://nces.ed.gov/nhes/pdf/userman/NHES_2005_Vol_IV_AE.pdf",
+                "https://nces.ed.gov/nhes/pdf/adulted/2005_ae.pdf"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2004/2005",
+            "title": "National Household Education Surveys Program, 2005 Adult Education Survey"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "EDFacts Title I, 2011-12 (EDFacts T1:2011-12), is one of 17 'topics' identified in the EDFacts documentation (in this database, each 'topic' is entered as a separate study); program data is available since 2005 at <ed.gov/about/inits/ed/edfacts>. EDFacts T1:2011-12 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states about student participants and staff of Title I, Part A of the Elementary and Secondary Act (ESEA), as amended, at the school, LEA, and state levels. EDFacts T1:2011-12 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts T1:2011-12 are from 18 data groups with information on Economically Disadvantaged Students, School Poverty Indicator, Public School Choice - Eligible, Public School Choice - Applied for Transfer, Public School Choice - Transferred, Public School Choice - Implementation, Public School Choice - 20% Transportation Reservation, Public School Choice - Funds Spent, SES - Applied to Receive Services, SES - Eligible to Receive Services, SES - Funds Spent, SES - Per Pupil Expenditure, SES - Received Services, Title I Part A Participation, Title I Status, Title I Part A SWP/TAS Participation, Title I TAS Staff Funded (FTE), Title I Part A TAS. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "ED Data Express",
                     "description": "EDFacts Title I 2011-12 data available through ED Data Express",
                     "downloadURL": "https://eddataexpress.ed.gov/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "ED Data Express"
                 }
             ],
+            "identifier": "80ba0e83-4959-43a0-975a-eb5762d62e73",
+            "issued": "2013-06-01",
             "keyword": [
                 "7c15ea20-6617-4989-aa89-4f48c8a5517a",
                 "edfacts",
@@ -76479,33 +76469,70 @@
                 "tas",
                 "title-i"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-22T20:24:23.866468",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Department of Education",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "U.S. Government"
+                }
+            },
             "references": [
                 "https://eddataexpress.ed.gov/faqs.cfm",
                 "https://eddataexpress.ed.gov/definitions.cfm"
-            ]
+            ],
+            "spatial": "United States",
+            "temporal": "2012/2013",
+            "title": "EDFacts Title I, 2011-12"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "National Household Education Surveys Program, 2003 Parent and Family Involvement in Education Survey",
-            "description": "The National Household Education Survey, 2003 Parent and Family Involvement in Education (PFI-NHES:2003), is a study that is part of the National Household Education Survey (NHES) program. PFI-NHES:2003 (https://nces.ed.gov/nhes/) is a cross-sectional survey that collects data directly from households on educational issues. This study was conducted using an address based sample of self-administered questionnaires of households. Households in 2003 were sampled. The study's response rate was 64.7 percent. Key statistics produced from PFI-NHES:2003 are early childhood care and education, children's readiness for school, parent perceptions of school safety and discipline, before- and after-school activities of school-age children, and homeschooling.",
-            "modified": "2023-06-22T20:23:41.502263",
             "accessLevel": "public",
-            "identifier": "4fd7fccf-50fb-4130-9e38-e449b0dcd500",
+            "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Sarah Grady",
+                "hasEmail": "mailto:sarah.grady@ed.gov"
+            },
             "dataQuality": true,
+            "description": "The National Household Education Survey, 2003 Parent and Family Involvement in Education (PFI-NHES:2003), is a study that is part of the National Household Education Survey (NHES) program. PFI-NHES:2003 (https://nces.ed.gov/nhes/) is a cross-sectional survey that collects data directly from households on educational issues. This study was conducted using an address based sample of self-administered questionnaires of households. Households in 2003 were sampled. The study's response rate was 64.7 percent. Key statistics produced from PFI-NHES:2003 are early childhood care and education, children's readiness for school, parent perceptions of school safety and discipline, before- and after-school activities of school-age children, and homeschooling.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "describedBy": "https://nces.ed.gov/nhes/pdf/codebook/NHES_2003_PFI_Codebook.pdf",
+                    "describedByType": "application/pdf",
+                    "description": "Parent and Family Involvement in Education public-use data",
+                    "downloadURL": "https://nces.ed.gov/nhes/data/pfiasc.zip",
+                    "format": "Zipped CSV",
+                    "mediaType": "application/zip",
+                    "title": "pfiasc.zip"
+                }
+            ],
+            "identifier": "4fd7fccf-50fb-4130-9e38-e449b0dcd500",
             "issued": "2004-08-06",
+            "keyword": [
+                "0ee4621b-38be-46bb-8360-219726022a58",
+                "parental-involvement-in-education-homeschooling"
+            ],
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2002/2003",
+            "modified": "2023-06-22T20:23:41.502263",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -76526,81 +76553,36 @@
                     }
                 }
             },
-            "accrualPeriodicity": "irregular",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Sarah Grady",
-                "hasEmail": "mailto:sarah.grady@ed.gov"
-            },
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped CSV",
-                    "title": "pfiasc.zip",
-                    "description": "Parent and Family Involvement in Education public-use data",
-                    "describedBy": "https://nces.ed.gov/nhes/pdf/codebook/NHES_2003_PFI_Codebook.pdf",
-                    "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/nhes/data/pfiasc.zip"
-                }
-            ],
-            "keyword": [
-                "0ee4621b-38be-46bb-8360-219726022a58",
-                "parental-involvement-in-education-homeschooling"
-            ],
             "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
-            "language": [
-                "en-US"
-            ]
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2002/2003",
+            "title": "National Household Education Surveys Program, 2003 Parent and Family Involvement in Education Survey"
         },
         {
             "@type": "dcat:Dataset",
-            "title": "EDFacts Title III/Limited English Proficiency, 2011-12",
-            "description": "EDFacts Title III/Limited English Proficiency, 2011-12 (EDFacts T3/LEP:2011-12), is one of 17 'topics' identified in the EDFacts documentation (in this database, each 'topic' is entered as a separate study); program data is available since 2005 at <ed.gov/about/inits/ed/edfacts>. EDFacts T3/LEP:2011-12 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states to support oversight and reporting of programs for the education of limited English proficient students as contained in Title I and Title III of the Elementary and Secondary Education Act (ESEA), as amended. Title III also provides programs for students who are immigrants at the SEA and LEA levels. EDFacts T3/LEP:2011-12 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts T3/LEP:2011-12 are from 13 data groups: AMAO I LEP Making Progress, AMAO II LEP English Attainment, AMAO III AYP for LEP, Immigrant, LEP Enrolled, LEP Students in LEP Program, LEP English Language Proficiency Results, LEP English Language Proficiency Test, Title III Teachers, Title III LEP English Language Proficiency Results, Title III LEP English Language Proficiency Test, Title III LEP Students Served, and Title III Former LEP Students. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
-            "modified": "2023-06-22T20:22:12.631498",
             "accessLevel": "public",
-            "identifier": "444ecc2e-3907-48e5-89a0-682f60bf7704",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2011/2012",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of English Language Acquisition (OELA)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of the Secretary (OS)",
-                    "subOrganizationOf": {
-                        "@type": "org:Organization",
-                        "name": "U.S. Department of Education",
-                        "subOrganizationOf": {
-                            "@type": "org:Organization",
-                            "name": "U.S. Government"
-                        }
-                    }
-                }
-            },
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:15"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kelly Worthington",
                 "hasEmail": "mailto:kelly.worthington@ed.gov"
             },
+            "dataQuality": true,
+            "description": "EDFacts Title III/Limited English Proficiency, 2011-12 (EDFacts T3/LEP:2011-12), is one of 17 'topics' identified in the EDFacts documentation (in this database, each 'topic' is entered as a separate study); program data is available since 2005 at <ed.gov/about/inits/ed/edfacts>. EDFacts T3/LEP:2011-12 (ed.gov/about/inits/ed/edfacts) annually collects cross-sectional data from states to support oversight and reporting of programs for the education of limited English proficient students as contained in Title I and Title III of the Elementary and Secondary Education Act (ESEA), as amended. Title III also provides programs for students who are immigrants at the SEA and LEA levels. EDFacts T3/LEP:2011-12 data were collected using the EDFacts Submission System (ESS), a centralized portal and their submission by states is mandatory and required for benefits. Not submitting the required reports by a state constitutes a failure to comply with law and may have consequences for federal funding to the state. Key statistics produced from EDFacts T3/LEP:2011-12 are from 13 data groups: AMAO I LEP Making Progress, AMAO II LEP English Attainment, AMAO III AYP for LEP, Immigrant, LEP Enrolled, LEP Students in LEP Program, LEP English Language Proficiency Results, LEP English Language Proficiency Test, Title III Teachers, Title III LEP English Language Proficiency Results, Title III LEP English Language Proficiency Test, Title III LEP Students Served, and Title III Former LEP Students. For the purposes of this system, data groups are referred to as 'variables', as a result of the structure and format of EDFacts' data.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "ED Data Express",
                     "description": "EDFacts Title III/Limited English Proficiency 2011-12 data available through ED Data Express",
                     "downloadURL": "https://eddataexpress.ed.gov/",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "ED Data Express"
                 }
             ],
+            "identifier": "444ecc2e-3907-48e5-89a0-682f60bf7704",
             "keyword": [
                 "6c548925-1c84-490a-b972-9ef7c1ca1183",
                 "amao",
@@ -76620,39 +76602,17 @@
                 "title-iii-lep",
                 "title-iiilep"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:15"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://eddataexpress.ed.gov/faqs.cfm",
-                "https://eddataexpress.ed.gov/definitions.cfm"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Household Education Surveys Program, 2003 Adult Education for Work-Related Reasons",
-            "description": "The National Household Education Survey, 2003 Adult Education for Work-Related Seasons (AEWR-NHES:2003), is a study that is part of the National Household Education Survey (NHES) program. AEWR-NHES:2003 (https://nces.ed.gov/nhes/) is a cross-sectional survey that collects data directly from households on educational issues. This study was conducted using an address based sample of self-administered questionnaires of households. Households in 2003 were sampled. The study response rate was 64.7 percent. Key statistics produced from AEWR-NHES:2003 are participation in adult and continuing education.",
-            "modified": "2023-06-22T20:20:12.121720",
-            "accessLevel": "public",
-            "identifier": "3c02e5a2-0816-4017-bf4e-72f5095ae20c",
-            "dataQuality": true,
-            "issued": "2004-08-06",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2002/2003",
+            "modified": "2023-06-22T20:22:12.631498",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "National Center for Education Statistics (NCES)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Institute of Education Sciences (IES)",
+                "name": "Office of English Language Acquisition (OELA)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Office of the Secretary (OS)",
@@ -76665,60 +76625,63 @@
                         }
                     }
                 }
-                }
             },
+            "references": [
+                "https://eddataexpress.ed.gov/faqs.cfm",
+                "https://eddataexpress.ed.gov/definitions.cfm"
+            ],
+            "spatial": "United States",
+            "temporal": "2011/2012",
+            "title": "EDFacts Title III/Limited English Proficiency, 2011-12"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sarah Grady",
                 "hasEmail": "mailto:sarah.grady@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Household Education Survey, 2003 Adult Education for Work-Related Seasons (AEWR-NHES:2003), is a study that is part of the National Household Education Survey (NHES) program. AEWR-NHES:2003 (https://nces.ed.gov/nhes/) is a cross-sectional survey that collects data directly from households on educational issues. This study was conducted using an address based sample of self-administered questionnaires of households. Households in 2003 were sampled. The study response rate was 64.7 percent. Key statistics produced from AEWR-NHES:2003 are participation in adult and continuing education.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped CSV",
-                    "title": "aewrasc.zip",
-                    "description": "Adult Education for Work-Related Reasons public-use data",
                     "describedBy": "https://nces.ed.gov/nhes/pdf/codebook/NHES_2003_AEWR_Codebook.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/nhes/data/aewrasc.zip"
+                    "description": "Adult Education for Work-Related Reasons public-use data",
+                    "downloadURL": "https://nces.ed.gov/nhes/data/aewrasc.zip",
+                    "format": "Zipped CSV",
+                    "mediaType": "application/zip",
+                    "title": "aewrasc.zip"
                 }
             ],
+            "identifier": "3c02e5a2-0816-4017-bf4e-72f5095ae20c",
+            "issued": "2004-08-06",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "adult-education",
                 "continuing-education",
                 "education-for-work-related-reasons"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-22T20:20:12.121720",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Equity in Athletics Disclosure Act Survey, 2013",
-            "description": "The Equity in Athletics Disclosure Act Survey, 2013 (EADA 2013), is part of the Equity in Athletics Disclosure Act Survey (EADA) program (https://www2.ed.gov/finaid/prof/resources/athletics/eada.html). Data is available since 2003 at <https://ope.ed.gov/athletics/>. The Equity in Athletics Disclosure Act requires co-educational institutions of postsecondary education that participate in a Title IV, federal student financial assistance program, and have an intercollegiate athletic program, to prepare an annual report to the Department of Education on athletic participation, staffing, and revenues and expenses, by men's and women's teams. This cross-sectional data collection was administered via an online survey. In 2013, the collection's response rate was 100 percent. Key statistics from EADA 2013 were designed to make prospective students aware of a schools\u00c3\u0192\u00c6\u2019\u00c3\u201a\u00c2\u00af\u00c3\u0192\u00e2\u20ac\u0161\u00c3\u201a\u00c2\u00bf\u00c3\u0192\u00e2\u20ac\u0161\u00c3\u201a\u00c2\u00bd commitment to providing equitable athletic opportunities for its men and women students; as well, results were used in the Department's report to Congress on gender equity in intercollegiate athletics.",
-            "modified": "2023-06-22T20:17:33.610340",
-            "accessLevel": "public",
-            "identifier": "30527239-cc79-402b-99df-7812e73da8bb",
-            "dataQuality": true,
-            "issued": "2011-12-13",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2013/P1Y",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Postsecondary Education (OPE)",
+                "name": "National Center for Education Statistics (NCES)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Office of the Under Secretary (OUS)",
+                    "name": "Institute of Education Sciences (IES)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -76733,12 +76696,25 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2002/2003",
+            "title": "National Household Education Surveys Program, 2003 Adult Education for Work-Related Reasons"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:40"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Ashley Higgins",
                 "hasEmail": "mailto:ashley.higgins@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The Equity in Athletics Disclosure Act Survey, 2013 (EADA 2013), is part of the Equity in Athletics Disclosure Act Survey (EADA) program (https://www2.ed.gov/finaid/prof/resources/athletics/eada.html). Data is available since 2003 at <https://ope.ed.gov/athletics/>. The Equity in Athletics Disclosure Act requires co-educational institutions of postsecondary education that participate in a Title IV, federal student financial assistance program, and have an intercollegiate athletic program, to prepare an annual report to the Department of Education on athletic participation, staffing, and revenues and expenses, by men's and women's teams. This cross-sectional data collection was administered via an online survey. In 2013, the collection's response rate was 100 percent. Key statistics from EADA 2013 were designed to make prospective students aware of a schools\u00c3\u0192\u00c6\u2019\u00c3\u201a\u00c2\u00af\u00c3\u0192\u00e2\u20ac\u0161\u00c3\u201a\u00c2\u00bf\u00c3\u0192\u00e2\u20ac\u0161\u00c3\u201a\u00c2\u00bd commitment to providing equitable athletic opportunities for its men and women students; as well, results were used in the Department's report to Congress on gender equity in intercollegiate athletics.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -76747,6 +76723,8 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "30527239-cc79-402b-99df-7812e73da8bb",
+            "issued": "2011-12-13",
             "keyword": [
                 "athletic-participation",
                 "athletics",
@@ -76772,37 +76750,20 @@
                 "survey",
                 "team"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:40"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://www2.ed.gov/finaid/prof/resources/athletics/eada.html"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Postsecondary Student Aid Study, 1999-2000",
-            "description": "The National Postsecondary Student Aid Study, 1999-2000 (NPSAS:2000), is a study that is part of the National Postsecondary Student Aid Study (NPSAS) program; program data is available since 1989-90 at https://nces.ed.gov/pubsearch/getpubcats.asp?sid=013. NPSAS:2000 (https://nces.ed.gov/surveys/npsas/about.asp) is a cross-sectional survey that is designed to compile a comprehensive research dataset, based on student-level records, on financial aid provided by the federal government, the states, postsecondary institutions, employers, and private agencies along with student demographic and enrollment data. The study was conducted using multiple sources, including institutional records, government databases, and student interviews. NPSAS:2000 was the first to employ a web-based instrument for collection of institutional records. NPSAS:2000 contains the data on a sample of about 70,200 postsecondary students who were enrolled at any time between July 1, 1999 and June 30, 2000 in about 1,100 postsecondary institutions. The data are representative of all undergraduate and graduate students enrolled in postsecondary institutions in the 50 United States, the District of Columbia, and Puerto Rico that were eligible to participate in the federal financial aid programs in Title IV of the Higher Education Act. After adjusting for institutional nonresponse and for attendance at more than one institution, the overall weighted study response rate was 89 percent. Statistics produced from the NPSAS:2000 provide reliable national estimates of characteristics related to financial aid for postsecondary students.",
-            "modified": "2023-06-22T20:13:56.554285",
-            "accessLevel": "public",
-            "identifier": "cde33cf0-600b-4ad9-9414-e9e927d8fef7",
-            "dataQuality": true,
-            "issued": "2003-11-14",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "1999/2000",
+            "modified": "2023-06-22T20:17:33.610340",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "National Center for Education Statistics (NCES)",
+                "name": "Office of Postsecondary Education (OPE)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                    "name": "Institute of Education Sciences (IES)",
+                    "name": "Office of the Under Secretary (OUS)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -76817,22 +76778,39 @@
                     }
                 }
             },
+            "references": [
+                "https://www2.ed.gov/finaid/prof/resources/athletics/eada.html"
+            ],
+            "spatial": "United States",
+            "temporal": "2013/P1Y",
+            "title": "Equity in Athletics Disclosure Act Survey, 2013"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P4Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tracy Hunt-White",
                 "hasEmail": "mailto:tracy.hunt-white@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Postsecondary Student Aid Study, 1999-2000 (NPSAS:2000), is a study that is part of the National Postsecondary Student Aid Study (NPSAS) program; program data is available since 1989-90 at https://nces.ed.gov/pubsearch/getpubcats.asp?sid=013. NPSAS:2000 (https://nces.ed.gov/surveys/npsas/about.asp) is a cross-sectional survey that is designed to compile a comprehensive research dataset, based on student-level records, on financial aid provided by the federal government, the states, postsecondary institutions, employers, and private agencies along with student demographic and enrollment data. The study was conducted using multiple sources, including institutional records, government databases, and student interviews. NPSAS:2000 was the first to employ a web-based instrument for collection of institutional records. NPSAS:2000 contains the data on a sample of about 70,200 postsecondary students who were enrolled at any time between July 1, 1999 and June 30, 2000 in about 1,100 postsecondary institutions. The data are representative of all undergraduate and graduate students enrolled in postsecondary institutions in the 50 United States, the District of Columbia, and Puerto Rico that were eligible to participate in the federal financial aid programs in Title IV of the Higher Education Act. After adjusting for institutional nonresponse and for attendance at more than one institution, the overall weighted study response rate was 89 percent. Statistics produced from the NPSAS:2000 provide reliable national estimates of characteristics related to financial aid for postsecondary students.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "Data Explorer",
-                    "title": "PowerStats",
                     "description": "1999-2000 National Postsecondary Student Aid Study data available through PowerStats in the NCES Datalab",
                     "downloadURL": "https://nces.ed.gov/datalab/postsecondary/index.aspx",
-                    "mediaType": "text/plain"
+                    "format": "Data Explorer",
+                    "mediaType": "text/plain",
+                    "title": "PowerStats"
                 }
             ],
+            "identifier": "cde33cf0-600b-4ad9-9414-e9e927d8fef7",
+            "issued": "2003-11-14",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "cost-of-higher-education",
@@ -76841,32 +76819,14 @@
                 "postsecondary-education",
                 "student-record"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/datalab/powerstats/pdf/npsas2000gr_varname.pdf",
-                "https://nces.ed.gov/datalab/powerstats/pdf/npsas2000ug_varname.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Postsecondary Student Aid Study, 1992-93",
-            "description": "The National Postsecondary Student Aid Study, 1992-93 (NPSAS:93), is a study that is part of the National Postsecondary Student Aid Study (NPSAS) program; program data is available since 1989-90 at https://nces.ed.gov/pubsearch/getpubcats.asp?sid=013. NPSAS:93 (https://nces.ed.gov/surveys/npsas/about.asp) is a cross-sectional survey that is designed to compile a comprehensive research dataset, based on student-level records, on financial aid provided by the federal government, the states, postsecondary institutions, employers, and private agencies along with student demographic and enrollment data. The study was conducted using multiple sources, including institutional records, government databases, and student interviews. NPSAS:93 contains the data on a sample of about 66,000 eligible postsecondary students who were enrolled at any time between July 1, 1992 and June 30, 1993 in about 1,100 postsecondary institutions. The data are representative of all undergraduate and graduate students enrolled in postsecondary institutions in the 50 United States, the District of Columbia, and Puerto Rico that were eligible to participate in the federal financial aid programs in Title IV of the Higher Education Act. After adjusting for institutional nonresponse and for attendance at more than one institution, the overall weighted study response rate was 85 percent. Statistics produced from the NPSAS:93 provide reliable national estimates of characteristics related to financial aid for postsecondary students.",
-            "modified": "2023-06-22T20:11:19.226621",
-            "accessLevel": "public",
-            "identifier": "aaab5347-1807-45b1-8070-2e38d497a8e3",
-            "dataQuality": true,
-            "issued": "1995-12-04",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "1992/1993",
+            "modified": "2023-06-22T20:13:56.554285",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -76887,21 +76847,39 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/datalab/powerstats/pdf/npsas2000gr_varname.pdf",
+                "https://nces.ed.gov/datalab/powerstats/pdf/npsas2000ug_varname.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "1999/2000",
+            "title": "National Postsecondary Student Aid Study, 1999-2000"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P4Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tracy Hunt-White",
                 "hasEmail": "mailto:tracy.hunt-white@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Postsecondary Student Aid Study, 1992-93 (NPSAS:93), is a study that is part of the National Postsecondary Student Aid Study (NPSAS) program; program data is available since 1989-90 at https://nces.ed.gov/pubsearch/getpubcats.asp?sid=013. NPSAS:93 (https://nces.ed.gov/surveys/npsas/about.asp) is a cross-sectional survey that is designed to compile a comprehensive research dataset, based on student-level records, on financial aid provided by the federal government, the states, postsecondary institutions, employers, and private agencies along with student demographic and enrollment data. The study was conducted using multiple sources, including institutional records, government databases, and student interviews. NPSAS:93 contains the data on a sample of about 66,000 eligible postsecondary students who were enrolled at any time between July 1, 1992 and June 30, 1993 in about 1,100 postsecondary institutions. The data are representative of all undergraduate and graduate students enrolled in postsecondary institutions in the 50 United States, the District of Columbia, and Puerto Rico that were eligible to participate in the federal financial aid programs in Title IV of the Higher Education Act. After adjusting for institutional nonresponse and for attendance at more than one institution, the overall weighted study response rate was 85 percent. Statistics produced from the NPSAS:93 provide reliable national estimates of characteristics related to financial aid for postsecondary students.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "CD-ROM: National Postsecondary Student Aid Study: 1992-93 Data Analysis System Public Use File",
                     "description": "CD-ROM containing 1992-93 National Postsecondary Student Aid Study data in a data analysis system",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=95365",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "CD-ROM: National Postsecondary Student Aid Study: 1992-93 Data Analysis System Public Use File"
                 }
             ],
+            "identifier": "aaab5347-1807-45b1-8070-2e38d497a8e3",
+            "issued": "1995-12-04",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "cost-of-higher-education",
@@ -76910,32 +76888,14 @@
                 "postsecondary-education",
                 "student-record"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2000193"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Postsecondary Student Aid Study, 2003-04",
-            "description": "The National Postsecondary Student Aid Study, 2003-04 (NPSAS:04), is a study that is part of the National Postsecondary Student Aid Study (NPSAS) program. NPSAS:04 (https://nces.ed.gov/surveys/npsas/about.asp) is a cross-sectional survey that is designed to compile a comprehensive research dataset, based on student-level records, on financial aid provided by the federal government, the states, postsecondary institutions, employers, and private agencies along with student demographic and enrollment data. The study was conducted using multiple sources, including institutional records, government databases, and student interviews. NPSAS:04 contains the data on a sample of about 109,210 postsecondary students who were enrolled at any time between July 1, 2003 and June 30, 2004 in about 1,670 postsecondary institutions. The data are representative of all undergraduate and graduate students enrolled in postsecondary institutions in the 50 United States, the District of Columbia, and Puerto Rico that were eligible to participate in the federal financial aid programs in Title IV of the Higher Education Act. Statistics produced from the NPSAS:04 provide reliable national estimates of characteristics related to financial aid for postsecondary students.",
-            "modified": "2023-06-22T20:08:55.676846",
-            "accessLevel": "public",
-            "identifier": "c3833f52-9d38-45d7-8149-96abb34a6ce6",
-            "dataQuality": true,
-            "issued": "2005-02-11",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2003/2004",
+            "modified": "2023-06-22T20:11:19.226621",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -76956,34 +76916,51 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2000193"
+            ],
+            "spatial": "United States",
+            "temporal": "1992/1993",
+            "title": "National Postsecondary Student Aid Study, 1992-93"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P4Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tracy Hunt-White",
                 "hasEmail": "mailto:tracy.hunt-white@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Postsecondary Student Aid Study, 2003-04 (NPSAS:04), is a study that is part of the National Postsecondary Student Aid Study (NPSAS) program. NPSAS:04 (https://nces.ed.gov/surveys/npsas/about.asp) is a cross-sectional survey that is designed to compile a comprehensive research dataset, based on student-level records, on financial aid provided by the federal government, the states, postsecondary institutions, employers, and private agencies along with student demographic and enrollment data. The study was conducted using multiple sources, including institutional records, government databases, and student interviews. NPSAS:04 contains the data on a sample of about 109,210 postsecondary students who were enrolled at any time between July 1, 2003 and June 30, 2004 in about 1,670 postsecondary institutions. The data are representative of all undergraduate and graduate students enrolled in postsecondary institutions in the 50 United States, the District of Columbia, and Puerto Rico that were eligible to participate in the federal financial aid programs in Title IV of the Higher Education Act. Statistics produced from the NPSAS:04 provide reliable national estimates of characteristics related to financial aid for postsecondary students.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Datalab for Postsecondary Education",
                     "downloadURL": "https://nces.ed.gov/datalab/postsecondary/index.aspx",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Datalab for Postsecondary Education"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "2003-04 National Postsecondary Student Aid Study (NPSAS:04): Graduate Data Analysis System",
                     "description": "Graduate data for the 2003-04 National Postsecondary Student Aid Study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2005165",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "2003-04 National Postsecondary Student Aid Study (NPSAS:04): Graduate Data Analysis System"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "2003-04 National Postsecondary Student Aid Study (NPSAS:04): Undergraduate Data Analysis System",
                     "description": "Undergraduate data for the 2003-04 National Postsecondary Student Aid Study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2005164",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "2003-04 National Postsecondary Student Aid Study (NPSAS:04): Undergraduate Data Analysis System"
                 }
             ],
+            "identifier": "c3833f52-9d38-45d7-8149-96abb34a6ce6",
+            "issued": "2005-02-11",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "cost-of-higher-education",
@@ -76992,29 +76969,14 @@
                 "postsecondary-education",
                 "student-record"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-22T20:08:55.676846",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Postsecondary Student Aid Study, 2011-12",
-            "description": "The National Postsecondary Student Aid Study, 2011-12 (NPSAS:12), is a study that is part of the National Postsecondary Student Aid Study (NPSAS) program. NPSAS:12 (https://nces.ed.gov/surveys/npsas/about.asp) is a cross-sectional survey that is designed to compile a comprehensive research dataset, based on student-level records, on financial aid provided by the federal government, the states, postsecondary institutions, employers, and private agencies, along with student demographic and enrollment data. The study was conducted using multiple sources, including institutional records, government databases, and student interviews. To be eligible to participate in the study,  students have to be enrolled in a postsecondary institution. The data are representative of all undergraduate and graduate students enrolled in postsecondary institutions in the 50 United States and the District of Columbia that were eligible to participate in the federal financial aid programs in Title IV of the Higher Education Act. Statistics produced from NPSAS:12 provide reliable national estimates of characteristics related to financial aid for postsecondary students.",
-            "modified": "2023-06-22T20:08:19.239772",
-            "accessLevel": "public",
-            "identifier": "073f0d76-5edd-4494-98da-c32205de2a42",
-            "dataQuality": true,
-            "issued": "2013-08-20",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2011/2012",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -77035,34 +76997,49 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2003/2004",
+            "title": "National Postsecondary Student Aid Study, 2003-04"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P4Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tracy Hunt-White",
                 "hasEmail": "mailto:tracy.hunt-white@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The National Postsecondary Student Aid Study, 2011-12 (NPSAS:12), is a study that is part of the National Postsecondary Student Aid Study (NPSAS) program. NPSAS:12 (https://nces.ed.gov/surveys/npsas/about.asp) is a cross-sectional survey that is designed to compile a comprehensive research dataset, based on student-level records, on financial aid provided by the federal government, the states, postsecondary institutions, employers, and private agencies, along with student demographic and enrollment data. The study was conducted using multiple sources, including institutional records, government databases, and student interviews. To be eligible to participate in the study,  students have to be enrolled in a postsecondary institution. The data are representative of all undergraduate and graduate students enrolled in postsecondary institutions in the 50 United States and the District of Columbia that were eligible to participate in the federal financial aid programs in Title IV of the Higher Education Act. Statistics produced from NPSAS:12 provide reliable national estimates of characteristics related to financial aid for postsecondary students.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Datalab for Postsecondary Education",
                     "downloadURL": "https://nces.ed.gov/datalab/postsecondary/index.aspx",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Datalab for Postsecondary Education"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "2011-12 National Postsecondary Student Aid Study (NPSAS:12) Restricted-Use Data File",
                     "description": "Restricted-use data file for the 2011-12 National Postsecondary Student Aid Study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2013181",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "2011-12 National Postsecondary Student Aid Study (NPSAS:12) Restricted-Use Data File"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "2011-12 National Postsecondary Student Aid Study (NPSAS:12) Restricted-Use Data File",
                     "description": "Revised restricted-use data file for the 2011-12 National Postsecondary Student Aid Study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2013181rev",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "2011-12 National Postsecondary Student Aid Study (NPSAS:12) Restricted-Use Data File"
                 }
             ],
+            "identifier": "073f0d76-5edd-4494-98da-c32205de2a42",
+            "issued": "2013-08-20",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "cost-of-higher-education",
@@ -77071,34 +77048,14 @@
                 "postsecondary-education",
                 "student-record"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/pubs2014/2014182.pdf",
-                "https://nces.ed.gov/pubs2014/2014182_1.pdf",
-                "https://nces.ed.gov/pubs2014/2014182_2.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Educational Technology and Teacher Education Programs for Initial Licensure, 2006",
-            "description": "Educational Technology and Teacher Education Programs for Initial Licensure, 2006 (PEQIS 15), is a study that is part of the Postsecondary Education Quick Information System (PEQIS) program; program data is available since 1997 at <https://nces.ed.gov/surveys/peqis/>. PEQIS 15 (https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2008040) is a cross-sectional survey that collected information about teacher education programs for initial licensure of pre-kindergarten through 12th grade (PK-12) teachers. Title IV four-year degree-granting postsecondary institutions located in the 50 United States and the District of Columbia were sampled. The study was conducted using questionnaires for all eligible four-year institutions in the United States as identified from the 2004 Integrated Postsecondary Education Data System (IPEDS) \"Institutional Characteristics\" survey (IPEDS-IC). The study's response rate was 95 percent. Key statistics produced from PEQIS 15 include information on the educational technology-related topics and practices taught within teacher education programs for initial licensure, the extent to which teacher candidates are taught to use technology tools for a variety of purposes, the extent to which teacher candidates are able to practice what they learn during their field experiences (and the extent to which this opportunity is impeded by a variety of barriers within classrooms), and the perceived program outcomes for graduates of programs for initial licensure.",
-            "modified": "2023-06-22T20:05:05.526117",
-            "accessLevel": "public",
-            "identifier": "ff05e7a1-5efd-45f3-8143-c7a12f585343",
-            "dataQuality": true,
-            "issued": "2008-04-09",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2005/2006",
+            "modified": "2023-06-22T20:08:19.239772",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -77119,20 +77076,40 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/pubs2014/2014182.pdf",
+                "https://nces.ed.gov/pubs2014/2014182_1.pdf",
+                "https://nces.ed.gov/pubs2014/2014182_2.pdf"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2011/2012",
+            "title": "National Postsecondary Student Aid Study, 2011-12"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "Educational Technology and Teacher Education Programs for Initial Licensure, 2006 (PEQIS 15), is a study that is part of the Postsecondary Education Quick Information System (PEQIS) program; program data is available since 1997 at <https://nces.ed.gov/surveys/peqis/>. PEQIS 15 (https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2008040) is a cross-sectional survey that collected information about teacher education programs for initial licensure of pre-kindergarten through 12th grade (PK-12) teachers. Title IV four-year degree-granting postsecondary institutions located in the 50 United States and the District of Columbia were sampled. The study was conducted using questionnaires for all eligible four-year institutions in the United States as identified from the 2004 Integrated Postsecondary Education Data System (IPEDS) \"Institutional Characteristics\" survey (IPEDS-IC). The study's response rate was 95 percent. Key statistics produced from PEQIS 15 include information on the educational technology-related topics and practices taught within teacher education programs for initial licensure, the extent to which teacher candidates are taught to use technology tools for a variety of purposes, the extent to which teacher candidates are able to practice what they learn during their field experiences (and the extent to which this opportunity is impeded by a variety of barriers within classrooms), and the perceived program outcomes for graduates of programs for initial licensure.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Public-Use Data Files and Documentation: Educational Technology in Teacher Education Programs for Initial Licensure",
                     "description": "Educational Technology and Teacher Education Programs for Initial Licensure, 2006 public-use data.",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2008013",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Public-Use Data Files and Documentation: Educational Technology in Teacher Education Programs for Initial Licensure"
                 }
             ],
+            "identifier": "ff05e7a1-5efd-45f3-8143-c7a12f585343",
+            "issued": "2008-04-09",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "educational-technology",
@@ -77142,29 +77119,14 @@
                 "teacher-education-programs",
                 "technology"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-22T20:05:05.526117",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Dual Enrollment Programs and Courses for High School Students, 2002-03",
-            "description": "Dual Enrollment Programs and Courses for High School Students, 2002-03 (PEQIS 14), is a study that is part of the Postsecondary Education Quick Information System (PEQIS) program; program data is available since 1997 at <https://nces.ed.gov/surveys/peqis/>. PEQIS 14 (https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2009045) is a cross-sectional survey that collected information on the topic of dual enrollment of high school students at postsecondary institutions. 1,600 Title IV degree-granting postsecondary institutions in the 50 United States and the District of Columbia were sampled. The study was conducted using online or paper surveys. The overall response rates were 92 percent weighted and 91 percent unweighted. Key statistics produced from PEQIS 14 were information on the prevalence of college course-taking by high school students at their institutions during the 2002-03 12-month academic year, both within and outside of dual enrollment programs. Among institutions with dual enrollment programs, additional information was obtained on the characteristics of programs, including course location and type of instructors, program and course curriculum, academic eligibility requirements, and funding.",
-            "modified": "2023-06-22T20:03:30.906453",
-            "accessLevel": "public",
-            "identifier": "b1b22578-f4b7-4be2-80d4-2f5d63d65ba0",
-            "dataQuality": true,
-            "issued": "2005-04-06",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2002/2003",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -77185,29 +77147,44 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2005/2006",
+            "title": "Educational Technology and Teacher Education Programs for Initial Licensure, 2006"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "Dual Enrollment Programs and Courses for High School Students, 2002-03 (PEQIS 14), is a study that is part of the Postsecondary Education Quick Information System (PEQIS) program; program data is available since 1997 at <https://nces.ed.gov/surveys/peqis/>. PEQIS 14 (https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2009045) is a cross-sectional survey that collected information on the topic of dual enrollment of high school students at postsecondary institutions. 1,600 Title IV degree-granting postsecondary institutions in the 50 United States and the District of Columbia were sampled. The study was conducted using online or paper surveys. The overall response rates were 92 percent weighted and 91 percent unweighted. Key statistics produced from PEQIS 14 were information on the prevalence of college course-taking by high school students at their institutions during the 2002-03 12-month academic year, both within and outside of dual enrollment programs. Among institutions with dual enrollment programs, additional information was obtained on the characteristics of programs, including course location and type of instructors, program and course curriculum, academic eligibility requirements, and funding.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "peqis14dat.zip",
                     "description": "Dual Enrollment Programs and Courses for High School Students (PEQIS 14): Public Use Data Files and Documentation (NCES 2009-045)",
-                    "downloadURL": "https://nces.ed.gov/surveys/peqis/download/data/peqis14dat.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/peqis/download/data/peqis14dat.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "peqis14dat.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS7BDAT",
-                    "title": "peqis14sas.zip",
                     "description": "Dual Enrollment Programs and Courses for High School Students (PEQIS 14): Public Use Data Files and Documentation (NCES 2009-045)",
-                    "downloadURL": "https://nces.ed.gov/surveys/peqis/download/data/peqis14sas.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/peqis/download/data/peqis14sas.zip",
+                    "format": "Zipped SAS7BDAT",
+                    "mediaType": "application/zip",
+                    "title": "peqis14sas.zip"
                 }
             ],
+            "identifier": "b1b22578-f4b7-4be2-80d4-2f5d63d65ba0",
+            "issued": "2005-04-06",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "college-credit",
@@ -77220,32 +77197,14 @@
                 "secondary-education",
                 "students"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/surveys/peqis/download/data/peqis14doc.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Online and Distance Education at Postsecondary Institutions, 2006-07",
-            "description": "Online and Distance Education at Postsecondary Institutions, 2006-07 (PEQIS 16), is a study that is part of the Postsecondary Education Quick Information System (PEQIS) program; program data is available since 1997 at <https://nces.ed.gov/surveys/peqis/>. PEQIS 16 (https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2009044) is a survey that collects data on the prevalence and delivery of distance education courses in the 2006-07 12-month academic year, including the number of courses and enrollment for online courses, hybrid/blended online courses, and all other distance education courses. The survey also collects information about numbers of degree or certificate programs designed to be completed entirely through distance education and the technologies used for the instructional delivery of credit-granting distance education courses. The study was conducted using paper and web surveys. The weighted response rate was 87 percent.  Postsecondary institutions were sample for this study. Key statistics produced from PEQIS 16 relate to information on the prevalence, types, delivery, policies, and acquisition or development of distance education courses and programs.",
-            "modified": "2023-06-22T19:59:15.921615",
-            "accessLevel": "public",
-            "identifier": "3127fe7a-cfbc-4c45-b6e2-f4c0ee62cb2b",
-            "dataQuality": true,
-            "issued": "2009-09-24",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2006/2007",
+            "modified": "2023-06-22T20:03:30.906453",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -77266,19 +77225,37 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/surveys/peqis/download/data/peqis14doc.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2002/2003",
+            "title": "Dual Enrollment Programs and Courses for High School Students, 2002-03"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "Online and Distance Education at Postsecondary Institutions, 2006-07 (PEQIS 16), is a study that is part of the Postsecondary Education Quick Information System (PEQIS) program; program data is available since 1997 at <https://nces.ed.gov/surveys/peqis/>. PEQIS 16 (https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2009044) is a survey that collects data on the prevalence and delivery of distance education courses in the 2006-07 12-month academic year, including the number of courses and enrollment for online courses, hybrid/blended online courses, and all other distance education courses. The survey also collects information about numbers of degree or certificate programs designed to be completed entirely through distance education and the technologies used for the instructional delivery of credit-granting distance education courses. The study was conducted using paper and web surveys. The weighted response rate was 87 percent.  Postsecondary institutions were sample for this study. Key statistics produced from PEQIS 16 relate to information on the prevalence, types, delivery, policies, and acquisition or development of distance education courses and programs.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Public-Use Data Files and Documentation (PEQIS 16): Distance Education at Postsecondary Institutions, 2006-07",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2009074",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Public-Use Data Files and Documentation (PEQIS 16): Distance Education at Postsecondary Institutions, 2006-07"
                 }
             ],
+            "identifier": "3127fe7a-cfbc-4c45-b6e2-f4c0ee62cb2b",
+            "issued": "2009-09-24",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "acquisition-or-development-of-distance-or-education",
@@ -77291,29 +77268,14 @@
                 "prevalence-of-distance-education",
                 "types-of-distance-education"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-22T19:59:15.921615",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Dual Enrollment Programs and Courses of High School Students, 2010-11",
-            "description": "Dual Enrollment Programs and Courses for High School Students, 2010-11 (PEQIS 18), is part of the Postsecondary Education Quick Information System (PEQIS); program data is available since 1997 at <https://nces.ed.gov/surveys/peqis/>. The study was conducted using paper surveys, non-computer-assisted telephone instruments, and email. Postsecondary institution personnel were sampled for this survey. The study's weighted response rate was 94 percent. Key statistics produced from PEQIS 18 are on the prevalence and characteristics of dual enrollment programs at postsecondary institutions in the United States.",
-            "modified": "2023-06-22T19:58:07.050520",
-            "accessLevel": "public",
-            "identifier": "f3b2ef23-dec1-4d0d-b469-e270d95aaefb",
-            "dataQuality": true,
-            "issued": "2013-03-05",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2010/2011",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -77334,29 +77296,44 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2006/2007",
+            "title": "Online and Distance Education at Postsecondary Institutions, 2006-07"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "Dual Enrollment Programs and Courses for High School Students, 2010-11 (PEQIS 18), is part of the Postsecondary Education Quick Information System (PEQIS); program data is available since 1997 at <https://nces.ed.gov/surveys/peqis/>. The study was conducted using paper surveys, non-computer-assisted telephone instruments, and email. Postsecondary institution personnel were sampled for this survey. The study's weighted response rate was 94 percent. Key statistics produced from PEQIS 18 are on the prevalence and characteristics of dual enrollment programs at postsecondary institutions in the United States.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "pq18dat.zip",
                     "description": "Public-Use Data Files and Documentation (PEQIS 18): Dual Enrollment Programs and Courses for High School Students, 2010-11 (NCES 2013-006)",
-                    "downloadURL": "https://nces.ed.gov/surveys/peqis/download/data/pq18dat.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/peqis/download/data/pq18dat.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "pq18dat.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS7BDAT",
-                    "title": "pq18sas.zip",
                     "description": "Public-Use Data Files and Documentation (PEQIS 18): Dual Enrollment Programs and Courses for High School Students, 2010-11 (NCES 2013-006)",
-                    "downloadURL": "https://nces.ed.gov/surveys/peqis/download/data/pq18sas.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/peqis/download/data/pq18sas.zip",
+                    "format": "Zipped SAS7BDAT",
+                    "mediaType": "application/zip",
+                    "title": "pq18sas.zip"
                 }
             ],
+            "identifier": "f3b2ef23-dec1-4d0d-b469-e270d95aaefb",
+            "issued": "2013-03-05",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "dual-credit",
@@ -77370,32 +77347,14 @@
                 "prevalence-and-enrollment-of-dual-credit-and-exam-based-courses-in-public-high-schools",
                 "prevalence-of-college-course-taking-by-high-school-students"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
-            "programCode": [
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-22T19:58:07.050520",
+            "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://nces.ed.gov/surveys/peqis/download/data/pq18doc.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Students with Disabilities at Postsecondary Education Institutions, 2008-09",
-            "description": "Students with Disabilities at Postsecondary Education Institutions, 2008-09 (PEQIS 17), is a study that is part of the Postsecondary Education Quick Information System (PEQIS) program; program data is available since 1997 at <https://nces.ed.gov/surveys/peqis/>. PEQIS 17 (https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2011018) is a survey that provides information about students with disabilities at postsecondary institutions and the services, accommodations and institutional accessibility provided to these students. The study was conducted using paper surveys and non-computer-assisted telephone instruments. Postsecondary institutions were sampled  for this study. The study's response rate was 91 percent. Key statistics produced from PEQIS 17 are national data about students with disabilities, the services and accommodations provided to these students, how institutions keep track of students with disabilities, institutional policies regarding disabled students, and various aspects of institutional accessibility.",
-            "modified": "2023-06-22T19:52:33.159160",
-            "accessLevel": "public",
-            "identifier": "62729d94-3732-481f-ab5c-99719860c8cf",
-            "dataQuality": true,
-            "issued": "2011-06-23",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2008/2009",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -77416,30 +77375,48 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/surveys/peqis/download/data/pq18doc.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2010/2011",
+            "title": "Dual Enrollment Programs and Courses of High School Students, 2010-11"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "Students with Disabilities at Postsecondary Education Institutions, 2008-09 (PEQIS 17), is a study that is part of the Postsecondary Education Quick Information System (PEQIS) program; program data is available since 1997 at <https://nces.ed.gov/surveys/peqis/>. PEQIS 17 (https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2011018) is a survey that provides information about students with disabilities at postsecondary institutions and the services, accommodations and institutional accessibility provided to these students. The study was conducted using paper surveys and non-computer-assisted telephone instruments. Postsecondary institutions were sampled  for this study. The study's response rate was 91 percent. Key statistics produced from PEQIS 17 are national data about students with disabilities, the services and accommodations provided to these students, how institutions keep track of students with disabilities, institutional policies regarding disabled students, and various aspects of institutional accessibility.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped DAT",
-                    "title": "peqis17dat.zip",
                     "description": "Students with Disabilities at Postsecondary Education Institutions, 2008-09 data in a zipped DAT file",
-                    "downloadURL": "https://nces.ed.gov/surveys/peqis/download/data/peqis17dat.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/peqis/download/data/peqis17dat.zip",
+                    "format": "Zipped DAT",
+                    "mediaType": "application/zip",
+                    "title": "peqis17dat.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS",
-                    "title": "peqis17sas.zip",
                     "description": "Students with Disabilities at Postsecondary Education Institutions, 2008-09 data in a zipped SAS file",
-                    "downloadURL": "https://nces.ed.gov/surveys/peqis/download/data/peqis17sas.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/peqis/download/data/peqis17sas.zip",
+                    "format": "Zipped SAS",
+                    "mediaType": "application/zip",
+                    "title": "peqis17sas.zip"
                 }
             ],
+            "identifier": "62729d94-3732-481f-ab5c-99719860c8cf",
+            "issued": "2011-06-23",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "disabilities",
@@ -77454,32 +77431,14 @@
                 "teacher-training",
                 "technology-in-education"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/surveys/peqis/download/data/peqis17doc.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Services and Support Programs for Military Service Members and Veterans, 2012-13",
-            "description": "Services and Support Programs for Military Service Members and Veterans, 2012-13 (PEQIS 19), is a study that is part of the Postsecondary Education Quick Information System (PEQIS) program; program data is available since 1997-98 at <https://nces.ed.gov/pubsearch/getpubcats.asp?sid=016>. PEQIS 19 (https://nces.ed.gov/peqis/) is a cross-sectional survey that collected information on the services and support programs available to students who are military service members and veterans at the institution. The study was conducted using self-administered paper-and-pencil questionnaires of a person at the postsecondary institution that is familiar with the institution programs for military service members and veterans. Key statistics produced from PEQIS 19 were services and support programs for military members and veterans.",
-            "modified": "2023-06-22T19:48:59.055073",
-            "accessLevel": "public",
-            "identifier": "bda844a3-68d2-4d20-b59e-616a7b58ccfc",
-            "dataQuality": true,
-            "issued": "2014-03-25",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2012/2013",
+            "modified": "2023-06-22T19:52:33.159160",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -77500,29 +77459,47 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/surveys/peqis/download/data/peqis17doc.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2008/2009",
+            "title": "Students with Disabilities at Postsecondary Education Institutions, 2008-09"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Ralph",
                 "hasEmail": "mailto:john.ralph@ed.gov"
             },
+            "dataQuality": true,
+            "description": "Services and Support Programs for Military Service Members and Veterans, 2012-13 (PEQIS 19), is a study that is part of the Postsecondary Education Quick Information System (PEQIS) program; program data is available since 1997-98 at <https://nces.ed.gov/pubsearch/getpubcats.asp?sid=016>. PEQIS 19 (https://nces.ed.gov/peqis/) is a cross-sectional survey that collected information on the services and support programs available to students who are military service members and veterans at the institution. The study was conducted using self-administered paper-and-pencil questionnaires of a person at the postsecondary institution that is familiar with the institution programs for military service members and veterans. Key statistics produced from PEQIS 19 were services and support programs for military members and veterans.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped CSV",
-                    "title": "pq19data.zip",
                     "description": "Public-use PEQIS 19 data as a CSV file",
-                    "downloadURL": "https://nces.ed.gov/surveys/peqis/download/data/pq19data.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/peqis/download/data/pq19data.zip",
+                    "format": "Zipped CSV",
+                    "mediaType": "application/zip",
+                    "title": "pq19data.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS7BDAT",
-                    "title": "pq19sas.zip",
                     "description": "Public-use PEQIS 19 data as a SAS binary file",
-                    "downloadURL": "https://nces.ed.gov/surveys/peqis/download/data/pq19sas.zip"
+                    "downloadURL": "https://nces.ed.gov/surveys/peqis/download/data/pq19sas.zip",
+                    "format": "Zipped SAS7BDAT",
+                    "mediaType": "application/zip",
+                    "title": "pq19sas.zip"
                 }
             ],
+            "identifier": "bda844a3-68d2-4d20-b59e-616a7b58ccfc",
+            "issued": "2014-03-25",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "academic-advising",
@@ -77537,31 +77514,14 @@
                 "tutoring",
                 "veterans"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/surveys/peqis/download/data/pq19doc.zip"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Private School Universe Survey, 1991-92",
-            "description": "The 1991-92 Private School Universe Survey (PSS 1991-92) is a study that is part of the Private School Universe program; program data is available since 1989-1990 at <https://nces.ed.gov/surveys/pss/pssdata.asp>. PSS 1991-92 (https://nces.ed.gov/surveys/pss/) is a cross-sectional survey that collects data on private elementary and secondary schools, including religious orientation, level of school, length of school year, length of school day, total enrollment (K-12), race/ethnicity of students, number of high school graduates, number of teachers employed, program emphasis, and existence and type of kindergarten program. The study was conducted using mail questionnaires and telephone follow-up of all private schools in the United States. The PSS includes both schools with a religious orientation (e.g., Catholic, Lutheran, or Jewish) and nonsectarian schools with programs ranging from regular to special emphasis and special education. Key statistics produced from PSS 1991-92 are on the number of religiously affiliated schools, the number of private high school graduates, and the number of private school students and teachers.",
-            "modified": "2023-06-22T19:46:55.062187",
-            "accessLevel": "public",
-            "identifier": "29a6f655-c5f5-4f7e-ac27-d584ebec87c4",
-            "dataQuality": true,
-            "issued": "2007-01-31",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "1991/1992",
+            "modified": "2023-06-22T19:48:59.055073",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -77582,44 +77542,62 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/surveys/peqis/download/data/pq19doc.zip"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2012/2013",
+            "title": "Services and Support Programs for Military Service Members and Veterans, 2012-13"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P2Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Broughman",
                 "hasEmail": "mailto:stephen.broughman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The 1991-92 Private School Universe Survey (PSS 1991-92) is a study that is part of the Private School Universe program; program data is available since 1989-1990 at <https://nces.ed.gov/surveys/pss/pssdata.asp>. PSS 1991-92 (https://nces.ed.gov/surveys/pss/) is a cross-sectional survey that collects data on private elementary and secondary schools, including religious orientation, level of school, length of school year, length of school day, total enrollment (K-12), race/ethnicity of students, number of high school graduates, number of teachers employed, program emphasis, and existence and type of kindergarten program. The study was conducted using mail questionnaires and telephone follow-up of all private schools in the United States. The PSS includes both schools with a religious orientation (e.g., Catholic, Lutheran, or Jewish) and nonsectarian schools with programs ranging from regular to special emphasis and special education. Key statistics produced from PSS 1991-92 are on the number of religiously affiliated schools, the number of private high school graduates, and the number of private school students and teachers.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped TSV",
-                    "title": "TXT_PSS9192.zip",
-                    "description": "1991-92 Private School Universe Survey data as a zipped TSV file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_9192.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/TXT_PSS9192.zip"
+                    "description": "1991-92 Private School Universe Survey data as a zipped TSV file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/TXT_PSS9192.zip",
+                    "format": "Zipped TSV",
+                    "mediaType": "application/zip",
+                    "title": "TXT_PSS9192.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS7BDAT",
-                    "title": "PSS9192_SAS7BDAT.zip",
-                    "description": "1991-92 Private School Universe Survey data as a zipped SAS 7-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_9192.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/PSS9192_SAS7BDAT.zip"
+                    "description": "1991-92 Private School Universe Survey data as a zipped SAS 7-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/PSS9192_SAS7BDAT.zip",
+                    "format": "Zipped SAS7BDAT",
+                    "mediaType": "application/zip",
+                    "title": "PSS9192_SAS7BDAT.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAV",
-                    "title": "SAV_PSS9192.zip",
-                    "description": "1991-92 Private School Universe Survey data as a zipped SPSS-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_9192.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/SAV_PSS9192.zip"
+                    "description": "1991-92 Private School Universe Survey data as a zipped SPSS-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/SAV_PSS9192.zip",
+                    "format": "Zipped SAV",
+                    "mediaType": "application/zip",
+                    "title": "SAV_PSS9192.zip"
                 }
             ],
+            "identifier": "29a6f655-c5f5-4f7e-ac27-d584ebec87c4",
+            "issued": "2007-01-31",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "church-related-schools",
@@ -77628,33 +77606,14 @@
                 "private-school-graduates",
                 "private-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/pubs94/94350.pdf",
-                "https://nces.ed.gov/surveys/pss/zip/LAYOUT_9192.zip",
-                "https://nces.ed.gov/surveys/pss/pdf/quest_9192.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Private School Universe Survey, 1989-90",
-            "description": "The 1989-90 Private School Universe Survey (PSS 1989-90) is a study that is part of the Private School Universe program; program data is available since 1989-1990 at <https://nces.ed.gov/surveys/pss/pssdata.asp>. PSS 1989-90 (https://nces.ed.gov/surveys/pss/) is a cross-sectional survey that collects data on private elementary and secondary schools, including religious orientation, level of school, length of school year, length of school day, total enrollment (K-12), race/ethnicity of students, number of high school graduates, number of teachers employed, program emphasis, and existence and type of kindergarten program. The study was conducted using mail questionnaires and telephone follow-up of all private schools in the United States. The PSS includes both schools with a religious orientation (e.g., Catholic, Lutheran, or Jewish) and nonsectarian schools with programs ranging from regular to special emphasis and special education. Key statistics produced from PSS 1989-90 are on the number of religiously affiliated schools, the number of private high school graduates, and the number of private school students and teachers.",
-            "modified": "2023-06-22T19:24:28.381888",
-            "accessLevel": "public",
-            "identifier": "9097c6e7-25d3-48d7-9744-8582bb9266f8",
-            "dataQuality": true,
-            "issued": "2007-02-12",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "1989/1990",
+            "modified": "2023-06-22T19:46:55.062187",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -77675,44 +77634,63 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/pubs94/94350.pdf",
+                "https://nces.ed.gov/surveys/pss/zip/LAYOUT_9192.zip",
+                "https://nces.ed.gov/surveys/pss/pdf/quest_9192.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "1991/1992",
+            "title": "Private School Universe Survey, 1991-92"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P2Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Broughman",
                 "hasEmail": "mailto:stephen.broughman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The 1989-90 Private School Universe Survey (PSS 1989-90) is a study that is part of the Private School Universe program; program data is available since 1989-1990 at <https://nces.ed.gov/surveys/pss/pssdata.asp>. PSS 1989-90 (https://nces.ed.gov/surveys/pss/) is a cross-sectional survey that collects data on private elementary and secondary schools, including religious orientation, level of school, length of school year, length of school day, total enrollment (K-12), race/ethnicity of students, number of high school graduates, number of teachers employed, program emphasis, and existence and type of kindergarten program. The study was conducted using mail questionnaires and telephone follow-up of all private schools in the United States. The PSS includes both schools with a religious orientation (e.g., Catholic, Lutheran, or Jewish) and nonsectarian schools with programs ranging from regular to special emphasis and special education. Key statistics produced from PSS 1989-90 are on the number of religiously affiliated schools, the number of private high school graduates, and the number of private school students and teachers.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped TSV",
-                    "title": "TXT_PSS8990.zip",
-                    "description": "1989-90 Private School Universe Survey data as a zipped TSV file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_8990.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/TXT_PSS8990.zip"
+                    "description": "1989-90 Private School Universe Survey data as a zipped TSV file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/TXT_PSS8990.zip",
+                    "format": "Zipped TSV",
+                    "mediaType": "application/zip",
+                    "title": "TXT_PSS8990.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS7BDAT",
-                    "title": "PSS8990_SAS7BDAT.zip",
-                    "description": "1989-90 Private School Universe Survey data as a zipped SAS 7-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_8990.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/PSS8990_SAS7BDAT.zip"
+                    "description": "1989-90 Private School Universe Survey data as a zipped SAS 7-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/PSS8990_SAS7BDAT.zip",
+                    "format": "Zipped SAS7BDAT",
+                    "mediaType": "application/zip",
+                    "title": "PSS8990_SAS7BDAT.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAV",
-                    "title": "SAV_PSS8990.zip",
-                    "description": "1989-90 Private School Universe Survey data as a zipped SPSS-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_8990.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/SAV_PSS8990.zip"
+                    "description": "1989-90 Private School Universe Survey data as a zipped SPSS-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/SAV_PSS8990.zip",
+                    "format": "Zipped SAV",
+                    "mediaType": "application/zip",
+                    "title": "SAV_PSS8990.zip"
                 }
             ],
+            "identifier": "9097c6e7-25d3-48d7-9744-8582bb9266f8",
+            "issued": "2007-02-12",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "church-related-schools",
@@ -77721,54 +77699,66 @@
                 "private-school-graduates",
                 "private-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/pubs93/93122.pdf",
-                "https://nces.ed.gov/surveys/pss/zip/LAYOUT_8990.zip",
-                "https://nces.ed.gov/surveys/pss/pdf/quest_8990.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "School Improvement 2010 Grants",
-            "description": "Since President Obama took office, Congress has appropriated more than $4 billion to help turn around the nation's lowest-performing schools. States were awarded nearly $3.5 billion in School Improvement Grant funds in 2010 to turn around their persistently lowest achieving schools. School districts then applied to state for the funds this spring. When school districts applied, they were required to indicate that they would implement one of the following four models in their persistently lowest achieving schools: Turnaround Model: Replace the principal, screen existing school staff, and rehire no more than half the teachers; adopt a new governance structure; and improve the school through curriculum reform, professional development, extending learning time, and other strategies. Restart Model: Convert a school or close it and re-open it as a charter school or under an education management organization. School Closure: Close the school and send the students to higher-achieving schools in the district. Transformation Model: Replace the principal and improve the school through comprehensive curriculum reform, professional development, extending learning time, and other strategies.",
-            "modified": "2023-06-22T19:11:32.134037",
-            "accessLevel": "public",
-            "identifier": "e51595bd-5692-4e89-8ae0-f54bc9d487a9",
-            "dataQuality": true,
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2010/P1Y",
+            "modified": "2023-06-22T19:24:28.381888",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for Education Statistics (NCES)",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Institute of Education Sciences (IES)",
+                    "subOrganizationOf": {
+                        "@type": "org:Organization",
+                        "name": "Office of the Secretary (OS)",
+                        "subOrganizationOf": {
                             "@type": "org:Organization",
                             "name": "U.S. Department of Education",
                             "subOrganizationOf": {
                                 "@type": "org:Organization",
                                 "name": "U.S. Government"
                             }
+                        }
+                    }
+                }
+            },
+            "references": [
+                "https://nces.ed.gov/pubs93/93122.pdf",
+                "https://nces.ed.gov/surveys/pss/zip/LAYOUT_8990.zip",
+                "https://nces.ed.gov/surveys/pss/pdf/quest_8990.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "1989/1990",
+            "title": "Private School Universe Survey, 1989-90"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Hyon Kim",
                 "hasEmail": "mailto:hyon.kim@gsa.gov"
             },
+            "dataQuality": true,
+            "description": "Since President Obama took office, Congress has appropriated more than $4 billion to help turn around the nation's lowest-performing schools. States were awarded nearly $3.5 billion in School Improvement Grant funds in 2010 to turn around their persistently lowest achieving schools. School districts then applied to state for the funds this spring. When school districts applied, they were required to indicate that they would implement one of the following four models in their persistently lowest achieving schools: Turnaround Model: Replace the principal, screen existing school staff, and rehire no more than half the teachers; adopt a new governance structure; and improve the school through curriculum reform, professional development, extending learning time, and other strategies. Restart Model: Convert a school or close it and re-open it as a charter school or under an education management organization. School Closure: Close the school and send the students to higher-achieving schools in the district. Transformation Model: Replace the principal and improve the school through comprehensive curriculum reform, professional development, extending learning time, and other strategies.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/csv",
+                    "downloadURL": "https://inventory.data.gov/dataset/ce23c458-9c25-4bcc-a7bd-0490641dec8e/resource/9665a448-6f2f-4872-99b9-bf12b5af84f4/download/userssharedsdfschoolimprovement2010grants.csv",
                     "format": "CSV",
-                    "title": "userssharedsdfschoolimprovement2010grants.csv",
-                    "downloadURL": "https://inventory.data.gov/dataset/ce23c458-9c25-4bcc-a7bd-0490641dec8e/resource/9665a448-6f2f-4872-99b9-bf12b5af84f4/download/userssharedsdfschoolimprovement2010grants.csv"
+                    "mediaType": "text/csv",
+                    "title": "userssharedsdfschoolimprovement2010grants.csv"
                 }
             ],
+            "identifier": "e51595bd-5692-4e89-8ae0-f54bc9d487a9",
             "keyword": [
                 "7c15ea20-6617-4989-aa89-4f48c8a5517a",
                 "grants",
@@ -77776,23 +77766,11 @@
                 "interactive",
                 "school"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-22T19:11:32.134037",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "ED Grants: School Improvement Grant (SIG)",
-            "description": "The School Improvement Grant (SIG) program data depicts the location, award amount and type of model selected by States in awarding nearly $3.5 billion in School Improvement Grant funds in 2010 to turn around their persistently lowest achieving schools.",
-            "modified": "2023-06-22T18:23:33.718571",
-            "accessLevel": "public",
-            "identifier": "a022f176-da12-4aae-ada4-27fba7c8fd98",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "U.S. Department of Education",
@@ -77801,22 +77779,35 @@
                     "name": "U.S. Government"
                 }
             },
+            "spatial": "United States",
+            "temporal": "2010/P1Y",
+            "title": "School Improvement 2010 Grants"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "irregular",
+            "bureauCode": [
+                "018:00"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David Harrity",
                 "hasEmail": "mailto:david.harrity@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The School Improvement Grant (SIG) program data depicts the location, award amount and type of model selected by States in awarding nearly $3.5 billion in School Improvement Grant funds in 2010 to turn around their persistently lowest achieving schools.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "sig_database.xls",
                     "description": "School Improvement Grant (SIG) data available in a Microsoft Excel file",
-                    "downloadURL": "https://www.ed.gov/sites/default/files/sig_database.xls"
+                    "downloadURL": "https://www.ed.gov/sites/default/files/sig_database.xls",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "sig_database.xls"
                 }
             ],
+            "identifier": "a022f176-da12-4aae-ada4-27fba7c8fd98",
             "keyword": [
                 "7c15ea20-6617-4989-aa89-4f48c8a5517a",
                 "achievement",
@@ -77826,1145 +77817,1132 @@
                 "high-school",
                 "performance"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:00"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://www.ed.gov/sites/default/files/SIG%20Database%20Documentation.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color",
-            "description": "My Brother's Keeper (MBK) initiative is an interagency effort to improve measurably the expected educational and life outcomes for and address the persistent opportunity gaps faced by boys and young men of color (including African Americans, Hispanic Americans, and Native Americans). The MBK Task Force coordinates a Federal effort to improve significantly the expected life outcomes for boys and young men of color and their contributions to U.S. prosperity. The MBK Task Force collaborated with the Interagency Forum on Child and Family Statistics and federal statistical agencies to pull together new statistics for key indicators - derived from existing, publicly available datasets - cross tabulated for race and gender for the first time. These statistics are highlighted in the MBK Task Force May 2014 report and are posted on MBK.ed.gov.",
-            "modified": "2023-06-22T18:19:32.597150",
-            "accessLevel": "public",
-            "identifier": "7aa6e529-91df-439a-8342-a00c3dd70b81",
-            "dataQuality": true,
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "2014/P1Y",
+            "modified": "2023-06-22T18:23:33.718571",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for Education Statistics (NCES)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Institute of Education Sciences (IES)",
-                    "subOrganizationOf": {
-                        "@type": "org:Organization",
-                        "name": "Office of the Secretary (OS)",
-                        "subOrganizationOf": {
                 "@type": "org:Organization",
                 "name": "U.S. Department of Education",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "U.S. Government"
                 }
-                        }
-                    }
-                }
             },
+            "references": [
+                "https://www.ed.gov/sites/default/files/SIG%20Database%20Documentation.pdf"
+            ],
+            "spatial": "United States",
+            "title": "ED Grants: School Improvement Grant (SIG)"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Chris Chapman",
                 "hasEmail": "mailto:chris.chapman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "My Brother's Keeper (MBK) initiative is an interagency effort to improve measurably the expected educational and life outcomes for and address the persistent opportunity gaps faced by boys and young men of color (including African Americans, Hispanic Americans, and Native Americans). The MBK Task Force coordinates a Federal effort to improve significantly the expected life outcomes for boys and young men of color and their contributions to U.S. prosperity. The MBK Task Force collaborated with the Interagency Forum on Child and Family Statistics and federal statistical agencies to pull together new statistics for key indicators - derived from existing, publicly available datasets - cross tabulated for race and gender for the first time. These statistics are highlighted in the MBK Task Force May 2014 report and are posted on MBK.ed.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Births-to-young-adult-women_verified.no-chart.two-tabs-with-rates.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on births to young adult women in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Births-to-young-adult-women_verified.no-chart.two-tabs-with-rates.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Births-to-young-adult-women_verified.no-chart.two-tabs-with-rates.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Births-to-young-adult-women_verified.no-chart.two-tabs-with-rates.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "userssharedsdfratebrthsyaw1819raceethncty20002012.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on births to young adult women in a CSV file",
-                    "downloadURL": "https://inventory.data.gov/dataset/cedbc0ee-d679-4ebf-8b00-502dc0de5738/resource/ef734bd0-0aff-4687-9b8a-fc69b937be63/download/userssharedsdfratebrthsyaw1819raceethncty20002012.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/cedbc0ee-d679-4ebf-8b00-502dc0de5738/resource/ef734bd0-0aff-4687-9b8a-fc69b937be63/download/userssharedsdfratebrthsyaw1819raceethncty20002012.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "userssharedsdfratebrthsyaw1819raceethncty20002012.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Adolescent-births_verified.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on adolescent births in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Adolescent-births_verified.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Adolescent-births_verified.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Adolescent-births_verified.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "userssharedsdfadolescentsbirthsage1517re20002012.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on adolescent births in a CSV file",
-                    "downloadURL": "https://inventory.data.gov/dataset/8a9b7321-9844-4461-a81e-2766b472d833/resource/a0e56395-dd48-4765-b5d5-bf7db0708888/download/userssharedsdfadolescentsbirthsage1517re20002012.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/8a9b7321-9844-4461-a81e-2766b472d833/resource/a0e56395-dd48-4765-b5d5-bf7db0708888/download/userssharedsdfadolescentsbirthsage1517re20002012.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "userssharedsdfadolescentsbirthsage1517re20002012.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Family-structure_verified.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on family structure and children's living arrangements in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Family-structure_verified.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Family-structure_verified.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Family-structure_verified.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "userssharedsdfpercchldrn017byprsncprntshshldsre20012013.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on family structure and children's living arrangements in a CSV file",
-                    "downloadURL": "https://inventory.data.gov/dataset/b73b9d48-fd53-4c17-b2b3-f4bd6e00a106/resource/4b0bc75c-6ac4-49a9-8ca1-92a46058f8d3/download/userssharedsdfpercchldrn017byprsncprntshshldsre20012013.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/b73b9d48-fd53-4c17-b2b3-f4bd6e00a106/resource/4b0bc75c-6ac4-49a9-8ca1-92a46058f8d3/download/userssharedsdfpercchldrn017byprsncprntshshldsre20012013.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "userssharedsdfpercchldrn017byprsncprntshshldsre20012013.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Living-arrangements_verified.se_.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on living arrangements of young adults in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Living-arrangements_verified.se_.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Living-arrangements_verified.se_.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Living-arrangements_verified.se_.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "Living-arrangements_verified_2014_0731_1331.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on living arrangements of young adults in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Living-arrangements_verified_2014_0731_1331.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Living-arrangements_verified_2014_0731_1331.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "Living-arrangements_verified_2014_0731_1331.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Children-in-households-with-violent-crime-by-hh-race-eth-sex-2000-2012.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on crime in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Children-in-households-with-violent-crime-by-hh-race-eth-sex-2000-2012.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Children-in-households-with-violent-crime-by-hh-race-eth-sex-2000-2012.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Children-in-households-with-violent-crime-by-hh-race-eth-sex-2000-2012.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "Children-in-households-with-violent-crime_2014_0731_1400.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on crime in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Children-in-households-with-violent-crime_2014_0731_1400.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Children-in-households-with-violent-crime_2014_0731_1400.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "Children-in-households-with-violent-crime_2014_0731_1400.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Child-poverty_Percent.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on children in poverty in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Child-poverty_Percent.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Child-poverty_Percent.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Child-poverty_Percent.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "Child-poverty_Percent_2014_0731_1100.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on children in poverty in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Child-poverty_Percent_2014_0731_1100.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Child-poverty_Percent_2014_0731_1100.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "Child-poverty_Percent_2014_0731_1100.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Housing-problems_verified1.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on housing problems in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Housing-problems_verified1.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Housing-problems_verified1.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Housing-problems_verified1.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "Housing-problems_verified_2014_0804_1600.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on housing problems in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Housing-problems_verified_2014_0804_1600.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Housing-problems_verified_2014_0804_1600.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "Housing-problems_verified_2014_0804_1600.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Fam7a_new-indicators.simplified.xls",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on substantiated maltreatment reports in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Fam7a_new-indicators.simplified.xls"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Fam7a_new-indicators.simplified.xls",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Fam7a_new-indicators.simplified.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "Fam7a_new-indicators_2014_0731_1400.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on substantiated maltreatment reports in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Fam7a_new-indicators_2014_0731_1400.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Fam7a_new-indicators_2014_0731_1400.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "Fam7a_new-indicators_2014_0731_1400.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "NAEP4-reading-trans_verified.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on 4th grade NAEP reading scale scores in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP4-reading-trans_verified.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP4-reading-trans_verified.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "NAEP4-reading-trans_verified.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "userssharedsdfnaepscalescoresof4thgpsssresy200213.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on 4th grade NAEP reading scale scores in a CSV file",
-                    "downloadURL": "https://inventory.data.gov/dataset/fcc30ea5-be51-4a12-9dad-40db27dbf939/resource/ff146412-88f3-42b8-88ad-84737f192ef2/download/userssharedsdfnaepscalescoresof4thgpsssresy200213.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/fcc30ea5-be51-4a12-9dad-40db27dbf939/resource/ff146412-88f3-42b8-88ad-84737f192ef2/download/userssharedsdfnaepscalescoresof4thgpsssresy200213.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "userssharedsdfnaepscalescoresof4thgpsssresy200213.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "NAEP4-reading-disabilities-trans_verified.xls",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on 4th graders with disabilities NAEP reading scale scores in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP4-reading-disabilities-trans_verified.xls"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP4-reading-disabilities-trans_verified.xls",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "NAEP4-reading-disabilities-trans_verified.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "NAEP4-reading-disabilities-trans_verified_2014_0801_1550.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on 4th graders with disabilities NAEP reading scale scores in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP4-reading-disabilities-trans_verified_2014_0801_1550.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP4-reading-disabilities-trans_verified_2014_0801_1550.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "NAEP4-reading-disabilities-trans_verified_2014_0801_1550.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "NAEP8-reading-trans_verified.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on 8th grade NAEP reading scale scores in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP8-reading-trans_verified.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP8-reading-trans_verified.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "NAEP8-reading-trans_verified.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "userssharedsdfnaepscalescoresof8thgpsssresy200213.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on 8th grade NAEP reading scale scores in a CSV file",
-                    "downloadURL": "https://inventory.data.gov/dataset/f5e55f09-548b-4e7d-ab19-ad6011fa4131/resource/8194be53-7c72-4f20-b893-62662df7ff5b/download/userssharedsdfnaepscalescoresof8thgpsssresy200213.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/f5e55f09-548b-4e7d-ab19-ad6011fa4131/resource/8194be53-7c72-4f20-b893-62662df7ff5b/download/userssharedsdfnaepscalescoresof8thgpsssresy200213.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "userssharedsdfnaepscalescoresof8thgpsssresy200213.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "NAEP8-reading-disabilities-trans_verified.xls",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on 8th graders with disabilities NAEP reading scale scores in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP8-reading-disabilities-trans_verified.xls"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP8-reading-disabilities-trans_verified.xls",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "NAEP8-reading-disabilities-trans_verified.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "NAEP8-math-disabilities-trans_verified_2014_0804_1715.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on 8th graders with disabilities NAEP reading scale scores in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP8-math-disabilities-trans_verified_2014_0804_1715.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP8-math-disabilities-trans_verified_2014_0804_1715.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "NAEP8-math-disabilities-trans_verified_2014_0804_1715.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "NAEP12-reading-trans_verified.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on 12th grade NAEP reading scale scores in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP12-reading-trans_verified.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP12-reading-trans_verified.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "NAEP12-reading-trans_verified.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "userssharedsdfnaepscalescoresof12thgpsssresy200213.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on 12th grade NAEP reading scale scores in a CSV file",
-                    "downloadURL": "https://inventory.data.gov/dataset/87183bac-3c00-4963-84fd-2f815d6ae1fa/resource/c636d78e-a5e2-4430-9e39-35d24cdf0a3f/download/userssharedsdfnaepscalescoresof12thgpsssresy200213.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/87183bac-3c00-4963-84fd-2f815d6ae1fa/resource/c636d78e-a5e2-4430-9e39-35d24cdf0a3f/download/userssharedsdfnaepscalescoresof12thgpsssresy200213.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "userssharedsdfnaepscalescoresof12thgpsssresy200213.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "NAEP12-reading-disabilities-trans_verified.xls",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on 12th graders with disabilities NAEP reading scale scores in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP12-reading-disabilities-trans_verified.xls"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP12-reading-disabilities-trans_verified.xls",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "NAEP12-reading-disabilities-trans_verified.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "NAEP12-reading-disabilities-trans_verified-2014_0804_1718.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on 12th graders with disabilities NAEP reading scale scores in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP12-reading-disabilities-trans_verified-2014_0804_1718.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP12-reading-disabilities-trans_verified-2014_0804_1718.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "NAEP12-reading-disabilities-trans_verified-2014_0804_1718.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "NAEP4-math-trans_verified.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on 4th grade NAEP mathematics scale scores in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP4-math-trans_verified.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP4-math-trans_verified.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "NAEP4-math-trans_verified.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "NAEP4-math-trans_verified_2014_0801_1536.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on 4th grade NAEP mathematics scale scores in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP4-math-trans_verified_2014_0801_1536.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP4-math-trans_verified_2014_0801_1536.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "NAEP4-math-trans_verified_2014_0801_1536.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "NAEP4-math-disabilities-trans_verified.xls",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on 4th graders with disabilities NAEP mathematics scale scores in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP4-math-disabilities-trans_verified.xls"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP4-math-disabilities-trans_verified.xls",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "NAEP4-math-disabilities-trans_verified.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "NAEP4-math-disabilities-trans_verified_2014_0801_1539.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on 4th graders with disabilities NAEP mathematics scale scores in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP4-math-disabilities-trans_verified_2014_0801_1539.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP4-math-disabilities-trans_verified_2014_0801_1539.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "NAEP4-math-disabilities-trans_verified_2014_0801_1539.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "NAEP8-math-trans_verified.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on 8th grade NAEP mathematics scale scores in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP8-math-trans_verified.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP8-math-trans_verified.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "NAEP8-math-trans_verified.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "NAEP8-math_verified-2014_0804_1700.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on 8th grade NAEP mathematics scale scores in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP8-math_verified-2014_0804_1700.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP8-math_verified-2014_0804_1700.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "NAEP8-math_verified-2014_0804_1700.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "NAEP8-math-disabilities-trans_verified.xls",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on 8th graders with disabilities NAEP mathematics scale scores in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP8-math-disabilities-trans_verified.xls"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP8-math-disabilities-trans_verified.xls",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "NAEP8-math-disabilities-trans_verified.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "NAEP8-math-disabilities-trans_verified_2014_0804_17151.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on 8th graders with disabilities NAEP mathematics scale scores in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP8-math-disabilities-trans_verified_2014_0804_17151.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP8-math-disabilities-trans_verified_2014_0804_17151.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "NAEP8-math-disabilities-trans_verified_2014_0804_17151.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "NAEP12-math-trans_verified.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on 12th grade NAEP mathematics scale scores in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP12-math-trans_verified.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP12-math-trans_verified.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "NAEP12-math-trans_verified.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "NAEP12-math-trans_verified-2014_0804_1720.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on 12th grade NAEP mathematics scale scores in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP12-math-trans_verified-2014_0804_1720.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP12-math-trans_verified-2014_0804_1720.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "NAEP12-math-trans_verified-2014_0804_1720.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "NAEP12-math-disabilities-trans_verified.xls",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on 12th graders with disabilities NAEP mathematics scale scores in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP12-math-disabilities-trans_verified.xls"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP12-math-disabilities-trans_verified.xls",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "NAEP12-math-disabilities-trans_verified.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "NAEP12-math-disabilities-trans_verified-2014_0804_1715.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on 12th graders with disabilities NAEP mathematics scale scores in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP12-math-disabilities-trans_verified-2014_0804_1715.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NAEP12-math-disabilities-trans_verified-2014_0804_1715.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "NAEP12-math-disabilities-trans_verified-2014_0804_1715.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Child-care_verified.no-chart.simplified.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on center-based child care usage in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Child-care_verified.no-chart.simplified.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Child-care_verified.no-chart.simplified.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Child-care_verified.no-chart.simplified.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "IBenrollment-trans_Final_nces.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on International Baccalaureate (IB) program enrollment in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/IBenrollment-trans_Final_nces.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/IBenrollment-trans_Final_nces.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "IBenrollment-trans_Final_nces.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "userssharedsdfibprogenrollof11thand12th201112.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on International Baccalaureate (IB) program enrollment in a CSV file",
-                    "downloadURL": "https://inventory.data.gov/dataset/20e4afd5-4812-424a-aade-6c2f45e6d2a0/resource/488c382d-ae71-43ab-928b-dfbabd7b9071/download/userssharedsdfibprogenrollof11thand12th201112.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/20e4afd5-4812-424a-aade-6c2f45e6d2a0/resource/488c382d-ae71-43ab-928b-dfbabd7b9071/download/userssharedsdfibprogenrollof11thand12th201112.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "userssharedsdfibprogenrollof11thand12th201112.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "APenrollment-trans_Final_nces.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on Advanced Placement (AP) course enrollment in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/APenrollment-trans_Final_nces.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/APenrollment-trans_Final_nces.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "APenrollment-trans_Final_nces.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "userssharedsdfstdntsap11and12grdenrllsre201112.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on Advanced Placement (AP) course enrollment in a CSV file",
-                    "downloadURL": "https://inventory.data.gov/dataset/3b9414d1-22dd-4cbc-bad1-fdc44817b0c1/resource/1ac26874-4196-4284-a3fa-1c1b3e225ac0/download/userssharedsdfstdntsap11and12grdenrllsre201112.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/3b9414d1-22dd-4cbc-bad1-fdc44817b0c1/resource/1ac26874-4196-4284-a3fa-1c1b3e225ac0/download/userssharedsdfstdntsap11and12grdenrllsre201112.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "userssharedsdfstdntsap11and12grdenrllsre201112.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "poverty-trans_verified.xls",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on high poverty school enrollment in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/poverty-trans_verified.xls"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/poverty-trans_verified.xls",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "poverty-trans_verified.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "Poverty-trans_verified.percount_2014_0804_1615.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on high poverty school enrollment in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Poverty-trans_verified.percount_2014_0804_1615.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Poverty-trans_verified.percount_2014_0804_1615.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "Poverty-trans_verified.percount_2014_0804_1615.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "schoolpov-disabilities-trans_verified.percount2.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on students with disabilities and high poverty school enrollment in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/schoolpov-disabilities-trans_verified.percount2.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/schoolpov-disabilities-trans_verified.percount2.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "schoolpov-disabilities-trans_verified.percount2.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "schoolpov-disabilities-trans_verified.percount_2014_0730_1600.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on students with disabilities and high poverty school enrollment in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/schoolpov-disabilities-trans_verified.percount_2014_0730_1600.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/schoolpov-disabilities-trans_verified.percount_2014_0730_1600.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "schoolpov-disabilities-trans_verified.percount_2014_0730_1600.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Expulsions-trans_verified.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on expulsions in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Expulsions-trans_verified.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Expulsions-trans_verified.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Expulsions-trans_verified.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "userssharedsdfpercpblcschlstdntsexplldcysre201112.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on expulsions in a CSV file",
-                    "downloadURL": "https://inventory.data.gov/dataset/eb114613-4dfa-40d9-813a-0721b611f437/resource/6500f082-d8a0-4ffc-86ae-28641b6fd6be/download/userssharedsdfpercpblcschlstdntsexplldcysre201112.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/eb114613-4dfa-40d9-813a-0721b611f437/resource/6500f082-d8a0-4ffc-86ae-28641b6fd6be/download/userssharedsdfpercpblcschlstdntsexplldcysre201112.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "userssharedsdfpercpblcschlstdntsexplldcysre201112.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Suspensions-trans_verified.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on out-of-school suspensions in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Suspensions-trans_verified.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Suspensions-trans_verified.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Suspensions-trans_verified.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "userssharedsdfpercpblcschlstdntsoossuspncysre201112.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on out-of-school suspensions in a CSV file",
-                    "downloadURL": "https://inventory.data.gov/dataset/62c6bf6b-2531-4dea-a9e2-888569b9c3fa/resource/14acd41d-9788-4f10-b870-9bd5ba57a431/download/userssharedsdfpercpblcschlstdntsoossuspncysre201112.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/62c6bf6b-2531-4dea-a9e2-888569b9c3fa/resource/14acd41d-9788-4f10-b870-9bd5ba57a431/download/userssharedsdfpercpblcschlstdntsoossuspncysre201112.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "userssharedsdfpercpblcschlstdntsoossuspncysre201112.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "disabilities-trans_verified.xls",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on students with disabilities in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/disabilities-trans_verified.xls"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/disabilities-trans_verified.xls",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "disabilities-trans_verified.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "disabilities-trans_verified_2014_0731_0900.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on students with disabilities in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/disabilities-trans_verified_2014_0731_0900.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/disabilities-trans_verified_2014_0731_0900.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "disabilities-trans_verified_2014_0731_0900.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Expulsions_IDEA-trans_verified.xls",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on expelled students with disabilities in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Expulsions_IDEA-trans_verified.xls"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Expulsions_IDEA-trans_verified.xls",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Expulsions_IDEA-trans_verified.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "expulsions_IDEA-trans_verified_CSVconversion_2014_0731_1100.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on expelled students with disabilities in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/expulsions_IDEA-trans_verified_CSVconversion_2014_0731_1100.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/expulsions_IDEA-trans_verified_CSVconversion_2014_0731_1100.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "expulsions_IDEA-trans_verified_CSVconversion_2014_0731_1100.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Suspensions_IDEA-trans_verified.xls",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on students with disabilities receiving out-of-school suspensions in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Suspensions_IDEA-trans_verified.xls"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Suspensions_IDEA-trans_verified.xls",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Suspensions_IDEA-trans_verified.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "Suspensions_IDEA-trans_verified_2014_0804_1500.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on students with disabilities receiving out-of-school suspensions in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Suspensions_IDEA-trans_verified_2014_0804_1500.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Suspensions_IDEA-trans_verified_2014_0804_1500.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "Suspensions_IDEA-trans_verified_2014_0804_1500.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Attainment-high-school_Final_nces.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on educational attainment in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Attainment-high-school_Final_nces.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Attainment-high-school_Final_nces.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Attainment-high-school_Final_nces.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "userssharedsdfperc18to24yohgstlvledctnlattnmthssre20002013.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on educational attainment in a CSV file",
-                    "downloadURL": "https://inventory.data.gov/dataset/1728cea3-d72d-4f55-8582-d199e5a37b9c/resource/9e6efcb7-cb41-4497-8e58-e6e2725a6193/download/userssharedsdfperc18to24yohgstlvledctnlattnmthssre20002013.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/1728cea3-d72d-4f55-8582-d199e5a37b9c/resource/9e6efcb7-cb41-4497-8e58-e6e2725a6193/download/userssharedsdfperc18to24yohgstlvledctnlattnmthssre20002013.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "userssharedsdfperc18to24yohgstlvledctnlattnmthssre20002013.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Remedial-trans_verified.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on enrollment in remedial classes in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Remedial-trans_verified.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Remedial-trans_verified.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Remedial-trans_verified.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "userssharedsdfpercfygsrmdledctncrsessresy19992000201112.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on enrollment in remedial classes in a CSV file",
-                    "downloadURL": "https://inventory.data.gov/dataset/12a2908c-27b7-4f46-a62e-114d2d508c1b/resource/33e6f63b-297f-4fc5-aa91-5fc9b3741368/download/userssharedsdfpercfygsrmdledctncrsessresy19992000201112.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/12a2908c-27b7-4f46-a62e-114d2d508c1b/resource/33e6f63b-297f-4fc5-aa91-5fc9b3741368/download/userssharedsdfpercfygsrmdledctncrsessresy19992000201112.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "userssharedsdfpercfygsrmdledctncrsessresy19992000201112.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "College-enrollment-rates-trans_verified.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on postsecondary enrollment in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/College-enrollment-rates-trans_verified.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/College-enrollment-rates-trans_verified.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "College-enrollment-rates-trans_verified.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "userssharedsdfperc18to24yoenrld24ycsre20002012.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on postsecondary enrollment in a CSV file",
-                    "downloadURL": "https://inventory.data.gov/dataset/efd85e6e-ee78-4978-bbf7-aeae4114605c/resource/e918f758-502b-42e9-ae05-d42c155b65b7/download/userssharedsdfperc18to24yoenrld24ycsre20002012.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/efd85e6e-ee78-4978-bbf7-aeae4114605c/resource/e918f758-502b-42e9-ae05-d42c155b65b7/download/userssharedsdfperc18to24yoenrld24ycsre20002012.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "userssharedsdfperc18to24yoenrld24ycsre20002012.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "attain-somecollege-trans_verified.percount.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on educational attainment in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/attain-somecollege-trans_verified.percount.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/attain-somecollege-trans_verified.percount.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "attain-somecollege-trans_verified.percount.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "Attain-somecollege_2014_0731_1400.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on educational attainment in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Attain-somecollege_2014_0731_1400.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Attain-somecollege_2014_0731_1400.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "Attain-somecollege_2014_0731_1400.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "attain-associate-trans_verified.percount.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on educational attainment in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/attain-associate-trans_verified.percount.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/attain-associate-trans_verified.percount.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "attain-associate-trans_verified.percount.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "attain-associate-trans_verified_2014_0731_1100.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on educational attainment in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/attain-associate-trans_verified_2014_0731_1100.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/attain-associate-trans_verified_2014_0731_1100.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "attain-associate-trans_verified_2014_0731_1100.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "attain-bachelors-trans_verified.percount.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on bachelor's or higher degree completion in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/attain-bachelors-trans_verified.percount.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/attain-bachelors-trans_verified.percount.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "attain-bachelors-trans_verified.percount.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "attain-bachelors-trans_verified_2014_0731_1100.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on bachelor's or higher degree completion in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/attain-bachelors-trans_verified_2014_0731_1100.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/attain-bachelors-trans_verified_2014_0731_1100.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "attain-bachelors-trans_verified_2014_0731_1100.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "STEM-trans_verified.percount2.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on STEM degrees in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/STEM-trans_verified.percount2.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/STEM-trans_verified.percount2.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "STEM-trans_verified.percount2.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "STEM-trans_verified_2014_0804_1421.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on STEM degrees in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/STEM-trans_verified_2014_0804_1421.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/STEM-trans_verified_2014_0804_1421.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "STEM-trans_verified_2014_0804_1421.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "LFPR_rates_verified.xls",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on labor force participation in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/LFPR_rates_verified.xls"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/LFPR_rates_verified.xls",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "LFPR_rates_verified.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "LFPR_rates_verfied_2014_0731_1335.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on labor force participation in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/LFPR_rates_verfied_2014_0731_1335.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/LFPR_rates_verfied_2014_0731_1335.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "LFPR_rates_verfied_2014_0731_1335.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Not-enrolled-nor-working_Final_nces.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on 18- to 24-year olds neither enrolled in school nor working in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Not-enrolled-nor-working_Final_nces.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Not-enrolled-nor-working_Final_nces.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Not-enrolled-nor-working_Final_nces.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "userssharedsdfperc18to24yowhonethenrlschlnorworksre20002012.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on 18- to 24-year olds neither enrolled in school nor working in a CSV file",
-                    "downloadURL": "https://inventory.data.gov/dataset/3ab579fe-7e09-4fcc-a926-b909aa8647f7/resource/90a03e60-697c-41a6-8539-ed91b70c3b75/download/userssharedsdfperc18to24yowhonethenrlschlnorworksre20002012.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/3ab579fe-7e09-4fcc-a926-b909aa8647f7/resource/90a03e60-697c-41a6-8539-ed91b70c3b75/download/userssharedsdfperc18to24yowhonethenrlschlnorworksre20002012.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "userssharedsdfperc18to24yowhonethenrlschlnorworksre20002012.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Median-Earnings_Less-than-high-school_verified.xls",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on median annual earnings of individuals with less than high school completion in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Median-Earnings_Less-than-high-school_verified.xls"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Median-Earnings_Less-than-high-school_verified.xls",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Median-Earnings_Less-than-high-school_verified.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "Median-Earnings_Less-than-high-school_verified.percount_2014_0801_1603.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on median annual earnings of individuals with less than high school completion in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Median-Earnings_Less-than-high-school_verified.percount_2014_0801_1603.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Median-Earnings_Less-than-high-school_verified.percount_2014_0801_1603.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "Median-Earnings_Less-than-high-school_verified.percount_2014_0801_1603.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Median-Earnings_High-school_verified.xls",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on median annual earnings of individuals with only high school completion in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Median-Earnings_High-school_verified.xls"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Median-Earnings_High-school_verified.xls",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Median-Earnings_High-school_verified.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "Median-Earnings_High-school_verified.percount_2014_0801_1607.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on median annual earnings of individuals with only high school completion in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Median-Earnings_High-school_verified.percount_2014_0801_1607.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Median-Earnings_High-school_verified.percount_2014_0801_1607.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "Median-Earnings_High-school_verified.percount_2014_0801_1607.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Median-Earnings_Some-college_verified.xls",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on median annual earnings of individuals with only some college completion in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Median-Earnings_Some-college_verified.xls"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Median-Earnings_Some-college_verified.xls",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Median-Earnings_Some-college_verified.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "Median-Earnings_Some-college_verified.percount_2014_0801_1556.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on median annual earnings of individuals with only some college completion in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Median-Earnings_Some-college_verified.percount_2014_0801_1556.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Median-Earnings_Some-college_verified.percount_2014_0801_1556.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "Median-Earnings_Some-college_verified.percount_2014_0801_1556.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Median-Earnings_Associates-degree_verified.xls",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on median annual earnings of individuals with only an associate's degree completion in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Median-Earnings_Associates-degree_verified.xls"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Median-Earnings_Associates-degree_verified.xls",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Median-Earnings_Associates-degree_verified.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "Median-Earnings_Associates-degree_verified.percount_2014_0801_1613.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on median annual earnings of individuals with only an associate's degree completion in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Median-Earnings_Associates-degree_verified.percount_2014_0801_1613.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Median-Earnings_Associates-degree_verified.percount_2014_0801_1613.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "Median-Earnings_Associates-degree_verified.percount_2014_0801_1613.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Unemployment-Rates_verified.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on unemployment rates in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Unemployment-Rates_verified.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Unemployment-Rates_verified.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Unemployment-Rates_verified.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "userssharedsdfunemplymntrateyaa1824sre19802013aa.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on unemployment rates in a CSV file",
-                    "downloadURL": "https://inventory.data.gov/dataset/c714f3df-9663-4291-a26d-a04884b73573/resource/888daf2d-26a2-4aa8-acf0-8770b470ccad/download/userssharedsdfunemplymntrateyaa1824sre19802013aa.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/c714f3df-9663-4291-a26d-a04884b73573/resource/888daf2d-26a2-4aa8-acf0-8770b470ccad/download/userssharedsdfunemplymntrateyaa1824sre19802013aa.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "userssharedsdfunemplymntrateyaa1824sre19802013aa.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Healthy-Eating-Index-2005-scores_verified.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on average Healthy Eating Index-2005 scores in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Healthy-Eating-Index-2005-scores_verified.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Healthy-Eating-Index-2005-scores_verified.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Healthy-Eating-Index-2005-scores_verified.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "DATA_HIV_-MBK-Data-Request-5-15-14_verified.percount2.xls",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on HIV infections in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/DATA_HIV_-MBK-Data-Request-5-15-14_verified.percount2.xls"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/DATA_HIV_-MBK-Data-Request-5-15-14_verified.percount2.xls",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "DATA_HIV_-MBK-Data-Request-5-15-14_verified.percount2.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "Data_HIV_MBK-Data-Request_2014_0731_1100.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on HIV infections in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Data_HIV_MBK-Data-Request_2014_0731_1100.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Data_HIV_MBK-Data-Request_2014_0731_1100.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "Data_HIV_MBK-Data-Request_2014_0731_1100.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Low-birthweight_NCHS_Pastor4.25_verified.xls",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on infants with low birthweights in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Low-birthweight_NCHS_Pastor4.25_verified.xls"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Low-birthweight_NCHS_Pastor4.25_verified.xls",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Low-birthweight_NCHS_Pastor4.25_verified.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "Low-birthweight_NCHS_Pastor4.26_verified_2014_0731_1345.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on infants with low birthweights in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Low-birthweight_NCHS_Pastor4.26_verified_2014_0731_1345.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Low-birthweight_NCHS_Pastor4.26_verified_2014_0731_1345.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "Low-birthweight_NCHS_Pastor4.26_verified_2014_0731_1345.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "MBK_ObesityPrevalence_Age6-17_Age18-24updt_verified.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on obese young adults in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/MBK_ObesityPrevalence_Age6-17_Age18-24updt_verified.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/MBK_ObesityPrevalence_Age6-17_Age18-24updt_verified.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "MBK_ObesityPrevalence_Age6-17_Age18-24updt_verified.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "MBK_ObesityPrevalence_Age6-17and18-24_2014_0731_1345.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on obese young adults in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/MBK_ObesityPrevalence_Age6-17and18-24_2014_0731_1345.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/MBK_ObesityPrevalence_Age6-17and18-24_2014_0731_1345.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "MBK_ObesityPrevalence_Age6-17and18-24_2014_0731_1345.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Usual-source-of-health-care_verified.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on health care in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Usual-source-of-health-care_verified.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Usual-source-of-health-care_verified.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Usual-source-of-health-care_verified.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "userssharedsdfpercchldrn017bynounuslsrchlthcaresre20002012.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on health care in a CSV file",
-                    "downloadURL": "https://inventory.data.gov/dataset/7d45db5b-29d2-4f27-97c6-890447069096/resource/8ccc548a-1d23-4678-bd4e-123aa496fc27/download/userssharedsdfpercchldrn017bynounuslsrchlthcaresre20002012.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/7d45db5b-29d2-4f27-97c6-890447069096/resource/8ccc548a-1d23-4678-bd4e-123aa496fc27/download/userssharedsdfpercchldrn017bynounuslsrchlthcaresre20002012.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "userssharedsdfpercchldrn017bynounuslsrchlthcaresre20002012.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "NH1112_udcariesAges-15-24_verified.xls",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on untreated dental caries in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NH1112_udcariesAges-15-24_verified.xls"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/NH1112_udcariesAges-15-24_verified.xls",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "NH1112_udcariesAges-15-24_verified.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Rev_Asthma_current_0_17_05282014_verified.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on asthma in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Rev_Asthma_current_0_17_05282014_verified.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Rev_Asthma_current_0_17_05282014_verified.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Rev_Asthma_current_0_17_05282014_verified.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "Rev_Asthma_current_2014_0804_1630.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on asthma in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Rev_Asthma_current_2014_0804_1630.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Rev_Asthma_current_2014_0804_1630.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "Rev_Asthma_current_2014_0804_1630.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Regular-cigarette-smoking.g8_NIDA_verified4.25.xls",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on smoking 8th graders in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Regular-cigarette-smoking.g8_NIDA_verified4.25.xls"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Regular-cigarette-smoking.g8_NIDA_verified4.25.xls",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Regular-cigarette-smoking.g8_NIDA_verified4.25.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "Regular-cigarette-smoking.g8_NIDA_verified_2014_0804_1211.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on smoking 8th graders in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Regular-cigarette-smoking.g8_NIDA_verified_2014_0804_1211.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Regular-cigarette-smoking.g8_NIDA_verified_2014_0804_1211.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "Regular-cigarette-smoking.g8_NIDA_verified_2014_0804_1211.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Regular-cigarette-smoking.g10_NIDA_verified4.25.xls",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on smoking 10th graders in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Regular-cigarette-smoking.g10_NIDA_verified4.25.xls"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Regular-cigarette-smoking.g10_NIDA_verified4.25.xls",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Regular-cigarette-smoking.g10_NIDA_verified4.25.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "Regular-cigarette-smoking.g10_NIDA_verified_2014_0804_1237.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on smoking 10th graders in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Regular-cigarette-smoking.g10_NIDA_verified_2014_0804_1237.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Regular-cigarette-smoking.g10_NIDA_verified_2014_0804_1237.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "Regular-cigarette-smoking.g10_NIDA_verified_2014_0804_1237.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Regular-cigarette-smoking-Alcohol-use-and-Illicit-drug-use_verified.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on smoking 12th graders in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Regular-cigarette-smoking-Alcohol-use-and-Illicit-drug-use_verified.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Regular-cigarette-smoking-Alcohol-use-and-Illicit-drug-use_verified.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Regular-cigarette-smoking-Alcohol-use-and-Illicit-drug-use_verified.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "Regular-cigarette-smoking.g12_NIDA_verified_2014_0804_1310.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on smoking 12th graders in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Regular-cigarette-smoking.g12_NIDA_verified_2014_0804_1310.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Regular-cigarette-smoking.g12_NIDA_verified_2014_0804_1310.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "Regular-cigarette-smoking.g12_NIDA_verified_2014_0804_1310.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Alcohol-use.g8_NIDA_verified4.25.xls",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on drinking 8th graders in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Alcohol-use.g8_NIDA_verified4.25.xls"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Alcohol-use.g8_NIDA_verified4.25.xls",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Alcohol-use.g8_NIDA_verified4.25.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "Alcohol-use.g8_2014_0731_0900.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on drinking 8th graders in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Alcohol-use.g8_2014_0731_0900.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Alcohol-use.g8_2014_0731_0900.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "Alcohol-use.g8_2014_0731_0900.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Alcohol-use.g10_NIDA_verified4.25.xls",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on drinking 10th graders in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Alcohol-use.g10_NIDA_verified4.25.xls"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Alcohol-use.g10_NIDA_verified4.25.xls",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Alcohol-use.g10_NIDA_verified4.25.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "Alcohol-use.g10_2014_0731_0900.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on drinking 10th graders in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Alcohol-use.g10_2014_0731_0900.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Alcohol-use.g10_2014_0731_0900.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "Alcohol-use.g10_2014_0731_0900.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Alcohol-use.g12_NIDA_verified4.25.xls",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on drinking 12th graders in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Alcohol-use.g12_NIDA_verified4.25.xls"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Alcohol-use.g12_NIDA_verified4.25.xls",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Alcohol-use.g12_NIDA_verified4.25.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "Alcohol-use.g12_2014_0731_0900.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on drinking 12th graders in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Alcohol-use.g12_2014_0731_0900.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Alcohol-use.g12_2014_0731_0900.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "Alcohol-use.g12_2014_0731_0900.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Illicit-drug-use.g8_NIDA_verified4.25.xls",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on illicit drug use among 8th graders in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Illicit-drug-use.g8_NIDA_verified4.25.xls"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Illicit-drug-use.g8_NIDA_verified4.25.xls",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Illicit-drug-use.g8_NIDA_verified4.25.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "Illicit-drug-use.g8_2014_0731_0900.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on illicit drug use among 8th graders in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Illicit-drug-use.g8_2014_0731_0900.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Illicit-drug-use.g8_2014_0731_0900.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "Illicit-drug-use.g8_2014_0731_0900.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Illicit-drug-use.g10_NIDA_verified4.25.xls",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on illicit drug use among 10th graders in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Illicit-drug-use.g10_NIDA_verified4.25.xls"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Illicit-drug-use.g10_NIDA_verified4.25.xls",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Illicit-drug-use.g10_NIDA_verified4.25.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "Illicit-drug-use.g10_2014_0731_0900.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on illicit drug use among 10th graders in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Illicit-drug-use.g10_2014_0731_0900.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Illicit-drug-use.g10_2014_0731_0900.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "Illicit-drug-use.g10_2014_0731_0900.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Illicit-drug-use.g12_NIDA_verified4.25.xls",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on illicit drug use among 12th graders in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Illicit-drug-use.g12_NIDA_verified4.25.xls"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Illicit-drug-use.g12_NIDA_verified4.25.xls",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Illicit-drug-use.g12_NIDA_verified4.25.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "Illicit-drug-use.g12_2014_0731_0900.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on illicit drug use among 12th graders in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Illicit-drug-use.g12_2014_0731_0900.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Illicit-drug-use.g12_2014_0731_0900.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "Illicit-drug-use.g12_2014_0731_0900.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Emot_behav_diff_5_17_05282014_verified.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on personality troubles in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Emot_behav_diff_5_17_05282014_verified.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Emot_behav_diff_5_17_05282014_verified.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Emot_behav_diff_5_17_05282014_verified.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "Emot_behave_diff_2014_0731_0900.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on personality troubles in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Emot_behave_diff_2014_0731_0900.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Emot_behave_diff_2014_0731_0900.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "Emot_behave_diff_2014_0731_0900.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Condom-use_verified.xls",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on unprotected sex in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Condom-use_verified.xls"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Condom-use_verified.xls",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Condom-use_verified.xls"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "Condom-use_verified_CSVconversion_2014_0731_0900.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on unprotected sex in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Condom-use_verified_CSVconversion_2014_0731_0900.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Condom-use_verified_CSVconversion_2014_0731_0900.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "Condom-use_verified_CSVconversion_2014_0731_0900.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "suicide_americachildren_final_05282014_verified.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on suicide rates in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/suicide_americachildren_final_05282014_verified.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/suicide_americachildren_final_05282014_verified.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "suicide_americachildren_final_05282014_verified.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "suicide_americachildren_final_15-17ages18-24ages_2014_0804_1645.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on suicide rates in a CSV file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/suicide_americachildren_final_15-17ages18-24ages_2014_0804_1645.csv"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/suicide_americachildren_final_15-17ages18-24ages_2014_0804_1645.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "suicide_americachildren_final_15-17ages18-24ages_2014_0804_1645.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "CDC-Homicide-Rates-2000-2010_verified.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on homicides in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/CDC-Homicide-Rates-2000-2010_verified.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/CDC-Homicide-Rates-2000-2010_verified.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "CDC-Homicide-Rates-2000-2010_verified.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "userssharedsdfhmcdsper100kyngadults1824sre20002010.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on homicides in a CSV file",
-                    "downloadURL": "https://inventory.data.gov/dataset/d28861f3-9c77-41f3-b646-d881615e56d1/resource/d910579e-3ae8-4117-8a7c-13a01489c89d/download/userssharedsdfhmcdsper100kyngadults1824sre20002010.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/d28861f3-9c77-41f3-b646-d881615e56d1/resource/d910579e-3ae8-4117-8a7c-13a01489c89d/download/userssharedsdfhmcdsper100kyngadults1824sre20002010.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "userssharedsdfhmcdsper100kyngadults1824sre20002010.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Imprisonment-rates_verified.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on imprisonment in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Imprisonment-rates_verified.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Imprisonment-rates_verified.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Imprisonment-rates_verified.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "userssharedsdfimprisonmentratesof1824yosre20002012.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on imprisonment in a CSV file",
-                    "downloadURL": "https://inventory.data.gov/dataset/ab727e43-c577-416d-ab17-837f1451a1da/resource/793ab04c-04fe-4e19-ad75-e5815d03570c/download/userssharedsdfimprisonmentratesof1824yosre20002012.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/ab727e43-c577-416d-ab17-837f1451a1da/resource/793ab04c-04fe-4e19-ad75-e5815d03570c/download/userssharedsdfimprisonmentratesof1824yosre20002012.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "userssharedsdfimprisonmentratesof1824yosre20002012.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Adolescent-mortality_verified2.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on mortality rate in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Adolescent-mortality_verified2.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Adolescent-mortality_verified2.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Adolescent-mortality_verified2.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Nonfatal-victimization-rates_verified.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on nonfatal victimization rates in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Nonfatal-victimization-rates_verified.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Nonfatal-victimization-rates_verified.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Nonfatal-victimization-rates_verified.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "userssharedsdfnonfatalvictimizationratessre20002012.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on nonfatal victimization rates in a CSV file",
-                    "downloadURL": "https://inventory.data.gov/dataset/3e2b3d42-11e8-4617-a02b-9b5ac09925b9/resource/0519f88b-b30a-48b2-9ce9-fadf9e3409d7/download/userssharedsdfnonfatalvictimizationratessre20002012.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/3e2b3d42-11e8-4617-a02b-9b5ac09925b9/resource/0519f88b-b30a-48b2-9ce9-fadf9e3409d7/download/userssharedsdfnonfatalvictimizationratessre20002012.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "userssharedsdfnonfatalvictimizationratessre20002012.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Juveniles-in-juvenile-correction-facilities_verified.no-chart.percount2.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on rate of juveniles placed in residential facilities in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Juveniles-in-juvenile-correction-facilities_verified.no-chart.percount2.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Juveniles-in-juvenile-correction-facilities_verified.no-chart.percount2.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Juveniles-in-juvenile-correction-facilities_verified.no-chart.percount2.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "userssharedsdfratejvnlsplcdresdfacltssresy20012011.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on rate of juveniles placed in residential facilities in a CSV file",
-                    "downloadURL": "https://inventory.data.gov/dataset/2dffc4e3-a60a-43f0-99fd-fc1da1e4795b/resource/2cf70e84-d615-4365-afe9-00a9e616e729/download/userssharedsdfratejvnlsplcdresdfacltssresy20012011.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/2dffc4e3-a60a-43f0-99fd-fc1da1e4795b/resource/2cf70e84-d615-4365-afe9-00a9e616e729/download/userssharedsdfratejvnlsplcdresdfacltssresy20012011.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "userssharedsdfratejvnlsplcdresdfacltssresy20012011.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "Youth-victims-of-serious-violent-crimes_verified.no-chart.percount.xlsx",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on rate of serious violent crime victimization in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Youth-victims-of-serious-violent-crimes_verified.no-chart.percount.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/Youth-victims-of-serious-violent-crimes_verified.no-chart.percount.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Youth-victims-of-serious-violent-crimes_verified.no-chart.percount.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "userssharedsdfratesrusvlntcrmvctmztnyouthsre20002012.csv",
                     "description": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color data on rate of serious violent crime victimization in a CSV file",
-                    "downloadURL": "https://inventory.data.gov/dataset/435c468b-aac8-40a8-af84-990e4d57ebe2/resource/6b6eef5a-2467-47dd-8726-841bd64e68c9/download/userssharedsdfratesrusvlntcrmvctmztnyouthsre20002012.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/435c468b-aac8-40a8-af84-990e4d57ebe2/resource/6b6eef5a-2467-47dd-8726-841bd64e68c9/download/userssharedsdfratesrusvlntcrmvctmztnyouthsre20002012.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "userssharedsdfratesrusvlntcrmvctmztnyouthsre20002012.csv"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "Microsoft Excel",
-                    "title": "HS-attain-dropout-trans_verified.xlsx",
                     "description": "Percentage of 18- to 24-year-olds who have not completed high school by sex and race/ethnicity, 2000-2013 in a Microsoft Excel file",
-                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/HS-attain-dropout-trans_verified.xlsx"
+                    "downloadURL": "https://www2.ed.gov/rschstat/statistics/surveys/mbk/HS-attain-dropout-trans_verified.xlsx",
+                    "format": "Microsoft Excel",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "HS-attain-dropout-trans_verified.xlsx"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "text/CSV",
-                    "format": "CSV",
-                    "title": "userssharedsdfperc18to24yowhonotcomphssre20002013.csv",
                     "description": "Percentage of 18- to 24-year-olds who have not completed high school by sex and race/ethnicity, 2000-2013 in a CSV file",
-                    "downloadURL": "https://inventory.data.gov/dataset/988dfe28-739a-418c-8bee-47fec76944e0/resource/4499fc97-7ace-4723-a66e-7b477eac2d19/download/userssharedsdfperc18to24yowhonotcomphssre20002013.csv"
+                    "downloadURL": "https://inventory.data.gov/dataset/988dfe28-739a-418c-8bee-47fec76944e0/resource/4499fc97-7ace-4723-a66e-7b477eac2d19/download/userssharedsdfperc18to24yowhonotcomphssre20002013.csv",
+                    "format": "CSV",
+                    "mediaType": "text/CSV",
+                    "title": "userssharedsdfperc18to24yowhonotcomphssre20002013.csv"
                 }
             ],
+            "identifier": "7aa6e529-91df-439a-8342-a00c3dd70b81",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "adolescent-births",
@@ -78986,28 +78964,14 @@
                 "students",
                 "victims-of-crimes"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-22T18:19:32.597150",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Private School Universe Survey, 1993-94",
-            "description": "The 1993-94 Private School Universe Survey (PSS 1993-94) is a study that is part of the Private School Universe program; program data is available since 1989-1990 at <https://nces.ed.gov/surveys/pss/pssdata.asp>. PSS 1993-94 (https://nces.ed.gov/surveys/pss/) is a cross-sectional survey that collects data on private elementary and secondary schools, including religious orientation, level of school, length of school year, length of school day, total enrollment, race/ethnicity of students, number of high school graduates, number of teachers employed, program emphasis, and existence and type of kindergarten program. The study was conducted using mail questionnaires and telephone follow-up of all private schools in the United States. The PSS includes both schools with a religious orientation (e.g., Catholic, Lutheran, or Jewish) and nonsectarian schools with programs ranging from regular to special emphasis and special education. Key statistics produced from PSS 1993-94 are on the number of religiously affiliated schools, the number of private high school graduates, and the number of private school students and teachers.",
-            "modified": "2023-06-22T18:11:02.343833",
-            "accessLevel": "public",
-            "identifier": "d0025cea-b63f-47bd-bfb1-a897152bffa3",
-            "dataQuality": true,
-            "issued": "2006-06-28",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "1993/1994",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -79028,44 +78992,58 @@
                     }
                 }
             },
+            "spatial": "United States",
+            "temporal": "2014/P1Y",
+            "title": "My Brother's Keeper Key Statistical Indicators on Boys and Men of Color"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P2Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Broughman",
                 "hasEmail": "mailto:stephen.broughman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The 1993-94 Private School Universe Survey (PSS 1993-94) is a study that is part of the Private School Universe program; program data is available since 1989-1990 at <https://nces.ed.gov/surveys/pss/pssdata.asp>. PSS 1993-94 (https://nces.ed.gov/surveys/pss/) is a cross-sectional survey that collects data on private elementary and secondary schools, including religious orientation, level of school, length of school year, length of school day, total enrollment, race/ethnicity of students, number of high school graduates, number of teachers employed, program emphasis, and existence and type of kindergarten program. The study was conducted using mail questionnaires and telephone follow-up of all private schools in the United States. The PSS includes both schools with a religious orientation (e.g., Catholic, Lutheran, or Jewish) and nonsectarian schools with programs ranging from regular to special emphasis and special education. Key statistics produced from PSS 1993-94 are on the number of religiously affiliated schools, the number of private high school graduates, and the number of private school students and teachers.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped TSV",
-                    "title": "TXT_PSS9394.zip",
-                    "description": "1993-94 Private School Universe Survey data as a zipped TSV file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_9394.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/TXT_PSS9394.zip"
+                    "description": "1993-94 Private School Universe Survey data as a zipped TSV file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/TXT_PSS9394.zip",
+                    "format": "Zipped TSV",
+                    "mediaType": "application/zip",
+                    "title": "TXT_PSS9394.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS7BDAT",
-                    "title": "PSS9394_SAS7BDAT.zip",
-                    "description": "1993-94 Private School Universe Survey data as a zipped SAS 7-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_9394.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/PSS9394_SAS7BDAT.zip"
+                    "description": "1993-94 Private School Universe Survey data as a zipped SAS 7-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/PSS9394_SAS7BDAT.zip",
+                    "format": "Zipped SAS7BDAT",
+                    "mediaType": "application/zip",
+                    "title": "PSS9394_SAS7BDAT.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAV",
-                    "title": "SAV_PSS9394.zip",
-                    "description": "1993-94 Private School Universe Survey data as a zipped SPSS-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_9394.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/SAV_PSS9394.zip"
+                    "description": "1993-94 Private School Universe Survey data as a zipped SPSS-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/SAV_PSS9394.zip",
+                    "format": "Zipped SAV",
+                    "mediaType": "application/zip",
+                    "title": "SAV_PSS9394.zip"
                 }
             ],
+            "identifier": "d0025cea-b63f-47bd-bfb1-a897152bffa3",
+            "issued": "2006-06-28",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "church-related-schools",
@@ -79074,34 +79052,14 @@
                 "private-school-graduates",
                 "private-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/pubs/96143.pdf",
-                "https://nces.ed.gov/surveys/pss/zip/LAYOUT_9394.zip",
-                "https://nces.ed.gov/surveys/pss/pdf/quest_9394.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "National Postsecondary Student Aid Study, 2015-16",
-            "description": "The 2015-16 National Postsecondary Student Aid Study (NPSAS:16) is a data collection that is part of the National Postsecondary Student Aid Study (NPSAS) program; program data is available since 1989 at <https://nces.ed.gov/pubsearch/getpubcats.asp?sid=013>. NPSAS:16 (https://nces.ed.gov/surveys/npsas/about.asp) is a cross-sectional survey that is designed to compile a comprehensive research dataset based on student-level records, on financial aid provided by the federal government, the States, postsecondary institutions, employers, and private agencies, along with student demographic and enrollment data. The study was conducted using multiple sources, including institutional records, government databases, and student interviews. Students enrolled in a postsecondary institution were sampled. The data are representative of all undergraduate, graduate, and first-professional students enrolled in postsecondary institutions in the 50 United States, the District of Columbia, and Puerto Rico that were eligible to participate in the federal financial aid programs under Title IV of the Higher Education Act as amended. Key statistics produced from NPSAS:16 are reliable national estimates of characteristics related to financial aid for postsecondary students.",
-            "modified": "2023-06-16T16:49:50.336973",
-            "accessLevel": "public",
-            "identifier": "dc85b2fa-cc1d-429f-b521-6824b423c69b",
-            "dataQuality": true,
-            "issued": "2018-05-15",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
-            "temporal": "2015/2016",
+            "modified": "2023-06-22T18:11:02.343833",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -79122,27 +79080,46 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/pubs/96143.pdf",
+                "https://nces.ed.gov/surveys/pss/zip/LAYOUT_9394.zip",
+                "https://nces.ed.gov/surveys/pss/pdf/quest_9394.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "1993/1994",
+            "title": "Private School Universe Survey, 1993-94"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P4Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tracy Hunt-White",
                 "hasEmail": "mailto:tracy.hunt-white@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The 2015-16 National Postsecondary Student Aid Study (NPSAS:16) is a data collection that is part of the National Postsecondary Student Aid Study (NPSAS) program; program data is available since 1989 at <https://nces.ed.gov/pubsearch/getpubcats.asp?sid=013>. NPSAS:16 (https://nces.ed.gov/surveys/npsas/about.asp) is a cross-sectional survey that is designed to compile a comprehensive research dataset based on student-level records, on financial aid provided by the federal government, the States, postsecondary institutions, employers, and private agencies, along with student demographic and enrollment data. The study was conducted using multiple sources, including institutional records, government databases, and student interviews. Students enrolled in a postsecondary institution were sampled. The data are representative of all undergraduate, graduate, and first-professional students enrolled in postsecondary institutions in the 50 United States, the District of Columbia, and Puerto Rico that were eligible to participate in the federal financial aid programs under Title IV of the Higher Education Act as amended. Key statistics produced from NPSAS:16 are reliable national estimates of characteristics related to financial aid for postsecondary students.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Datalab for Postsecondary Education",
                     "downloadURL": "https://nces.ed.gov/datalab/postsecondary/index.aspx",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Datalab for Postsecondary Education"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "title": "2015-16 National Postsecondary Student Aid Study (NPSAS:16) Restricted-Use Data File",
                     "description": "Restricted-use data file for the 2015-16 National Postsecondary Student Aid Study",
                     "downloadURL": "https://nces.ed.gov/pubsearch/pubsinfo.asp?pubid=2018484",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "2015-16 National Postsecondary Student Aid Study (NPSAS:16) Restricted-Use Data File"
                 }
             ],
+            "identifier": "dc85b2fa-cc1d-429f-b521-6824b423c69b",
+            "issued": "2018-05-15",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "academic-programs",
@@ -79154,33 +79131,14 @@
                 "postsecondary-education",
                 "student-record"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/pubs2018/2018482.pdf",
-                "https://nces.ed.gov/pubs2018/2018482_1.pdf",
-                "https://nces.ed.gov/pubs2018/2018482_2.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Private School Universe Survey, 1999-2000",
-            "description": "The 1999-2000 Private School Universe Survey (PSS 1999-2000) is a study that is part of the Private School Universe program; program data is available since 1989-1990 at <https://nces.ed.gov/surveys/pss/pssdata.asp>. PSS 1999-2000 (https://nces.ed.gov/surveys/pss/) is a cross-sectional survey that collects data on private elementary and secondary schools, including religious orientation, level of school, length of school year, length of school day, total enrollment, race/ethnicity of students, number of high school graduates, number of teachers employed, program emphasis, and existence and type of kindergarten program. The study was conducted using mail questionnaires and telephone follow-up of all private schools in the United States. The PSS includes both schools with a religious orientation (e.g., Catholic, Lutheran, or Jewish) and nonsectarian schools with programs ranging from regular to special emphasis and special education. Key statistics produced from PSS 1999-2000 are on the number of religiously affiliated schools, the number of private high school graduates, and the number of private school students and teachers.",
-            "modified": "2023-06-16T16:45:35.862248",
-            "accessLevel": "public",
-            "identifier": "018b3977-b86a-4a3d-8ce0-eb8ac377c5a3",
-            "dataQuality": true,
-            "issued": "2009-09-02",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "1999/2000",
+            "modified": "2023-06-16T16:49:50.336973",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -79201,51 +79159,71 @@
                     }
                 }
             },
-            "accrualPeriodicity": "R/P2Y",
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Stephen Broughman",
-                "hasEmail": "mailto:stephen.broughman@ed.gov"
-            },
-            "distribution": [
-                {
+            "references": [
+                "https://nces.ed.gov/pubs2018/2018482.pdf",
+                "https://nces.ed.gov/pubs2018/2018482_1.pdf",
+                "https://nces.ed.gov/pubs2018/2018482_2.pdf"
+            ],
+            "spatial": "United States",
+            "systemOfRecords": "https://www2.ed.gov/notices/pai/pai-18-13-01.pdf",
+            "temporal": "2015/2016",
+            "title": "National Postsecondary Student Aid Study, 2015-16"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "accrualPeriodicity": "R/P2Y",
+            "bureauCode": [
+                "018:50"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Stephen Broughman",
+                "hasEmail": "mailto:stephen.broughman@ed.gov"
+            },
+            "dataQuality": true,
+            "description": "The 1999-2000 Private School Universe Survey (PSS 1999-2000) is a study that is part of the Private School Universe program; program data is available since 1989-1990 at <https://nces.ed.gov/surveys/pss/pssdata.asp>. PSS 1999-2000 (https://nces.ed.gov/surveys/pss/) is a cross-sectional survey that collects data on private elementary and secondary schools, including religious orientation, level of school, length of school year, length of school day, total enrollment, race/ethnicity of students, number of high school graduates, number of teachers employed, program emphasis, and existence and type of kindergarten program. The study was conducted using mail questionnaires and telephone follow-up of all private schools in the United States. The PSS includes both schools with a religious orientation (e.g., Catholic, Lutheran, or Jewish) and nonsectarian schools with programs ranging from regular to special emphasis and special education. Key statistics produced from PSS 1999-2000 are on the number of religiously affiliated schools, the number of private high school graduates, and the number of private school students and teachers.",
+            "distribution": [
+                {
                     "@type": "dcat:Distribution",
-                    "title": "Elementary/Secondary Information System",
                     "description": "The Elementary/Secondary Information System (ELSi) is an NCES web application that allows users to quickly view public and private school data and create custom tables and charts using data from the Common Core of Data (CCD) and Private School Survey (PSS)",
                     "downloadURL": "https://nces.ed.gov/ccd/elsi/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Elementary/Secondary Information System"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped TSV",
-                    "title": "TXT_PSS9900.zip",
-                    "description": "1999-2000 Private School Universe Survey data as a zipped TSV file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_9900.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/TXT_PSS9900.zip"
+                    "description": "1999-2000 Private School Universe Survey data as a zipped TSV file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/TXT_PSS9900.zip",
+                    "format": "Zipped TSV",
+                    "mediaType": "application/zip",
+                    "title": "TXT_PSS9900.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS7BDAT",
-                    "title": "PSS9900_SAS7BDAT.zip",
-                    "description": "1999-2000 Private School Universe Survey data as a zipped SAS 7-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_9900.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/PSS9900_SAS7BDAT.zip"
+                    "description": "1999-2000 Private School Universe Survey data as a zipped SAS 7-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/PSS9900_SAS7BDAT.zip",
+                    "format": "Zipped SAS7BDAT",
+                    "mediaType": "application/zip",
+                    "title": "PSS9900_SAS7BDAT.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAV",
-                    "title": "SAV_PSS9900.zip",
-                    "description": "1999-2000 Private School Universe Survey data as a zipped SPSS-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_9900.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/SAV_PSS9900.zip"
+                    "description": "1999-2000 Private School Universe Survey data as a zipped SPSS-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/SAV_PSS9900.zip",
+                    "format": "Zipped SAV",
+                    "mediaType": "application/zip",
+                    "title": "SAV_PSS9900.zip"
                 }
             ],
+            "identifier": "018b3977-b86a-4a3d-8ce0-eb8ac377c5a3",
+            "issued": "2009-09-02",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "church-related-schools",
@@ -79254,33 +79232,14 @@
                 "private-school-graduates",
                 "private-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/pubs2001/2001330.pdf",
-                "https://nces.ed.gov/surveys/pss/zip/LAYOUT_9900.zip",
-                "https://nces.ed.gov/surveys/pss/pdf/quest_9900.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Private School Universe Survey, 1997-98",
-            "description": "The 1997-98 Private School Universe Survey (PSS 1997-98) is a study that is part of the Private School Universe program; program data is available since 1989-1990 at <https://nces.ed.gov/surveys/pss/pssdata.asp>. PSS 1997-98 (https://nces.ed.gov/surveys/pss/) is a cross-sectional survey that collects data on private elementary and secondary schools, including religious orientation, level of school, length of school year, length of school day, total enrollment, race/ethnicity of students, number of high school graduates, number of teachers employed, program emphasis, and existence and type of kindergarten program. The study was conducted using mail questionnaires and telephone follow-up of all private schools in the United States. The PSS includes both schools with a religious orientation (e.g., Catholic, Lutheran, or Jewish) and nonsectarian schools with programs ranging from regular to special emphasis and special education. Key statistics produced from PSS 1997-98 are on the number of religiously affiliated schools, the number of private high school graduates, and the number of private school students and teachers.",
-            "modified": "2023-06-16T16:35:08.215118",
-            "accessLevel": "public",
-            "identifier": "74f064cd-aba3-4e80-b8ef-b18b52b019cc",
-            "dataQuality": true,
-            "issued": "2006-06-28",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "1997/1998",
+            "modified": "2023-06-16T16:45:35.862248",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -79301,51 +79260,70 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/pubs2001/2001330.pdf",
+                "https://nces.ed.gov/surveys/pss/zip/LAYOUT_9900.zip",
+                "https://nces.ed.gov/surveys/pss/pdf/quest_9900.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "1999/2000",
+            "title": "Private School Universe Survey, 1999-2000"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P2Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Broughman",
                 "hasEmail": "mailto:stephen.broughman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The 1997-98 Private School Universe Survey (PSS 1997-98) is a study that is part of the Private School Universe program; program data is available since 1989-1990 at <https://nces.ed.gov/surveys/pss/pssdata.asp>. PSS 1997-98 (https://nces.ed.gov/surveys/pss/) is a cross-sectional survey that collects data on private elementary and secondary schools, including religious orientation, level of school, length of school year, length of school day, total enrollment, race/ethnicity of students, number of high school graduates, number of teachers employed, program emphasis, and existence and type of kindergarten program. The study was conducted using mail questionnaires and telephone follow-up of all private schools in the United States. The PSS includes both schools with a religious orientation (e.g., Catholic, Lutheran, or Jewish) and nonsectarian schools with programs ranging from regular to special emphasis and special education. Key statistics produced from PSS 1997-98 are on the number of religiously affiliated schools, the number of private high school graduates, and the number of private school students and teachers.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Elementary/Secondary Information System",
                     "description": "The Elementary/Secondary Information System (ELSi) is an NCES web application that allows users to quickly view public and private school data and create custom tables and charts using data from the Common Core of Data (CCD) and Private School Survey (PSS)",
                     "downloadURL": "https://nces.ed.gov/ccd/elsi/",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Elementary/Secondary Information System"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped TSV",
-                    "title": "TXT_PSS9798.zip",
-                    "description": "1997-98 Private School Universe Survey data as a zipped TSV file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_9798.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/TXT_PSS9798.zip"
+                    "description": "1997-98 Private School Universe Survey data as a zipped TSV file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/TXT_PSS9798.zip",
+                    "format": "Zipped TSV",
+                    "mediaType": "application/zip",
+                    "title": "TXT_PSS9798.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS7BDAT",
-                    "title": "PSS9798_SAS7BDAT.zip",
-                    "description": "1997-98 Private School Universe Survey data as a zipped SAS 7-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_9798.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/PSS9798_SAS7BDAT.zip"
+                    "description": "1997-98 Private School Universe Survey data as a zipped SAS 7-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/PSS9798_SAS7BDAT.zip",
+                    "format": "Zipped SAS7BDAT",
+                    "mediaType": "application/zip",
+                    "title": "PSS9798_SAS7BDAT.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAV",
-                    "title": "SAV_PSS9798.zip",
-                    "description": "1997-98 Private School Universe Survey data as a zipped SPSS-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_9798.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/SAV_PSS9798.zip"
+                    "description": "1997-98 Private School Universe Survey data as a zipped SPSS-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/SAV_PSS9798.zip",
+                    "format": "Zipped SAV",
+                    "mediaType": "application/zip",
+                    "title": "SAV_PSS9798.zip"
                 }
             ],
+            "identifier": "74f064cd-aba3-4e80-b8ef-b18b52b019cc",
+            "issued": "2006-06-28",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "church-related-schools",
@@ -79354,33 +79332,14 @@
                 "private-school-graduates",
                 "private-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
-            ],
-            "programCode": [
-                "018:000"
-            ],
             "language": [
                 "en-US"
             ],
-            "references": [
-                "https://nces.ed.gov/pubs99/1999319.pdf",
-                "https://nces.ed.gov/surveys/pss/zip/LAYOUT_9798.zip",
-                "https://nces.ed.gov/surveys/pss/pdf/quest_9798.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Private School Universe Survey, 1995-96",
-            "description": "The 1995 Private School Universe Survey (PSS 1995) is a study that is part of the Private School Universe program; program data is available since 1989-1990 at <https://nces.ed.gov/surveys/pss/pssdata.asp>. PSS 1995 (https://nces.ed.gov/surveys/pss/) is a cross-sectional survey that collects data on private elementary and secondary schools, including religious orientation, level of school, length of school year, length of school day, total enrollment, race/ethnicity of students, number of high school graduates, number of teachers employed, program emphasis, and existence and type of kindergarten program. The study was conducted using mail questionnaires and telephone follow-up of all private schools in the United States. The PSS includes both schools with a religious orientation (e.g., Catholic, Lutheran, or Jewish) and nonsectarian schools with programs ranging from regular to special emphasis and special education. Key statistics produced from PSS 1995-96 are on the number of religiously affiliated schools, the number of private high school graduates, and the number of private school students and teachers.",
-            "modified": "2023-06-16T16:32:20.715879",
-            "accessLevel": "public",
-            "identifier": "0727e76e-6f2a-4e25-b30c-7469f14d4805",
-            "dataQuality": true,
-            "issued": "1996-03-25",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "temporal": "1995/1996",
+            "modified": "2023-06-16T16:35:08.215118",
+            "programCode": [
+                "018:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "National Center for Education Statistics (NCES)",
@@ -79401,44 +79360,63 @@
                     }
                 }
             },
+            "references": [
+                "https://nces.ed.gov/pubs99/1999319.pdf",
+                "https://nces.ed.gov/surveys/pss/zip/LAYOUT_9798.zip",
+                "https://nces.ed.gov/surveys/pss/pdf/quest_9798.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "1997/1998",
+            "title": "Private School Universe Survey, 1997-98"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P2Y",
+            "bureauCode": [
+                "018:50"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Stephen Broughman",
                 "hasEmail": "mailto:stephen.broughman@ed.gov"
             },
+            "dataQuality": true,
+            "description": "The 1995 Private School Universe Survey (PSS 1995) is a study that is part of the Private School Universe program; program data is available since 1989-1990 at <https://nces.ed.gov/surveys/pss/pssdata.asp>. PSS 1995 (https://nces.ed.gov/surveys/pss/) is a cross-sectional survey that collects data on private elementary and secondary schools, including religious orientation, level of school, length of school year, length of school day, total enrollment, race/ethnicity of students, number of high school graduates, number of teachers employed, program emphasis, and existence and type of kindergarten program. The study was conducted using mail questionnaires and telephone follow-up of all private schools in the United States. The PSS includes both schools with a religious orientation (e.g., Catholic, Lutheran, or Jewish) and nonsectarian schools with programs ranging from regular to special emphasis and special education. Key statistics produced from PSS 1995-96 are on the number of religiously affiliated schools, the number of private high school graduates, and the number of private school students and teachers.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped TSV",
-                    "title": "TXT_PSS9596.zip",
-                    "description": "1995-96 Private School Universe Survey data as a zipped TSV file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_9596.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/TXT_PSS9596.zip"
+                    "description": "1995-96 Private School Universe Survey data as a zipped TSV file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/TXT_PSS9596.zip",
+                    "format": "Zipped TSV",
+                    "mediaType": "application/zip",
+                    "title": "TXT_PSS9596.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAS7BDAT",
-                    "title": "PSS9596_SAS7BDAT.zip",
-                    "description": "1995-96 Private School Universe Survey data as a zipped SAS 7-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_9596.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/PSS9596_SAS7BDAT.zip"
+                    "description": "1995-96 Private School Universe Survey data as a zipped SAS 7-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/PSS9596_SAS7BDAT.zip",
+                    "format": "Zipped SAS7BDAT",
+                    "mediaType": "application/zip",
+                    "title": "PSS9596_SAS7BDAT.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/zip",
-                    "format": "Zipped SAV",
-                    "title": "SAV_PSS9596.zip",
-                    "description": "1995-96 Private School Universe Survey data as a zipped SPSS-formatted binary data file",
                     "describedBy": "https://nces.ed.gov/surveys/pss/pdf/CODEBOOK_9596.pdf",
                     "describedByType": "application/pdf",
-                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/SAV_PSS9596.zip"
+                    "description": "1995-96 Private School Universe Survey data as a zipped SPSS-formatted binary data file",
+                    "downloadURL": "https://nces.ed.gov/surveys/pss/zip/SAV_PSS9596.zip",
+                    "format": "Zipped SAV",
+                    "mediaType": "application/zip",
+                    "title": "SAV_PSS9596.zip"
                 }
             ],
+            "identifier": "0727e76e-6f2a-4e25-b30c-7469f14d4805",
+            "issued": "1996-03-25",
             "keyword": [
                 "0ee4621b-38be-46bb-8360-219726022a58",
                 "church-related-schools",
@@ -79447,39 +79425,20 @@
                 "private-school-graduates",
                 "private-schools"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:50"
+            "language": [
+                "en-US"
             ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-16T16:32:20.715879",
             "programCode": [
                 "018:000"
             ],
-            "language": [
-                "en-US"
-            ],
-            "references": [
-                "https://nces.ed.gov/pubs98/98229.pdf",
-                "https://nces.ed.gov/surveys/pss/zip/LAYOUT_9596.zip",
-                "https://nces.ed.gov/surveys/pss/pdf/quest_9596.pdf"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Title I Part C Performance, Participation, and Funding Data",
-            "description": "Performance, participation, and funding data related to Title I, Part C (Migratory students). Data  from SY 2010-11 onward.",
-            "modified": "2023-06-08T11:57:03.895551",
-            "accessLevel": "public",
-            "identifier": "9fad21b2-2344-4fd9-8c82-a8ee8d4948e4",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Advisory Committee on Student Financial Assistance (ACSFA)",
-                "subOrganizationOf": {
-                    "@type": "org:Organization",
-                    "name": "Office of Federal Student Aid (FSA)",
+                "name": "National Center for Education Statistics (NCES)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
-                        "name": "Office of the Under Secretary (OUS)",
+                    "name": "Institute of Education Sciences (IES)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -79493,32 +79452,48 @@
                         }
                     }
                 }
-                }
             },
+            "references": [
+                "https://nces.ed.gov/pubs98/98229.pdf",
+                "https://nces.ed.gov/surveys/pss/zip/LAYOUT_9596.zip",
+                "https://nces.ed.gov/surveys/pss/pdf/quest_9596.pdf"
+            ],
+            "spatial": "United States",
+            "temporal": "1995/1996",
+            "title": "Private School Universe Survey, 1995-96"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:45"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Office of Elementary and Secondary Education",
                 "hasEmail": "mailto:eddataexpress@ed.gov"
             },
+            "description": "Performance, participation, and funding data related to Title I, Part C (Migratory students). Data  from SY 2010-11 onward.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "HTML",
-                    "title": "Title I Part C Data Dashboards",
                     "description": "Dashboard presentation of data representing gap in performance between migratory students and all students, participation, and funding.  Data  from SY 2010-11 onward.",
                     "downloadURL": "https://eddataexpress.ed.gov/dashboard/mep?sy=147",
-                    "mediaType": "text/plain"
+                    "format": "HTML",
+                    "mediaType": "text/plain",
+                    "title": "Title I Part C Data Dashboards"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "HTML",
-                    "title": "Title I Part C Participation Data",
                     "description": "Participation data of migratory students in states that receive Title I, Part C funding. Data  from SY 2010-11 onward available for download.",
                     "downloadURL": "https://eddataexpress.ed.gov/download?f%5B0%5D=program%3ATitle%20I%2C%20Part%20C",
-                    "mediaType": "text/plain"
+                    "format": "HTML",
+                    "mediaType": "text/plain",
+                    "title": "Title I Part C Participation Data"
                 }
             ],
+            "identifier": "9fad21b2-2344-4fd9-8c82-a8ee8d4948e4",
             "keyword": [
                 "edfacts",
                 "elementary",
@@ -79528,21 +79503,11 @@
                 "secondary",
                 "state"
             ],
-            "bureauCode": [
-                "018:45"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2023-06-08T11:57:03.895551",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "McKinney-Vento Act Performance, Participation, and Funding Data",
-            "description": "Participation, status, and funding data on homeless student enrollment.   Data from 2011-12 onward",
-            "modified": "2023-06-08T11:54:49.750587",
-            "accessLevel": "public",
-            "identifier": "1345239b-5bb0-4f4b-a3ab-ae8855070505",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Advisory Committee on Student Financial Assistance (ACSFA)",
@@ -79567,38 +79532,48 @@
                     }
                 }
             },
+            "title": "Title I Part C Performance, Participation, and Funding Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:45"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Office of Elementary and Secondary Education",
                 "hasEmail": "mailto:eddataexpress@ed.gov"
             },
+            "description": "Participation, status, and funding data on homeless student enrollment.   Data from 2011-12 onward",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "HTML",
-                    "title": "McKinney-Vento Act Data Dashboard",
                     "description": "Dashboard presentation of participation, status, and funding data on homeless student enrollment.   Data from 2011-12 onward",
                     "downloadURL": "https://eddataexpress.ed.gov/dashboard/homeless",
-                    "mediaType": "text/plain"
+                    "format": "HTML",
+                    "mediaType": "text/plain",
+                    "title": "McKinney-Vento Act Data Dashboard"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "HTML",
-                    "title": "McKinney-Vento Act Participation Data",
                     "description": "Participation data on homeless student enrollment. Data from 2011-12 onward available for download.",
                     "downloadURL": "https://eddataexpress.ed.gov/download?f%5B0%5D=program%3AMcKinney-Vento%20Act&f%5B3%5D=type_of_data%3AParticipation",
-                    "mediaType": "text/plain"
+                    "format": "HTML",
+                    "mediaType": "text/plain",
+                    "title": "McKinney-Vento Act Participation Data"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "HTML",
-                    "title": "McKinney-Vento Act Status Data",
                     "description": "Status data on homeless student enrollment.  Data from 2011-12 onward available for download.",
                     "downloadURL": "https://eddataexpress.ed.gov/download?f%5B0%5D=program%3AMcKinney-Vento%20Act&f%5B3%5D=type_of_data%3AStatus",
-                    "mediaType": "text/plain"
+                    "format": "HTML",
+                    "mediaType": "text/plain",
+                    "title": "McKinney-Vento Act Status Data"
                 }
             ],
+            "identifier": "1345239b-5bb0-4f4b-a3ab-ae8855070505",
             "keyword": [
                 "district",
                 "edfacts",
@@ -79611,22 +79586,15 @@
                 "secondary",
                 "state"
             ],
-            "bureauCode": [
-                "018:45"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            "modified": "2023-06-08T11:54:49.750587",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Default Rates",
-            "description": "Cohort default rates for the\u00a0federal student loan\u00a0programs and quarterly\u00a0new defaults.",
-            "modified": "2023-06-08T11:47:03.763582",
-            "accessLevel": "public",
-            "identifier": "3d0071fe-75d8-403f-be79-61409b80de5e",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
+            ],
             "publisher": {
+                "@type": "org:Organization",
+                "name": "Advisory Committee on Student Financial Assistance (ACSFA)",
+                "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Office of Federal Student Aid (FSA)",
                     "subOrganizationOf": {
@@ -79645,22 +79613,33 @@
                             }
                         }
                     }
+                }
             },
+            "title": "McKinney-Vento Act Performance, Participation, and Funding Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1D",
+            "bureauCode": [
+                "018:45"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tara Marini",
                 "hasEmail": "mailto:tara.marini@ed.gov"
             },
+            "description": "Cohort default rates for the\u00a0federal student loan\u00a0programs and quarterly\u00a0new defaults.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "title": "Default Rate Report Links",
                     "description": "The reports are: Cohort Default Rates by school, lender, state and institution type,  Budget Lifetime and Cumulative Lifetime Default Rates,  New Direct Loan Defaults, and Default Recoveries by Private Collection Agency.",
                     "downloadURL": "https://studentaid.gov/data-center/student/default",
-                    "mediaType": "text/plain"
+                    "mediaType": "text/plain",
+                    "title": "Default Rate Report Links"
                 }
             ],
+            "identifier": "3d0071fe-75d8-403f-be79-61409b80de5e",
             "keyword": [
                 "cohort",
                 "default rates",
@@ -79668,25 +79647,17 @@
                 "loans",
                 "student loans"
             ],
-            "spatial": "United States",
-            "bureauCode": [
-                "018:45"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2023-06-08T11:47:03.763582",
             "programCode": [
                 "018:000"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Title I Part D Performance, Participation, and Funding Data",
-            "description": "Data related to Title I, Part D performance, participation, and funding.  Data from SY 2010-11 onward.",
-            "modified": "2023-06-08T11:46:07.893030",
-            "accessLevel": "public",
-            "identifier": "768d631c-36e4-47c2-90ca-525f62a2c2f6",
-            "license": "http://www.opendefinition.org/licenses/cc-by",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Elementary and Secondary Education (OESE)",
+                "name": "Office of Federal Student Aid (FSA)",
+                "subOrganizationOf": {
+                    "@type": "org:Organization",
+                    "name": "Office of the Under Secretary (OUS)",
                     "subOrganizationOf": {
                         "@type": "org:Organization",
                         "name": "Office of the Secretary (OS)",
@@ -79699,43 +79670,55 @@
                             }
                         }
                     }
+                }
+            },
+            "spatial": "United States",
+            "title": "Default Rates"
         },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:10"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Office of Elementary and Secondary Education",
                 "hasEmail": "mailto:eddataexpress@ed.gov"
             },
+            "description": "Data related to Title I, Part D performance, participation, and funding.  Data from SY 2010-11 onward.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://eddataexpress.ed.gov/dashboard/title-i-part-d-subpart-1?sy=2304",
+                    "description": "Dashboard presentation of participation, performance, and funding for Title I, Part D, Subpart I.  Data from SY 2010-11 onward.",
                     "format": "HTML",
-                    "title": "Title I Part D, Subpart 1 Data Dashboard",
-                    "description": "Dashboard presentation of participation, performance, and funding for Title I, Part D, Subpart I.  Data from SY 2010-11 onward."
+                    "title": "Title I Part D, Subpart 1 Data Dashboard"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://eddataexpress.ed.gov/dashboard/title-i-part-d-subpart-2",
+                    "description": "Dashboard presentation of participation, performance, and funding data for Title I, Part D, Subpart 2.  Data from SY 2010-11 onward.",
                     "format": "HTML",
-                    "title": "Title 1, Part D, Subpart 2 Data Dashboard",
-                    "description": "Dashboard presentation of participation, performance, and funding data for Title I, Part D, Subpart 2.  Data from SY 2010-11 onward."
+                    "title": "Title 1, Part D, Subpart 2 Data Dashboard"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://eddataexpress.ed.gov/download?f%5B0%5D=program%3ATitle%20I%2C%20Part%20D&f%5B1%5D=type_of_data%3AParticipation",
+                    "description": "Participation data for Title I, Part D. Data from SY 2010-11 onward available for download.",
                     "format": "HTML",
-                    "title": "Title 1, Part D Participation Data",
-                    "description": "Participation data for Title I, Part D. Data from SY 2010-11 onward available for download."
+                    "title": "Title 1, Part D Participation Data"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://eddataexpress.ed.gov/download?f%5B0%5D=program%3ATitle%20I%2C%20Part%20D&f%5B1%5D=type_of_data%3APerformance",
+                    "description": "Performance data for Title I, Part D. Data from SY 2010-11 onward available for download.",
                     "format": "HTML",
-                    "title": "Title 1, Part D Performance Data",
-                    "description": "Performance data for Title I, Part D. Data from SY 2010-11 onward available for download."
+                    "title": "Title 1, Part D Performance Data"
                 }
             ],
+            "identifier": "768d631c-36e4-47c2-90ca-525f62a2c2f6",
             "keyword": [
                 "district",
                 "edfacts",
@@ -79746,24 +79729,14 @@
                 "secondary",
                 "state"
             ],
-            "bureauCode": [
-                "018:10"
-            ],
+            "license": "http://www.opendefinition.org/licenses/cc-by",
+            "modified": "2023-06-08T11:46:07.893030",
             "programCode": [
                 "018:010"
-            ]
-        },
-        {
-            "@type": "dcat:Dataset",
-            "title": "Part B State Performance Plans (SPP) and Annual Performance Report (APR)",
-            "description": "This site offers links to the data and additional information related to the Individuals with Disabilities Education Act (IDEA) Part B state performance plan/annual performance reports (SPP/APR). IDEA requires each state to develop an SPP/APR that evaluates the state\u2019s efforts to implement the requirements and purposes of the IDEA and describes how the state will improve its implementation. The SPP/APRs include indicators that measure child and family outcomes and other indicators that measure compliance with the requirements of the IDEA.\r\n\r\nIn addition, each state reports annually to the public on the performance of each of its local educational agencies according to the targets in its SPP. The state also reports annually to the Secretary on its performance in meeting its SPP targets. This report is called the Part B Annual Performance Report (APR), this report must also be posted on the state's website.\r\n\r\nThe Office of Special Education Programs' (OSEP) responses to the states' SPP and APRs are posted on this page as letters are issued.\r\n\r\nPrior to December 2005, OSEP required the submission of Annual Performance Reports under 34 CFR 80.40. OSEP required states to submit Part C APRs in July 2003, and both Part B and Part C APRs on March 31, 2004. OSEP responses to those submissions are included below.\r\n\r\nPlease note: Office of Special Education Programs Monitoring and State Improvement Planning Division 550 12th Street, SW Washington, DC 20202-2600 Telephone: 202-245-7584\r\n\r\nIf a state is not listed on this page, no data is available at this time.",
-            "modified": "2023-06-06T20:28:37.182407",
-            "accessLevel": "public",
-            "identifier": "c2391fd1-5835-47fe-8466-0369f11df52e",
-            "license": "http://www.opendefinition.org/licenses/cc-zero",
+            ],
             "publisher": {
                 "@type": "org:Organization",
-                "name": "Office of Special Education and Rehabilitative Services (OSERS)",
+                "name": "Office of Elementary and Secondary Education (OESE)",
                 "subOrganizationOf": {
                     "@type": "org:Organization",
                     "name": "Office of the Secretary (OS)",
@@ -79777,972 +79750,982 @@
                     }
                 }
             },
+            "title": "Title I Part D Performance, Participation, and Funding Data"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
             "accrualPeriodicity": "R/P1Y",
+            "bureauCode": [
+                "018:20"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Office of Special Education (OSEP), Monitoring and State Improvement Planning (MSIP) Division",
                 "hasEmail": "mailto:osers@ed.gov"
             },
+            "description": "This site offers links to the data and additional information related to the Individuals with Disabilities Education Act (IDEA) Part B state performance plan/annual performance reports (SPP/APR). IDEA requires each state to develop an SPP/APR that evaluates the state\u2019s efforts to implement the requirements and purposes of the IDEA and describes how the state will improve its implementation. The SPP/APRs include indicators that measure child and family outcomes and other indicators that measure compliance with the requirements of the IDEA.\r\n\r\nIn addition, each state reports annually to the public on the performance of each of its local educational agencies according to the targets in its SPP. The state also reports annually to the Secretary on its performance in meeting its SPP targets. This report is called the Part B Annual Performance Report (APR), this report must also be posted on the state's website.\r\n\r\nThe Office of Special Education Programs' (OSEP) responses to the states' SPP and APRs are posted on this page as letters are issued.\r\n\r\nPrior to December 2005, OSEP required the submission of Annual Performance Reports under 34 CFR 80.40. OSEP required states to submit Part C APRs in July 2003, and both Part B and Part C APRs on March 31, 2004. OSEP responses to those submissions are included below.\r\n\r\nPlease note: Office of Special Education Programs Monitoring and State Improvement Planning Division 550 12th Street, SW Washington, DC 20202-2600 Telephone: 202-245-7584\r\n\r\nIf a state is not listed on this page, no data is available at this time.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "OSEP Response to SPP/APR: ALABAMA 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/d417640f-b2b5-4c5e-a00b-d0158e2495e9/download/alabama-resultsmatrix-2014b.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/d417640f-b2b5-4c5e-a00b-d0158e2495e9/download/alabama-resultsmatrix-2014b.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "OSEP Response to SPP/APR: ALABAMA 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "OSEP Response to SPP/APR ALABAMA 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/173206b4-bccd-4028-885a-afee52588d8f/download/alabama-matrix-2013b.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/173206b4-bccd-4028-885a-afee52588d8f/download/alabama-matrix-2013b.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "OSEP Response to SPP/APR ALABAMA 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR ALASKA 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/b574142b-08df-47e5-a29e-4fb97bf22f9f/download/alaska-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/b574142b-08df-47e5-a29e-4fb97bf22f9f/download/alaska-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR ALASKA 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "OSEP Response to SPP/APR ALASKA 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/7d33a849-4e99-43b2-b3e5-139ea6267a88/download/alaska-matrix-2013b.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/7d33a849-4e99-43b2-b3e5-139ea6267a88/download/alaska-matrix-2013b.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "OSEP Response to SPP/APR ALASKA 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR AMERICAN SAMOA 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/b53e246c-e760-4074-990d-c21e2281c3e9/download/american-samoa-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/b53e246c-e760-4074-990d-c21e2281c3e9/download/american-samoa-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR AMERICAN SAMOA 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR AMERICAN SAMOA 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/09f115f5-75c2-409a-808a-1016a74e6be8/download/american-samoa-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/09f115f5-75c2-409a-808a-1016a74e6be8/download/american-samoa-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR AMERICAN SAMOA 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR ARIZONA 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/3ffa7b4d-c6ba-40fb-9e7f-c19bb98f2794/download/arizona-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/3ffa7b4d-c6ba-40fb-9e7f-c19bb98f2794/download/arizona-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR ARIZONA 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "OSEP Response to SPP/APR ARIZONA 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/048ec9c8-cb2e-4a5a-920d-9baa43a36df5/download/arizona-matrix-2013b.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/048ec9c8-cb2e-4a5a-920d-9baa43a36df5/download/arizona-matrix-2013b.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "OSEP Response to SPP/APR ARIZONA 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR ARKANSAS 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/c48b8c0a-9f7a-447c-8357-66b7e38cfd5e/download/arkansas-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/c48b8c0a-9f7a-447c-8357-66b7e38cfd5e/download/arkansas-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR ARKANSAS 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR ARKANSAS 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/90c2b3e1-3eef-42b8-b4b1-d9cfdd38af77/download/arkansas-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/90c2b3e1-3eef-42b8-b4b1-d9cfdd38af77/download/arkansas-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR ARKANSAS 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR BIE 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/3212728f-9451-4ed1-82bc-58cddc2dcd0d/download/bie-matrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/3212728f-9451-4ed1-82bc-58cddc2dcd0d/download/bie-matrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR BIE 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR BIE 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/57041a40-52b4-4b3e-9a8e-09c391e51da1/download/bie-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/57041a40-52b4-4b3e-9a8e-09c391e51da1/download/bie-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR BIE 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR CALIFORNIA 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/bb0f58fc-be08-40bf-8200-0b11c6c4dd04/download/california-resultsmatrix-2014b-revised.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/bb0f58fc-be08-40bf-8200-0b11c6c4dd04/download/california-resultsmatrix-2014b-revised.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR CALIFORNIA 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR CALIFORNIA 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/4d6c0ebf-8781-4577-9a28-ec0f766db829/download/california-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/4d6c0ebf-8781-4577-9a28-ec0f766db829/download/california-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR CALIFORNIA 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR COLORADO 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/88fb4530-b346-4296-b58e-7524ea2f4ecb/download/colorado-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/88fb4530-b346-4296-b58e-7524ea2f4ecb/download/colorado-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR COLORADO 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR COLORADO 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/45624625-2f5d-4d57-af9a-5f8df937379d/download/colorado-co-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/45624625-2f5d-4d57-af9a-5f8df937379d/download/colorado-co-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR COLORADO 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR CONNECTICUT 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/84edf70f-1fd5-4fb0-bfbd-1196d3b2cb57/download/connecticut-ct-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/84edf70f-1fd5-4fb0-bfbd-1196d3b2cb57/download/connecticut-ct-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR CONNECTICUT 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.ms-excel",
-                    "format": "XLS",
-                    "title": "OSEP Response to SPP/APR CONNECTICUT 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/0057a16f-d4be-48a9-9510-25e527298d39/download/connecticut-ct-matrix-2013b.xls"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/0057a16f-d4be-48a9-9510-25e527298d39/download/connecticut-ct-matrix-2013b.xls",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "OSEP Response to SPP/APR CONNECTICUT 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR DC 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/a61a8d35-6f60-4cbe-99a3-63e5751c45e8/download/district-of-columbia-dc-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/a61a8d35-6f60-4cbe-99a3-63e5751c45e8/download/district-of-columbia-dc-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR DC 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR DC 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/92faeb3a-87d4-4b90-af62-f88d963c8a84/download/district-of-columbia-dc-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/92faeb3a-87d4-4b90-af62-f88d963c8a84/download/district-of-columbia-dc-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR DC 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR DELAWARE 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/3bd0fc0d-b256-4a22-a633-99919a82e1d4/download/delaware-de-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/3bd0fc0d-b256-4a22-a633-99919a82e1d4/download/delaware-de-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR DELAWARE 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR DELAWARE 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/a7398c20-6f16-4822-b85f-fb2859219fe2/download/delaware-de-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/a7398c20-6f16-4822-b85f-fb2859219fe2/download/delaware-de-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR DELAWARE 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR FSM 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/e48cfc38-dc19-4f8f-a19c-c9aaca059b45/download/federated-states-of-micronesia-fsm-matrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/e48cfc38-dc19-4f8f-a19c-c9aaca059b45/download/federated-states-of-micronesia-fsm-matrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR FSM 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR FSM 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/3c72e882-bdda-428e-b342-fdcbb1e89de4/download/federated-states-of-micronesia-fsm-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/3c72e882-bdda-428e-b342-fdcbb1e89de4/download/federated-states-of-micronesia-fsm-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR FSM 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR FLORIDA 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/4ab66099-5a15-467c-9504-1b9a46a3ca30/download/florida-fl-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/4ab66099-5a15-467c-9504-1b9a46a3ca30/download/florida-fl-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR FLORIDA 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR FLORIDA 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/844dc977-cc97-41b0-a02a-15e6f5cd4527/download/florida-fl-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/844dc977-cc97-41b0-a02a-15e6f5cd4527/download/florida-fl-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR FLORIDA 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR GEORGIA 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/7cb743fb-9849-4ec9-a74d-49f982d5d074/download/georgia-ga-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/7cb743fb-9849-4ec9-a74d-49f982d5d074/download/georgia-ga-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR GEORGIA 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR: GEORGIA 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/5c4f8982-bc67-435d-b994-36c543d41294/download/georgia-ga-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/5c4f8982-bc67-435d-b994-36c543d41294/download/georgia-ga-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR: GEORGIA 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR: GUAM 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/490d4f3e-9716-4601-a35e-fb6f03520496/download/guam-gu-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/490d4f3e-9716-4601-a35e-fb6f03520496/download/guam-gu-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR: GUAM 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR: GUAM 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/d27d35dc-3e12-46b4-b874-71739640eea0/download/guam-gu-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/d27d35dc-3e12-46b4-b874-71739640eea0/download/guam-gu-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR: GUAM 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR: HAWAII 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/73741890-b06f-4472-943c-d1f02deceeba/download/hawaii-hi-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/73741890-b06f-4472-943c-d1f02deceeba/download/hawaii-hi-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR: HAWAII 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR HAWAII 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/08597be6-9016-4e80-bcfa-74ae302e669c/download/hawaii-hi-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/08597be6-9016-4e80-bcfa-74ae302e669c/download/hawaii-hi-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR HAWAII 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR IDAHO 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/d0eefa14-5a8d-4f6e-93d9-0341afee26a5/download/idaho-id-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/d0eefa14-5a8d-4f6e-93d9-0341afee26a5/download/idaho-id-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR IDAHO 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR IDAHO 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/03d37372-430d-495e-a152-4adaa6471778/download/idaho-id-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/03d37372-430d-495e-a152-4adaa6471778/download/idaho-id-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR IDAHO 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR: ILLINOIS 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/713805b8-1a8c-48bc-98c6-0597ca4778b9/download/illinois-il-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/713805b8-1a8c-48bc-98c6-0597ca4778b9/download/illinois-il-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR: ILLINOIS 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR ILLINOIS 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/8cae2205-06eb-42a6-b300-6099fc3fe37b/download/illinois-il-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/8cae2205-06eb-42a6-b300-6099fc3fe37b/download/illinois-il-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR ILLINOIS 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR INDIANA 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/70593a49-0d17-4146-bf64-69676c1a196c/download/indiana-in-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/70593a49-0d17-4146-bf64-69676c1a196c/download/indiana-in-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR INDIANA 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR INDIANA 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/8cd49c82-02d6-497a-af5a-d9cc9d0458b1/download/indiana-in-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/8cd49c82-02d6-497a-af5a-d9cc9d0458b1/download/indiana-in-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR INDIANA 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR IOWA 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/d8e519a3-ddb6-412d-b3f6-afed6740fd49/download/iowa-ia-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/d8e519a3-ddb6-412d-b3f6-afed6740fd49/download/iowa-ia-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR IOWA 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR IOWA 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/612b46a8-9fb1-4e12-ade2-dda9da0f795f/download/iowa-ia-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/612b46a8-9fb1-4e12-ade2-dda9da0f795f/download/iowa-ia-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR IOWA 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR KANSAS 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/9360bfef-4021-47fd-af29-c0aa8b62da3d/download/kansas-ks-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/9360bfef-4021-47fd-af29-c0aa8b62da3d/download/kansas-ks-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR KANSAS 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR KANSAS 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/9d34e8f2-b2fc-4f23-bb9b-9ad467911712/download/kansas-ks-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/9d34e8f2-b2fc-4f23-bb9b-9ad467911712/download/kansas-ks-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR KANSAS 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR KENTUCKY 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/03ff3eaf-8609-4e90-bb2f-29a5bb229143/download/kentucky-ky-resultsmatrix-2014b-revised.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/03ff3eaf-8609-4e90-bb2f-29a5bb229143/download/kentucky-ky-resultsmatrix-2014b-revised.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR KENTUCKY 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR KENTUCKY 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/92bcb937-5af6-49c5-b647-afc702010474/download/kentucky-ky-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/92bcb937-5af6-49c5-b647-afc702010474/download/kentucky-ky-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR KENTUCKY 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR: LOUISIANA 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/334759ed-f7a7-4e30-afcc-1a4201c5d9b2/download/louisiana-la-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/334759ed-f7a7-4e30-afcc-1a4201c5d9b2/download/louisiana-la-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR: LOUISIANA 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR LOUISIANA 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/f7b44c84-6a2f-4ede-8586-aef23e6e81f1/download/louisiana-la-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/f7b44c84-6a2f-4ede-8586-aef23e6e81f1/download/louisiana-la-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR LOUISIANA 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR: MAINE 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/15b13776-5551-4dcc-884a-38fabecc2931/download/maine-me-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/15b13776-5551-4dcc-884a-38fabecc2931/download/maine-me-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR: MAINE 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR MAINE 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/b1183a50-43f1-4b1e-aefa-1c865fe1de8b/download/maine-me-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/b1183a50-43f1-4b1e-aefa-1c865fe1de8b/download/maine-me-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR MAINE 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR MARSHALL ISLANDS 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/b029792f-a8ab-4030-87e7-64fa4c3f1b84/download/marshall-islands-mh-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/b029792f-a8ab-4030-87e7-64fa4c3f1b84/download/marshall-islands-mh-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR MARSHALL ISLANDS 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR MARSHALL ISLANDS 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/1379fa91-5c11-44ec-848b-8cc490e11a0d/download/marshall-islands-mh-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/1379fa91-5c11-44ec-848b-8cc490e11a0d/download/marshall-islands-mh-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR MARSHALL ISLANDS 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR MARYLAND 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/1ae15c64-c781-46a1-ab9c-72865af47e95/download/maryland-md-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/1ae15c64-c781-46a1-ab9c-72865af47e95/download/maryland-md-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR MARYLAND 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR MARYLAND 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/a5e980c9-cae9-44cf-b1be-0eb231c67886/download/maryland-md-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/a5e980c9-cae9-44cf-b1be-0eb231c67886/download/maryland-md-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR MARYLAND 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR MASSACHUSETTS 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/c5c7f20b-8d9e-4e47-b841-5698938bc959/download/massachusetts-ma-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/c5c7f20b-8d9e-4e47-b841-5698938bc959/download/massachusetts-ma-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR MASSACHUSETTS 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR MASSACHUSETTS 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/4d8ad4f9-12fb-4d3d-ac5b-ab3f12015f34/download/massachusetts-ma-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/4d8ad4f9-12fb-4d3d-ac5b-ab3f12015f34/download/massachusetts-ma-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR MASSACHUSETTS 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR MICHIGAN 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/9dbdb7ff-b89e-4b55-99ad-88bf31cdc72f/download/michigan-mi-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/9dbdb7ff-b89e-4b55-99ad-88bf31cdc72f/download/michigan-mi-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR MICHIGAN 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR MICHIGAN 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/b74ce60d-88d7-454c-ad38-1bb4cd6ae060/download/michigan-mi-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/b74ce60d-88d7-454c-ad38-1bb4cd6ae060/download/michigan-mi-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR MICHIGAN 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR: MINNESOTA 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/8b83a1ae-af4e-45fb-832c-b9e3c86f5868/download/minnesota-mn-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/8b83a1ae-af4e-45fb-832c-b9e3c86f5868/download/minnesota-mn-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR: MINNESOTA 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR MINNESOTA 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/1f87475d-251d-45b9-a7ac-6ef53943a7eb/download/minnesota-mn-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/1f87475d-251d-45b9-a7ac-6ef53943a7eb/download/minnesota-mn-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR MINNESOTA 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR: MISSISSIPPI 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/cd0f4de8-88b7-4164-bcda-6c486654ea33/download/mississippi-ms-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/cd0f4de8-88b7-4164-bcda-6c486654ea33/download/mississippi-ms-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR: MISSISSIPPI 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR MISSISSIPPI 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/a91a1455-8a76-42e7-814d-dc64ecb1c9ca/download/mississippi-ms-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/a91a1455-8a76-42e7-814d-dc64ecb1c9ca/download/mississippi-ms-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR MISSISSIPPI 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR MISSOURI 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/c46e655c-65d4-4c40-a365-e58d6ebfae25/download/missouri-mo-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/c46e655c-65d4-4c40-a365-e58d6ebfae25/download/missouri-mo-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR MISSOURI 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR MISSOURI 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/51d2ffab-9588-47cc-a155-651589c323af/download/missouri-mo-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/51d2ffab-9588-47cc-a155-651589c323af/download/missouri-mo-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR MISSOURI 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR MONTANA 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/6c3042f6-e1c2-4c59-986a-a678db1c8b85/download/montana-mt-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/6c3042f6-e1c2-4c59-986a-a678db1c8b85/download/montana-mt-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR MONTANA 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR MONTANA 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/86851a57-5443-4550-ae14-da939c834eab/download/montana-mt-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/86851a57-5443-4550-ae14-da939c834eab/download/montana-mt-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR MONTANA 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR NEBRASKA 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/408d9333-3809-492f-8ae4-06db603c329f/download/nebraska-ne-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/408d9333-3809-492f-8ae4-06db603c329f/download/nebraska-ne-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR NEBRASKA 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR NEBRASKA 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/edd71cdf-83c2-4c28-8715-a5604fcb537b/download/nebraska-ne-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/edd71cdf-83c2-4c28-8715-a5604fcb537b/download/nebraska-ne-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR NEBRASKA 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR NEVADA 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/f519c418-a2e5-4e9c-8422-040afe1d4b9e/download/nevada-nv-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/f519c418-a2e5-4e9c-8422-040afe1d4b9e/download/nevada-nv-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR NEVADA 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR NEVADA 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/15629137-015f-4fb1-bee6-31b91e9bf0c3/download/nevada-nv-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/15629137-015f-4fb1-bee6-31b91e9bf0c3/download/nevada-nv-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR NEVADA 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR NEW HAMPSHIRE 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/d2bd1c10-c9c7-4ce3-8d64-4966dbd90bf6/download/new-hampshire-nh-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/d2bd1c10-c9c7-4ce3-8d64-4966dbd90bf6/download/new-hampshire-nh-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR NEW HAMPSHIRE 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR NEW HAMPSHIRE 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/98fa314d-543b-4aa8-a3b5-af276098e90f/download/new-hampshier-nh-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/98fa314d-543b-4aa8-a3b5-af276098e90f/download/new-hampshier-nh-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR NEW HAMPSHIRE 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR NEW JERSEY 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/c8859b57-d074-4ec2-9547-7d755dec733a/download/new-jersey-nj-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/c8859b57-d074-4ec2-9547-7d755dec733a/download/new-jersey-nj-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR NEW JERSEY 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR NEW JERSEY 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/164b4e77-1809-4ba8-802f-af5d0840df73/download/new-jersey-nj-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/164b4e77-1809-4ba8-802f-af5d0840df73/download/new-jersey-nj-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR NEW JERSEY 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR NEW MEXICO 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/ecf92897-9ee4-4799-beb4-0c1378655eef/download/new-mexico-nm-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/ecf92897-9ee4-4799-beb4-0c1378655eef/download/new-mexico-nm-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR NEW MEXICO 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR NEW MEXICO 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/4cdbfa50-0e57-4272-af89-74a65268af0f/download/new-mexico-nm-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/4cdbfa50-0e57-4272-af89-74a65268af0f/download/new-mexico-nm-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR NEW MEXICO 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR NEW YORK 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/526446b2-c459-4378-981c-34a31c83ed7c/download/new-mexico-nm-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/526446b2-c459-4378-981c-34a31c83ed7c/download/new-mexico-nm-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR NEW YORK 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR NEW YORK 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/360dd9d9-c848-483f-9246-f9bac4867ea3/download/new-york-ny-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/360dd9d9-c848-483f-9246-f9bac4867ea3/download/new-york-ny-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR NEW YORK 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR NORTH CAROLINA 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/4188eba9-3d8b-4e2b-87d0-e8a2c2c45b55/download/north-carolina-nc-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/4188eba9-3d8b-4e2b-87d0-e8a2c2c45b55/download/north-carolina-nc-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR NORTH CAROLINA 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR NORTH CAROLINA 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/f680cb2d-ca83-4481-8f19-0db8df119d2d/download/north-carolina-nc-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/f680cb2d-ca83-4481-8f19-0db8df119d2d/download/north-carolina-nc-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR NORTH CAROLINA 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR NORTH DAKOTA 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/5dae17d1-baa9-41f7-bada-807aac776ace/download/north-dakota-nd-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/5dae17d1-baa9-41f7-bada-807aac776ace/download/north-dakota-nd-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR NORTH DAKOTA 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR NORTH DAKOTA 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/0a42bae9-a42f-4cc6-a424-2d5a32dc05b6/download/north-dakota-nd-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/0a42bae9-a42f-4cc6-a424-2d5a32dc05b6/download/north-dakota-nd-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR NORTH DAKOTA 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR NORTHERN MARIANA 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/7bc18637-4809-4cad-ae0d-95a01cf02acc/download/northern-mariana-islands-mp-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/7bc18637-4809-4cad-ae0d-95a01cf02acc/download/northern-mariana-islands-mp-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR NORTHERN MARIANA 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR NORTHERN MARIANA 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/1075104f-8528-4d63-9eeb-0a092cbc1e57/download/northern-mariana-islands-mp-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/1075104f-8528-4d63-9eeb-0a092cbc1e57/download/northern-mariana-islands-mp-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR NORTHERN MARIANA 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR OHIO 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/0508628e-14f7-4ddd-b6d5-ffad3a06abb7/download/ohio-oh-resultsmatrix-2014b-revised.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/0508628e-14f7-4ddd-b6d5-ffad3a06abb7/download/ohio-oh-resultsmatrix-2014b-revised.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR OHIO 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR OHIO 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/e7cec73e-68fa-4424-ad4b-adb56eb02fde/download/ohio-oh-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/e7cec73e-68fa-4424-ad4b-adb56eb02fde/download/ohio-oh-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR OHIO 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR OKLAHOMA 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/72255c12-fec2-49d4-a141-471f31ea4a31/download/oklahoma-ok-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/72255c12-fec2-49d4-a141-471f31ea4a31/download/oklahoma-ok-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR OKLAHOMA 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR OKLAHOMA 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/341cdb2a-b14d-47d2-954c-6ba83e14887a/download/oklahoma-ok-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/341cdb2a-b14d-47d2-954c-6ba83e14887a/download/oklahoma-ok-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR OKLAHOMA 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR OREGON 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/a4fe5e00-46d1-46be-9bb4-cc1d4108abc9/download/oregon-or-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/a4fe5e00-46d1-46be-9bb4-cc1d4108abc9/download/oregon-or-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR OREGON 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR OREGON 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/f449345e-16e2-4fc0-8fda-9664425802cf/download/oregon-or-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/f449345e-16e2-4fc0-8fda-9664425802cf/download/oregon-or-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR OREGON 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR PALAU 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/5ba8b0c2-eee2-4a28-9425-d20f84fdedc3/download/palau-pw-resultsmatrix-2014b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/5ba8b0c2-eee2-4a28-9425-d20f84fdedc3/download/palau-pw-resultsmatrix-2014b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR PALAU 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR PALAU 2013b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/4f2b8da3-6c76-4608-8d91-ef68fa1b6627/download/palau-pw-matrix-2013b.xlsx"
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/4f2b8da3-6c76-4608-8d91-ef68fa1b6627/download/palau-pw-matrix-2013b.xlsx",
+                    "format": "XLSX",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR PALAU 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/0ab94969-1d4c-432e-854b-df621f8d5359/download/pennsylvania-pa-resultsmatrix-2014b.xlsx",
                     "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR PENNSYLVANIA 2014b",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/0ab94969-1d4c-432e-854b-df621f8d5359/download/pennsylvania-pa-resultsmatrix-2014b.xlsx"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR PENNSYLVANIA 2014b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/4c72ef7d-5d92-443f-a725-5680594b11a1/download/pennsylvania-pa-matrix-2013b.xlsx",
                     "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR PENNSYLVANIA 2013b",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/4c72ef7d-5d92-443f-a725-5680594b11a1/download/pennsylvania-pa-matrix-2013b.xlsx"
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "title": "OSEP Response to SPP/APR PENNSYLVANIA 2013b"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "format": "XLSX",
-                    "title": "OSEP Response to SPP/APR PUERTO RICO 2014b",
                     "description": "Part B State Performance Plans (SPP) Letters and Annual Performance Report (APR) Letters - Individuals with Disabilities Education Act",
-                    "downloadURL": "https://data.ed.gov/dataset/c2391fd1-5835-47fe-8466-0369f11df52e/resource/54c0edfa-f1c4-4500-a61d-7874a2713854/download/puerto-rico-pr-resultsmatrix-2014b.xlsx"
```

