# Change History for va.json (Part 3)

### Changes from 31606f9 to dd2190f (Part 3/7)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
             "description": "<p>VBA PROGRAM BENEFITS for Automobiles and Adaptive Equipment for Certain Disabled Veterans and Members of the Armed Forces. Veterans with honorable service and servicepersons on duty having a service-connected disability due to loss or permanent loss of use of one or both feet, one or both hands, or a permanent impairment of vision of both eyes to a prescribed degree. For adaptive equipment only, eligibility also exists if there is service-connected ankylosis of one or both knees or one or both hips. Personnel on active duty also qualify under the same criteria as veterans. Uses &amp; Use Restrictions:  Assistance toward purchase of an automobile or other conveyance is a one-time payment only. Necessary adaptive equipment may be furnished, repaired, replaced, or reinstalled on a conveyance which may be purchased with assistance or any other conveyance subsequently or previously acquired. Adaptive equipment will be provided for no more than two conveyances during any four-year period unless one of those two vehicles becomes unavailable to the veteran.</p>",
-            "title": "USA SPENDING CH39 B100 AUTOMOBILE AND ADAPTIVE EQUIPMENT ALLOWANCE FEB2019",
-            "isPartOf": "70535216-31bf-416c-9ff4-3ec839abed4c",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27569,43 +27553,74 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/am3n-jg4e/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/am3n-jg4e/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/am3n-jg4e/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/am3n-jg4e/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/am3n-jg4e/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/am3n-jg4e/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/am3n-jg4e/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/am3n-jg4e/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/am3n-jg4e/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/am3n-jg4e",
+            "isPartOf": "70535216-31bf-416c-9ff4-3ec839abed4c",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 100"
+            ],
+            "landingPage": "https://www.data.va.gov/d/am3n-jg4e",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-14",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING CH39 B100 AUTOMOBILE AND ADAPTIVE EQUIPMENT ALLOWANCE FEB2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "accrualPeriodicity": "R/P2W",
             "bureauCode": [
                 "029:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/access-audit.asp",
+            "description": "<p>This release included wait time data for each facility down to the Community Based Outpatient Clinic (CBOC) level.  Wait times are calculated using the Preferred Date for all patients.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/1_February_2015_Access_Data_Pending_02192015.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Pending February Appointments"
+                }
+            ],
+            "identifier": "VA-VHA-OIA-096",
+            "isPartOf": "VA-VHA-OIA-073",
             "issued": "2017-07-26",
-            "temporal": "2015-02-01T05:00:00Z/2015-02-01T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "access",
                 "appointment",
@@ -27619,72 +27634,42 @@
                 "wait list",
                 "wait time"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:041"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-OIA-096",
-            "description": "<p>This release included wait time data for each facility down to the Community Based Outpatient Clinic (CBOC) level.  Wait times are calculated using the Preferred Date for all patients.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 Feb 19",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/1_February_2015_Access_Data_Pending_02192015.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Pending February Appointments"
-                }
-            ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2W",
+            "temporal": "2015-02-01T05:00:00Z/2015-02-01T05:00:00Z",
             "theme": [
                 "Accelerating Access"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 Feb 19"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/Report.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2005-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "unique veteran",
-                "users"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:tom.garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-057",
-            "description": "<p>This report provides demographic, socio-economic, and utilization trends of Veterans who used at least one VA benefit or service each year between FY 2005 and FY 2012. It also includes a comparison of Veterans who used VA benefits to Veterans who did not use VA benefits.</p>",
-            "title": "FY 2012 Profile of Unique Veteran Users",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/vetdata/docs/SpecialReports/Profile_of_Unique_Veteran_Users.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "029:086"
-            ],
+            "description": "<p>This report provides demographic, socio-economic, and utilization trends of Veterans who used at least one VA benefit or service each year between FY 2005 and FY 2012. It also includes a comparison of Veterans who used VA benefits to Veterans who did not use VA benefits.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27693,28 +27678,46 @@
                     "title": "pdf"
                 }
             ],
-            "describedBy": "https://www.va.gov/vetdata/docs/SpecialReports/Profile_of_Unique_Veteran_Users.pdf",
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-057",
+            "issued": "2017-07-26",
+            "keyword": [
+                "unique veteran",
+                "users"
+            ],
+            "landingPage": "https://www.va.gov/vetdata/Report.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2005-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "unique veteran users"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 2012 Profile of Unique Veteran Users"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/anm5-vwhs",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The Post-Deployment Health Strategic Healthcare Group (PDHSHG) Registry System of Records is the information system encompassing the Ionizing Radiation Registry (IRR), the Agent Orange Registry (AOR), and the Gulf War Registry (GWR) which also includes related Depleted Uranium (DU) exams. The IRR area of the Environmental Health Program (EHP) database contains the results of questionnaires completed by Veterans who may have been exposed to ionizing radiation while on active military duty and have had an IRR examination at a VA medical facility.</p>",
+            "identifier": "VA-VHA-OPH-008",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2002-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "health",
                 "ionizing",
@@ -27724,91 +27727,71 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/anm5-vwhs",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:041"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-OPH-008",
-            "description": "<p>The Post-Deployment Health Strategic Healthcare Group (PDHSHG) Registry System of Records is the information system encompassing the Ionizing Radiation Registry (IRR), the Agent Orange Registry (AOR), and the Gulf War Registry (GWR) which also includes related Depleted Uranium (DU) exams. The IRR area of the Environmental Health Program (EHP) database contains the results of questionnaires completed by Veterans who may have been exposed to ionizing radiation while on active military duty and have had an IRR examination at a VA medical facility.</p>",
-            "title": "Ionizing Radiation Registry (IRR) - The Environmental Hazards Strategic Healthcare Group (EHSHG) Registry System of Records",
-            "programCode": [
-                "029:041"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "temporal": "2002-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Ionizing Radiation Registry (IRR) - The Environmental Hazards Strategic Healthcare Group (EHSHG) Registry System of Records"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/anmw-z3rg",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-10-30",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-04",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "11b63572-a824-42b5-99dc-a7a1beee34c7",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Maryland FY2017",
+            "identifier": "11b63572-a824-42b5-99dc-a7a1beee34c7",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/anmw-z3rg",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-04",
             "programCode": [
                 "029:086"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summary Maryland FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/anrg-c2yk",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "michigan",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:Tom.Garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-109",
             "description": "<p>This is a summary of the programs and services provided by VA in Michigan in fiscal year 2014.</p>",
-            "title": "State Summary:  Michigan",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27817,44 +27800,45 @@
                     "title": "State Summary:  Michigan"
                 }
             ],
+            "identifier": "VA-OEI-OEI-109",
+            "issued": "2017-07-26",
+            "keyword": [
+                "michigan",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/anrg-c2yk",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "State Summary:  Michigan"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/anvk-kjcb",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-21",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 116"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/anvk-kjcb",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION PROGRAMS to provide, through purchase and/or fabrication, prosthetic and related appliances, equipment and services to eligible veterans so that they may live and work as productive citizens. Veterans eligible for prosthetic services are service-connected veterans seeking care for a service-connected disability; veterans with compensable service-connected disabilities generally rated 10 percent or more; former prisoners of war, veterans discharged or released from active military service for a disability that was incurred or aggravated in the line of duty, and veterans who are in receipt of Section 1151 benefits; veterans who are in receipt of increased pension based on a need of regular aid and attendance or by reason of being permanently housebound; veterans who have annual income and net worth below the \"means test\" threshold; all other veterans who are not required to pay a copayment for their care, i.e., veterans of the Mexican border period and World War I, compensated zero (0) percent service-connected veterans who are receiving statutory awards, veterans exposed to a toxic substance, radiation or environmental hazard (limited to certain disabilities); and veterans who must pay a copayment for their care. Ineligible veterans are nonservice-connected veterans residing or sojourning in foreign lands.</p>",
-            "title": "USA SPENDING EDUCATION CH31 B116 VETERANS PROSTHETIC APPLIANCES MAY2019",
-            "isPartOf": "5760c6c5-d531-4dc3-9e99-4418034dbb16",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27862,58 +27846,58 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/anvk-kjcb/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/anvk-kjcb/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/anvk-kjcb/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/anvk-kjcb/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/anvk-kjcb/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/anvk-kjcb/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/anvk-kjcb/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/anvk-kjcb/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/anvk-kjcb/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/anvk-kjcb",
+            "isPartOf": "5760c6c5-d531-4dc3-9e99-4418034dbb16",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 116"
+            ],
+            "landingPage": "https://www.data.va.gov/d/anvk-kjcb",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "USA SPENDING EDUCATION CH31 B116 VETERANS PROSTHETIC APPLIANCES MAY2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/aqf3-bdfm",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-11-13",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "3b745127-694f-4e1e-bc3c-50236cb13c91",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary New Mexico FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -27921,80 +27905,80 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "3b745127-694f-4e1e-bc3c-50236cb13c91",
+            "issued": "2017-11-13",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/aqf3-bdfm",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summary New Mexico FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://benefits.va.gov/benefits/media-publications.asp",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Elwell",
+                "hasEmail": "mailto:thomas.elwell@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>Veterans Group Life Insurance (VGLI)</p>",
+            "identifier": "VA-VBA-MEDIAPUB-047",
+            "isPartOf": "VA-VBA-MASTER-MEDIAPUBLICATIONS-001",
             "issued": "2017-07-26",
-            "temporal": "2012-09-01T04:00:00Z/2012-09-01T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-08",
             "keyword": [
                 "benefits fact sheet",
                 "general benefit information",
                 "va benefits",
                 "va fact sheet"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Elwell",
-                "hasEmail": "mailto:thomas.elwell@va.gov"
-            },
+            "landingPage": "https://benefits.va.gov/benefits/media-publications.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-03-08",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-MEDIAPUB-047",
-            "description": "<p>Veterans Group Life Insurance (VGLI)</p>",
-            "title": "Veterans Group Life Insurance (VGLI)",
-            "isPartOf": "VA-VBA-MASTER-MEDIAPUBLICATIONS-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2012-09-01T04:00:00Z/2012-09-01T04:00:00Z",
             "theme": [
                 "General Benefit Information"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veterans Group Life Insurance (VGLI)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/asne-dmv7",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "All data is within the public domain and is currently available for download.",
-            "issued": "2024-09-04",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-04",
-            "keyword": [
-                "ptsd-repository",
-                "risk of bias"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for PTSD",
                 "hasEmail": "mailto:ncptsd@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for PTSD"
-            },
-            "identifier": "https://www.data.va.gov/api/views/asne-dmv7",
+            "dataQuality": true,
             "description": "Each study in the PTSD-Repository was coded for risk of bias (ROB) in specific domains as well as an overall risk of bias for the study. Detailed information about the specific coding strategy is available in Comparative Effectiveness Review [CER] No. 207, Psychological and Pharmacological Treatments for Adults with Posttraumatic Stress Disorder. (See our \"Risk of Bias\" data story.)\nMost domains were rated as Yes (i.e., minimal risk of bias), No (i.e., high risk of bias) or Unclear (i.e., bias could not be determined). The overall study rating is based on the domains and is coded as low, medium or high risk of bias. The 4 domains that were included as components of the overall rating include: Selection bias--randomization adequate, allocation concealment adequate, groups similar at baseline and whether they used intention to treat analyses; Performance bias--care providers masked and patients masked; Detection bias--outcome assessors masked; Attrition bias--overall attrition less than or equal to 20% vs over 20%; differential attrition less than or equal to 15% vs over 15%.\nAdditional items assessed (but not considered as part of the overall rating) include: Reporting bias--all prespecified outcomes reported; Reporting bias--method for handling dropouts; Outcome measures equal valid and reliable; Study reports adequate treatment fidelity based on measurements by independent raters.",
-            "title": "Risk Of Bias",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28002,106 +27986,106 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/asne-dmv7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/asne-dmv7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/asne-dmv7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/asne-dmv7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/asne-dmv7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/asne-dmv7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/asne-dmv7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/asne-dmv7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/asne-dmv7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y",
-            "theme": [
-                "PTSD-Repository"
+            "identifier": "https://www.data.va.gov/api/views/asne-dmv7",
+            "issued": "2024-09-04",
+            "keyword": [
+                "ptsd-repository",
+                "risk of bias"
             ],
+            "landingPage": "https://www.data.va.gov/d/asne-dmv7",
             "language": [
                 "en-US"
-            ]
+            ],
+            "modified": "2024-09-04",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for PTSD"
+            },
+            "rights": "All data is within the public domain and is currently available for download.",
+            "theme": [
+                "PTSD-Repository"
+            ],
+            "title": "Risk Of Bias"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.usaspending.gov",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Dusca Fichtel",
+                "hasEmail": "mailto:Dusca.Fichtel@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>USA Spending- Face Amount of New Life Insurance Policies Issued- December 2013.</p>",
+            "identifier": "VA-VBA-USASPENDING122013-012",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2013-12-01T05:00:00Z/2013-12-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 030",
                 "direct payment to veterans",
                 "insurance service",
                 "usa spending"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Dusca Fichtel",
-                "hasEmail": "mailto:Dusca.Fichtel@va.gov"
-            },
+            "landingPage": "https://www.usaspending.gov",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-USASPENDING122013-012",
-            "description": "<p>USA Spending- Face Amount of New Life Insurance Policies Issued- December 2013.</p>",
-            "title": "USA Spending file- Direct Payments for Veterans-Insurance -  CFDA 64.031",
-            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2013-12-01T05:00:00Z/2013-12-30T05:00:00Z",
             "theme": [
                 "USA Spending"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USA Spending file- Direct Payments for Veterans-Insurance -  CFDA 64.031"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/at5z-znru",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-11-13",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "f9e44218-5c06-4f26-a266-5c0418228cc3",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary South Dakota FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28109,39 +28093,37 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "f9e44218-5c06-4f26-a266-5c0418228cc3",
+            "issued": "2017-11-13",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/at5z-znru",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2020-11-12",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summary South Dakota FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/at9t-esyb",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2019-05-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "burial data",
-                "cemeteries",
-                "gravesites",
-                "veterans and beneficiaries"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCA NGL Data",
                 "hasEmail": "mailto:NCANGLData@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-NCA-MS-20190501-035",
             "description": "<p>Gravesite locations of Veterans and beneficiaries in NEW YORK, as of May 2019.</p>",
-            "title": "Gravesite locations of Veterans and beneficiaries in NEW YORK, as of May 2019.",
-            "programCode": [
-                "029:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28150,36 +28132,40 @@
                     "title": "Gravesite locations of Veterans and beneficiaries in NEW YORK, as of May 2019."
                 }
             ],
+            "identifier": "VA-NCA-MS-20190501-035",
+            "issued": "2019-05-01",
+            "keyword": [
+                "burial data",
+                "cemeteries",
+                "gravesites",
+                "veterans and beneficiaries"
+            ],
+            "landingPage": "https://www.data.va.gov/d/at9t-esyb",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M"
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Gravesite locations of Veterans and beneficiaries in NEW YORK, as of May 2019."
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/au9q-4hkn",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2018-03-19",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-19",
-            "keyword": [
-                "equitable relief report"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Sharon Weiner",
                 "hasEmail": "mailto:Sharon.Weiner@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "ee734493-3fbf-40e2-983b-21c3fc098a33",
+            "dataQuality": true,
             "description": "<p>Equitable Relief Reports as submitted to Congress</p>",
-            "title": "Equitable Relief Reports 2011",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28187,46 +28173,44 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "ee734493-3fbf-40e2-983b-21c3fc098a33",
+            "issued": "2018-03-19",
+            "keyword": [
+                "equitable relief report"
+            ],
+            "landingPage": "https://www.data.va.gov/d/au9q-4hkn",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-11-19",
+            "programCode": [
+                "029:083"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Equitable Relief Reports 2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/auud-t2uk",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 114"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/auud-t2uk",
+            "dataQuality": true,
             "description": "<p>VBA HOUSING BENEFITS PROGRAM to provide veterans who are eligible for a Specially Adapted Housing grant with loan directly from the VA in certain circumstances. Permanently and totally disabled Veterans who served on active duty on or after September 16, 1940 and are eligible for a Specially Adapted Housing grant. VA may make loans up to $33,000 to eligible applicants if (a) the veteran is eligible for a VA Specially Adapted Housing grant, and (b) a loan is necessary to supplement the grant, and (c) home loans from a private lender are not available in the area where the property involved is located.</p>",
-            "title": "USA SPENDING LGY B114 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS APR2019",
-            "isPartOf": "bd8fa8ad-9de6-41b7-a863-09ed5197e048",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28234,62 +28218,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/auud-t2uk/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/auud-t2uk/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/auud-t2uk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/auud-t2uk/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/auud-t2uk/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/auud-t2uk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/auud-t2uk/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/auud-t2uk/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/auud-t2uk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/auud-t2uk",
+            "isPartOf": "bd8fa8ad-9de6-41b7-a863-09ed5197e048",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 114"
+            ],
+            "landingPage": "https://www.data.va.gov/d/auud-t2uk",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING LGY B114 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS APR2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/aw65-r2k3",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2023-10-19",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-19",
-            "keyword": [
-                "branch",
-                "branch of service",
-                "vetpop2020"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:vaconcvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/aw65-r2k3",
             "description": "Estimated number of Veterans by branch of service for fiscal years 2000 to 2023.\n\n\u201cAll Others\u201d includes U.S. Coast Guard, U.S. Public Health Service, National Oceanic and Atmospheric Administration, and Reserves.",
-            "title": "VetPop2020 Branch of Service FY2000-2023",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28297,62 +28279,58 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/aw65-r2k3/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/aw65-r2k3/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/aw65-r2k3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/aw65-r2k3/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/aw65-r2k3/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/aw65-r2k3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/aw65-r2k3/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/aw65-r2k3/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/aw65-r2k3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/aw65-r2k3",
+            "issued": "2023-10-19",
+            "keyword": [
+                "branch",
+                "branch of service",
+                "vetpop2020"
+            ],
+            "landingPage": "https://www.data.va.gov/d/aw65-r2k3",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-10-19",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2020 Branch of Service FY2000-2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/awky-9bj7",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2022-03-18",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-05",
-            "keyword": [
-                "utilization",
-                "va benefits",
-                "va programs",
-                "va services",
-                "veteran benefits",
-                "veterans",
-                "veterans benefits"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:VANCVAS@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/awky-9bj7",
             "description": "Trends among Service-Connected Disabled Veterans in Percentage Enrolled & Using Health Care, Enrolled & Not Using Health Care, and Not Enrolled for Health Care, FY 2010-2021. Data underlying the second figure of Part 3 of the FY2021 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Trend in Percent Health Care Enrolled Users, Enrolled Non-Users & Non-Enrolled among Service-Connected Disabled Veterans, FY2010-2021",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28360,58 +28338,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/awky-9bj7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/awky-9bj7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/awky-9bj7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/awky-9bj7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/awky-9bj7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/awky-9bj7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/awky-9bj7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/awky-9bj7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/awky-9bj7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/awky-9bj7",
+            "issued": "2022-03-18",
+            "keyword": [
+                "utilization",
+                "va benefits",
+                "va programs",
+                "va services",
+                "veteran benefits",
+                "veterans",
+                "veterans benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/awky-9bj7",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-01-05",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Trend in Percent Health Care Enrolled Users, Enrolled Non-Users & Non-Enrolled among Service-Connected Disabled Veterans, FY2010-2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/finance/overpaymentsReport.asp",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-07-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "improper payments",
-                "overpayments"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Katherine Palmer",
                 "hasEmail": "mailto:Katherine.Palmer@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-088",
+            "dataQuality": true,
             "description": "<p>FY 2012 Fourth Quarter High-Dollar Overpayments Report</p>",
-            "title": "FY 2012 Fourth Quarter High-Dollar Overpayments Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28420,44 +28404,44 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-088",
+            "issued": "2017-07-26",
+            "keyword": [
+                "improper payments",
+                "overpayments"
+            ],
+            "landingPage": "https://www.va.gov/finance/overpaymentsReport.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2012-07-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 2012 Fourth Quarter High-Dollar Overpayments Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/axm8-z759",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 106"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/axm8-z759",
+            "dataQuality": true,
             "description": "<p>VBA SPECIALLY ADAPTED HOUSING BENEFIT PROGRAMS. The Specially Adapted Housing (SAH) grant program helps Veterans with certain service-connected disabilities live independently in a barrier-free environment. SAH grants can be used in one of the following ways: (1) construct a suitable home on suitable land either already owned or to be acquired by the veteran, or (2) remodel an existing home if it can be suitably adapted, or (3) acquire a suitably adapted home or reduce the outstanding mortgage on a suitably adapted home already owned by the veteran. b. The Special Housing Adaptation (SHA) grant program helps veterans with certain service-connected disabilities adapt or purchase a home to accommodate the disability. SHA grants can be used in one of the following ways: (1) adapt an existing home the veteran or a family member already owns in which the veteran lives; (2) adapt a home the veteran or family member intends to purchase in which the veteran will live; (3) help a veteran purchase a home already adapted in which the veteran will live. c. . The Temporary Residence Adaptations (TRA) program provides adaptation assistance to veterans who are residing, but do not intend to permanently reside, in the a residence owned by a family member. If a veteran is otherwise eligible for SAH or SHA, the assistance is limited. d. SAH and SHA grants may be used up to three times, as long as the aggregate grant amount does not exceed the statutory dollar limitation. TRA grants may only be used once (and count as a grant usage for purposes of the limit of three), and the amount of assistance provided will be subtracted from the veteran's available statutory maximum.</p>",
-            "title": "USA SPENDING CH39 B106 SPECIALLY ADAPTED HOUSING FOR DISABLED VETERANS NOV2018",
-            "isPartOf": "bc3a6e1f-3fb0-4fb1-8b07-59efaf92222b",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28465,61 +28449,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/axm8-z759/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/axm8-z759/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/axm8-z759/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/axm8-z759/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/axm8-z759/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/axm8-z759/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/axm8-z759/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/axm8-z759/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/axm8-z759/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/axm8-z759",
+            "isPartOf": "bc3a6e1f-3fb0-4fb1-8b07-59efaf92222b",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 106"
+            ],
+            "landingPage": "https://www.data.va.gov/d/axm8-z759",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING CH39 B106 SPECIALLY ADAPTED HOUSING FOR DISABLED VETERANS NOV2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/aynt-bsmd",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 118"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/aynt-bsmd",
+            "dataQuality": true,
             "description": "<p>VBA HOUSING BENEFITS PROGRAM to provide veterans who are eligible for a Specially Adapted Housing grant with loan directly from the VA in certain circumstances. Permanently and totally disabled Veterans who served on active duty on or after September 16, 1940 and are eligible for a Specially Adapted Housing grant. VA may make loans up to $33,000 to eligible applicants if (a) the veteran is eligible for a VA Specially Adapted Housing grant, and (b) a loan is necessary to supplement the grant, and (c) home loans from a private lender are not available in the area where the property involved is located</p>",
-            "title": "USA SPENDING LGY B118 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS MAY2019",
-            "isPartOf": "7d0e269c-91a6-4b56-9c6a-68d0e7617aab",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28527,61 +28511,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/aynt-bsmd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/aynt-bsmd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/aynt-bsmd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/aynt-bsmd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/aynt-bsmd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/aynt-bsmd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/aynt-bsmd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/aynt-bsmd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/aynt-bsmd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/aynt-bsmd",
+            "isPartOf": "7d0e269c-91a6-4b56-9c6a-68d0e7617aab",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 118"
+            ],
+            "landingPage": "https://www.data.va.gov/d/aynt-bsmd",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING LGY B118 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS MAY2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/b2cd-9fba",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-10-30",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "620fed3a-485a-42b4-9cbc-e42c891dc05a",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Washington FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28589,55 +28573,77 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "620fed3a-485a-42b4-9cbc-e42c891dc05a",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/b2cd-9fba",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-12",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data",
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "State Summary Washington FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/b3gk-fhv9",
-            "issued": "2024-06-12",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-12",
-            "keyword": [
-                "fy2023",
-                "missouri",
-                "ncvas state summary"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Florinda Balfour",
                 "hasEmail": "mailto:VACONCVAS@VA.GOV"
             },
+            "description": "NCVAS State Summary Missouri FY2023",
+            "identifier": "https://www.data.va.gov/api/views/b3gk-fhv9",
+            "issued": "2024-06-12",
+            "keyword": [
+                "fy2023",
+                "missouri",
+                "ncvas state summary"
+            ],
+            "landingPage": "https://www.data.va.gov/d/b3gk-fhv9",
+            "modified": "2024-07-12",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/b3gk-fhv9",
-            "description": "NCVAS State Summary Missouri FY2023",
-            "title": "NCVAS State Summary Missouri FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Missouri FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.usaspending.gov",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Monica Reyes",
+                "hasEmail": "mailto:monica.reyes@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>USA Spending- Post-Vietnam Era Veterans Educational Assistance- Chapter 32- for December 2013.</p>",
+            "identifier": "VA-VBA-USASPENDING122013-003",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2013-12-01T05:00:00Z/2013-12-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 120",
                 "chapter 35",
@@ -28645,66 +28651,66 @@
                 "usa spending",
                 "veap"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Monica Reyes",
-                "hasEmail": "mailto:monica.reyes@va.gov"
-            },
+            "landingPage": "https://www.usaspending.gov",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-USASPENDING122013-003",
-            "description": "<p>USA Spending- Post-Vietnam Era Veterans Educational Assistance- Chapter 32- for December 2013.</p>",
-            "title": "USA Spending file- Education- Chapter 32- CFDA 64.120",
-            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2013-12-01T05:00:00Z/2013-12-30T05:00:00Z",
             "theme": [
                 "USA Spending"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USA Spending file- Education- Chapter 32- CFDA 64.120"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/b5df-nb2b",
-            "issued": "2023-08-11",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-20",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary West Virginia FY2021",
+            "identifier": "https://www.data.va.gov/api/views/b5df-nb2b",
+            "issued": "2023-08-11",
             "keyword": [
                 "fy2021 data",
                 "ncvas state summary",
                 "west virginia"
             ],
-            "identifier": "https://www.data.va.gov/api/views/b5df-nb2b",
+            "landingPage": "https://www.data.va.gov/d/b5df-nb2b",
+            "modified": "2024-06-20",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary West Virginia FY2021",
             "title": "NCVAS State Summary West Virginia FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.usaspending.gov/",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Monica Reyes",
+                "hasEmail": "mailto:monica.reyes@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>USA Spending- Education-Post 9/11 Veterans Educational Assistance ( Chapter33) for March 2014.</p>",
+            "identifier": "VA-VBA-USASPENDING032014-050",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-03-01T05:00:00Z/2014-03-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 028",
                 "ch33",
@@ -28712,65 +28718,39 @@
                 "education",
                 "usa spending"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Monica Reyes",
-                "hasEmail": "mailto:monica.reyes@va.gov"
-            },
+            "landingPage": "https://www.usaspending.gov/",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-USASPENDING032014-050",
-            "description": "<p>USA Spending- Education-Post 9/11 Veterans Educational Assistance ( Chapter33) for March 2014.</p>",
-            "title": "USA Spending file- 03/2014-Education- Chapter 33/ CFDA 64.028",
-            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2014-03-01T05:00:00Z/2014-03-31T04:00:00Z",
             "theme": [
                 "USA Spending"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USA Spending file- 03/2014-Education- Chapter 33/ CFDA 64.028"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-02",
-            "keyword": [
-                "fy2012 benefits",
-                "fy2012 vba",
-                "vba",
-                "vba benefits",
-                "vba benefits by state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Elwell",
                 "hasEmail": "mailto:thomas.elwell@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-ABR2012-080",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Arkansas-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28778,44 +28758,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-080",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "fy2012 benefits",
+                "fy2012 vba",
+                "vba",
+                "vba benefits",
+                "vba benefits by state"
+            ],
+            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2022-03-02",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "ABR 2012"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Arkansas-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/b68g-ti39",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2016-09-28",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "health",
-                "statistics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:tom.garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "afe5a9bc-805e-4f64-b883-c0e36c7c4357",
+            "dataQuality": true,
             "description": "<p>This table shows a brief summary of enrollees, outpatient visits and inpatient admissions.</p>",
-            "title": "Selected Veterans Health Administration Characteristics: FY2002 to FY2014",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28823,48 +28807,43 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "afe5a9bc-805e-4f64-b883-c0e36c7c4357",
+            "issued": "2016-09-28",
+            "keyword": [
+                "health",
+                "statistics"
+            ],
+            "landingPage": "https://www.data.va.gov/d/b68g-ti39",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "Selected Veterans Health Administration Characteristics: FY2002 to FY2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www1.va.gov/vetdata/docs/DataGov_Compensation_and_Pension_by_County_Technical_Notes.doc",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2007-10-01T04:00:00Z/2008-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "references": [
-                "https://www1.va.gov/vetdata/docs/DataGov_Compensation_and_Pension_by_County_Technical_Notes.doc"
-            ],
-            "keyword": [
-                "disability compensation",
-                "pension",
-                "veteran"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS mailbox",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-CP2008-001",
+            "dataQuality": true,
             "description": "<p>The Compensation and Pension by County dataset is a count of the number of veterans receiving disability compensation or pension payments from the Department of Veterans Affairs.   The data is reported at the county level, by age group and by % disability rating for each state plus recipients in Guam, Philippines and Puerto Rico.</p>",
-            "title": "FY08  Veterans Compensation and Pension by County",
-            "isPartOf": "VA-VBA-MASTER-COMPENSATIONPENSION-001",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28872,44 +28851,49 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-CP2008-001",
+            "isPartOf": "VA-VBA-MASTER-COMPENSATIONPENSION-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "disability compensation",
+                "pension",
+                "veteran"
+            ],
+            "landingPage": "https://www1.va.gov/vetdata/docs/DataGov_Compensation_and_Pension_by_County_Technical_Notes.doc",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-11-12",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www1.va.gov/vetdata/docs/DataGov_Compensation_and_Pension_by_County_Technical_Notes.doc"
+            ],
+            "temporal": "2007-10-01T04:00:00Z/2008-09-30T04:00:00Z",
             "theme": [
                 "Section 11. Social Insurance and Human Services"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY08  Veterans Compensation and Pension by County"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/b6dc-6d9r",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-11-13",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "8bb15f19-6a51-478a-8a1a-9131d1e66827",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary New Hampshire FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28917,43 +28901,38 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "8bb15f19-6a51-478a-8a1a-9131d1e66827",
+            "issued": "2017-11-13",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/b6dc-6d9r",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2020-11-12",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summary New Hampshire FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/VGLI_Enrollment_by_State_February_2012.csv",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-02-01T05:00:00Z/2012-02-29T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Number_of_Veterans_Enrolled_in_VGLI_by_State_4.doc"
-            ],
-            "keyword": [
-                "benefits",
-                "insurance",
-                "state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dusca Fichtel",
                 "hasEmail": "mailto:dusca.fichtel@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-INS2012-008",
+            "dataQuality": true,
             "description": "<p>Provides the number of Veterans insured under the Veterans' Group Life Insurance (VGLI) program by state.  This report provides a snapshot of the active VGLI membership as of February 29, 2012.  For members who reside outside the United States, membership is not identified by individual country.  The total number of members was captured to ensure 100% of the population was identified in the report.</p>",
-            "title": "Number of Veterans Insurance by VGLI by State Feb 2012",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -28961,70 +28940,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/b6qe-qhgn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/b6qe-qhgn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/b6qe-qhgn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/b6qe-qhgn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/b6qe-qhgn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/b6qe-qhgn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/b6qe-qhgn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/b6qe-qhgn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/b6qe-qhgn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2012-008",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/VGLI_Enrollment_by_State_February_2012.csv",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Number_of_Veterans_Enrolled_in_VGLI_by_State_4.doc"
+            ],
+            "temporal": "2012-02-01T05:00:00Z/2012-02-29T05:00:00Z",
             "theme": [
                 "Section 1. Population"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Number of Veterans Insurance by VGLI by State Feb 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-02",
-            "keyword": [
-                "fy2012 benefits",
-                "fy2012 vba",
-                "vba",
-                "vba benefits",
-                "vba benefits by state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Elwell",
                 "hasEmail": "mailto:thomas.elwell@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-ABR2012-115",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Oregon-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29032,45 +29012,49 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-115",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "fy2012 benefits",
+                "fy2012 vba",
+                "vba",
+                "vba benefits",
+                "vba benefits by state"
+            ],
+            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2022-03-02",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "ABR 2012"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Oregon-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.cfm.va.gov/historic/index.asp",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Public",
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2014-01-06T05:00:00Z/2014-10-20T04:00:00Z",
-            "modified": "2024-08-26",
-            "keyword": [
-                "archaeological requirements construction management cultural resource management directive 7545"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Robert Connor",
                 "hasEmail": "mailto:robert.connor@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-CFM-HistPres-0013",
+            "dataQuality": true,
             "description": "<p>The VA Historic Preservation Office keeps information about VA's programs to comply with Federal preservation requirements, and also interesting information about VA history.</p>",
-            "title": "Historic Preservation Information CFM Website",
-            "programCode": [
-                "029:090"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29079,46 +29063,46 @@
                     "title": "html"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-CFM-HistPres-0013",
+            "issued": "2017-07-26",
+            "keyword": [
+                "archaeological requirements construction management cultural resource management directive 7545"
+            ],
+            "landingPage": "https://www.cfm.va.gov/historic/index.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2024-08-26",
+            "programCode": [
+                "029:090"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Public",
+            "temporal": "2014-01-06T05:00:00Z/2014-10-20T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Historic Preservation Information CFM Website"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/badk-zyfx",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2017-11-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "appeals"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Shawn Henning",
                 "hasEmail": "mailto:shawn.henning@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-ORCH-1",
+            "dataQuality": true,
             "description": "<p>ESS Adapter interfaces for the VACOLS database</p>",
-            "title": "Appeals Service",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29127,46 +29111,41 @@
                     "title": "Appeals Service"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "identifier": "VA-ORCH-1",
+            "issued": "2017-11-17",
+            "keyword": [
+                "appeals"
+            ],
+            "landingPage": "https://www.data.va.gov/d/badk-zyfx",
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
+            "title": "Appeals Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/VGLI_Coverage_Amount_by_State.csv",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2010-10-01T04:00:00Z/2011-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Number_of_Veterans_Enrolled_in_VGLI_by_State_2.doc"
-            ],
-            "keyword": [
-                "benefits",
-                "insurance",
-                "state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dusca Fichtel",
                 "hasEmail": "mailto:dusca.fichtel@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-INS2011-010",
+            "dataQuality": true,
             "description": "<p>Provides the amount of Veterans' Group Life Insurance (VGLI) coverage by state.  This report provides a snapshot of the amount of VGLI coverage as of October 31, 2011.  For members who reside outside the United States, coverage is not identified by individual country.  The total amount of coverage was captured to ensure 100% of the population was identified in the report.</p>",
-            "title": "FY11_EOM_OCT_VGLI Coverage Amount by State as of October 31, 2011",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29174,68 +29153,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/badw-egtj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/badw-egtj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/badw-egtj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/badw-egtj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/badw-egtj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/badw-egtj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/badw-egtj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/badw-egtj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/badw-egtj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2011-010",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/VGLI_Coverage_Amount_by_State.csv",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_Number_of_Veterans_Enrolled_in_VGLI_by_State_2.doc"
+            ],
+            "temporal": "2010-10-01T04:00:00Z/2011-09-30T04:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY11_EOM_OCT_VGLI Coverage Amount by State as of October 31, 2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/bam8-9mxz",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2023-10-12",
-            "@type": "dcat:Dataset",
-            "modified": "2023-10-12",
-            "keyword": [
-                "branch",
-                "branch of service",
-                "vetpop2020"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:vaconcvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/bam8-9mxz",
             "description": "Percent distribution of VetPop2020 estimates and projections by branch of service for fiscal years 2000 through 2023.  \n\n\u201cAll Others\u201d includes U.S. Coast Guard, U.S. Public Health Service, National Oceanic and Atmospheric Administration, and Reserves",
-            "title": "VetPop2020 Branch Distribution, FY2000-2023",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29243,57 +29225,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/bam8-9mxz/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/bam8-9mxz/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/bam8-9mxz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/bam8-9mxz/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/bam8-9mxz/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/bam8-9mxz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/bam8-9mxz/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/bam8-9mxz/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/bam8-9mxz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/bam8-9mxz",
+            "issued": "2023-10-12",
+            "keyword": [
+                "branch",
+                "branch of service",
+                "vetpop2020"
+            ],
+            "landingPage": "https://www.data.va.gov/d/bam8-9mxz",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-10-12",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2020 Branch Distribution, FY2000-2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/bbx2-yhvw",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2021-06-28",
-            "@type": "dcat:Dataset",
-            "modified": "2021-08-27",
-            "keyword": [
-                "ncvas",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VANCVAS",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/bbx2-yhvw",
+            "dataQuality": true,
             "description": "This dataset is comprised of 1 year estimate data from the American Community Survey published as of 2019.",
-            "title": "NCVAS State Summaries - Education Percentages (chart)",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29301,64 +29286,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/bbx2-yhvw/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/bbx2-yhvw/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/bbx2-yhvw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/bbx2-yhvw/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/bbx2-yhvw/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/bbx2-yhvw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/bbx2-yhvw/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/bbx2-yhvw/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/bbx2-yhvw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/bbx2-yhvw",
+            "issued": "2021-06-28",
+            "keyword": [
+                "ncvas",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/bbx2-yhvw",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y"
+            "modified": "2021-08-27",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "NCVAS State Summaries - Education Percentages (chart)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/Report.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2010-10-01T04:00:00Z/2011-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.benefits.va.gov/reports/annual_performance_reports.asp"
-            ],
-            "keyword": [
-                "compensation",
-                "county",
-                "pension"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:tom.garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-043",
+            "dataQuality": true,
+            "describedBy": "https://www.benefits.va.gov/reports/annual_performance_reports.asp",
             "description": "<p>This report uses data from the 2011 American Community Survey to compare the demographic and socioeconomic characteristics of minority Veterans and minority non-Veterans.  It also explores future projections of the minority Veteran population using VetPop 2011 and possible health issues that may affect the minority Veterans.</p>",
-            "title": "Compensation and Pension by County: 2011",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29367,46 +29348,48 @@
                     "title": "pdf"
                 }
             ],
-            "describedBy": "https://www.benefits.va.gov/reports/annual_performance_reports.asp",
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-043",
+            "issued": "2017-07-26",
+            "keyword": [
+                "compensation",
+                "county",
+                "pension"
+            ],
+            "landingPage": "https://www.va.gov/vetdata/Report.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.benefits.va.gov/reports/annual_performance_reports.asp"
+            ],
+            "temporal": "2010-10-01T04:00:00Z/2011-09-30T04:00:00Z",
             "theme": [
                 "Compensation and Pension by County"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Compensation and Pension by County: 2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/bcki-48pu",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "keyword": [
-                "food",
-                "food stamps",
-                "nutrition"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS Mailbox",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-103",
+            "dataQuality": true,
             "description": "<p>Characteristics of Veterans in Supplemental Nutritional Assistance Program (SNAP) household.  Regardless of race, marital status, education, and income veteran households participate in SNAP less than non-veteran households.</p>",
-            "title": "Veteran\u2019s Supplemental Nutritional Assistance Program (SNAP) Participants: 2013",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29414,47 +29397,67 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-103",
+            "issued": "2017-07-26",
+            "keyword": [
+                "food",
+                "food stamps",
+                "nutrition"
+            ],
+            "landingPage": "https://www.data.va.gov/d/bcki-48pu",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-12",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Socioeconomics"
-            ]
+            ],
+            "title": "Veteran\u2019s Supplemental Nutritional Assistance Program (SNAP) Participants: 2013"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/bcrp-8tg2",
-            "issued": "2023-07-04",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-10",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Michigan FY2021",
+            "identifier": "https://www.data.va.gov/api/views/bcrp-8tg2",
+            "issued": "2023-07-04",
             "keyword": [
                 "fy2021 data",
                 "michigan",
                 "ncvas state summary"
             ],
-            "identifier": "https://www.data.va.gov/api/views/bcrp-8tg2",
+            "landingPage": "https://www.data.va.gov/d/bcrp-8tg2",
+            "modified": "2024-06-10",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Michigan FY2021",
             "title": "NCVAS State Summary Michigan FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/bd7w-6j3d",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The Patient Advocate Tracking System (PATS) is a centralized, web based application that records and tracks instances of patient compliments and complaints concerning their care at VA health care facilities. These instances of patient contacts may come from a variety of sources including the patient, family members, congressional members and/or Veterans service organizations on behalf of the Veterans receiving care at VA facilities. This database provides a menu of reports that can be used to track and trend data across Veterans Integrated Service Networks (VISNs). Reports of contact allow the Patient Advocate to trend compliments and complaints, and ensure that issues raised are resolved. The reports include data such as patient demographics, date of contact, method of contact, who made the contact, issues involved, what service was involved, resolution date and resolution status. Data is collected from Veterans Affairs Medical Centers and sent to the VHA Support Service Center (VSSC) where the data is maintained and reports created.</p>",
+            "identifier": "VA-VHA-VHA-003",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2000-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "advocate",
                 "complaint",
@@ -29465,43 +29468,44 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/bd7w-6j3d",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:040"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-VHA-003",
-            "description": "<p>The Patient Advocate Tracking System (PATS) is a centralized, web based application that records and tracks instances of patient compliments and complaints concerning their care at VA health care facilities. These instances of patient contacts may come from a variety of sources including the patient, family members, congressional members and/or Veterans service organizations on behalf of the Veterans receiving care at VA facilities. This database provides a menu of reports that can be used to track and trend data across Veterans Integrated Service Networks (VISNs). Reports of contact allow the Patient Advocate to trend compliments and complaints, and ensure that issues raised are resolved. The reports include data such as patient demographics, date of contact, method of contact, who made the contact, issues involved, what service was involved, resolution date and resolution status. Data is collected from Veterans Affairs Medical Centers and sent to the VHA Support Service Center (VSSC) where the data is maintained and reports created.</p>",
-            "title": "Patient Advocate Tracking System (PATS)",
-            "programCode": [
-                "029:040"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "temporal": "2000-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Patient Advocate Tracking System (PATS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/bdep-miyj",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The Drug Accountability database collects information on medication dispensed to both inpatient and outpatient Veterans who receive health care from the VA.  Information for the Drug Accountability database is extracted from a number of files found within the Veterans Health Information Systems and Technology Architecture (VistA) environment.  Each month the extracted information is sent via MailMan messages from all VistA systems to the VA Pharmacy Benefits Management (PBM) office in Hines, Illinois.  At Hines, quality assurance procedures are performed on the data and local pharmaceutical names are converted to common names before the information is entered into the Drug Accountability database.  The users of this database include the PBM, Veterans Affairs Medical Centers (VAMCs), the Veterans Integrated Service Networks (VISNs), and the VA Research community.</p>",
+            "identifier": "VA-VHA-PBM-002",
+            "isPartOf": "VA-VHA-PBM-008",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1998-01-01T05:00:00Z/2011-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "accountability",
                 "benefit",
@@ -29514,63 +29518,41 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/bdep-miyj",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:041"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-PBM-002",
-            "description": "<p>The Drug Accountability database collects information on medication dispensed to both inpatient and outpatient Veterans who receive health care from the VA.  Information for the Drug Accountability database is extracted from a number of files found within the Veterans Health Information Systems and Technology Architecture (VistA) environment.  Each month the extracted information is sent via MailMan messages from all VistA systems to the VA Pharmacy Benefits Management (PBM) office in Hines, Illinois.  At Hines, quality assurance procedures are performed on the data and local pharmaceutical names are converted to common names before the information is entered into the Drug Accountability database.  The users of this database include the PBM, Veterans Affairs Medical Centers (VAMCs), the Veterans Integrated Service Networks (VISNs), and the VA Research community.</p>",
-            "title": "Drug Accountability",
-            "isPartOf": "VA-VHA-PBM-008",
-            "programCode": [
-                "029:041"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "temporal": "1998-01-01T05:00:00Z/2011-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Drug Accountability"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/bdus-iu2h",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2018-02-23",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-22",
-            "keyword": [
-                "access",
-                "identity",
-                "security"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jeff Podolec",
                 "hasEmail": "mailto:jeff.podolec@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "b0dc51dc-9676-4ecc-9964-361f3e2874c9",
+            "dataQuality": true,
             "description": "<p>User provisioning is the process of associating a digital identity with one or more resource access accounts, which may serve as records for user data and permissions. This may include the creation, modification, deletion, suspension, or restoration of such accounts and also synchronizing user data. Managing user accounts locally creates redundancy in collecting and managing user information. This may lead to inaccuracies and inconsistencies with user data that is stored in authoritative sources, and this may also create security vulnerabilities by maintaining accounts for terminated users. By leveraging Provisioning, VA applications are able to centrally manage user information, attributes, roles, and accounts using data from authoritative identity sources. Once a manually intensive and disjointed process, VAs Provisioning (Prov) service leverages automated and centralized workflows to enhance security and bolster efficiency. As a result, application administrators, who previously had to manually manage user administration, now have services available to automate the process. Provisioning assigns the Security Identifier (SecID) as a unique user identifier for integrated applications to use for user authorization and audit. SecID is a unique ID assigned to a user when they are added to the Provisioning system via an on-boarding event. SecID, once assigned, remains the same even if the user status with VA changes over time (i.e., a Veteran becomes a contractor and then later becomes an employee). SecID is the identifier used to correlate Provisioning records to MVIs integration control number (ICN), which is the unique person identifier. Provisioning automates the on-boarding and off-boarding flows. Applications leveraging Provisioning gain an added benefit of automated account removal (deprovisioning) during off-boarding. The following table lists the detailed functions offered by the Provisioning service. Additionally, the Provisioning service includes a Role Engineering and Compliance Tool (RECT) that can help applications:  Conduct Role Analysis: Provides the ability to analyze current roles and permissions to rapidly build and deploy an enterprise role model  Certify User Roles: Provides the ability to have access privileges reviewed and managed by designated reviewers</p>",
-            "title": "Provisioning (Prov)",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29579,42 +29561,40 @@
                     "title": "Provisioning (Prov)"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "b0dc51dc-9676-4ecc-9964-361f3e2874c9",
+            "issued": "2018-02-23",
+            "keyword": [
+                "access",
+                "identity",
+                "security"
+            ],
+            "landingPage": "https://www.data.va.gov/d/bdus-iu2h",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-03-22",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
+            "title": "Provisioning (Prov)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/FY11_June_EDU_recp_by_Training_Type.csv",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2010-10-01T04:00:00Z/2011-06-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/FY11_June_EDU_recp_by_Training_Type.csv"
-            ],
-            "keyword": [
-                "education",
-                "veteran"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Salminio Garner",
                 "hasEmail": "mailto:salminio.garner1@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-EDU2011-002",
+            "dataQuality": true,
             "description": "<p>FY 11 Education Recipients by training type  and VA Education Benefit Program (Through June FY11). The data represents the number of individuals by VA education program who have used their VA education benefit during fiscal year 2011(Through the June FY11). Training type statistics may include individuals who used their education benefits in more than one training type, therefore the total within this table may be different than the total number of beneficiaries during the fiscal year.</p>",
-            "title": "EOM June FY 11 Education Recipients by Training Type and VA Education Benefit Program",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29622,65 +29602,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/be4x-ietg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/be4x-ietg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/be4x-ietg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/be4x-ietg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/be4x-ietg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/be4x-ietg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/be4x-ietg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/be4x-ietg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/be4x-ietg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-EDU2011-002",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "education",
+                "veteran"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/FY11_June_EDU_recp_by_Training_Type.csv",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/VETDATA/docs/Datagov/FY11_June_EDU_recp_by_Training_Type.csv"
+            ],
+            "temporal": "2010-10-01T04:00:00Z/2011-06-30T04:00:00Z",
             "theme": [
                 "Section 4. Education"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "EOM June FY 11 Education Recipients by Training Type and VA Education Benefit Program"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/beyn-kshi",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-11-01T04:00:00Z/2014-11-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "debt referral"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vikki Soukup",
                 "hasEmail": "mailto:Vikki.Soukup@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-108",
             "description": "<p>Debt referrals to credit reporting agencies and the treasury offset program.</p>",
-            "title": "COIN 0146 MONTHLY TOP TOTALS REPORT Nov 2014",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29688,41 +29671,42 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-108",
+            "issued": "2017-07-26",
+            "keyword": [
+                "debt referral"
+            ],
+            "landingPage": "https://www.data.va.gov/d/beyn-kshi",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2014-11-01T04:00:00Z/2014-11-30T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "COIN 0146 MONTHLY TOP TOTALS REPORT Nov 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/bfre-mkpi",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-08-15",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "rural veterans",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rural Veterans by State (2015)",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "0950b2ee-a159-4321-a420-3ca83113993b",
+            "dataQuality": true,
             "description": "<p>This spreadsheet contains data from the 2015 American Community Survey and shows the demographic and socioeconomic characteristics of Veterans who live in rural and urban areas.  The spreadsheet includes variables like:  raw numbers, unemployment rate, disability rate, median personal income, age groups, period of service and other variables.</p>",
-            "title": "Rural Veterans by State (2015)",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29730,36 +29714,36 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "0950b2ee-a159-4321-a420-3ca83113993b",
+            "issued": "2017-08-15",
+            "keyword": [
+                "rural veterans",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/bfre-mkpi",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Rural Veterans by State (2015)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/bha8-j4n5",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "louisiana"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:tom.garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-188",
             "description": "<p>This summary describes the programs and services VA provided in Louisiana in fiscal year 2015.</p>",
-            "title": "State Summary: Louisiana",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29768,24 +29752,43 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-OEI-OEI-188",
+            "issued": "2017-07-26",
+            "keyword": [
+                "louisiana"
+            ],
+            "landingPage": "https://www.data.va.gov/d/bha8-j4n5",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "State Summary: Louisiana"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/bhqz-62fb",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1992-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The Clinical Case Registries (CCR) replaced the former Immunology Case Registry and the Hepatitis C Case Registry with local and national databases. The CCR:HIV and CCR:HCV are administrative and clinical databases designed to provide population-based data on VA patients infected with Human Immunodeficiency Virus (HIV) and/or Hepatitis C virus (HCV).  Each Veterans Health Information Systems and Technology Architecture (VistA) system contains a local CCR where patients who are potentially HIV or HCV infected are identified based on International Classification of Diseases (ICD-9) codes and/or positive antibody test results. The local HIV or HCV coordinator must review these cases to determine which patients are truly infected and should be added to the local registry. The local CCR provides extensive reporting capabilities to the local HIV and HCV clinicians to monitor their patient population. The local CCR software also extracts data elements from multiple VistA packages and transmits Health Level Seven (HL7) messages to the national database at VA Austin Information Technology Center. The national database is used for monitoring clinical outcomes, assessing resource utilization and quality assurance.</p>",
+            "identifier": "VA-VHA-OPH-003",
+            "issued": "2017-07-26",
             "keyword": [
                 "aids",
                 "health",
@@ -29799,61 +29802,42 @@
                 "veteran",
                 "vista"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/bhqz-62fb",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:040"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-OPH-003",
-            "description": "<p>The Clinical Case Registries (CCR) replaced the former Immunology Case Registry and the Hepatitis C Case Registry with local and national databases. The CCR:HIV and CCR:HCV are administrative and clinical databases designed to provide population-based data on VA patients infected with Human Immunodeficiency Virus (HIV) and/or Hepatitis C virus (HCV).  Each Veterans Health Information Systems and Technology Architecture (VistA) system contains a local CCR where patients who are potentially HIV or HCV infected are identified based on International Classification of Diseases (ICD-9) codes and/or positive antibody test results. The local HIV or HCV coordinator must review these cases to determine which patients are truly infected and should be added to the local registry. The local CCR provides extensive reporting capabilities to the local HIV and HCV clinicians to monitor their patient population. The local CCR software also extracts data elements from multiple VistA packages and transmits Health Level Seven (HL7) messages to the national database at VA Austin Information Technology Center. The national database is used for monitoring clinical outcomes, assessing resource utilization and quality assurance.</p>",
-            "title": "Clinical Case Registries (CCR)",
-            "programCode": [
-                "029:040"
-            ],
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "1992-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Clinical Case Registries (CCR)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/bi2v-v4rk",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 106"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/bi2v-v4rk",
+            "dataQuality": true,
             "description": "<p>VBA SPECIALLY ADAPTED HOUSING BENEFIT PROGRAMS. The Specially Adapted Housing (SAH) grant program helps Veterans with certain service-connected disabilities live independently in a barrier-free environment. SAH grants can be used in one of the following ways: (1) construct a suitable home on suitable land either already owned or to be acquired by the veteran, or (2) remodel an existing home if it can be suitably adapted, or (3) acquire a suitably adapted home or reduce the outstanding mortgage on a suitably adapted home already owned by the veteran. b. The Special Housing Adaptation (SHA) grant program helps veterans with certain service-connected disabilities adapt or purchase a home to accommodate the disability. SHA grants can be used in one of the following ways: (1) adapt an existing home the veteran or a family member already owns in which the veteran lives; (2) adapt a home the veteran or family member intends to purchase in which the veteran will live; (3) help a veteran purchase a home already adapted in which the veteran will live. c. . The Temporary Residence Adaptations (TRA) program provides adaptation assistance to veterans who are residing, but do not intend to permanently reside, in the a residence owned by a family member. If a veteran is otherwise eligible for SAH or SHA, the assistance is limited. d. SAH and SHA grants may be used up to three times, as long as the aggregate grant amount does not exceed the statutory dollar limitation. TRA grants may only be used once (and count as a grant usage for purposes of the limit of three), and the amount of assistance provided will be subtracted from the veteran's available statutory maximum.</p>",
-            "title": "USA SPENDING CH39 B106 SPECIALLY ADAPTED HOUSING FOR DISABLED VETERANS JAN2019",
-            "isPartOf": "bc3a6e1f-3fb0-4fb1-8b07-59efaf92222b",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29861,61 +29845,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/bi2v-v4rk/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/bi2v-v4rk/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/bi2v-v4rk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/bi2v-v4rk/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/bi2v-v4rk/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/bi2v-v4rk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/bi2v-v4rk/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/bi2v-v4rk/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/bi2v-v4rk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/bi2v-v4rk",
+            "isPartOf": "bc3a6e1f-3fb0-4fb1-8b07-59efaf92222b",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 106"
+            ],
+            "landingPage": "https://www.data.va.gov/d/bi2v-v4rk",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING CH39 B106 SPECIALLY ADAPTED HOUSING FOR DISABLED VETERANS JAN2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/bifp-gvdp",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "ogc",
-                "opinion"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "OGC Law Library",
                 "hasEmail": "mailto:OGCLawLibrary@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OGC-040",
             "description": "<p>Clothing Allowance Benefit \u2013 38 U.S.C. \u00a7 1162 and attach to this the first opinion attached.</p>",
-            "title": "OGC Precedent Opinion 4-2010",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29924,73 +29907,73 @@
                     "title": "OGC Precedent Opinion 4-2010"
                 }
             ],
+            "identifier": "VA-OGC-040",
+            "issued": "2017-07-26",
+            "keyword": [
+                "ogc",
+                "opinion"
+            ],
+            "landingPage": "https://www.data.va.gov/d/bifp-gvdp",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:083"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "OGC Precedent Opinion 4-2010"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/bjgd-xnjp",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-07-13",
-            "keyword": [
-                "oklahoma",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VANCVAS",
                 "hasEmail": "mailto:VANCVAS@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/bjgd-xnjp",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Oklahoma",
+            "identifier": "https://www.data.va.gov/api/views/bjgd-xnjp",
+            "issued": "2021-08-26",
+            "keyword": [
+                "oklahoma",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/bjgd-xnjp",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-07-13",
             "programCode": [
                 "029:086"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summaries_Oklahoma"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/FUND/VA_Franchise_Fund_Annual_Reports.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2003-10-01T04:00:00Z/2004-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-10",
-            "keyword": [
-                "annual report",
-                "franchise fund",
-                "fy 2004"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VA OM Open Data",
                 "hasEmail": "mailto:VAOMOpenData@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-041",
+            "dataQuality": true,
             "description": "<p>Franchise Fund FY 2004 Annual Report</p>",
-            "title": "Franchise Fund FY 2004 Annual Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -29999,27 +29982,47 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-041",
+            "issued": "2017-07-26",
+            "keyword": [
+                "annual report",
+                "franchise fund",
+                "fy 2004"
+            ],
+            "landingPage": "https://www.va.gov/FUND/VA_Franchise_Fund_Annual_Reports.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-06-10",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2003-10-01T04:00:00Z/2004-09-30T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Franchise Fund FY 2004 Annual Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/bk5m-88q6",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The Resident Assessment Instrument/Minimum Data Set (RAI/MDS) is a comprehensive assessment and care planning process used by the nursing home industry since 1990 as a requirement for nursing home participation in the Medicare and Medicaid programs. The RAI/MDS provides data for monitoring changes in resident status that are consistent and reliable over time. The VA commitment to quality propelled the implementation of the RAI/MDS in its nursing homes now known as VA Community Living Centers (CLC). In addition to providing consistent clinical information, the RAI/MDS can be used as a measure of both quality and resource utilization, thereby serving as a benchmark for quality and cost data within the VA as well as with community based nursing facilities. Workload based on RAI/MDS can be calculated electronically by the interactions of the elements of the MDS data and grouped into 53 categories referred to as Resource Utilization Groups (RUG-IV). Residents are assessed quarterly. The data is grouped for analysis at the Austin Information Technology Center (AITC). Conversion to electronic data entry and transmission to the AITC was completed system-wide by year-end 2000. In 2010, the Centeres for Medicare and Medicaide Services released a significantly upgraded version, MDS 3.0, to begin to be implemented on October 1, 2011 in VHA CLCs.  Training is underway currently.  The MDS 3.0 will generate a new set of Quality Indicators and Quality Monitors as well the RUGs will increase to 64 RUGs from the current 53 RUG groups.</p>",
+            "identifier": "VA-VHA-GER-003",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2001-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "assessment",
                 "benchmark",
@@ -30039,62 +30042,43 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/bk5m-88q6",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:054"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-GER-003",
-            "description": "<p>The Resident Assessment Instrument/Minimum Data Set (RAI/MDS) is a comprehensive assessment and care planning process used by the nursing home industry since 1990 as a requirement for nursing home participation in the Medicare and Medicaid programs. The RAI/MDS provides data for monitoring changes in resident status that are consistent and reliable over time. The VA commitment to quality propelled the implementation of the RAI/MDS in its nursing homes now known as VA Community Living Centers (CLC). In addition to providing consistent clinical information, the RAI/MDS can be used as a measure of both quality and resource utilization, thereby serving as a benchmark for quality and cost data within the VA as well as with community based nursing facilities. Workload based on RAI/MDS can be calculated electronically by the interactions of the elements of the MDS data and grouped into 53 categories referred to as Resource Utilization Groups (RUG-IV). Residents are assessed quarterly. The data is grouped for analysis at the Austin Information Technology Center (AITC). Conversion to electronic data entry and transmission to the AITC was completed system-wide by year-end 2000. In 2010, the Centeres for Medicare and Medicaide Services released a significantly upgraded version, MDS 3.0, to begin to be implemented on October 1, 2011 in VHA CLCs.  Training is underway currently.  The MDS 3.0 will generate a new set of Quality Indicators and Quality Monitors as well the RUGs will increase to 64 RUGs from the current 53 RUG groups.</p>",
-            "title": "Resident Assessment Instrument/Minimum Data Set (RAI/MDS)",
-            "programCode": [
-                "029:054"
-            ],
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2001-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Resident Assessment Instrument/Minimum Data Set (RAI/MDS)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/budget/products.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2015-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-10",
-            "keyword": [
-                "budget",
-                "fy2015"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VA OM Open Data",
                 "hasEmail": "mailto:VAOMOpenData@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-098",
+            "dataQuality": true,
             "description": "<p>FY 2015 Budget Submission Volume II: Medical Programs and Information Technology Programs</p>",
-            "title": "FY 2015 Budget Submission Volume II",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30103,43 +30087,44 @@
                     "title": "FY 2015 Budget Submission"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-098",
+            "issued": "2017-07-26",
+            "keyword": [
+                "budget",
+                "fy2015"
+            ],
+            "landingPage": "https://www.va.gov/budget/products.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-06-10",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2014-10-01T04:00:00Z/2015-09-30T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 2015 Budget Submission Volume II"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/bpe7-d8rh",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-10-29",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "keyword": [
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "5b9b18eb-5079-43b6-bf49-a3800302f245",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary District of Columbia FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30147,45 +30132,43 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "5b9b18eb-5079-43b6-bf49-a3800302f245",
+            "issued": "2018-10-29",
+            "keyword": [
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/bpe7-d8rh",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-12",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data",
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "State Summary District of Columbia FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/budget/report/",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2006-01-01T05:00:00Z/2006-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "accountability",
-                "performance",
-                "report"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David Zlowe",
                 "hasEmail": "mailto:David.Zlowe@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-013",
+            "dataQuality": true,
             "description": "<p>2006 VA Performance and Accountability Report.</p>",
-            "title": "2006 VA Performance and Accountability Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30194,46 +30177,44 @@
                     "title": "zip"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-013",
+            "issued": "2017-07-26",
+            "keyword": [
+                "accountability",
+                "performance",
+                "report"
+            ],
+            "landingPage": "https://www.va.gov/budget/report/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2006-01-01T05:00:00Z/2006-12-31T05:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2006 VA Performance and Accountability Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/bpyp-2skf",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2002-10-01T04:00:00Z/2003-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-10",
-            "keyword": [
-                "annual report",
-                "financial statements",
-                "franchise fund"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VA OM Open Data",
                 "hasEmail": "mailto:VAOMOpenData@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-115",
             "description": "<p>FY 2003 Franchise Fund Annual Report Consolidated Financial Statements</p>",
-            "title": "FY 2003 Franchise Fund Annual Report Consolidated Financial Statements",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30242,49 +30223,47 @@
                     "title": "FY 2003 Franchise Fund Annual Report Consolidated Financial Statements"
                 }
             ],
+            "identifier": "VA-OM-OM-115",
+            "issued": "2017-07-26",
+            "keyword": [
+                "annual report",
+                "financial statements",
+                "franchise fund"
+            ],
+            "landingPage": "https://www.data.va.gov/d/bpyp-2skf",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-06-10",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2002-10-01T04:00:00Z/2003-09-30T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "FY 2003 Franchise Fund Annual Report Consolidated Financial Statements"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/health/",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-10-01T04:00:00Z/2013-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cboc",
-                "health",
-                "healthcare",
-                "outpatient",
-                "outpatient clinic",
-                "va",
-                "va clinics",
-                "veteran"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VHA Open Data",
                 "hasEmail": "mailto:vhaopendata@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VHA-OIA-115",
-            "description": "<p>Community Based Outpatient Clinics (CBOCs) at the end of Fiscal Year 2013. Data includes number of unique patients and clinic encounters.</p>",
-            "title": "VA Community Based Outpatient Clinics, FY2013",
+            "dataQuality": true,
+            "describedBy": "https://github.com/department-of-veterans-affairs/VA_Data_Assets_VHA/raw/master/VA_DataDefinitions_VisitsBedsCBOC_2015.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "029:042"
-            ],
+            "description": "<p>Community Based Outpatient Clinics (CBOCs) at the end of Fiscal Year 2013. Data includes number of unique patients and clinic encounters.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30292,77 +30271,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/bqa8-ptxs/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/bqa8-ptxs/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/bqa8-ptxs/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/bqa8-ptxs/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/bqa8-ptxs/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/bqa8-ptxs/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/bqa8-ptxs/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/bqa8-ptxs/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/bqa8-ptxs/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://github.com/department-of-veterans-affairs/VA_Data_Assets_VHA/raw/master/VA_DataDefinitions_VisitsBedsCBOC_2015.pdf",
-            "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
+            "identifier": "VA-VHA-OIA-115",
+            "issued": "2017-07-26",
+            "keyword": [
+                "cboc",
+                "health",
+                "healthcare",
+                "outpatient",
+                "outpatient clinic",
+                "va",
+                "va clinics",
+                "veteran"
+            ],
+            "landingPage": "https://www.va.gov/health/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:042"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
+            "temporal": "2012-10-01T04:00:00Z/2013-09-30T04:00:00Z",
             "theme": [
                 "VA Healthcare Utilization"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA Community Based Outpatient Clinics, FY2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/br8p-iseu",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2024-04-23",
-            "@type": "dcat:Dataset",
-            "modified": "2024-04-23",
-            "keyword": [
-                "2023",
-                "2023 pension",
-                "fy2023",
-                "fy 2023",
-                "fy 2023 pension",
-                "fy2023 pension",
-                "fy23",
-                "fy 23",
-                "fy 23 pension",
-                "fy23 pension",
-                "pension",
-                "state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Mike Schwaber",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/br8p-iseu",
+            "dataQuality": true,
             "description": "This report provides state-level estimates of the number of Veterans who were receiving VA Pension benefits as of the end of fiscal year 2023. It includes the Veterans\u2019 gender. Blank values represent small cell counts that have been suppressed to protect the identity of Veterans as well as some cell counts that have been suppressed in order to prevent the determination of the values of the aforementioned small cell counts. Some categories may not sum to the total due to missing information (e.g., gender, etc.).\n\nThe availability of gender data is limited as some records have no gender available. In the table, there are 123 Veterans whose gender is not available.\n\nThere are a small number of pension recipients for whom neither state nor country could be determined from the data sources used.  These pension recipients are not included in the table.\n\nThe number of Veterans who were pension recipients during FY 2023 but were no longer pension recipients at the end of FY 2023 is 32,176.  These Veterans are not included in the table.\n\nSource: Department of Veterans Affairs, Office of Enterprise Integration, Veteran Object FY23 data and Veterans Benefits Administration VETSNET FY 2023 pension data.\n\nPrepared by National Center for Veterans Analysis & Statistics, www.va.gov/vetdata.",
-            "title": "FY 2023 Pension Recipients by State",
-            "programCode": [
-                "029:009"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30370,62 +30345,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/br8p-iseu/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/br8p-iseu/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/br8p-iseu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/br8p-iseu/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/br8p-iseu/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/br8p-iseu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/br8p-iseu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/br8p-iseu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/br8p-iseu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y",
-            "language": [
-                "English"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/bsqp-yupb",
-            "bureauCode": [
-                "029:40"
-            ],
-            "issued": "2019-05-29",
-            "temporal": "2020-09-30T00:00:00Z/2020-09-30T00:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-21",
+            "identifier": "https://www.data.va.gov/api/views/br8p-iseu",
+            "issued": "2024-04-23",
             "keyword": [
-                "va performance"
+                "2023",
+                "2023 pension",
+                "fy2023",
+                "fy 2023",
+                "fy 2023 pension",
+                "fy2023 pension",
+                "fy23",
+                "fy 23",
+                "fy 23 pension",
+                "fy23 pension",
+                "pension",
+                "state"
+            ],
+            "landingPage": "https://www.data.va.gov/d/br8p-iseu",
+            "language": [
+                "English"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-04-23",
+            "programCode": [
+                "029:009"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "FY 2023 Pension Recipients by State"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "029:40"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Gretchen DePasquale",
                 "hasEmail": "mailto:Gretchen.DePasquale@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "7caba99c-eb3e-4b4d-bdce-93e80bad2c78",
+            "dataQuality": true,
             "description": "<p>This Excel file contains two spreadsheets: one for performance results in FY 2018 and a second containing performance measures and targets for FYs 2019 and 2020.</p>",
-            "title": "Department of Veterans Affairs FY 2020 Annual Performance Plan",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30433,106 +30417,105 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "7caba99c-eb3e-4b4d-bdce-93e80bad2c78",
+            "issued": "2019-05-29",
+            "keyword": [
+                "va performance"
+            ],
+            "landingPage": "https://www.data.va.gov/d/bsqp-yupb",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-21",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2020-09-30T00:00:00Z/2020-09-30T00:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Department of Veterans Affairs FY 2020 Annual Performance Plan"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/bswg-6jzm",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-08",
-            "keyword": [
-                "georgia",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VANCVAS",
                 "hasEmail": "mailto:VANCVAS@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/bswg-6jzm",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Georgia",
+            "identifier": "https://www.data.va.gov/api/views/bswg-6jzm",
+            "issued": "2021-08-26",
+            "keyword": [
+                "georgia",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/bswg-6jzm",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-08",
             "programCode": [
                 "029:086"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summaries_Georgia"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/btw6-zj4c",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VA Open Data",
+                "hasEmail": "mailto:OITOpenData@va.gov"
+            },
+            "description": "This page provides some instructions, tips, and videos to help you perform common tasks on the platform. It also contains links to more in-depth help content.",
+            "identifier": "https://www.data.va.gov/api/views/btw6-zj4c",
             "issued": "2019-10-16",
-            "@type": "dcat:Dataset",
-            "modified": "2020-04-10",
             "keyword": [
                 "data portal",
                 "faq",
                 "help"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VA Open Data",
-                "hasEmail": "mailto:OITOpenData@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/btw6-zj4c",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-04-10",
+            "programCode": [
+                "029:001"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/btw6-zj4c",
-            "description": "This page provides some instructions, tips, and videos to help you perform common tasks on the platform. It also contains links to more in-depth help content.",
-            "title": "How to get Started Using our Platform",
-            "programCode": [
-                "029:001"
-            ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "title": "How to get Started Using our Platform"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/bu46-h759",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2015-01-01T05:00:00Z/2015-01-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-21",
-            "keyword": [
-                "debt referalls"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vikki Soukup",
                 "hasEmail": "mailto:Vikki.Soukup@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-125",
             "description": "<p>Debt referrals to credit reporting agencies and the treasury offset program.</p>",
-            "title": "COIN 0146 MONTHLY TOP TOTALS REPORT JAN 2015",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30540,41 +30523,42 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-125",
+            "issued": "2017-07-26",
+            "keyword": [
+                "debt referalls"
+            ],
+            "landingPage": "https://www.data.va.gov/d/bu46-h759",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-21",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2015-01-01T05:00:00Z/2015-01-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "COIN 0146 MONTHLY TOP TOTALS REPORT JAN 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/bu8u-bu43",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-27",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 109"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/bu8u-bu43",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to compensate veterans for disabilities incurred or aggravated during military service according to the average impairment in earning capacity such disability would cause in civilian occupations. Persons who have suffered disabilities resulting from service in the Armed Forces of the United States. The disability must have been incurred or aggravated by service in the line of duty. Separation from service must have been under other than dishonorable conditions for the period in which the disability was incurred or aggravated.</p>",
-            "title": "USA SPENDING C&P B109 VETERANS COMPENSATION FOR SERVICE-CONNECTED DISABILITY MAR2019",
-            "isPartOf": "6013cae5-a8c2-47ff-9c90-9cbdba7bda63",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30582,121 +30566,119 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/bu8u-bu43/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/bu8u-bu43/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/bu8u-bu43/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/bu8u-bu43/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/bu8u-bu43/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/bu8u-bu43/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/bu8u-bu43/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/bu8u-bu43/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/bu8u-bu43/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/bu8u-bu43",
+            "isPartOf": "6013cae5-a8c2-47ff-9c90-9cbdba7bda63",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 109"
+            ],
+            "landingPage": "https://www.data.va.gov/d/bu8u-bu43",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING C&P B109 VETERANS COMPENSATION FOR SERVICE-CONNECTED DISABILITY MAR2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/buhd-duk4",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Indiana FY2023",
+            "identifier": "https://www.data.va.gov/api/views/buhd-duk4",
             "issued": "2024-06-02",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-11",
             "keyword": [
                 "fy2024",
                 "indiana",
                 "ncvas state summary"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/buhd-duk4",
+            "modified": "2024-07-11",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/buhd-duk4",
-            "description": "NCVAS State Summary Indiana FY2023",
-            "title": "NCVAS State Summary Indiana FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Indiana FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/bumw-yk6w",
-            "issued": "2024-05-29",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-11",
-            "keyword": [
-                "ncvas state summary. illinois. fy2024"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Florinda Balfour",
                 "hasEmail": "mailto:VACONCVAS@VA.GOV"
             },
+            "description": "NCVAS State Summary Illinois FY2023",
+            "identifier": "https://www.data.va.gov/api/views/bumw-yk6w",
+            "issued": "2024-05-29",
+            "keyword": [
+                "ncvas state summary. illinois. fy2024"
+            ],
+            "landingPage": "https://www.data.va.gov/d/bumw-yk6w",
+            "modified": "2024-07-11",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/bumw-yk6w",
-            "description": "NCVAS State Summary Illinois FY2023",
-            "title": "NCVAS State Summary Illinois FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Illinois FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/buv8-w97u",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-01-01T05:00:00Z/2015-07-28T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "development",
-                "history",
-                "nca"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James Killens III",
                 "hasEmail": "mailto:james.killensiii@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-NCA-MP-014",
+            "dataQuality": true,
             "description": "<p>This document provides information on the history of the National Cemetery Administration.</p>",
-            "title": "History and Development of the National Cemetery Administration",
-            "programCode": [
-                "029:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30705,46 +30687,43 @@
                     "title": "History and Development of the National Cemetery Administration"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-NCA-MP-014",
+            "issued": "2017-07-26",
+            "keyword": [
+                "development",
+                "history",
+                "nca"
+            ],
+            "landingPage": "https://www.data.va.gov/d/buv8-w97u",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2014-01-01T05:00:00Z/2015-07-28T04:00:00Z",
             "theme": [
                 "History"
-            ]
+            ],
+            "title": "History and Development of the National Cemetery Administration"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/VGLI_Coverage_Amount_by_State_February_2012.csv",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-02-01T05:00:00Z/2012-02-29T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_VGLI_Coverage_Amount_by_State_3.doc"
-            ],
-            "keyword": [
-                "benefits",
-                "insurance",
-                "state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dusca Fichtel",
                 "hasEmail": "mailto:dusca.fichtel@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-INS2012-018",
+            "dataQuality": true,
             "description": "<p>Provides the amount of Veterans' Group Life Insurance (VGLI) coverage by state.  This report provides a snapshot of the amount of VGLI coverage as of February 29, 2012.  For members who reside outside the United States, coverage is not identified by individual country.  The total amount of coverage was captured to ensure 100% of the population was identified in the report.</p>",
-            "title": "VGLI Coverage Amount by State by 2012-02-29",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30752,67 +30731,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/bv9n-5ar9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/bv9n-5ar9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/bv9n-5ar9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/bv9n-5ar9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/bv9n-5ar9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/bv9n-5ar9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/bv9n-5ar9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/bv9n-5ar9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/bv9n-5ar9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2012-018",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/VGLI_Coverage_Amount_by_State_February_2012.csv",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/VETDATA/docs/Datagov/Technical_Notes_VGLI_Coverage_Amount_by_State_3.doc"
+            ],
+            "temporal": "2012-02-01T05:00:00Z/2012-02-29T05:00:00Z",
             "theme": [
                 "Section 1. Population"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VGLI Coverage Amount by State by 2012-02-29"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/bw4s-p8kp",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "congressional district",
-                "state",
-                "va facilities"
-            ],
             "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Florinda Balfour",
                 "hasEmail": "mailto:florinda.balfour@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-069",
             "description": "<p>National Center for Veterans Analysis and Statistics aggregates a list of VA Facilities by State, Congressional District, and Congressional District Representatives</p>",
-            "title": "Department of Veterans Affairs Facilities by State",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30821,51 +30803,46 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-OEI-OEI-069",
+            "issued": "2017-07-26",
+            "keyword": [
+                "congressional district",
+                "state",
+                "va facilities"
+            ],
+            "landingPage": "https://www.data.va.gov/d/bw4s-p8kp",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "Department of Veterans Affairs Facilities by State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/bwbs-yum6",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2008-10-01T04:00:00Z/2009-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/vetdata/docs/VHA_2009_Facility_Quality_and_Safety_Report_Final.pdf"
-            ],
-            "keyword": [
-                "health",
-                "healthcare",
-                "hospital accreditation",
-                "patient safety",
-                "quality of care",
-                "satisfaction",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VHA Open Data",
                 "hasEmail": "mailto:vhaopendata@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VHA-OIA-002",
-            "description": "<p>The 2008 Hospital Report Card was mandated by the FY08 Appropriations Act, and focused on Congressionally-mandated metrics applicable to general patient populations. The 2009 VHA Facility Quality and Safety Repor report, not required by Congress, shifts to Veteran-centered metrics, and includes information related to infrastructure, care provided in outpatient and hospital settings, quality of care within given patient populations, accreditation status, patient satisfaction and patient outcomes for FY2008.  The data in this report have been compiled from multiple sources throughout VHA. This dataset  is a compilation of available services within each medical center, whether a medical center is accreditated by Joint commission and/or CARF and details the number of admissions by bed section, admissions per 1000 uniques, and average length of stay by bed sections. Total number of outpatient visits, number of unique patients and the medical center staffing.</p>",
-            "title": "2009 VHA Facility Quality and Safety Report - Infrastructure",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/vetdata/docs/VHA_Facility_Quality_and_Safety_Report_Infrastructure_Data_Elements.doc",
             "describedByType": "application/msword",
-            "programCode": [
-                "029:040"
-            ],
+            "description": "<p>The 2008 Hospital Report Card was mandated by the FY08 Appropriations Act, and focused on Congressionally-mandated metrics applicable to general patient populations. The 2009 VHA Facility Quality and Safety Repor report, not required by Congress, shifts to Veteran-centered metrics, and includes information related to infrastructure, care provided in outpatient and hospital settings, quality of care within given patient populations, accreditation status, patient satisfaction and patient outcomes for FY2008.  The data in this report have been compiled from multiple sources throughout VHA. This dataset  is a compilation of available services within each medical center, whether a medical center is accreditated by Joint commission and/or CARF and details the number of admissions by bed section, admissions per 1000 uniques, and average length of stay by bed sections. Total number of outpatient visits, number of unique patients and the medical center staffing.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -30873,51 +30850,86 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/bwbs-yum6/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/bwbs-yum6/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/bwbs-yum6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/bwbs-yum6/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/bwbs-yum6/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/bwbs-yum6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/bwbs-yum6/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/bwbs-yum6/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/bwbs-yum6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://www.va.gov/vetdata/docs/VHA_Facility_Quality_and_Safety_Report_Infrastructure_Data_Elements.doc",
-            "dataQuality": true,
+            "identifier": "VA-VHA-OIA-002",
+            "issued": "2017-07-26",
+            "keyword": [
+                "health",
+                "healthcare",
+                "hospital accreditation",
+                "patient safety",
+                "quality of care",
+                "satisfaction",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/bwbs-yum6",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:040"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/vetdata/docs/VHA_2009_Facility_Quality_and_Safety_Report_Final.pdf"
+            ],
+            "temporal": "2008-10-01T04:00:00Z/2009-09-30T04:00:00Z",
             "theme": [
                 "Section 3. Health and Nutrition"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2009 VHA Facility Quality and Safety Report - Infrastructure"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "accrualPeriodicity": "R/P2M",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2015-02-15T05:00:00Z/2015-02-15T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/health/access-audit.asp"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/access-audit.asp",
+            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/15_February_2015_Public_Data_Pending_03192015.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Pending Appointments 15 Feb 2015"
+                }
             ],
+            "identifier": "VA-VHA-OIA-097",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -30931,73 +30943,42 @@
                 "wait list",
                 "wait time"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:041"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-OIA-097",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 Feb 15",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/15_February_2015_Public_Data_Pending_03192015.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Pending Appointments 15 Feb 2015"
-                }
-            ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2015-02-15T05:00:00Z/2015-02-15T05:00:00Z",
             "theme": [
                 "Accelerating Access",
                 "Pending Appointments"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 Feb 15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/bx88-z2b2",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2023-06-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-26",
-            "keyword": [
-                "fy2021",
-                "ncvas",
-                "state summary",
-                "va expenditures"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/bx88-z2b2",
             "description": "FY2021 VA expenditures data provided by the National Center for Veterans Analysis and Statistics, published in 2023.",
-            "title": "FY 2021_NCVAS Expenditures Data For State Summaries",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31005,59 +30986,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/bx88-z2b2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/bx88-z2b2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/bx88-z2b2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/bx88-z2b2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/bx88-z2b2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/bx88-z2b2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/bx88-z2b2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/bx88-z2b2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/bx88-z2b2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/bx88-z2b2",
+            "issued": "2023-06-13",
+            "keyword": [
+                "fy2021",
+                "ncvas",
+                "state summary",
+                "va expenditures"
+            ],
+            "landingPage": "https://www.data.va.gov/d/bx88-z2b2",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-08-26",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "FY 2021_NCVAS Expenditures Data For State Summaries"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/byjw-yeir",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-01-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cemetaries",
-                "map",
-                "statistics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vicki Cordes",
                 "hasEmail": "mailto:noemailprovided@usa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/byjw-yeir",
+            "dataQuality": true,
             "description": "<p>Data assets for <a href=\"https://www.data.va.gov/story/national-cemetery-administration\">https://www.data.va.gov/story/national-cemetery-administration</a>.</p>",
-            "title": "USVA Cemetery Sites",
-            "isPartOf": "8ea07f95-2a7f-494d-a275-5420bcd938fb",
-            "programCode": [
-                "029:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31065,46 +31047,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/byjw-yeir/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/byjw-yeir/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/byjw-yeir/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/byjw-yeir/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/byjw-yeir/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/byjw-yeir/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/byjw-yeir/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/byjw-yeir/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/byjw-yeir/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/byjw-yeir",
+            "isPartOf": "8ea07f95-2a7f-494d-a275-5420bcd938fb",
+            "issued": "2017-01-24",
+            "keyword": [
+                "cemetaries",
+                "map",
+                "statistics"
+            ],
+            "landingPage": "https://www.data.va.gov/d/byjw-yeir",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "USVA Cemetery Sites"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/byue-sdxz",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>Civilian Health and Medical Program of the Department of Veterans Affairs (CHAMPVA) is a health care benefit program designed for the dependents of certain Veterans. Administered by the Health Administration Center (HAC), Denver, Colorado, CHAMPVA shares the cost of necessary health care services and supplies with eligible beneficiaries. The CHAMPVA Eligibility &amp; Payment Functions (CVA) database is used by HAC for the administration of the CHAMPVA program.</p>",
+            "identifier": "VA-VHA-CBO-002",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1987-01-01T05:00:00Z/2013-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "benefit",
                 "champva",
@@ -31115,66 +31118,42 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/byue-sdxz",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:066"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-CBO-002",
-            "description": "<p>Civilian Health and Medical Program of the Department of Veterans Affairs (CHAMPVA) is a health care benefit program designed for the dependents of certain Veterans. Administered by the Health Administration Center (HAC), Denver, Colorado, CHAMPVA shares the cost of necessary health care services and supplies with eligible beneficiaries. The CHAMPVA Eligibility &amp; Payment Functions (CVA) database is used by HAC for the administration of the CHAMPVA program.</p>",
-            "title": "Civilian Health and Medical Program of the Department of Veterans Affairs (CHAMPVA)",
-            "programCode": [
-                "029:066"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "temporal": "1987-01-01T05:00:00Z/2013-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Civilian Health and Medical Program of the Department of Veterans Affairs (CHAMPVA)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Number_of_Veterans_Enrolled_in_VGLI_by_State.csv",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2011-10-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/TechnicalNotesVGLI_Coverage_Amount_by_State.doc"
-            ],
-            "keyword": [
-                "benefits",
-                "insurance",
-                "state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dusca Fichtel",
                 "hasEmail": "mailto:dusca.fichtel@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-INS2011-017",
+            "dataQuality": true,
             "description": "<p>Provides the number of Veterans insured under the Veterans' Group Life Insurance (VGLI) program by state.  This report provides a snapshot of the active VGLI membership as of October 31, 2011.  For members who reside outside the United States, membership is not identified by individual country.  The total number of members was captured to ensure 100% of the population was identified in the report.</p>",
-            "title": "FY11_EOM_OCT_Number of Veterans Insured by VGLI by State as of October 31, 2011",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31182,91 +31161,96 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/bzgc-83jt/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/bzgc-83jt/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/bzgc-83jt/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/bzgc-83jt/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/bzgc-83jt/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/bzgc-83jt/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/bzgc-83jt/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/bzgc-83jt/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/bzgc-83jt/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2011-017",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Number_of_Veterans_Enrolled_in_VGLI_by_State.csv",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/VETDATA/docs/Datagov/TechnicalNotesVGLI_Coverage_Amount_by_State.doc"
+            ],
+            "temporal": "2011-10-01T04:00:00Z/2011-10-30T04:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY11_EOM_OCT_Number of Veterans Insured by VGLI by State as of October 31, 2011"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/bzjr-km3v",
-            "issued": "2023-06-19",
             "@type": "dcat:Dataset",
-            "modified": "2024-05-20",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Delaware FY2021",
+            "identifier": "https://www.data.va.gov/api/views/bzjr-km3v",
+            "issued": "2023-06-19",
             "keyword": [
                 "delaware",
                 "fy2021 data",
                 "ncvas state summary"
             ],
-            "identifier": "https://www.data.va.gov/api/views/bzjr-km3v",
+            "landingPage": "https://www.data.va.gov/d/bzjr-km3v",
+            "modified": "2024-05-20",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Delaware FY2021",
             "title": "NCVAS State Summary Delaware FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.data.va.gov/d/c2xv-2vkn",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2018-02-23",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "pharmacy"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Short",
                 "hasEmail": "mailto:vhaopendata@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "dcbd0744-db34-407a-924d-4b4f1de78f35",
+            "dataQuality": true,
             "description": "<p>The OneVA Pharmacy application design consists of 3 main components: VistA Medication Profile screen, Health Data Record Clinical Data Service (HDR/CDS), and OneVA Pharmacy message flow. The VistA Medication Profile screen expands available pharmacy information in VistA to provide pharmacists direct access to query, and refill patients active and refillable prescriptions. The HDR/CDS provides a patients active and refillable prescriptions. The OneVA Pharmacy message flow enables the secure, bi-directional exchange of electronic health records between local/remote VistA Servers, and between VistA servers and HDR.</p>",
-            "title": "OneVA Pharmacy",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31275,19 +31259,48 @@
                     "title": "OneVA Pharmacy"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "dcbd0744-db34-407a-924d-4b4f1de78f35",
+            "issued": "2018-02-23",
+            "keyword": [
+                "pharmacy"
+            ],
+            "landingPage": "https://www.data.va.gov/d/c2xv-2vkn",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
+            "title": "OneVA Pharmacy"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ptsd.va.gov/about/divisions/evaluation",
             "bureauCode": [
                 "029:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.data.va.gov/dataset/va-ptsd-veteran-patient-statistics-2014/resource/e7ecb39c-6a66-4e1e-b7e6-063f2934dadb",
+            "description": "<p>National-level, VISN-level, and/or VAMC-level statistics on the numbers and percentages of users of VHA care form the Northeast Program Evaluation Center (NEPEC).  Some datasets focus on PTSD others on mental health.  There is no record-level data.  Information is for fiscal year 2014.  <b> This dataset is no longer supported and is provided as-is. Any historical knowledge regarding meta data or it's creation is no longer available.  All known information is proved as part of this data set.</b></p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/c3fv-cihs/application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                }
+            ],
+            "identifier": "VA-VHA-10N-009",
+            "isPartOf": "VA-VHA-10N-014",
             "issued": "2017-07-26",
-            "temporal": "2013-10-01T04:00:00Z/2014-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2021-06-29",
             "keyword": [
                 "2014",
                 "disorder",
@@ -31302,68 +31315,38 @@
                 "veteran",
                 "vha"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.ptsd.va.gov/about/divisions/evaluation",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-06-29",
+            "programCode": [
+                "029:042"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-10N-009",
-            "description": "<p>National-level, VISN-level, and/or VAMC-level statistics on the numbers and percentages of users of VHA care form the Northeast Program Evaluation Center (NEPEC).  Some datasets focus on PTSD others on mental health.  There is no record-level data.  Information is for fiscal year 2014.  <b> This dataset is no longer supported and is provided as-is. Any historical knowledge regarding meta data or it's creation is no longer available.  All known information is proved as part of this data set.</b></p>",
-            "title": "VA PTSD Veteran Patient Statistics - 2014",
-            "isPartOf": "VA-VHA-10N-014",
-            "programCode": [
-                "029:042"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/c3fv-cihs/application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
-                }
-            ],
-            "describedBy": "https://www.data.va.gov/dataset/va-ptsd-veteran-patient-statistics-2014/resource/e7ecb39c-6a66-4e1e-b7e6-063f2934dadb",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2013-10-01T04:00:00Z/2014-09-30T04:00:00Z",
             "theme": [
                 "PTSD",
                 "Mental Health"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA PTSD Veteran Patient Statistics - 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/c3qm-38dv",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2019-09-19",
-            "@type": "dcat:Dataset",
-            "modified": "2021-07-19",
-            "keyword": [
-                "healthcare",
-                "rural veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VHA Office of Health Equity",
                 "hasEmail": "mailto:healthequity@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/c3qm-38dv",
             "description": "Summary level data from the National Veteran Health Equity Report - FY2013, filtered by geography.",
-            "title": "VA-OHE-NVHER-FY13-Sociodemographic-Geography",
-            "programCode": [
-                "029:048"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31371,93 +31354,89 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/c3qm-38dv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/c3qm-38dv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/c3qm-38dv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/c3qm-38dv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/c3qm-38dv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/c3qm-38dv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/c3qm-38dv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/c3qm-38dv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/c3qm-38dv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/c3qm-38dv",
+            "issued": "2019-09-19",
+            "keyword": [
+                "healthcare",
+                "rural veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/c3qm-38dv",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-07-19",
+            "programCode": [
+                "029:048"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VA-OHE-NVHER-FY13-Sociodemographic-Geography"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/c4jq-4xrn",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Georgia FY2023",
+            "identifier": "https://www.data.va.gov/api/views/c4jq-4xrn",
             "issued": "2024-05-23",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-22",
             "keyword": [
                 "fy2024 data",
                 "ga",
                 "ncvas state summary"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/c4jq-4xrn",
+            "modified": "2024-07-22",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/c4jq-4xrn",
-            "description": "NCVAS State Summary Georgia FY2023",
-            "title": "NCVAS State Summary Georgia FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Georgia FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www1.va.gov/VETDATA/docs/Datagov/FY_07_Insurance_Expenditure_by_CD_and_State.csv",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2007-01-01T05:00:00Z/2007-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www1.va.gov/VETDATA/docs/Datagov/FY_07_Insurance_Expenditure_by_CD_and_State.csv"
-            ],
-            "keyword": [
-                "expenditure",
-                "insurance",
-                "veteran"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dusca Fichtel",
                 "hasEmail": "mailto:dusca.fichtel@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-INS2007-001",
+            "dataQuality": true,
             "description": "<p>2007 Veteran life insurance expenditures by state and county.  Expenditures were derived from Insurance Actuarial reports that used the total Insurance program cash disbursed.  The total cash disbursed was prorated by in-force data by state, which was further prorated by county and congressional district.</p>",
-            "title": "2007 Veterans' Insurance Expenditure by State and Congressional District",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31465,67 +31444,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/c4wi-zwyv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/c4wi-zwyv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/c4wi-zwyv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/c4wi-zwyv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/c4wi-zwyv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/c4wi-zwyv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/c4wi-zwyv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/c4wi-zwyv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/c4wi-zwyv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2007-001",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "expenditure",
+                "insurance",
+                "veteran"
+            ],
+            "landingPage": "https://www1.va.gov/VETDATA/docs/Datagov/FY_07_Insurance_Expenditure_by_CD_and_State.csv",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www1.va.gov/VETDATA/docs/Datagov/FY_07_Insurance_Expenditure_by_CD_and_State.csv"
+            ],
+            "temporal": "2007-01-01T05:00:00Z/2007-12-31T05:00:00Z",
             "theme": [
                 "Section 9. Federal Government Finances and Employment"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2007 Veterans' Insurance Expenditure by State and Congressional District"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/c5xe-pgqq",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2021-02-20",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-24",
-            "keyword": [
-                "benefits",
-                "race/ethnicity",
-                "va programs",
-                "veteran"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tamara Lee",
                 "hasEmail": "mailto:vaconcvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/c5xe-pgqq",
             "description": "Take-up rate within 2 years of tranistioning out of military by race/ethnicity and VA Benefit or Service.",
-            "title": "Take-up Rate by Program and Race/Ethnicity",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31533,40 +31514,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/c5xe-pgqq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/c5xe-pgqq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/c5xe-pgqq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/c5xe-pgqq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/c5xe-pgqq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/c5xe-pgqq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/c5xe-pgqq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/c5xe-pgqq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/c5xe-pgqq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/c5xe-pgqq",
+            "issued": "2021-02-20",
+            "keyword": [
+                "benefits",
+                "race/ethnicity",
+                "va programs",
+                "veteran"
+            ],
+            "landingPage": "https://www.data.va.gov/d/c5xe-pgqq",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-02-24",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Take-up Rate by Program and Race/Ethnicity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/c67s-arvy",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The Functional Status and Outcome Database (FSOD) captures and tracks information about patient rehabilitative care throughout the VA. FSOD supports the entry of information from acute and sub-acute inpatient rehabilitation programs, as well as a broad range of outpatient rehabilitation programs. Outcome-based information including length of stay and cost is also tracked. Participating Veterans Affairs Medical Center staff enter information into FSOD on-line through a software program called VA FIMware (Functional Independence Measurement (FIM)). Users throughout the VA can access stored FSOD data through VA FIMware. Quarterly, FSOD data is transferred electronically to the Uniform Data System for Medical Rehabilitation (UDSmr) server in Buffalo, New York. The UDSmr database contains a U.S. national roll-up of rehabilitative programs. Users include all VA personnel involved in rehabilitative care and the UDSmr.</p>",
+            "identifier": "VA-VHA-PCS-008",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1997-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "fsod",
                 "functional",
@@ -31579,62 +31582,43 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VHA-PCS-008",
-            "description": "<p>The Functional Status and Outcome Database (FSOD) captures and tracks information about patient rehabilitative care throughout the VA. FSOD supports the entry of information from acute and sub-acute inpatient rehabilitation programs, as well as a broad range of outpatient rehabilitation programs. Outcome-based information including length of stay and cost is also tracked. Participating Veterans Affairs Medical Center staff enter information into FSOD on-line through a software program called VA FIMware (Functional Independence Measurement (FIM)). Users throughout the VA can access stored FSOD data through VA FIMware. Quarterly, FSOD data is transferred electronically to the Uniform Data System for Medical Rehabilitation (UDSmr) server in Buffalo, New York. The UDSmr database contains a U.S. national roll-up of rehabilitative programs. Users include all VA personnel involved in rehabilitative care and the UDSmr.</p>",
-            "title": "Functional Status and Outcome Database (FSOD)",
+            "landingPage": "https://www.data.va.gov/d/c67s-arvy",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
             "programCode": [
                 "029:040"
             ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "1997-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Functional Status and Outcome Database (FSOD)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/finance/overpaymentsReport.asp",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2009-10-01T04:00:00Z/2009-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "improper payments",
-                "overpayments"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Katherine Palmer",
                 "hasEmail": "mailto:Katherine.Palmer@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-093",
+            "dataQuality": true,
             "description": "<p>FY 2010 First Quarter High-Dollar Overpayments Report</p>",
-            "title": "FY 2010 First Quarter High-Dollar Overpayments Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31643,44 +31627,44 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-093",
+            "issued": "2017-07-26",
+            "keyword": [
+                "improper payments",
+                "overpayments"
+            ],
+            "landingPage": "https://www.va.gov/finance/overpaymentsReport.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2009-10-01T04:00:00Z/2009-12-31T05:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 2010 First Quarter High-Dollar Overpayments Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/c6pc-frdg",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-08-06",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS mailbox",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "00002fd0-0880-40f3-8ebf-837d47d695a6",
+            "dataQuality": true,
             "description": "<p>This data table provides a brief demographic profile of Veterans who separated from the military at two points in time: 2011 and 2017.  It contains distributions on age, sex, race/ethnicity, and military component</p>",
-            "title": "Demographic Characteristics of Veterans Who Separated in 2011 and 2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31688,42 +31672,38 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "00002fd0-0880-40f3-8ebf-837d47d695a6",
+            "issued": "2018-08-06",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/c6pc-frdg",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Demographic Characteristics of Veterans Who Separated in 2011 and 2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-02",
-            "keyword": [
-                "abr",
-                "abr2012",
-                "compensation benefits fy12",
-                "dic benefits",
-                "vba benefits"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Elwell",
                 "hasEmail": "mailto:thomas.elwell@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-ABR2012-025",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Service Connected Disabilities at the End of FY2012 by Period of Service",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31731,46 +31711,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-025",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "abr",
+                "abr2012",
+                "compensation benefits fy12",
+                "dic benefits",
+                "vba benefits"
+            ],
+            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2022-03-02",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "ABR Reports"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Service Connected Disabilities at the End of FY2012 by Period of Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.data.va.gov/d/c7db-tep2",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2018-02-23",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-22",
-            "keyword": [
-                "access",
-                "identity",
-                "security"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jeff Podolec",
                 "hasEmail": "mailto:jeff.podolec@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "64b048b3-e55e-49ce-b86f-615a47451b2c",
+            "dataQuality": true,
             "description": "<p>The authoritative source for person identity data. Maintains identity data for persons across VA systems. Provides a unique universal identifier for each person. Stores identity data as correlations for each system where a person is known. Provides a probabilistic matching algorithm. (Includes MPI, PSIM, and IdM TK) Maintains a gold copy known as a Primary View of the persons identity data. Broadcasts identity trait updates to systems of interest. Maintains a record locator service.</p>",
-            "title": "Master Veteran Index (MVI) Service",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31779,42 +31761,40 @@
                     "title": "Master Veteran Index (MVI) Service"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "64b048b3-e55e-49ce-b86f-615a47451b2c",
+            "issued": "2018-02-23",
+            "keyword": [
+                "access",
+                "identity",
+                "security"
+            ],
+            "landingPage": "https://www.data.va.gov/d/c7db-tep2",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-03-22",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
+            "title": "Master Veteran Index (MVI) Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-02",
-            "keyword": [
-                "fy2012 benefits",
-                "fy2012 vba",
-                "vba",
-                "vba benefits",
-                "vba benefits by state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Elwell",
                 "hasEmail": "mailto:thomas.elwell@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-ABR2012-084",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Connecticut-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31822,47 +31802,48 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-084",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "fy2012 benefits",
+                "fy2012 vba",
+                "vba",
+                "vba benefits",
+                "vba benefits by state"
+            ],
+            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2022-03-02",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "ABR 2012"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Connecticut-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.data.va.gov/d/c8yk-c7yu",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2017-11-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "call",
-                "healthcare",
-                "patient",
-                "provider"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Clark Timmins",
                 "hasEmail": "mailto:clark.timmins@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VIA-2",
+            "dataQuality": true,
             "description": "<p>This service provides web services used to obtain claims-related data for patients. Users of this service are intended to be healthcare providers.</p>",
-            "title": "Claim Service",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31871,22 +31852,54 @@
                     "title": "Claim Service"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "identifier": "VA-VIA-2",
+            "issued": "2017-11-17",
+            "keyword": [
+                "call",
+                "healthcare",
+                "patient",
+                "provider"
+            ],
+            "landingPage": "https://www.data.va.gov/d/c8yk-c7yu",
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
+            "title": "Claim Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/c9bm-vkqa",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Sail Operations",
+                "hasEmail": "mailto:VHASailOperations@va.gov"
+            },
+            "dataQuality": true,
+            "description": "Why Not the Best VA or WNTBVA is a system for comparing Veterans Health Administration (VHA) hospital system performance with regional and U.S. national benchmarks.  This report includes key quality measures available on CMS Hospital Compare and top hospital recognition programs from reporting agencies of hospital quality.  These .ZIP files are no longer supported and are in an 'as-is' state.  They were accurate at time of publication.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/c9bm-vkqa/application/zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "identifier": "https://www.data.va.gov/api/views/c9bm-vkqa",
+            "isPartOf": "VA-VHA-OIA-122",
             "issued": "2020-10-23",
-            "@type": "dcat:Dataset",
-            "temporal": "2016-10-01/2017-09-30",
-            "modified": "2021-06-24",
             "keyword": [
                 "2017",
                 "fy2017",
@@ -31905,68 +31918,38 @@
                 "vha",
                 "wntbva"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Sail Operations",
-                "hasEmail": "mailto:VHASailOperations@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/c9bm-vkqa",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-06-24",
+            "programCode": [
+                "029:040"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/c9bm-vkqa",
-            "description": "Why Not the Best VA or WNTBVA is a system for comparing Veterans Health Administration (VHA) hospital system performance with regional and U.S. national benchmarks.  This report includes key quality measures available on CMS Hospital Compare and top hospital recognition programs from reporting agencies of hospital quality.  These .ZIP files are no longer supported and are in an 'as-is' state.  They were accurate at time of publication.",
-            "title": "Why Not the Best VA FY2017 Hospital Performance - All Facilities",
-            "isPartOf": "VA-VHA-OIA-122",
-            "programCode": [
-                "029:040"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/c9bm-vkqa/application/zip",
-                    "mediaType": "application/zip"
-                }
-            ],
             "spatial": "United States, Puerto Rico",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "temporal": "2016-10-01/2017-09-30",
             "theme": [
                 "Hospital Quality Measurement"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Why Not the Best VA FY2017 Hospital Performance - All Facilities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/c9v2-5egj",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "coin",
-                "finance"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vicki Soukup",
                 "hasEmail": "mailto:vicki.soukup@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "OM-OM-171",
             "description": "<p>COIN Report 146 March 2016</p>",
-            "title": "COIN 146 March 2016",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -31974,42 +31957,43 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "OM-OM-171",
+            "issued": "2017-07-26",
+            "keyword": [
+                "coin",
+                "finance"
+            ],
+            "landingPage": "https://www.data.va.gov/d/c9v2-5egj",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "COIN 146 March 2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/budget/products.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-07",
-            "keyword": [
-                "budget",
-                "fy2012"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VA OM Open Data",
                 "hasEmail": "mailto:VAOMOpenData@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-027",
+            "dataQuality": true,
             "description": "<p>FY2012 VA Budget Submission.</p>",
-            "title": "FY2012 VA Budget Submission",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32018,44 +32002,43 @@
                     "title": "zip"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-027",
+            "issued": "2017-07-26",
+            "keyword": [
+                "budget",
+                "fy2012"
+            ],
+            "landingPage": "https://www.va.gov/budget/products.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-06-07",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY2012 VA Budget Submission"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/OGC/opinions/2014PrecedentOpinions.asp",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "ogc",
-                "opinion"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "OGC Law Library",
                 "hasEmail": "mailto:OGCLawLibrary@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OGC-010",
             "description": "<p>Notice Required by 38 USC \u00a7 513(a)(1) upon Receipt of a New and Material Evidence Claim</p>",
-            "title": "OGC Precedent Opinion 6-2014",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32064,46 +32047,45 @@
                     "title": "VAOGCPREC 6-2014"
                 }
             ],
+            "identifier": "VA-OGC-010",
+            "issued": "2017-07-26",
+            "keyword": [
+                "ogc",
+                "opinion"
+            ],
+            "landingPage": "https://www.va.gov/OGC/opinions/2014PrecedentOpinions.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:083"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OGC Precedent Opinion 6-2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/cber-kxf9",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2018-02-23",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-22",
-            "keyword": [
-                "access",
-                "identity",
-                "security"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Jeff Podolec",
                 "hasEmail": "mailto:jeff.podolec@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "19f464c4-6865-44fe-9881-9d95316173ed",
+            "dataQuality": true,
             "description": "<p>Provides single sign-on solution for internal facing VA applications. Allows internal users access to a variety of VA systems and applications using a reduced set of login credentials, including VA-issued PIV cards (LOA 4) and credentials generated by the VA Active Directory (LOA 2). Supports application implementation of PIV requirement</p>",
-            "title": "Single Sign On Internal (SSOi)",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32112,37 +32094,38 @@
                     "title": "Single Sign On Internal (SSOi)"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "19f464c4-6865-44fe-9881-9d95316173ed",
+            "issued": "2018-02-23",
+            "keyword": [
+                "access",
+                "identity",
+                "security"
+            ],
+            "landingPage": "https://www.data.va.gov/d/cber-kxf9",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-03-22",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
+            "title": "Single Sign On Internal (SSOi)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/cbic-8md8",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2015-01-01T05:00:00Z/2015-01-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "accounts receivable"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vikki Soukup",
                 "hasEmail": "mailto:Vikki.Soukup@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-119",
             "description": "<p>COIN 0017 CARS AGE PROFILE REPORT JAN 2015</p>",
-            "title": "COIN 0017 CARS AGE PROFILE REPORT JAN 2015",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32150,41 +32133,42 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-119",
+            "issued": "2017-07-26",
+            "keyword": [
+                "accounts receivable"
+            ],
+            "landingPage": "https://www.data.va.gov/d/cbic-8md8",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "theme": [
-                "Basic Statistics",
-                "Use",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2015-01-01T05:00:00Z/2015-01-31T05:00:00Z",
+            "theme": [
+                "Basic Statistics",
+                "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "COIN 0017 CARS AGE PROFILE REPORT JAN 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/cc9d-gj4h",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-29",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 101"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/cc9d-gj4h",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to assist States and federally recognized tribal governments in the establishment, expansion, and improvement of veterans' cemeteries. Monetary assistance is provided under this program to establish, expand, and improve State or Tribal government veterans\u2019 cemeteries. Cemeteries must be State or Tribal Government owned and operated solely for the interment of eligible veterans and their dependents and/or spouses. Construction cost means the amount found necessary to convert a tract of land to an operational cemetery. The cemetery must be used solely for the interment of veterans, their wives, husbands, surviving spouses, minor children, and unmarried adult children who were physically or mentally disabled and incapable of self-support: section 38 CFR Part 38.620.</p>",
-            "title": "USA SPENDING C&P BURIAL B101 VETERANS CEMETARY GRANTS PROGRAM APR2019",
-            "isPartOf": "d17c822a-717c-40ff-8fbe-3dcaefddb706",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32192,57 +32176,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/cc9d-gj4h/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cc9d-gj4h/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cc9d-gj4h/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/cc9d-gj4h/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cc9d-gj4h/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cc9d-gj4h/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/cc9d-gj4h/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cc9d-gj4h/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cc9d-gj4h/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/cc9d-gj4h",
+            "isPartOf": "d17c822a-717c-40ff-8fbe-3dcaefddb706",
+            "issued": "2019-03-29",
+            "keyword": [
+                "cfda 64 101"
+            ],
+            "landingPage": "https://www.data.va.gov/d/cc9d-gj4h",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING C&P BURIAL B101 VETERANS CEMETARY GRANTS PROGRAM APR2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/cd2t-9a6f",
-            "issued": "2023-02-21",
-            "@type": "dcat:Dataset",
-            "modified": "2023-02-21",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:VANCVAS@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/cd2t-9a6f",
             "description": "VetPop2020 Period of service distribution in FY 2023 and FY 2050",
-            "title": "VetPop2020 Period of Service FY23 & FY50",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32250,39 +32237,65 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/cd2t-9a6f/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cd2t-9a6f/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cd2t-9a6f/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/cd2t-9a6f/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cd2t-9a6f/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cd2t-9a6f/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/cd2t-9a6f/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cd2t-9a6f/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cd2t-9a6f/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/cd2t-9a6f",
+            "issued": "2023-02-21",
+            "landingPage": "https://www.data.va.gov/d/cd2t-9a6f",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-02-21",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2020 Period of Service FY23 & FY50"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.oprm.va.gov/foia/",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:40"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VA OM Open Data",
+                "hasEmail": "mailto:VAOMOpenData@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) Report for Fiscal Year 2003.  The report contains metrics on FOIA requests received, processed, and pending by agency/component.  It also contains metrics on exemptions, appeals, consultations, response times, and backlogs.  Fees collected, fees waived, and FOIA personnel and costs are reported.  Comparison of metrics attained for the previous year is also included.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.oprm.va.gov/docs/foia/Report2003.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "pdf"
+                }
+            ],
+            "identifier": "VA-OIT-ITIS-11",
             "issued": "2017-07-26",
-            "temporal": "2002-10-01T04:00:00Z/2003-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-07",
             "keyword": [
                 "2003",
                 "appeals",
@@ -32299,69 +32312,41 @@
                 "response time",
                 "va"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VA OM Open Data",
-                "hasEmail": "mailto:VAOMOpenData@va.gov"
-            },
+            "landingPage": "https://www.oprm.va.gov/foia/",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-06-07",
+            "programCode": [
+                "029:080"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-OIT-ITIS-11",
-            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) Report for Fiscal Year 2003.  The report contains metrics on FOIA requests received, processed, and pending by agency/component.  It also contains metrics on exemptions, appeals, consultations, response times, and backlogs.  Fees collected, fees waived, and FOIA personnel and costs are reported.  Comparison of metrics attained for the previous year is also included.</p>",
-            "title": "Department of Veterans Affairs Freedom of Information Act (FOIA) Report for Fiscal Year 2003",
-            "programCode": [
-                "029:080"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.oprm.va.gov/docs/foia/Report2003.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "pdf"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2002-10-01T04:00:00Z/2003-09-30T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Department of Veterans Affairs Freedom of Information Act (FOIA) Report for Fiscal Year 2003"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/cddm-afdy",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2024-06-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-06",
-            "keyword": [
-                "annual report",
-                "financial statements"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VA OM Open Data",
                 "hasEmail": "mailto:vaomopendata@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/cddm-afdy",
+            "dataQuality": true,
             "description": "Fiscal Year 2023 Section II of Agency Financial Report, Financial Results",
-            "title": "2023 VA AFR Section II Financial Results",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32369,58 +32354,55 @@
                     "mediaType": "application/pdf"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/cddm-afdy",
+            "issued": "2024-06-06",
+            "keyword": [
+                "annual report",
+                "financial statements"
+            ],
+            "landingPage": "https://www.data.va.gov/d/cddm-afdy",
             "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y"
+            "modified": "2024-06-06",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "2023 VA AFR Section II Financial Results"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/cdv7-ictv",
-            "issued": "2024-03-27",
             "@type": "dcat:Dataset",
-            "modified": "2024-03-27",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rebecca Matteo",
                 "hasEmail": "mailto:no-reply@ptsd-va.data.socrata.com"
             },
+            "description": "",
             "identifier": "https://www.data.va.gov/api/views/cdv7-ictv",
+            "issued": "2024-03-27",
+            "landingPage": "https://www.data.va.gov/d/cdv7-ictv",
+            "modified": "2024-03-27",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "",
             "title": "How do I use the data to perform a meta-analysis?"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/cf4n-nahu",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "ogc",
-                "opinion",
-                "public law 110-181"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "OGC Law Library",
                 "hasEmail": "mailto:OGCLawLibrary@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OGC-052",
             "description": "<p>Servicemembers' Entitlement to Rehabilitation and Vocational Benefits under Public Law 110-181</p>",
-            "title": "OGC Precedent Opinion 2-2008",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32429,43 +32411,44 @@
                     "title": "OGC Precedent Opinion 2-2008"
                 }
             ],
+            "identifier": "VA-OGC-052",
+            "issued": "2017-07-26",
+            "keyword": [
+                "ogc",
+                "opinion",
+                "public law 110-181"
+            ],
+            "landingPage": "https://www.data.va.gov/d/cf4n-nahu",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:083"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "OGC Precedent Opinion 2-2008"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/budget/report/",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2009-01-01T05:00:00Z/2009-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "accountability",
-                "performance",
-                "report"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David Zlowe",
                 "hasEmail": "mailto:David.Zlowe@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-007",
+            "dataQuality": true,
             "description": "<p>2009 VA Performance and Accountability Report.</p>",
-            "title": "2009 VA Performance and Accountability Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32474,48 +32457,45 @@
                     "title": "zip"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-007",
+            "issued": "2017-07-26",
+            "keyword": [
+                "accountability",
+                "performance",
+                "report"
+            ],
+            "landingPage": "https://www.va.gov/budget/report/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2009-01-01T05:00:00Z/2009-12-31T05:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2009 VA Performance and Accountability Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/cfep-k67g",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "age",
-                "detailed geography",
-                "gis",
-                "period of service",
-                "veteran population"
-            ],
             "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Florinda Balfour",
                 "hasEmail": "mailto:florinda.balfour@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-068",
             "description": "<p>National Center for Veterans and Analysis Statistics Population Maps are a compilation of facts related to the count of Veterans at multiple geographies.</p>",
-            "title": "Department of Veterans Affairs Various Maps",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32524,24 +32504,56 @@
                     "title": "Department of Veterans Affairs Various Maps"
                 }
             ],
+            "identifier": "VA-OEI-OEI-068",
+            "issued": "2017-07-26",
+            "keyword": [
+                "age",
+                "detailed geography",
+                "gis",
+                "period of service",
+                "veteran population"
+            ],
+            "landingPage": "https://www.data.va.gov/d/cfep-k67g",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Demographics"
-            ]
+            ],
+            "title": "Department of Veterans Affairs Various Maps"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/cfms-iawk",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2009-10-01T04:00:00Z/2010-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/health/HospitalReportCard.asp"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/HospitalReportCard.asp",
+            "description": "<p>Composite scores reflecting quality of care for outpatients (NEXUS) and inpatients (ORYX). Quality of outpatient care is further stratified by comparison of outpatient care by gender and age.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/VETDATA/docs/Datagov/Data_Gov_VHA_2010_Dataset5_Population_Quality_Care.xml",
+                    "mediaType": "application/xml",
+                    "title": "Population Quality of Care"
+                }
             ],
+            "identifier": "VA-VHA-OIA-046",
+            "isPartOf": "VA-VHA-OIA-584",
+            "issued": "2017-07-26",
             "keyword": [
                 "ambulatory",
                 "care",
@@ -32564,79 +32576,40 @@
                 "urban",
                 "veterans"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/cfms-iawk",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:040"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-OIA-046",
-            "description": "<p>Composite scores reflecting quality of care for outpatients (NEXUS) and inpatients (ORYX). Quality of outpatient care is further stratified by comparison of outpatient care by gender and age.</p>",
-            "title": "Veterans Health Administration 2010 Facility Quality and Safety Report - Population Quality of Care",
-            "isPartOf": "VA-VHA-OIA-584",
-            "programCode": [
-                "029:040"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/VETDATA/docs/Datagov/Data_Gov_VHA_2010_Dataset5_Population_Quality_Care.xml",
-                    "mediaType": "application/xml",
-                    "title": "Population Quality of Care"
-                }
+            "references": [
+                "https://www.va.gov/health/HospitalReportCard.asp"
             ],
-            "describedBy": "https://www.va.gov/health/HospitalReportCard.asp",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2009-10-01T04:00:00Z/2010-09-30T04:00:00Z",
             "theme": [
                 "Section 3. Health and Nutrition"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veterans Health Administration 2010 Facility Quality and Safety Report - Population Quality of Care"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/cg9c-gfgn",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2021-01-13",
-            "@type": "dcat:Dataset",
-            "modified": "2021-03-04",
-            "keyword": [
-                "address",
-                "benefits",
-                "exam",
-                "examinations",
-                "latitude",
-                "longitude",
-                "open data",
-                "va",
-                "va facilities",
-                "vba",
-                "veterans",
-                "zip code"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Elwell",
                 "hasEmail": "mailto:pai.vbaco@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/cg9c-gfgn",
             "description": "This is number 1 of 3 data sets that accompany Open Data Maps Data Story on VA's Open Data Site.\n\nSpecifically this is a crosswalk data set that identifies VA facilities and their locations via postal address with zip codes and Latitude and Longitude information for facility geo plotting postal addresses.  Facility location information as of 2018.",
-            "title": "PAI Data Set For Open Data Maps Data Story 1 of 3",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32644,57 +32617,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/cg9c-gfgn/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cg9c-gfgn/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cg9c-gfgn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/cg9c-gfgn/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cg9c-gfgn/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cg9c-gfgn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/cg9c-gfgn/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cg9c-gfgn/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cg9c-gfgn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/cg9c-gfgn",
+            "issued": "2021-01-13",
+            "keyword": [
+                "address",
+                "benefits",
+                "exam",
+                "examinations",
+                "latitude",
+                "longitude",
+                "open data",
+                "va",
+                "va facilities",
+                "vba",
+                "veterans",
+                "zip code"
+            ],
+            "landingPage": "https://www.data.va.gov/d/cg9c-gfgn",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-03-04",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "PAI Data Set For Open Data Maps Data Story 1 of 3"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/cgcp-e2pu",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2019-10-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "median household income",
-                "minority veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tamara Lee",
                 "hasEmail": "mailto:tamara.lee@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veteran Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/cgcp-e2pu",
             "description": "Dataset listing median household income, for the year 2014, of Minority veterans as well as non-veterans, by age.",
-            "title": "2014 MEDIAN HOUSEHOLD INCOME of Minority Veterans and Non-Veterans by Age",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32702,142 +32685,141 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/cgcp-e2pu/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cgcp-e2pu/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cgcp-e2pu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/cgcp-e2pu/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cgcp-e2pu/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cgcp-e2pu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/cgcp-e2pu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cgcp-e2pu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cgcp-e2pu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/cgcp-e2pu",
+            "issued": "2019-10-24",
+            "keyword": [
+                "median household income",
+                "minority veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/cgcp-e2pu",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veteran Affairs"
+            },
+            "title": "2014 MEDIAN HOUSEHOLD INCOME of Minority Veterans and Non-Veterans by Age"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/cgsj-chh2",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary West Virginia FY2023",
+            "identifier": "https://www.data.va.gov/api/views/cgsj-chh2",
             "issued": "2024-06-20",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-12",
             "keyword": [
                 "fy2023",
                 "ncvas state summary",
                 "west virginia"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/cgsj-chh2",
+            "modified": "2024-07-12",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/cgsj-chh2",
-            "description": "NCVAS State Summary West Virginia FY2023",
-            "title": "NCVAS State Summary West Virginia FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary West Virginia FY2023"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ch38-5zxg",
-            "issued": "2023-08-10",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-17",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Rhode Island FY2021",
+            "identifier": "https://www.data.va.gov/api/views/ch38-5zxg",
+            "issued": "2023-08-10",
             "keyword": [
                 "fy2021 data",
                 "ncvas state summary",
                 "rhode island"
             ],
-            "identifier": "https://www.data.va.gov/api/views/ch38-5zxg",
+            "landingPage": "https://www.data.va.gov/d/ch38-5zxg",
+            "modified": "2024-06-17",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Rhode Island FY2021",
             "title": "NCVAS State Summary Rhode Island FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/ch42-aa32",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-12",
-            "keyword": [
-                "montana",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VANCVAS",
                 "hasEmail": "mailto:VANCVAS@VA.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/ch42-aa32",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Montana",
+            "identifier": "https://www.data.va.gov/api/views/ch42-aa32",
+            "issued": "2021-08-26",
+            "keyword": [
+                "montana",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ch42-aa32",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-12",
             "programCode": [
                 "029:086"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summaries_Montana"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.oit.va.gov/docs/dashboard/201301_OIT_PMAS_Dashboard_Active_Jan_2013.pdf",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "dashboard",
-                "pmas",
-                "va"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rodney Emery",
                 "hasEmail": "mailto:rodney.emery@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OIT-OIT-020",
             "description": "<p>PMAS Dashboard Jan 2013</p>",
-            "title": "PMAS Dashboard Jan 2013",
-            "programCode": [
-                "029:080"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32852,23 +32834,46 @@
                     "title": "csv"
                 }
             ],
+            "identifier": "VA-OIT-OIT-020",
+            "issued": "2017-07-26",
+            "keyword": [
+                "dashboard",
+                "pmas",
+                "va"
+            ],
+            "landingPage": "https://www.oit.va.gov/docs/dashboard/201301_OIT_PMAS_Dashboard_Active_Jan_2013.pdf",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:080"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "PMAS Dashboard Jan 2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.nvsbe.com",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:40"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Armando Herrera",
+                "hasEmail": "mailto:Armando.Herrera@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>National Veterans Small Business Engagement homepage</p>",
+            "identifier": "VA-00SB-NVSBE0001",
             "issued": "2017-07-26",
-            "temporal": "2014-06-11T04:00:00Z/2015-04-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "conference",
                 "engagement",
@@ -32879,61 +32884,40 @@
                 "veterans affairs",
                 "vets"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Armando Herrera",
-                "hasEmail": "mailto:Armando.Herrera@va.gov"
-            },
+            "landingPage": "http://www.nvsbe.com",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:081"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-00SB-NVSBE0001",
-            "description": "<p>National Veterans Small Business Engagement homepage</p>",
-            "title": "NVSBE Website - Homepage",
-            "programCode": [
-                "029:081"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2014-06-11T04:00:00Z/2015-04-30T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NVSBE Website - Homepage"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/cj65-5pt5",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 114"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/cj65-5pt5",
+            "dataQuality": true,
             "description": "<p>VBA HOUSING BENEFITS PROGRAM to provide veterans who are eligible for a Specially Adapted Housing grant with loan directly from the VA in certain circumstances. Permanently and totally disabled Veterans who served on active duty on or after September 16, 1940 and are eligible for a Specially Adapted Housing grant. VA may make loans up to $33,000 to eligible applicants if (a) the veteran is eligible for a VA Specially Adapted Housing grant, and (b) a loan is necessary to supplement the grant, and (c) home loans from a private lender are not available in the area where the property involved is located.</p>",
-            "title": "USA SPENDING LGY B114 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS OCT2018",
-            "isPartOf": "bd8fa8ad-9de6-41b7-a863-09ed5197e048",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -32941,63 +32925,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/cj65-5pt5/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cj65-5pt5/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cj65-5pt5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/cj65-5pt5/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cj65-5pt5/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cj65-5pt5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/cj65-5pt5/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cj65-5pt5/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cj65-5pt5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/cj65-5pt5",
+            "isPartOf": "bd8fa8ad-9de6-41b7-a863-09ed5197e048",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 114"
+            ],
+            "landingPage": "https://www.data.va.gov/d/cj65-5pt5",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING LGY B114 VETERANS HOUSING DIRECT LOANS FOR CERTAIN DISABLED VETERANS OCT2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/cmr2-gys7",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2020-10-06",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-26",
-            "keyword": [
-                "utilization",
-                "veteran benefits",
-                "veterans",
-                "veterans benefits"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Mark Guagliardo",
                 "hasEmail": "mailto:VANCVAS@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/cmr2-gys7",
             "description": "Age Distribution of Users by Gender FY2018. Data underlying the fourth figure of Part 1 of the FY2018 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Veterans Utilization Profile FY18 - Fig 5, Age Distribution of Users by Gender FY2018",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33005,76 +32986,78 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/cmr2-gys7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cmr2-gys7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cmr2-gys7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/cmr2-gys7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cmr2-gys7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cmr2-gys7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/cmr2-gys7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cmr2-gys7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cmr2-gys7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://www.usa.gov/government-works"
+            "identifier": "https://www.data.va.gov/api/views/cmr2-gys7",
+            "issued": "2020-10-06",
+            "keyword": [
+                "utilization",
+                "veteran benefits",
+                "veterans",
+                "veterans benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/cmr2-gys7",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-08-26",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Veterans Utilization Profile FY18 - Fig 5, Age Distribution of Users by Gender FY2018"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/cmvw-a856",
-            "issued": "2024-04-30",
             "@type": "dcat:Dataset",
-            "modified": "2024-09-04",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rebecca Matteo",
                 "hasEmail": "mailto:no-reply@ptsd-va.data.socrata.com"
             },
+            "description": "Learn about treatment options for people with PTSD who also have substance use problems.",
             "identifier": "https://www.data.va.gov/api/views/cmvw-a856",
+            "issued": "2024-04-30",
+            "landingPage": "https://www.data.va.gov/d/cmvw-a856",
+            "modified": "2024-09-04",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "Learn about treatment options for people with PTSD who also have substance use problems.",
             "title": "What treatments are used for people with PTSD and substance use problems?"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/cmx2-7kgw",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "coin",
-                "finance"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vicki Soukup",
                 "hasEmail": "mailto:vicki.soukup@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "OM-OM-178",
             "description": "<p>COIN report 0022 Feb 2017</p>",
-            "title": "COIN 0022 Feb 2017",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33082,40 +33065,41 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "OM-OM-178",
+            "issued": "2017-07-26",
+            "keyword": [
+                "coin",
+                "finance"
+            ],
+            "landingPage": "https://www.data.va.gov/d/cmx2-7kgw",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "COIN 0022 Feb 2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/cnn6-g5i6",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "south dakota"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DG&amp;A Mailgroup",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-213",
             "description": "<p>This summary describes the programs and services VA provided in  South Dakota in fiscal year 2015.</p>",
-            "title": "State Summary:  South Dakota FY15",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33124,41 +33108,40 @@
                     "title": "South Dakota"
                 }
             ],
+            "identifier": "VA-OEI-OEI-213",
+            "issued": "2017-07-26",
+            "keyword": [
+                "south dakota"
+            ],
+            "landingPage": "https://www.data.va.gov/d/cnn6-g5i6",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "State Summary:  South Dakota FY15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/cp9u-b2pq",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2024-07-30",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-10",
-            "keyword": [
-                "veterans",
-                "women veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS",
                 "hasEmail": "mailto:vaconcvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/cp9u-b2pq",
             "description": "",
-            "title": "Employment Status of Veterans by Age and Gender",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33166,72 +33149,101 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/cp9u-b2pq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cp9u-b2pq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cp9u-b2pq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/cp9u-b2pq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cp9u-b2pq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cp9u-b2pq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/cp9u-b2pq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cp9u-b2pq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cp9u-b2pq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/cp9u-b2pq",
+            "issued": "2024-07-30",
+            "keyword": [
+                "veterans",
+                "women veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/cp9u-b2pq",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-12-10",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Employment Status of Veterans by Age and Gender"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/cprf-5mbx",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary New Hampshire FY2023",
+            "identifier": "https://www.data.va.gov/api/views/cprf-5mbx",
             "issued": "2024-06-14",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-12",
             "keyword": [
                 "fy2023",
                 "ncvas state summary",
                 "new hampshire"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/cprf-5mbx",
+            "modified": "2024-07-12",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/cprf-5mbx",
-            "description": "NCVAS State Summary New Hampshire FY2023",
-            "title": "NCVAS State Summary New Hampshire FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary New Hampshire FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-06-09T04:00:00Z/2014-06-09T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/health/access-audit.asp"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/access-audit.asp",
+            "description": "<p>On Wednesday, May 21, 2014, VA launched the Accelerating Access to Care Initiative, a nation-wide program to ensure timely access to care. As directed by President Obama, VHA has identified Veterans across the system experiencing waits that do not meet Veterans expectations for timeliness. VA has begun contacting and scheduling all Veterans who are waiting for care in VA clinics or arranging for care in the community, while simultaneously addressing the underlying issues that impede Veterans\u2019 access.The nationwide Access Audit covered a total of 731 separate points of access, and involved over 3,772 interviews of clinical and administrative staff involved in the scheduling process at VA Medical Centers (VAMC), large Community Based Outpatient Clinics (CBOC) serving at least 10,000 Veterans and a sampling of smaller clinics. A complete list of VISN facilities with components reviewed as part of the Access Audit is included in this package</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.va.gov/health/docs/VISN20FACTSHEET140609.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "VISN 20 Fact Sheet"
+                }
             ],
+            "identifier": "VA-VHA-OIA-092",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -33247,71 +33259,43 @@
                 "wait list",
                 "wait time"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:041"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-OIA-092",
-            "description": "<p>On Wednesday, May 21, 2014, VA launched the Accelerating Access to Care Initiative, a nation-wide program to ensure timely access to care. As directed by President Obama, VHA has identified Veterans across the system experiencing waits that do not meet Veterans expectations for timeliness. VA has begun contacting and scheduling all Veterans who are waiting for care in VA clinics or arranging for care in the community, while simultaneously addressing the underlying issues that impede Veterans\u2019 access.The nationwide Access Audit covered a total of 731 separate points of access, and involved over 3,772 interviews of clinical and administrative staff involved in the scheduling process at VA Medical Centers (VAMC), large Community Based Outpatient Clinics (CBOC) serving at least 10,000 Veterans and a sampling of smaller clinics. A complete list of VISN facilities with components reviewed as part of the Access Audit is included in this package</p>",
-            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 20",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "http://www.va.gov/health/docs/VISN20FACTSHEET140609.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "VISN 20 Fact Sheet"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2014-06-09T04:00:00Z/2014-06-09T04:00:00Z",
             "theme": [
                 "Accelerating Access",
                 "Audit"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 20"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/cpxg-h9zq",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-22",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-14",
-            "keyword": [
-                "cfda 64 100"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:Annette.Brown2@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/cpxg-h9zq",
+            "dataQuality": true,
             "description": "<p>VBA PROGRAM BENEFITS for Automobiles and Adaptive Equipment for Certain Disabled Veterans and Members of the Armed Forces. Veterans with honorable service and servicepersons on duty having a service-connected disability due to loss or permanent loss of use of one or both feet, one or both hands, or a permanent impairment of vision of both eyes to a prescribed degree. For adaptive equipment only, eligibility also exists if there is service-connected ankylosis of one or both knees or one or both hips. Personnel on active duty also qualify under the same criteria as veterans. Uses &amp; Use Restrictions:  Assistance toward purchase of an automobile or other conveyance is a one-time payment only. Necessary adaptive equipment may be furnished, repaired, replaced, or reinstalled on a conveyance which may be purchased with assistance or any other conveyance subsequently or previously acquired. Adaptive equipment will be provided for no more than two conveyances during any four-year period unless one of those two vehicles becomes unavailable to the veteran.</p>",
-            "title": "USA SPENDING CH39 B100 AUTOMOBILE AND ADAPTIVE EQUIPMENT ALLOWANCE MAR2019",
-            "isPartOf": "70535216-31bf-416c-9ff4-3ec839abed4c",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33319,61 +33303,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/cpxg-h9zq/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cpxg-h9zq/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cpxg-h9zq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/cpxg-h9zq/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cpxg-h9zq/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cpxg-h9zq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/cpxg-h9zq/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cpxg-h9zq/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cpxg-h9zq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/cpxg-h9zq",
+            "isPartOf": "70535216-31bf-416c-9ff4-3ec839abed4c",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 100"
+            ],
+            "landingPage": "https://www.data.va.gov/d/cpxg-h9zq",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-14",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING CH39 B100 AUTOMOBILE AND ADAPTIVE EQUIPMENT ALLOWANCE MAR2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/cq3z-ckwz",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "ogc",
-                "opinion"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "OGC Law Library",
                 "hasEmail": "mailto:OGCLawLibrary@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OGC-021",
             "description": "<p>Whether Graves of Civil War-Era Soldiers Currently Identified with Marble Stones with Numerical Inscriptions Constitute Unmarked Graves for Purposes of VA Furnishing a Headstone or Marker under 38 U.S.C. \u00a7 2306  Author: Lee, Y.K.</p>",
-            "title": "OGC Precedent Opinion 3-2015",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33382,41 +33365,42 @@
                     "title": "OGC Precedent Opinion 3-2015"
                 }
             ],
+            "identifier": "VA-OGC-021",
+            "issued": "2017-07-26",
+            "keyword": [
+                "ogc",
+                "opinion"
+            ],
+            "landingPage": "https://www.data.va.gov/d/cq3z-ckwz",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:083"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "OGC Precedent Opinion 3-2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/crdj-d6f2",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-21",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 116"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/crdj-d6f2",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION PROGRAMS to provide, through purchase and/or fabrication, prosthetic and related appliances, equipment and services to eligible veterans so that they may live and work as productive citizens. Veterans eligible for prosthetic services are service-connected veterans seeking care for a service-connected disability; veterans with compensable service-connected disabilities generally rated 10 percent or more; former prisoners of war, veterans discharged or released from active military service for a disability that was incurred or aggravated in the line of duty, and veterans who are in receipt of Section 1151 benefits; veterans who are in receipt of increased pension based on a need of regular aid and attendance or by reason of being permanently housebound; veterans who have annual income and net worth below the \"means test\" threshold; all other veterans who are not required to pay a copayment for their care, i.e., veterans of the Mexican border period and World War I, compensated zero (0) percent service-connected veterans who are receiving statutory awards, veterans exposed to a toxic substance, radiation or environmental hazard (limited to certain disabilities); and veterans who must pay a copayment for their care. Ineligible veterans are nonservice-connected veterans residing or sojourning in foreign lands.</p>",
-            "title": "USA SPENDING EDUCATION CH31 B116 VETERANS PROSTHETIC APPLIANCES APR2019",
-            "isPartOf": "5760c6c5-d531-4dc3-9e99-4418034dbb16",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33424,90 +33408,88 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/crdj-d6f2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/crdj-d6f2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/crdj-d6f2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/crdj-d6f2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/crdj-d6f2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/crdj-d6f2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/crdj-d6f2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/crdj-d6f2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/crdj-d6f2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/crdj-d6f2",
+            "isPartOf": "5760c6c5-d531-4dc3-9e99-4418034dbb16",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 116"
+            ],
+            "landingPage": "https://www.data.va.gov/d/crdj-d6f2",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "USA SPENDING EDUCATION CH31 B116 VETERANS PROSTHETIC APPLIANCES APR2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/cruv-8y3m",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Arizona FY2023",
+            "identifier": "https://www.data.va.gov/api/views/cruv-8y3m",
             "issued": "2024-05-16",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-10",
             "keyword": [
                 "arizona",
                 "fy2024 data",
                 "ncvas state summary"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/cruv-8y3m",
+            "modified": "2024-07-10",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/cruv-8y3m",
-            "description": "NCVAS State Summary Arizona FY2023",
-            "title": "NCVAS State Summary Arizona FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Arizona FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/csjp-ca6i",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-12-04",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-21",
-            "keyword": [
-                "ethnicity",
-                "race",
-                "veterans",
-                "vietnam war"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCAVS Mailbox",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "f7b43670-af56-492b-bebf-220d9a6b1bf5",
+            "dataQuality": true,
             "description": "<p>This spreadsheet contains estimates and margins of error of Vietnam Veterans\u2019 race/ethnicity by state.</p>",
-            "title": "Vietnam War Veterans by State and Race/Ethnicity: 2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33515,43 +33497,42 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "f7b43670-af56-492b-bebf-220d9a6b1bf5",
+            "issued": "2018-12-04",
+            "keyword": [
+                "ethnicity",
+                "race",
+                "veterans",
+                "vietnam war"
+            ],
+            "landingPage": "https://www.data.va.gov/d/csjp-ca6i",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2020-11-21",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Vietnam War Veterans by State and Race/Ethnicity: 2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/",
+            "accrualPeriodicity": "R/P2M",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2013-10-01T04:00:00Z/2014-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "compensation",
-                "county",
-                "department of veterans affairs",
-                "disability",
-                "pension",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:Tom.Garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-075",
-            "description": "<p>This report provides county-level estimates of the number of Veterans who received VA Disability Compensation or Pension benefits during FY 2014.</p>",
-            "title": "FY 2014 Disability Compensation and Pension Recipients by County Report (C&P by County)",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/vetdata/docs/SpecialReports/Comp_n_pen_by_Cnty_2014.xlsx",
             "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-            "programCode": [
-                "029:086"
-            ],
+            "description": "<p>This report provides county-level estimates of the number of Veterans who received VA Disability Compensation or Pension benefits during FY 2014.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33560,75 +33541,77 @@
                     "title": "This report provides county-level estimates of the number of Veterans who received VA Disability Compensation or Pension benefits during FY 2014"
                 }
             ],
-            "describedBy": "https://www.va.gov/vetdata/docs/SpecialReports/Comp_n_pen_by_Cnty_2014.xlsx",
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-075",
+            "issued": "2017-07-26",
+            "keyword": [
+                "compensation",
+                "county",
+                "department of veterans affairs",
+                "disability",
+                "pension",
+                "veterans"
+            ],
+            "landingPage": "https://www.va.gov/vetdata/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2013-10-01T04:00:00Z/2014-09-30T04:00:00Z",
             "theme": [
                 "Compensation and Pension"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 2014 Disability Compensation and Pension Recipients by County Report (C&P by County)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/cswe-qpbk",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-08",
-            "keyword": [
-                "veterans",
-                "west virginia"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VANCVAS",
                 "hasEmail": "mailto:VANCVAS@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/cswe-qpbk",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_West Virginia",
+            "identifier": "https://www.data.va.gov/api/views/cswe-qpbk",
+            "issued": "2021-08-26",
+            "keyword": [
+                "veterans",
+                "west virginia"
+            ],
+            "landingPage": "https://www.data.va.gov/d/cswe-qpbk",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-08-08",
             "programCode": [
                 "029:086"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summaries_West Virginia"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/cupt-prh9",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "idaho",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:Tom.Garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-097",
             "description": "<p>This is a summary of the programs and services provided by VA in Idaho in fiscal year 2014.</p>",
-            "title": "State Summary:  Idaho",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33637,44 +33620,44 @@
                     "title": "State Summary:  Idaho"
                 }
             ],
+            "identifier": "VA-OEI-OEI-097",
+            "issued": "2017-07-26",
+            "keyword": [
+                "idaho",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/cupt-prh9",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "State Summary:  Idaho"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/cvcv-ijat",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2015-03-01T05:00:00Z/2015-03-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "debt referrals"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vikki Soukup",
                 "hasEmail": "mailto:Vikki.Soukup@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-137",
             "description": "<p>Debt referrals to credit reporting agencies and the treasury offset program.</p>",
-            "title": "COIN 0146 MONTHLY TOP TOTALS REPORT MAR 2015",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33682,41 +33665,42 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-137",
+            "issued": "2017-07-26",
+            "keyword": [
+                "debt referrals"
+            ],
+            "landingPage": "https://www.data.va.gov/d/cvcv-ijat",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2015-03-01T05:00:00Z/2015-03-31T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "COIN 0146 MONTHLY TOP TOTALS REPORT MAR 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/cwsv-gx2i",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 106"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/cwsv-gx2i",
+            "dataQuality": true,
             "description": "<p>VBA SPECIALLY ADAPTED HOUSING BENEFIT PROGRAMS. The Specially Adapted Housing (SAH) grant program helps Veterans with certain service-connected disabilities live independently in a barrier-free environment. SAH grants can be used in one of the following ways: (1) construct a suitable home on suitable land either already owned or to be acquired by the veteran, or (2) remodel an existing home if it can be suitably adapted, or (3) acquire a suitably adapted home or reduce the outstanding mortgage on a suitably adapted home already owned by the veteran. b. The Special Housing Adaptation (SHA) grant program helps veterans with certain service-connected disabilities adapt or purchase a home to accommodate the disability. SHA grants can be used in one of the following ways: (1) adapt an existing home the veteran or a family member already owns in which the veteran lives; (2) adapt a home the veteran or family member intends to purchase in which the veteran will live; (3) help a veteran purchase a home already adapted in which the veteran will live. c. . The Temporary Residence Adaptations (TRA) program provides adaptation assistance to veterans who are residing, but do not intend to permanently reside, in the a residence owned by a family member. If a veteran is otherwise eligible for SAH or SHA, the assistance is limited. d. SAH and SHA grants may be used up to three times, as long as the aggregate grant amount does not exceed the statutory dollar limitation. TRA grants may only be used once (and count as a grant usage for purposes of the limit of three), and the amount of assistance provided will be subtracted from the veteran's available statutory maximum.</p>",
-            "title": "USA SPENDING CH39 B106 SPECIALLY ADAPTED HOUSING FOR DISABLED VETERANS OCT2018",
-            "isPartOf": "bc3a6e1f-3fb0-4fb1-8b07-59efaf92222b",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33724,62 +33708,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/cwsv-gx2i/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cwsv-gx2i/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cwsv-gx2i/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/cwsv-gx2i/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cwsv-gx2i/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cwsv-gx2i/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/cwsv-gx2i/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cwsv-gx2i/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cwsv-gx2i/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/cwsv-gx2i",
+            "isPartOf": "bc3a6e1f-3fb0-4fb1-8b07-59efaf92222b",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 106"
+            ],
+            "landingPage": "https://www.data.va.gov/d/cwsv-gx2i",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING CH39 B106 SPECIALLY ADAPTED HOUSING FOR DISABLED VETERANS OCT2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/cwtz-96pj",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-27",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 105",
-                "cfda 64 110"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/cwtz-96pj",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to provide educational opportunities to the dependents of certain disabled and deceased veterans. Spouses, surviving spouses, and children (including stepchild or adopted child) between age 18 and 26 of veterans who died from service-connected disabilities, of living veterans whose service-connected disabilities are considered permanently and totally disabling, of those who died from any cause while such service-connected disabilities were in existence, of servicepersons who have been listed for a total of more than 90 days as currently missing in action, or as currently prisoners of war, a service member who VA determines has a service connected permanent and total disability and at the time of VA's determination is a member of the Armed Forces who is hospitalized or receiving outpatient medical care, services, or treatment; and is likely to be discharged or released from service for this service-connected disability. Children under the age of 18 may be eligible under special circumstances.</p>",
-            "title": "USA SPENDING C&P B105 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE MAY2019",
-            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33787,62 +33770,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/cwtz-96pj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cwtz-96pj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cwtz-96pj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/cwtz-96pj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cwtz-96pj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cwtz-96pj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/cwtz-96pj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cwtz-96pj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cwtz-96pj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/cwtz-96pj",
+            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 105",
+                "cfda 64 110"
+            ],
+            "landingPage": "https://www.data.va.gov/d/cwtz-96pj",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING C&P B105 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE MAY2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/cwwu-x776",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2021-02-18",
-            "@type": "dcat:Dataset",
-            "modified": "2021-03-23",
-            "keyword": [
-                "disability pension",
-                "veteran",
-                "veteran benefits"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Florinda Balfour",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/cwwu-x776",
             "description": "Compensation & Pension: All Veterans who received VA disability compensation or pension payments were included. Veterans who received Special Adaptive Housing benefits were also included in the analysis. Veterans with pending or denied claims were not included. Veterans Benefits Administration (VBA) provides Compensation and Pension disability benefits.",
-            "title": "Veterans who used VA Disability Pension Benefits",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33850,61 +33832,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/cwwu-x776/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cwwu-x776/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cwwu-x776/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/cwwu-x776/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cwwu-x776/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cwwu-x776/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/cwwu-x776/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/cwwu-x776/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/cwwu-x776/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "State",
-            "license": "https://www.usa.gov/government-works",
+            "identifier": "https://www.data.va.gov/api/views/cwwu-x776",
+            "issued": "2021-02-18",
+            "keyword": [
+                "disability pension",
+                "veteran",
+                "veteran benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/cwwu-x776",
             "language": [
                 "English"
-            ]
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2021-03-23",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "spatial": "State",
+            "title": "Veterans who used VA Disability Pension Benefits"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/Report.asp",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-10-01T04:00:00Z/2013-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:Tom.Garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-081",
+            "dataQuality": true,
             "description": "<p>This report uses data from the 2013 American Community Survey and USVETS (2013) data to compare the demographic and socioeconomic characteristics of Post-9/11 Veterans and non-Post-9/11 Veterans and non-Veterans. It also illustrates utilization differences between Post-9/11 Veterans and other Veterans.</p>",
-            "title": "Profile of Post-9/11 Veterans: 2013",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33913,43 +33897,42 @@
                     "title": "Profile of Post-9/11 Veterans: 2013"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-081",
+            "issued": "2017-07-26",
+            "keyword": [
+                "veterans"
+            ],
+            "landingPage": "https://www.va.gov/vetdata/Report.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2012-10-01T04:00:00Z/2013-09-30T04:00:00Z",
             "theme": [
                 "Demographics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Profile of Post-9/11 Veterans: 2013"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/czbe-mbxw",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "veterans",
-                "west virginia"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:Tom.Garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-135",
             "description": "<p>This is a summary of the programs and services provided by VA in West Virginia in fiscal year 2014.</p>",
-            "title": "State Summary:  West Virginia",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -33958,49 +33941,46 @@
                     "title": "State Summary:  West Virginia"
                 }
             ],
+            "identifier": "VA-OEI-OEI-135",
+            "issued": "2017-07-26",
+            "keyword": [
+                "veterans",
+                "west virginia"
+            ],
+            "landingPage": "https://www.data.va.gov/d/czbe-mbxw",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "State Summary:  West Virginia"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/d34z-ny8c",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Web site is available to the general public",
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2012-01-01T05:00:00Z/2014-08-04T04:00:00Z",
-            "modified": "2020-05-15",
-            "keyword": [
-                "center for women veterans",
-                "female veterans",
-                "resources women veterans",
-                "women veterans",
-                "women veterans health care"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Desiree Long",
                 "hasEmail": "mailto:desiree.long@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-CWV-CWV-001",
+            "dataQuality": true,
             "description": "<p>Web site for the Center for Women Veterans.  Web site includes resources and events for women Veterans.</p>",
-            "title": "Center for Women Veterans Web Site",
-            "programCode": [
-                "029:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34009,87 +33989,91 @@
                     "title": "Center for Women Veterans Web Site"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-CWV-CWV-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "center for women veterans",
+                "female veterans",
+                "resources women veterans",
+                "women veterans",
+                "women veterans health care"
+            ],
+            "landingPage": "https://www.data.va.gov/d/d34z-ny8c",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Web site is available to the general public",
+            "temporal": "2012-01-01T05:00:00Z/2014-08-04T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Center for Women Veterans Web Site"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.usaspending.gov",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2013-12-01T05:00:00Z/2013-12-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
-            "keyword": [
-                "cfda 64 118",
-                "direct home loan",
-                "lgy",
-                "usa spending"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Monica Reyes",
                 "hasEmail": "mailto:monica.reyes@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-USASPENDING122013-014",
+            "dataQuality": true,
             "description": "<p>USA Spending- Direct Home Loan- December 2013.</p>",
-            "title": "USA Spending file- Direct Home Loan-  CFDA 64.118",
+            "identifier": "VA-VBA-USASPENDING122013-014",
             "isPartOf": "VA-VBA-MASTER-USA Spending-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "cfda 64 118",
+                "direct home loan",
+                "lgy",
+                "usa spending"
+            ],
+            "landingPage": "https://www.usaspending.gov",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
             "programCode": [
                 "029:003"
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2013-12-01T05:00:00Z/2013-12-30T05:00:00Z",
             "theme": [
                 "USA Spending"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USA Spending file- Direct Home Loan-  CFDA 64.118"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/d49k-xwff",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "north carolina"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DG&amp;A Mailgroup",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-204",
             "description": "<p>This summary describes the programs and services VA provided in North Carolina in fiscal year 2015.</p>",
-            "title": "State Summary: North Carolina FY15",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34098,46 +34082,42 @@
                     "title": "North Carolina"
                 }
             ],
+            "identifier": "VA-OEI-OEI-204",
+            "issued": "2017-07-26",
+            "keyword": [
+                "north carolina"
+            ],
+            "landingPage": "https://www.data.va.gov/d/d49k-xwff",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "State Summary: North Carolina FY15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-02",
-            "keyword": [
-                "abr",
-                "abr2012",
-                "compensation benefits fy12",
-                "dic benefits",
-                "vba benefits"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Elwell",
                 "hasEmail": "mailto:thomas.elwell@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-ABR2012-017",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Most Prevalent Disabilities for Veterans Receiving Compensation at the End of Fiscal Year 2012",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34145,51 +34125,51 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-017",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "abr",
+                "abr2012",
+                "compensation benefits fy12",
+                "dic benefits",
+                "vba benefits"
+            ],
+            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2022-03-02",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "Use of Benefits and Services"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Most Prevalent Disabilities for Veterans Receiving Compensation at the End of Fiscal Year 2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/health/",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2013-10-01T04:00:00Z/2014-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cboc",
-                "health",
-                "healthcare",
-                "outpatient",
-                "va",
-                "va clinics",
-                "veteran"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VHA Open Data",
                 "hasEmail": "mailto:vhaopendata@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VHA-OIA-114",
-            "description": "<p>Community Based Outpatient Clinics (CBOCs) at the end of Fiscal Year 2014. Data includes number of unique patients and clinic encounters.</p>",
-            "title": "VA Community Based Outpatient Clinics, FY2014",
+            "dataQuality": true,
+            "describedBy": "https://github.com/department-of-veterans-affairs/VA_Data_Assets_VHA/raw/master/VA_DataDefinitions_VisitsBedsCBOC_2015.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "029:042"
-            ],
+            "description": "<p>Community Based Outpatient Clinics (CBOCs) at the end of Fiscal Year 2014. Data includes number of unique patients and clinic encounters.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34197,69 +34177,70 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/d4u9-d4m9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/d4u9-d4m9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/d4u9-d4m9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/d4u9-d4m9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/d4u9-d4m9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/d4u9-d4m9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/d4u9-d4m9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/d4u9-d4m9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/d4u9-d4m9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://github.com/department-of-veterans-affairs/VA_Data_Assets_VHA/raw/master/VA_DataDefinitions_VisitsBedsCBOC_2015.pdf",
-            "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
+            "identifier": "VA-VHA-OIA-114",
+            "issued": "2017-07-26",
+            "keyword": [
+                "cboc",
+                "health",
+                "healthcare",
+                "outpatient",
+                "va",
+                "va clinics",
+                "veteran"
+            ],
+            "landingPage": "https://www.va.gov/health/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:042"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
+            "temporal": "2013-10-01T04:00:00Z/2014-09-30T04:00:00Z",
             "theme": [
                 "VA Healthcare Utilization"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA Community Based Outpatient Clinics, FY2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/d5k2-t34u",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2020-11-19",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-22",
-            "keyword": [
-                "utilization",
-                "veteran benefits",
-                "veterans",
-                "veterans benefits"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Mark Guagliardo",
                 "hasEmail": "mailto:VANCVAS@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/d5k2-t34u",
             "description": "Percentage of Service-Connected Disabled Who Did and Did Not Use Health Care, by Race. Data underlying the fourth figure of Part 2 of the FY2018 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Veterans Utilization Profile FY18 - Fig 17, Percentage of Service-Connected Disabled Who Did and Did Not Use Health Care, by Race",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34267,68 +34248,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/d5k2-t34u/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/d5k2-t34u/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/d5k2-t34u/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/d5k2-t34u/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/d5k2-t34u/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/d5k2-t34u/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/d5k2-t34u/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/d5k2-t34u/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/d5k2-t34u/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://www.usa.gov/government-works"
+            "identifier": "https://www.data.va.gov/api/views/d5k2-t34u",
+            "issued": "2020-11-19",
+            "keyword": [
+                "utilization",
+                "veteran benefits",
+                "veterans",
+                "veterans benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/d5k2-t34u",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2020-12-22",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Veterans Utilization Profile FY18 - Fig 17, Percentage of Service-Connected Disabled Who Did and Did Not Use Health Care, by Race"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/d5kr-n6fv",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2007-10-01T04:00:00Z/2008-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf"
-            ],
-            "keyword": [
-                "health",
-                "healthcare",
-                "hospital accreditation",
-                "patient safety",
-                "quality of care",
-                "satisfaction",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VHA Open Data",
                 "hasEmail": "mailto:vhaopendata@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VHA-OIA-028",
-            "description": "<p>Report to the Appropriations Committee of the United States House of Representatives in Response to Conference Committee Report to PL 110-186.  In an effort to provide a snapshot of the quality of care provided at VA health care facilities, this report includes information about waiting times, staffing level, infection rates, surgical volumes, quality measures, patient satisfaction, service availability and complexity, accreditation status, and patient safety. The data in this report have been drawn from multiple sources across VHA.  This dataset contains the data about Central Line Infections and Ventilator Associated Pnemonia.</p>",
-            "title": "Veterans Health Administration 2008 Hospital Report Card - Nosocomial Infections",
-            "isPartOf": "VA-VHA-OIA-583",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "029:040"
-            ],
+            "description": "<p>Report to the Appropriations Committee of the United States House of Representatives in Response to Conference Committee Report to PL 110-186.  In an effort to provide a snapshot of the quality of care provided at VA health care facilities, this report includes information about waiting times, staffing level, infection rates, surgical volumes, quality measures, patient satisfaction, service availability and complexity, accreditation status, and patient safety. The data in this report have been drawn from multiple sources across VHA.  This dataset contains the data about Central Line Infections and Ventilator Associated Pnemonia.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34336,67 +34312,75 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/d5kr-n6fv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/d5kr-n6fv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/d5kr-n6fv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/d5kr-n6fv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/d5kr-n6fv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/d5kr-n6fv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/d5kr-n6fv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/d5kr-n6fv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/d5kr-n6fv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf",
-            "dataQuality": true,
+            "identifier": "VA-VHA-OIA-028",
+            "isPartOf": "VA-VHA-OIA-583",
+            "issued": "2017-07-26",
+            "keyword": [
+                "health",
+                "healthcare",
+                "hospital accreditation",
+                "patient safety",
+                "quality of care",
+                "satisfaction",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/d5kr-n6fv",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:040"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf"
+            ],
+            "temporal": "2007-10-01T04:00:00Z/2008-09-30T04:00:00Z",
             "theme": [
                 "Section 3. Health and Nutrition"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veterans Health Administration 2008 Hospital Report Card - Nosocomial Infections"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/pocketcard/index.asp",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "statistics",
-                "veterans",
-                "women"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS Mailbox",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-236",
+            "dataQuality": true,
             "description": "<p>This report summarizes the history of women Veterans in the military and as Veterans. It profiles the characteristics of women Veterans in 2015, and illustrates how women Veterans used some of the major benefits and services that are offered by the Department of Veterans Affairs.</p>",
-            "title": "Women Veteran Report",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34405,48 +34389,45 @@
                     "title": "Women Veteran Report"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-236",
+            "issued": "2017-07-26",
+            "keyword": [
+                "statistics",
+                "veterans",
+                "women"
+            ],
+            "landingPage": "https://www.va.gov/vetdata/pocketcard/index.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Veteran Benefits",
                 "Veteran Utilization",
                 "Statistics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Women Veteran Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.oit.va.gov/docs/dashboard/201301_OIT_PMAS_Dashboard_Summary_Jan_2013.pdf",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "dashboard",
-                "pmas",
-                "summary",
-                "va"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rodney Emery",
                 "hasEmail": "mailto:rodney.emery@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OIT-OIT-058",
             "description": "<p>Jan 2013 Summary of PMAS Dashboard</p>",
-            "title": "OIT PMAS Dashboard Summary",
-            "programCode": [
-                "029:080"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34455,47 +34436,44 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-OIT-OIT-058",
+            "issued": "2017-07-26",
+            "keyword": [
+                "dashboard",
+                "pmas",
+                "summary",
+                "va"
+            ],
+            "landingPage": "https://www.oit.va.gov/docs/dashboard/201301_OIT_PMAS_Dashboard_Summary_Jan_2013.pdf",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:080"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "OIT PMAS Dashboard Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Number_of_Policyholders_by_Program_by_State_Dec_2011.csv",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-12-01T05:00:00Z/2011-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/TechnicalNotes_Number_of_Policyholders_by_Program_by_State_Dec_2011.doc"
-            ],
-            "keyword": [
-                "benefits",
-                "insurance",
-                "state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dusca Fichtel",
                 "hasEmail": "mailto:dusca.fichtel@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-INS2011-013",
+            "dataQuality": true,
             "description": "<p>Number of life insurance policyholders for each administered life insurance program listed by state. Data is current as of 12/31/11.  All programs are closed to new issues except for Service-Disabled Veterans' Insurance and Veterans' Mortgage Life Insurance.  United States Government Life Insurance was issued to WWI military personnel and Veterans.  National Service Life Insurance was established to meet the needs of WWII military personnel and Veterans.  Veterans' Special Life Insurance was issued to Korean War-era Veterans.  Veterans' Reopened Insurance provides coverage to certain classes of disabled Veterans from WWII and the Korean conflict who had dropped their government life insurance coverage.  Service-Disabled Veterans' Insurance was established in 1951 and is available to Veterans with service-connected disabilities.  Veterans' Mortgage Life Insurance was established in 1971 to provide mortgage protection life insurance to severely disabled Veterans who have received grants for the purchase of specially-adapted housing.</p>",
-            "title": "Number of Life Insurance Policyholders by Program by State",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34503,103 +34481,105 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/d6s8-i5ww/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/d6s8-i5ww/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/d6s8-i5ww/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/d6s8-i5ww/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/d6s8-i5ww/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/d6s8-i5ww/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/d6s8-i5ww/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/d6s8-i5ww/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/d6s8-i5ww/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2011-013",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Number_of_Policyholders_by_Program_by_State_Dec_2011.csv",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/VETDATA/docs/Datagov/TechnicalNotes_Number_of_Policyholders_by_Program_by_State_Dec_2011.doc"
+            ],
+            "temporal": "2011-12-01T05:00:00Z/2011-12-31T05:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Number of Life Insurance Policyholders by Program by State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/d7d8-fkip",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-06",
-            "keyword": [
-                "alabama",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VANCVAS",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/d7d8-fkip",
+            "dataQuality": true,
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State and Territories.",
-            "title": "State Summaries_Alabama",
+            "identifier": "https://www.data.va.gov/api/views/d7d8-fkip",
+            "issued": "2021-08-26",
+            "keyword": [
+                "alabama",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/d7d8-fkip",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-06",
             "programCode": [
                 "029:086"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summaries_Alabama"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-02",
-            "keyword": [
-                "fy2012 benefits",
-                "fy2012 vba",
-                "vba",
-                "vba benefits",
-                "vba benefits by state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Elwell",
                 "hasEmail": "mailto:thomas.elwell@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-ABR2012-096",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Lousiana-FY Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34607,45 +34587,47 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
-            "theme": [
-                "ABR 2012"
-            ],
-            "language": [
-                "en-US"
-            ]
-        },
+            "identifier": "VA-VBA-ABR2012-096",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "fy2012 benefits",
+                "fy2012 vba",
+                "vba",
+                "vba benefits",
+                "vba benefits by state"
+            ],
+            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-03-02",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
+            "theme": [
+                "ABR 2012"
+            ],
+            "title": "Lousiana-FY Benefits Summary"
+        },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/d7ik-gyvd",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2002-10-01T04:00:00Z/2003-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-10",
-            "keyword": [
-                "annual report",
-                "franchise fund"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VA OM Open Data",
                 "hasEmail": "mailto:VAOMOpenData@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-110",
             "description": "<p>FY 2003 Franchise Fund Annual Report at a Glance</p>",
-            "title": "FY 2003 Franchise Fund Annual Report at a Glance",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34654,46 +34636,44 @@
                     "title": "FY 2003 Franchise Fund Annual Report at a Glance"
                 }
             ],
+            "identifier": "VA-OM-OM-110",
+            "issued": "2017-07-26",
+            "keyword": [
+                "annual report",
+                "franchise fund"
+            ],
+            "landingPage": "https://www.data.va.gov/d/d7ik-gyvd",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-06-10",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2002-10-01T04:00:00Z/2003-09-30T04:00:00Z",
             "theme": [
                 "Financial"
-            ]
+            ],
+            "title": "FY 2003 Franchise Fund Annual Report at a Glance"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/HEALTHPOLICYPLANNING/PAF.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2015-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "county",
-                "enrollee",
-                "fips",
-                "health",
-                "healthcare",
-                "state",
-                "veteran"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VHA Open Data",
                 "hasEmail": "mailto:vhaopendata@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VHA-OPP-001",
-            "description": "<p>The VA's Veteran Health Administration, in support of the Open Data Initiative, is providing the number of Veteran enrollees by state/county for fiscal year 2015.  For additional information about Veteran Priority Groups, see the data assets metadata.</p>",
-            "title": "FY2015 VHA Enrollees by County",
+            "dataQuality": true,
+            "describedBy": "https://raw.githubusercontent.com/vacobrydsk/VAEnrolleesByCountyDataDictionary/master/VAEnrolleesByCountyDataDictionary.xlsx",
             "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-            "programCode": [
-                "029:080"
-            ],
+            "description": "<p>The VA's Veteran Health Administration, in support of the Open Data Initiative, is providing the number of Veteran enrollees by state/county for fiscal year 2015.  For additional information about Veteran Priority Groups, see the data assets metadata.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34701,70 +34681,73 @@
                     "mediaType": "text/plain"
                 }
             ],
-            "describedBy": "https://raw.githubusercontent.com/vacobrydsk/VAEnrolleesByCountyDataDictionary/master/VAEnrolleesByCountyDataDictionary.xlsx",
-            "dataQuality": true,
+            "identifier": "VA-VHA-OPP-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "county",
+                "enrollee",
+                "fips",
+                "health",
+                "healthcare",
+                "state",
+                "veteran"
+            ],
+            "landingPage": "https://www.va.gov/HEALTHPOLICYPLANNING/PAF.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:080"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2014-10-01T04:00:00Z/2015-09-30T04:00:00Z",
             "theme": [
                 "Veteran Health Administration Enrollee by County"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY2015 VHA Enrollees by County"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/d7xw-7fqx",
-            "issued": "2023-07-19",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-16",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary North Dakota FY2021",
+            "identifier": "https://www.data.va.gov/api/views/d7xw-7fqx",
+            "issued": "2023-07-19",
             "keyword": [
                 "fy2021 data",
                 "ncvas state summary",
                 "north dakota"
             ],
-            "identifier": "https://www.data.va.gov/api/views/d7xw-7fqx",
+            "landingPage": "https://www.data.va.gov/d/d7xw-7fqx",
+            "modified": "2024-06-16",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary North Dakota FY2021",
             "title": "NCVAS State Summary North Dakota FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.data.va.gov/d/d8r4-2pub",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2017-11-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "healthcare",
-                "tbi"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Clark Timmins",
                 "hasEmail": "mailto:clark.timmins@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VIA-9",
+            "dataQuality": true,
             "description": "<p>This Service provides access to Tramatic Brain injury patient data consult notes. The service also provides one write service method writeNote. The Service supports single site data access. Users of this Service are intended to be healthcare providers.</p>",
-            "title": "Traumatic Brain Injury service (TBI) Service",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34773,45 +34756,42 @@
                     "title": "Traumatic Brain Injury service (TBI) Service"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "identifier": "VA-VIA-9",
+            "issued": "2017-11-17",
+            "keyword": [
+                "healthcare",
+                "tbi"
+            ],
+            "landingPage": "https://www.data.va.gov/d/d8r4-2pub",
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
+            "title": "Traumatic Brain Injury service (TBI) Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-02",
-            "keyword": [
-                "fy2012 benefits",
-                "fy2012 vba",
-                "vba",
-                "vba benefits",
-                "vba benefits by state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Elwell",
                 "hasEmail": "mailto:thomas.elwell@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-ABR2012-116",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Other_Foreign-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34819,46 +34799,47 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-116",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "fy2012 benefits",
+                "fy2012 vba",
+                "vba",
+                "vba benefits",
+                "vba benefits by state"
+            ],
+            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2022-03-02",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "ABR 2012"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Other_Foreign-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/d9p6-7mi4",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2020-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "department of veterans affairs",
-                "strategic plan",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:Tom.Garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-078",
             "description": "<p>The VA Strategic Plan for 2010\u20132014 established our enduring principles: people-centric, results-driven, and forward-looking. We will continue to use those principles to increase Veterans\u2019 access to benefits, eliminate the disability claims backlog, and end the rescue phase of Veteran homelessness.</p>",
-            "title": "Department of Veterans Affairs FY 2014-2020 Strategic Plan",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34867,44 +34848,46 @@
                     "title": "Department of Veterans Affairs FY 2014- 2012 Strategic Plan"
                 }
             ],
+            "identifier": "VA-OEI-OEI-078",
+            "issued": "2017-07-26",
+            "keyword": [
+                "department of veterans affairs",
+                "strategic plan",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/d9p6-7mi4",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2014-10-01T04:00:00Z/2020-09-30T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Department of Veterans Affairs FY 2014-2020 Strategic Plan"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/daw2-u66m",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "new jersey",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:Tom.Garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-117",
             "description": "<p>This is a summary of the services and program provided by VA in New Jersey in fiscal year 2014.</p>",
-            "title": "State Summary:  New Jersey",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34913,40 +34896,44 @@
                     "title": "State Summary:  New Jersey"
                 }
             ],
+            "identifier": "VA-OEI-OEI-117",
+            "issued": "2017-07-26",
+            "keyword": [
+                "new jersey",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/daw2-u66m",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "State Summary:  New Jersey"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/dbei-k7u8",
-            "issued": "2023-06-14",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-26",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/dbei-k7u8",
             "description": "These data are based on the latest Veteran Population Projection Model, VetPop2020, provided by the National Center for Veterans Statistics and Analysis, published in 2023.",
-            "title": "FY 2021_NCVAS Age Group Over Time Data For State Summaries",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -34954,62 +34941,55 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/dbei-k7u8/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dbei-k7u8/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dbei-k7u8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/dbei-k7u8/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dbei-k7u8/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dbei-k7u8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/dbei-k7u8/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dbei-k7u8/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dbei-k7u8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/dbei-k7u8",
+            "issued": "2023-06-14",
+            "landingPage": "https://www.data.va.gov/d/dbei-k7u8",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-08-26",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "FY 2021_NCVAS Age Group Over Time Data For State Summaries"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-02",
-            "keyword": [
-                "fy2012 benefits",
-                "fy2012 vba",
-                "vba",
-                "vba benefits",
-                "vba benefits by state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Elwell",
                 "hasEmail": "mailto:thomas.elwell@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-ABR2012-102",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Mississippi-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35017,79 +34997,79 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-102",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "fy2012 benefits",
+                "fy2012 vba",
+                "vba",
+                "vba benefits",
+                "vba benefits by state"
+            ],
+            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2022-03-02",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "ABR 2012"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Mississippi-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/dbya-s55i",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary New York FY2023",
+            "identifier": "https://www.data.va.gov/api/views/dbya-s55i",
             "issued": "2024-06-16",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-12",
             "keyword": [
                 "fy2023",
                 "ncvas state summary",
                 "new york"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/dbya-s55i",
+            "modified": "2024-07-12",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/dbya-s55i",
-            "description": "NCVAS State Summary New York FY2023",
-            "title": "NCVAS State Summary New York FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary New York FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www1.va.gov/VETDATA/docs/Datagov/FY09_EDU_Recipients_by_State.csv",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2008-10-01T04:00:00Z/2009-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www1.va.gov/VETDATA/docs/Datagov/FY09_EDU_Recipients_by_State.csv"
-            ],
-            "keyword": [
-                "education",
-                "veteran"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Salminio Garner",
                 "hasEmail": "mailto:salminio.garner1@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-EDU2009-001",
+            "dataQuality": true,
             "description": "<p>FY 09 Education Recipients by State. The data represents the number of individuals by VA education program who have used their VA education benefit during fiscal year 2009. The data does not include 34,393  individuals who used the Post-9/11 GI Bill during fiscal year 2009, nor does it include 23,181 individuals located in the Philippines and Other Foreign locations as well as those where the address data could not be specifically attributed to a specific state.</p>",
-            "title": "FY 09 Education Recipients by State.",
-            "isPartOf": "VA-VBA-MASTER-EDUCATION-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35097,105 +35077,106 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/dc2s-kiey/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dc2s-kiey/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dc2s-kiey/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/dc2s-kiey/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dc2s-kiey/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dc2s-kiey/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/dc2s-kiey/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dc2s-kiey/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dc2s-kiey/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-EDU2009-001",
+            "isPartOf": "VA-VBA-MASTER-EDUCATION-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "education",
+                "veteran"
+            ],
+            "landingPage": "https://www1.va.gov/VETDATA/docs/Datagov/FY09_EDU_Recipients_by_State.csv",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www1.va.gov/VETDATA/docs/Datagov/FY09_EDU_Recipients_by_State.csv"
+            ],
+            "temporal": "2008-10-01T04:00:00Z/2009-09-30T04:00:00Z",
             "theme": [
                 "Section 4. Education"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 09 Education Recipients by State."
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/dc5k-d9hk",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-10-30",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "bf2434e8-7e16-4489-a778-f4e20f93479f",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary South Carolina FY2017",
+            "identifier": "bf2434e8-7e16-4489-a778-f4e20f93479f",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/dc5k-d9hk",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
             "programCode": [
                 "029:086"
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data",
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "State Summary South Carolina FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ptsd.va.gov/repository",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "All data is within the public domain and is currently available for download.",
-            "issued": "2021-09-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-29",
-            "keyword": [
-                "ptsd-repository",
-                "ptsd treatment",
-                "reference guide",
-                "treatment coding"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for PTSD",
                 "hasEmail": "mailto:ncptsd@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for PTSD"
-            },
-            "identifier": "https://www.data.va.gov/api/views/dd6z-c9xm",
             "description": "This document contains brief descriptions of many of the treatments found in the PTSD Repository, organized by treatment category.\n\nNote: The download is a .zip file which contains the PDF Reference Guide.",
-            "title": "Reference Guide - Treatments Found in the PTSD Repository",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35203,47 +35184,46 @@
                     "mediaType": "application/x-zip-compressed"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
-            "theme": [
-                "PTSD Randomized Controlled Trials"
+            "identifier": "https://www.data.va.gov/api/views/dd6z-c9xm",
+            "issued": "2021-09-13",
+            "keyword": [
+                "ptsd-repository",
+                "ptsd treatment",
+                "reference guide",
+                "treatment coding"
             ],
+            "landingPage": "https://www.ptsd.va.gov/repository",
             "language": [
                 "en-US"
-            ]
+            ],
+            "modified": "2024-03-29",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for PTSD"
+            },
+            "rights": "All data is within the public domain and is currently available for download.",
+            "theme": [
+                "PTSD Randomized Controlled Trials"
+            ],
+            "title": "Reference Guide - Treatments Found in the PTSD Repository"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-02",
-            "keyword": [
-                "fy2012 benefits",
-                "fy2012 vba",
-                "vba",
-                "vba benefits",
-                "vba benefits by state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Elwell",
                 "hasEmail": "mailto:thomas.elwell@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-ABR2012-130",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Wyoming-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35251,91 +35231,79 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-130",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "fy2012 benefits",
+                "fy2012 vba",
+                "vba",
+                "vba benefits",
+                "vba benefits by state"
+            ],
+            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2022-03-02",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "ABR 2012"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Wyoming-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/df26-ez7w",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary New Jersey FY2023",
+            "identifier": "https://www.data.va.gov/api/views/df26-ez7w",
             "issued": "2024-06-14",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-12",
             "keyword": [
                 "fy2023",
                 "ncvas state summary",
                 "new jersey"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/df26-ez7w",
+            "modified": "2024-07-12",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/df26-ez7w",
-            "description": "NCVAS State Summary New Jersey FY2023",
-            "title": "NCVAS State Summary New Jersey FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary New Jersey FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/dg8j-vep9",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2022-11-28",
-            "@type": "dcat:Dataset",
-            "modified": "2022-11-28",
-            "keyword": [
-                "2021",
-                "ethnicity",
-                "fy2021",
-                "fy 2021",
-                "fy21",
-                "fy 21",
-                "healthcare",
-                "health care",
-                "race",
-                "va healthcare",
-                "va health care",
-                "va user",
-                "va users",
-                "veteran",
-                "veteran healthcare",
-                "veteran health care",
-                "veterans",
-                "veteran user",
-                "veteran users"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Mike Schwaber",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/dg8j-vep9",
+            "dataQuality": true,
             "description": "Notes:\n\n\"Total Number of Veterans\" represents FY 2021 projected Veteran counts from VA's Veteran Population Projection Model 2020 (VetPop20). These projections represent living Veterans as of 9/30/2021 and are made with the assumption that Veterans are not missing information (e.g., race, etc.).\n\n\"Veteran VA Users\" represents historical Veteran VA user counts from VA's United States Veterans Eligibility Trends and Statistics 2021 (USVETS 2021). These counts represent Veterans who used any VA benefit or service during FY 2021 (includes both living and deceased Veterans as of end of FY 2021).\n\n\"Veteran VA Healthcare Users\" represents historical Veteran VA healthcare user counts from VA's United States Veterans Eligibility Trends and Statistics 2021 (USVETS 2021). These counts represent Veterans who used VA healthcare during FY 2021 (includes both living and deceased Veterans as of end of FY 2021).\n\n\"Veteran VA Users\" includes Veteran users of VA healthcare or any other VA benefit or service.\n\nSources: USVETS 2021 and VetPop20\nEffective Date: 9/30/2021",
-            "title": "FY 2021 Total Number of Veterans, Veteran VA Users, and Veteran VA Healthcare Users by Race",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35343,62 +35311,78 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/dg8j-vep9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dg8j-vep9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dg8j-vep9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/dg8j-vep9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dg8j-vep9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dg8j-vep9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/dg8j-vep9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dg8j-vep9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dg8j-vep9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y",
+            "identifier": "https://www.data.va.gov/api/views/dg8j-vep9",
+            "issued": "2022-11-28",
+            "keyword": [
+                "2021",
+                "ethnicity",
+                "fy2021",
+                "fy 2021",
+                "fy21",
+                "fy 21",
+                "healthcare",
+                "health care",
+                "race",
+                "va healthcare",
+                "va health care",
+                "va user",
+                "va users",
+                "veteran",
+                "veteran healthcare",
+                "veteran health care",
+                "veterans",
+                "veteran user",
+                "veteran users"
+            ],
+            "landingPage": "https://www.data.va.gov/d/dg8j-vep9",
             "language": [
                 "English"
-            ]
+            ],
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode",
+            "modified": "2022-11-28",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "FY 2021 Total Number of Veterans, Veteran VA Users, and Veteran VA Healthcare Users by Race"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/di4c-6ppw",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-11-09",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "e21528a4-8d84-4602-96d8-64450c3cdd3d",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Illinois FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35406,52 +35390,36 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "e21528a4-8d84-4602-96d8-64450c3cdd3d",
+            "issued": "2017-11-09",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/di4c-6ppw",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summary Illinois FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/dipq-gh5w",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2020-10-28",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-05",
-            "keyword": [
-                "cemetery",
-                "disability compensation",
-                "disability pension",
-                "gulf war",
-                "healthcare",
-                "health care",
-                "home loan guaranty",
-                "life insurance",
-                "memorial",
-                "memorials",
-                "pension",
-                "veteran population",
-                "veterans",
-                "veterans affairs",
-                "veterans data",
-                "vocational rehabilitation",
-                "vocational rehabilitation services"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Mark Guagliardo",
                 "hasEmail": "mailto:VANCVAS@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/dipq-gh5w",
             "description": "This data set consists of one row per federal fiscal year (FY) from FY 2005 - FY 2019, and reports the number and percent of users each of seven VA programs for Veterans who were in service at any time between August 2, 1990, and September 10, 2001, the dates of the Pre-9/11 Gulf War era. The denominator of percent is the number of living Veterans in the FY. The number and percent of users is cumulative since FY 2005. Thus, for example FY 2006 data includes all Veterans who served in the era, were alive at some time during FY 2006 and participated in the program at any time during FY 2005 and FY 2006.",
-            "title": "Gulf War - Pre 9/11 Veterans: Trends in Cumulative Users by VA Program",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35459,99 +35427,114 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/dipq-gh5w/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dipq-gh5w/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dipq-gh5w/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/dipq-gh5w/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dipq-gh5w/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dipq-gh5w/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/dipq-gh5w/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dipq-gh5w/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dipq-gh5w/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://www.usa.gov/government-works"
+            "identifier": "https://www.data.va.gov/api/views/dipq-gh5w",
+            "issued": "2020-10-28",
+            "keyword": [
+                "cemetery",
+                "disability compensation",
+                "disability pension",
+                "gulf war",
+                "healthcare",
+                "health care",
+                "home loan guaranty",
+                "life insurance",
+                "memorial",
+                "memorials",
+                "pension",
+                "veteran population",
+                "veterans",
+                "veterans affairs",
+                "veterans data",
+                "vocational rehabilitation",
+                "vocational rehabilitation services"
+            ],
+            "landingPage": "https://www.data.va.gov/d/dipq-gh5w",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2020-11-05",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Gulf War - Pre 9/11 Veterans: Trends in Cumulative Users by VA Program"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.usaspending.gov/",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Monica Reyes",
+                "hasEmail": "mailto:monica.reyes@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>USA Spending- Veterans Surviving Spouses and Children- February 2014</p>",
+            "identifier": "VA-VBA-USASPENDING012014-033",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-02-01T05:00:00Z/2014-02-28T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 105",
                 "compensation and pension",
                 "usa spending",
                 "veterans surviving spouses and children"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Monica Reyes",
-                "hasEmail": "mailto:monica.reyes@va.gov"
-            },
+            "landingPage": "https://www.usaspending.gov/",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:033"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-USASPENDING012014-033",
-            "description": "<p>USA Spending- Veterans Surviving Spouses and Children- February 2014</p>",
-            "title": "USA Spending file- 02/2014 Compensation and Pension-  CFDA 64.105",
-            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
-            "programCode": [
-                "029:033"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2014-02-01T05:00:00Z/2014-02-28T05:00:00Z",
             "theme": [
                 "USA Spending"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USA Spending file- 02/2014 Compensation and Pension-  CFDA 64.105"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/dirw-rjsf",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "illinois",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:Tom.Garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-098",
             "description": "<p>This is a summary of the programs and services provided by VA in Illinois in fiscal year 2014.</p>",
-            "title": "State Summary:  Illinois",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35560,43 +35543,44 @@
                     "title": "State Summary:  Illinois"
                 }
             ],
+            "identifier": "VA-OEI-OEI-098",
+            "issued": "2017-07-26",
+            "keyword": [
+                "illinois",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/dirw-rjsf",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "State Summary:  Illinois"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/diy6-2dij",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "pennsylvania"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DG&amp;A Mailgroup",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-209",
             "description": "<p>This summary describes the programs and services VA provided in Pennsylvania in fiscal year 2015.</p>",
-            "title": "State Summary: Pennsylvania FY15",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35605,41 +35589,41 @@
                     "title": "Pennsylvania"
                 }
             ],
+            "identifier": "VA-OEI-OEI-209",
+            "issued": "2017-07-26",
+            "keyword": [
+                "pennsylvania"
+            ],
+            "landingPage": "https://www.data.va.gov/d/diy6-2dij",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "State Summary: Pennsylvania FY15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/dizi-2nzn",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2019-06-13",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS Mailbox",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "3c3df421-7430-4f27-99fc-cafa97b1e37f",
+            "dataQuality": true,
             "description": "<p>To show percentage of distribution of Veterans by gender and civilian population for age, race/ethnicity, important socio-economic characteristics and period of service.</p>",
-            "title": "Profile of Veterans: (2017)",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35647,38 +35631,37 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "3c3df421-7430-4f27-99fc-cafa97b1e37f",
+            "issued": "2019-06-13",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/dizi-2nzn",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Profile of Veterans: (2017)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.data.va.gov/d/dj7m-f7gw",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2017-11-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "healthcare",
-                "patient"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Clark Timmins",
                 "hasEmail": "mailto:clark.timmins@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VIA-4",
+            "dataQuality": true,
             "description": "<p>Used to obtain patient specific data</p>",
-            "title": "Find Patient Service",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35687,22 +35670,51 @@
                     "title": "Find Patient Service"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "identifier": "VA-VIA-4",
+            "issued": "2017-11-17",
+            "keyword": [
+                "healthcare",
+                "patient"
+            ],
+            "landingPage": "https://www.data.va.gov/d/dj7m-f7gw",
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
+            "title": "Find Patient Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/dk4k-6q54",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHASAILOperations",
+                "hasEmail": "mailto:VHASAILOperations@va.gov"
+            },
+            "dataQuality": true,
+            "description": "VA Community Care Comparison or VAC3 (formerly Why Not the Best VA) is a system for comparing Veterans Health Administration (VHA) hospital system performance with regional and U.S. national benchmarks.\u00a0 This report includes key quality measures available on CMS Hospital Compare and top hospital recognition programs from reporting agencies of hospital quality.\u00a0VAC3 data tables are updated every quarter.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/dk4k-6q54/application/x-zip-compressed",
+                    "mediaType": "application/x-zip-compressed"
+                }
+            ],
+            "identifier": "https://www.data.va.gov/api/views/dk4k-6q54",
             "issued": "2021-06-24",
-            "@type": "dcat:Dataset",
-            "temporal": "2020-10-01/2021-9-30",
-            "modified": "2022-01-10",
             "keyword": [
                 "2021",
                 "fy2021",
@@ -35726,162 +35738,133 @@
                 "veteran",
                 "wntbva"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHASAILOperations",
-                "hasEmail": "mailto:VHASAILOperations@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/dk4k-6q54",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-01-10",
+            "programCode": [
+                "029:040"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/dk4k-6q54",
-            "description": "VA Community Care Comparison or VAC3 (formerly Why Not the Best VA) is a system for comparing Veterans Health Administration (VHA) hospital system performance with regional and U.S. national benchmarks.\u00a0 This report includes key quality measures available on CMS Hospital Compare and top hospital recognition programs from reporting agencies of hospital quality.\u00a0VAC3 data tables are updated every quarter.",
-            "title": "VA Community Care Comparison  (VAC3)  - FY2021 All Facilities - Formerly Why Not the Best VA",
-            "programCode": [
-                "029:040"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/dk4k-6q54/application/x-zip-compressed",
-                    "mediaType": "application/x-zip-compressed"
-                }
-            ],
             "spatial": "United States, Puerto Rico",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "temporal": "2020-10-01/2021-9-30",
             "theme": [
                 "Hospital Quality Measurement"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA Community Care Comparison  (VAC3)  - FY2021 All Facilities - Formerly Why Not the Best VA"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/dktx-ecys",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Nevada FY2023",
+            "identifier": "https://www.data.va.gov/api/views/dktx-ecys",
             "issued": "2024-06-14",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-12",
             "keyword": [
                 "fy2023",
                 "ncvas state summary",
                 "nevada"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/dktx-ecys",
+            "modified": "2024-07-12",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/dktx-ecys",
-            "description": "NCVAS State Summary Nevada FY2023",
-            "title": "NCVAS State Summary Nevada FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Nevada FY2023"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/dmn9-k44e",
-            "issued": "2023-07-18",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-16",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary New York FY2021",
+            "identifier": "https://www.data.va.gov/api/views/dmn9-k44e",
+            "issued": "2023-07-18",
             "keyword": [
                 "fy2021 data",
                 "ncvas state summary",
                 "new york"
             ],
-            "identifier": "https://www.data.va.gov/api/views/dmn9-k44e",
+            "landingPage": "https://www.data.va.gov/d/dmn9-k44e",
+            "modified": "2024-06-16",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary New York FY2021",
             "title": "NCVAS State Summary New York FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://benefits.va.gov/benefits/media-publications.asp",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Elwell",
+                "hasEmail": "mailto:thomas.elwell@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>Survivors &amp; Dependents Educational Assistance- Chapter 35</p>",
+            "identifier": "VA-VBA-MEDIAPUB-039",
+            "isPartOf": "VA-VBA-MASTER-MEDIAPUBLICATIONS-001",
             "issued": "2017-07-26",
-            "temporal": "2012-09-01T04:00:00Z/2012-09-01T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-08",
             "keyword": [
                 "benefits fact sheet",
                 "general benefit information",
                 "va benefits",
                 "va fact sheet"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Elwell",
-                "hasEmail": "mailto:thomas.elwell@va.gov"
-            },
+            "landingPage": "https://benefits.va.gov/benefits/media-publications.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-03-08",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-MEDIAPUB-039",
-            "description": "<p>Survivors &amp; Dependents Educational Assistance- Chapter 35</p>",
-            "title": "Survivors & Dependents Educational Assistance- Chapter 35",
-            "isPartOf": "VA-VBA-MASTER-MEDIAPUBLICATIONS-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2012-09-01T04:00:00Z/2012-09-01T04:00:00Z",
             "theme": [
                 "General Benefit Information"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Survivors & Dependents Educational Assistance- Chapter 35"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/dph5-xt4w",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2019-09-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "rural veterans",
-                "veterans farmer"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tamara Lee",
                 "hasEmail": "mailto:tamara.lee@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veteran Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/dph5-xt4w",
             "description": "The Office of Data Governance and Analysis (DGA) creates statistical data for various Veteran related projects. This table displays the count and percent, by county, of Veterans who are farmers and/or dairymen comparative for the entire state's population of Veteran farmers or dairymen in California for 2015. The data was created from our administrative database U.S. Veterans Eligibility Trends and Statistics (USVETS), for the recent event Apps for Ag Hackathon.  \n\n\nThe U.S. Veterans Eligibility Trends and Statistics (USVETS) is the single integrated dataset of Veteran demographic and socioeconomic data. It provides the most comprehensive picture of the Veteran population possible to support statistical, trend and longitudinal analysis. USVETS has both a static dataset, represents a single authoritative record of all living and deceased Veterans, and fiscal year datasets, represents a snapshot of a Veteran for each fiscal year. USVETS consists mainly of data sources from the Veterans Benefit Administration, the Veterans Health Administration, the Department of Defense\u2019s Defense Manpower Data Center, and other data sources including commercial data sources. This dataset contains information about individual Veterans including demographics, details of military service, VA benefit usage, and more. The dataset contains one record per Veteran. It includes all living and deceased Veterans. USVETS data includes Veterans residing in states, US territories and foreign countries. VA uses this database to conduct statistical analytics, predictive modeling, and other data reporting. USVETS includes the software, hardware, and the associated processes that produce various VA work products and related files for Veteran analytics.",
-            "title": "Veteran Farmer Counts and Percentages in California Counties (2015)",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -35889,111 +35872,131 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/dph5-xt4w/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dph5-xt4w/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dph5-xt4w/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/dph5-xt4w/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dph5-xt4w/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dph5-xt4w/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/dph5-xt4w/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dph5-xt4w/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dph5-xt4w/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/dph5-xt4w",
+            "issued": "2019-09-17",
+            "keyword": [
+                "rural veterans",
+                "veterans farmer"
+            ],
+            "landingPage": "https://www.data.va.gov/d/dph5-xt4w",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veteran Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "Veteran Farmer Counts and Percentages in California Counties (2015)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.usaspending.gov",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Monica Reyes",
+                "hasEmail": "mailto:monica.reyes@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>USA Spending- Veterans Surviving Spouses and Children- December 2013.</p>",
+            "identifier": "VA-VBA-USASPENDING122013-007",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2013-12-01T05:00:00Z/2013-12-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 105",
                 "compensation and pension",
                 "usa spending",
                 "veterans surviving spouses and children"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Monica Reyes",
-                "hasEmail": "mailto:monica.reyes@va.gov"
-            },
+            "landingPage": "https://www.usaspending.gov",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-USASPENDING122013-007",
-            "description": "<p>USA Spending- Veterans Surviving Spouses and Children- December 2013.</p>",
-            "title": "USA Spending file- Compensation and Pension-  CFDA 64.105",
-            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2013-12-01T05:00:00Z/2013-12-30T05:00:00Z",
             "theme": [
                 "USA Spending"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USA Spending file- Compensation and Pension-  CFDA 64.105"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/dqja-7dy4",
-            "issued": "2023-08-11",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-20",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Vermont FY2021",
+            "identifier": "https://www.data.va.gov/api/views/dqja-7dy4",
+            "issued": "2023-08-11",
             "keyword": [
                 "fy2021 data",
                 "ncvas state summary",
                 "vermont"
             ],
-            "identifier": "https://www.data.va.gov/api/views/dqja-7dy4",
+            "landingPage": "https://www.data.va.gov/d/dqja-7dy4",
+            "modified": "2024-06-20",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Vermont FY2021",
             "title": "NCVAS State Summary Vermont FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/dqvz-widg",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The Consolidated Copayment Processing Center (CCPC) database contains Veteran patient contact and billing information in order to support the printing and mailing of patient billing statements. The CCPC system is designed to handle first-party medical debt billing information. First-party billing is defined as a patient debt for which the patient is responsible for payment (normally co-payment) for health care treatment. This differs from third-party billing where a third party (e.g., insurance company, Health Maintenance Organization (HMO)) is primarily responsible for repaying the VA. CCPC does not handle third-party billing information. The Veterans Health Information Systems and Technology Architecture Accounts Receivable (AR) module collects information for CCPC at every Veterans Affairs Medical Center (VAMC). A daily batch process is used to collect and transmit the information to the VA Austin Information Technology Center. All collected patient and billing information is kept active on CCPC for a period of one month. A master list containing six months activity is archived for reference should historical information be needed. The users of this database include the VAMCs, Veterans Health Administration Chief Business Office, and the patients who receive billing statements.</p>",
+            "identifier": "VA-VHA-CBO-003",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1997-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "bill",
                 "billing",
@@ -36007,61 +36010,42 @@
                 "va",
                 "veteran"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/dqvz-widg",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:041"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-CBO-003",
-            "description": "<p>The Consolidated Copayment Processing Center (CCPC) database contains Veteran patient contact and billing information in order to support the printing and mailing of patient billing statements. The CCPC system is designed to handle first-party medical debt billing information. First-party billing is defined as a patient debt for which the patient is responsible for payment (normally co-payment) for health care treatment. This differs from third-party billing where a third party (e.g., insurance company, Health Maintenance Organization (HMO)) is primarily responsible for repaying the VA. CCPC does not handle third-party billing information. The Veterans Health Information Systems and Technology Architecture Accounts Receivable (AR) module collects information for CCPC at every Veterans Affairs Medical Center (VAMC). A daily batch process is used to collect and transmit the information to the VA Austin Information Technology Center. All collected patient and billing information is kept active on CCPC for a period of one month. A master list containing six months activity is archived for reference should historical information be needed. The users of this database include the VAMCs, Veterans Health Administration Chief Business Office, and the patients who receive billing statements.</p>",
-            "title": "Consolidated Copayment Processing Center (CCPC)",
-            "programCode": [
-                "029:041"
-            ],
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "1997-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Consolidated Copayment Processing Center (CCPC)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/dqya-pnmj",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-29",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 101"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/dqya-pnmj",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to assist States and federally recognized tribal governments in the establishment, expansion, and improvement of veterans' cemeteries. Monetary assistance is provided under this program to establish, expand, and improve State or Tribal government veterans\u2019 cemeteries. Cemeteries must be State or Tribal Government owned and operated solely for the interment of eligible veterans and their dependents and/or spouses. Construction cost means the amount found necessary to convert a tract of land to an operational cemetery. The cemetery must be used solely for the interment of veterans, their wives, husbands, surviving spouses, minor children, and unmarried adult children who were physically or mentally disabled and incapable of self-support: section 38 CFR Part 38.620.</p>",
-            "title": "USA SPENDING C&P BURIAL B101 VETERANS CEMETARY GRANTS PROGRAM MAR2019",
-            "isPartOf": "d17c822a-717c-40ff-8fbe-3dcaefddb706",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36069,100 +36053,97 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/dqya-pnmj/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dqya-pnmj/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dqya-pnmj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/dqya-pnmj/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dqya-pnmj/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dqya-pnmj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/dqya-pnmj/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dqya-pnmj/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dqya-pnmj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/dqya-pnmj",
+            "isPartOf": "d17c822a-717c-40ff-8fbe-3dcaefddb706",
+            "issued": "2019-03-29",
+            "keyword": [
+                "cfda 64 101"
+            ],
+            "landingPage": "https://www.data.va.gov/d/dqya-pnmj",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING C&P BURIAL B101 VETERANS CEMETARY GRANTS PROGRAM MAR2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/dr7d-pwue",
             "bureauCode": [
                 "029:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Tom Garin",
+                "hasEmail": "mailto:tom.garin@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>This dataset contains information on minority veteran healthcare usage, educational attainment, unemployment rates, median income, and projected population figures.</p>",
+            "identifier": "1d427f8d-0018-4fac-905b-6008ead44b3d",
             "issued": "2017-03-15",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "health care",
                 "income",
                 "statistics"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Tom Garin",
-                "hasEmail": "mailto:tom.garin@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/dr7d-pwue",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "1d427f8d-0018-4fac-905b-6008ead44b3d",
-            "description": "<p>This dataset contains information on minority veteran healthcare usage, educational attainment, unemployment rates, median income, and projected population figures.</p>",
-            "title": "2014 Minority Veterans Demographics",
-            "programCode": [
-                "029:086"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
-        },
-        {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/drhc-gfsc",
-            "bureauCode": [
-                "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "1873",
-                "annual report",
-                "deparment of veterans affairs",
-                "veterans"
+            "title": "2014 Minority Veterans Demographics"
+        },
+        {
+            "@type": "dcat:Dataset",
+            "accessLevel": "public",
+            "bureauCode": [
+                "029:00"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:Tom.Garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-138",
             "description": "<p>VA Historical Annual Reports detail services provided by the Department for each Fiscal Year, including Benefits, Healthcare, and Burial/Memorial services.  The Reports also describe the topics of administration and management within VA, ranging from data on personnel to information on construction projects.  Statistical tables for a variety of subjects are also included.</p>",
-            "title": "Annual Report:  1873",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36171,43 +36152,44 @@
                     "title": "Annual Report:  1873"
                 }
             ],
+            "identifier": "VA-OEI-OEI-138",
+            "issued": "2017-07-26",
+            "keyword": [
+                "1873",
+                "annual report",
+                "deparment of veterans affairs",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/drhc-gfsc",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Demographics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Annual Report:  1873"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/drst-em7u",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2014-10-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-21",
-            "keyword": [
-                "cars",
-                "establishments"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vikki Soukup",
                 "hasEmail": "mailto:Vikki.Soukup@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-102",
             "description": "<p>Activity in terms of establishments and dispositions for CARS on a monthly basis</p>",
-            "title": "COIN 0022 CARS MONTHLY CRS TOTALS REPORT Oct 2014",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36215,42 +36197,42 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-102",
+            "issued": "2017-07-26",
+            "keyword": [
+                "cars",
+                "establishments"
+            ],
+            "landingPage": "https://www.data.va.gov/d/drst-em7u",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-21",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2014-10-01T04:00:00Z/2014-10-31T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "COIN 0022 CARS MONTHLY CRS TOTALS REPORT Oct 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/drup-y3qq",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "locations",
-                "ptsd",
-                "va"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Kevin Reid",
                 "hasEmail": "mailto:vawebservices@med.va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OIT-OIT-053",
             "description": "<p>The PTSD web service provides PTSD Program information from Facilities and Leadership Directory database.</p>",
-            "title": "Posttraumatic Stress Disorder (PTSD) Programs",
-            "programCode": [
-                "029:080"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36259,43 +36241,44 @@
                     "title": "Post Trauamatic Stress Disorder (PTSD) Progrms"
                 }
             ],
+            "identifier": "VA-OIT-OIT-053",
+            "issued": "2017-07-26",
+            "keyword": [
+                "locations",
+                "ptsd",
+                "va"
+            ],
+            "landingPage": "https://www.data.va.gov/d/drup-y3qq",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:080"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "Posttraumatic Stress Disorder (PTSD) Programs"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/budget/report/",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-01-01T05:00:00Z/2011-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "accountability",
-                "performance",
-                "report"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David Zlowe",
                 "hasEmail": "mailto:David.Zlowe@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-003",
+            "dataQuality": true,
             "description": "<p>2011 VA Performance and Accountability Report.</p>",
-            "title": "2011 VA Performance and Accountability Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36304,44 +36287,46 @@
                     "title": "zip"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-003",
+            "issued": "2017-07-26",
+            "keyword": [
+                "accountability",
+                "performance",
+                "report"
+            ],
+            "landingPage": "https://www.va.gov/budget/report/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-01-01T05:00:00Z/2011-12-31T05:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2011 VA Performance and Accountability Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ds2g-hy9f",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-20",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cdfa 64.124"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE D BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/ds2g-hy9f",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION PROGRAM to provide educational assistance to persons entering the Armed Forces after December 31, 1976, and before July 1, 1985; to assist persons in obtaining an education they might otherwise not be able to afford; and to promote and assist the all volunteer military program of the United States by attracting qualified persons to serve in the Armed Forces. The participant must have entered on active duty on or after January 1, 1977, and before July 1, 1985, and either served on active duty for more than 180 continuous days receiving an other than dishonorable discharge, or have been discharged after January, 1, 1977 because of a service-connected disability. Also eligible are participants who serve for more than 180 days and who continue on active duty and have completed their first period of obligated service (or 6 years of active duty, whichever comes first). Participants must also have satisfactorily contributed to the program. (Satisfactory contribution consists of monthly deduction of $25 to $100 from military pay, up to a maximum of $2,700, for deposit in a special training fund.) Participants may make lump-sum contributions. No individuals on active duty in the Armed Forces may initially begin contributing to this program after March 31, 1987.</p>",
-            "title": "USA SPENDING EDUCATION CH30 B124 POST-VIETNAM ERA VETERANS\u2019 EDUCATIONAL ASSISTANCE APR2019",
-            "isPartOf": "d7a8ad46-1fb5-4469-82c4-e2ee7348136c",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36349,43 +36334,62 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ds2g-hy9f/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ds2g-hy9f/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ds2g-hy9f/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ds2g-hy9f/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ds2g-hy9f/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ds2g-hy9f/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ds2g-hy9f/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ds2g-hy9f/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ds2g-hy9f/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/ds2g-hy9f",
+            "isPartOf": "d7a8ad46-1fb5-4469-82c4-e2ee7348136c",
+            "issued": "2019-03-20",
+            "keyword": [
+                "cdfa 64.124"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ds2g-hy9f",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING EDUCATION CH30 B124 POST-VIETNAM ERA VETERANS\u2019 EDUCATIONAL ASSISTANCE APR2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/ds6c-w7wj",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Mark Guagliardo",
+                "hasEmail": "mailto:VANCVAS@va.gov"
+            },
+            "description": "Background information and charts concerning the cohort of veterans who served from the time of the Persian Gulf War (1990-1991) to September 11, 2001. The story also invites all veterans to avail themselves of all VA benefits for which they qualify.",
+            "identifier": "https://www.data.va.gov/api/views/ds6c-w7wj",
             "issued": "2020-10-20",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-05",
             "keyword": [
                 "cemetery",
                 "disability compensation",
@@ -36409,52 +36413,30 @@
                 "vocational rehabilitation",
                 "vocational rehabilitation services"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Mark Guagliardo",
-                "hasEmail": "mailto:VANCVAS@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/ds6c-w7wj",
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2021-01-05",
+            "programCode": [
+                "029:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/ds6c-w7wj",
-            "description": "Background information and charts concerning the cohort of veterans who served from the time of the Persian Gulf War (1990-1991) to September 11, 2001. The story also invites all veterans to avail themselves of all VA benefits for which they qualify.",
-            "title": "Pre 9/11 Gulf War Cohort",
-            "programCode": [
-                "029:000"
-            ],
-            "license": "https://www.usa.gov/government-works"
+            "title": "Pre 9/11 Gulf War Cohort"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/dsam-p4tf",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2023-04-18",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-19",
-            "keyword": [
-                "death rate",
-                "life expectancy",
-                "life table"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/dsam-p4tf",
             "description": "",
-            "title": "Table 7 - U. S. Veterans Life Table for Male 2010-2019",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36462,42 +36444,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/dsam-p4tf/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dsam-p4tf/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dsam-p4tf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/dsam-p4tf/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dsam-p4tf/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dsam-p4tf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/dsam-p4tf/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dsam-p4tf/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dsam-p4tf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/dsam-p4tf",
+            "issued": "2023-04-18",
+            "keyword": [
+                "death rate",
+                "life expectancy",
+                "life table"
+            ],
+            "landingPage": "https://www.data.va.gov/d/dsam-p4tf",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-04-19",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Table 7 - U. S. Veterans Life Table for Male 2010-2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "accrualPeriodicity": "R/P2M",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2015-03-01T05:00:00Z/2015-03-01T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/health/access-audit.asp"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/access-audit.asp",
+            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/1_March_2015_Public_Data_Pending_03192015.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Pending Appointments 1 March 2015"
+                }
             ],
+            "identifier": "VA-VHA-OIA-099",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -36511,71 +36523,43 @@
                 "wait list",
                 "wait time"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:041"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-OIA-099",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 Mar 1",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/1_March_2015_Public_Data_Pending_03192015.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Pending Appointments 1 March 2015"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2015-03-01T05:00:00Z/2015-03-01T05:00:00Z",
             "theme": [
                 "Accelerating Access",
                 "Pending Appointments"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 Mar 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/dt5a-n6f9",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 032"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/dt5a-n6f9",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION BENEFITS PROGRAM to encourage membership in units of the Selected Reserve of the Ready Reserve and to provide educational assistance to members of the reserve components called or ordered to active service in response to a war or national emergency declared by the President or Congress. Generally, to qualify for benefits under MGIB-SR you must (1) Have a six-year obligation to serve in the Selected Reserve signed after June 30, 1985. If you are an officer, you must have agreed to serve six years in addition to your original obligation. For some types of training, it is necessary to have a six-year commitment that begins after September 30, 1990; (2) Complete your initial active duty for training (IADT); (3) Meet the requirement to receive a high school diploma or equivalency certificate before completing IADT. You may not use 12 hours toward a college degree to meet this requirement; and (4) Remain in good standing while serving in an active Selected Reserve unit. Generally, to qualify for benefits under REAP you must have served at least 90 consecutive days on active duty as a result of a call or order to active duty from a reserve component in response to a war or national emergency declared by the President or Congress. This is not a complete list of eligibility requirements. For more information on MGIB-SR and REAP visit <a href=\"http://www.gibill.va.gov\">http://www.gibill.va.gov</a>.</p>",
-            "title": "USA SPENDING EDUCATION CH1606 & CH1607 B032 MONTGOMERY GI BILL SELECTED RESERVE; RESERVE EDUCATIONAL ASSISTANCE PROGRAM MAY2019",
-            "isPartOf": "b2a0a5f0-3d2f-490f-8b42-3eb1db21b8e0",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36583,62 +36567,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/dt5a-n6f9/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dt5a-n6f9/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dt5a-n6f9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/dt5a-n6f9/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dt5a-n6f9/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dt5a-n6f9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/dt5a-n6f9/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dt5a-n6f9/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dt5a-n6f9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/dt5a-n6f9",
+            "isPartOf": "b2a0a5f0-3d2f-490f-8b42-3eb1db21b8e0",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 032"
+            ],
+            "landingPage": "https://www.data.va.gov/d/dt5a-n6f9",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING EDUCATION CH1606 & CH1607 B032 MONTGOMERY GI BILL SELECTED RESERVE; RESERVE EDUCATIONAL ASSISTANCE PROGRAM MAY2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.ptsd.va.gov/repository",
+            "accrualPeriodicity": "Irregular",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "All data is within the public domain and is currently available for download.",
-            "issued": "2024-03-20",
-            "@type": "dcat:Dataset",
-            "modified": "2024-03-22",
-            "keyword": [
-                "meta-analysis",
-                "research methodology"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for PTSD",
                 "hasEmail": "mailto:ncptsd@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "National Center for PTSD"
-            },
-            "identifier": "https://www.data.va.gov/api/views/dtae-hx8d",
             "description": "Download this free, step-by-step guide for conducting meta-analyses focused on mental health research. Dr. Pim Cuijpers reviews each element of performing meta-analyses, including: defining research questions, searching bibliographical databases, selecting studies and retrieving data, determining risk of bias, calculating and pooling effect sizes, examining heterogeneity and potential publication bias, and writing and publishing meta-analyses.",
-            "title": "Meta-analyses in mental health research: A practical guide. Cuijpers (2016)",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36646,42 +36629,43 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "spatial": "International",
+            "identifier": "https://www.data.va.gov/api/views/dtae-hx8d",
+            "issued": "2024-03-20",
+            "keyword": [
+                "meta-analysis",
+                "research methodology"
+            ],
+            "landingPage": "https://www.ptsd.va.gov/repository",
             "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode",
-            "accrualPeriodicity": "Irregular",
+            "modified": "2024-03-22",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Center for PTSD"
+            },
+            "rights": "All data is within the public domain and is currently available for download.",
+            "spatial": "International",
             "theme": [
                 "PTSD Randomized Controlled Trials"
-            ]
+            ],
+            "title": "Meta-analyses in mental health research: A practical guide. Cuijpers (2016)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/dtcn-jc6n",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-02-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "minorities",
-                "statistics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS Mailbox",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-237",
+            "dataQuality": true,
             "description": "<p>This report is the first comprehensive report that chronicles the history of racial and ethnic minorities in the military and as Veterans, profiles characteristics of minority Veterans in 2014, illustrates how minority Veterans utilized some of the major benefits and services offered by the VA.</p>",
-            "title": "Minority Veteran Report 2014",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36690,57 +36674,49 @@
                     "title": "Minority Veteran Report 2014"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-237",
+            "issued": "2018-02-01",
+            "keyword": [
+                "minorities",
+                "statistics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/dtcn-jc6n",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Veteran Benefits",
                 "Veteran Utilization",
                 "Statistics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Minority Veteran Report 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/dtea-zjkr",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2007-10-01T04:00:00Z/2008-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf"
-            ],
-            "keyword": [
-                "health",
-                "healthcare",
-                "hospital accreditation",
-                "patient safety",
-                "quality of care",
-                "satisfaction",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VHA Open Data",
                 "hasEmail": "mailto:vhaopendata@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VHA-OIA-035",
-            "description": "<p>Report to the Appropriations Committee of the United States House of Representatives in Response to Conference Committee Report to PL 110-186.  In an effort to provide a snapshot of the quality of care provided at VA health care facilities, this report includes information about waiting times, staffing level, infection rates, surgical volumes, quality measures, patient satisfaction, service availability and complexity, accreditation status, and patient safety. The data in this report have been drawn from multiple sources across VHA.  This dataset contains the data about wait times to be seen in Primary and Specialty Care Services.</p>",
-            "title": "Veterans Health Administration 2008 Hospital Report Card - Waiting Times",
-            "isPartOf": "VA-VHA-OIA-583",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "029:040"
-            ],
+            "description": "<p>Report to the Appropriations Committee of the United States House of Representatives in Response to Conference Committee Report to PL 110-186.  In an effort to provide a snapshot of the quality of care provided at VA health care facilities, this report includes information about waiting times, staffing level, infection rates, surgical volumes, quality measures, patient satisfaction, service availability and complexity, accreditation status, and patient safety. The data in this report have been drawn from multiple sources across VHA.  This dataset contains the data about wait times to be seen in Primary and Specialty Care Services.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36748,51 +36724,87 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/dtea-zjkr/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dtea-zjkr/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dtea-zjkr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/dtea-zjkr/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dtea-zjkr/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dtea-zjkr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/dtea-zjkr/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dtea-zjkr/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dtea-zjkr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf",
-            "dataQuality": true,
+            "identifier": "VA-VHA-OIA-035",
+            "isPartOf": "VA-VHA-OIA-583",
+            "issued": "2017-07-26",
+            "keyword": [
+                "health",
+                "healthcare",
+                "hospital accreditation",
+                "patient safety",
+                "quality of care",
+                "satisfaction",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/dtea-zjkr",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:040"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf"
+            ],
+            "temporal": "2007-10-01T04:00:00Z/2008-09-30T04:00:00Z",
             "theme": [
                 "Section 3. Health and Nutrition"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veterans Health Administration 2008 Hospital Report Card - Waiting Times"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/dubs-jeiv",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2009-10-01T04:00:00Z/2010-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/health/HospitalReportCard.asp"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/HospitalReportCard.asp",
+            "description": "<p>Available services within each medical center.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/VETDATA/docs/Datagov/Data_Gov_VHA_2010_Dataset1_Infrastructure.xml",
+                    "mediaType": "application/xml",
+                    "title": "Infrastructure"
+                }
             ],
+            "identifier": "VA-VHA-OIA-040",
+            "isPartOf": "VA-VHA-OIA-584",
+            "issued": "2017-07-26",
             "keyword": [
                 "ambulatory",
                 "care",
@@ -36815,94 +36827,64 @@
                 "urban",
                 "veterans"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/dubs-jeiv",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:040"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-OIA-040",
-            "description": "<p>Available services within each medical center.</p>",
-            "title": "Veterans Health Administration 2010 Facility Quality and Safety Report - Infrastructure",
-            "isPartOf": "VA-VHA-OIA-584",
-            "programCode": [
-                "029:040"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/VETDATA/docs/Datagov/Data_Gov_VHA_2010_Dataset1_Infrastructure.xml",
-                    "mediaType": "application/xml",
-                    "title": "Infrastructure"
-                }
+            "references": [
+                "https://www.va.gov/health/HospitalReportCard.asp"
             ],
-            "describedBy": "https://www.va.gov/health/HospitalReportCard.asp",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2009-10-01T04:00:00Z/2010-09-30T04:00:00Z",
             "theme": [
                 "Section 3. Health and Nutrition"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veterans Health Administration 2010 Facility Quality and Safety Report - Infrastructure"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/dugp-fudf",
-            "issued": "2023-07-03",
             "@type": "dcat:Dataset",
-            "modified": "2024-06-07",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Maine FY2021",
+            "identifier": "https://www.data.va.gov/api/views/dugp-fudf",
+            "issued": "2023-07-03",
             "keyword": [
                 "fy2021 data",
                 "maine",
                 "ncvas state summary"
             ],
-            "identifier": "https://www.data.va.gov/api/views/dugp-fudf",
+            "landingPage": "https://www.data.va.gov/d/dugp-fudf",
+            "modified": "2024-06-07",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Maine FY2021",
             "title": "NCVAS State Summary Maine FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/dukd-ufj2",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2023-04-18",
-            "@type": "dcat:Dataset",
-            "modified": "2023-04-19",
-            "keyword": [
-                "death rate",
-                "life expectancy",
-                "life table"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/dukd-ufj2",
             "description": "",
-            "title": "Table 3 - U. S. Veterans Life Table for Male 1990-1999",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36910,81 +36892,82 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/dukd-ufj2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dukd-ufj2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dukd-ufj2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/dukd-ufj2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dukd-ufj2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dukd-ufj2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/dukd-ufj2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dukd-ufj2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dukd-ufj2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/dukd-ufj2",
+            "issued": "2023-04-18",
+            "keyword": [
+                "death rate",
+                "life expectancy",
+                "life table"
+            ],
+            "landingPage": "https://www.data.va.gov/d/dukd-ufj2",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-04-19",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Table 3 - U. S. Veterans Life Table for Male 1990-1999"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/dv22-m54f",
-            "issued": "2023-06-19",
             "@type": "dcat:Dataset",
-            "modified": "2024-05-23",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Florida FY2021",
+            "identifier": "https://www.data.va.gov/api/views/dv22-m54f",
+            "issued": "2023-06-19",
             "keyword": [
                 "florida",
                 "fy2021 data",
                 "ncvas state summary"
             ],
-            "identifier": "https://www.data.va.gov/api/views/dv22-m54f",
+            "landingPage": "https://www.data.va.gov/d/dv22-m54f",
+            "modified": "2024-05-23",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Florida FY2021",
             "title": "NCVAS State Summary Florida FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/dwpj-hgp7",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2019-09-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-08-24",
-            "keyword": [
-                "opioid",
-                "prescribing"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VA OIT Open Data",
                 "hasEmail": "mailto:OITOPENDATA@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veteran Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/dwpj-hgp7",
             "description": "Dataset showing Opioid Prescribing Rates, by VA facility, between 2012 and 2018",
-            "title": "Opioid Prescribing Rates at VA Facilities 2012 - 2018",
-            "programCode": [
-                "029:040"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -36992,42 +36975,71 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/dwpj-hgp7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dwpj-hgp7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dwpj-hgp7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/dwpj-hgp7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dwpj-hgp7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dwpj-hgp7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/dwpj-hgp7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/dwpj-hgp7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/dwpj-hgp7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/dwpj-hgp7",
+            "issued": "2019-09-17",
+            "keyword": [
+                "opioid",
+                "prescribing"
+            ],
+            "landingPage": "https://www.data.va.gov/d/dwpj-hgp7",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-08-24",
+            "programCode": [
+                "029:040"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veteran Affairs"
+            },
+            "title": "Opioid Prescribing Rates at VA Facilities 2012 - 2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "accrualPeriodicity": "R/P2M",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2015-12-01T05:00:00Z/2015-12-01T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/health/access-audit.asp"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/access-audit.asp",
+            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR35_122015_Pending_and_EWL_Biweekly_Desired_Date_Division.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Pending Appointments 1 December 2015"
+                }
             ],
+            "identifier": "VA-VHA-OIA-430",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -37041,54 +37053,45 @@
                 "wait list",
                 "wait time"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:041"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-OIA-430",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 December 1",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR35_122015_Pending_and_EWL_Biweekly_Desired_Date_Division.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Pending Appointments 1 December 2015"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2015-12-01T05:00:00Z/2015-12-01T05:00:00Z",
             "theme": [
                 "Accelerating Access",
                 "Pending Appointments"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 December 1"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/dxnj-e7hw",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The Health Services Training Report (HST) Database tracks the overall number of Personnel and Accounting Integrated Data Systems (PAID) and Without Compensation (WOC) Trainee positions by the cooperating academic institutions for all medical center approved health services programs. Information in the database comes from all Veterans Affairs Medical Centers (VAMCs) who have Office of Academic Affiliations (OAA) approved HST programs. Worksheets and memos are distributed to participating VAMCs by the OAA annually. VAMC personnel enter the information electronically into the database located at the OAA Support Center (OAASC) in St. Louis, Missouri. The main user of this database is the OAA.</p>",
+            "identifier": "VA-VHA-OAA-001",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1997-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "academic",
                 "affiliations",
@@ -37099,66 +37102,43 @@
                 "without compensation",
                 "woc"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/dxnj-e7hw",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:041"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-OAA-001",
-            "description": "<p>The Health Services Training Report (HST) Database tracks the overall number of Personnel and Accounting Integrated Data Systems (PAID) and Without Compensation (WOC) Trainee positions by the cooperating academic institutions for all medical center approved health services programs. Information in the database comes from all Veterans Affairs Medical Centers (VAMCs) who have Office of Academic Affiliations (OAA) approved HST programs. Worksheets and memos are distributed to participating VAMCs by the OAA annually. VAMC personnel enter the information electronically into the database located at the OAA Support Center (OAASC) in St. Louis, Missouri. The main user of this database is the OAA.</p>",
-            "title": "Health Services Training Report (HST) Database",
-            "programCode": [
-                "029:041"
-            ],
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "1997-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Health Services Training Report (HST) Database"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-02",
-            "keyword": [
-                "abr",
-                "abr2012",
-                "lgy",
-                "loan guarantee benefits fy12",
-                "vba benefits"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Elwell",
                 "hasEmail": "mailto:thomas.elwell@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-ABR2012-046",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Number of Loans Guaranteed by Age by Fiscal Year",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37166,43 +37146,47 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-046",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "abr",
+                "abr2012",
+                "lgy",
+                "loan guarantee benefits fy12",
+                "vba benefits"
+            ],
+            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2022-03-02",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "ABR Reports"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Number of Loans Guaranteed by Age by Fiscal Year"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/dzc4-j2cj",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "debt referrals"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vicki Soukup",
                 "hasEmail": "mailto:vicki.soukup@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-163",
             "description": "<p>Debt referrals to credit reporting agencies and the treasury offset program. Monthly Top Totals 9/30/15</p>",
-            "title": "COIN 146 - Monthly Top Totals - 09/20/2015",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37210,40 +37194,38 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-163",
+            "issued": "2017-07-26",
+            "keyword": [
+                "debt referrals"
+            ],
+            "landingPage": "https://www.data.va.gov/d/dzc4-j2cj",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "financial"
-            ]
+            ],
+            "title": "COIN 146 - Monthly Top Totals - 09/20/2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.techstrategies.oit.va.gov/docs/CTSNotes/TS%20Note%20Vol%202%20Issue%2010%20Final.pdf",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "data",
-                "hybrid",
-                "infrastructure"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Mark Peterson",
                 "hasEmail": "mailto:mark.peterson3@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OIT-ASD-TSNV2-010",
             "description": "<p>VA Executive's Guide to Hybrid Data Infrastructure</p>",
-            "title": "TS Note Vol 2 Issue 10",
-            "programCode": [
-                "029:078"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37252,41 +37234,43 @@
                     "title": "TS Note Vol 2 Issue 10"
                 }
             ],
+            "identifier": "VA-OIT-ASD-TSNV2-010",
+            "issued": "2017-07-26",
+            "keyword": [
+                "data",
+                "hybrid",
+                "infrastructure"
+            ],
+            "landingPage": "https://www.techstrategies.oit.va.gov/docs/CTSNotes/TS%20Note%20Vol%202%20Issue%2010%20Final.pdf",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:078"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "TS Note Vol 2 Issue 10"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/e2e4-bybg",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-21",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 116"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/e2e4-bybg",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION PROGRAMS to provide, through purchase and/or fabrication, prosthetic and related appliances, equipment and services to eligible veterans so that they may live and work as productive citizens. Veterans eligible for prosthetic services are service-connected veterans seeking care for a service-connected disability; veterans with compensable service-connected disabilities generally rated 10 percent or more; former prisoners of war, veterans discharged or released from active military service for a disability that was incurred or aggravated in the line of duty, and veterans who are in receipt of Section 1151 benefits; veterans who are in receipt of increased pension based on a need of regular aid and attendance or by reason of being permanently housebound; veterans who have annual income and net worth below the \"means test\" threshold; all other veterans who are not required to pay a copayment for their care, i.e., veterans of the Mexican border period and World War I, compensated zero (0) percent service-connected veterans who are receiving statutory awards, veterans exposed to a toxic substance, radiation or environmental hazard (limited to certain disabilities); and veterans who must pay a copayment for their care. Ineligible veterans are nonservice-connected veterans residing or sojourning in foreign lands.</p>",
-            "title": "USA SPENDING EDUCATION CH31 B116 VETERANS PROSTHETIC APPLIANCES MAR2019",
-            "isPartOf": "5760c6c5-d531-4dc3-9e99-4418034dbb16",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37294,54 +37278,57 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/e2e4-bybg/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/e2e4-bybg/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/e2e4-bybg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/e2e4-bybg/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/e2e4-bybg/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/e2e4-bybg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/e2e4-bybg/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/e2e4-bybg/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/e2e4-bybg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/e2e4-bybg",
+            "isPartOf": "5760c6c5-d531-4dc3-9e99-4418034dbb16",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 116"
+            ],
+            "landingPage": "https://www.data.va.gov/d/e2e4-bybg",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "USA SPENDING EDUCATION CH31 B116 VETERANS PROSTHETIC APPLIANCES MAR2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/e2yy-nw8i",
-            "issued": "2024-04-19",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-02",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Florinda Balfour",
                 "hasEmail": "mailto:VACONCVAS@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/e2yy-nw8i",
             "description": "",
-            "title": "vetpop_pos",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37349,118 +37336,114 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/e2yy-nw8i/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/e2yy-nw8i/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/e2yy-nw8i/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/e2yy-nw8i/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/e2yy-nw8i/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/e2yy-nw8i/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/e2yy-nw8i/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/e2yy-nw8i/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/e2yy-nw8i/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/e2yy-nw8i",
+            "issued": "2024-04-19",
+            "landingPage": "https://www.data.va.gov/d/e2yy-nw8i",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-05-02",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "vetpop_pos"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/e3g6-pgxi",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Montana FY2023",
+            "identifier": "https://www.data.va.gov/api/views/e3g6-pgxi",
             "issued": "2024-06-12",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-12",
             "keyword": [
                 "fy2023",
                 "montana",
                 "ncvas state summary"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/e3g6-pgxi",
+            "modified": "2024-07-12",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/e3g6-pgxi",
-            "description": "NCVAS State Summary Montana FY2023",
-            "title": "NCVAS State Summary Montana FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Montana FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/e44m-e7w9",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Florinda Balfour",
+                "hasEmail": "mailto:VACONCVAS@VA.GOV"
+            },
+            "description": "NCVAS State Summary Rhode Island FY2023",
+            "identifier": "https://www.data.va.gov/api/views/e44m-e7w9",
             "issued": "2024-06-18",
-            "@type": "dcat:Dataset",
-            "modified": "2024-07-12",
             "keyword": [
                 "fy2023",
                 "ncvas state summary",
                 "rhode island"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Florinda Balfour",
-                "hasEmail": "mailto:VACONCVAS@VA.GOV"
-            },
+            "landingPage": "https://www.data.va.gov/d/e44m-e7w9",
+            "modified": "2024-07-12",
+            "programCode": [
+                "029:086"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/e44m-e7w9",
-            "description": "NCVAS State Summary Rhode Island FY2023",
-            "title": "NCVAS State Summary Rhode Island FY2023",
-            "programCode": [
-                "029:086"
-            ]
+            "title": "NCVAS State Summary Rhode Island FY2023"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/e58w-9aq7",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2021-02-19",
-            "@type": "dcat:Dataset",
-            "modified": "2021-02-21",
-            "keyword": [
-                "race/ethnicity",
-                "transition",
-                "veteran"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tamara Lee",
                 "hasEmail": "mailto:vaconcvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/e58w-9aq7",
+            "dataQuality": true,
             "description": "Race/ethnicity of 4.4 million Servicemembers who transitioned to Veteran Status from FY 2005 to 2020.",
-            "title": "Race/Ethnicity of Transitioned Servicemembers",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37468,57 +37451,58 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/e58w-9aq7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/e58w-9aq7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/e58w-9aq7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/e58w-9aq7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/e58w-9aq7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/e58w-9aq7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/e58w-9aq7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/e58w-9aq7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/e58w-9aq7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
+            "identifier": "https://www.data.va.gov/api/views/e58w-9aq7",
+            "issued": "2021-02-19",
+            "keyword": [
+                "race/ethnicity",
+                "transition",
+                "veteran"
+            ],
+            "landingPage": "https://www.data.va.gov/d/e58w-9aq7",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2021-02-21",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Race/Ethnicity of Transitioned Servicemembers"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/e6h6-ps6e",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "kansas"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:tom.garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-186",
             "description": "<p>This summary describes the programs and services VA provided in Kansas in fiscal year 2015.</p>",
-            "title": "State Summary: Kansas",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37527,46 +37511,41 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-OEI-OEI-186",
+            "issued": "2017-07-26",
+            "keyword": [
+                "kansas"
+            ],
+            "landingPage": "https://www.data.va.gov/d/e6h6-ps6e",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "State Summary: Kansas"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/e6h8-8ke4",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "budget",
-                "compensation",
-                "facilities",
-                "pension",
-                "utilization",
-                "veteran population"
-            ],
             "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Florinda Balfour",
                 "hasEmail": "mailto:florinda.balfour@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-066",
             "description": "<p>National Center for Veterans Analysis and Statistics Pocket Cards archives are a compilation of facts related to the count of Veterans receiving Department of Veterans Affairs benefits and healthcare utilization.</p>",
-            "title": "National Center for Veterans Analysis and Statistics At-A-Glance Pocket Cards",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37575,39 +37554,43 @@
                     "title": "National Center for Veterans Analysis and Statistics At-A-Glance Pocket Cards"
                 }
             ],
+            "identifier": "VA-OEI-OEI-066",
+            "issued": "2017-07-26",
+            "keyword": [
+                "budget",
+                "compensation",
+                "facilities",
+                "pension",
+                "utilization",
+                "veteran population"
+            ],
+            "landingPage": "https://www.data.va.gov/d/e6h8-8ke4",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Demographics"
-            ]
+            ],
+            "title": "National Center for Veterans Analysis and Statistics At-A-Glance Pocket Cards"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/e6r5-gecx",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "coin",
-                "finance"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vicki Soukup",
                 "hasEmail": "mailto:vicki.soukup@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "OM-OM-170",
             "description": "<p>COIN Report 145 March 2016</p>",
-            "title": "COIN 145 March 2016",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37615,43 +37598,43 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "OM-OM-170",
+            "issued": "2017-07-26",
+            "keyword": [
+                "coin",
+                "finance"
+            ],
+            "landingPage": "https://www.data.va.gov/d/e6r5-gecx",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "COIN 145 March 2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.green.va.gov/fleet/",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-10-01T04:00:00Z/2013-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-10",
-            "keyword": [
-                "budget",
-                "fleet",
-                "fy 2013"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VA OM Open Data",
                 "hasEmail": "mailto:VAOMOpenData@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-046",
+            "dataQuality": true,
             "description": "<p>FY 2013 Fleet Management Plan and Budget Narrative</p>",
-            "title": "FY 2013 Fleet Management Plan and Budget Narrative",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37659,51 +37642,81 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-046",
+            "issued": "2017-07-26",
+            "keyword": [
+                "budget",
+                "fleet",
+                "fy 2013"
+            ],
+            "landingPage": "https://www.green.va.gov/fleet/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-06-10",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2012-10-01T04:00:00Z/2013-09-30T04:00:00Z",
             "theme": [
                 "Fleet",
                 "Budget"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 2013 Fleet Management Plan and Budget Narrative"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/e7xj-djda",
-            "issued": "2023-06-29",
             "@type": "dcat:Dataset",
-            "modified": "2024-04-23",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "State Summaries Review Team",
                 "hasEmail": "mailto:no-reply@www.data.va.gov"
             },
+            "description": "NCVAS State Summary Kentucky FY2021",
+            "identifier": "https://www.data.va.gov/api/views/e7xj-djda",
+            "issued": "2023-06-29",
             "keyword": [
                 "fy2021 data",
                 "kentucky",
                 "ncvas state summary"
             ],
-            "identifier": "https://www.data.va.gov/api/views/e7xj-djda",
+            "landingPage": "https://www.data.va.gov/d/e7xj-djda",
+            "modified": "2024-04-23",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "NCVAS State Summary Kentucky FY2021",
             "title": "NCVAS State Summary Kentucky FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/e85x-qxkv",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Sail Operations",
+                "hasEmail": "mailto:VHASailOperations@va.gov"
+            },
+            "dataQuality": true,
+            "description": "Strategic Analytics for Improvement and Learning Value Model or SAIL, is a system for summarizing hospital system performance within Veterans Health Administration (VHA). SAIL assesses key Quality measures in areas such as death rate, complications, and patient satisfaction, as well as overall efficiency at individual VA Medical Centers (VAMCs).  These .ZIP files are no longer supported and are in an 'as-is' state.  They were accurate at time of publication.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/e85x-qxkv/application/zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "identifier": "https://www.data.va.gov/api/views/e85x-qxkv",
+            "isPartOf": "VA-VHA-OIA-122",
             "issued": "2020-08-18",
-            "@type": "dcat:Dataset",
-            "temporal": "2015-10-01/2016-09-30",
-            "modified": "2021-06-24",
             "keyword": [
                 "2016",
                 "analytics",
@@ -37724,146 +37737,117 @@
                 "veterans health administration",
                 "vha"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Sail Operations",
-                "hasEmail": "mailto:VHASailOperations@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/e85x-qxkv",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-06-24",
+            "programCode": [
+                "029:040"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/e85x-qxkv",
-            "description": "Strategic Analytics for Improvement and Learning Value Model or SAIL, is a system for summarizing hospital system performance within Veterans Health Administration (VHA). SAIL assesses key Quality measures in areas such as death rate, complications, and patient satisfaction, as well as overall efficiency at individual VA Medical Centers (VAMCs).  These .ZIP files are no longer supported and are in an 'as-is' state.  They were accurate at time of publication.",
-            "title": "SAIL FY2016 Hospital Performance - All Facilities",
-            "isPartOf": "VA-VHA-OIA-122",
-            "programCode": [
-                "029:040"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/e85x-qxkv/application/zip",
-                    "mediaType": "application/zip"
-                }
-            ],
             "spatial": "United States, Puerto Rico",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "temporal": "2015-10-01/2016-09-30",
             "theme": [
                 "Hospital Quality Measurement"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "SAIL FY2016 Hospital Performance - All Facilities"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/e8ki-zx5h",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-21",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
-            "keyword": [
-                "cfda 64 117"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "f9dff532-b60f-484c-aa3a-38716834d803",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION PROGRAM BENEFITS to provide educational opportunities to the dependents of certain disabled and deceased veterans. Spouses, surviving spouses, and children (including stepchild or adopted child) between age 18 and 26 of veterans who died from service-connected disabilities, of living veterans whose service-connected disabilities are considered permanently and totally disabling, of those who died from any cause while such service-connected disabilities were in existence, of servicepersons who have been listed for a total of more than 90 days as currently missing in action, or as currently prisoners of war, a service member who VA determines has a service connected permanent and total disability and at the time of VA\u2019s determination is a member of the Armed Forces who is hospitalized or receiving outpatient medical care, services, or treatment; and is likely to be discharged or released from service for this service-connected disability. Children under the age of 18 may be eligible under special circumstances.</p>",
-            "title": "USA SPENDING EDUCATION CH35 B117 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE FY2019",
+            "identifier": "f9dff532-b60f-484c-aa3a-38716834d803",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 117"
+            ],
+            "landingPage": "https://www.data.va.gov/d/e8ki-zx5h",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
             "programCode": [
                 "029:003"
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING EDUCATION CH35 B117 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE FY2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://benefits.va.gov/benefits/media-publications.asp",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Thomas Elwell",
+                "hasEmail": "mailto:thomas.elwell@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>Post 9/11 GI Bill- General Information</p>",
+            "identifier": "VA-VBA-MEDIAPUB-021",
+            "isPartOf": "VA-VBA-MASTER-MEDIAPUBLICATIONS-001",
             "issued": "2017-07-26",
-            "temporal": "2012-09-01T04:00:00Z/2012-09-01T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-08",
             "keyword": [
                 "benefits fact sheet",
                 "general benefit information",
                 "va benefits",
                 "va fact sheet"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Thomas Elwell",
-                "hasEmail": "mailto:thomas.elwell@va.gov"
-            },
+            "landingPage": "https://benefits.va.gov/benefits/media-publications.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-03-08",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-MEDIAPUB-021",
-            "description": "<p>Post 9/11 GI Bill- General Information</p>",
-            "title": "Post 9/11 GI Bill- General Information",
-            "isPartOf": "VA-VBA-MASTER-MEDIAPUBLICATIONS-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2012-09-01T04:00:00Z/2012-09-01T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Post 9/11 GI Bill- General Information"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/finance/overpaymentsReport.asp",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-04-01T04:00:00Z/2014-06-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "improper payments",
-                "overpayments"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Katherine Palmer",
                 "hasEmail": "mailto:Katherine.Palmer@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-080",
+            "dataQuality": true,
             "description": "<p>FY 2014 Third Quarter High-Dollar Overpayments Report</p>",
-            "title": "FY 2014 Third Quarter High-Dollar Overpayments Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37872,43 +37856,43 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-080",
+            "issued": "2017-07-26",
+            "keyword": [
+                "improper payments",
+                "overpayments"
+            ],
+            "landingPage": "https://www.va.gov/finance/overpaymentsReport.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2014-04-01T04:00:00Z/2014-06-30T04:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 2014 Third Quarter High-Dollar Overpayments Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/e9mv-fahs",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "vermont"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DG&amp;A Mailgroup",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-217",
             "description": "<p>This summary describes the programs and services VA provided in  Vermont in fiscal year 2015.</p>",
-            "title": "State Summary: Vermont FY15",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37917,41 +37901,41 @@
                     "title": "Vermont"
                 }
             ],
+            "identifier": "VA-OEI-OEI-217",
+            "issued": "2017-07-26",
+            "keyword": [
+                "vermont"
+            ],
+            "landingPage": "https://www.data.va.gov/d/e9mv-fahs",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "State Summary: Vermont FY15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/e9vp-w8ah",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-11-09",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "60aec5e3-faf5-4ba5-99fa-90f4c26655f2",
+            "dataQuality": true,
             "description": "<p>The FY2016 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Indiana FY2016",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -37959,39 +37943,37 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "60aec5e3-faf5-4ba5-99fa-90f4c26655f2",
+            "issued": "2017-11-09",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/e9vp-w8ah",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2020-11-12",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summary Indiana FY2016"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/Surveys.asp",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2007-04-23T04:00:00Z/2007-08-22T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "employment",
-                "survey",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:tom.garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-49",
+            "dataQuality": true,
             "description": "<p>The Employment Histories Report is a study to better understand the employment histories and outcomes of recently separated servicemembers.</p>",
-            "title": "Employment Histories Report",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38000,43 +37982,45 @@
                     "title": "pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-49",
+            "issued": "2017-07-26",
+            "keyword": [
+                "employment",
+                "survey",
+                "veterans"
+            ],
+            "landingPage": "https://www.va.gov/vetdata/Surveys.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2007-04-23T04:00:00Z/2007-08-22T04:00:00Z",
             "theme": [
                 "Employment Data on Veterans"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Employment Histories Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ea4r-apb9",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2015-06-01T04:00:00Z/2015-06-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-21",
-            "keyword": [
-                "debt referrals"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vikki Soukup",
                 "hasEmail": "mailto:Vikki.Soukup@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-144",
+            "dataQuality": true,
             "description": "<p>Debt referrals to credit reporting agencies and the treasury offset program.</p>",
-            "title": "June 2015 Coin 145",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38044,43 +38028,42 @@
                     "mediaType": "text/plain"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-144",
+            "issued": "2017-07-26",
+            "keyword": [
+                "debt referrals"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ea4r-apb9",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-21",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2015-06-01T04:00:00Z/2015-06-30T04:00:00Z",
             "theme": [
                 "financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "June 2015 Coin 145"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ebfc-rjyn",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2015-04-01T04:00:00Z/2015-04-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "debt referrals"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vikki Soukup",
                 "hasEmail": "mailto:Vikki.Soukup@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-132",
             "description": "<p>Debt referrals to credit reporting agencies and the treasury offset program.</p>",
-            "title": "COIN 0145 MONTHLY CRS TOTALS REPORT APR 2015",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38088,42 +38071,42 @@
                     "mediaType": "text/plain"
                 }
             ],
+            "identifier": "VA-OM-OM-132",
+            "issued": "2017-07-26",
+            "keyword": [
+                "debt referrals"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ebfc-rjyn",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2015-04-01T04:00:00Z/2015-04-30T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "COIN 0145 MONTHLY CRS TOTALS REPORT APR 2015"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.data.va.gov/d/ebk7-yc7m",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2018-02-23",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "jalfhcc",
-                "patient"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "John Short",
                 "hasEmail": "mailto:vhaopendata@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "ab2c26e7-c5cf-46f0-a0ee-f05c6f8cb89f",
+            "dataQuality": true,
             "description": "<p>The Captain James A. Lovell Federal Health Care Center (JALFHCC) Patient Registration Service supports the operation of the first VA/Navy Federal Health Care Center and involves leveraging of the Veterans Health Information Systems and Technology Architecture (VistA) for VA and the Department of Defenses (DoDs) Health Information System.The integration of JALFHCC and eMI was accomplished in multiple phases. JALFHCC Phase 1 consisted of the integration of the Orders Portability service with eMI to allow for VA and DoD communications for Orders Portability through eMI. JALFHCC Phase 1 went live in production in May 2015 and supported an average of 10,000 messages per day. JALFHCC Phase 2 and 3 involved the integration of five additional services or message flows with eMI and the full sunset of the Vitria Businessware Service, JALFHCC Oracle Service Bus (OSB), and Oracle Service Registry (OSR) at VA JALFHCC. JALFHCC Phase 2 and 3 went live in August 2015.</p>",
-            "title": "JALFHCC - Patient Registration Service",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38132,39 +38115,37 @@
                     "title": "JALFHCC - Patient Registration Service"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "ab2c26e7-c5cf-46f0-a0ee-f05c6f8cb89f",
+            "issued": "2018-02-23",
+            "keyword": [
+                "jalfhcc",
+                "patient"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ebk7-yc7m",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
+            "title": "JALFHCC - Patient Registration Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ebuf-mu9w",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "civil war",
-                "historic burials",
-                "historic cemeteries",
-                "national register"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James Killens III",
                 "hasEmail": "mailto:james.killensiii@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-NCA-MPS-004",
             "description": "<p>This document provides information on the oldest National Cemeteries which are on the National Register of Historic Places</p>",
-            "title": "NCA National Cemeteries and Soldiers Lots on the National Register of Historic Places",
-            "programCode": [
-                "029:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38173,46 +38154,43 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-NCA-MPS-004",
+            "issued": "2017-07-26",
+            "keyword": [
+                "civil war",
+                "historic burials",
+                "historic cemeteries",
+                "national register"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ebuf-mu9w",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "NCA National Cemeteries and Soldiers Lots on the National Register of Historic Places"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ebun-952t",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2022-03-17",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-05",
-            "keyword": [
-                "utilization",
-                "va benefits",
-                "va programs",
-                "va services",
-                "veteran benefits",
-                "veterans",
-                "veterans benefits"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:VANCVAS@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/ebun-952t",
             "description": "Percent Users vs Non-Users Distribution by Age Group - Males. Data underlying the second figure of Part 2 of the FY2021 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Percentage Age Distribution of Male Users and Non-Users, FY 2021",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38220,58 +38198,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ebun-952t/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ebun-952t/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ebun-952t/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ebun-952t/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ebun-952t/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ebun-952t/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ebun-952t/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ebun-952t/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ebun-952t/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/ebun-952t",
+            "issued": "2022-03-17",
+            "keyword": [
+                "utilization",
+                "va benefits",
+                "va programs",
+                "va services",
+                "veteran benefits",
+                "veterans",
+                "veterans benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ebun-952t",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-01-05",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Percentage Age Distribution of Male Users and Non-Users, FY 2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.green.va.gov/fleet/",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-01-01T05:00:00Z/2011-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-07",
-            "keyword": [
-                "fleet management plan",
-                "vehicle allocation methodology"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VA OM Open Data",
                 "hasEmail": "mailto:VAOMOpenData@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-047",
+            "dataQuality": true,
             "description": "<p>VA 2011 Vehicle Allocation Methodology (VAM) Fleet Management Plan</p>",
-            "title": "VA 2011 Vehicle Allocation Methodology (VAM) Fleet Management Plan",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38279,44 +38263,43 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-047",
+            "issued": "2017-07-26",
+            "keyword": [
+                "fleet management plan",
+                "vehicle allocation methodology"
+            ],
+            "landingPage": "https://www.green.va.gov/fleet/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-06-07",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-01-01T05:00:00Z/2011-12-31T05:00:00Z",
             "theme": [
                 "Fleet"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA 2011 Vehicle Allocation Methodology (VAM) Fleet Management Plan"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/ecf6-zj3f",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2024-07-31",
-            "@type": "dcat:Dataset",
-            "modified": "2024-12-10",
-            "keyword": [
-                "veterans",
-                "women veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS",
                 "hasEmail": "mailto:vaconcvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/ecf6-zj3f",
             "description": "",
-            "title": "Employment Status of Men Veterans by Age",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38324,58 +38307,58 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ecf6-zj3f/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ecf6-zj3f/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ecf6-zj3f/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ecf6-zj3f/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ecf6-zj3f/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ecf6-zj3f/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ecf6-zj3f/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ecf6-zj3f/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ecf6-zj3f/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/ecf6-zj3f",
+            "issued": "2024-07-31",
+            "keyword": [
+                "veterans",
+                "women veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ecf6-zj3f",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-12-10",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Employment Status of Men Veterans by Age"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/finance/overpaymentsReport.asp",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2015-10-01T04:00:00Z/2015-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "improper payments",
-                "overpayments"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vikki Soukup",
                 "hasEmail": "mailto:Vikki.Soukup@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-146",
+            "dataQuality": true,
             "description": "<p>FY 2015 First Quarter High-Dollar Overpayments Report</p>",
-            "title": "FY 2015 First Quarter High-Dollar Overpayments Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38384,25 +38367,56 @@
                     "title": "FY 2015 First Quarter High-Dollar Overpayments Report"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-146",
+            "issued": "2017-07-26",
+            "keyword": [
+                "improper payments",
+                "overpayments"
+            ],
+            "landingPage": "https://www.va.gov/finance/overpaymentsReport.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2015-10-01T04:00:00Z/2015-12-31T05:00:00Z",
             "theme": [
                 "financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 2015 First Quarter High-Dollar Overpayments Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ecq5-ttv5",
             "bureauCode": [
                 "029:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://raw.githubusercontent.com/vacobrydsk/VeteransCrisisLineDataDictionary/master/VeteransCrisisLineDataDictionary.xlsx",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "description": "<p>Record-level data released on Freedom of Information Act (FOIA) Request 15-00242-F appeal.  Fields with value of b6 indicate data withheld in accordance with VHA Expert Determination methodology and/or VA Office of General Counsel direction.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/ecq5-ttv5/application/zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "identifier": "VA-VHA-10N-008",
+            "isPartOf": "VA-VHA-10N-013",
             "issued": "2017-07-26",
-            "temporal": "2013-10-01T04:00:00Z/2014-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
             "keyword": [
                 "crisis",
                 "foia",
@@ -38415,54 +38429,52 @@
                 "veteran",
                 "vha"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/ecq5-ttv5",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-12",
+            "programCode": [
+                "029:042"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-10N-008",
-            "description": "<p>Record-level data released on Freedom of Information Act (FOIA) Request 15-00242-F appeal.  Fields with value of b6 indicate data withheld in accordance with VHA Expert Determination methodology and/or VA Office of General Counsel direction.</p>",
-            "title": "Veterans Crisis Line calls FY2014 Record-Level Data",
-            "isPartOf": "VA-VHA-10N-013",
-            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
-            "programCode": [
-                "029:042"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/ecq5-ttv5/application/zip",
-                    "mediaType": "application/zip"
-                }
-            ],
-            "describedBy": "https://raw.githubusercontent.com/vacobrydsk/VeteransCrisisLineDataDictionary/master/VeteransCrisisLineDataDictionary.xlsx",
             "systemOfRecords": "https://www.federalregister.gov/articles/2015/04/24/2015-09567/privacy-act-of-1974-system-of-records",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "temporal": "2013-10-01T04:00:00Z/2014-09-30T04:00:00Z",
             "theme": [
                 "Suicide Prevention"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veterans Crisis Line calls FY2014 Record-Level Data"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-06-09T04:00:00Z/2014-06-09T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/health/access-audit.asp"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/access-audit.asp",
+            "description": "<p>On Wednesday, May 21, 2014, VA launched the Accelerating Access to Care Initiative, a nation-wide program to ensure timely access to care. As directed by President Obama, VHA has identified Veterans across the system experiencing waits that do not meet Veterans expectations for timeliness. VA has begun contacting and scheduling all Veterans who are waiting for care in VA clinics or arranging for care in the community, while simultaneously addressing the underlying issues that impede Veterans\u2019 access.The nationwide Access Audit covered a total of 731 separate points of access, and involved over 3,772 interviews of clinical and administrative staff involved in the scheduling process at VA Medical Centers (VAMC), large Community Based Outpatient Clinics (CBOC) serving at least 10,000 Veterans and a sampling of smaller clinics. A complete list of VISN facilities with components reviewed as part of the Access Audit is included in this package</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/health/docs/VISN8FACTSHEET140609.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "VISN 8 Fact Sheet"
+                }
             ],
+            "identifier": "VA-VHA-OIA-082",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -38478,53 +38490,46 @@
                 "wait list",
                 "wait time"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:041"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-OIA-082",
-            "description": "<p>On Wednesday, May 21, 2014, VA launched the Accelerating Access to Care Initiative, a nation-wide program to ensure timely access to care. As directed by President Obama, VHA has identified Veterans across the system experiencing waits that do not meet Veterans expectations for timeliness. VA has begun contacting and scheduling all Veterans who are waiting for care in VA clinics or arranging for care in the community, while simultaneously addressing the underlying issues that impede Veterans\u2019 access.The nationwide Access Audit covered a total of 731 separate points of access, and involved over 3,772 interviews of clinical and administrative staff involved in the scheduling process at VA Medical Centers (VAMC), large Community Based Outpatient Clinics (CBOC) serving at least 10,000 Veterans and a sampling of smaller clinics. A complete list of VISN facilities with components reviewed as part of the Access Audit is included in this package</p>",
-            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 8",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/health/docs/VISN8FACTSHEET140609.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "VISN 8 Fact Sheet"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2014-06-09T04:00:00Z/2014-06-09T04:00:00Z",
             "theme": [
                 "Accelerating Access",
                 "Audit"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "VA Access Audit & Wait Times Fact Sheet: VISN 8"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "http://www.nvsbe.com/why-attend/about-nvsbe/",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:40"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Armando Herrera",
+                "hasEmail": "mailto:Armando.Herrera@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>National Veterans Small Business Engagement website - about NVSBE webpage</p>",
+            "identifier": "VA-00SB-NVSBE0005",
             "issued": "2017-07-26",
-            "temporal": "2014-06-11T04:00:00Z/2015-04-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "about nvsbe",
                 "conference",
@@ -38536,61 +38541,39 @@
                 "veterans affairs",
                 "vets"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Armando Herrera",
-                "hasEmail": "mailto:Armando.Herrera@va.gov"
-            },
+            "landingPage": "http://www.nvsbe.com/why-attend/about-nvsbe/",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:081"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-00SB-NVSBE0005",
-            "description": "<p>National Veterans Small Business Engagement website - about NVSBE webpage</p>",
-            "title": "NVSBE Website - About NVSBE",
-            "programCode": [
-                "029:081"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2014-06-11T04:00:00Z/2015-04-30T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "NVSBE Website - About NVSBE"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "annual report",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:Tom.Garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-146",
             "description": "<p>This reports the activities of the Veterans Administration for the fiscal year ending September 30, 1983.</p>",
-            "title": "Annual Report:  1983",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38599,42 +38582,43 @@
                     "title": "Annual Report: 1983"
                 }
             ],
+            "identifier": "VA-OEI-OEI-146",
+            "issued": "2017-07-26",
+            "keyword": [
+                "annual report",
+                "veterans"
+            ],
+            "landingPage": "https://www.va.gov/vetdata/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Demographics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Annual Report:  1983"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/eex4-q387",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-21",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 028"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/eex4-q387",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION BENEFITS PROGRAM to help servicepersons adjust to civilian life after separation from military service, assist in the recruitment and retention of highly qualified personnel in the active and reserve components in the Armed Forces by providing education benefits, and to provide educational opportunities to the dependents of certain service members and veterans. Individuals who entered active duty after September 10, 2001 may be eligible for the Post-9/11 GI Bill. Individuals can use the Post-9/11 GI Bill after serving 90 days on active duty (excluding entry level and skill training). Only periods of active duty under title 10 will be used to establish eligibility for the Post 9/11 GI Bill. A high school diploma or equivalency certificate is always required for eligibility. Individuals who are eligible for the Montgomery GI Bill \u2013 Active Duty (chapter 30), the Montgomery GI Bill \u2013 Selected Reserve (chapter 1606), or the Reserve Educational Assistance Program (REAP) will have to make an irrevocable election to relinquish eligibility under one of those benefit programs to establish eligibility under the Post-9/11 GI Bill. The dependent children of a person who died in the line of duty while serving as a member of the Armed Forces may be eligible to use benefits under the Fry Scholarship provision of the Post-9/11 GI Bill. The spouse and/or child(ren) of a veteran or service member may be eligible for the Post 9/11 GI Bill if the veteran or service member transfers entitlement to those dependents. Eligibility to transfer entitlement to dependents is determined by the Department of Defense. This is not a complete list of eligibility requirements. For more information on the latest changes to the Post-9/11 GI Bill go to the VA web-site.</p>",
-            "title": "USA SPENDING EDUCATION CH33 B028 POST-9/11 VETERANS EDUCATIONAL ASSISTANCE OCT2018",
-            "isPartOf": "b1ccf8ba-c587-42fb-a25b-e8aa08fcc90b",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38642,67 +38626,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/eex4-q387/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/eex4-q387/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/eex4-q387/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/eex4-q387/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/eex4-q387/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/eex4-q387/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/eex4-q387/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/eex4-q387/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/eex4-q387/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/eex4-q387",
+            "isPartOf": "b1ccf8ba-c587-42fb-a25b-e8aa08fcc90b",
+            "issued": "2019-03-21",
+            "keyword": [
+                "cfda 64 028"
+            ],
+            "landingPage": "https://www.data.va.gov/d/eex4-q387",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING EDUCATION CH33 B028 POST-9/11 VETERANS EDUCATIONAL ASSISTANCE OCT2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Number_of_policies_by_Program_by_state_Oct2011.csv",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2010-10-01T04:00:00Z/2011-10-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/Technicalnotes_policies_in_force_by_program_Oct2011.doc"
-            ],
-            "keyword": [
-                "benefits",
-                "insurance",
-                "state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Dusca Fichtel",
                 "hasEmail": "mailto:dusca.fichtel@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-INS2011-009",
+            "dataQuality": true,
             "description": "<p>Number of life insurance policies for each administered life insurance program listed by state. Data is current as of 10/31/11.  All programs are closed to new issues except for Service-Disabled Veterans' Insurance and Veterans' Mortgage Life Insurance.  United States Government Life Insurance was issued to WWI military personnel and Veterans.  National Service Life Insurance was established to meet the needs of WWII military personnel and Veterans.  Veterans' Special Life Insurance was issued to Korean War-era Veterans.  Veterans' Reopened Insurance provides coverage to certain classes of disabled Veterans from WWII and the Korean conflict who had dropped their government life insurance coverage.  Service-Disabled Veterans' Insurance was established in 1951 and is available to Veterans with service-connected disabilities.  Veterans' Mortgage Life Insurance was established in 1971 to provide mortgage protection life insurance to severely disabled Veterans who have received grants for the purchase of specially-adapted housing.</p>",
-            "title": "FY11_EOM_Oct_Number of Life Insurance Policies by Program by State 2011/10/31",
-            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38710,121 +38688,113 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/efdb-fqcm/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/efdb-fqcm/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/efdb-fqcm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/efdb-fqcm/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/efdb-fqcm/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/efdb-fqcm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/efdb-fqcm/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/efdb-fqcm/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/efdb-fqcm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INS2011-009",
+            "isPartOf": "VA-VBA-MASTER-INSURANCE-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "benefits",
+                "insurance",
+                "state"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/Number_of_policies_by_Program_by_state_Oct2011.csv",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/VETDATA/docs/Datagov/Technicalnotes_policies_in_force_by_program_Oct2011.doc"
+            ],
+            "temporal": "2010-10-01T04:00:00Z/2011-10-31T04:00:00Z",
             "theme": [
                 "Section 25. Banking",
                 "Finance",
                 "and Insurance"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY11_EOM_Oct_Number of Life Insurance Policies by Program by State 2011/10/31"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.usaspending.gov",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Monica Reyes",
+                "hasEmail": "mailto:monica.reyes@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>USA Spending- Native American direct Loan- December 2013.</p>",
+            "identifier": "VA-VBA-USASPENDING122013-015",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2013-12-01T05:00:00Z/2013-12-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 126",
                 "lgy",
                 "native american direct loan",
                 "usa spending"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Monica Reyes",
-                "hasEmail": "mailto:monica.reyes@va.gov"
-            },
+            "landingPage": "https://www.usaspending.gov",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-USASPENDING122013-015",
-            "description": "<p>USA Spending- Native American direct Loan- December 2013.</p>",
-            "title": "USA Spending file- Native American direct Loan-  CFDA 64.126",
-            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2013-12-01T05:00:00Z/2013-12-30T05:00:00Z",
             "theme": [
                 "USA Spending"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USA Spending file- Native American direct Loan-  CFDA 64.126"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/egzm-u7ar",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2019-11-12",
-            "@type": "dcat:Dataset",
-            "modified": "2021-07-19",
-            "keyword": [
-                "age",
-                "demographics",
-                "ethnicity",
-                "geography",
-                "health",
-                "health-equity",
-                "mental health",
-                "ohe",
-                "patient",
-                "race",
-                "registry",
-                "sex",
-                "utilization",
-                "va",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VHA Office of Health Equity",
                 "hasEmail": "mailto:healthequity@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/egzm-u7ar",
             "description": "A subset of the FY13 National Veteran Health Equity Report, filtered by age group.\n\nThe National Veteran Health Equity Report details patterns and provides comparative rates of health conditions for vulnerable Veteran groups. Specifically, this report is designed to provide basic comparative information on the sociodemographics, utilization patterns and rates of diagnosed health conditions among the groups over which the VHA Office of Health Equity (OHE) has responsibility with respect to monitoring, evaluating and acting on identified disparities in access, use, care, quality and outcomes. The report allows the VA, Veterans, and stakeholders to monitor the care vulnerable Veterans receive and set goals for improving their care.",
-            "title": "VA-OHE-NVHER-FY13-Diagnoses-Age",
-            "programCode": [
-                "029:048"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38832,62 +38802,72 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/egzm-u7ar/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/egzm-u7ar/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/egzm-u7ar/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/egzm-u7ar/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/egzm-u7ar/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/egzm-u7ar/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/egzm-u7ar/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/egzm-u7ar/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/egzm-u7ar/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode"
+            "identifier": "https://www.data.va.gov/api/views/egzm-u7ar",
+            "issued": "2019-11-12",
+            "keyword": [
+                "age",
+                "demographics",
+                "ethnicity",
+                "geography",
+                "health",
+                "health-equity",
+                "mental health",
+                "ohe",
+                "patient",
+                "race",
+                "registry",
+                "sex",
+                "utilization",
+                "va",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/egzm-u7ar",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode",
+            "modified": "2021-07-19",
+            "programCode": [
+                "029:048"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VA-OHE-NVHER-FY13-Diagnoses-Age"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-02",
-            "keyword": [
-                "fy2012 benefits",
-                "fy2012 vba",
-                "vba",
-                "vba benefits",
-                "vba benefits by state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Elwell",
                 "hasEmail": "mailto:thomas.elwell@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-ABR2012-077",
+            "dataQuality": true,
             "description": "<p>State FY2012 benefit summary for all VBA businesslines.</p>",
-            "title": "Alabama-FY12 Benefits Summary",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38895,49 +38875,47 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-077",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "fy2012 benefits",
+                "fy2012 vba",
+                "vba",
+                "vba benefits",
+                "vba benefits by state"
+            ],
+            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2022-03-02",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "ABR 2012"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Alabama-FY12 Benefits Summary"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ehsn-n78r",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2022-03-15",
-            "@type": "dcat:Dataset",
-            "modified": "2023-01-05",
-            "keyword": [
-                "utilization",
-                "va benefits",
-                "va programs",
-                "va services",
-                "veteran benefits",
-                "veterans",
-                "veterans benefits"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:VANCVAS@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/ehsn-n78r",
             "description": "Data underlying the first figure in the FY2021 Utilization Profile, a report on Veterans' use of VA benefits and services.",
-            "title": "Users of VA Benefits by Program, FY2021",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -38945,59 +38923,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ehsn-n78r/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ehsn-n78r/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ehsn-n78r/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ehsn-n78r/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ehsn-n78r/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ehsn-n78r/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ehsn-n78r/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ehsn-n78r/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ehsn-n78r/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/ehsn-n78r",
+            "issued": "2022-03-15",
+            "keyword": [
+                "utilization",
+                "va benefits",
+                "va programs",
+                "va services",
+                "veteran benefits",
+                "veterans",
+                "veterans benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ehsn-n78r",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-01-05",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Users of VA Benefits by Program, FY2021"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/budget/report/",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-01-01T05:00:00Z/2012-12-31T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "accountability",
-                "performance",
-                "report"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "David Zlowe",
                 "hasEmail": "mailto:David.Zlowe@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-002",
+            "dataQuality": true,
             "description": "<p>2012 VA Performance and Accountability Report.</p>",
-            "title": "2012 VA Performance and Accountability Report",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39006,44 +38989,46 @@
                     "title": "zip"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-002",
+            "issued": "2017-07-26",
+            "keyword": [
+                "accountability",
+                "performance",
+                "report"
+            ],
+            "landingPage": "https://www.va.gov/budget/report/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2012-01-01T05:00:00Z/2012-12-31T05:00:00Z",
             "theme": [
                 "Financial"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "2012 VA Performance and Accountability Report"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ei7n-2zy7",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-20",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cdfa 64.124"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE D BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/ei7n-2zy7",
+            "dataQuality": true,
             "description": "<p>VBA EDUCATION PROGRAM to provide educational assistance to persons entering the Armed Forces after December 31, 1976, and before July 1, 1985; to assist persons in obtaining an education they might otherwise not be able to afford; and to promote and assist the all volunteer military program of the United States by attracting qualified persons to serve in the Armed Forces. The participant must have entered on active duty on or after January 1, 1977, and before July 1, 1985, and either served on active duty for more than 180 continuous days receiving an other than dishonorable discharge, or have been discharged after January, 1, 1977 because of a service-connected disability. Also eligible are participants who serve for more than 180 days and who continue on active duty and have completed their first period of obligated service (or 6 years of active duty, whichever comes first). Participants must also have satisfactorily contributed to the program. (Satisfactory contribution consists of monthly deduction of $25 to $100 from military pay, up to a maximum of $2,700, for deposit in a special training fund.) Participants may make lump-sum contributions. No individuals on active duty in the Armed Forces may initially begin contributing to this program after March 31, 1987.</p>",
-            "title": "USA SPENDING EDUCATION CH30 B124 POST-VIETNAM ERA VETERANS\u2019 EDUCATIONAL ASSISTANCE APR2019",
-            "isPartOf": "d7a8ad46-1fb5-4469-82c4-e2ee7348136c",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39051,61 +39036,60 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ei7n-2zy7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ei7n-2zy7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ei7n-2zy7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ei7n-2zy7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ei7n-2zy7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ei7n-2zy7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ei7n-2zy7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ei7n-2zy7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ei7n-2zy7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/ei7n-2zy7",
+            "isPartOf": "d7a8ad46-1fb5-4469-82c4-e2ee7348136c",
+            "issued": "2019-03-20",
+            "keyword": [
+                "cdfa 64.124"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ei7n-2zy7",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING EDUCATION CH30 B124 POST-VIETNAM ERA VETERANS\u2019 EDUCATIONAL ASSISTANCE APR2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/eime-8fwr",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "new jersey"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DG&amp;A Mailgroup",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-201",
             "description": "<p>This summary describes the programs and services VA provided in New Jersey in fiscal year 2015.</p>",
-            "title": "State Summary: New Jersey FY15",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39114,42 +39098,41 @@
                     "title": "New Jersey FY 15"
                 }
             ],
+            "identifier": "VA-OEI-OEI-201",
+            "issued": "2017-07-26",
+            "keyword": [
+                "new jersey"
+            ],
+            "landingPage": "https://www.data.va.gov/d/eime-8fwr",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "State Summary: New Jersey FY15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/index.asp",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "demographic characteristics",
-                "rural",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:Tom.Garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-169",
+            "dataQuality": true,
             "description": "<p>VA released Profile of Rural Veterans: 2014. located on the Reports page under the Population category. This profile uses data from the 2014 American Community Survey data to compare the demographic and socioeconomic characteristics of Veterans who live in rural and urban areas. The profile also compares Rural Veterans with Rural non-Veterans</p>",
-            "title": "Profile of Rural Veterans: 2014",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39158,22 +39141,45 @@
                     "title": "Profile of Rural Veterans: 2014"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-169",
+            "issued": "2017-07-26",
+            "keyword": [
+                "demographic characteristics",
+                "rural",
+                "veterans"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/index.asp",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Demographics"
-            ]
+            ],
+            "title": "Profile of Rural Veterans: 2014"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.usaspending.gov",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Monica Reyes",
+                "hasEmail": "mailto:monica.reyes@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>USA Spending- Education-Post 9/11 Veterans Educational Assistance ( Chapter33) for December 2013.</p>",
+            "identifier": "VA-VBA-USASPENDING122013-001",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2013-12-01T05:00:00Z/2013-12-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 028",
                 "ch33",
@@ -39181,60 +39187,38 @@
                 "education",
                 "usa spending"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Monica Reyes",
-                "hasEmail": "mailto:monica.reyes@va.gov"
-            },
+            "landingPage": "https://www.usaspending.gov",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-USASPENDING122013-001",
-            "description": "<p>USA Spending- Education-Post 9/11 Veterans Educational Assistance ( Chapter33) for December 2013.</p>",
-            "title": "USA Spending file- Education- Chapter 33/ CFDA 64.028",
-            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2013-12-01T05:00:00Z/2013-12-30T05:00:00Z",
             "theme": [
                 "USA Spending"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USA Spending file- Education- Chapter 33/ CFDA 64.028"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/emne-4iim",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-10-30",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "27c57b7b-932b-40ee-8d28-9ea2711becd5",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Pennsylvania FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39242,28 +39226,56 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "27c57b7b-932b-40ee-8d28-9ea2711becd5",
+            "issued": "2018-10-30",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/emne-4iim",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data",
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "State Summary Pennsylvania FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/emp2-27uk",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2009-10-01T04:00:00Z/2010-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/health/HospitalReportCard.asp"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/HospitalReportCard.asp",
+            "description": "<p>Defines the quality of care at a national level between rural vs urban populations.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/VETDATA/docs/Datagov/Data_Gov_VHA_2010_Dataset13_Urban_Rural.xml",
+                    "mediaType": "application/xml",
+                    "title": "Rural vs Urban"
+                }
             ],
+            "identifier": "VA-VHA-OIA-048",
+            "isPartOf": "VA-VHA-OIA-584",
+            "issued": "2017-07-26",
             "keyword": [
                 "ambulatory",
                 "care",
@@ -39286,68 +39298,40 @@
                 "urban",
                 "veterans"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/emp2-27uk",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:040"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-OIA-048",
-            "description": "<p>Defines the quality of care at a national level between rural vs urban populations.</p>",
-            "title": "Veterans Health Administration 2010 Facility Quality and Safety Report - Rural vs Urban",
-            "isPartOf": "VA-VHA-OIA-584",
-            "programCode": [
-                "029:040"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/VETDATA/docs/Datagov/Data_Gov_VHA_2010_Dataset13_Urban_Rural.xml",
-                    "mediaType": "application/xml",
-                    "title": "Rural vs Urban"
-                }
+            "references": [
+                "https://www.va.gov/health/HospitalReportCard.asp"
             ],
-            "describedBy": "https://www.va.gov/health/HospitalReportCard.asp",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "2009-10-01T04:00:00Z/2010-09-30T04:00:00Z",
             "theme": [
                 "Section 3. Health and Nutrition"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veterans Health Administration 2010 Facility Quality and Safety Report - Rural vs Urban"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/emq7-gze7",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "maryland"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:tom.garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-190",
             "description": "<p>This summary describes the programs and services VA provided in Maine in fiscal year 2015.</p>",
-            "title": "State Summary: Maryland",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39356,42 +39340,41 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-OEI-OEI-190",
+            "issued": "2017-07-26",
+            "keyword": [
+                "maryland"
+            ],
+            "landingPage": "https://www.data.va.gov/d/emq7-gze7",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "State Summary: Maryland"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "annual report",
-                "va",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:Tom.Garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-149",
+            "dataQuality": true,
             "description": "<p>This reports the activities of the Veterans Administration for the fiscal year ending September 30, 1986.</p>",
-            "title": "Annual Report:  1986",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39400,48 +39383,45 @@
                     "title": "Annual Report:  1986"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-149",
+            "issued": "2017-07-26",
+            "keyword": [
+                "annual report",
+                "va",
+                "veterans"
+            ],
+            "landingPage": "https://www.va.gov/vetdata/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Demographics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Annual Report:  1986"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/FY11_End_of_April_EDU_recp_by_Training_Type.csv",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-04-01T04:00:00Z/2011-04-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/VETDATA/docs/Datagov/FY11_End_of_April_EDU_recp_by_Training_Type.csv"
-            ],
-            "keyword": [
-                "education",
-                "veteran"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Salminio Garner",
                 "hasEmail": "mailto:salminio.garner1@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-EDU2011-001",
+            "dataQuality": true,
             "description": "<p>FY 11 Education Recipients by training type  and VA Education Benefit Program (Through April. FY11). The data represents the number of individuals by VA education program who have used their VA education benefit during fiscal year 2011(Through the April. FY11). Training type statistics may include individuals who used their education benefits in more than one training type, therefore the total within this table may be different than the total number of beneficiaries during the fiscal year.</p>",
-            "title": "EOM April FY 11  Education Recipients by Training Type and VA Education Benefit Program",
-            "isPartOf": "VA-VBA-MASTER-EDUCATION-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39449,66 +39429,69 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ep4d-p7p2/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ep4d-p7p2/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ep4d-p7p2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ep4d-p7p2/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ep4d-p7p2/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ep4d-p7p2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ep4d-p7p2/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ep4d-p7p2/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ep4d-p7p2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-EDU2011-001",
+            "isPartOf": "VA-VBA-MASTER-EDUCATION-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "education",
+                "veteran"
+            ],
+            "landingPage": "https://www.va.gov/VETDATA/docs/Datagov/FY11_End_of_April_EDU_recp_by_Training_Type.csv",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/VETDATA/docs/Datagov/FY11_End_of_April_EDU_recp_by_Training_Type.csv"
+            ],
+            "temporal": "2011-04-01T04:00:00Z/2011-04-30T04:00:00Z",
             "theme": [
                 "Section 4. Education"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "EOM April FY 11  Education Recipients by Training Type and VA Education Benefit Program"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ep92-fg9j",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-27",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 105",
-                "cfda 64 110"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/ep92-fg9j",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to provide educational opportunities to the dependents of certain disabled and deceased veterans. Spouses, surviving spouses, and children (including stepchild or adopted child) between age 18 and 26 of veterans who died from service-connected disabilities, of living veterans whose service-connected disabilities are considered permanently and totally disabling, of those who died from any cause while such service-connected disabilities were in existence, of servicepersons who have been listed for a total of more than 90 days as currently missing in action, or as currently prisoners of war, a service member who VA determines has a service connected permanent and total disability and at the time of VA's determination is a member of the Armed Forces who is hospitalized or receiving outpatient medical care, services, or treatment; and is likely to be discharged or released from service for this service-connected disability. Children under the age of 18 may be eligible under special circumstances.</p>",
-            "title": "USA SPENDING C&P B110 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE FEB2019",
-            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39516,63 +39499,63 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ep92-fg9j/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ep92-fg9j/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ep92-fg9j/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ep92-fg9j/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ep92-fg9j/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ep92-fg9j/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ep92-fg9j/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ep92-fg9j/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ep92-fg9j/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/ep92-fg9j",
+            "isPartOf": "8ad0aa0e-af41-448e-8ebf-287798035e69",
+            "issued": "2019-03-27",
+            "keyword": [
+                "cfda 64 105",
+                "cfda 64 110"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ep92-fg9j",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING C&P B110 SURVIVORS AND DEPENDENTS EDUCATIONAL ASSISTANCE FEB2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.green.va.gov/fleet/",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2012-10-01T04:00:00Z/2013-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-04",
-            "keyword": [
-                "alternative fuel vehicles",
-                "fleet",
-                "vehicle"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VA OM Open Data",
                 "hasEmail": "mailto:VAOMOpenData@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OM-OM-045",
+            "dataQuality": true,
             "description": "FY 2013 Annual Vehicle Fleet Report on Alternative Fuel Vehicles",
-            "title": "FY 2013 Annual Vehicle Fleet Report on Alternative Fuel Vehicles",
-            "programCode": [
-                "029:084"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39580,44 +39563,45 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OM-OM-045",
+            "issued": "2017-07-26",
+            "keyword": [
+                "alternative fuel vehicles",
+                "fleet",
+                "vehicle"
+            ],
+            "landingPage": "https://www.green.va.gov/fleet/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2024-06-04",
+            "programCode": [
+                "029:084"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2012-10-01T04:00:00Z/2013-09-30T04:00:00Z",
             "theme": [
                 "Fleet"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "FY 2013 Annual Vehicle Fleet Report on Alternative Fuel Vehicles"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/epjn-fgke",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-22",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 106"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/epjn-fgke",
+            "dataQuality": true,
             "description": "<p>VBA SPECIALLY ADAPTED HOUSING BENEFIT PROGRAMS. The Specially Adapted Housing (SAH) grant program helps Veterans with certain service-connected disabilities live independently in a barrier-free environment. SAH grants can be used in one of the following ways: (1) construct a suitable home on suitable land either already owned or to be acquired by the veteran, or (2) remodel an existing home if it can be suitably adapted, or (3) acquire a suitably adapted home or reduce the outstanding mortgage on a suitably adapted home already owned by the veteran. b. The Special Housing Adaptation (SHA) grant program helps veterans with certain service-connected disabilities adapt or purchase a home to accommodate the disability. SHA grants can be used in one of the following ways: (1) adapt an existing home the veteran or a family member already owns in which the veteran lives; (2) adapt a home the veteran or family member intends to purchase in which the veteran will live; (3) help a veteran purchase a home already adapted in which the veteran will live. c. . The Temporary Residence Adaptations (TRA) program provides adaptation assistance to veterans who are residing, but do not intend to permanently reside, in the a residence owned by a family member. If a veteran is otherwise eligible for SAH or SHA, the assistance is limited. d. SAH and SHA grants may be used up to three times, as long as the aggregate grant amount does not exceed the statutory dollar limitation. TRA grants may only be used once (and count as a grant usage for purposes of the limit of three), and the amount of assistance provided will be subtracted from the veteran's available statutory maximum.</p>",
-            "title": "USA SPENDING CH39 B106 SPECIALLY ADAPTED HOUSING FOR DISABLED VETERANS FEB2019",
-            "isPartOf": "bc3a6e1f-3fb0-4fb1-8b07-59efaf92222b",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39625,64 +39609,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/epjn-fgke/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/epjn-fgke/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/epjn-fgke/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/epjn-fgke/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/epjn-fgke/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/epjn-fgke/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/epjn-fgke/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/epjn-fgke/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/epjn-fgke/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/epjn-fgke",
+            "isPartOf": "bc3a6e1f-3fb0-4fb1-8b07-59efaf92222b",
+            "issued": "2019-03-22",
+            "keyword": [
+                "cfda 64 106"
+            ],
+            "landingPage": "https://www.data.va.gov/d/epjn-fgke",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING CH39 B106 SPECIALLY ADAPTED HOUSING FOR DISABLED VETERANS FEB2019"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/ogc/",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "This is content from the public-facing web site currently accessible through standard web browsing methods",
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2014-10-01T04:00:00Z/2015-10-01T04:00:00Z",
-            "modified": "2020-05-15",
-            "keyword": [
-                "districts",
-                "map",
-                "web site"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Melinda Perritano",
                 "hasEmail": "mailto:Melinda.Perritano@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OGC-002",
+            "dataQuality": true,
             "description": "<p>A map of the geographical layout of OGC Districts.</p>",
-            "title": "OGC District Counsel Map",
-            "programCode": [
-                "029:083"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39691,27 +39672,59 @@
                     "title": "OGC Chief Counsel District Map"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-OGC-002",
+            "issued": "2017-07-26",
+            "keyword": [
+                "districts",
+                "map",
+                "web site"
+            ],
+            "landingPage": "https://www.va.gov/ogc/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:083"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "This is content from the public-facing web site currently accessible through standard web browsing methods",
+            "temporal": "2014-10-01T04:00:00Z/2015-10-01T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "OGC District Counsel Map"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/eqkg-9xmk",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "029:00"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Sail Operations",
+                "hasEmail": "mailto:VHASailOperations@va.gov"
+            },
+            "dataQuality": true,
+            "description": "Why Not the Best VA or WNTBVA is a system for comparing Veterans Health Administration (VHA) hospital system performance with regional and U.S. national benchmarks.  This report includes key quality measures available on CMS Hospital Compare and top hospital recognition programs from reporting agencies of hospital quality.  These .ZIP files are no longer supported and are in an 'as-is' state.  They were accurate at time of publication.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.data.va.gov/download/eqkg-9xmk/application/zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "identifier": "https://www.data.va.gov/api/views/eqkg-9xmk",
+            "isPartOf": "VA-VHA-OIA-122",
             "issued": "2020-10-23",
-            "@type": "dcat:Dataset",
-            "temporal": "2017-10-01/2018-09-30",
-            "modified": "2021-06-24",
             "keyword": [
                 "2018",
                 "fy2018",
@@ -39730,70 +39743,39 @@
                 "veteran",
                 "wntbva"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Sail Operations",
-                "hasEmail": "mailto:VHASailOperations@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/eqkg-9xmk",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-06-24",
+            "programCode": [
+                "029:040"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "https://www.data.va.gov/api/views/eqkg-9xmk",
-            "description": "Why Not the Best VA or WNTBVA is a system for comparing Veterans Health Administration (VHA) hospital system performance with regional and U.S. national benchmarks.  This report includes key quality measures available on CMS Hospital Compare and top hospital recognition programs from reporting agencies of hospital quality.  These .ZIP files are no longer supported and are in an 'as-is' state.  They were accurate at time of publication.",
-            "title": "Why Not the Best VA FY2018 Hospital Performance - All Facilities",
-            "isPartOf": "VA-VHA-OIA-122",
-            "programCode": [
-                "029:040"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.data.va.gov/download/eqkg-9xmk/application/zip",
-                    "mediaType": "application/zip"
-                }
-            ],
             "spatial": "United States, Puerto Rico",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P3M",
+            "temporal": "2017-10-01/2018-09-30",
             "theme": [
                 "Hospital Quality Measurement"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Why Not the Best VA FY2018 Hospital Performance - All Facilities"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/esdj-yhpu",
-            "bureauCode": [
-                "029:00"
-            ],
-            "issued": "2017-03-15",
             "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "health care",
-                "income",
-                "statistics"
+            "accessLevel": "public",
+            "bureauCode": [
+                "029:00"
             ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:tom.garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/esdj-yhpu",
+            "dataQuality": true,
             "description": "<p>This dataset contains information on minority veteran healthcare usage, educational attainment, unemployment rates, median income, and projected population figures.</p>",
-            "title": "Projected Population Growth of Minority Veterans, 2014-2043",
-            "isPartOf": "1d427f8d-0018-4fac-905b-6008ead44b3d",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39801,46 +39783,67 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/esdj-yhpu/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/esdj-yhpu/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/esdj-yhpu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/esdj-yhpu/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/esdj-yhpu/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/esdj-yhpu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/esdj-yhpu/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/esdj-yhpu/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/esdj-yhpu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/esdj-yhpu",
+            "isPartOf": "1d427f8d-0018-4fac-905b-6008ead44b3d",
+            "issued": "2017-03-15",
+            "keyword": [
+                "health care",
+                "income",
+                "statistics"
+            ],
+            "landingPage": "https://www.data.va.gov/d/esdj-yhpu",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "Projected Population Growth of Minority Veterans, 2014-2043"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "non-public",
-            "landingPage": "https://www.data.va.gov/d/espt-hpfu",
             "bureauCode": [
                 "029:15"
             ],
-            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>The Environmental Agent Service (EAS) Registries is the information system encompassing the Ionizing Radiation Registry (IRR), the Agent Orange Registry (AOR), and the Gulf War Registry (GWR) which also includes related Depleted Uranium (DU) exams.  These registries were originally developed using paper code sheets that were sent to the VA Austin Information Technology Center where typists converted to data files on the mainframe. The Registries have undergone a modernization and simplification effort that allows the entry of data via a web interface at <a href=\"https://vaww.registries.aac.va.gov/eas/\">https://vaww.registries.aac.va.gov/eas/</a> by staff at the VA medical centers. In compliance with the Federal Information Systems Management Act (FISMA) this is considered a single system of records with the three registry components i.e. IRR, AOR, GWR with DU that have been integrated into a single Oracle database.  Please see individual Monograph entries for specific details on:  Ionizing Radiation Registry (IRR), Agent Orange Registry (AOR), and the Gulf War Registry (GWR).</p>",
+            "identifier": "VA-VHA-OPH-006",
             "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "1998-01-01T05:00:00Z/2014-12-31T05:00:00Z",
-            "modified": "2020-12-01",
             "keyword": [
                 "agent",
                 "agent orange",
@@ -39855,56 +39858,40 @@
                 "veteran",
                 "war"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.data.va.gov/d/espt-hpfu",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:041"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-OPH-006",
-            "description": "<p>The Environmental Agent Service (EAS) Registries is the information system encompassing the Ionizing Radiation Registry (IRR), the Agent Orange Registry (AOR), and the Gulf War Registry (GWR) which also includes related Depleted Uranium (DU) exams.  These registries were originally developed using paper code sheets that were sent to the VA Austin Information Technology Center where typists converted to data files on the mainframe. The Registries have undergone a modernization and simplification effort that allows the entry of data via a web interface at <a href=\"https://vaww.registries.aac.va.gov/eas/\">https://vaww.registries.aac.va.gov/eas/</a> by staff at the VA medical centers. In compliance with the Federal Information Systems Management Act (FISMA) this is considered a single system of records with the three registry components i.e. IRR, AOR, GWR with DU that have been integrated into a single Oracle database.  Please see individual Monograph entries for specific details on:  Ionizing Radiation Registry (IRR), Agent Orange Registry (AOR), and the Gulf War Registry (GWR).</p>",
-            "title": "Environmental Agents Service (EAS) Registry System of Records",
-            "programCode": [
-                "029:041"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "rights": "Health Insurance Portability and Accountability Act, protected health information.",
+            "temporal": "1998-01-01T05:00:00Z/2014-12-31T05:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Environmental Agents Service (EAS) Registry System of Records"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/esyr-iidp",
-            "issued": "2024-04-19",
-            "@type": "dcat:Dataset",
-            "modified": "2024-05-02",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Florinda Balfour",
                 "hasEmail": "mailto:VACONCVAS@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/esyr-iidp",
             "description": "",
-            "title": "vetpop_age",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39912,56 +39899,53 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/esyr-iidp/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/esyr-iidp/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/esyr-iidp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/esyr-iidp/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/esyr-iidp/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/esyr-iidp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/esyr-iidp/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/esyr-iidp/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/esyr-iidp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/esyr-iidp",
+            "issued": "2024-04-19",
+            "landingPage": "https://www.data.va.gov/d/esyr-iidp",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-05-02",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "vetpop_age"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/etfd-3wdi",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "north dakota"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DG&amp;A Mailgroup",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-205",
             "description": "<p>This summary describes the programs and services VA provided in North Dakota in fiscal year 2015.</p>",
-            "title": "State Summary: North Dakota FY15",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -39970,60 +39954,59 @@
                     "title": "North Dakota"
                 }
             ],
+            "identifier": "VA-OEI-OEI-205",
+            "issued": "2017-07-26",
+            "keyword": [
+                "north dakota"
+            ],
+            "landingPage": "https://www.data.va.gov/d/etfd-3wdi",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "State Summary: North Dakota FY15"
         },
         {
-            "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/etht-qz26",
-            "issued": "2024-03-27",
             "@type": "dcat:Dataset",
-            "modified": "2024-09-04",
+            "accessLevel": "public",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Rebecca Matteo",
                 "hasEmail": "mailto:no-reply@ptsd-va.data.socrata.com"
             },
+            "description": "Learn about this resource that brings together information from over 500 published studies on a wide range of PTSD treatments.",
             "identifier": "https://www.data.va.gov/api/views/etht-qz26",
+            "issued": "2024-03-27",
+            "landingPage": "https://www.data.va.gov/d/etht-qz26",
+            "modified": "2024-09-04",
             "publisher": {
                 "@type": "org:Organization",
                 "name": "www.data.va.gov"
             },
-            "description": "Learn about this resource that brings together information from over 500 published studies on a wide range of PTSD treatments.",
             "title": "For Everyone: About the PTSD Repository"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/etxu-jw8r",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "certificates",
-                "presidential"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "James Killens III",
                 "hasEmail": "mailto:james.killensiii@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-NCA-PMC-001",
             "description": "<p>This fact sheet provides and background information and history of the Presidential Memorial Certificates Office</p>",
-            "title": "Presidential Memorial Certificates Fact Sheet",
-            "programCode": [
-                "029:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40032,47 +40015,42 @@
                     "title": "pdf"
                 }
             ],
+            "identifier": "VA-NCA-PMC-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "certificates",
+                "presidential"
+            ],
+            "landingPage": "https://www.data.va.gov/d/etxu-jw8r",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "Presidential Memorial Certificates Fact Sheet"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.medicare.gov/nursinghomecompare/search.html?",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2018-06-12",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "analytics",
-                "compare",
-                "health",
-                "healthcare",
-                "nursing home",
-                "performance",
-                "quality",
-                "veteran"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VHA Open Data",
                 "hasEmail": "mailto:vhaopendata@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "e076b291-3c59-49e9-bb31-4f46ec9cf1b7",
+            "dataQuality": true,
             "description": "<p>Nursing Home Compare has detailed information about every Medicare and Medicaid nursing home in the country. A nursing home is a place for people who can\u2019t be cared for at home and need 24-hour nursing care.  These are the official datasets used on the Medicare.gov Nursing Home Compare Website provided by the Centers for Medicare &amp; Medicaid Services. These data allow you to compare the quality of care at every Medicare and Medicaid-certified nursing home in the country, including over 15,000 nationwide.</p>",
-            "title": "Nursing Home Compare",
-            "programCode": [
-                "029:055"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40081,45 +40059,51 @@
                     "title": "Nursing Home Compare Datasets"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "e076b291-3c59-49e9-bb31-4f46ec9cf1b7",
+            "issued": "2018-06-12",
+            "keyword": [
+                "analytics",
+                "compare",
+                "health",
+                "healthcare",
+                "nursing home",
+                "performance",
+                "quality",
+                "veteran"
+            ],
+            "landingPage": "https://www.medicare.gov/nursinghomecompare/search.html?",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:055"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Nursing Home Compare"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/evtj-p45r",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-08-01",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS mailbox",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "41fcda1d-ddbe-4bc8-a519-35c84abd444c",
+            "dataQuality": true,
             "description": "<p>GDX provides VA expenditure data at the state, county, and Congressional District levels.  It contains data on the Veteran population, Compensation and Pension, Medical Care, and other categories.  Data sources include the Veteran Population Projection Model 2016, the Financial Management System, USASpending, and the Allocation Resource Center.</p>",
-            "title": "GDX FY17",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40127,19 +40111,50 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
+            "identifier": "41fcda1d-ddbe-4bc8-a519-35c84abd444c",
+            "issued": "2018-08-01",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/evtj-p45r",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2020-11-12",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "GDX FY17"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "accrualPeriodicity": "R/P2W",
             "bureauCode": [
                 "029:15"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/access-audit.asp",
+            "description": "<p>This release included wait time data for each facility down to the Community Based Outpatient Clinic (CBOC) level.  Wait times are calculated using the Preferred Date for all patients.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/PublicData_Completed_Access_Data_20150531RptDate_Final.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Completed Appointments 31 May 2015"
+                }
+            ],
+            "identifier": "VA-VHA-OIA-110",
+            "isPartOf": "VA-VHA-OIA-073",
             "issued": "2017-07-26",
-            "temporal": "2015-05-31T04:00:00Z/2015-05-31T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
             "keyword": [
                 "access",
                 "appointment",
@@ -40153,70 +40168,39 @@
                 "wait list",
                 "wait time"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:041"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-OIA-110",
-            "description": "<p>This release included wait time data for each facility down to the Community Based Outpatient Clinic (CBOC) level.  Wait times are calculated using the Preferred Date for all patients.</p>",
-            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2015 May 31",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/PublicData_Completed_Access_Data_20150531RptDate_Final.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Completed Appointments 31 May 2015"
-                }
-            ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2W",
+            "temporal": "2015-05-31T04:00:00Z/2015-05-31T04:00:00Z",
             "theme": [
                 "Accelerating Access"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Completed Appointments - Report 2015 May 31"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/evx4-bqnp",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2018-10-29",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "demographics",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "vancvas@va.gov",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "ee16f454-0bfc-4c8a-8619-e88383dc4a63",
+            "dataQuality": true,
             "description": "<p>The FY2017 State Summaries provide an overview of benefits, services, demographics and population of Veterans analyzed by state.</p>",
-            "title": "State Summary Alabama FY2017",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40224,26 +40208,55 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "ee16f454-0bfc-4c8a-8619-e88383dc4a63",
+            "issued": "2018-10-29",
+            "keyword": [
+                "demographics",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/evx4-bqnp",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data",
                 "Demographics",
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "State Summary Alabama FY2017"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.oprm.va.gov/foia/",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:40"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VA OM Open Data",
+                "hasEmail": "mailto:VAOMOpenData@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) Report for Fiscal Year 1999.  The report contains metrics on FOIA requests received, processed, and pending by agency/component.  It also contains metrics on exemptions, appeals, consultations, response times, and backlogs.  Fees collected, fees waived, and FOIA personnel and costs are reported.  Comparison of metrics attained for the previous year is also included.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.oprm.va.gov/docs/foia/Report1999.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "pdf"
+                }
+            ],
+            "identifier": "VA-OIT-ITIS-15",
             "issued": "2017-07-26",
-            "temporal": "1998-10-01T04:00:00Z/1999-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-06-07",
             "keyword": [
                 "1999",
                 "appeals",
@@ -40260,113 +40273,85 @@
                 "response time",
                 "va"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VA OM Open Data",
-                "hasEmail": "mailto:VAOMOpenData@va.gov"
-            },
+            "landingPage": "https://www.oprm.va.gov/foia/",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-06-07",
+            "programCode": [
+                "029:080"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-OIT-ITIS-15",
-            "description": "<p>This is the Department of Veterans Affairs, Freedom of Information Act (FOIA) Report for Fiscal Year 1999.  The report contains metrics on FOIA requests received, processed, and pending by agency/component.  It also contains metrics on exemptions, appeals, consultations, response times, and backlogs.  Fees collected, fees waived, and FOIA personnel and costs are reported.  Comparison of metrics attained for the previous year is also included.</p>",
-            "title": "Department of Veterans Affairs Freedom of Information Act (FOIA) Report for Fiscal Year 1999",
-            "programCode": [
-                "029:080"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.oprm.va.gov/docs/foia/Report1999.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "pdf"
-                }
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "temporal": "1998-10-01T04:00:00Z/1999-09-30T04:00:00Z",
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Department of Veterans Affairs Freedom of Information Act (FOIA) Report for Fiscal Year 1999"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.usaspending.gov/",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "029:25"
             ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Monica Reyes",
+                "hasEmail": "mailto:monica.reyes@va.gov"
+            },
+            "dataQuality": true,
+            "description": "<p>USA Spending- Veterans Dependency and indemnity Compensation for Service-Connected Death-- March 2014</p>",
+            "identifier": "VA-VBA-USASPENDING032014-049",
+            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
             "issued": "2017-07-26",
-            "temporal": "2014-02-01T05:00:00Z/2014-02-28T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-12-01",
             "keyword": [
                 "cfda 64 110",
                 "compensation and pension",
                 "dependency and indemnity compensation for service connected death",
                 "usa spending"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Monica Reyes",
-                "hasEmail": "mailto:monica.reyes@va.gov"
-            },
+            "landingPage": "https://www.usaspending.gov/",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-12-01",
+            "programCode": [
+                "029:003"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VBA-USASPENDING032014-049",
-            "description": "<p>USA Spending- Veterans Dependency and indemnity Compensation for Service-Connected Death-- March 2014</p>",
-            "title": "USA Spending file- 03/2014 Veterans Dependency and indemnity Compensation for Service-Connected Death-  CFDA 64.110",
-            "isPartOf": "VA-VBA-MASTER-USA Spending-001",
-            "programCode": [
-                "029:003"
-            ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1M",
+            "temporal": "2014-02-01T05:00:00Z/2014-02-28T05:00:00Z",
             "theme": [
                 "USA Spending"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "USA Spending file- 03/2014 Veterans Dependency and indemnity Compensation for Service-Connected Death-  CFDA 64.110"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/vetdata/",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "rights": "Public",
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "temporal": "2011-01-01T05:00:00Z/2011-12-31T05:00:00Z",
-            "modified": "2020-05-15",
-            "keyword": [
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:tom.garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-015",
-            "description": "<p>This report uses data from the 2011 American Community Survey to compare the demographic and socioeconomic characteristics of Veterans and non-Veterans. It also explores the differences between male and female Veterans.</p>",
-            "title": "Profile of Veterans 2011",
+            "dataQuality": true,
+            "describedBy": "https://www.census.gov/acs/www/Downloads/data_documentation/pums/DataDict/PUMSDataDict10.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "029:086"
-            ],
+            "description": "<p>This report uses data from the 2011 American Community Survey to compare the demographic and socioeconomic characteristics of Veterans and non-Veterans. It also explores the differences between male and female Veterans.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40375,61 +40360,45 @@
                     "title": "pdf"
                 }
             ],
-            "describedBy": "https://www.census.gov/acs/www/Downloads/data_documentation/pums/DataDict/PUMSDataDict10.pdf",
-            "dataQuality": true,
+            "identifier": "VA-OEI-OEI-015",
+            "issued": "2017-07-26",
+            "keyword": [
+                "veterans"
+            ],
+            "landingPage": "https://www.va.gov/vetdata/",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Public",
+            "temporal": "2011-01-01T05:00:00Z/2011-12-31T05:00:00Z",
             "theme": [
                 "Demographics"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Profile of Veterans 2011"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ewtj-e7sk",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2022-05-04",
-            "@type": "dcat:Dataset",
-            "modified": "2022-05-04",
-            "keyword": [
-                "ethnicity",
-                "fy20",
-                "fy 20",
-                "fy2020",
-                "fy 2020",
-                "healthcare",
-                "health care",
-                "race",
-                "va healthcare",
-                "va health care",
-                "va user",
-                "va users",
-                "veteran",
-                "veteran healthcare",
-                "veteran health care",
-                "veterans",
-                "veteran user",
-                "veteran users"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Mike Schwaber",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/ewtj-e7sk",
+            "dataQuality": true,
             "description": "Note: \"Total Number of Veterans\" represents FY 2020 projected Veteran counts from VA's Veteran Population Projection Model 2018 (VetPop18). These projections are made with the assumption that Veterans are not missing information (e.g. ethnicity, etc.).\nNote: \"Veteran VA Users\" and \"Veteran VA Healthcare Users\" represent historical Veteran counts from VA's United States Veterans Eligibility Trends and Statistics 2020 (USVETS 2020).\nNote: \"Veteran VA Users\" includes Veteran users of VA healthcare or any other VA benefit or service.\n\nSources: USVETS 2020 and VetPop18",
-            "title": "FY 2020 Total Number of Veterans, Veteran VA Users, and Veteran VA Healthcare Users by Ethnicity",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40437,62 +40406,77 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ewtj-e7sk/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ewtj-e7sk/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ewtj-e7sk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ewtj-e7sk/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ewtj-e7sk/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ewtj-e7sk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ewtj-e7sk/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ewtj-e7sk/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ewtj-e7sk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y",
+            "identifier": "https://www.data.va.gov/api/views/ewtj-e7sk",
+            "issued": "2022-05-04",
+            "keyword": [
+                "ethnicity",
+                "fy20",
+                "fy 20",
+                "fy2020",
+                "fy 2020",
+                "healthcare",
+                "health care",
+                "race",
+                "va healthcare",
+                "va health care",
+                "va user",
+                "va users",
+                "veteran",
+                "veteran healthcare",
+                "veteran health care",
+                "veterans",
+                "veteran user",
+                "veteran users"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ewtj-e7sk",
             "language": [
                 "English"
-            ]
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2022-05-04",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "FY 2020 Total Number of Veterans, Veteran VA Users, and Veteran VA Healthcare Users by Ethnicity"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.data.va.gov/d/ewx6-sb25",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2017-11-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "d2d"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bret Meyer",
                 "hasEmail": "mailto:bret.meyer@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-ORCH-8",
+            "dataQuality": true,
             "description": "<p>D2D Enables external systems to submit (through VLER) structured official VA Forms with/without attachment documents and orchestrates temporary storage, virus checking and message durability. When complete, submits form to appropriate Form Submission Service for orchestration</p>",
-            "title": "Digits-to-Digits (D2D)",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40501,71 +40485,69 @@
                     "title": "Digits-to-Digits (D2D)"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "identifier": "VA-ORCH-8",
+            "issued": "2017-11-17",
+            "keyword": [
+                "d2d"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ewx6-sb25",
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
+            "title": "Digits-to-Digits (D2D)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/ext4-vs3c",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-08",
-            "keyword": [
-                "kansas",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VANCVAS",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/ext4-vs3c",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Kansas",
+            "identifier": "https://www.data.va.gov/api/views/ext4-vs3c",
+            "issued": "2021-08-26",
+            "keyword": [
+                "kansas",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ext4-vs3c",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-08",
             "programCode": [
                 "029:086"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summaries_Kansas"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ey9g-uxvm",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2021-02-18",
-            "@type": "dcat:Dataset",
-            "modified": "2021-03-23",
-            "keyword": [
-                "home loan guaranty",
-                "veteran",
-                "veteran benefits"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Florinda Balfour",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/ey9g-uxvm",
             "description": "Loan Guaranty: All Veterans who had an active, new or re-financed VA-guaranteed home loan were included. Veterans Benefits Administration (VBA) provides Home Loan Guaranty assistance.",
-            "title": "Veterans who participated in VA Home Loan Guaranty Program",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40573,67 +40555,64 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ey9g-uxvm/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ey9g-uxvm/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ey9g-uxvm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ey9g-uxvm/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ey9g-uxvm/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ey9g-uxvm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ey9g-uxvm/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ey9g-uxvm/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ey9g-uxvm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "spatial": "State",
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "identifier": "https://www.data.va.gov/api/views/ey9g-uxvm",
+            "issued": "2021-02-18",
+            "keyword": [
+                "home loan guaranty",
+                "veteran",
+                "veteran benefits"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ey9g-uxvm",
             "language": [
                 "English"
-            ]
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-03-23",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "spatial": "State",
+            "title": "Veterans who participated in VA Home Loan Guaranty Program"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/eyxf-rta7",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2022-11-30",
-            "@type": "dcat:Dataset",
-            "modified": "2022-11-30",
-            "keyword": [
-                "2021",
-                "compensation and pension",
-                "fy2021",
-                "fy 2021",
-                "fy21",
-                "fy 21",
-                "pension",
-                "state"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Mike Schwaber",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/eyxf-rta7",
+            "dataQuality": true,
             "description": "This report provides state-level estimates of the number of Veterans who received VA Pension benefits during fiscal year 2021. It includes the Veterans\u2019 gender. Blank values represent small cell counts that have been suppressed to protect the identity of Veterans. Some categories may not sum to the total due to missing information (e.g., gender, etc.).\n\nSource: Department of Veterans Affairs, Office of Enterprise Integration, United States Veterans Eligibility Trends & Statistics (USVETS) 2021 and Veterans Benefits Administration VETSNET FY 2021 pension data.\n\nPrepared by National Center for Veterans Analysis & Statistics, www.va.gov/vetdata.",
-            "title": "FY 2021 Pension Recipients by State",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40641,111 +40620,116 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/eyxf-rta7/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/eyxf-rta7/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/eyxf-rta7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/eyxf-rta7/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/eyxf-rta7/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/eyxf-rta7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/eyxf-rta7/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/eyxf-rta7/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/eyxf-rta7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode",
-            "dataQuality": true,
-            "accrualPeriodicity": "R/P1Y",
+            "identifier": "https://www.data.va.gov/api/views/eyxf-rta7",
+            "issued": "2022-11-30",
+            "keyword": [
+                "2021",
+                "compensation and pension",
+                "fy2021",
+                "fy 2021",
+                "fy21",
+                "fy 21",
+                "pension",
+                "state"
+            ],
+            "landingPage": "https://www.data.va.gov/d/eyxf-rta7",
             "language": [
                 "English"
-            ]
+            ],
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode",
+            "modified": "2022-11-30",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "FY 2021 Pension Recipients by State"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/directory/guide/home.asp",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2014-10-01T04:00:00Z/2014-12-30T05:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2024-11-25",
-            "keyword": [
-                "state veterans affairs offices",
-                "vba offices"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Elwell",
                 "hasEmail": "mailto:thomas.elwell@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-INFO-002",
+            "dataQuality": true,
             "description": "<p>List of all Veterans located in all states in USA and territories.</p>",
-            "title": "State Veterans Affairs Offices",
-            "isPartOf": "VA-VBA-MASTER-GENERAL INFORMATION-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
-                    "mediaType": "text/html",
-                    "downloadURL": "https://www.va.gov/directory/guide/home.asp",
-                    "description": "This site is a storehouse of facility and key staff information within 1960 VA facilities, maintained on a regular basis by editors and administrators nationwide throughout the VA network. Designed for ease-of-use, this site categorizes information for browsing by state and administration, as well as by viewing through an interactive map of the United States.",
                     "@type": "dcat:Distribution",
+                    "description": "This site is a storehouse of facility and key staff information within 1960 VA facilities, maintained on a regular basis by editors and administrators nationwide throughout the VA network. Designed for ease-of-use, this site categorizes information for browsing by state and administration, as well as by viewing through an interactive map of the United States.",
+                    "downloadURL": "https://www.va.gov/directory/guide/home.asp",
+                    "mediaType": "text/html",
                     "title": "State Veterans Affairs Offices"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-INFO-002",
+            "isPartOf": "VA-VBA-MASTER-GENERAL INFORMATION-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "state veterans affairs offices",
+                "vba offices"
+            ],
+            "landingPage": "https://www.va.gov/directory/guide/home.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-11-25",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2014-10-01T04:00:00Z/2014-12-30T05:00:00Z",
             "theme": [
                 "VBA Offices",
                 "State Veterans Affairs Offices"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "State Veterans Affairs Offices"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/ezz5-cnqv",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2019-03-29",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cfda 64 101"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "ANNETTE BROWN",
                 "hasEmail": "mailto:ANNETTE.BROWN2@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/ezz5-cnqv",
+            "dataQuality": true,
             "description": "<p>VBA BENEFIT PROGRAM to assist States and federally recognized tribal governments in the establishment, expansion, and improvement of veterans' cemeteries. Monetary assistance is provided under this program to establish, expand, and improve State or Tribal government veterans\u2019 cemeteries. Cemeteries must be State or Tribal Government owned and operated solely for the interment of eligible veterans and their dependents and/or spouses. Construction cost means the amount found necessary to convert a tract of land to an operational cemetery. The cemetery must be used solely for the interment of veterans, their wives, husbands, surviving spouses, minor children, and unmarried adult children who were physically or mentally disabled and incapable of self-support: section 38 CFR Part 38.620.</p>",
-            "title": "USA SPENDING C&P BURIAL B101 VETERANS CEMETARY GRANTS PROGRAM NOV2018",
-            "isPartOf": "d17c822a-717c-40ff-8fbe-3dcaefddb706",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40753,60 +40737,61 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ezz5-cnqv/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ezz5-cnqv/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ezz5-cnqv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/ezz5-cnqv/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ezz5-cnqv/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ezz5-cnqv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/ezz5-cnqv/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/ezz5-cnqv/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/ezz5-cnqv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/ezz5-cnqv",
+            "isPartOf": "d17c822a-717c-40ff-8fbe-3dcaefddb706",
+            "issued": "2019-03-29",
+            "keyword": [
+                "cfda 64 101"
+            ],
+            "landingPage": "https://www.data.va.gov/d/ezz5-cnqv",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Use of Benefits and Services"
-            ]
+            ],
+            "title": "USA SPENDING C&P BURIAL B101 VETERANS CEMETARY GRANTS PROGRAM NOV2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/f2az-8wb5",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2019-06-10",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-03",
-            "keyword": [
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "NCVAS Mailbox",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "c3b3794d-13a2-4d0a-8bc3-6863e6828d15",
+            "dataQuality": true,
             "description": "<p>Number of Veteran Patients by Healthcare Priority Group: FY2000 to FY2018</p>",
-            "title": "Number of Veteran Patients by Healthcare Priority Group: FY2000 to FY2018",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40814,22 +40799,49 @@
                     "mediaType": "application/vnd.ms-excel"
                 }
             ],
+            "identifier": "c3b3794d-13a2-4d0a-8bc3-6863e6828d15",
+            "issued": "2019-06-10",
+            "keyword": [
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/f2az-8wb5",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "dataQuality": true
+            "modified": "2020-11-03",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Number of Veteran Patients by Healthcare Priority Group: FY2000 to FY2018"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "accrualPeriodicity": "R/P2M",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2015-09-15T04:00:00Z/2015-09-15T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/health/access-audit.asp"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/access-audit.asp",
+            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR30_092015_Pending_and_EWL_Biweekly_Desired_Date_Division_PDFReady.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Pending Appointments 15 September 2015"
+                }
             ],
+            "identifier": "VA-VHA-OIA-424",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -40843,101 +40855,72 @@
                 "wait list",
                 "wait time"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:041"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-OIA-424",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 September 15",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR30_092015_Pending_and_EWL_Biweekly_Desired_Date_Division_PDFReady.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Pending Appointments 15 September 2015"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2015-09-15T04:00:00Z/2015-09-15T04:00:00Z",
             "theme": [
                 "Accelerating Access",
                 "Pending Appointments"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 September 15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/f3au-3njd",
-            "issued": "2021-08-27",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-07",
-            "keyword": [
-                "district of columbia",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VANCVAS",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/f3au-3njd",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_District of Columbia",
+            "identifier": "https://www.data.va.gov/api/views/f3au-3njd",
+            "issued": "2021-08-27",
+            "keyword": [
+                "district of columbia",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/f3au-3njd",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-07",
             "programCode": [
                 "029:086"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summaries_District of Columbia"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/f3d9-rfxv",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "missouri",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tom Garin",
                 "hasEmail": "mailto:Tom.Garin@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-112",
             "description": "<p>This is a summary of the programs and services provided by VA in Missouri in fiscal year 2014.</p>",
-            "title": "State Summary:  Missouri",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -40946,55 +40929,48 @@
                     "title": "State Summary:  Missouri"
                 }
             ],
+            "identifier": "VA-OEI-OEI-112",
+            "issued": "2017-07-26",
+            "keyword": [
+                "missouri",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/f3d9-rfxv",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "State Summary:  Missouri"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/f3mc-6dun",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2007-10-01T04:00:00Z/2008-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf"
-            ],
-            "keyword": [
-                "health",
-                "healthcare",
-                "hospital accreditation",
-                "patient safety",
-                "quality of care",
-                "satisfaction",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VHA Open Data",
                 "hasEmail": "mailto:vhaopendata@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VHA-OIA-026",
-            "description": "<p>Report to the Appropriations Committee of the United States House of Representatives in Response to Conference Committee Report to PL 110-186.  In an effort to provide a snapshot of the quality of care provided at VA health care facilities, this report includes information about waiting times, staffing level, infection rates, surgical volumes, quality measures, patient satisfaction, service availability and complexity, accreditation status, and patient safety. The data in this report have been drawn from multiple sources across VHA.  This dataset identifies whether the facility has Joint Commission Accrediation and/or CARF Accreditation.</p>",
-            "title": "Veterans Health Administration 2008 Hospital Report Card - Hospital Accreditation",
-            "isPartOf": "VA-VHA-OIA-583",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "029:040"
-            ],
+            "description": "<p>Report to the Appropriations Committee of the United States House of Representatives in Response to Conference Committee Report to PL 110-186.  In an effort to provide a snapshot of the quality of care provided at VA health care facilities, this report includes information about waiting times, staffing level, infection rates, surgical volumes, quality measures, patient satisfaction, service availability and complexity, accreditation status, and patient safety. The data in this report have been drawn from multiple sources across VHA.  This dataset identifies whether the facility has Joint Commission Accrediation and/or CARF Accreditation.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41002,68 +40978,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/f3mc-6dun/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/f3mc-6dun/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/f3mc-6dun/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/f3mc-6dun/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/f3mc-6dun/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/f3mc-6dun/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/f3mc-6dun/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/f3mc-6dun/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/f3mc-6dun/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "describedBy": "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf",
-            "dataQuality": true,
+            "identifier": "VA-VHA-OIA-026",
+            "isPartOf": "VA-VHA-OIA-583",
+            "issued": "2017-07-26",
+            "keyword": [
+                "health",
+                "healthcare",
+                "hospital accreditation",
+                "patient safety",
+                "quality of care",
+                "satisfaction",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/f3mc-6dun",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:040"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "references": [
+                "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf"
+            ],
+            "temporal": "2007-10-01T04:00:00Z/2008-09-30T04:00:00Z",
             "theme": [
                 "Section 3. Health and Nutrition"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Veterans Health Administration 2008 Hospital Report Card - Hospital Accreditation"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/f43c-vb9n",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2024-09-09",
-            "@type": "dcat:Dataset",
-            "modified": "2024-09-09",
-            "keyword": [
-                "veteran population",
-                "veterans",
-                "vetpop",
-                "vetpop2023"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:VANCVAS@VA.GOV"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/f43c-vb9n",
             "description": "VetPop2023 projection of living Veterans by gender and 5-year age groups at the state level. \n\nNote: Rounding to the nearest 1,000 is always appropriate for VetPop estimates.",
-            "title": "VetPop2023 State Data, 6L",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41071,42 +41052,73 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/f43c-vb9n/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/f43c-vb9n/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/f43c-vb9n/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/f43c-vb9n/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/f43c-vb9n/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/f43c-vb9n/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/f43c-vb9n/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/f43c-vb9n/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/f43c-vb9n/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/f43c-vb9n",
+            "issued": "2024-09-09",
+            "keyword": [
+                "veteran population",
+                "veterans",
+                "vetpop",
+                "vetpop2023"
+            ],
+            "landingPage": "https://www.data.va.gov/d/f43c-vb9n",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-09-09",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "VetPop2023 State Data, 6L"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "accrualPeriodicity": "R/P2M",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2015-10-15T04:00:00Z/2015-10-15T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/health/access-audit.asp"
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VHA Open Data",
+                "hasEmail": "mailto:vhaopendata@va.gov"
+            },
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/health/access-audit.asp",
+            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR32_102015_Pending_and_EWL_Biweekly_Desired_Date_Division_PDFReady.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "Pending Appointments 15 October 2015"
+                }
             ],
+            "identifier": "VA-VHA-OIA-427",
+            "isPartOf": "VA-VHA-OIA-073",
+            "issued": "2017-07-26",
             "keyword": [
                 "access",
                 "appointment",
@@ -41120,76 +41132,44 @@
                 "wait list",
                 "wait time"
             ],
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "VHA Open Data",
-                "hasEmail": "mailto:vhaopendata@va.gov"
-            },
+            "landingPage": "https://www.va.gov/health/access-audit.asp",
+            "language": [
+                "en-US"
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:041"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Department of Veterans Affairs"
             },
-            "identifier": "VA-VHA-OIA-427",
-            "description": "<p>VA is posting regular data updates showing progress on its efforts to accelerate access to quality health care for Veterans who have been waiting for appointments. These access data updates will be posted at the middle and end of each month at VA.gov. The facility-level data show the current status of VA's: 1) New Enrollee Appointment Request (NEAR) List: The total number of newly enrolled Veterans that have asked for an appointment during the enrollment process.  Out of an abundance of caution, VA reviewed the NEAR data from the past decade to identify any individual who:  has enrolled for care since the inception of enrollment,  indicated they desired an appointment on the enrollment form, and has not yet had a scheduled appointment in the VHA health care system. 2) Electronic Wait List (EWL) Count: The total number of all new patients (those who have not been seen in the specific clinic in the previous 24 months) for whom appointments cannot be scheduled in 90 days or less; and 3) Total Appointments Scheduled: Every appointment scheduled at the facility except surgery and medical procedures.  The term 'pending' has replaced the term 'prospective,' which predicts the availability of scheduled appointments in the future for new Veterans on a given date, and the term 'completed' replaced the term 'retrospective,' which indicates when appointments actually occurred.</p>",
-            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 October 15",
-            "isPartOf": "VA-VHA-OIA-073",
-            "programCode": [
-                "029:041"
-            ],
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "downloadURL": "https://www.va.gov/HEALTH/docs/DR32_102015_Pending_and_EWL_Biweekly_Desired_Date_Division_PDFReady.pdf",
-                    "mediaType": "application/pdf",
-                    "title": "Pending Appointments 15 October 2015"
-                }
+            "references": [
+                "https://www.va.gov/health/access-audit.asp"
             ],
-            "describedBy": "https://www.va.gov/health/access-audit.asp",
             "systemOfRecords": "https://www.gpo.gov/fdsys/pkg/FR-2012-05-11/pdf/2012-11487.pdf",
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P2M",
+            "temporal": "2015-10-15T04:00:00Z/2015-10-15T04:00:00Z",
             "theme": [
                 "Accelerating Access",
                 "Pending Appointments"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Accelerating Access to Care Initiative Pending Appointments - Report 2015 October 15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-02",
-            "keyword": [
-                "abr",
-                "abr2012",
-                "compensation benefits fy12",
-                "dic benefits",
-                "vba benefits"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Elwell",
                 "hasEmail": "mailto:thomas.elwell@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-ABR2012-009",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Children Receiving DIC by Age at the End of FY2012",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41197,77 +41177,77 @@
                     "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-009",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "abr",
+                "abr2012",
+                "compensation benefits fy12",
+                "dic benefits",
+                "vba benefits"
+            ],
+            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2022-03-02",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "ABR Reports"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Children Receiving DIC by Age at the End of FY2012"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/f5wf-ycrb",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-08-08",
-            "keyword": [
-                "south carolina",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VANCVAS",
                 "hasEmail": "mailto:VANCVAS@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/f5wf-ycrb",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_South Carolina",
+            "identifier": "https://www.data.va.gov/api/views/f5wf-ycrb",
+            "issued": "2021-08-26",
+            "keyword": [
+                "south carolina",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/f5wf-ycrb",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-08-08",
             "programCode": [
                 "029:086"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summaries_South Carolina"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/f6q6-hh5x",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2020-11-10",
-            "@type": "dcat:Dataset",
-            "modified": "2021-01-04",
-            "keyword": [
-                "covid-19",
-                "crowdsourcing",
-                "data science challenges",
-                "electronic health record",
-                "precisionfda"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Amanda Purnell",
                 "hasEmail": "mailto:amanda.purnell@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/f6q6-hh5x",
             "description": "The dataset is a synthetic cohort for use for the VHA Innovation Ecosystem and precisionFDA COVID-19 Risk Factor Modeling Challenge. The dataset was generated using Synthea, a tool created by MITRE to generate synthetic electronic health records (EHRs) from curated care maps and publicly available statistics. This dataset represents 147,451 patients developed using the COVID-19 module. The dataset format conforms to the CSV file outputs. Below are links to all relevant information.\n\nPrecisionFDA Challenge: https://precision.fda.gov/challenges/11\nSynthea hompage: https://synthetichealth.github.io/synthea/\nSynethea GitHub repository: https://github.com/synthetichealth/synthea\nSynthea COVID-19 Module publication: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7531559/\nCSV File Format Data Dictionary: https://github.com/synthetichealth/synthea/wiki/CSV-File-Data-Dictionary",
-            "title": "Synthetic Cohort for VHA Innovation Ecosystem and precisionFDA COVID-19 Risk Factor Modeling Challenge",
-            "programCode": [
-                "029:048"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41275,37 +41255,42 @@
                     "mediaType": "application/zip"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/f6q6-hh5x",
+            "issued": "2020-11-10",
+            "keyword": [
+                "covid-19",
+                "crowdsourcing",
+                "data science challenges",
+                "electronic health record",
+                "precisionfda"
+            ],
+            "landingPage": "https://www.data.va.gov/d/f6q6-hh5x",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2021-01-04",
+            "programCode": [
+                "029:048"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "Synthetic Cohort for VHA Innovation Ecosystem and precisionFDA COVID-19 Risk Factor Modeling Challenge"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/f6vj-xedj",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-12",
-            "@type": "dcat:Dataset",
-            "modified": "2020-11-12",
-            "keyword": [
-                "rural veterans",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Tamara Lee",
                 "hasEmail": "mailto:tamara.lee@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "8da70b14-46af-4d4d-a71b-e51968225d46",
-            "description": "<p>This spreadsheet contains data from the 2015 American Community Survey and shows a select subset of demographic and socioeconomic characteristics of Veterans and non-Veterans by state. The spreadsheet includes variables like:  raw numbers, unemployment rate, disability rate, median personal income, age groups, period of service and other variables.</p>",
-            "title": "Veteran Farmer Data by State (2015)",
+            "dataQuality": true,
+            "describedBy": "https://www.va.gov/data/VAOpenDataMigration2019/Data-Dictionary-Apps-for-Ag.pdf",
             "describedByType": "application/pdf",
-            "programCode": [
-                "029:086"
-            ],
+            "description": "<p>This spreadsheet contains data from the 2015 American Community Survey and shows a select subset of demographic and socioeconomic characteristics of Veterans and non-Veterans by state. The spreadsheet includes variables like:  raw numbers, unemployment rate, disability rate, median personal income, age groups, period of service and other variables.</p>",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41313,42 +41298,40 @@
                     "mediaType": "application/pdf"
                 }
             ],
-            "describedBy": "https://www.va.gov/data/VAOpenDataMigration2019/Data-Dictionary-Apps-for-Ag.pdf",
-            "dataQuality": true,
+            "identifier": "8da70b14-46af-4d4d-a71b-e51968225d46",
+            "issued": "2017-07-12",
+            "keyword": [
+                "rural veterans",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/f6vj-xedj",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-11-12",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Demographics"
-            ]
+            ],
+            "title": "Veteran Farmer Data by State (2015)"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.data.va.gov/d/f75g-za88",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2017-11-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "emis",
-                "military"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Bret Meyer",
                 "hasEmail": "mailto:bret.meyer@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-ORCH-10",
+            "dataQuality": true,
             "description": "<p>The service is the authoritative service for a veteran's military service record and the coordination point for updates and corrections between the DoD and VA.</p>",
-            "title": "Enterprise Military Information Service (eMIS) Military Information Service",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41357,66 +41340,70 @@
                     "title": "Enterprise Military Information Service (eMIS) Military Information Service"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "identifier": "VA-ORCH-10",
+            "issued": "2017-11-17",
+            "keyword": [
+                "emis",
+                "military"
+            ],
+            "landingPage": "https://www.data.va.gov/d/f75g-za88",
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
+            "title": "Enterprise Military Information Service (eMIS) Military Information Service"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/f8id-9phi",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-06",
-            "keyword": [
-                "colorado",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VANCVAS",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/f8id-9phi",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Colorado",
+            "identifier": "https://www.data.va.gov/api/views/f8id-9phi",
+            "issued": "2021-08-26",
+            "keyword": [
+                "colorado",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/f8id-9phi",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-06",
             "programCode": [
                 "029:086"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summaries_Colorado"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/fbbn-zqhd",
-            "issued": "2023-06-13",
-            "@type": "dcat:Dataset",
-            "modified": "2024-08-26",
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "National Center for Veterans Analysis and Statistics",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/fbbn-zqhd",
             "description": "This dataset is comprised of 1-year estimate data from the American Community Survey published as of 2021.",
-            "title": "FY 2021_NCVAS Population Data For State Summaries",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41424,56 +41411,53 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/fbbn-zqhd/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/fbbn-zqhd/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/fbbn-zqhd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/fbbn-zqhd/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/fbbn-zqhd/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/fbbn-zqhd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/fbbn-zqhd/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/fbbn-zqhd/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/fbbn-zqhd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "identifier": "https://www.data.va.gov/api/views/fbbn-zqhd",
+            "issued": "2023-06-13",
+            "landingPage": "https://www.data.va.gov/d/fbbn-zqhd",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2024-08-26",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "FY 2021_NCVAS Population Data For State Summaries"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/fbdb-eurg",
             "bureauCode": [
                 "029:00"
             ],
-            "issued": "2017-07-26",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "wyoming"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "DG&amp;A Mailgroup",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-OEI-OEI-222",
             "description": "<p>This summary describes the programs and services VA provided in Wyoming in fiscal year 2015.</p>",
-            "title": "State Summary: Wyoming FY15",
-            "programCode": [
-                "029:086"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41482,43 +41466,41 @@
                     "title": "Wyoming"
                 }
             ],
+            "identifier": "VA-OEI-OEI-222",
+            "issued": "2017-07-26",
+            "keyword": [
+                "wyoming"
+            ],
+            "landingPage": "https://www.data.va.gov/d/fbdb-eurg",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:086"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "State Summary: Wyoming FY15"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "restricted public",
-            "landingPage": "https://www.data.va.gov/d/fbdg-7vgd",
             "bureauCode": [
                 "029:40"
             ],
-            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
-            "issued": "2017-11-17",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "healthcare",
-                "notes",
-                "tiu"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Clark Timmins",
                 "hasEmail": "mailto:clark.timmins@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VIA-10",
+            "dataQuality": true,
             "description": "<p>This Service allows the creation of addenda to TIU Documents, and save and sign a note for an encounter at a VistA site.</p>",
-            "title": "TiuNotes",
-            "programCode": [
-                "029:000"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41527,75 +41509,73 @@
                     "title": "TiuNotes"
                 }
             ],
-            "dataQuality": true,
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "identifier": "VA-VIA-10",
+            "issued": "2017-11-17",
+            "keyword": [
+                "healthcare",
+                "notes",
+                "tiu"
+            ],
+            "landingPage": "https://www.data.va.gov/d/fbdg-7vgd",
             "language": [
                 "en-US"
-            ]
+            ],
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "rights": "Protected by Privacy Act and/or Health Insurance Portability and Accountability Act",
+            "title": "TiuNotes"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
             "bureauCode": [
                 "029:00"
             ],
-            "landingPage": "https://www.data.va.gov/d/fbhj-bg8n",
-            "issued": "2021-08-26",
-            "@type": "dcat:Dataset",
-            "modified": "2023-06-08",
-            "keyword": [
-                "kentucky",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VANCVAS",
                 "hasEmail": "mailto:vancvas@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/fbhj-bg8n",
             "description": "VA State Summary Reports are produced using data from the National Center for Veterans Analysis and Statistics and provide a comprehensive overview of Veterans in each U.S. State.  We also use data from the Census Bureau, DoD, and IPUMS. Guam and Puerto Rico summaries are produced, but no other territories.",
-            "title": "State Summaries_Kentucky",
+            "identifier": "https://www.data.va.gov/api/views/fbhj-bg8n",
+            "issued": "2021-08-26",
+            "keyword": [
+                "kentucky",
+                "veterans"
+            ],
+            "landingPage": "https://www.data.va.gov/d/fbhj-bg8n",
+            "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2023-06-08",
             "programCode": [
                 "029:086"
             ],
-            "license": "https://creativecommons.org/publicdomain/zero/1.0/"
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "title": "State Summaries_Kentucky"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:25"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2022-03-08",
-            "keyword": [
-                "abr",
-                "abr2012",
-                "insurance",
-                "insurance benefits fy12",
-                "vba benefits"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Thomas Elwell",
                 "hasEmail": "mailto:thomas.elwell@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VBA-ABR2012-068",
+            "dataQuality": true,
             "description": "<p>The Annual Benefits Report (ABR) clearly summarizes the benefit programs delivered by VBA identifies the current level of program participation by eligible persons, and profiles the beneficiaries.</p>",
-            "title": "Insurance Death Awards (Amount) by Fiscal Year",
-            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
-            "programCode": [
-                "029:003"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41604,46 +41584,48 @@
                     "title": "Insurance Death Awards (Amount) by Fiscal Year"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "VA-VBA-ABR2012-068",
+            "isPartOf": "VA-VBA-MASTER-2012ABR-001",
+            "issued": "2017-07-26",
+            "keyword": [
+                "abr",
+                "abr2012",
+                "insurance",
+                "insurance benefits fy12",
+                "vba benefits"
+            ],
+            "landingPage": "https://www.benefits.va.gov/REPORTS/abr_archive.asp",
+            "language": [
+                "en-US"
+            ],
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
-            "accrualPeriodicity": "R/P1Y",
+            "modified": "2022-03-08",
+            "programCode": [
+                "029:003"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
+            "temporal": "2011-10-01T04:00:00Z/2012-09-30T04:00:00Z",
             "theme": [
                 "ABR Reports"
             ],
-            "language": [
-                "en-US"
-            ]
+            "title": "Insurance Death Awards (Amount) by Fiscal Year"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/fcxt-zc8r",
             "bureauCode": [
                 "029:40"
             ],
-            "issued": "2017-01-24",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "keyword": [
-                "cemetaries",
-                "map",
-                "statistics"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Vicki Cordes",
                 "hasEmail": "mailto:noemailprovided@usa.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "https://www.data.va.gov/api/views/fcxt-zc8r",
+            "dataQuality": true,
             "description": "<p>Data assets for <a href=\"https://www.data.va.gov/story/national-cemetery-administration\">https://www.data.va.gov/story/national-cemetery-administration</a>.</p>",
-            "title": "VA National Cemetery Sites",
-            "isPartOf": "8ea07f95-2a7f-494d-a275-5420bcd938fb",
-            "programCode": [
-                "029:001"
-            ],
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
@@ -41651,74 +41633,68 @@
                     "mediaType": "text/csv"
                 },
                 {
-                    "mediaType": "application/rdf+xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/fcxt-zc8r/rows.rdf?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/fcxt-zc8r/columns.rdf",
                     "describedByType": "application/rdf+xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/fcxt-zc8r/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
                 },
                 {
-                    "mediaType": "application/json",
-                    "downloadURL": "https://www.data.va.gov/api/views/fcxt-zc8r/rows.json?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/fcxt-zc8r/columns.json",
                     "describedByType": "application/json",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/fcxt-zc8r/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
                 },
                 {
-                    "mediaType": "application/xml",
-                    "downloadURL": "https://www.data.va.gov/api/views/fcxt-zc8r/rows.xml?accessType=DOWNLOAD",
+                    "@type": "dcat:Distribution",
                     "describedBy": "https://www.data.va.gov/api/views/fcxt-zc8r/columns.xml",
                     "describedByType": "application/xml",
-                    "@type": "dcat:Distribution"
+                    "downloadURL": "https://www.data.va.gov/api/views/fcxt-zc8r/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
                 }
             ],
-            "dataQuality": true,
+            "identifier": "https://www.data.va.gov/api/views/fcxt-zc8r",
+            "isPartOf": "8ea07f95-2a7f-494d-a275-5420bcd938fb",
+            "issued": "2017-01-24",
+            "keyword": [
+                "cemetaries",
+                "map",
+                "statistics"
+            ],
+            "landingPage": "https://www.data.va.gov/d/fcxt-zc8r",
             "license": "https://creativecommons.org/publicdomain/zero/1.0/",
+            "modified": "2020-05-15",
+            "programCode": [
+                "029:001"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Veterans Affairs"
+            },
             "theme": [
                 "Basic Statistics",
                 "Use",
                 "and Operational Data"
-            ]
+            ],
+            "title": "VA National Cemetery Sites"
         },
         {
+            "@type": "dcat:Dataset",
             "accessLevel": "public",
-            "landingPage": "https://www.data.va.gov/d/fd22-twij",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "029:15"
             ],
-            "issued": "2017-07-26",
-            "temporal": "2007-10-01T04:00:00Z/2008-09-30T04:00:00Z",
-            "@type": "dcat:Dataset",
-            "modified": "2020-05-15",
-            "references": [
-                "https://www.va.gov/health/docs/Hospital_Quality_Report.pdf"
-            ],
-            "keyword": [
-                "health",
-                "healthcare",
-                "hospital accreditation",
-                "patient safety",
-                "quality of care",
-                "satisfaction",
-                "veterans"
-            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "VHA Open Data",
                 "hasEmail": "mailto:vhaopendata@va.gov"
             },
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Department of Veterans Affairs"
-            },
-            "identifier": "VA-VHA-OIA-027",
```

