# Change History for dhs.json

### Changes from 31606f9 to dd2190f (Part 1/3)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
diff --git a/dhs.json b/dhs.json
index 7c6d508..07f6450 100644
--- a/dhs.json
+++ b/dhs.json
@@ -3,42 +3,51 @@
     "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
     "dataset": [
         {
-            "title": "COVID-19 Passenger Throughput",
+            "accessLevel": "public",
+            "bureauCode": [
+                "024:056"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
             "description": "Since the beginning of the COVID-19 pandemic, TSA has published the daily passenger checkpoint throughput numbers along with the prior two-year comparison on the public-facing TSA.gov website. It is intended to show the pandemic's impact on air travel.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.tsa.gov/coronavirus/passenger-throughput"
+                }
+            ],
+            "identifier": "TSA-1ebecc72-746a-4a36-b278-b3e5e31dc9cc",
             "keyword": [
                 "Airport",
                 "Passenger Throughput"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-22T12:25:27-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "TSA.GOV Public Website"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "COVID-19 Passenger Throughput"
         },
-            "identifier": "TSA-1ebecc72-746a-4a36-b278-b3e5e31dc9cc",
+        {
             "accessLevel": "public",
             "bureauCode": [
-                "024:056"
-            ],
-            "programCode": [
-                "024:000"
+                "024:070"
             ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.tsa.gov/coronavirus/passenger-throughput"
-                }
-            ]
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "USFA NFIRS 2008 Basic Fire Incident Data",
             "description": "The 2008 US Fire Administration Fire (USFA) Fire Incident & Cause Data was provided by the U.S. Fire Administration's (USFA) National Fire Data Center's (NFDC's) National Fire Incident Reporting System has numerous data elements that detail fire incidents for example  the fire department  fire incident  the occupants  structure and equipment used  hazard material involved and casualty details.",
+            "identifier": "FEMA-01818",
             "keyword": [
                 "Announcement",
                 "Broadcast",
@@ -51,30 +60,30 @@
                 "Reporting System",
                 "Statement"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-29T14:00:03-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "USFA NFIRS 2008 Basic Fire Incident Data"
         },
-            "identifier": "FEMA-01818",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "USFA NFIRS 2009 Basic Fire Incident Data",
             "description": "The 2009 US Fire Administration Fire (USFA) Fire Incident & Cause Data was provided by the U.S. Fire Administration's (USFA) National Fire Data Center's (NFDC's) National Fire Incident Reporting System has numerous data elements that detail fire incidents for example  the fire department  fire incident  the occupants  structure and equipment used  hazard material involved and casualty details.",
+            "identifier": "FEMA-01819",
             "keyword": [
                 "Announcement",
                 "Broadcast",
@@ -87,30 +96,30 @@
                 "Reporting System",
                 "Statement"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-29T14:00:03-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "USFA NFIRS 2009 Basic Fire Incident Data"
         },
-            "identifier": "FEMA-01819",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "USFA NFIRS 2010 Fire Incident & Cause Data",
             "description": "NFIRS has two objectives to help State and local governments develop fire reporting and analysis capability for their own use  and to obtain data that can be used to more accurately assess and subsequently combat the fire problem at a national level.",
+            "identifier": "FEMA-02236",
             "keyword": [
                 "Communication",
                 "Announcement",
@@ -126,30 +135,30 @@
                 "Incident",
                 "Occurrence Type"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-29T14:00:03-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "USFA NFIRS 2010 Fire Incident & Cause Data"
         },
-            "identifier": "FEMA-02236",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "USFA NFIRS 2011 Fire Incident & Cause Data",
             "description": "National Fire Incident Reporting System has numerous data elements that detail fire incidents for example  the fire department  fire incident  the occupants  structure and equipment used  hazard material involved and casualty details.",
+            "identifier": "FEMA-02237",
             "keyword": [
                 "Communication",
                 "Announcement",
@@ -165,30 +174,30 @@
                 "Incident",
                 "Occurrence Type"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-29T14:00:03-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "USFA NFIRS 2011 Fire Incident & Cause Data"
         },
-            "identifier": "FEMA-02237",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "USFA NFIRS 2013 Fire Incident & Cause Data",
             "description": "The 2013 Fire Causes & Incident data was provided by the U.S. Fire Administration-s (USFA) National Fire Data Center-s (NFDC-s) National Fire Incident Reporting System. The National Fire Incident Reporting System (NFIRS) is a reporting standard that fire departments use to uniformly report on the full range of their activities  from fire to emergency medical services (EMS) to equipment involved in the response. NFIRS is the world-s largest  national  annual database of fire incident information  and comprises about 75 percent of all reported fires that occur annually. NFIRS is a voluntary tool",
+            "identifier": "FEMA-02238",
             "keyword": [
                 "Communication",
                 "Announcement",
@@ -203,30 +212,30 @@
                 "Statement",
                 "Incident"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-29T14:00:03-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "USFA NFIRS 2013 Fire Incident & Cause Data"
         },
-            "identifier": "FEMA-02238",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Daily Public Assistance Grants Award Activity",
             "description": "Daily activity of Public Assistance Grant Awards  including FEMA Region  State  Disaster Declaration Number  Event description  Mission Assigned agency  Assistance Requested  Obligated Federal dollars  and Date of Obligation as required by HR152 - Sandy Recovery Improvement Act of 2013.",
+            "identifier": "FEMA-01686",
             "keyword": [
                 "Account",
                 "Activity",
@@ -275,30 +284,30 @@
                 "Sole",
                 "Spot"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-29T14:00:03-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Daily Public Assistance Grants Award Activity"
         },
-            "identifier": "FEMA-01686",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "FEMA Archived Registration Intake and Individuals and Households Program Data",
             "description": "Contains aggregated  non-PII data generated by FEMA-s Enterprise Coordination & Information Management (ECIM) Reporting team to share archived data on registrations and Individuals and Households Program (IHP)  for archived declarations starting with declaration number 1539 segmented by city where registration is valid. Additional core data elements include: valid call center registrations  valid web registrations  valid mobile registrations  IHP eligible  IHP amount  Housing Assistance (HA) referrals  HA eligible  HA amount  Other Needs Assistance (ONA) eligible  and ONA amount.",
+            "identifier": "FEMA-02318",
             "keyword": [
                 "Event",
                 "Occurrence",
@@ -316,30 +325,30 @@
                 "Benefit Type",
                 "Disaster Assistance Type"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-29T14:00:03-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "FEMA Archived Registration Intake and Individuals and Households Program Data"
         },
-            "identifier": "FEMA-02318",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "FEMA Grants Program Directorate - Preparedness (Non-Disaster) and Assistance to Firefighter Grants",
             "description": "The Grant Programs Directorate (GPD) strategically and effectively administers and manages FEMA grants to ensure critical and measurable results for customers and stakeholders. The grants represented in this data reflect two sets of grants: Preparedness Non-Disaster (ND) and Assistance to Firefighter Grants (AFG).  ND and AFG are awarded and managed differently within GPD and should be treated with discretion. The only measure in this data set is Award Amount. It is an additive measure that can be applied across multiple dimensions to create various views of the data.",
+            "identifier": "FEMA-01687",
             "keyword": [
                 "Account",
                 "Activity",
@@ -388,30 +397,30 @@
                 "Sole",
                 "Spot"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-29T14:00:03-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "FEMA Grants Program Directorate - Preparedness (Non-Disaster) and Assistance to Firefighter Grants"
         },
-            "identifier": "FEMA-01687",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "FEMA Individual and Households Program (IHP) Flood Damage",
             "description": "This-dataset contains aggregated  non-PII data from FEMA-s Recovery Directorate to share data on registrations and Individuals and Households Program (IHP).",
+            "identifier": "FEMA-07618",
             "keyword": [
                 "Event",
                 "Occurrence",
@@ -422,30 +431,30 @@
                 "Aid",
                 "Benefit"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-29T14:00:03-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "FEMA Individual and Households Program (IHP) Flood Damage"
         },
-            "identifier": "FEMA-07618",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "FEMA Individual Assistance Open Disaster Statistics",
             "description": "Individual Assistance (IA) is provided by the Federal Emergency Management Agency to individuals and families who have sustained losses due to disasters. Homeowners  renters and business owners in designated counties who sustained damage to their homes  vehicles  personal property  businesses or inventory as a result of a federally declared disaster may apply for disaster assistance. Disaster assistance may include grants to help pay for temporary housing  emergency home repairs  uninsured and underinsured personal property losses  and medical dental and funeral expenses caused by the disaster",
+            "identifier": "FEMA-07616",
             "keyword": [
                 "Account",
                 "Assignment",
@@ -463,30 +472,30 @@
                 "Benefit Type",
                 "Attain"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-29T14:00:03-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "FEMA Individual Assistance Open Disaster Statistics"
         },
-            "identifier": "FEMA-07616",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "FEMA Public Assistance Applicants - API",
             "description": "This dataset lists summarized Applicant (sub-grantee) information that supplements the Public Assistance Funded Projects Detail dataset.",
+            "identifier": "FEMA-04396",
             "keyword": [
                 "Group",
                 "Organization",
@@ -501,30 +510,30 @@
                 "Geographic Area",
                 "Organization Role"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-29T14:00:03-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "FEMA Public Assistance Applicants - API"
         },
-            "identifier": "FEMA-04396",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "FEMA Registration Intake and Individuals and Households (RI-IHP) Program Data",
             "description": "This dataset contains aggregated  non-PII data generated by FEMA-s Enterprise Coordination & Information Management (ECIM) Reporting team to share data on Registrations and Individuals and Households Program (IHP) where registration for disaster is valid. Segmented by zip-code additional core data elements include: valid call center registrations  valid web registrations  valid mobile registrations  IHP eligible  IHP amount  Housing Assistance (HA) referrals  HA eligible  HA amount  Other Needs Assistance (ONA) eligible  and ONA amount.",
+            "identifier": "FEMA-02319",
             "keyword": [
                 "Occurrence",
                 "Incident",
@@ -539,58 +548,58 @@
                 "Benefit",
                 "Benefit Type"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-29T14:00:03-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "FEMA Registration Intake and Individuals and Households (RI-IHP) Program Data"
         },
-            "identifier": "FEMA-02319",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "FEMA Registration Intake and Individuals Household Program - API",
             "description": "The dataset is composed of Registration Intake and Individuals and Households Program (IHP) Information from the Individual Assistance (IA) reporting authority where registration is valid.This dataset contains aggregated  non-PII data by generated FEMA's ECIM (Enterprise Coordination & Information Management) Reporting team to share data on registrations and Individuals and Households Program (IHP) for Hurricane Sandy  segmented by city for the state of New Jersey AND New York where registration is valid.",
+            "identifier": "FEMA-02196",
             "keyword": [
                 "Individual Registrant",
                 "Disaster Assistance Type"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-29T14:00:03-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "FEMA Registration Intake and Individuals Household Program - API"
         },
-            "identifier": "FEMA-02196",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "National Fire Incident Reporting System (NFIRS)",
             "description": "The National Fire Incident Reporting System (NFIRS) is a reporting standard that fire departments use to uniformly report on the full range of their activities  from fire to emergency medical services (EMS) to equipment involved in the response.",
+            "identifier": "FEMA-02257",
             "keyword": [
                 "Communication",
                 "Announcement",
@@ -612,84 +621,84 @@
                 "Amount",
                 "Declaration"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-29T14:00:03-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "National Fire Incident Reporting System (NFIRS)"
         },
-            "identifier": "FEMA-02257",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "OpenFEMA Dataset Fields - API",
             "description": "The dataset lists the fields for each of the published data sets available via the OpenFEMA APIs",
+            "identifier": "FEMA-02197",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-29T14:00:03-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "OpenFEMA Dataset Fields - API"
         },
-            "identifier": "FEMA-02197",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "OpenFEMA Datasets - API",
             "description": "The dataset lists the published datasets available via FEMA's - API",
+            "identifier": "FEMA-02198",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-29T14:00:03-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "OpenFEMA Datasets - API"
         },
-            "identifier": "FEMA-02198",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Residential Fire Fatalities in the News",
             "description": "Information on residential fire fatalities compiled through a daily Internet search (Monday-Friday) of U.S. news media reports.",
+            "identifier": "FEMA-00938",
             "keyword": [
                 "Communication",
                 "Announcement",
@@ -711,30 +720,30 @@
                 "Amount",
                 "Declaration"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-29T14:00:03-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Residential Fire Fatalities in the News"
         },
-            "identifier": "FEMA-00938",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "US Fire Administration Fire Statistics",
             "description": "The U.S. Fire Administration collects data from a variety of sources to provide information and analyses on the status and scope of the fire problem in the United States. We use these data to highlight current and emerging trends in fires  including what causes fires  where they occur  and who is impacted the most by fire. We also analyze the circumstances surrounding on-duty firefighter casualties to help identify approaches that can reduce the number of deaths and injuries in future years.",
+            "identifier": "FEMA-02256",
             "keyword": [
                 "Communication",
                 "Event",
@@ -743,30 +752,30 @@
                 "Incident",
                 "Incident Type"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-29T14:00:03-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "US Fire Administration Fire Statistics"
         },
-            "identifier": "FEMA-02256",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "USFA NFIRS 1999 Basic Fire Incident Data",
             "description": "The 1999 US Fire Administration Fire (USFA) Fire Incident & Cause Data was provided by the U.S. Fire Administration's (USFA) National Fire Data Center's (NFDC's) National Fire Incident Reporting System has numerous data elements that detail fire incidents for example  the fire department  fire incident  the occupants  structure and equipment used  hazard material involved and casualty details.",
+            "identifier": "FEMA-01806",
             "keyword": [
                 "Announcement",
                 "Broadcast",
@@ -779,30 +788,30 @@
                 "Reporting System",
                 "Statement"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-29T14:00:03-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "USFA NFIRS 1999 Basic Fire Incident Data"
         },
-            "identifier": "FEMA-01806",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "USFA NFIRS 2000 Basic Fire Incident Data",
             "description": "The 2000 US Fire Administration Fire (USFA) Fire Incident & Cause Data was provided by the U.S. Fire Administration's (USFA) National Fire Data Center's (NFDC's) National Fire Incident Reporting System has numerous data elements that detail fire incidents for example  the fire department  fire incident  the occupants  structure and equipment used  hazard material involved and casualty details.",
+            "identifier": "FEMA-01807",
             "keyword": [
                 "Announcement",
                 "Broadcast",
@@ -815,30 +824,30 @@
                 "Reporting System",
                 "Statement"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-29T14:00:03-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "USFA NFIRS 2000 Basic Fire Incident Data"
         },
-            "identifier": "FEMA-01807",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "USFA NFIRS 2001 Basic Fire Incident Data",
             "description": "The 2001 US Fire Administration Fire (USFA) Fire Incident & Cause Data was provided by the U.S. Fire Administration's (USFA) National Fire Data Center's (NFDC's) National Fire Incident Reporting System has numerous data elements that detail fire incidents for example  the fire department  fire incident  the occupants  structure and equipment used  hazard material involved and casualty details.",
+            "identifier": "FEMA-01808",
             "keyword": [
                 "Announcement",
                 "Broadcast",
@@ -851,30 +860,30 @@
                 "Reporting System",
                 "Statement"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-29T14:00:03-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "USFA NFIRS 2001 Basic Fire Incident Data"
         },
-            "identifier": "FEMA-01808",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "USFA NFIRS 2002 Basic Fire Incident Data",
             "description": "The 2002 US Fire Administration Fire (USFA) Fire Incident & Cause Data was provided by the U.S. Fire Administration's (USFA) National Fire Data Center's (NFDC's) National Fire Incident Reporting System has numerous data elements that detail fire incidents for example  the fire department  fire incident  the occupants  structure and equipment used  hazard material involved and casualty details.",
+            "identifier": "FEMA-01809",
             "keyword": [
                 "Announcement",
                 "Broadcast",
@@ -887,30 +896,30 @@
                 "Reporting System",
                 "Statement"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-29T14:00:03-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "USFA NFIRS 2002 Basic Fire Incident Data"
         },
-            "identifier": "FEMA-01809",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "USFA NFIRS 2003 Basic Fire Incident Data",
             "description": "The 2003 US Fire Administration Fire (USFA) Fire Incident & Cause Data was provided by the U.S. Fire Administration's (USFA) National Fire Data Center's (NFDC's) National Fire Incident Reporting System has numerous data elements that detail fire incidents for example  the fire department  fire incident  the occupants  structure and equipment used  hazard material involved and casualty details.",
+            "identifier": "FEMA-01810",
             "keyword": [
                 "Announcement",
                 "Broadcast",
@@ -923,30 +932,30 @@
                 "Reporting System",
                 "Statement"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-29T14:00:03-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "USFA NFIRS 2003 Basic Fire Incident Data"
         },
-            "identifier": "FEMA-01810",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "USFA NFIRS 2004 Basic Fire Incident Data",
             "description": "The 2004 US Fire Administration Fire (USFA) Fire Incident & Cause Data was provided by the U.S. Fire Administration's (USFA) National Fire Data Center's (NFDC's) National Fire Incident Reporting System has numerous data elements that detail fire incidents for example  the fire department  fire incident  the occupants  structure and equipment used  hazard material involved and casualty details.",
+            "identifier": "FEMA-01811",
             "keyword": [
                 "Announcement",
                 "Broadcast",
@@ -959,30 +968,30 @@
                 "Reporting System",
                 "Statement"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-29T14:00:03-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "USFA NFIRS 2004 Basic Fire Incident Data"
         },
-            "identifier": "FEMA-01811",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "USFA NFIRS 2005 Basic Fire Incident Data",
             "description": "The 2005 US Fire Administration Fire (USFA) Fire Incident & Cause Data was provided by the U.S. Fire Administration's (USFA) National Fire Data Center's (NFDC's) National Fire Incident Reporting System has numerous data elements that detail fire incidents for example  the fire department  fire incident  the occupants  structure and equipment used  hazard material involved and casualty details.",
+            "identifier": "FEMA-01812",
             "keyword": [
                 "Announcement",
                 "Broadcast",
@@ -995,30 +1004,30 @@
                 "Reporting System",
                 "Statement"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-29T14:00:03-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "USFA NFIRS 2005 Basic Fire Incident Data"
         },
-            "identifier": "FEMA-01812",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "USFA NFIRS 2006 Basic Fire Incident Data",
             "description": "The 2006 US Fire Administration Fire (USFA) Fire Incident & Cause Data was provided by the U.S. Fire Administration's (USFA) National Fire Data Center's (NFDC's) National Fire Incident Reporting System has numerous data elements that detail fire incidents for example  the fire department  fire incident  the occupants  structure and equipment used  hazard material involved and casualty details.",
+            "identifier": "FEMA-01816",
             "keyword": [
                 "Announcement",
                 "Broadcast",
@@ -1031,30 +1040,30 @@
                 "Reporting System",
                 "Statement"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-29T14:00:04-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "USFA NFIRS 2006 Basic Fire Incident Data"
         },
-            "identifier": "FEMA-01816",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "USFA NFIRS 2007 Basic Fire Incident Data",
             "description": "The 2007 US Fire Administration Fire (USFA) Fire Incident & Cause Data was provided by the U.S. Fire Administration's (USFA) National Fire Data Center's (NFDC's) National Fire Incident Reporting System has numerous data elements that detail fire incidents for example  the fire department  fire incident  the occupants  structure and equipment used  hazard material involved and casualty details.",
+            "identifier": "FEMA-01817",
             "keyword": [
                 "Announcement",
                 "Broadcast",
@@ -1067,122 +1076,122 @@
                 "Reporting System",
                 "Statement"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-29T14:00:04-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "USFA NFIRS 2007 Basic Fire Incident Data"
         },
-            "identifier": "FEMA-01817",
+        {
             "accessLevel": "public",
             "bureauCode": [
-                "024:070"
-            ],
-            "programCode": [
-                "024:000"
+                "024:010"
             ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "DHS Strategic Plan",
             "description": "The U.S. Department of Homeland Security's Strategic Plan for Fiscal Years 2020-2024 fulfills the GPRA Modification Act of 2010 (P.L. 111-352) and the Office of Management and Budget's Circular A-11, Part 6 (2013) requirement for all Federal departments and agencies to publish an Agency Strategic Plan. The FY20-24 Strategic Plan provides an analytic foundation for the Department's Unity of Effort Initiative by articulating the Department's missions and goals, the strategies we employ to achieve each goal, and long-term performance that we use to evaluate our progress.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.dhs.gov/strategic-planning"
+                }
+            ],
+            "identifier": "MGMT-OCIO-Mobius-1",
             "keyword": [
                 "Strategy",
                 "Plan"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "DHS Strategic Plan"
         },
-            "identifier": "MGMT-OCIO-Mobius-1",
-            "accessLevel": "public",
+        {
+            "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.dhs.gov/strategic-planning"
-                }
-            ]
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Taxonomies",
             "description": "A set of hierarchical taxonomies used to categorize technology products.",
+            "identifier": "MGMT-OCIO-Mobius-10",
             "keyword": [
                 "Taxonomy",
                 "Technology"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Taxonomies"
         },
-            "identifier": "MGMT-OCIO-Mobius-10",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Capabilities and Activities List REST API",
             "description": "The DHS Functional Capabilities and Activities List (CAL) presents an integrated list of enterprise level functional capabilities and activities aligned to the Mission Functional Areas in the Business Architecture that the Department requires for executing its diverse missions. It represents at the enterprise level, the type of \u201cwork\u201d the Department engages in to execute its operations and business.",
+            "identifier": "MGMT-OCIO-Mobius-11",
             "keyword": [
                 "Capability",
                 "Activity",
                 "API",
                 "REST"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Capabilities and Activities List REST API"
         },
-            "identifier": "MGMT-OCIO-Mobius-11",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "FISMA System Inventory REST API",
             "description": "A system is identified by constructing logical boundaries around a set of processes, communications, storage, and related resources. The elements within these boundaries constitute a single system requiring a security plan. Each element of the system must (1) be under the same direct management control, (2) have the same function or mission objective, (3) have essentially the same operating characteristics and security needs, and (4) reside in the same general operating environment.  This service produces a list of FISMA Systems that belong to DHS Components.",
+            "identifier": "MGMT-OCIO-Mobius-12",
             "keyword": [
                 "API",
                 "REST",
@@ -1190,30 +1199,30 @@
                 "Application",
                 "System"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "FISMA System Inventory REST API"
         },
-            "identifier": "MGMT-OCIO-Mobius-12",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "FEMA FISMA System Inventory REST API",
             "description": "A system is identified by constructing logical boundaries around a set of processes, communications, storage, and related resources. The elements within these boundaries constitute a single system requiring a security plan. Each element of the system must (1) be under the same direct management control, (2) have the same function or mission objective, (3) have essentially the same operating characteristics and security needs, and (4) reside in the same general operating environment.  This service produces a list of FISMA Systems that belong to FEMA.",
+            "identifier": "MGMT-OCIO-Mobius-13",
             "keyword": [
                 "API",
                 "REST",
@@ -1221,30 +1230,30 @@
                 "Application",
                 "System"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "FEMA FISMA System Inventory REST API"
         },
-            "identifier": "MGMT-OCIO-Mobius-13",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "FISMA System to CAL Alignment REST API",
             "description": "FISMA System to Capability and Activity List Alignment",
+            "identifier": "MGMT-OCIO-Mobius-14",
             "keyword": [
                 "Capability",
                 "Activity",
@@ -1254,30 +1263,30 @@
                 "System",
                 "FISMA"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "FISMA System to CAL Alignment REST API"
         },
-            "identifier": "MGMT-OCIO-Mobius-14",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "FISMA System to Investments Alignment REST API",
             "description": "A service that provides consumers with the alignment between FISMA Systems and Capital Investments.  Essentially this represents the funding stream for each system.  Capital Investments fund FISMA Systems.",
+            "identifier": "MGMT-OCIO-Mobius-15",
             "keyword": [
                 "API",
                 "REST",
@@ -1287,30 +1296,30 @@
                 "Investment",
                 "Funding"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
+            "rights": null,
+            "title": "FISMA System to Investments Alignment REST API"
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "024:010"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Open Data (MGMT)",
                 "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-            "identifier": "MGMT-OCIO-Mobius-15",
-            "accessLevel": "non-public",
-            "bureauCode": [
-                "024:010"
-            ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
-        },
-        {
-            "title": "Capital Investments REST API",
             "description": "Capital Investment refers to the planning, development, and acquisition of a capital asset and the management and operation of that asset through its usable life after the initial acquisition. IT capital Investments may consist of one or more assets which provide functionality in an operational (production) environment.",
+            "identifier": "MGMT-OCIO-Mobius-16",
             "keyword": [
                 "API",
                 "REST",
@@ -1319,30 +1328,30 @@
                 "Program",
                 "CPIC"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Capital Investments REST API"
         },
-            "identifier": "MGMT-OCIO-Mobius-16",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Programs and Mission Activities for Current Congressional Phase REST API",
             "description": "Data regarding the Programs, Sub-Programs, and Mission Activities for the Most Recent Congressional Phase.",
+            "identifier": "MGMT-OCIO-Mobius-17",
             "keyword": [
                 "Plan",
                 "API",
@@ -1354,30 +1363,30 @@
                 "Budget",
                 "Execution"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Programs and Mission Activities for Current Congressional Phase REST API"
         },
-            "identifier": "MGMT-OCIO-Mobius-17",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Strategic Plan REST API",
             "description": "This service lists the department's Missions, Goals, and Objectives for the most recent Congressional Justification.",
+            "identifier": "MGMT-OCIO-Mobius-18",
             "keyword": [
                 "API",
                 "REST",
@@ -1387,30 +1396,30 @@
                 "Strategy",
                 "Strategic"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Strategic Plan REST API"
         },
-            "identifier": "MGMT-OCIO-Mobius-18",
-            "accessLevel": "public",
+        {
+            "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Strategic Plan and Mission Activity Alignment REST API",
             "description": "Data regarding the alignment between strategic plan and mission activity for the most recent congressional phase.",
+            "identifier": "MGMT-OCIO-Mobius-19",
             "keyword": [
                 "Plan",
                 "API",
@@ -1427,58 +1436,58 @@
                 "Strategic",
                 "PPBE"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Strategic Plan and Mission Activity Alignment REST API"
         },
-            "identifier": "MGMT-OCIO-Mobius-19",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Capabilities and Activities List",
             "description": "The DHS Functional Capabilities and Activities List (CAL) presents an integrated list of enterprise level functional capabilities and activities aligned to the Mission Functional Areas in the Business Architecture that the Department requires for executing its diverse missions. It represents at the enterprise level, the type of \u201cwork\u201d the Department engages in to execute its operations and business.",
+            "identifier": "MGMT-OCIO-Mobius-2",
             "keyword": [
                 "Capability",
                 "Activity"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Capabilities and Activities List"
         },
-            "identifier": "MGMT-OCIO-Mobius-2",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Systems & Investments REST API",
             "description": "A service that provides consumers with the alignment between FISMA Systems and Capital Investments.  Essentially this represents the funding stream for each system.  Capital Investments fund FISMA Systems.",
+            "identifier": "MGMT-OCIO-Mobius-20",
             "keyword": [
                 "API",
                 "REST",
@@ -1488,30 +1497,30 @@
                 "Investment",
                 "Funding"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Systems & Investments REST API"
         },
-            "identifier": "MGMT-OCIO-Mobius-20",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "TRM Component Baseline REST API",
             "description": "Technical Reference Model (TRM) is a set of categorized software and non-commodity hardware products that is the starting point for all IT purchases at the Department. It also includes the associated status of each software and hardware such as approved, prohibited, restricted, etc. This is a searchable reference model governed by TRM as a Service (TRMaaS).",
+            "identifier": "MGMT-OCIO-Mobius-21",
             "keyword": [
                 "API",
                 "REST",
@@ -1519,30 +1528,30 @@
                 "Governance",
                 "Technology Governance"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "TRM Component Baseline REST API"
         },
-            "identifier": "MGMT-OCIO-Mobius-21",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "TRM Service REST API",
             "description": "Technical Reference Model (TRM) is a set of categorized software and non-commodity hardware products that is the starting point for all IT purchases at the Department. It also includes the associated status of each software and hardware such as approved, prohibited, restricted, etc. This is a searchable reference model governed by TRM as a Service (TRMaaS).",
+            "identifier": "MGMT-OCIO-Mobius-22",
             "keyword": [
                 "API",
                 "REST",
@@ -1550,30 +1559,30 @@
                 "Governance",
                 "Technology Governance"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "TRM Service REST API"
         },
-            "identifier": "MGMT-OCIO-Mobius-22",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "USSS TRM Service REST API",
             "description": "Technical Reference Model (TRM) is a set of categorized software and non-commodity hardware products that is the starting point for all IT purchases at the Department. It also includes the associated status of each software and hardware such as approved, prohibited, restricted, etc. This is a searchable reference model governed by TRM as a Service (TRMaaS).  This service lists only those products that have been govern by the United States Secret Service.",
+            "identifier": "MGMT-OCIO-Mobius-23",
             "keyword": [
                 "API",
                 "REST",
@@ -1581,351 +1590,351 @@
                 "Governance",
                 "Technology Governance"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "USSS TRM Service REST API"
         },
-            "identifier": "MGMT-OCIO-Mobius-23",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Anticipated Systems Not Mapped to Published Data Assets Report",
             "description": "Displays Anticipated Systems not mapped to a Published data asset. An Anticipated System can be described as a system expected to have at least one associated data asset. It excludes systems exclusively designated as Network, WAN, Web Server and has a Lifecycle Configuration Status as Canceled, Decommission, Deleted, Development, Discontinued, Disposal, or Renamed. This report can be used to help improve the Percentage of Data Assets to Anticipated Systems Mapped Score from Enterprise Data Management (EDM) Scorecard by identifying which anticipated system need to be mapped to a data asset.",
+            "identifier": "MGMT-OCIO-Mobius-24",
             "keyword": [
                 "Data Asset",
                 "Dataset",
                 "FISMA System"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Anticipated Systems Not Mapped to Published Data Assets Report"
         },
-            "identifier": "MGMT-OCIO-Mobius-24",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Authoritative and/or Trusted Data Detail Report",
             "description": "Displays Documented Authoritative and/or Trusted data assets and the relevant associated Datasets. Published data assets that are considered documented have met the appropriate criteria. An Authoritative data asset must have a Legal Authority associated to it. A Trusted data asset must have a Yes selected for the following fields: Logical Data Model (LDM) Available, Data Management Plan (DMP) Completed, and Data Quality Plan (DQP) in Use. A data asset identified as Both must fulfill the criteria for Authoritative and Trusted. Datasets associated to a Producer data asset can also be identified as Authoritative and/or Trusted and are included in this report.",
+            "identifier": "MGMT-OCIO-Mobius-25",
             "keyword": [
                 "Data Asset",
                 "Dataset",
                 "Report"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Authoritative and/or Trusted Data Detail Report"
         },
-            "identifier": "MGMT-OCIO-Mobius-25",
-            "accessLevel": "non-public",
+        {
+            "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Data Inventory Program (DIP) Report",
             "description": "Display all data uploaded to the Data Inventory Program.",
+            "identifier": "MGMT-OCIO-Mobius-26",
             "keyword": [
                 "Report",
                 "Dataset"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Data Inventory Program (DIP) Report"
         },
-            "identifier": "MGMT-OCIO-Mobius-26",
-            "accessLevel": "public",
+        {
+            "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Data Inventory Program (DIP) Test Report",
             "description": "Display all data uploaded to the Data Inventory Program's testing tool.  This is used by data stewards to test their upload of data catalog entries.",
+            "identifier": "MGMT-OCIO-Mobius-27",
             "keyword": [
                 "Report",
                 "Dataset"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Data Inventory Program (DIP) Test Report"
         },
-            "identifier": "MGMT-OCIO-Mobius-27",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Incomplete Published Data Assets Report",
             "description": "Displays incomplete Published data assets. This report can be used to help improve the Data Asset Completeness score from the Enterprise Data Management (EDM) Scorecard by identifying which missing fields are required for completeness.",
+            "identifier": "MGMT-OCIO-Mobius-28",
             "keyword": [
                 "Data Asset",
                 "Dataset",
                 "Report"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Incomplete Published Data Assets Report"
         },
-            "identifier": "MGMT-OCIO-Mobius-28",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Invalid Point of Contact Emails Report",
             "description": "Displays all invalid point of contact emails in the Data Asset Repository. Emails are considered invalid if they cannot be validated by the trusted identity exchange (TIE). All profile and role information for an invalid email is provided.",
+            "identifier": "MGMT-OCIO-Mobius-29",
             "keyword": [
                 "Data Asset",
                 "Dataset",
                 "Report"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Invalid Point of Contact Emails Report"
         },
-            "identifier": "MGMT-OCIO-Mobius-29",
-            "accessLevel": "non-public",
+        {
+            "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Program Listing",
             "description": "\u200b\u200bIn 2004, the Homeland Security Act was modified to establish the PPBE system as the means by which DHS allocates resources and directs programmed resources to be reported in the Future Years Homeland Security Program (FYHSP).  The intent is to ensure that resource proposals and budget execution are examined from a broader perspective which are linked to and follow strategy.  This system is comprised of four (sometimes overlapping) phases:rn- Planning establishes strategic priorities and capabilities required to achieve the strategy;rn- Programming applies the resources to \u201cPrograms and looks at alternatives to providing capabilities required to achieve the strategic priorities;rn- Budgeting properly prices the Programs, develops justifications, and an execution plan; andrn- Execution performs and monitors the approved plan.",
+            "identifier": "MGMT-OCIO-Mobius-3",
             "keyword": [
                 "Planning",
                 "Budget",
                 "Execution",
                 "Program"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Program Listing"
         },
-            "identifier": "MGMT-OCIO-Mobius-3",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "OMB Enterprise Data Inventory Report",
             "description": "Displays a report of the entire enterprise data inventory for all published data assets in Mobius so that this data can be reported to OMB.",
+            "identifier": "MGMT-OCIO-Mobius-30",
             "keyword": [
                 "Dataset",
                 "Open Data",
                 "Data Asset"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "OMB Enterprise Data Inventory Report"
         },
-            "identifier": "MGMT-OCIO-Mobius-30",
-            "accessLevel": "public",
+        {
+            "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Points of Contact Report",
             "description": "Displays all contact information by role within the Data Asset Repository in Mobius so that point of contact information is readily available to the DHS Community.",
+            "identifier": "MGMT-OCIO-Mobius-31",
             "keyword": [
                 "Report",
                 "Point of Contact",
                 "Contact",
                 "POC"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Points of Contact Report"
         },
-            "identifier": "MGMT-OCIO-Mobius-31",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Published Data Assets Not Mapped to Anticipated System(s) Report",
             "description": "Displays Published data assets not mapped to an anticipated system. This report can be used to help improve the Percentage of Data Assets to Anticipated Systems Mapped Score from Enterprise Data Management (EDM) Scorecard by identifying which published data assets need to be mapped to a system.",
+            "identifier": "MGMT-OCIO-Mobius-32",
             "keyword": [
                 "Data Asset",
                 "Dataset",
                 "FISMA System",
                 "Report"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Published Data Assets Not Mapped to Anticipated System(s) Report"
         },
-            "identifier": "MGMT-OCIO-Mobius-32",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Investment Line of Sight Report",
             "description": "Displays details for investments by budget year, along with the investment's associated missions/goals/objectives, systems, functional capabilities and activities, and FYHSP Programs.",
+            "identifier": "MGMT-OCIO-Mobius-33",
             "keyword": [
                 "Investment",
                 "Capital Investment",
                 "Program",
                 "CPIC"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Investment Line of Sight Report"
         },
-            "identifier": "MGMT-OCIO-Mobius-33",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Investments Without Data Assets Report",
             "description": "Displays which investments are funding systems that do not have at least one data asset associated with them. Details are given by budget year.",
+            "identifier": "MGMT-OCIO-Mobius-34",
             "keyword": [
                 "Investment",
                 "Program",
@@ -1935,380 +1944,380 @@
                 "Report",
                 "Capital Investment"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Investments Without Data Assets Report"
         },
-            "identifier": "MGMT-OCIO-Mobius-34",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Component Baseline Report",
             "description": "IT product versions (regardless of status) within the TRM for a specific Component. All other Components' products are excluded.",
+            "identifier": "MGMT-OCIO-Mobius-35",
             "keyword": [
                 "Technology",
                 "Governance",
                 "Technology Governance",
                 "Report"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Component Baseline Report"
         },
-            "identifier": "MGMT-OCIO-Mobius-35",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Monthly TRM Report",
             "description": "Displays all Products for the DHS TRM. The target technologies have an Approved or Go-To status and the baseline technologies have a Restricted, Divest, Prohibited, or Emerging status. This list was previously used to generate the monthly TRM spreadsheet in Microsoft Excel.",
+            "identifier": "MGMT-OCIO-Mobius-36",
             "keyword": [
                 "Technology",
                 "Governance",
                 "Technology Governance",
                 "Report"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Monthly TRM Report"
         },
-            "identifier": "MGMT-OCIO-Mobius-36",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Potential Duplicate Products Report",
             "description": "Displays potential software and hardware product duplicates within a manufacturer. Product duplicates have the same name, component, and manufacturer. Also displays duplicate software versions (patch level and edition must be the same) and hardware models within a product.",
+            "identifier": "MGMT-OCIO-Mobius-37",
             "keyword": [
                 "Technology",
                 "Governance",
                 "Technology Governance",
                 "Report"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Potential Duplicate Products Report"
         },
-            "identifier": "MGMT-OCIO-Mobius-37",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "TRM Lifecycle Report",
             "description": "Displays product lifecycle status and related information per component, along with recommended actions to take.",
+            "identifier": "MGMT-OCIO-Mobius-38",
             "keyword": [
                 "Technology",
                 "Governance",
                 "Technology Governance",
                 "Report"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "TRM Lifecycle Report"
         },
-            "identifier": "MGMT-OCIO-Mobius-38",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "TRM Products in Workbook Format Report",
             "description": "Displays all products, along with the manufacturer, implementation, version, and model data in a format consistent with the TRM upload workbook. Downloading this report provides and excel file that can then be used with the Upload TRM Workbook.",
+            "identifier": "MGMT-OCIO-Mobius-39",
             "keyword": [
                 "Technology",
                 "Governance",
                 "Technology Governance",
                 "Report"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "TRM Products in Workbook Format Report"
         },
-            "identifier": "MGMT-OCIO-Mobius-39",
-            "accessLevel": "non-public",
+        {
+            "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Capital Investments",
             "description": "Capital investment is the planning, development, acquisition of a capital asset and the management and operation of that asset through its usable life after the initial acquisition. IT Capital investments may consist of one or more assets, the planning, development and acquisition of which are managed through projects, and which then provide useful components in an operational (production) environment.",
+            "identifier": "MGMT-OCIO-Mobius-4",
             "keyword": [
                 "Investment",
                 "Capital Investment",
                 "Program",
                 "CPIC"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Capital Investments"
         },
-            "identifier": "MGMT-OCIO-Mobius-4",
-            "accessLevel": "public",
+        {
+            "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "TRM Upsert Validation Report",
             "description": "Displays products that were updated via the workbook upload process over the past 3 months. The report includes: All the data and columns from the workbook, the audit id, Data and time of when the upsert was run, Links to the product paged in Mobius for the updated products. This report is only visible to TRM Enterprise Admins",
+            "identifier": "MGMT-OCIO-Mobius-40",
             "keyword": [
                 "Technology",
                 "Governance",
                 "Technology Governance",
                 "Report"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "TRM Upsert Validation Report"
         },
-            "identifier": "MGMT-OCIO-Mobius-40",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Welcome to Mobius Video",
             "description": "This video introduces you to the power of Mobius, explaining how Mobius connects management and IT Data across the Enterprise for everyone to access.",
+            "identifier": "MGMT-OCIO-Mobius-41",
             "keyword": [
                 "Mobius",
                 "Video"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Welcome to Mobius Video"
         },
-            "identifier": "MGMT-OCIO-Mobius-41",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Mobius \u2013 General Overview Video",
             "description": "This video is your launch pad for understanding the capabilities of the homepage. Learn about the homepage visualizations, menu behavior, and different search options.",
+            "identifier": "MGMT-OCIO-Mobius-42",
             "keyword": [
                 "Mobius",
                 "Video"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Mobius \u2013 General Overview Video"
         },
-            "identifier": "MGMT-OCIO-Mobius-42",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Mobius \u2013 Reporting Overview Video",
             "description": "This video explains how you can manipulate your view of reporting data in Mobius.",
+            "identifier": "MGMT-OCIO-Mobius-43",
             "keyword": [
                 "Mobius",
                 "Video"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Mobius \u2013 Reporting Overview Video"
         },
-            "identifier": "MGMT-OCIO-Mobius-43",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Mobius - Content Overview Video",
             "description": "This video explains how you can search for information about the DHS Enterprise based on content area. Learn the various ways you can navigate to search results and refine search results for discovery and download.",
+            "identifier": "MGMT-OCIO-Mobius-44",
             "keyword": [
                 "Mobius",
                 "Video"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2023-03-16T10:52:02-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Mobius - Content Overview Video"
         },
-            "identifier": "MGMT-OCIO-Mobius-44",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Mobius \u2013 Personalization Overview Video",
             "description": "This video explains how you can personalize your view of the data in Mobius.",
+            "identifier": "MGMT-OCIO-Mobius-45",
             "keyword": [
                 "Mobius",
                 "Video"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Mobius \u2013 Personalization Overview Video"
         },
-            "identifier": "MGMT-OCIO-Mobius-45",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Mobius Data Dictionary",
             "description": "This document shows and describes the logical data model (Entity Relationship Diagram) for the Mobius application",
+            "identifier": "MGMT-OCIO-Mobius-46",
             "keyword": [
                 "Mobius",
                 "Data Dictionary",
@@ -2316,343 +2325,343 @@
                 "ERD",
                 "Entity Relationship Diagram"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Mobius Data Dictionary"
         },
-            "identifier": "MGMT-OCIO-Mobius-46",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Segment Architectures",
             "description": "It defines a simple roadmap for a core mission area, business service, or enterprise service. Segment architecture is driven by business management and delivers products that improve the delivery of services to citizens and agency staff. From an investment perspective, segment architecture drives decisions for a business case or group of business cases supporting a core mission area or common or shared service.",
+            "identifier": "MGMT-OCIO-Mobius-5",
             "keyword": [
                 "Architecture",
                 "Enterprise Architecture",
                 "Segment"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Segment Architectures"
         },
-            "identifier": "MGMT-OCIO-Mobius-5",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "CAL_3.0_Handbook_Final_20171205.pdf",
             "description": "A document that describes how to understand and how to use the Capabilities and Activities List",
+            "identifier": "MGMT-OCIO-Mobius-53",
             "keyword": [
                 "Capability",
                 "Activity",
                 "CAL"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "CAL_3.0_Handbook_Final_20171205.pdf"
         },
-            "identifier": "MGMT-OCIO-Mobius-53",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "DHS_FY2019_IT_Strategic_Plan.pdf",
             "description": "This Enterprise Architecture Board (EAB) Guide is designed to address several major purposes:rn\u2022 EAB Process Overview. Help all DHS personnel\u2014especially leadership, program personnel and EAB stakeholders \u2014understand the role of the EAB in supporting Enterprise Architecture (EA) and EA stakeholders within DHS, as well as for DHS enterprise processes.rn\u2022 Practitioners\u2019 Guidance. Assist DHS personnel in understanding, aligning their activities with, preparing for, and executing the EAB process.rn\u2022 EAB Outreach, Support and Reviews. The EAB\u2019s primary operational activity is planning and performing Reviews. EAB Reviews are comprehensive and right-sized to their position in a specific program\u2019s lifecycle. They support critical recommendations and decisions at key points for managing acquisitions, investments, and capabilities, primarily within the Acquisition Lifecycle Framework (ALF), and specifically prior to an Acquisition Decision Event (ADE). The EAB initiates outreach, provides expert guidance and support to program stakeholders, assesses inputs and artifacts, and provides recommendations.",
+            "identifier": "MGMT-OCIO-Mobius-54",
             "keyword": [
                 "Strategy",
                 "Plan"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "DHS_FY2019_IT_Strategic_Plan.pdf"
         },
-            "identifier": "MGMT-OCIO-Mobius-54",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "EAB Guide FINAL.pdf",
             "description": "This Guide is intended to help stakeholders understand the EAB\u2019s role in promoting, operationalizing and supporting EA in the DHS enterprise. The EAB serves as a conduit for marshalling and channeling EA guidance and services to DHS programs and their architecture content developers. These content developers, in collaboration with Headquarters, can then successfully develop program artifacts to meet ALF requirements and timelines. The EAB also helps stakeholders to identify and address technical and programmatic risks and issues. These risks are identified and addressed in conjunction with management oversight entities such as the Acquisition Review Team (ART) and Acquisition Review Board (ARB).",
+            "identifier": "MGMT-OCIO-Mobius-55",
             "keyword": [
                 "Enterprise Architecture",
                 "EAB"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "EAB Guide FINAL.pdf"
         },
-            "identifier": "MGMT-OCIO-Mobius-55",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "EAB Guide Overview.pdf",
             "description": "This Enterprise Architecture Board (EAB) Guide is designed to address several major purposes:rn\u2022 EAB Process Overview. Help all DHS personnel\u2014especially leadership, program personnel and EAB stakeholders \u2014understand the role of the EAB in supporting Enterprise Architecture (EA) and EA stakeholders within DHS, as well as for DHS enterprise processes.rn\u2022 Practitioners\u2019 Guidance. Assist DHS personnel in understanding, aligning their activities with, preparing for, and executing the EAB process.rn\u2022 EAB Outreach, Support and Reviews. The EAB\u2019s primary operational activity is planning and performing Reviews. EAB Reviews are comprehensive and right-sized to their position in a specific program\u2019s lifecycle. They support critical recommendations and decisions at key points for managing acquisitions, investments, and capabilities, primarily within the Acquisition Lifecycle Framework (ALF), and specifically prior to an Acquisition Decision Event (ADE). The EAB initiates outreach, provides expert guidance and support to program stakeholders, assesses inputs and artifacts, and provides recommendations.",
+            "identifier": "MGMT-OCIO-Mobius-56",
             "keyword": [
                 "Enterprise Architecture",
                 "EAB"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-12-07T10:58:38-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "EAB Guide Overview.pdf"
         },
-            "identifier": "MGMT-OCIO-Mobius-56",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Functional_Capabilities_and_Activities_Catalog_CAL_3.0_FINAL-Dec_2017.pdf",
             "description": "The DHS Functional Capabilities and Activities List (CAL) presents an integrated list of enterprise level functional capabilities and activities aligned to the Mission Functional Areas in the Business Architecture that the Department requires for executing its diverse missions. It represents at the enterprise level, the type of \u201cwork\u201d the Department engages in to execute its operations and business.",
+            "identifier": "MGMT-OCIO-Mobius-57",
             "keyword": [
                 "Capability",
                 "Activity",
                 "CAL"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Functional_Capabilities_and_Activities_Catalog_CAL_3.0_FINAL-Dec_2017.pdf"
         },
-            "identifier": "MGMT-OCIO-Mobius-57",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "GovernanceLifecycleManagement_v1.pdf",
             "description": "Process diagram depicting the TRM governance lifecycle management process",
+            "identifier": "MGMT-OCIO-Mobius-58",
             "keyword": [
                 "Technology",
                 "Governance",
                 "Technology Lifecycle"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "GovernanceLifecycleManagement_v1.pdf"
         },
-            "identifier": "MGMT-OCIO-Mobius-58",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Mobius_SlickSheet.pdf",
             "description": "High level overview of the Mobius application.  This slick sheet is generally handed out at demonstrations and events.",
+            "identifier": "MGMT-OCIO-Mobius-59",
             "keyword": [
                 "Mobius",
                 "Mobius Overview"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Mobius_SlickSheet.pdf"
         },
-            "identifier": "MGMT-OCIO-Mobius-59",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "FISMA System Inventory",
             "description": "A system is identified by constructing logical boundaries around a set of processes, communications, storage, and related resources. The elements within these boundaries constitute a single system requiring a security plan. Each element of the system must (1) be under the same direct management control, (2) have the same function or mission objective, (3) have essentially the same operating characteristics and security needs, and (4) reside in the same general operating environment.",
+            "identifier": "MGMT-OCIO-Mobius-6",
             "keyword": [
                 "FISMA",
                 "Application",
                 "System"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "FISMA System Inventory"
         },
-            "identifier": "MGMT-OCIO-Mobius-6",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "audit.log",
             "description": "Audit log of transactions taking place within Mobius.  This is used by the Security Operations Center to help determine the cyber health of our system",
+            "identifier": "MGMT-OCIO-Mobius-60",
             "keyword": [
                 "Mobius",
                 "Application Audit Log"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "audit.log"
         },
-            "identifier": "MGMT-OCIO-Mobius-60",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "nest.log",
             "description": "Audit log of database transactions taking place within Mobius.  This is used by the Security Operations Center to help determine the cyber health of our system",
+            "identifier": "MGMT-OCIO-Mobius-61",
             "keyword": [
                 "Mobius",
                 "Database Audit Log"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "nest.log"
         },
-            "identifier": "MGMT-OCIO-Mobius-61",
-            "accessLevel": "non-public",
+        {
+            "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Enterprise Data Inventory",
             "description": "The DHS Data Inventory Program is working to create a single data inventory of all data within DHS, including the DHS Components, the DHS Functional Data Domains, and DHS HQ. rnrnThe Data Inventory Program is designed to exceed DHS obligations under the Foundations for Evidence-Based Policymaking Act (the Evidence Act), the OPEN Government Data Act, the DHS Data Framework Act of 2018, and DHS Delegation Number 04004 rev 00 of May 18, 2021 from Secretary Mayorkas to the Chief Data Officer. The goal is to create a data inventory that will be useful for all of DHS to help answer questions about DHS data in a timely manner and help DHS leadership plan new activities.",
+            "identifier": "MGMT-OCIO-Mobius-7",
             "keyword": [
                 "Inventory",
                 "DCAT",
@@ -2661,129 +2670,94 @@
                 "Data Catalogue",
                 "Catalog"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Enterprise Data Inventory"
         },
-            "identifier": "MGMT-OCIO-Mobius-7",
-            "accessLevel": "public",
+        {
+            "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Technology Reference Model",
             "description": "Technical Reference Model (TRM) is a set of categorized software and non-commodity hardware products that is the starting point for all IT purchases at the Department. It also includes the associated status of each software and hardware such as approved, prohibited, restricted, etc. This is a searchable reference model governed by TRM as a Service (TRMaaS).",
+            "identifier": "MGMT-OCIO-Mobius-8",
             "keyword": [
                 "Technology",
                 "Governance",
                 "Technology Governance"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Technology Reference Model"
         },
-            "identifier": "MGMT-OCIO-Mobius-8",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Technology Manufacturers",
             "description": "Vendors who supply DHS with technology products (hardware and software)",
+            "identifier": "MGMT-OCIO-Mobius-9",
             "keyword": [
                 "Technology",
                 "Vendor",
                 "Manufacturer"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-11-07T15:52:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
-            },
-            "identifier": "MGMT-OCIO-Mobius-9",
-            "accessLevel": "non-public",
-            "bureauCode": [
-                "024:010"
-            ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "rights": null,
+            "title": "Technology Manufacturers"
         },
         {
-            "title": "U.S. Border Patrol Family Unit and Unaccompanied Alien Children (0-17) Apprehensions",
-            "description": "Beginning in 2013 and specifically in the first half of 2014, CBP has seen an overall increase in the apprehension of Unaccompanied Alien Children from Central America at the Southwest Border, specifically in the Rio Grande Valley.  Family Unit and Unaccompanied Alien Children (0-17) apprehensions FY 14 through June, compared to the same time period for FY 13.",
-            "keyword": [
-                "TECS",
-                "Apprehension Booking",
-                "Enforcement Case Tracking System",
-                "EABM",
-                "ENFORCE",
-                "IAFIS",
-                "IDENT",
-                "Inspection/NSEERS",
-                "State Department"
+            "accessLevel": "public",
+            "bureauCode": [
+                "024:054"
             ],
-            "modified": "2022-03-30T14:03:24-04:00",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "BEMSD"
-            },
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Open Data (MGMT)",
                 "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-            "identifier": "CBP-000196",
-            "accessLevel": "public",
-            "bureauCode": [
-                "024:054"
-            ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "description": "Beginning in 2013 and specifically in the first half of 2014, CBP has seen an overall increase in the apprehension of Unaccompanied Alien Children from Central America at the Southwest Border, specifically in the Rio Grande Valley.  Family Unit and Unaccompanied Alien Children (0-17) apprehensions FY 14 through June, compared to the same time period for FY 13.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://www.cbp.gov/newsroom/stats/southwest-border-unaccompanied-children/fy-2016"
                 }
-            ]
-        },
-        {
-            "title": "U.S. Border Patrol Fiscal Year 2011 Sector Profile",
-            "description": "Apprehensions / Seizure Statistics - Fiscal Year 2011 (Oct. 1st through Sept. 30th)Fiscal Year 2011 - Nationwide Apprehensions By Sector: Accompanied / Unaccompanied Juveniles, Total Juveniles, Total AdultsFiscal Year 2011 - Nationwide Apprehensions by Sector: by GenderFiscal Year 2011 - Nationwide Apprehensions/Seizures",
+            ],
+            "identifier": "CBP-000196",
             "keyword": [
                 "TECS",
                 "Apprehension Booking",
@@ -2795,36 +2769,36 @@
                 "Inspection/NSEERS",
                 "State Department"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:24-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "BEMSD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "U.S. Border Patrol Family Unit and Unaccompanied Alien Children (0-17) Apprehensions"
         },
-            "identifier": "CBP-000197",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:054"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Apprehensions / Seizure Statistics - Fiscal Year 2011 (Oct. 1st through Sept. 30th)Fiscal Year 2011 - Nationwide Apprehensions By Sector: Accompanied / Unaccompanied Juveniles, Total Juveniles, Total AdultsFiscal Year 2011 - Nationwide Apprehensions by Sector: by GenderFiscal Year 2011 - Nationwide Apprehensions/Seizures",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://www.cbp.gov/sites/default/files/documents/U.S.%20Border%20Patrol%20Fiscal%20Year%202011%20Sector%20Profile.pdf"
                 }
-            ]
-        },
-        {
-            "title": "U.S. Border Patrol Fiscal Year 2012 Sector Profile",
-            "description": "Apprehensions / Seizure Statistics - Fiscal Year 2012 (Oct. 1st through Sept. 30th) Fiscal Year 2012 - Nationwide Apprehensions By Sector: Accompanied / Unaccompanied Juveniles, Total Juveniles, Total AdultsFiscal Year 2012 - Nationwide Apprehensions by Sector: by GenderFiscal Year 2012 - Nationwide Apprehensions/Seizures by Border Region",
+            ],
+            "identifier": "CBP-000197",
             "keyword": [
                 "TECS",
                 "Apprehension Booking",
@@ -2836,36 +2810,36 @@
                 "Inspection/NSEERS",
                 "State Department"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:24-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "BEMSD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "U.S. Border Patrol Fiscal Year 2011 Sector Profile"
         },
-            "identifier": "CBP-000198",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:054"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Apprehensions / Seizure Statistics - Fiscal Year 2012 (Oct. 1st through Sept. 30th) Fiscal Year 2012 - Nationwide Apprehensions By Sector: Accompanied / Unaccompanied Juveniles, Total Juveniles, Total AdultsFiscal Year 2012 - Nationwide Apprehensions by Sector: by GenderFiscal Year 2012 - Nationwide Apprehensions/Seizures by Border Region",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://www.cbp.gov/sites/default/files/documents/U.S.%20Border%20Patrol%20Fiscal%20Year%202012%20Sector%20Profile.pdf"
                 }
-            ]
-        },
-        {
-            "title": "U.S. Border Patrol Fiscal Year 2013 Sector Profile",
-            "description": "Apprehensions / Seizure Statistics - Fiscal Year 2013 (Oct. 1st through Sept. 30th)Fiscal Year 2013 - Nationwide Apprehensions By Sector: Accompanied / Unaccompanied Juveniles, Total Juveniles, Total AdultsFiscal Year 2013 - Nationwide Apprehensions by Sector: by GenderFiscal Year 2013 - Nationwide Apprehensions/Seizures by Border Region",
+            ],
+            "identifier": "CBP-000198",
             "keyword": [
                 "TECS",
                 "Apprehension Booking",
@@ -2877,36 +2851,36 @@
                 "Inspection/NSEERS",
                 "State Department"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:24-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "BEMSD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "U.S. Border Patrol Fiscal Year 2012 Sector Profile"
         },
-            "identifier": "CBP-000199",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:054"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Apprehensions / Seizure Statistics - Fiscal Year 2013 (Oct. 1st through Sept. 30th)Fiscal Year 2013 - Nationwide Apprehensions By Sector: Accompanied / Unaccompanied Juveniles, Total Juveniles, Total AdultsFiscal Year 2013 - Nationwide Apprehensions by Sector: by GenderFiscal Year 2013 - Nationwide Apprehensions/Seizures by Border Region",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://www.cbp.gov/sites/default/files/documents/U.S.%20Border%20Patrol%20Fiscal%20Year%202013%20Profile.pdf"
                 }
-            ]
-        },
-        {
-            "title": "U.S. Border Patrol Fiscal Year Apprehension Statistics Nationwide - FY 1925 through FY 2013",
-            "description": "Nationwide Illegal Alien Apprehensions Statistics Fiscal Years 1925 - 2013",
+            ],
+            "identifier": "CBP-000199",
             "keyword": [
                 "TECS",
                 "Apprehension Booking",
@@ -2918,36 +2892,36 @@
                 "Inspection/NSEERS",
                 "State Department"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:24-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "BEMSD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "U.S. Border Patrol Fiscal Year 2013 Sector Profile"
         },
-            "identifier": "CBP-000200",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:054"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Nationwide Illegal Alien Apprehensions Statistics Fiscal Years 1925 - 2013",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://www.cbp.gov/newsroom/media-resources/stats?title=Border+Patrol"
                 }
-            ]
-        },
-        {
-            "title": "U.S. Border Patrol Fiscal Year Apprehension Statistics Nationwide FY 2015",
-            "description": "Nationwide Illegal Alien Apprehension Statistics Fiscal Year 2015",
+            ],
+            "identifier": "CBP-000200",
             "keyword": [
                 "TECS",
                 "Apprehension Booking",
@@ -2959,36 +2933,36 @@
                 "Inspection/NSEERS",
                 "State Department"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:24-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "BEMSD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "U.S. Border Patrol Fiscal Year Apprehension Statistics Nationwide - FY 1925 through FY 2013"
         },
-            "identifier": "CBP-000201",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:054"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Nationwide Illegal Alien Apprehension Statistics Fiscal Year 2015",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.cbp.gov/sites/default/files/documents/USBP%20Stats%20FY2015%20sector%20profile.pdf"
                 }
-            ]
-        },
-        {
-            "title": "U.S. Border Patrol Fiscal Year Apprehension Statistics Nationwide FY 2016",
-            "description": "Nationwide Illegal Alien Apprehension Statistics Fiscal Year 2016",
+            ],
+            "identifier": "CBP-000201",
             "keyword": [
                 "TECS",
                 "Apprehension Booking",
@@ -3000,36 +2974,36 @@
                 "Inspection/NSEERS",
                 "State Department"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:24-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "BEMSD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "U.S. Border Patrol Fiscal Year Apprehension Statistics Nationwide FY 2015"
         },
-            "identifier": "CBP-000202",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:054"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Nationwide Illegal Alien Apprehension Statistics Fiscal Year 2016",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.cbp.gov/sites/default/files/assets/documents/2017-Jan/USBP%20Stats%20FY2016%20sector%20profile.pdf"
                 }
-            ]
-        },
-        {
-            "title": "U.S. Border Patrol Fiscal Year Apprehension Statistics Nationwide FY 2017",
-            "description": "Nationwide Illegal Alien Apprehension Statistics Fiscal Year 2017",
+            ],
+            "identifier": "CBP-000202",
             "keyword": [
                 "TECS",
                 "Apprehension Booking",
@@ -3041,36 +3015,36 @@
                 "Inspection/NSEERS",
                 "State Department"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:24-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "BEMSD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "U.S. Border Patrol Fiscal Year Apprehension Statistics Nationwide FY 2016"
         },
-            "identifier": "CBP-000203",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:054"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Nationwide Illegal Alien Apprehension Statistics Fiscal Year 2017",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.cbp.gov/sites/default/files/assets/documents/2017-Dec/USBP%20Stats%20FY2017%20sector%20profile.pdf"
                 }
-            ]
-        },
-        {
-            "title": "U.S. Border Patrol Fiscal Year Apprehension Statistics Southwest border sectors - FY 1960 through FY 2014",
-            "description": "Total Illegal Alien Apprehensions  for the Southwest Border Sectors by Fiscal Year by Sector: 1960 - 2014.",
+            ],
+            "identifier": "CBP-000203",
             "keyword": [
                 "TECS",
                 "Apprehension Booking",
@@ -3082,36 +3056,77 @@
                 "Inspection/NSEERS",
                 "State Department"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:24-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "BEMSD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "U.S. Border Patrol Fiscal Year Apprehension Statistics Nationwide FY 2017"
         },
-            "identifier": "CBP-000204",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:054"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Total Illegal Alien Apprehensions  for the Southwest Border Sectors by Fiscal Year by Sector: 1960 - 2014.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://www.cbp.gov/newsroom/media-resources/stats?title=Border+Patrol"
                 }
-            ]
+            ],
+            "identifier": "CBP-000204",
+            "keyword": [
+                "TECS",
+                "Apprehension Booking",
+                "Enforcement Case Tracking System",
+                "EABM",
+                "ENFORCE",
+                "IAFIS",
+                "IDENT",
+                "Inspection/NSEERS",
+                "State Department"
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2022-03-30T14:03:24-04:00",
+            "programCode": [
+                "024:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "BEMSD"
+            },
+            "rights": null,
+            "title": "U.S. Border Patrol Fiscal Year Apprehension Statistics Southwest border sectors - FY 1960 through FY 2014"
         },
         {
-            "title": "U.S. Border Patrol Fiscal Year Budget Statistics Border Patrol Program Budget - FY 1990 through FY 2013",
+            "accessLevel": "public",
+            "bureauCode": [
+                "024:054"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
             "description": "Enacted Border Patrol Program Budget by Fiscal Year (Dollars in Thousands)for FY-1990 to FY 2013",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "http://www.cbp.gov/newsroom/media-resources/stats?title=Border+Patrol"
+                }
+            ],
+            "identifier": "CBP-000205",
             "keyword": [
                 "SAP",
                 "Revenue and Asset Management",
@@ -3120,36 +3135,36 @@
                 "Budget Control System",
                 "Enterprise Resource Planning (ERP)"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:24-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "BEMSD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "U.S. Border Patrol Fiscal Year Budget Statistics Border Patrol Program Budget - FY 1990 through FY 2013"
         },
-            "identifier": "CBP-000205",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:054"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Total Illegal Alien Apprehensions By Month From FY 1999 through FY 2014",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://www.cbp.gov/newsroom/media-resources/stats?title=Border+Patrol"
                 }
-            ]
-        },
-        {
-            "title": "U.S. Border Patrol Fiscal Year Monthly Apprehension Statistics",
-            "description": "Total Illegal Alien Apprehensions By Month From FY 1999 through FY 2014",
+            ],
+            "identifier": "CBP-000206",
             "keyword": [
                 "TECS",
                 "Apprehension Booking",
@@ -3161,36 +3176,36 @@
                 "Inspection/NSEERS",
                 "State Department"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:24-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "BEMSD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "U.S. Border Patrol Fiscal Year Monthly Apprehension Statistics"
         },
-            "identifier": "CBP-000206",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:054"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Southwest Border Sectors include: Del Rio, El Centro, El Paso, Laredo, Rio Grande Valley, San Diego, Tucson, YumaSouthwest Border Deaths By Fiscal Year (Oct. 1st through Sept. 30th)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://www.cbp.gov/newsroom/media-resources/stats?title=Border+Patrol"
                 }
-            ]
-        },
-        {
-            "title": "U.S. Border Patrol Fiscal Year Statistics Southwest border sector deaths - FY 1998 through FY 2013",
-            "description": "Southwest Border Sectors include: Del Rio, El Centro, El Paso, Laredo, Rio Grande Valley, San Diego, Tucson, YumaSouthwest Border Deaths By Fiscal Year (Oct. 1st through Sept. 30th)",
+            ],
+            "identifier": "CBP-000207",
             "keyword": [
                 "TECS",
                 "Apprehension Booking",
@@ -3202,36 +3217,30 @@
                 "Inspection/NSEERS",
                 "State Department"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:24-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "BEMSD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "U.S. Border Patrol Fiscal Year Statistics Southwest border sector deaths - FY 1998 through FY 2013"
         },
-            "identifier": "CBP-000207",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:054"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "http://www.cbp.gov/newsroom/media-resources/stats?title=Border+Patrol"
-                }
-            ]
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "CBP Active Dumping and Active Countervailing (AD/CVD) Cases",
             "description": "The datasets provide information from CBP's reference files on active anti-dumping and active countervailing cases.  This data includes associated case numbers (if any), ISO country code, tariff number and short descriptions of the case.",
+            "identifier": "CBP-000045",
             "keyword": [
                 "Communication",
                 "Obligation",
@@ -3251,30 +3260,36 @@
                 "Message",
                 "Point"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:25-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "CSPD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "CBP Active Dumping and Active Countervailing (AD/CVD) Cases"
         },
-            "identifier": "CBP-000045",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:054"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "CBP Customs Rulings Online Search System (CROSS)",
             "description": "CROSS is a searchable database of CBP rulings that can be retrieved based on simple or complex search characteristics using keywords and Boolean operators. CROSS has the added functionality of CROSS referencing rulings from the initial search result set with their modified, revoked or referenced counterparts. Rulings collections are separated into Headquarters and New York.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "http://rulings.cbp.gov/"
+                }
+            ],
+            "identifier": "CBP-000051",
             "keyword": [
                 "Directive",
                 "Guideline",
@@ -3291,36 +3306,36 @@
                 "Trade Community",
                 "Verdict"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:25-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "BEMSD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "CBP Customs Rulings Online Search System (CROSS)"
         },
-            "identifier": "CBP-000051",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:054"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Contains the CBP eRulings data that is available to the public via HTML Web Page",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "http://rulings.cbp.gov/"
+                    "accessURL": "https://apps.cbp.gov/erulings/"
                 }
-            ]
-        },
-        {
-            "title": "CBP eRulings Web dataset",
-            "description": "Contains the CBP eRulings data that is available to the public via HTML Web Page",
+            ],
+            "identifier": "CBP-000054",
             "keyword": [
                 "Decision",
                 "Ruling",
@@ -3329,36 +3344,36 @@
                 "Customs and Border Protection - E-Rulings",
                 "Electronic Ruling"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:25-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "BEMSD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "CBP eRulings Web dataset"
         },
-            "identifier": "CBP-000054",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:054"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "This dataset provides a Complete Listing Of valid District/Port Codes in the U.S.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://apps.cbp.gov/erulings/"
+                    "accessURL": "https://www.cbp.gov/document/technical-documentation/ace-appendix-d-export-port-codes"
                 }
-            ]
-        },
-        {
-            "title": "CBP Port Codes",
-            "description": "This dataset provides a Complete Listing Of valid District/Port Codes in the U.S.",
+            ],
+            "identifier": "CBP-000060",
             "keyword": [
                 "Air",
                 "Cargo",
@@ -3377,36 +3392,36 @@
                 "Vehicle",
                 "Admission"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:25-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "CSPD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "CBP Port Codes"
         },
-            "identifier": "CBP-000060",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:054"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "CBP public forms is a repository CBP forms in PDF format that supports the CBP Office of Finance by making available to the public and trade community electronic forms that can be completed online, saved and printed. There is no database associated to this collection of documents. Downloadable forms meets the business need of CBP to increase efficiency in processing of form related activities and to meet objectives of the Paper Reduction Act.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.cbp.gov/document/technical-documentation/ace-appendix-d-export-port-codes"
+                    "accessURL": "https://www.cbp.gov/newsroom/publications/forms"
                 }
-            ]
-        },
-        {
-            "title": "Customs and Border Protection - Public Forms Master Dataset",
-            "description": "CBP public forms is a repository CBP forms in PDF format that supports the CBP Office of Finance by making available to the public and trade community electronic forms that can be completed online, saved and printed. There is no database associated to this collection of documents. Downloadable forms meets the business need of CBP to increase efficiency in processing of form related activities and to meet objectives of the Paper Reduction Act.",
+            ],
+            "identifier": "CBP-000080",
             "keyword": [
                 "Online",
                 "CBP PF",
@@ -3415,208 +3430,208 @@
                 "Information Collection",
                 "Paperless"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:25-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "BEMSD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Customs and Border Protection - Public Forms Master Dataset"
         },
-            "identifier": "CBP-000080",
+        {
             "accessLevel": "public",
             "bureauCode": [
-                "024:054"
-            ],
-            "programCode": [
-                "024:000"
+                "024:010"
             ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.cbp.gov/newsroom/publications/forms"
-                }
-            ]
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "NFC - EmpowHR",
             "description": "EmpowHR is an integrated suite of commercial and Government applications that supports all critical HR components in a single enterprise system. It provides comprehensive employee information enabling agencies to: (1) make critical decisions concerning workforce utilization, (2) forecast workforce turnover and placement, and (3) project future resource budget allocations on a fiscal year basis",
+            "identifier": "MGMT-OCHCO-NFC-EMPOWHR",
             "keyword": [
                 "Employee",
                 "NFC",
                 "USDA",
                 "EmpowHR"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-03-06T14:41:29-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NFC"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NFC - EmpowHR"
         },
-            "identifier": "MGMT-OCHCO-NFC-EMPOWHR",
+        {
             "accessLevel": "public",
             "bureauCode": [
-                "024:010"
-            ],
-            "programCode": [
-                "024:000"
+                "024:056"
             ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "TSA FOIA Reading Room - Weekly Passenger Throughput Data",
             "description": "A report of hourly passenger throughput data for each airport and checkpoint that is published in the TSA FOIA Reading Room every week.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.tsa.gov/foia/readingroom"
+                }
+            ],
+            "identifier": "TSA-4dbbabdb-cbce-4d6a-b0fa-bca2f074bdca",
             "keyword": [
                 "checkpoint",
                 "throughput",
                 "airport",
                 "passenger"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-22T12:25:28-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Security Operations"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "TSA FOIA Reading Room - Weekly Passenger Throughput Data"
         },
-            "identifier": "TSA-4dbbabdb-cbce-4d6a-b0fa-bca2f074bdca",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "A log of all Freedom of Information Act (FOIA) requests received by TSA that contains the requester name and a description of the request.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.tsa.gov/foia/readingroom"
                 }
-            ]
-        },
-        {
-            "title": "TSA FOIA Reading Room - Quarterly FOIA Log",
-            "description": "A log of all Freedom of Information Act (FOIA) requests received by TSA that contains the requester name and a description of the request.",
+            ],
+            "identifier": "TSA-cde7f7f9-b081-4389-ad30-a85f1325ae5c",
             "keyword": [
                 "public data",
                 "FOIA",
                 "request"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-22T12:25:28-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "TSA Freedom of Information Act (FOIA) Branch"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "TSA FOIA Reading Room - Quarterly FOIA Log"
         },
-            "identifier": "TSA-cde7f7f9-b081-4389-ad30-a85f1325ae5c",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "FOIA requests posted to the FOIA electronic reading room for TSA Contact Center Quarterly Reports.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.tsa.gov/foia/readingroom"
                 }
-            ]
-        },
-        {
-            "title": "TSA FOIA Reading Room - TSA Contact Center (TCC) Quarterly Report",
-            "description": "FOIA requests posted to the FOIA electronic reading room for TSA Contact Center Quarterly Reports.",
+            ],
+            "identifier": "TSA-e2b8f496-0f0d-4049-bebf-5b1492c88001",
             "keyword": [
                 "public data",
                 "FOIA",
                 "request"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-22T12:25:28-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "TSA Freedom of Information Act (FOIA) Branch"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "TSA FOIA Reading Room - TSA Contact Center (TCC) Quarterly Report"
         },
-            "identifier": "TSA-e2b8f496-0f0d-4049-bebf-5b1492c88001",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "FOIA requests posted to the FOIA electronic reading room for TSA complaints.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.tsa.gov/foia/readingroom"
                 }
-            ]
-        },
-        {
-            "title": "TSA FOIA Reading Room - TSA Complaints",
-            "description": "FOIA requests posted to the FOIA electronic reading room for TSA complaints.",
+            ],
+            "identifier": "TSA-6385a84a-2e8f-4ccd-a66d-25f78df6c400",
             "keyword": [
                 "complaints",
                 "public data",
                 "FOIA",
                 "request"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-22T12:25:28-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "TSA Freedom of Information Act (FOIA) Branch"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "TSA FOIA Reading Room - TSA Complaints"
         },
-            "identifier": "TSA-6385a84a-2e8f-4ccd-a66d-25f78df6c400",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "FOIA requests posted to the FOIA electronic reading room for TSA rail complaint data",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.tsa.gov/foia/readingroom"
                 }
-            ]
-        },
-        {
-            "title": "TSA FOIA Reading Room - Rail Complaint Data (CY 2014-2016)",
-            "description": "FOIA requests posted to the FOIA electronic reading room for TSA rail complaint data",
+            ],
+            "identifier": "TSA-b4515ece-bd08-490f-8bf3-25c3ada1779b",
             "keyword": [
                 "complaints",
                 "public data",
@@ -3624,212 +3639,212 @@
                 "request",
                 "rail"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-22T12:25:28-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "TSA Freedom of Information Act (FOIA) Branch"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "TSA FOIA Reading Room - Rail Complaint Data (CY 2014-2016)"
         },
-            "identifier": "TSA-b4515ece-bd08-490f-8bf3-25c3ada1779b",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "TSA has implemented congressionally mandated security fees to help finance the increased cost of securing the nation's aviation transportation system. The revenue generated from these security fees is utilized to help ensure the safe and efficient flow of people and commerce.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.tsa.gov/foia/readingroom"
+                    "accessURL": "https://www.tsa.gov/for-industry/security-fees"
                 }
-            ]
-        },
-        {
-            "title": "Passenger Fee",
-            "description": "TSA has implemented congressionally mandated security fees to help finance the increased cost of securing the nation's aviation transportation system. The revenue generated from these security fees is utilized to help ensure the safe and efficient flow of people and commerce.",
+            ],
+            "identifier": "TSA-81eab61d-534a-42f6-8d09-97f0e44b6fab",
             "keyword": [
                 "Passenger Fee",
                 "Security Fee"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2023-05-25T14:27:18-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Passenger Fee"
         },
-            "identifier": "TSA-81eab61d-534a-42f6-8d09-97f0e44b6fab",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Airport prohibited items detected overlay with geography or time hierarchy",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.tsa.gov/for-industry/security-fees"
+                    "accessURL": "https://www.tsa.gov/travel/security-screening/whatcanibring"
                 }
-            ]
-        },
-        {
-            "title": "Prohibited Items",
-            "description": "Airport prohibited items detected overlay with geography or time hierarchy",
+            ],
+            "identifier": "TSA-3212a3cf-f541-4131-85eb-a6d8ecdbf43d",
             "keyword": [
                 "Prohibited Item",
                 "Carry-On"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2023-12-28T13:22:11-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "TSA.GOV Public Website"
             },
+            "rights": null,
+            "title": "Prohibited Items"
+        },
+        {
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "024:040"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Open Data (MGMT)",
                 "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-            "identifier": "TSA-3212a3cf-f541-4131-85eb-a6d8ecdbf43d",
-            "accessLevel": "public",
-            "bureauCode": [
-                "024:056"
+            "description": "USSS contract and procurment management dataset built off of Unison's PRISM COTS application (to be decommissioned and procurement data set merges into CLM on 6/15/2022)",
+            "identifier": "USSS_PRISM_141",
+            "keyword": [
+                "none"
             ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2022-06-28T09:02:47-04:00",
             "programCode": [
                 "024:000"
             ],
-            "license": "https://www.usa.gov/government-works",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "USSS CFO"
+            },
             "rights": null,
-            "distribution": [
+            "title": "PRISM"
+        },
         {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.tsa.gov/travel/security-screening/whatcanibring"
-                }
-            ]
-        },
-        {
-            "title": "PRISM",
-            "description": "USSS contract and procurment management dataset built off of Unison's PRISM COTS application (to be decommissioned and procurement data set merges into CLM on 6/15/2022)",
-            "keyword": [
-                "none"
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "024:040"
             ],
-            "modified": "2022-06-28T09:02:47-04:00",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "USSS CFO"
-            },
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Open Data (MGMT)",
                 "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-            "identifier": "USSS_PRISM_141",
-            "accessLevel": "non-public",
-            "bureauCode": [
-                "024:040"
-            ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
-        },
-        {
-            "title": "CLM",
             "description": "USSS contract and procurment management dataset built off of Oracle ERP module CLM application",
+            "identifier": "USSS_CLM_142",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-06-28T09:02:47-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "USSS CFO"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "CLM"
         },
-            "identifier": "USSS_CLM_142",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:040"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Oracle Federal Financials",
             "description": "USSS employee travel and expense management dataset built off of Oracle Federal Financials COTS applications",
+            "identifier": "USSS_OFF_143",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-06-28T09:02:47-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "USSS CFO"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Oracle Federal Financials"
         },
-            "identifier": "USSS_OFF_143",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:040"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Sunflower Asset",
             "description": "USSS Asset tracking data set",
+            "identifier": "USSS_ASSETS_145",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-06-28T09:02:47-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "USSS CFO"
             },
+            "rights": null,
+            "title": "Sunflower Asset"
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "024:056"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Open Data (MGMT)",
                 "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-            "identifier": "USSS_ASSETS_145",
-            "accessLevel": "non-public",
-            "bureauCode": [
-                "024:040"
-            ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
-        },
-        {
-            "title": "Cargo Quantity Reporting",
             "description": "Provides entities that perform air cargo screening with the capability to enter and report the amount of air cargo they tendered to an air carrier  the amount screened  and the amount the air carrier uplifted.  This information enables TSA to audit and verify compliance with the 100% screening mandate in the Implementing Recommendations of the 9/11 Commission Act of 2007",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.tsa.gov/for-industry/cargo-programs"
+                }
+            ],
+            "identifier": "TSA-3b6cef3f-3047-443d-8a5c-ca16375a85e9",
             "keyword": [
                 "Screening",
                 "Air Carrier Compliance Reporting",
@@ -3841,277 +3856,277 @@
                 "FAS",
                 "Freight Assessment Tool"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2023-05-25T14:27:17-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Air Cargo Charters"
             },
+            "rights": null,
+            "title": "Cargo Quantity Reporting"
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "024:070"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Open Data (MGMT)",
                 "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-            "identifier": "TSA-3b6cef3f-3047-443d-8a5c-ca16375a85e9",
-            "accessLevel": "public",
-            "bureauCode": [
-                "024:056"
-            ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "description": "The Community Rating System (CRS) is a voluntary incentive program that recognizes and encourages community floodplain management practices that exceed the minimum requirements of the National Flood Insurance Program (NFIP).  Active CRS community flood insurance premium rates are discounted to reflect the reduced flood risk resulting from the community\u2019s efforts that address the three goals of the program: 1. Reduce and avoid flood damage to insurable property; 2. Strengthen and support the insurance aspects of the National Flood Insurance Program; and 3. Foster comprehensive floodplain management.  rnrnThe Flood insurance premium rates in Community Rating System communities are discounted in increments of 5%. A Class 10 community is not participating in the CRS and receives no discount. A Class 9 community receives a 5% discount for all policies in its Special Flood Hazard Areas, a Class 8 community receives a 10% discount, all the way to a Class 1 community, which receives a 45% premium discount. Classifications are based on 19 creditable activities, organized in four categories: Public Information, Mapping and Regulations, Flood Damage Reduction, Warning and Response.  Quantitative CRS datasets are avaialble about community floodplain mangament practices that validates the CRS community rating classifications and credit points. The abridged public dataset is available at https://www.fema.gov/floodplain-management/community-rating-system.  CRS dataset is updated semiannually in CIS.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.tsa.gov/for-industry/cargo-programs"
+                    "accessURL": "https://www.fema.gov/floodplain-management/community-rating-system#participating"
                 }
-            ]
-        },
-        {
-            "title": "National Flood Insurance Program (NFIP) - Community Rating System Dataset",
-            "description": "The Community Rating System (CRS) is a voluntary incentive program that recognizes and encourages community floodplain management practices that exceed the minimum requirements of the National Flood Insurance Program (NFIP).  Active CRS community flood insurance premium rates are discounted to reflect the reduced flood risk resulting from the community\u2019s efforts that address the three goals of the program: 1. Reduce and avoid flood damage to insurable property; 2. Strengthen and support the insurance aspects of the National Flood Insurance Program; and 3. Foster comprehensive floodplain management.  rnrnThe Flood insurance premium rates in Community Rating System communities are discounted in increments of 5%. A Class 10 community is not participating in the CRS and receives no discount. A Class 9 community receives a 5% discount for all policies in its Special Flood Hazard Areas, a Class 8 community receives a 10% discount, all the way to a Class 1 community, which receives a 45% premium discount. Classifications are based on 19 creditable activities, organized in four categories: Public Information, Mapping and Regulations, Flood Damage Reduction, Warning and Response.  Quantitative CRS datasets are avaialble about community floodplain mangament practices that validates the CRS community rating classifications and credit points. The abridged public dataset is available at https://www.fema.gov/floodplain-management/community-rating-system.  CRS dataset is updated semiannually in CIS.",
+            ],
+            "identifier": "FEMA-0136",
             "keyword": [
                 "Assessments"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-10-02T14:25:01-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Hazard Mitigation Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "National Flood Insurance Program (NFIP) - Community Rating System Dataset"
         },
-            "identifier": "FEMA-0136",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "The National Flood Insurance Program (NFIP) Community Status Book Dataset contains information on the participation status of a jurisdiction with land use authority, along with attribution of  Community Rating System (CRS) status, risk map effective dates. The NFIP enables property owners to purchase flood insurance. In return, communities agree to adopt and implement local floodplain management regulations that contribute to protecting lives and reducing flood risk in identified floodplains .  The NFIP Community Status Book contains the current NFIP participation status of a community that joins the program.  A community can fall into one of three NFIP status categories: 1. Participate in the NFIP; 2. Does not participate in the NFIP; or 3. Is suspended or withdrawn.  A NFIP community status is an indicator variable for disaster assistance consideration process.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/floodplain-management/community-rating-system#participating"
+                    "accessURL": "https://www.fema.gov/api/open/v1/NfipCommunityStatusBook"
                 }
-            ]
-        },
-        {
-            "title": "National Flood Insurance Program (NFIP) - Community Status Book Dataset",
-            "description": "The National Flood Insurance Program (NFIP) Community Status Book Dataset contains information on the participation status of a jurisdiction with land use authority, along with attribution of  Community Rating System (CRS) status, risk map effective dates. The NFIP enables property owners to purchase flood insurance. In return, communities agree to adopt and implement local floodplain management regulations that contribute to protecting lives and reducing flood risk in identified floodplains .  The NFIP Community Status Book contains the current NFIP participation status of a community that joins the program.  A community can fall into one of three NFIP status categories: 1. Participate in the NFIP; 2. Does not participate in the NFIP; or 3. Is suspended or withdrawn.  A NFIP community status is an indicator variable for disaster assistance consideration process.",
+            ],
+            "identifier": "FEMA-0137",
             "keyword": [
                 "Assessments"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-12-02T10:48:00-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Hazard Mitigation Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "National Flood Insurance Program (NFIP) - Community Status Book Dataset"
         },
-            "identifier": "FEMA-0137",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "The National Public Warning System (NPWS), also known as Primary Entry Point (PEP) stations, are radio broadcast stations that work with FEMA to provide emergency alert and warning information to the public before, during and after incidents and disasters. The FEMA NPWS also serves as the primary source of initial broadcast for a national alert. NPWS stations are equipped with back-up communications equipment and power generators designed to enable them to continue broadcasting information to the public during and after an event. The NPWS can directly reach more than 90 %of the U.S. population and ensures that under all conditions the President can alert and warn the public.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v1/NfipCommunityStatusBook"
+                    "accessURL": "https://usfema.sharepoint.com/sites/OAI/ncp/ipaws/SitePages/Integrated-Public-Alerts-and-Warning-System.aspx"
                 }
-            ]
-        },
-        {
-            "title": "National Public Warning System (NPWS) Primary Entry Point (PEP) Station Asset List",
-            "description": "The National Public Warning System (NPWS), also known as Primary Entry Point (PEP) stations, are radio broadcast stations that work with FEMA to provide emergency alert and warning information to the public before, during and after incidents and disasters. The FEMA NPWS also serves as the primary source of initial broadcast for a national alert. NPWS stations are equipped with back-up communications equipment and power generators designed to enable them to continue broadcasting information to the public during and after an event. The NPWS can directly reach more than 90 %of the U.S. population and ensures that under all conditions the President can alert and warn the public.",
+            ],
+            "identifier": "FEMA-0454",
             "keyword": [
                 "Communications"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2025-01-02T13:11:38-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Federal Insurance Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "National Public Warning System (NPWS) Primary Entry Point (PEP) Station Asset List"
         },
-            "identifier": "FEMA-0454",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://usfema.sharepoint.com/sites/OAI/ncp/ipaws/SitePages/Integrated-Public-Alerts-and-Warning-System.aspx"
-                }
-            ]
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:fema-datainventoryprogram@fema.dhs.gov"
             },
-        {
-            "title": "Alerts and Warnings",
             "description": "Public alert and warning messages formatted in the Common Alerting Protocol standard  intended for public broadcast over the Emergency Alert System and Wireless Emergency Alert System",
+            "identifier": "FEMA-06316",
             "keyword": [
                 "Alert and Warning",
                 "IPAWS"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-06-28T15:06:01-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:fema-datainventoryprogram@fema.dhs.gov"
+            "rights": null,
+            "title": "Alerts and Warnings"
         },
-            "identifier": "FEMA-06316",
+        {
             "accessLevel": "public",
             "bureauCode": [
-                "024:070"
-            ],
-            "programCode": [
-                "024:000"
+                "024:010"
             ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Merit Systems Protection Board (MSPB) Survey",
             "description": "MSPB conducts surveys to measure the health of Federal merit systems and obtain employee or stakeholder perspectives on workforce issues and HR practices.",
+            "identifier": "MGMT-OCHCO-MPSB-SURVEY",
             "keyword": [
                 "MPSB",
                 "Survey",
                 "Merit Systems Protection"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MPSB"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Merit Systems Protection Board (MSPB) Survey"
         },
-            "identifier": "MGMT-OCHCO-MPSB-SURVEY",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
-        },
-        {
-            "title": "GSA Customer Satisfaction Survey",
-            "description": "Customer satisfaction survey for GSA Services.",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Customer satisfaction survey for GSA Services.",
+            "identifier": "MGMT-OCHCO-GSA-SURVEY",
             "keyword": [
                 "Survey",
                 "GSA"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "GSA"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "GSA Customer Satisfaction Survey"
         },
-            "identifier": "MGMT-OCHCO-GSA-SURVEY",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Skillsoft Percipio",
             "description": "Percipio enables DHS employees to access learning content on any mobile device, tablet, or computer, using AI algorithms recommendation capabilities to serve learners with curated content based on their interests, and those of learners with similar profiles. Federal learners can access Percipio through personal devices such as computer, tablet or smartphone and also Government furnished equipment such as laptops and smartphones.",
+            "identifier": "MGMT-OCHCO-SKILLSOFT-PERCIPIO",
             "keyword": [
                 "Training",
                 "Mobile"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-26T14:49:45-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Skillsoft Percipio"
         },
-            "identifier": "MGMT-OCHCO-SKILLSOFT-PERCIPIO",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "OPM USA Performance",
             "description": "USA Performance automates the planning, progress review, and rating processes of performance management",
+            "identifier": "MGMT-OCHCO-OPM-USAPERFORMANCE",
             "keyword": [
                 "Employee",
                 "OPM",
                 "Performance Management"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "OPM"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "OPM USA Performance"
         },
-            "identifier": "MGMT-OCHCO-OPM-USAPERFORMANCE",
+        {
             "accessLevel": "public",
             "bureauCode": [
-                "024:010"
-            ],
-            "programCode": [
-                "024:000"
+                "024:054"
             ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "I-94 Automation FAQs",
             "description": "In order to increase efficiency, reduce operating costs and streamline the admissions process, U.S. Customs and Border Protection has automated Form I-94 at air and sea ports of entry. The paper form will no longer be provided to a traveler upon arrival, except in limited circumstances. The traveler will be provided with a CBP admission stamp on their travel document.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.cbp.gov/sites/default/files/assets/documents/2016-Mar/i-94-automation-fact-sheet.pdf"
+                }
+            ],
+            "identifier": "CBP-000114",
             "keyword": [
                 "Map",
                 "Land",
@@ -4124,71 +4139,65 @@
                 "Passenger",
                 "Passenger Manifest"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:23-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "PSPD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "I-94 Automation FAQs"
         },
-            "identifier": "CBP-000114",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:054"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Contains the attendee's registration information",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.cbp.gov/sites/default/files/assets/documents/2016-Mar/i-94-automation-fact-sheet.pdf"
+                    "accessURL": "https://apps.cbp.gov/te_registration"
                 }
-            ]
-        },
-        {
-            "title": "TER On-line Registration Form",
-            "description": "Contains the attendee's registration information",
+            ],
+            "identifier": "CBP-000189",
             "keyword": [
                 "Trade",
                 "Registration",
                 "Event"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:24-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "BEMSD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "TER On-line Registration Form"
         },
-            "identifier": "CBP-000189",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:054"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://apps.cbp.gov/te_registration"
-                }
-            ]
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "U.S. Customs and Border Protection Import Trade Trends - FY 2011, Year-End Report",
             "description": "U.S. Customs and Border Protection is pleased to present the Import Trade Trends Report. This report is produced semiannually and features graphical analysis and trade highlights. While U.S. Census Bureau has been producing monthly trade statistics at the aggregate level, this report is designed to trace major trade patterns and their impact on CBP workload and initiatives.",
+            "identifier": "CBP-000209",
             "keyword": [
                 "Access",
                 "Admission",
@@ -4214,30 +4223,30 @@
                 "Trademark",
                 "Transactions"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:24-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "CSPD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "U.S. Customs and Border Protection Import Trade Trends - FY 2011, Year-End Report"
         },
-            "identifier": "CBP-000209",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:054"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "U.S. Customs and Border Protection Import Trade Trends -FY2012, Year-End Report",
             "description": "U.S. Customs and Border Protection is pleased to present the Import Trade Trends Report. This report is produced semiannually and features graphical analysis and trade highlights. While U.S. Census Bureau has been producing monthly trade statistics at the aggregate level, this report is designed to trace major trade patterns and their impact on CBP workload and initiatives.",
+            "identifier": "CBP-000210",
             "keyword": [
                 "Access",
                 "Admission",
@@ -4263,30 +4272,30 @@
                 "Trademark",
                 "Transactions"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:24-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "CSPD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "U.S. Customs and Border Protection Import Trade Trends -FY2012, Year-End Report"
         },
-            "identifier": "CBP-000210",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:054"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "U.S. Customs and Border Protection Top 5000 Importers FY 2012",
             "description": "The fiscal year 2012 Top 5000 Importer List is based on import value sorted alphabetically by company name.",
+            "identifier": "CBP-000211",
             "keyword": [
                 "Access",
                 "Admission",
@@ -4312,30 +4321,36 @@
                 "Trademark",
                 "Transactions"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:24-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "CSPD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "U.S. Customs and Border Protection Top 5000 Importers FY 2012"
         },
-            "identifier": "CBP-000211",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:054"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "CBP Border Wait Times",
             "description": "Estimated wait times for northern and southern border crossings.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "http://apps.cbp.gov/bwt/"
+                }
+            ],
+            "identifier": "CBP-000047",
             "keyword": [
                 "Boarders",
                 "Border Crossing",
@@ -4346,69 +4361,69 @@
                 "Status",
                 "Wait Time"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:25-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "BEMSD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "CBP Border Wait Times"
         },
-            "identifier": "CBP-000047",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:054"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "These sites provide assistance to those individuals who at the time of entry into the United States were scheduled for a deferred inspection or believe that the documentation and corresponding endorsements issued at the port of entry require review and possible correction.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "http://apps.cbp.gov/bwt/"
+                    "accessURL": "https://www.cbp.gov/document/guidance/deferred-inspection-sites"
                 }
-            ]
-        },
-        {
-            "title": "CBP Deferred Inspection Sites",
-            "description": "These sites provide assistance to those individuals who at the time of entry into the United States were scheduled for a deferred inspection or believe that the documentation and corresponding endorsements issued at the port of entry require review and possible correction.",
+            ],
+            "identifier": "CBP-000052",
             "keyword": [
                 "Port of Entry"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:25-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "PSPD"
             },
+            "rights": null,
+            "title": "CBP Deferred Inspection Sites"
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "024:054"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Open Data (MGMT)",
                 "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-            "identifier": "CBP-000052",
-            "accessLevel": "public",
-            "bureauCode": [
-                "024:054"
+            "description": "Products that infringe on U.S. trademarks, copyrights, and patents threaten the health and safety of American consumers, our economy, and our national security. U.S. Customs and Border Protection) and U.S. Immigration and Customs Enforcement-s Homeland Security Investigations continued Intellectual Property Rights enforcement against these illicit imports mitigates the financial and welfare risk",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "http://www.cbp.gov/trade/priority-issues/ipr/statistics"
+                }
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.cbp.gov/document/guidance/deferred-inspection-sites"
-                }
-            ]
-        },
-        {
-            "title": "CBP Intellectual Property Rights (IPR) Annual Seizure Statistics",
-            "description": "Products that infringe on U.S. trademarks, copyrights, and patents threaten the health and safety of American consumers, our economy, and our national security. U.S. Customs and Border Protection) and U.S. Immigration and Customs Enforcement-s Homeland Security Investigations continued Intellectual Property Rights enforcement against these illicit imports mitigates the financial and welfare risk",
+            "identifier": "CBP-000055",
             "keyword": [
                 "Access",
                 "Duty Collection",
@@ -4424,36 +4439,36 @@
                 "Patent",
                 "Trademark"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:25-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "CSPD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "CBP Intellectual Property Rights (IPR) Annual Seizure Statistics"
         },
-            "identifier": "CBP-000055",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:054"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "This datasets provides a Port of Entry in any state by clicking on the map.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "http://www.cbp.gov/trade/priority-issues/ipr/statistics"
+                    "accessURL": "http://www.cbp.gov/contact/ports"
                 }
-            ]
-        },
-        {
-            "title": "CBP List of of Port of Entries by Land, Air and Sea",
-            "description": "This datasets provides a Port of Entry in any state by clicking on the map.",
+            ],
+            "identifier": "CBP-000056",
             "keyword": [
                 "Map",
                 "Land",
@@ -4462,36 +4477,36 @@
                 "Boarder",
                 "Passenger Manifest"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:25-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "PSPD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "CBP List of of Port of Entries by Land, Air and Sea"
         },
-            "identifier": "CBP-000056",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:054"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "CBP Preclearance provides for the U.S. border inspection and clearance of commercial air passengers and their goods at (15) locations in (6) foreign countries. CBP Preclearance is focused solely on passenger processing (no cargo). Processing includes anything a traveler is bringing into the U.S. that belongs to them, for example: their luggage, clothing, souvenirs and any other personal effects.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "http://www.cbp.gov/contact/ports"
+                    "accessURL": "http://www.cbp.gov/border-security/ports-entry/operations/preclearance"
                 }
-            ]
-        },
-        {
-            "title": "CBP List of Preclearance Locations",
-            "description": "CBP Preclearance provides for the U.S. border inspection and clearance of commercial air passengers and their goods at (15) locations in (6) foreign countries. CBP Preclearance is focused solely on passenger processing (no cargo). Processing includes anything a traveler is bringing into the U.S. that belongs to them, for example: their luggage, clothing, souvenirs and any other personal effects.",
+            ],
+            "identifier": "CBP-000057",
             "keyword": [
                 "Port of Entry",
                 "Boarder",
@@ -4500,36 +4515,36 @@
                 "Passenger",
                 "Passenger Manifest"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:25-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "PSPD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "CBP List of Preclearance Locations"
         },
-            "identifier": "CBP-000057",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:054"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Quota information is issued for the trade community by the Quota Enforcement Administration Branch within the Office of International Trade. The Quota Bulletins have replaced the previous Quota Book Transmittals. Current and relevant previous year bulletins are organized by year of issuance.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "http://www.cbp.gov/border-security/ports-entry/operations/preclearance"
+                    "accessURL": "http://www.cbp.gov/trade/quota/bulletins"
                 }
-            ]
-        },
-        {
-            "title": "CBP Quota Bulletins",
-            "description": "Quota information is issued for the trade community by the Quota Enforcement Administration Branch within the Office of International Trade. The Quota Bulletins have replaced the previous Quota Book Transmittals. Current and relevant previous year bulletins are organized by year of issuance.",
+            ],
+            "identifier": "CBP-000061",
             "keyword": [
                 "Import",
                 "Transfer",
@@ -4542,1592 +4557,1586 @@
                 "Transactions",
                 "Admission"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:25-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "CSPD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "CBP Quota Bulletins"
         },
-            "identifier": "CBP-000061",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:054"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "E-Allegations is an online web page that provides a procedure by which concerned individuals can report suspected illegal import and export activity. By completing and submitting the form, the public can help CBP prevent international trade violations. The e-Allegations form feeds data in real-time to the Commercial Allegation Recording System (CARS), which enables CBP to escalate serious violations expediently. Submissions are received by the Commercial Targeting and Enforcement Division, Office of International Trade",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "http://www.cbp.gov/trade/quota/bulletins"
+                    "accessURL": "https://www.cbp.gov/trade/e-allegations"
                 }
-            ]
-        },
-        {
-            "title": "e-allegations",
-            "description": "E-Allegations is an online web page that provides a procedure by which concerned individuals can report suspected illegal import and export activity. By completing and submitting the form, the public can help CBP prevent international trade violations. The e-Allegations form feeds data in real-time to the Commercial Allegation Recording System (CARS), which enables CBP to escalate serious violations expediently. Submissions are received by the Commercial Targeting and Enforcement Division, Office of International Trade",
+            ],
+            "identifier": "CBP-000089",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:25-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "BEMSD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "e-allegations"
         },
-            "identifier": "CBP-000089",
+        {
             "accessLevel": "public",
             "bureauCode": [
-                "024:054"
-            ],
-            "programCode": [
-                "024:000"
+                "024:058"
             ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.cbp.gov/trade/e-allegations"
-                }
-            ]
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "FLETA.gov",
             "description": "The Federal Law Enforcement Accreditation (FLETA) dataset contains training, events, and news information for this effort.",
+            "identifier": "FLETC-07160-FLETC-DIR01",
             "keyword": [
                 "training accreditation events"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-03-01T11:54:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "FLETA.gov"
         },
-            "identifier": "FLETC-07160-FLETC-DIR01",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:058"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "FLETC.gov",
             "description": "This dataset contains the information that FLETC makes public for potential students, staff, and visitors.",
+            "identifier": "FLETC-07183-FGOV-DIR01",
             "keyword": [
                 "public FLETC information"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-03-01T11:54:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "FLETC.gov"
         },
-            "identifier": "FLETC-07183-FGOV-DIR01",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:058"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "USAJOBS-FLETC",
             "description": "This USAJOBS-FLETC dataset contains FLETC specific recruitment and job posting data.",
+            "identifier": "FLETC-05911-JOBSF-DIR01",
             "keyword": [
                 "recruitment jobs"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-03-01T11:54:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
+            "rights": null,
+            "title": "USAJOBS-FLETC"
+        },
+        {
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "024:010"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Open Data (MGMT)",
                 "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-            "identifier": "FLETC-05911-JOBSF-DIR01",
-            "accessLevel": "public",
-            "bureauCode": [
-                "024:058"
-            ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
-        },
-        {
-            "title": "Homeland Security Information Network",
             "description": "HSIN is the Department of Homeland Security's official system for trusted sharing of Sensitive But Unclassified information between federal, state, local, territorial, tribal, international and private sector partners.",
+            "identifier": "SDD-78",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "HSIN Program"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Homeland Security Information Network"
         },
-            "identifier": "SDD-78",
-            "accessLevel": "restricted public",
+        {
+            "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "OPM USAStaffing",
             "description": "USA Staffing",
+            "identifier": "MGMT-OCHCO-OPM-USAS",
             "keyword": [
                 "OPM",
                 "Staffing"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-03-06T14:40:15-05:00",
-            "publisher": {
-                "@type": "org:Organization",
+            "programCode": [
+                "024:000"
+            ],
+            "publisher": {
+                "@type": "org:Organization",
                 "name": "OPM"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "OPM USAStaffing"
         },
-            "identifier": "MGMT-OCHCO-OPM-USAS",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Electronic Official Personnel File (eOPF)",
             "description": "The Office of Personnel Management (OPM) allows DHS users secure access to their electronic official personnel folder",
+            "identifier": "MGMT-OCHCO-OPM-EOPF",
             "keyword": [
                 "OPM",
                 "Personnel files",
                 "electronic"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-03-06T14:43:20-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "OPM"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Electronic Official Personnel File (eOPF)"
         },
-            "identifier": "MGMT-OCHCO-OPM-EOPF",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "NFC - Payroll/Personnel System (PPS)",
             "description": "NFC Payroll/Personnel System PPS is an online database that maintains employee personnel records, time and attendance reports, and processes a biweekly payroll. The system as a whole includes EPICWeb, FOCUS NFC reporting, Table Management and Web SPPS.",
+            "identifier": "MGMT-OCHCO-NFC-PPS",
             "keyword": [
                 "NFC",
                 "USDA",
                 "employee"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-03-06T14:44:58-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NFC"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NFC - Payroll/Personnel System (PPS)"
         },
-            "identifier": "MGMT-OCHCO-NFC-PPS",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "OPM USA Surveys",
             "description": "The Senior Executive Service Candidate Development Program (SES CDP) prepares high-performing senior staff for the Senior Executive Service (SES) through an intensive leadership development program that lasts approximately 12 to 18 months. As part of the SES CDP, candidates are required to attend a three-day Senior Executive Assessment Program (SEAP) to identify ECQ competency gaps and assess overall readiness for senior leadership responsibilities. The SEAP includes a web-based multi-rater assessment process to collect feedback from the SES CDP candidate, as well as his/her boss, peers and direct reports. Data is collected via an online assessment tool using raters names and DHS email addresses, which would be provided in advance by SES CDP candidates to program administrators. PII data required for survey deployment is limited to names, email addresses and the category of relationship between the program candidate and the rater (Boss, Peer, Direct Report, Other). When assessment results are reviewed with the SES CDP candidate, this is generally delivered in a one-on-one feedback session between the participant and an assigned vendor coach/observer.",
+            "identifier": "MGMT-OCHCO-OPM-OPMSURVEYS",
             "keyword": [
                 "OPM"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "OPM"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "OPM USA Surveys"
         },
-            "identifier": "MGMT-OCHCO-OPM-OPMSURVEYS",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "The Mentoring Connection (TMC)",
             "description": "The Mentoring Connection (TMC) is an innovative web-based program designed to help manage the logistics of your mentoring programs and partnerships. TMC offers cohorts the opportunity to apply to the mentoring program on-line and all application and mentoring matching, calendar of events and program evaluations.",
+            "identifier": "MGMT-OCHCO-VPE-TMC",
             "keyword": [
                 "mentoring"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-03-06T14:46:26-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "The Mentoring Connection (TMC)"
         },
-            "identifier": "MGMT-OCHCO-VPE-TMC",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "FedHR Navigator",
             "description": "Data contained within FHR Navigator",
+            "identifier": "MGMT-OCHCO-ECONSYS-FHRNAVIGATOR",
             "keyword": [
                 "Benefits"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-11-13T09:50:07-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "FedHR Navigator"
         },
-            "identifier": "MGMT-OCHCO-ECONSYS-FHRNAVIGATOR",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "OPM USA Survey",
             "description": "workforce climate survey",
+            "identifier": "MGMT-OCHCO-OPM-USASURVEY",
             "keyword": [
                 "OPM",
                 "Survey"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "OPM"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "OPM USA Survey"
         },
-            "identifier": "MGMT-OCHCO-OPM-USASURVEY",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Human Capital Reporting",
             "description": "Human Capital Reporting tools",
+            "identifier": "MGMT-OCHCO-VPE-HCREPORTING",
             "keyword": [
                 "Human Capital",
                 "Reporting"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-08-19T14:23:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Human Capital Reporting"
         },
-            "identifier": "MGMT-OCHCO-VPE-HCREPORTING",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Parking and Transit Subsidy Application Tool (PTSAT)",
             "description": "The purpose of the PTSAT Application is to provide a paperless workflow tool that will assist DHS enrollees in the process of applying for transit and parking benefits. There is currently a paper form which is manually filled out and then faxed to the program office. This application tool will eliminate the paper process and faxing requirement. This tool will allow each enrollee to apply electronically and receive approval from their supervisor using the email account system. The system has a backend reporting tool which provides the parking and transit program managers access to maintaining electronic folders and ad hoc reporting functionality. This system will eliminate the manual processing of over 200 applications monthly. It will also eliminate the manual validation of over 2,500 headquarters participants.",
+            "identifier": "MGMT-OCHCO-PTSAT-TOOL",
             "keyword": [
                 "Parking",
                 "Transit Subsidy"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Parking and Transit Subsidy Application Tool (PTSAT)"
         },
-            "identifier": "MGMT-OCHCO-PTSAT-TOOL",
+        {
             "accessLevel": "public",
             "bureauCode": [
-                "024:010"
-            ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
-        },
-        {
-            "title": "Unclaimed Money at Airports in Fiscal Year 2017",
-            "description": "Congress has directed TSA to provide an annual accounting of the amount of unclaimed money recovered in total and at each individual airport. TSA also is directed to describe how that money is being used to provide civil aviation security.  This report provides the amount of unclaimed money recovered during FY 2017.",
-            "keyword": [
-                "Airports",
-                "Unclaimed Money",
-                "Loose Change"
+                "024:056"
             ],
-            "modified": "2024-02-29T10:46:59-05:00",
-            "publisher": {
-                "@type": "org:Organization",
-                "name": "Office of the Administrator"
-            },
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Open Data (MGMT)",
                 "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-            "identifier": "TSA-1d5ed30b-17fb-4f85-a9e8-f8ad2546f497",
-            "accessLevel": "public",
-            "bureauCode": [
-                "024:056"
-            ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "description": "Congress has directed TSA to provide an annual accounting of the amount of unclaimed money recovered in total and at each individual airport. TSA also is directed to describe how that money is being used to provide civil aviation security.  This report provides the amount of unclaimed money recovered during FY 2017.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dhs.gov/sites/default/files/publications/TSA%20-%20Unclaimed%20Money%20at%20Airports%2C%20Fiscal%20Year%202017.pdf"
                 }
-            ]
-        },
-        {
-            "title": "Unclaimed Money at Airports in Fiscal Year 2018",
-            "description": "Congress has directed TSA to provide an annual accounting of the amount of unclaimed money recovered in total and at each individual airport. TSA also is directed to describe how that money is being used to provide civil aviation security.  This report provides the amount of unclaimed money recovered during FY 2018.",
+            ],
+            "identifier": "TSA-1d5ed30b-17fb-4f85-a9e8-f8ad2546f497",
             "keyword": [
                 "Airports",
                 "Unclaimed Money",
                 "Loose Change"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-29T10:46:59-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Administrator"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Unclaimed Money at Airports in Fiscal Year 2017"
         },
-            "identifier": "TSA-11c7c139-bf4c-4be5-bb16-fdd1c1beb423",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Congress has directed TSA to provide an annual accounting of the amount of unclaimed money recovered in total and at each individual airport. TSA also is directed to describe how that money is being used to provide civil aviation security.  This report provides the amount of unclaimed money recovered during FY 2018.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dhs.gov/sites/default/files/publications/tsa_-_unclaimed_money_at_airports_in_fy_2018_0.pdf"
                 }
-            ]
-        },
-        {
-            "title": "Unclaimed Money at Airports in Fiscal Year 2019",
-            "description": "Congress has directed TSA to provide an annual accounting of the amount of unclaimed money recovered in total and at each individual airport. TSA also is directed to describe how that money is being used to provide civil aviation security.  This report provides the amount of unclaimed money recovered during FY 2019.",
+            ],
+            "identifier": "TSA-11c7c139-bf4c-4be5-bb16-fdd1c1beb423",
             "keyword": [
                 "Airports",
                 "Unclaimed Money",
                 "Loose Change"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-29T10:46:59-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Administrator"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Unclaimed Money at Airports in Fiscal Year 2018"
         },
-            "identifier": "TSA-38932c23-d900-4a30-af5a-e7647e61fe97",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Congress has directed TSA to provide an annual accounting of the amount of unclaimed money recovered in total and at each individual airport. TSA also is directed to describe how that money is being used to provide civil aviation security.  This report provides the amount of unclaimed money recovered during FY 2019.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.dhs.gov/sites/default/files/publications/tsa_-_unclaimed_money_at_airports_in_fy_2019_0.pdf"
                 }
-            ]
-        },
-        {
-            "title": "Unclaimed Money at Airports in Fiscal Year 2020",
-            "description": "Congress has directed TSA to provide an annual accounting of the amount of unclaimed money recovered in total and at each individual airport. TSA also is directed to describe how that money is being used to provide civil aviation security.  This report provides the amount of unclaimed money recovered during FY 2020.",
+            ],
+            "identifier": "TSA-38932c23-d900-4a30-af5a-e7647e61fe97",
             "keyword": [
                 "Airports",
                 "Unclaimed Money",
                 "Loose Change"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-29T10:46:59-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Administrator"
             },
+            "rights": null,
+            "title": "Unclaimed Money at Airports in Fiscal Year 2019"
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "024:056"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Open Data (MGMT)",
                 "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
+            "description": "Congress has directed TSA to provide an annual accounting of the amount of unclaimed money recovered in total and at each individual airport. TSA also is directed to describe how that money is being used to provide civil aviation security.  This report provides the amount of unclaimed money recovered during FY 2020.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.dhs.gov/sites/default/files/publications/tsa_-_unclaimed_money_at_airports_in_fiscal_year_2020.pdf"
+                }
+            ],
             "identifier": "TSA-ab042b4f-7a95-41fb-b52b-4d14175fa869",
-            "accessLevel": "public",
-            "bureauCode": [
-                "024:056"
+            "keyword": [
+                "Airports",
+                "Unclaimed Money",
+                "Loose Change"
             ],
+            "license": "https://www.usa.gov/government-works",
+            "modified": "2024-02-29T10:46:59-05:00",
             "programCode": [
                 "024:000"
             ],
-            "license": "https://www.usa.gov/government-works",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the Administrator"
+            },
             "rights": null,
+            "title": "Unclaimed Money at Airports in Fiscal Year 2020"
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "024:056"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "A collection of TSA Claims Data from 2002 to 2017 in the DHS Publication Library.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.dhs.gov/sites/default/files/publications/tsa_-_unclaimed_money_at_airports_in_fiscal_year_2020.pdf"
+                    "accessURL": "https://www.dhs.gov/tsa-claims-data"
                 }
-            ]
-        },
-        {
-            "title": "TSA Claims Data (Calendar Years 2002-2017)",
-            "description": "A collection of TSA Claims Data from 2002 to 2017 in the DHS Publication Library.",
+            ],
+            "identifier": "TSA-b170fb44-ca3a-4deb-8559-624a9de3bbeb",
             "keyword": [
                 "FOIA",
                 "Claims"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-22T12:25:28-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "TSA Claims Data (Calendar Years 2002-2017)"
         },
-            "identifier": "TSA-b170fb44-ca3a-4deb-8559-624a9de3bbeb",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "A collection of documents related to advanced imaging technology that are frequently requested through the Freedom of Information Act (FOIA).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.dhs.gov/tsa-claims-data"
+                    "accessURL": "https://www.dhs.gov/advanced-imaging-technology-documents"
                 }
-            ]
-        },
-        {
-            "title": "TSA Advanced Imaging Technology (AIT) Documents",
-            "description": "A collection of documents related to advanced imaging technology that are frequently requested through the Freedom of Information Act (FOIA).",
+            ],
+            "identifier": "TSA-971abd2a-aeb2-46c1-9428-3cb4824856b5",
             "keyword": [
                 "AIT"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-29T10:46:59-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "TSA Advanced Imaging Technology (AIT) Documents"
         },
-            "identifier": "TSA-971abd2a-aeb2-46c1-9428-3cb4824856b5",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "An archive of TSA Wait Times Reports for 2006 to 2015.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.dhs.gov/advanced-imaging-technology-documents"
+                    "accessURL": "https://www.dhs.gov/publication/tsa-wait-times-reports"
                 }
-            ]
-        },
-        {
-            "title": "TSA Wait Times (January 2006 to December 2015)",
-            "description": "An archive of TSA Wait Times Reports for 2006 to 2015.",
+            ],
+            "identifier": "TSA-bb24d82d-86d5-4823-9291-95d657971217",
             "keyword": [
                 "Checkpoint",
                 "Wait Times",
                 "Screening"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-29T10:46:59-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "TSA Wait Times (January 2006 to December 2015)"
         },
-            "identifier": "TSA-bb24d82d-86d5-4823-9291-95d657971217",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Congress has directed TSA to provide an annual accounting of the amount of unclaimed money recovered in total and at each individual airport. TSA also is directed to describe how that money is being used to provide civil aviation security.  This report provides the amount of unclaimed money recovered during FY 2014.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.dhs.gov/publication/tsa-wait-times-reports"
+                    "accessURL": "https://www.dhs.gov/sites/default/files/publications/OCFO/Transporation%20Security%20Adminstration%20%28TSA%29%20-%20FY%202014%20Unclaimed%20Money%20at%20Airports.pdf"
                 }
-            ]
-        },
-        {
-            "title": "Unclaimed Money at Airports in Fiscal Year 2014",
-            "description": "Congress has directed TSA to provide an annual accounting of the amount of unclaimed money recovered in total and at each individual airport. TSA also is directed to describe how that money is being used to provide civil aviation security.  This report provides the amount of unclaimed money recovered during FY 2014.",
+            ],
+            "identifier": "TSA-a3a4a332-56e5-43c3-9160-0d0690d2f3db",
             "keyword": [
                 "Airports",
                 "Unclaimed Money",
                 "Loose Change"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-29T10:46:59-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Administrator"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Unclaimed Money at Airports in Fiscal Year 2014"
         },
-            "identifier": "TSA-a3a4a332-56e5-43c3-9160-0d0690d2f3db",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Congress has directed TSA to provide an annual accounting of the amount of unclaimed money recovered in total and at each individual airport. TSA also is directed to describe how that money is being used to provide civil aviation security.  This report provides the amount of unclaimed money recovered during FY 2015.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.dhs.gov/sites/default/files/publications/OCFO/Transporation%20Security%20Adminstration%20%28TSA%29%20-%20FY%202014%20Unclaimed%20Money%20at%20Airports.pdf"
+                    "accessURL": "https://www.dhs.gov/sites/default/files/publications/Transportation%20Security%20Administration%20-%20Unclaimed%20Money%20at%20Airports.pdf"
                 }
-            ]
-        },
-        {
-            "title": "Unclaimed Money at Airports in Fiscal Year 2015",
-            "description": "Congress has directed TSA to provide an annual accounting of the amount of unclaimed money recovered in total and at each individual airport. TSA also is directed to describe how that money is being used to provide civil aviation security.  This report provides the amount of unclaimed money recovered during FY 2015.",
+            ],
+            "identifier": "TSA-88f3f243-34e6-47f6-933f-29179f2f4d09",
             "keyword": [
                 "Airports",
                 "Unclaimed Money",
                 "Loose Change"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-29T10:46:59-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Administrator"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Unclaimed Money at Airports in Fiscal Year 2015"
         },
-            "identifier": "TSA-88f3f243-34e6-47f6-933f-29179f2f4d09",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Congress has directed TSA to provide an annual accounting of the amount of unclaimed money recovered in total and at each individual airport. TSA also is directed to describe how that money is being used to provide civil aviation security.  This report provides the amount of unclaimed money recovered during FY 2016.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.dhs.gov/sites/default/files/publications/Transportation%20Security%20Administration%20-%20Unclaimed%20Money%20at%20Airports.pdf"
+                    "accessURL": "https://www.dhs.gov/sites/default/files/publications/TSA%20-%20Unclaimed%20Money%20at%20Airports%20-%20Fiscal%20Year%202016.pdf"
                 }
-            ]
-        },
-        {
-            "title": "Unclaimed Money at Airports in Fiscal Year 2016",
-            "description": "Congress has directed TSA to provide an annual accounting of the amount of unclaimed money recovered in total and at each individual airport. TSA also is directed to describe how that money is being used to provide civil aviation security.  This report provides the amount of unclaimed money recovered during FY 2016.",
+            ],
+            "identifier": "TSA-d4ec5d80-2e22-4688-b7d9-be8ab7bf7feb",
             "keyword": [
                 "Airports",
                 "Unclaimed Money",
                 "Loose Change"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-29T10:46:59-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Office of the Administrator"
             },
+            "rights": null,
+            "title": "Unclaimed Money at Airports in Fiscal Year 2016"
+        },
+        {
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "024:040"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Open Data (MGMT)",
                 "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-            "identifier": "TSA-d4ec5d80-2e22-4688-b7d9-be8ab7bf7feb",
-            "accessLevel": "public",
-            "bureauCode": [
-                "024:056"
-            ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.dhs.gov/sites/default/files/publications/TSA%20-%20Unclaimed%20Money%20at%20Airports%20-%20Fiscal%20Year%202016.pdf"
-                }
-            ]
-        },
-        {
-            "title": "FREDMART",
             "description": "USSS Datamart for CFO reporting of the dataset from CFO applications - Travel, Prism, Oracle Federal Financials, NFC Payroll",
+            "identifier": "USSS_FREDMART_144",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-06-28T09:02:47-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "USSS CFO"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "FREDMART"
         },
-            "identifier": "USSS_FREDMART_144",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:040"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "http://www.ncfi.usss.gov Dataset",
             "description": "Provides users with information regarding the National Cyber Forensics Institute to include, courses, schedules, news, partners, and contact information.",
+            "identifier": "USSS_NCFI_154",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-12-06T08:01:19-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "USSS CIO"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "http://www.ncfi.usss.gov Dataset"
         },
-            "identifier": "USSS_NCFI_154",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:040"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "http://www.usdollars.usss.gov dataset",
             "description": "Allows users to electronically submit one or more suspect counterfeit notes to the United States Secret Service.",
+            "identifier": "USSS_USD_155",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-12-06T08:01:53-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "USSS CIO"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "http://www.usdollars.usss.gov dataset"
         },
-            "identifier": "USSS_USD_155",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:040"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "eProperty",
             "description": "Personal Asset module under EPERSON which keeps track property assigned to individuals and inherited from Sunflower",
+            "identifier": "USSS_EPROPERTY_91",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-06-28T09:02:48-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "USSS CIO"
             },
+            "rights": null,
+            "title": "eProperty"
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "024:070"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Open Data (MGMT)",
                 "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-            "identifier": "USSS_EPROPERTY_91",
-            "accessLevel": "non-public",
-            "bureauCode": [
-                "024:040"
-            ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
-        },
-        {
-            "title": "Youth Preparedness",
             "description": "Repository of application submission information and scorecards.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.fema.gov/emergency-managers/individuals-communities/youth-preparedness-council"
+                }
+            ],
+            "identifier": "FEMA-0109",
             "keyword": [
                 "People"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-08-01T07:58:54-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/National Preparedness Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Youth Preparedness"
         },
-            "identifier": "FEMA-0109",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Includes a variety of resources both for education, and training, feedback from the public via surveys, news articles aimed to inform and promote activities, and user account information.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/emergency-managers/individuals-communities/youth-preparedness-council"
+                    "accessURL": "https://community.fema.gov/ProtectiveActions/s/"
                 }
-            ]
-        },
-        {
-            "title": "Preparedness Actions",
-            "description": "Includes a variety of resources both for education, and training, feedback from the public via surveys, news articles aimed to inform and promote activities, and user account information.",
+            ],
+            "identifier": "FEMA-0110",
             "keyword": [
                 "Threats and Hazards"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-08-01T07:58:54-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/National Preparedness Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Preparedness Actions"
         },
-            "identifier": "FEMA-0110",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Repository of Emergency Financial First Aid Kit (EFFAK)-related resources. Includes animations and direct links to EFFAK tools in a variety of languages.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://community.fema.gov/ProtectiveActions/s/"
+                    "accessURL": "https://community.fema.gov/PreparednessCommunity/s/emergency-financial-first-aid-kit?language=en_US"
                 }
-            ]
-        },
-        {
-            "title": "Personal Resilience",
-            "description": "Repository of Emergency Financial First Aid Kit (EFFAK)-related resources. Includes animations and direct links to EFFAK tools in a variety of languages.",
+            ],
+            "identifier": "FEMA-0111",
             "keyword": [
                 "People"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-08-01T07:58:54-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/National Preparedness Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Personal Resilience"
         },
-            "identifier": "FEMA-0111",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "The dataset is an online catalog of all National Incident Management System (NIMS) resource typing definitions, job titles/position qualification sheets, and position task book templates that have been released by FEMA. RTLT provides public access to published resources.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://community.fema.gov/PreparednessCommunity/s/emergency-financial-first-aid-kit?language=en_US"
+                    "accessURL": "https://rtlt.preptoolkit.fema.gov/Public"
                 }
-            ]
-        },
-        {
-            "title": "Resource Typing Library Tool (RTLT)",
-            "description": "The dataset is an online catalog of all National Incident Management System (NIMS) resource typing definitions, job titles/position qualification sheets, and position task book templates that have been released by FEMA. RTLT provides public access to published resources.",
+            ],
+            "identifier": "FEMA-0116",
             "keyword": [
                 "Authorities"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2025-01-02T13:11:38-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/National Preparedness Directorate"
             },
+            "rights": null,
+            "title": "Resource Typing Library Tool (RTLT)"
+        },
+        {
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "024:070"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Open Data (MGMT)",
                 "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-            "identifier": "FEMA-0116",
-            "accessLevel": "public",
-            "bureauCode": [
-                "024:070"
-            ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "description": "The dataset is a collection of resource inventories from local, state, tribal, territorial, and Federal agencies as well as NGOs and other partners nationwide that are inventoried in accordance with National Incident Management System (NIMS) guidance. Dataset includes, but is not limited to, resource name, type, location, owner, and point of contacts.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://rtlt.preptoolkit.fema.gov/Public"
+                    "accessURL": "https://preptoolkit.fema.gov/web/national-resource-hub/resourceinventorying"
                 }
-            ]
-        },
-        {
-            "title": "Resource Inventory System (RIS)",
-            "description": "The dataset is a collection of resource inventories from local, state, tribal, territorial, and Federal agencies as well as NGOs and other partners nationwide that are inventoried in accordance with National Incident Management System (NIMS) guidance. Dataset includes, but is not limited to, resource name, type, location, owner, and point of contacts.",
+            ],
+            "identifier": "FEMA-0117",
             "keyword": [
                 "External Coordination"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2025-01-02T13:11:38-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/National Preparedness Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Resource Inventory System (RIS)"
         },
-            "identifier": "FEMA-0117",
+        {
             "accessLevel": "restricted public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://preptoolkit.fema.gov/web/national-resource-hub/resourceinventorying"
-                }
-            ]
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "OneResponder",
             "description": "The dataset is a collection of personnel qualification records from local, state, tribal, territorial, and Federal agencies as well as NGOs and other partners nationwide in support of the implementation of the National Qualification System (NQS). Dataset includes, but is not limited to, personnel names, organizations, assigned position types, assigned Position Task Books (PTBs), and training records.",
+            "identifier": "FEMA-0118",
             "keyword": [
                 "External Coordination"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2025-01-02T13:11:38-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/National Preparedness Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "OneResponder"
         },
-            "identifier": "FEMA-0118",
-            "accessLevel": "restricted public",
+        {
+            "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "FEMA Course Catalogs",
             "description": "This dataset contains Course Catalog information for courses delivered by National Training and Education Division (NTED) Training Providers, the Center for Domestic Preparedness (CDP), and the Emergency Management Institute (EMI) . Course Catalog information includes information such as a Description of the courses, Objectives of the courses, Target Audience, Prerequisites, etc.",
-            "keyword": [
-                "Training and Exercises"
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.firstrespondertraining.gov/frts/npccatalog"
+                }
+            ],
+            "identifier": "FEMA-0119",
+            "keyword": [
+                "Training and Exercises"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-09-09T07:52:36-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Federal Insurance Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "FEMA Course Catalogs"
         },
-            "identifier": "FEMA-0119",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "This dataset contains information on upcoming training for courses in the FEMA Course Catalog. Data included is the dates of the training, time of the training, location of the training, and information on how to sign up/register for the training (this is usually a link to the training partner's site)",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.firstrespondertraining.gov/frts/npccatalog"
+                    "accessURL": "https://www.firstrespondertraining.gov/frts/schedule"
                 }
-            ]
-        },
-        {
-            "title": "Scheduled Courses",
-            "description": "This dataset contains information on upcoming training for courses in the FEMA Course Catalog. Data included is the dates of the training, time of the training, location of the training, and information on how to sign up/register for the training (this is usually a link to the training partner's site)",
+            ],
+            "identifier": "FEMA-0123",
             "keyword": [
                 "Training and Exercises"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-09-09T07:52:36-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Federal Insurance Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Scheduled Courses"
         },
-            "identifier": "FEMA-0123",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.firstrespondertraining.gov/frts/schedule"
-                }
-            ]
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Flood Risk Products",
             "description": "Flood Risk Products go beyond the basic flood hazard information on regulatory flood hazard products. Flood Risk Products provide a deeper and user-friendly analysis of flood risks within a Risk MAP Flood Risk Project.rnrnFRPs depict and assist users to understand risk but are not regulatory products.rnrnDatapoints include number of FRPs available.",
+            "identifier": "FEMA-0156",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-05-01T10:30:18-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Federal Insurance and Mitigation Administration"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Flood Risk Products"
         },
-            "identifier": "FEMA-0156",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Lidar Elevation",
             "description": "Light Detection and Ranging (lidar) is\u202fa technology\u202fused\u202fto create high-resolution\u202fmodels of ground elevation\u202fwith\u202fa\u202fvertical accuracy\u202fof\u202f10\u202fcentimeters\u202f(4 inches).\u202f rnrnFEMA collects lidar elevation data to support flood mapping. USGS is the primary Federal steward of lidar data. FEMA archives lidar data for FEMA projects where USGS does not manage the Lidar data collection. rnrnDatapoints include ground elevation models and vertical metrics for ground elevation.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://hazards.fema.gov"
+                }
+            ],
+            "identifier": "FEMA-0157",
             "keyword": [
                 "Threats and Hazards"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-07-01T07:47:17-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Risk Management Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Lidar Elevation"
         },
-            "identifier": "FEMA-0157",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Default Hazus Statewide databases used for baseline risk assessment.rnrnHazus produces a variety of actionable risk information including physical damage, estimated social impacts, economic impacts, and cost effectiveness.rnrnEarthquake model, Flood model, Hurricane model, Tsunami model, Inventory data, Hazus General Building Stock.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://hazards.fema.gov"
+                    "accessURL": "https://www.fema.gov/flood-maps/tools-resources/flood-map-products/hazus/software"
                 }
-            ]
-        },
-        {
-            "title": "Hazus Data",
-            "description": "Default Hazus Statewide databases used for baseline risk assessment.rnrnHazus produces a variety of actionable risk information including physical damage, estimated social impacts, economic impacts, and cost effectiveness.rnrnEarthquake model, Flood model, Hurricane model, Tsunami model, Inventory data, Hazus General Building Stock.",
+            ],
+            "identifier": "FEMA-0167",
             "keyword": [
                 "Threats and Hazards"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-10-02T14:25:01-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Risk Management Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Hazus Data"
         },
-            "identifier": "FEMA-0167",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "DRC locator is a public facing website that is used for disaster survivors to see the available DRC locations available in their areas.  The information is loaded from the DRC DOT application.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/flood-maps/tools-resources/flood-map-products/hazus/software"
+                    "accessURL": "https://egateway.fema.gov/ESF6/DRCLocator"
                 }
-            ]
-        },
-        {
-            "title": "Disaster Recovery Center (DRC) Locator",
-            "description": "DRC locator is a public facing website that is used for disaster survivors to see the available DRC locations available in their areas.  The information is loaded from the DRC DOT application.",
+            ],
+            "identifier": "FEMA-0169",
             "keyword": [
                 "External Coordination"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-07-01T07:47:17-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Response and Recovery/Recovery Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Disaster Recovery Center (DRC) Locator"
         },
-            "identifier": "FEMA-0169",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Centralized repository for accessing natural hazard risk information, curated by FEMA's Natural Hazards Risk Assessment Program (NHRAP). Risk assessment resources from the Hazus program are always freely available and transparently developed. rnrnDataset provides authoritative Hazus loss modeling results (Flood - Riverine and Coastal, Earthquake, Hurricane Wind, Tsunami).rnrnDatapoints are hard risk reports, result spreadsheets, geospatial data, hazard data, and Hazus Package Region (HPR).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://egateway.fema.gov/ESF6/DRCLocator"
+                    "accessURL": "https://hazards.fema.gov/hll/about"
                 }
-            ]
-        },
-        {
-            "title": "Hazus Loss Library/Archived Hazus Results",
-            "description": "Centralized repository for accessing natural hazard risk information, curated by FEMA's Natural Hazards Risk Assessment Program (NHRAP). Risk assessment resources from the Hazus program are always freely available and transparently developed. rnrnDataset provides authoritative Hazus loss modeling results (Flood - Riverine and Coastal, Earthquake, Hurricane Wind, Tsunami).rnrnDatapoints are hard risk reports, result spreadsheets, geospatial data, hazard data, and Hazus Package Region (HPR).",
+            ],
+            "identifier": "FEMA-0186",
             "keyword": [
                 "Threats and Hazards"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-10-02T14:25:01-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Risk Management Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Hazus Loss Library/Archived Hazus Results"
         },
-            "identifier": "FEMA-0186",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Centralized repository for accessing natural hazard risk information, curated by FEMA's Natural Hazards Risk Assessment Program (NHRAP). Risk assessment resources from the Hazus program are always freely available and transparently developed. rnrnDataset provides Hazus risk scores.rnrnDatapoints include Hazard Frequency, Hazard Exposure, SHELDUS, SoVI, BRIC.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://hazards.fema.gov/hll/about"
+                    "accessURL": "https://www.fema.gov/hazus"
                 }
-            ]
-        },
-        {
-            "title": "Hazus Risk Scores and Components",
-            "description": "Centralized repository for accessing natural hazard risk information, curated by FEMA's Natural Hazards Risk Assessment Program (NHRAP). Risk assessment resources from the Hazus program are always freely available and transparently developed. rnrnDataset provides Hazus risk scores.rnrnDatapoints include Hazard Frequency, Hazard Exposure, SHELDUS, SoVI, BRIC.",
+            ],
+            "identifier": "FEMA-0187",
             "keyword": [
                 "Assessments"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-09-09T07:52:36-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Risk Management Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Hazus Risk Scores and Components"
         },
-            "identifier": "FEMA-0187",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "The Mitigation Planning Portal (MPP) is an online platform for tracking and reporting mitigation plans and related data elements across all ten Federal Emergency Management Agency (FEMA) Regions. rnrnDataset is used to identify mitigation plans across states and regions.rnrnDatapoints include links to mitigation plans for each state (a separate excel file of state links is held on local drive).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/hazus"
+                    "accessURL": "https://fema.maps.arcgis.com/apps/webappviewer/index.html?id=ec2fb023df744cf480da89539338c386"
                 }
-            ]
-        },
-        {
-            "title": "Local Hazard Mitigation Plan Status Dynamic Map (Geoplatform)",
-            "description": "The Mitigation Planning Portal (MPP) is an online platform for tracking and reporting mitigation plans and related data elements across all ten Federal Emergency Management Agency (FEMA) Regions. rnrnDataset is used to identify mitigation plans across states and regions.rnrnDatapoints include links to mitigation plans for each state (a separate excel file of state links is held on local drive).",
+            ],
+            "identifier": "FEMA-0201",
             "keyword": [
                 "Threats and Hazards"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-12-02T10:48:00-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Risk Management Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Local Hazard Mitigation Plan Status Dynamic Map (Geoplatform)"
         },
-            "identifier": "FEMA-0201",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "DHS, FIMA, FEMA\u2019s Response Geospatial Office, Oak Ridge National Laboratory, and the U.S. Geological Survey collaborated to build and maintain the nation\u2019s first comprehensive inventory of all structures larger than 450 square feet for use in Flood Insurance Mitigation, Emergency Preparedness and Response.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://fema.maps.arcgis.com/apps/webappviewer/index.html?id=ec2fb023df744cf480da89539338c386"
+                    "accessURL": "https://gis-fema.hub.arcgis.com/pages/usa-structures"
                 }
-            ]
-        },
-        {
-            "title": "USA Structures",
-            "description": "DHS, FIMA, FEMA\u2019s Response Geospatial Office, Oak Ridge National Laboratory, and the U.S. Geological Survey collaborated to build and maintain the nation\u2019s first comprehensive inventory of all structures larger than 450 square feet for use in Flood Insurance Mitigation, Emergency Preparedness and Response.",
+            ],
+            "identifier": "FEMA-0209",
             "keyword": [
                 "Assets"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-09-09T07:52:36-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Response and Recovery/Response Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "USA Structures"
         },
-            "identifier": "FEMA-0209",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "A binary dasymetric analysis, using National Land Cover Databases (NLCD) as an auxiliary, is applied to US Census Tracts. American Community Survey (ACS) Demographic data is often joined and used to generate impacted population with a hazard/AOI.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://gis-fema.hub.arcgis.com/pages/usa-structures"
+                    "accessURL": "https://fema.maps.arcgis.com/home/item.html?id=841ec1a638604e88859caab828ae55a3"
                 }
-            ]
-        },
-        {
-            "title": "Dasymetric US Census Tracts",
-            "description": "A binary dasymetric analysis, using National Land Cover Databases (NLCD) as an auxiliary, is applied to US Census Tracts. American Community Survey (ACS) Demographic data is often joined and used to generate impacted population with a hazard/AOI.",
+            ],
+            "identifier": "FEMA-0213",
             "keyword": [
                 "People"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-09-09T07:52:36-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Response and Recovery/Response Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Dasymetric US Census Tracts"
         },
-            "identifier": "FEMA-0213",
-            "accessLevel": "public",
+        {
+            "accessLevel": "restricted public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://fema.maps.arcgis.com/home/item.html?id=841ec1a638604e88859caab828ae55a3"
-                }
-            ]
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Enriched USNGs (5km, 10km, and 1km)",
             "description": "A set of United States National Grids (USNGs) that are enriched with American Community Survey (ACS) Demographic, LandScan, USA structures, and other datasets. This dataset is use for prioritizing areas across political boundaries (County and State).",
+            "identifier": "FEMA-0214",
             "keyword": [
                 "People"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-09-09T07:52:36-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Response and Recovery/Response Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Enriched USNGs (5km, 10km, and 1km)"
         },
-            "identifier": "FEMA-0214",
-            "accessLevel": "restricted public",
+        {
+            "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "National Flood Hazard Layer",
             "description": "Homeland Infrastructure Foundation-Level Data (HIFLD) geospatial data sets containing information on National Flood Hazard Layer (NFHL).",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://msc.fema.gov/nfhl"
+                }
+            ],
+            "identifier": "FEMA-0145",
             "keyword": [
                 "Threats and Hazards"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-08-01T07:58:54-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Risk Management Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "National Flood Hazard Layer"
         },
-            "identifier": "FEMA-0145",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "The NFHL FIRMs and FIS are the official regulatory products for the NFIP.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://msc.fema.gov/nfhl"
+                    "accessURL": "https://msc.fema.gov"
                 }
-            ]
-        },
-        {
-            "title": "National Flood Hazard Layer, Flood Insurance Rate Maps, Flood Insurance Study",
-            "description": "The NFHL FIRMs and FIS are the official regulatory products for the NFIP.",
+            ],
+            "identifier": "FEMA-0155",
             "keyword": [
                 "Threats and Hazards"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-08-01T07:58:54-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Risk Management Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "National Flood Hazard Layer, Flood Insurance Rate Maps, Flood Insurance Study"
         },
-            "identifier": "FEMA-0155",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Local, State, Regional, and National Average Annual Loss data from the adoption of hazard-resistant building codes",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://msc.fema.gov"
+                    "accessURL": "https://www.fema.gov/sites/default/files/documents/fema_building-codes-save-study-results.xlsx"
                 }
-            ]
-        },
-        {
-            "title": "AALs from the adoption of I-Codes",
-            "description": "Local, State, Regional, and National Average Annual Loss data from the adoption of hazard-resistant building codes",
+            ],
+            "identifier": "FEMA-0173",
             "keyword": [
                 "Assessments"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-07-01T07:47:17-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Risk Management Directorate"
             },
+            "rights": null,
+            "title": "AALs from the adoption of I-Codes"
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "024:056"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Open Data (MGMT)",
                 "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-            "identifier": "FEMA-0173",
-            "accessLevel": "public",
-            "bureauCode": [
-                "024:070"
-            ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "description": "The Global Terrorism Database\u2122 (GTD) is an open-source database including information on terrorist events around the world from 1970 through 2020 (with annual updates planned for the future). Unlike many other event databases, the GTD includes systematic data on domestic as well as international terrorist incidents that have occurred during this time period and now includes more than 200,000 cases.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/sites/default/files/documents/fema_building-codes-save-study-results.xlsx"
+                    "accessURL": "https://www.start.umd.edu/gtd/"
                 }
-            ]
-        },
-        {
-            "title": "Global Terrorism Database",
-            "description": "The Global Terrorism Database\u2122 (GTD) is an open-source database including information on terrorist events around the world from 1970 through 2020 (with annual updates planned for the future). Unlike many other event databases, the GTD includes systematic data on domestic as well as international terrorist incidents that have occurred during this time period and now includes more than 200,000 cases.",
+            ],
+            "identifier": "TSA-79246a29-1862-4212-a26e-efc0c0828d6c",
             "keyword": [
                 "global terrorism",
                 "open data"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2023-05-25T14:27:17-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "University of Maryland (UMD)"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Global Terrorism Database"
         },
-            "identifier": "TSA-79246a29-1862-4212-a26e-efc0c0828d6c",
-            "accessLevel": "public",
+        {
+            "accessLevel": "non-public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.start.umd.edu/gtd/"
-                }
-            ]
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Claims Management - Check Claim Status",
             "description": "Data in the public facing website used for claimants to view the status of their claim as applies to lost/damaged bag or property. Claim Number and other Personal Identifiable Information (PII) are used to submit and check claim status.",
+            "identifier": "TSA-f7feb9a3-66ef-4d55-9482-c718a6cde0ff",
             "keyword": [
                 "property",
                 "lost",
@@ -6137,30 +6146,30 @@
                 "bag",
                 "damaged"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-22T12:25:28-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "TSA-Chief Finance Officer"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Claims Management - Check Claim Status"
         },
-            "identifier": "TSA-f7feb9a3-66ef-4d55-9482-c718a6cde0ff",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Claims Management - Submit Claim",
             "description": "Data in the public-facing website used to submit a claim for a specific airport.  Applies only to TSA federalized airports, not those that employ private screening companies. Prospective claimants provide information related to claim, including financial information in regards to items involved in the claim.",
+            "identifier": "TSA-bbe79ec0-519f-465b-b37a-89308835056f",
             "keyword": [
                 "property",
                 "lost",
@@ -6170,92 +6179,98 @@
                 "damaged",
                 "submit claim"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-22T12:25:28-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "TSA-Chief Finance Officer"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Claims Management - Submit Claim"
         },
-            "identifier": "TSA-bbe79ec0-519f-465b-b37a-89308835056f",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Claims Management System Status Data Asset",
             "description": "This is the collection of data for the Claims Management Systems (CMS) Status data asset.  Claims Management System tracks the claims submitted to TSA by the traveling public.",
+            "identifier": "TSA-11da9128-5355-4837-8450-6246077d0ded",
             "keyword": [
                 "claim",
                 "claim status"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-22T12:25:28-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "TSA-Chief Finance Officer"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Claims Management System Status Data Asset"
         },
-            "identifier": "TSA-11da9128-5355-4837-8450-6246077d0ded",
-            "accessLevel": "non-public",
+        {
+            "accessLevel": "public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "TSA Privacy Impact Assessment (PIA) Documents",
             "description": "A collection of Privacy documents for the Transportation Security Administration (TSA) published to DHS.gov.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.dhs.gov/privacy-documents-transportation-security-administration-tsa"
+                }
+            ],
+            "identifier": "TSA-f513e54e-2e46-4192-973e-3546b1483990",
             "keyword": [
                 "PIA",
                 "privacy"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2023-05-25T14:27:18-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "TSA - Civil Rights & Liberties, Ombudsman, Traveler Engagement"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "TSA Privacy Impact Assessment (PIA) Documents"
         },
-            "identifier": "TSA-f513e54e-2e46-4192-973e-3546b1483990",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "The collection of System of Records Notices for TSA systems.  A system of record is a group of any records under the control of TSA from which information is retrieved by the name of the individual or by some identifying number, symbol, or other identifier assigned to the individual.  The Privacy Act requires each agency to publish notice of its systems of records in the Federal Register.  This notice is generally referred to as System of Records Notice or SORN.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.dhs.gov/privacy-documents-transportation-security-administration-tsa"
+                    "accessURL": "https://www.dhs.gov/system-records-notices-sorns"
                 }
-            ]
-        },
-        {
-            "title": "TSA System of Record Notices (SORNs)",
-            "description": "The collection of System of Records Notices for TSA systems.  A system of record is a group of any records under the control of TSA from which information is retrieved by the name of the individual or by some identifying number, symbol, or other identifier assigned to the individual.  The Privacy Act requires each agency to publish notice of its systems of records in the Federal Register.  This notice is generally referred to as System of Records Notice or SORN.",
+            ],
+            "identifier": "TSA-9b1d4b59-4607-4f5d-82b5-7e1a1f738f5c",
             "keyword": [
                 "privacy",
                 "SORN",
@@ -6264,2466 +6279,2466 @@
                 "notice",
                 "individual"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2023-05-25T14:27:19-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "TSA - Civil Rights & Liberties, Ombudsman, Traveler Engagement"
             },
+            "rights": null,
+            "title": "TSA System of Record Notices (SORNs)"
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "024:070"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Open Data (MGMT)",
                 "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-            "identifier": "TSA-9b1d4b59-4607-4f5d-82b5-7e1a1f738f5c",
-            "accessLevel": "public",
-            "bureauCode": [
-                "024:056"
-            ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "description": "The dataset was generated by FEMA\u2019s Individual Assistance (IA) reporting team and contains raw, unedited data from FEMA's National Emergency Management Information System (NEMIS).rnThis dataset contains aggregated, non-PII data for registration renters from FEMA\u2019s Housing Assistance program within the state, county, zip where the registration is valid for the declarations, starting with disaster declaration DR4116 (declared in 2013). Core data elements include number of applicants, county, zip code, and severity of damage, with individual data elements and descriptions listed in the metadata information within the dataset. rnData is self-reported and subject to human error. For example, when an applicant registers online, they enter their street and city address. The system runs a check and suggests a county. The applicant can override that choice. Similarly, with a call center registration, the Human Services Specialist (HSS) representatives are instructed to ask what county they live in. An applicant has the right to choose the county.rnThe financial information is derived from NEMIS and not FEMA's official financial systems. Due to differences in reporting periods, status of obligations and application of business rules, this financial information may differ slightly from official publication on public websites such as usaspending.gov. This dataset is not intended to be used for any official federal reporting.rnTo learn more about disaster assistance please visit https://www.fema.gov/individual-disaster-assistance.rnCitation: The Agency\u2019s preferred citation for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page, Citing Data section: https://www.fema.gov/about/openfema/terms-conditions.rnIf you have media inquiries about this dataset, please email the FEMA News Desk FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open government program please contact the OpenFEMA team via email OpenFEMA@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.dhs.gov/system-records-notices-sorns"
+                    "accessURL": "https://www.fema.gov/api/open/v2/HousingAssistanceRenters"
                 }
-            ]
-        },
-        {
-            "title": "Housing Assistance Program Data - Renters",
-            "description": "The dataset was generated by FEMA\u2019s Individual Assistance (IA) reporting team and contains raw, unedited data from FEMA's National Emergency Management Information System (NEMIS).rnThis dataset contains aggregated, non-PII data for registration renters from FEMA\u2019s Housing Assistance program within the state, county, zip where the registration is valid for the declarations, starting with disaster declaration DR4116 (declared in 2013). Core data elements include number of applicants, county, zip code, and severity of damage, with individual data elements and descriptions listed in the metadata information within the dataset. rnData is self-reported and subject to human error. For example, when an applicant registers online, they enter their street and city address. The system runs a check and suggests a county. The applicant can override that choice. Similarly, with a call center registration, the Human Services Specialist (HSS) representatives are instructed to ask what county they live in. An applicant has the right to choose the county.rnThe financial information is derived from NEMIS and not FEMA's official financial systems. Due to differences in reporting periods, status of obligations and application of business rules, this financial information may differ slightly from official publication on public websites such as usaspending.gov. This dataset is not intended to be used for any official federal reporting.rnTo learn more about disaster assistance please visit https://www.fema.gov/individual-disaster-assistance.rnCitation: The Agency\u2019s preferred citation for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page, Citing Data section: https://www.fema.gov/about/openfema/terms-conditions.rnIf you have media inquiries about this dataset, please email the FEMA News Desk FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open government program please contact the OpenFEMA team via email OpenFEMA@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0369",
             "keyword": [
                 "Incidents"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-12-02T10:48:00-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Response and Recovery/Recovery Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Housing Assistance Program Data - Renters"
         },
-            "identifier": "FEMA-0369",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "This dataset was generated by FEMA's Individual Assistance (IA) reporting team to share data on FEMA's Housing Assistance program for house owners within the state, county, zip where the registration is valid for the declarations, starting with disaster declaration DR4116 (declared in 2013). rnThis dataset contains aggregated, non-PII data. Core data elements include number of applicants, county, zip code, inspections, severity of damage, and assistance provided. Individual data elements and descriptions are listed in the metadata information within the dataset.rnData is self-reported and subject to human error. For example, when an applicant registers online, they enter their street and city address. The system runs a check and suggests a county. The applicant can override that choice. Similarly, with a call center registration, the Human Services Specialist (HSS) representatives are instructed to ask what county they live in. An applicant has the right to choose the county. To learn more about disaster assistance please visit https://www.fema.gov/individual-disaster-assistance.rnThe financial information is derived from NEMIS and not FEMA's official financial systems. Due to differences in reporting periods, status of obligations and application of business rules, this financial information may differ slightly from official publication on public websites such as usaspending.gov. This dataset is not intended to be used for any official federal reporting.rnCitation: The Agency\u2019s preferred citation for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page, Citing Data section: https://www.fema.gov/about/openfema/terms-conditions.rnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v2/HousingAssistanceRenters"
+                    "accessURL": "https://www.fema.gov/api/open/v2/HousingAssistanceOwners"
                 }
-            ]
-        },
-        {
-            "title": "Housing Assistance Program Data - Owners",
-            "description": "This dataset was generated by FEMA's Individual Assistance (IA) reporting team to share data on FEMA's Housing Assistance program for house owners within the state, county, zip where the registration is valid for the declarations, starting with disaster declaration DR4116 (declared in 2013). rnThis dataset contains aggregated, non-PII data. Core data elements include number of applicants, county, zip code, inspections, severity of damage, and assistance provided. Individual data elements and descriptions are listed in the metadata information within the dataset.rnData is self-reported and subject to human error. For example, when an applicant registers online, they enter their street and city address. The system runs a check and suggests a county. The applicant can override that choice. Similarly, with a call center registration, the Human Services Specialist (HSS) representatives are instructed to ask what county they live in. An applicant has the right to choose the county. To learn more about disaster assistance please visit https://www.fema.gov/individual-disaster-assistance.rnThe financial information is derived from NEMIS and not FEMA's official financial systems. Due to differences in reporting periods, status of obligations and application of business rules, this financial information may differ slightly from official publication on public websites such as usaspending.gov. This dataset is not intended to be used for any official federal reporting.rnCitation: The Agency\u2019s preferred citation for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page, Citing Data section: https://www.fema.gov/about/openfema/terms-conditions.rnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0370",
             "keyword": [
                 "Incidents"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-12-02T10:48:00-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Response and Recovery/Recovery Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Housing Assistance Program Data - Owners"
         },
-            "identifier": "FEMA-0370",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Provides the list of FEMA Regions.  The dataset includes the address for each regions headquarters as well a point in GeoJSON format for the headquarter and a geometry shape for the region in GeoJSON format.rnrnIf you have media inquiries about this dataset please email the FEMA News Desk FEMA-News-Desk@dhs.gov or call (202) 646-3272.  For inquiries about FEMA's data and Open government program please contact the OpenFEMA team via email OpenFEMA@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v2/HousingAssistanceOwners"
+                    "accessURL": "https://www.fema.gov/api/open/v2/FemaRegions"
                 }
-            ]
-        },
-        {
-            "title": "FEMA Regions",
-            "description": "Provides the list of FEMA Regions.  The dataset includes the address for each regions headquarters as well a point in GeoJSON format for the headquarter and a geometry shape for the region in GeoJSON format.rnrnIf you have media inquiries about this dataset please email the FEMA News Desk FEMA-News-Desk@dhs.gov or call (202) 646-3272.  For inquiries about FEMA's data and Open government program please contact the OpenFEMA team via email OpenFEMA@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0371",
             "keyword": [
                 "External Coordination"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-12-02T10:48:00-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Mission Support/Office of Chief Information Officer"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "FEMA Regions"
         },
-            "identifier": "FEMA-0371",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "This dataset contains funded projects (financial obligation to grantee) under the Hazard Mitigation Assistance (HMA) grant programs. FEMA administers three programs that provide funding for eligible mitigation planning and projects to reduce disaster losses and protect life and property from future disaster damages. The three programs are the Hazard Mitigation Grant Program (HMGP), Flood Mitigation Assistance (FMA) grant program, and Pre-Disaster Mitigation (PDM) grant program. This dataset also contains data from the HMA grant programs that were eliminated by the Biggert-Waters Flood Insurance Reform Act of 2012 (BW-12): Repetitive Flood Claims (RFC) grant program and Severe Repetitive Loss (SRL) grant program. For more information on the Hazard Mitigation Assistance grant programs, please visit: https://www.fema.gov/grants/mitigation.rnrnThis is raw, unedited data from FEMA's mitigation grant systems (NEMIS-MT and e-Grants) and as such is subject to a small percentage of human error. The financial information is derived from FEMA's mitigation grant systems and not FEMA's official financial systems. Due to differences in reporting periods, status of obligations and how business rules are applied, this financial information may differ slightly from official publication on public websites such as usaspending.gov; this dataset is not intended to be used for any official federal financial reporting.rnrnMissing values - In some cases data was not provided by the subgrantee (subrecipient), grantee (recipient) and/or entered into the FEMA mitigation grant systems. The information is likely available as part of the paper file which is considered the file of record.rnrnrnA newer version of this OpenFEMA data set has been released. This older dataset version will no longer be updated and will be archived by the end of April 2020. The following page details the latest version of this data set: https://www.fema.gov/openfema-data-page/hazard-mitigation-assistance-projects-v2. CSV and JSON Files can be downloaded from the 'Full Data' section.rnrnTo access the dataset through an API endpoint, visit the 'API Endpoint' section of the above page. Accessing data in this fashion permits data filtering, sorting, and field selection. The OpenFEMA API Documentation page provides information on API usage. rnrnIf you have media inquiries about this dataset please email the FEMA News Desk FEMA-News-Desk@dhs.gov or call (202) 646-3272.  For inquiries about FEMA's data and Open government program please contact the OpenFEMA team via email OpenFEMA@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v2/FemaRegions"
+                    "accessURL": "https://www.fema.gov/api/open/v4/HazardMitigationAssistanceProjects"
                 }
-            ]
-        },
-        {
-            "title": "Hazard Mitigation Assistance Projects",
-            "description": "This dataset contains funded projects (financial obligation to grantee) under the Hazard Mitigation Assistance (HMA) grant programs. FEMA administers three programs that provide funding for eligible mitigation planning and projects to reduce disaster losses and protect life and property from future disaster damages. The three programs are the Hazard Mitigation Grant Program (HMGP), Flood Mitigation Assistance (FMA) grant program, and Pre-Disaster Mitigation (PDM) grant program. This dataset also contains data from the HMA grant programs that were eliminated by the Biggert-Waters Flood Insurance Reform Act of 2012 (BW-12): Repetitive Flood Claims (RFC) grant program and Severe Repetitive Loss (SRL) grant program. For more information on the Hazard Mitigation Assistance grant programs, please visit: https://www.fema.gov/grants/mitigation.rnrnThis is raw, unedited data from FEMA's mitigation grant systems (NEMIS-MT and e-Grants) and as such is subject to a small percentage of human error. The financial information is derived from FEMA's mitigation grant systems and not FEMA's official financial systems. Due to differences in reporting periods, status of obligations and how business rules are applied, this financial information may differ slightly from official publication on public websites such as usaspending.gov; this dataset is not intended to be used for any official federal financial reporting.rnrnMissing values - In some cases data was not provided by the subgrantee (subrecipient), grantee (recipient) and/or entered into the FEMA mitigation grant systems. The information is likely available as part of the paper file which is considered the file of record.rnrnrnA newer version of this OpenFEMA data set has been released. This older dataset version will no longer be updated and will be archived by the end of April 2020. The following page details the latest version of this data set: https://www.fema.gov/openfema-data-page/hazard-mitigation-assistance-projects-v2. CSV and JSON Files can be downloaded from the 'Full Data' section.rnrnTo access the dataset through an API endpoint, visit the 'API Endpoint' section of the above page. Accessing data in this fashion permits data filtering, sorting, and field selection. The OpenFEMA API Documentation page provides information on API usage. rnrnIf you have media inquiries about this dataset please email the FEMA News Desk FEMA-News-Desk@dhs.gov or call (202) 646-3272.  For inquiries about FEMA's data and Open government program please contact the OpenFEMA team via email OpenFEMA@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0372",
             "keyword": [
                 "Threats and Hazards"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-12-02T10:48:00-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Federal Insurance Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Hazard Mitigation Assistance Projects"
         },
-            "identifier": "FEMA-0372",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "This dataset lists all requests for major disaster declarations and emergency declarations that have been denied. For more information on the FEMA disaster declaration process, please visit: https://www.fema.gov/disasters/how-declared.rnrnThis is raw, unedited data from FEMA's National Emergency Management Information System (NEMIS) and as such is subject to a small percentage of human error. The dataset is primarily composed of historical data that was manually entered into NEMIS after it launched in 1998. This dataset only includes major and emergency disasters; there are no Fire Management Assistance Grants declarations. Additionally, NEMIS utilizes census data from the United States Census Bureau in which Tribal Nations are listed as localities within a State. As such, disaster declarations for Tribal Nations are currently included in State data.rnrnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v4/HazardMitigationAssistanceProjects"
+                    "accessURL": "https://www.fema.gov/api/open/v1/DeclarationDenials"
                 }
-            ]
-        },
-        {
-            "title": "Declaration Denials",
-            "description": "This dataset lists all requests for major disaster declarations and emergency declarations that have been denied. For more information on the FEMA disaster declaration process, please visit: https://www.fema.gov/disasters/how-declared.rnrnThis is raw, unedited data from FEMA's National Emergency Management Information System (NEMIS) and as such is subject to a small percentage of human error. The dataset is primarily composed of historical data that was manually entered into NEMIS after it launched in 1998. This dataset only includes major and emergency disasters; there are no Fire Management Assistance Grants declarations. Additionally, NEMIS utilizes census data from the United States Census Bureau in which Tribal Nations are listed as localities within a State. As such, disaster declarations for Tribal Nations are currently included in State data.rnrnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0376",
             "keyword": [
                 "Incidents"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-08-01T07:58:54-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Response and Recovery/Associate Administrator"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Declaration Denials"
         },
-            "identifier": "FEMA-0376",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "This data set contains general information on declared disasters, including the disaster number, declaration type, state, description, incident start and end dates, and incident type.rnrnIf you have media inquiries about this dataset please email the FEMA News Desk FEMA-News-Desk@dhs.gov or call (202) 646-3272.  For inquiries about FEMA's data and Open government program please contact the OpenFEMA team via email OpenFEMA@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v1/DeclarationDenials"
+                    "accessURL": "https://www.fema.gov/api/open/v1/FemaWebDeclarationAreas"
                 }
-            ]
-        },
-        {
-            "title": "FEMA Web Declaration Areas",
-            "description": "This data set contains general information on declared disasters, including the disaster number, declaration type, state, description, incident start and end dates, and incident type.rnrnIf you have media inquiries about this dataset please email the FEMA News Desk FEMA-News-Desk@dhs.gov or call (202) 646-3272.  For inquiries about FEMA's data and Open government program please contact the OpenFEMA team via email OpenFEMA@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0377",
             "keyword": [
                 "Incidents"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-08-01T07:58:54-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Office of External Affairs/Disaster Operations Division"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "FEMA Web Declaration Areas"
         },
-            "identifier": "FEMA-0377",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "This data set contains financial assistance values, including the number of approved applications, as well as individual, public assistance, and hazard mitigation grant amounts.rnrnThis is raw, unedited data from FEMA's National Emergency Management Information System (NEMIS) and as such is subject to a small percentage of human error. The financial information is derived from NEMIS and not FEMA's official financial systems. Due to differences in reporting periods, status of obligations and how business rules are applied, this financial information may differ slightly from official publication on public websites such as usaspending.gov; this dataset is not intended to be used for any official federal financial reporting.rnrnIf you have media inquiries about this dataset please email the FEMA News Desk FEMA-News-Desk@dhs.gov or call (202) 646-3272.  For inquiries about FEMA's data and Open government program please contact the OpenFEMA team via email OpenFEMA@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v1/FemaWebDeclarationAreas"
+                    "accessURL": "https://www.fema.gov/api/open/v1/FemaWebDisasterSummaries"
                 }
-            ]
-        },
-        {
-            "title": "FEMA Web Disaster Summaries",
-            "description": "This data set contains financial assistance values, including the number of approved applications, as well as individual, public assistance, and hazard mitigation grant amounts.rnrnThis is raw, unedited data from FEMA's National Emergency Management Information System (NEMIS) and as such is subject to a small percentage of human error. The financial information is derived from NEMIS and not FEMA's official financial systems. Due to differences in reporting periods, status of obligations and how business rules are applied, this financial information may differ slightly from official publication on public websites such as usaspending.gov; this dataset is not intended to be used for any official federal financial reporting.rnrnIf you have media inquiries about this dataset please email the FEMA News Desk FEMA-News-Desk@dhs.gov or call (202) 646-3272.  For inquiries about FEMA's data and Open government program please contact the OpenFEMA team via email OpenFEMA@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0378",
             "keyword": [
                 "Incidents"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-08-01T07:58:54-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Office of External Affairs/Public Affairs Division"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "FEMA Web Disaster Summaries"
         },
-            "identifier": "FEMA-0378",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "The Integrated Public Alert and Warning System (IPAWS) is a modernization of the nation's alert and warning infrastructure that unifies the United States' Emergency Alert System (EAS), Wireless Emergency Alerts (WEA), the National Oceanic and Atmospheric Administration (NOAA) Weather Radio, and other public alerting systems implemented as a set of Web services. Organized and managed by FEMA, the system supports alert origination by Federal, state, local, territorial and tribal officials, and subsequent dissemination to the public using a range of national and local alerting systems. This dataset contains recent*, historic, and archived IPAWS Common Alerting Protocol (CAP) v1.2 messages from June 2012 to the present including date, time, event code (examples listed below), city, county, joint agency, police, law enforcement, Collaborative Operating Group (COG), State(s), locality, territory or tribe. It can be used to capture and analyze historic and archived messages. *The dataset is published with a twenty-four (24) hour delay to reduce the risk of being confused with an active alert received from the live IPAWS feed. The most recent record will reflect the alert(s) sent twenty-four (24) hours ago (if such records exist). For example, if an alert originator sent an alert at 1459GMT on June 1st and sent a different alert at 1600GMT on June 2nd, these alerts will not be visible in the dataset until 1459GMT on June 2nd and 1600GMT June 3rd respectively. Information on signing up for receiving active alerts can be found at https://www.fema.gov/emergency-managers/practitioners/integrated-public-alert-warning-system . To request access to alerts issued through IPAWS or for a list of companies with access to the IPAWS All-Hazards Information Feed, email ipaws@fema.dhs.gov. The data elements within the CAP messages are well documented and can be found in the following technical document: https://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2-os.pdf See also: IPAWS Architecture - https://www.fema.gov/pdf/emergency/ipaws/architecture_diagram.pdf IPAWS Overview - https://www.fema.gov/emergency-managers/practitioners/integrated-public-alert-warning-system This is raw, unedited data with no personally identifiable information from the IPAWS Alert Aggregator from June 2012 to the present created by over 1450 Alert Originators across the country. FEMA does not validate the content of each message. As such, it may contain a small percentage of human error. OpenFEMA does not have a full backup capability so if the site goes down, the information will be inaccessible. This is a rare occurrence. Earlier messages may contain non-compliant geocoordinates. Recent versions of the software check these coordinates for compliance. This dataset is not intended to be an official federal report and should not be considered an official federal report. If you are using this site for other than research purposes, please understand that these CAP messages are captured only after the official IPAWS message has been sent. Note that the original IPAWS CAP message is provided in the originalMessage element of the returned JSON object. The XML based message is encoded such that a separate tool, such as a JSON parser, computer language, or browser must be used to view the original format. See the originalMessage field description for additional details. Due to its size and its hierarchical data structure, working with the IPAWS Archived Alerts file can be challenging. See the OpenFEMA Guide to Working with Large Data Sets page for useful hints and tips: https://www.fema.gov/about/openfema/working-with-large-data-sets . The Developer Resources page has sample IPAWS API queries in the section called IPAWS Archived Alerts Query Examples: https://www.fema.gov/about/openfema/developer-resources",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v1/FemaWebDisasterSummaries"
+                    "accessURL": "https://www.fema.gov/openfema-data-page/ipaws-archived-alerts-v1"
                 }
-            ]
-        },
-        {
-            "title": "IPAWS Archived Alerts",
-            "description": "The Integrated Public Alert and Warning System (IPAWS) is a modernization of the nation's alert and warning infrastructure that unifies the United States' Emergency Alert System (EAS), Wireless Emergency Alerts (WEA), the National Oceanic and Atmospheric Administration (NOAA) Weather Radio, and other public alerting systems implemented as a set of Web services. Organized and managed by FEMA, the system supports alert origination by Federal, state, local, territorial and tribal officials, and subsequent dissemination to the public using a range of national and local alerting systems. This dataset contains recent*, historic, and archived IPAWS Common Alerting Protocol (CAP) v1.2 messages from June 2012 to the present including date, time, event code (examples listed below), city, county, joint agency, police, law enforcement, Collaborative Operating Group (COG), State(s), locality, territory or tribe. It can be used to capture and analyze historic and archived messages. *The dataset is published with a twenty-four (24) hour delay to reduce the risk of being confused with an active alert received from the live IPAWS feed. The most recent record will reflect the alert(s) sent twenty-four (24) hours ago (if such records exist). For example, if an alert originator sent an alert at 1459GMT on June 1st and sent a different alert at 1600GMT on June 2nd, these alerts will not be visible in the dataset until 1459GMT on June 2nd and 1600GMT June 3rd respectively. Information on signing up for receiving active alerts can be found at https://www.fema.gov/emergency-managers/practitioners/integrated-public-alert-warning-system . To request access to alerts issued through IPAWS or for a list of companies with access to the IPAWS All-Hazards Information Feed, email ipaws@fema.dhs.gov. The data elements within the CAP messages are well documented and can be found in the following technical document: https://docs.oasis-open.org/emergency/cap/v1.2/CAP-v1.2-os.pdf See also: IPAWS Architecture - https://www.fema.gov/pdf/emergency/ipaws/architecture_diagram.pdf IPAWS Overview - https://www.fema.gov/emergency-managers/practitioners/integrated-public-alert-warning-system This is raw, unedited data with no personally identifiable information from the IPAWS Alert Aggregator from June 2012 to the present created by over 1450 Alert Originators across the country. FEMA does not validate the content of each message. As such, it may contain a small percentage of human error. OpenFEMA does not have a full backup capability so if the site goes down, the information will be inaccessible. This is a rare occurrence. Earlier messages may contain non-compliant geocoordinates. Recent versions of the software check these coordinates for compliance. This dataset is not intended to be an official federal report and should not be considered an official federal report. If you are using this site for other than research purposes, please understand that these CAP messages are captured only after the official IPAWS message has been sent. Note that the original IPAWS CAP message is provided in the originalMessage element of the returned JSON object. The XML based message is encoded such that a separate tool, such as a JSON parser, computer language, or browser must be used to view the original format. See the originalMessage field description for additional details. Due to its size and its hierarchical data structure, working with the IPAWS Archived Alerts file can be challenging. See the OpenFEMA Guide to Working with Large Data Sets page for useful hints and tips: https://www.fema.gov/about/openfema/working-with-large-data-sets . The Developer Resources page has sample IPAWS API queries in the section called IPAWS Archived Alerts Query Examples: https://www.fema.gov/about/openfema/developer-resources",
+            ],
+            "identifier": "FEMA-0379",
             "keyword": [
                 "Threats and Hazards"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-08-01T07:58:54-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Mission Support/Office of Chief Information Officer"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "IPAWS Archived Alerts"
         },
-            "identifier": "FEMA-0379",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "FEMA Disaster Declarations Summary is a summarized dataset describing all federally declared disasters. This dataset lists all official FEMA Disaster Declarations, beginning with the first disaster declaration in 1953 and features all three disaster declaration types: major disaster, emergency, and fire management assistance. The dataset includes declared recovery programs and geographic areas (county not available before 1964; Fire Management records are considered partial due to historical nature of the dataset).rnrnPlease note the unique structure of the disaster sequencing (due to a numbering system that originated in the 1950's-1970's):rn0001-1999     Major Disaster Declarationrn2000-2999     Fire Managementrn3000-3999     Emergency Declaration (Special Emergency)rn4000-              Major Disaster DeclarationrnrnFor more information on the disaster declaration process, see https://www.fema.gov/disasters and https://www.fema.gov/disasters/how-declared rnrnThis is raw, unedited data from FEMA's National Emergency Management Information System (NEMIS) and as such is subject to a small percentage of human error. The dataset is primarily composed of historical data that was manually entered into NEMIS after it launched in 1998. The financial information is derived from NEMIS and not FEMA's official financial systems.rnrnDue to differences in reporting periods, status of obligations, and how business rules are applied, this financial information may differ slightly from official publication on public websites such as www.usaspending.gov. This dataset is not intended to be used for any official federal financial reporting.rnrnA newer version of this OpenFEMA data set has been released. This older dataset version will no longer be updated and will be archived by the end of April 2020. The following page details the latest version of this data set: https://www.fema.gov/openfema-dataset-disaster-declarations-summaries-v2. CSV and JSON Files can be downloaded from the 'Full Data' section.rnrnTo access the dataset through an API endpoint, visit the 'API Endpoint' section of the above page. Accessing data in this fashion permits data filtering, sorting, and field selection. The OpenFEMA API Documentation page provides information on API usage. rnrnIf you have media inquiries about this dataset please email the FEMA News Desk FEMA-News-Desk@dhs.gov or call (202) 646-3272.  For inquiries about FEMA's data and Open government program please contact the OpenFEMA team via email OpenFEMA@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/openfema-data-page/ipaws-archived-alerts-v1"
+                    "accessURL": "https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries"
                 }
-            ]
-        },
-        {
-            "title": "Disaster Declarations Summaries",
-            "description": "FEMA Disaster Declarations Summary is a summarized dataset describing all federally declared disasters. This dataset lists all official FEMA Disaster Declarations, beginning with the first disaster declaration in 1953 and features all three disaster declaration types: major disaster, emergency, and fire management assistance. The dataset includes declared recovery programs and geographic areas (county not available before 1964; Fire Management records are considered partial due to historical nature of the dataset).rnrnPlease note the unique structure of the disaster sequencing (due to a numbering system that originated in the 1950's-1970's):rn0001-1999     Major Disaster Declarationrn2000-2999     Fire Managementrn3000-3999     Emergency Declaration (Special Emergency)rn4000-              Major Disaster DeclarationrnrnFor more information on the disaster declaration process, see https://www.fema.gov/disasters and https://www.fema.gov/disasters/how-declared rnrnThis is raw, unedited data from FEMA's National Emergency Management Information System (NEMIS) and as such is subject to a small percentage of human error. The dataset is primarily composed of historical data that was manually entered into NEMIS after it launched in 1998. The financial information is derived from NEMIS and not FEMA's official financial systems.rnrnDue to differences in reporting periods, status of obligations, and how business rules are applied, this financial information may differ slightly from official publication on public websites such as www.usaspending.gov. This dataset is not intended to be used for any official federal financial reporting.rnrnA newer version of this OpenFEMA data set has been released. This older dataset version will no longer be updated and will be archived by the end of April 2020. The following page details the latest version of this data set: https://www.fema.gov/openfema-dataset-disaster-declarations-summaries-v2. CSV and JSON Files can be downloaded from the 'Full Data' section.rnrnTo access the dataset through an API endpoint, visit the 'API Endpoint' section of the above page. Accessing data in this fashion permits data filtering, sorting, and field selection. The OpenFEMA API Documentation page provides information on API usage. rnrnIf you have media inquiries about this dataset please email the FEMA News Desk FEMA-News-Desk@dhs.gov or call (202) 646-3272.  For inquiries about FEMA's data and Open government program please contact the OpenFEMA team via email OpenFEMA@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0380",
             "keyword": [
                 "Incidents"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-12-02T10:48:00-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Response and Recovery/Response Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Disaster Declarations Summaries"
         },
-            "identifier": "FEMA-0380",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "This dataset contains a list of FEMA declaration types and the types of assistance authorized. For more information on the disaster declaration process, please visit https://www.fema.gov/disasters/how-declared.rnrnThis is raw, unedited data from FEMA's National Emergency Management Information System (NEMIS) and as such is subject to a small percentage of human error. The dataset is primarily composed of historical data that was manually entered into NEMIS after it launched in 1998. rnrnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries"
+                    "accessURL": "https://www.fema.gov/api/open/v1/FemaWebDisasterDeclarations"
                 }
-            ]
-        },
-        {
-            "title": "FEMA Web Disaster Declarations",
-            "description": "This dataset contains a list of FEMA declaration types and the types of assistance authorized. For more information on the disaster declaration process, please visit https://www.fema.gov/disasters/how-declared.rnrnThis is raw, unedited data from FEMA's National Emergency Management Information System (NEMIS) and as such is subject to a small percentage of human error. The dataset is primarily composed of historical data that was manually entered into NEMIS after it launched in 1998. rnrnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0381",
             "keyword": [
                 "Incidents"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-08-01T07:58:54-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Office of External Affairs/Public Affairs Division"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "FEMA Web Disaster Declarations"
         },
-            "identifier": "FEMA-0381",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "This dataset contains funded projects under FEMA's Hazard Mitigation Assistance (HMA) grant programs by communities participating in the National Flood Insurance Program (NFIP) Community Rating System (CRS). The Hazard Mitigation Assistance Projects by NFIP CRS Communities dataset can be joined to the OpenFEMA Hazard Mitigation Assistance Funded Project dataset by the Project Identifier field. Note, not all projects in the Hazard Mitigation Assistance Funded Project dataset will associate to an NFIP CRS Community. For more information on the NFIP CRS Program, visit https://www.fema.gov/flood-insurance/rules-legislation/community-rating-system.rnrnFEMA administers three programs that provide funding for eligible mitigation planning and projects that reduces disaster losses and protect life and property from future disaster damages. The three programs are the Hazard Mitigation Grant Program (HMGP), Flood Mitigation Assistance (FMA) grant program, and Building Resilient Infrastructure and Communities (BRIC) grant program. This dataset also contains data from the HMA grant programs that were eliminated by the Disaster Recovery Reform Act of 2018 (Pre-Disaster Mitigation (PDM) grant program) and Biggert Water Flood Insurance Reform Act of 2012 (Repetitive Flood Claims (RFC) grant program and Severe Repetitive Loss (SRL) grant program). For more information on the Hazard Mitigation Assistance grant programs, please visit: https://www.fema.gov/grants/mitigation.                                                                    rnrnThis is raw, unedited data from FEMA's National Emergency Management Information System (NEMIS) and Mitigation eGrants Systems and is dependent on Regional entry, as such it is subject to a small percentage of human error and delayed entry of plan information. The data is updated from authoritative sources and has a minimum 24 hour delay. This dataset is not derived from FEMA's official financial system and is not intended to be used for any official federal financial reporting. Due to differences in reporting periods, status of obligations and how business rules are applied, the financial information in this dataset may differ slightly from official publication on public websites such as usaspending.gov. rnrnPlease note that jurisdictions may participate in multiple plans. rnrnCitation: The Agency's preferred citation for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page, Citing Data section: https://www.fema.gov/about/openfema/terms-conditions.rnrnPlace name may differ from official naming standard referenced in update organization documents (i.e. Tribal name under BIA list or other authoritative source Village of, City of, etc).rnrnIf you have media inquiries about this dataset please email the FEMA News Desk FEMA-News-Desk@dhs.gov or call (202) 646-3272.  For inquiries about FEMA's data and Open government program please contact the OpenFEMA team via email OpenFEMA@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v1/FemaWebDisasterDeclarations"
+                    "accessURL": "https://www.fema.gov/api/open/v2/HazardMitigationAssistanceProjectsByNfipCrsCommunities"
                 }
-            ]
-        },
-        {
-            "title": "Hazard Mitigation Assistance Projects by NFIP CRS Communities",
-            "description": "This dataset contains funded projects under FEMA's Hazard Mitigation Assistance (HMA) grant programs by communities participating in the National Flood Insurance Program (NFIP) Community Rating System (CRS). The Hazard Mitigation Assistance Projects by NFIP CRS Communities dataset can be joined to the OpenFEMA Hazard Mitigation Assistance Funded Project dataset by the Project Identifier field. Note, not all projects in the Hazard Mitigation Assistance Funded Project dataset will associate to an NFIP CRS Community. For more information on the NFIP CRS Program, visit https://www.fema.gov/flood-insurance/rules-legislation/community-rating-system.rnrnFEMA administers three programs that provide funding for eligible mitigation planning and projects that reduces disaster losses and protect life and property from future disaster damages. The three programs are the Hazard Mitigation Grant Program (HMGP), Flood Mitigation Assistance (FMA) grant program, and Building Resilient Infrastructure and Communities (BRIC) grant program. This dataset also contains data from the HMA grant programs that were eliminated by the Disaster Recovery Reform Act of 2018 (Pre-Disaster Mitigation (PDM) grant program) and Biggert Water Flood Insurance Reform Act of 2012 (Repetitive Flood Claims (RFC) grant program and Severe Repetitive Loss (SRL) grant program). For more information on the Hazard Mitigation Assistance grant programs, please visit: https://www.fema.gov/grants/mitigation.                                                                    rnrnThis is raw, unedited data from FEMA's National Emergency Management Information System (NEMIS) and Mitigation eGrants Systems and is dependent on Regional entry, as such it is subject to a small percentage of human error and delayed entry of plan information. The data is updated from authoritative sources and has a minimum 24 hour delay. This dataset is not derived from FEMA's official financial system and is not intended to be used for any official federal financial reporting. Due to differences in reporting periods, status of obligations and how business rules are applied, the financial information in this dataset may differ slightly from official publication on public websites such as usaspending.gov. rnrnPlease note that jurisdictions may participate in multiple plans. rnrnCitation: The Agency's preferred citation for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page, Citing Data section: https://www.fema.gov/about/openfema/terms-conditions.rnrnPlace name may differ from official naming standard referenced in update organization documents (i.e. Tribal name under BIA list or other authoritative source Village of, City of, etc).rnrnIf you have media inquiries about this dataset please email the FEMA News Desk FEMA-News-Desk@dhs.gov or call (202) 646-3272.  For inquiries about FEMA's data and Open government program please contact the OpenFEMA team via email OpenFEMA@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0382",
             "keyword": [
                 "Threats and Hazards"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-12-02T10:48:00-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Federal Insurance Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Hazard Mitigation Assistance Projects by NFIP CRS Communities"
         },
-            "identifier": "FEMA-0382",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "This dataset was generated by FEMA's Public Assistance (PA) reporting team to share data on assistance made available to eligible state, local and tribal governments, and certain private nonprofit organizations as part of presidentially declared disasters. This data, starting with disaster declaration DR1239 (declared in 1998), lists applicant (subrecipient) information that supplements the 'Public Assistance Funded Projects Detail' dataset. This is raw, unedited data from FEMA's Emergency Management Mission Integrated Environment (EMMIE) and is subject to a small percentage of human error.rnAny financial information is derived from EMMIE and not FEMA's official financial systems. Due to differences in reporting periods, status of obligations and application of business rules, this financial information may differ slightly from official publication on public websites such as usaspending.gov. This dataset is not intended to be used for any official federal reporting. rnrnCitation: The Agency's preferred citation for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page, Citing Data section: https://www.fema.gov/about/openfema/terms-conditions.rnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v2/HazardMitigationAssistanceProjectsByNfipCrsCommunities"
+                    "accessURL": "https://www.fema.gov/api/open/v1/PublicAssistanceApplicants"
                 }
-            ]
-        },
-        {
-            "title": "Public Assistance Applicants",
-            "description": "This dataset was generated by FEMA's Public Assistance (PA) reporting team to share data on assistance made available to eligible state, local and tribal governments, and certain private nonprofit organizations as part of presidentially declared disasters. This data, starting with disaster declaration DR1239 (declared in 1998), lists applicant (subrecipient) information that supplements the 'Public Assistance Funded Projects Detail' dataset. This is raw, unedited data from FEMA's Emergency Management Mission Integrated Environment (EMMIE) and is subject to a small percentage of human error.rnAny financial information is derived from EMMIE and not FEMA's official financial systems. Due to differences in reporting periods, status of obligations and application of business rules, this financial information may differ slightly from official publication on public websites such as usaspending.gov. This dataset is not intended to be used for any official federal reporting. rnrnCitation: The Agency's preferred citation for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page, Citing Data section: https://www.fema.gov/about/openfema/terms-conditions.rnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0383",
             "keyword": [
                 "Incidents"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-12-02T10:48:00-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Response and Recovery/Recovery Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Public Assistance Applicants"
         },
-            "identifier": "FEMA-0383",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "FEMA's new Public Assistance (PA) case management system called the FEMA Applicant Case Tracker (FAC-Trax) includes the Grants Manager database and Grant Portal tool (collectively \u2018Grants Manager\u2019). rn FAC-Trax was developed in 2016 and became the processing system for all new PA grants starting on August  25, 2017. Grants Manager became a new database to document PA projects from formulation to a seamless transition to grant obligation and close-out with grant formulation being a new process not previously captured.rnThe previous database, the Emergency Management Mission Integration Environment (EMMIE) currently functions as the system for obligations with a few declarations now obligated in Grants Manager as test cases. All remaining EMMIE functions are scheduled to move to Grants Manager soon as well as the records for EMMIE and the previous database, the National Emergency Management Information System (NEMIS). rnThe 'Public Assistance Applicants Program Deliveries' dataset was generated from Grants Manager by the PA reporting team to share data on assistance made available to eligible state, local and tribal governments, and certain private nonprofit organizations as part of presidentially declared disasters. This dataset reports on the PA National Delivery Model process with summaries of projects and project statuses for all active applicants (subrecipients). The data reflects time sensitive, current phase information including pre-obligation (project formulation) phases starting in phase 2 to obligation in phase 5.rnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v1/PublicAssistanceApplicants"
+                    "accessURL": "https://www.fema.gov/api/open/v1/PublicAssistanceApplicantsProgramDeliveries"
                 }
-            ]
-        },
-        {
-            "title": "Public Assistance Applicants Program Deliveries",
-            "description": "FEMA's new Public Assistance (PA) case management system called the FEMA Applicant Case Tracker (FAC-Trax) includes the Grants Manager database and Grant Portal tool (collectively \u2018Grants Manager\u2019). rn FAC-Trax was developed in 2016 and became the processing system for all new PA grants starting on August  25, 2017. Grants Manager became a new database to document PA projects from formulation to a seamless transition to grant obligation and close-out with grant formulation being a new process not previously captured.rnThe previous database, the Emergency Management Mission Integration Environment (EMMIE) currently functions as the system for obligations with a few declarations now obligated in Grants Manager as test cases. All remaining EMMIE functions are scheduled to move to Grants Manager soon as well as the records for EMMIE and the previous database, the National Emergency Management Information System (NEMIS). rnThe 'Public Assistance Applicants Program Deliveries' dataset was generated from Grants Manager by the PA reporting team to share data on assistance made available to eligible state, local and tribal governments, and certain private nonprofit organizations as part of presidentially declared disasters. This dataset reports on the PA National Delivery Model process with summaries of projects and project statuses for all active applicants (subrecipients). The data reflects time sensitive, current phase information including pre-obligation (project formulation) phases starting in phase 2 to obligation in phase 5.rnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0384",
             "keyword": [
                 "Incidents"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-12-02T10:48:00-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Response and Recovery/Recovery Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Public Assistance Applicants Program Deliveries"
         },
-            "identifier": "FEMA-0384",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "This dataset contains the properties that were mitigated by projects funded under the Hazard Mitigation Assistance (HMA) grant programs. FEMA administers three programs that provide funding for eligible mitigation planning and projects to reduce disaster losses and protect life and property from future disaster damages. The three programs are the Hazard Mitigation Grant Program (HMGP), Flood Mitigation Assistance (FMA) grant program, and Pre-Disaster Mitigation (PDM) grant program. This dataset also contains data from the HMA grant programs that were eliminated by the Biggert Water Flood Insurance Reform Act of 2012 (BW-12): Repetitive Flood Claims (RFC) grant program and Severe Repetitive Loss (SRL) grant program. For more information on the Hazard Mitigation Assistance grant programs, please visit: https://www.fema.gov/grants/mitigation.rnrnThe dataset contains properties by project identifier, city, zip code, state and region and does not contain any Personally Identifiable Information (PII). The mitigated property dataset can be joined to the OpenFEMA Hazard Mitigation Assistance Funded Project dataset by the Project Identifier field. Note, not all projects in the Hazard Mitigation Assistance Funded Project dataset will have mitigated properties (e.g., Planning and Management Cost projects). In some cases data was not provided by the subgrantee (sub-recipient), grantee (recipient) and/or entered into the FEMA mitigation grant systems. The information is likely available as part of the paper file which is considered the file of record.rnrnThis is raw, unedited data from FEMA's mitigation grant systems (NEMIS-MT and e-Grants) and as such is subject to a small percentage of human error. The financial information is derived from FEMA's mitigation grant systems and not FEMA's official financial systems. Due to differences in reporting periods, status of obligations and how business rules are applied, this financial information may differ slightly from official publication on public websites such as www.usaspending.gov; this dataset is not intended to be used for any official federal financial reporting.rnrnMissing values - In some cases data was not provided by the subgrantee (subrecipient), grantee (recipient) and/or entered into the FEMA mitigation grant systems. The information is likely available as part of the paper file which is considered the file of record.rnrnA newer version of this OpenFEMA data set has been released. This older dataset version will no longer be updated and will be archived by the end of April 2020. The following page details the latest version of this data set:https://www.fema.gov/openfema-data-page/hazard-mitigation-assistance-mitigated-properties-v2. CSV and JSON Files can be downloaded from the 'Full Data' section.rnrnTo access the dataset through an API endpoint, visit the 'API Endpoint' section of the above page. Accessing data in this fashion permits data filtering, sorting, and field selection. The OpenFEMA API Documentation page provides information on API usage. rnrnIf you have media inquiries about this dataset, please email the FEMA News Desk FEMA-News-Desk@dhs.gov or call (202) 646-3272.  For inquiries about FEMA's Hazard Mitigation Assistance grant program data and Open government program, please contact the OpenFEMA team via email OpenFEMA@fema.dhs.gov and FEMA-HMAAnalytics@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v1/PublicAssistanceApplicantsProgramDeliveries"
+                    "accessURL": "https://www.fema.gov/api/open/v4/HazardMitigationAssistanceMitigatedProperties"
                 }
-            ]
-        },
-        {
-            "title": "Hazard Mitigation Assistance Mitigated Properties",
-            "description": "This dataset contains the properties that were mitigated by projects funded under the Hazard Mitigation Assistance (HMA) grant programs. FEMA administers three programs that provide funding for eligible mitigation planning and projects to reduce disaster losses and protect life and property from future disaster damages. The three programs are the Hazard Mitigation Grant Program (HMGP), Flood Mitigation Assistance (FMA) grant program, and Pre-Disaster Mitigation (PDM) grant program. This dataset also contains data from the HMA grant programs that were eliminated by the Biggert Water Flood Insurance Reform Act of 2012 (BW-12): Repetitive Flood Claims (RFC) grant program and Severe Repetitive Loss (SRL) grant program. For more information on the Hazard Mitigation Assistance grant programs, please visit: https://www.fema.gov/grants/mitigation.rnrnThe dataset contains properties by project identifier, city, zip code, state and region and does not contain any Personally Identifiable Information (PII). The mitigated property dataset can be joined to the OpenFEMA Hazard Mitigation Assistance Funded Project dataset by the Project Identifier field. Note, not all projects in the Hazard Mitigation Assistance Funded Project dataset will have mitigated properties (e.g., Planning and Management Cost projects). In some cases data was not provided by the subgrantee (sub-recipient), grantee (recipient) and/or entered into the FEMA mitigation grant systems. The information is likely available as part of the paper file which is considered the file of record.rnrnThis is raw, unedited data from FEMA's mitigation grant systems (NEMIS-MT and e-Grants) and as such is subject to a small percentage of human error. The financial information is derived from FEMA's mitigation grant systems and not FEMA's official financial systems. Due to differences in reporting periods, status of obligations and how business rules are applied, this financial information may differ slightly from official publication on public websites such as www.usaspending.gov; this dataset is not intended to be used for any official federal financial reporting.rnrnMissing values - In some cases data was not provided by the subgrantee (subrecipient), grantee (recipient) and/or entered into the FEMA mitigation grant systems. The information is likely available as part of the paper file which is considered the file of record.rnrnA newer version of this OpenFEMA data set has been released. This older dataset version will no longer be updated and will be archived by the end of April 2020. The following page details the latest version of this data set:https://www.fema.gov/openfema-data-page/hazard-mitigation-assistance-mitigated-properties-v2. CSV and JSON Files can be downloaded from the 'Full Data' section.rnrnTo access the dataset through an API endpoint, visit the 'API Endpoint' section of the above page. Accessing data in this fashion permits data filtering, sorting, and field selection. The OpenFEMA API Documentation page provides information on API usage. rnrnIf you have media inquiries about this dataset, please email the FEMA News Desk FEMA-News-Desk@dhs.gov or call (202) 646-3272.  For inquiries about FEMA's Hazard Mitigation Assistance grant program data and Open government program, please contact the OpenFEMA team via email OpenFEMA@fema.dhs.gov and FEMA-HMAAnalytics@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0385",
             "keyword": [
                 "Threats and Hazards"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-12-02T10:48:00-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Federal Insurance Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Hazard Mitigation Assistance Mitigated Properties"
         },
-            "identifier": "FEMA-0385",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "The Grant Programs Directorate strategically and effectively administers and manages FEMA grants to ensure critical and measurable results for customers and stakeholders. The grants represented in this dataset are Preparedness (Non-Disaster or ND) Grants and Assistance to Firefighters Grants (AFG).rnrnND Grants and AFG are awarded and managed differently within the Grants Program Directorate (GPD) and should be treated with discretion.rnrnThe only measure in this dataset is Award Amount. It is an additive measure that can be applied across multiple dimensions to create various views of the data.rnrnAFG awards are assigned to individual Fire Departments. ND Grants are typically assigned to state agencies; however, exceptions do exist such as Port Security Grant Program which is assigned to port areas and not States. It is important to know that when looking at Award Amount by State it does not mean the State actually received that money. In addition, some grant programs may have pass-through requirements where the recipient State is required to sub-grant a minimum amount of the award and only retain a portion of the award.rnrnGrants guidance is described in the Funding Opportunity Announcement (FOA). Each grant program has its own grant guidance containing eligibility requirements, program objectives, and funding restrictions which are published annually. FOAs are public documents and may be found online at www.fema.gov/grants.rnrnFor more information on grants, visit https://www.fema.gov/grants/preparedness and https://www.fema.gov/grants/preparedness/firefighters rnrnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v4/HazardMitigationAssistanceMitigatedProperties"
+                    "accessURL": "https://www.fema.gov/api/open/v1/NonDisasterAssistanceFirefighterGrants"
                 }
-            ]
-        },
-        {
-            "title": "Non-Disaster and Assistance to Firefighter Grants",
-            "description": "The Grant Programs Directorate strategically and effectively administers and manages FEMA grants to ensure critical and measurable results for customers and stakeholders. The grants represented in this dataset are Preparedness (Non-Disaster or ND) Grants and Assistance to Firefighters Grants (AFG).rnrnND Grants and AFG are awarded and managed differently within the Grants Program Directorate (GPD) and should be treated with discretion.rnrnThe only measure in this dataset is Award Amount. It is an additive measure that can be applied across multiple dimensions to create various views of the data.rnrnAFG awards are assigned to individual Fire Departments. ND Grants are typically assigned to state agencies; however, exceptions do exist such as Port Security Grant Program which is assigned to port areas and not States. It is important to know that when looking at Award Amount by State it does not mean the State actually received that money. In addition, some grant programs may have pass-through requirements where the recipient State is required to sub-grant a minimum amount of the award and only retain a portion of the award.rnrnGrants guidance is described in the Funding Opportunity Announcement (FOA). Each grant program has its own grant guidance containing eligibility requirements, program objectives, and funding restrictions which are published annually. FOAs are public documents and may be found online at www.fema.gov/grants.rnrnFor more information on grants, visit https://www.fema.gov/grants/preparedness and https://www.fema.gov/grants/preparedness/firefighters rnrnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0386",
             "keyword": [
                 "Finance"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-08-01T07:58:54-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Grant Programs Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Non-Disaster and Assistance to Firefighter Grants"
         },
-            "identifier": "FEMA-0386",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "This dataset is a summary of the OpenFEMA Individuals and Households Program - Valid Registrations (NEMIS) dataset and contains aggregated, non-PII data from Housing Assistance Program reporting authority within FEMA's Recovery Directorate to share data on registrations and Individuals and Households Program (IHP).  The data contains counts of program eligibility, referrals and registration methods as well as program award amounts segmented by city where registration is valid. Additionally disaster number, county and zip code are provided.rnrnPlease Note: IHP is intended to help with critical expenses that cannot be covered in other ways. The IHP is not intended to return all homes or belongings to their pre\u00e2\u20ac\u0090disaster condition. In some cases, IHP may only provide enough money, up to the program limits, for you to return an item to service. Secondary or vacation residencies do not qualify. Visit for more information about the program: https://www.fema.gov/assistance/public . rnrnThis is raw, unedited data from FEMA's National Emergency Management Information System (NEMIS) and as such is subject to a small percentage of human error. rnrnThe financial information is derived from NEMIS and not FEMA's official financial systems.  Due to differences in reporting periods, status of obligations and how business rules are applied, this financial information may differ slightly from official publication on public websites such as usaspending.gov;  this dataset is not intended to be used for any official federal financial reporting.rnrnCitation: The Agency's preferred citation for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page, Citing Data section: https://www.fema.gov/about/openfema/terms-conditions .rnrnThis dataset is not intended to be an official federal report, and should not be considered an official federal report.rnrnIf you have media inquiries about this dataset, please email the FEMA News Desk FEMA-News-Desk@dhs.gov or call (202) 646-3272.  For inquiries about FEMA's data and Open government program please contact the OpenFEMA team via email OpenFEMA@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v1/NonDisasterAssistanceFirefighterGrants"
+                    "accessURL": "https://www.fema.gov/api/open/v2/RegistrationIntakeIndividualsHouseholdPrograms"
                 }
-            ]
-        },
-        {
-            "title": "Registration Intake and Individuals Household Program (RI-IHP)",
-            "description": "This dataset is a summary of the OpenFEMA Individuals and Households Program - Valid Registrations (NEMIS) dataset and contains aggregated, non-PII data from Housing Assistance Program reporting authority within FEMA's Recovery Directorate to share data on registrations and Individuals and Households Program (IHP).  The data contains counts of program eligibility, referrals and registration methods as well as program award amounts segmented by city where registration is valid. Additionally disaster number, county and zip code are provided.rnrnPlease Note: IHP is intended to help with critical expenses that cannot be covered in other ways. The IHP is not intended to return all homes or belongings to their pre\u00e2\u20ac\u0090disaster condition. In some cases, IHP may only provide enough money, up to the program limits, for you to return an item to service. Secondary or vacation residencies do not qualify. Visit for more information about the program: https://www.fema.gov/assistance/public . rnrnThis is raw, unedited data from FEMA's National Emergency Management Information System (NEMIS) and as such is subject to a small percentage of human error. rnrnThe financial information is derived from NEMIS and not FEMA's official financial systems.  Due to differences in reporting periods, status of obligations and how business rules are applied, this financial information may differ slightly from official publication on public websites such as usaspending.gov;  this dataset is not intended to be used for any official federal financial reporting.rnrnCitation: The Agency's preferred citation for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page, Citing Data section: https://www.fema.gov/about/openfema/terms-conditions .rnrnThis dataset is not intended to be an official federal report, and should not be considered an official federal report.rnrnIf you have media inquiries about this dataset, please email the FEMA News Desk FEMA-News-Desk@dhs.gov or call (202) 646-3272.  For inquiries about FEMA's data and Open government program please contact the OpenFEMA team via email OpenFEMA@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0387",
             "keyword": [
                 "Incidents"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-12-02T10:48:00-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Response and Recovery/Recovery Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Registration Intake and Individuals Household Program (RI-IHP)"
         },
-            "identifier": "FEMA-0387",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Metadata for the OpenFEMA API data set fields. It contains descriptions, data types, and other attributes for each field.rnrnIf you have media inquiries about this dataset please email the FEMA News Desk FEMA-News-Desk@dhs.gov or call (202) 646-3272.  For inquiries about FEMA's data and Open government program please contact the OpenFEMA team via email OpenFEMA@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v2/RegistrationIntakeIndividualsHouseholdPrograms"
+                    "accessURL": "https://www.fema.gov/api/open/v1/OpenFemaDataSetFields"
                 }
-            ]
-        },
-        {
-            "title": "OpenFEMA Data Set Fields",
-            "description": "Metadata for the OpenFEMA API data set fields. It contains descriptions, data types, and other attributes for each field.rnrnIf you have media inquiries about this dataset please email the FEMA News Desk FEMA-News-Desk@dhs.gov or call (202) 646-3272.  For inquiries about FEMA's data and Open government program please contact the OpenFEMA team via email OpenFEMA@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0388",
             "keyword": [
                 "External Coordination"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-12-02T10:48:00-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Mission Support/Office of Chief Information Officer"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "OpenFEMA Data Set Fields"
         },
-            "identifier": "FEMA-0388",
+        {
             "accessLevel": "public",
-            "bureauCode": [
-                "024:070"
-            ],
-            "programCode": [
-                "024:000"
+            "bureauCode": [
+                "024:070"
             ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Individual Assistance (IA) is provided by the Federal Emergency Management Agency (FEMA) to individuals and families who have sustained losses due to disasters.rnHomeowners, renters, and business owners in designated counties who sustained damage to their homes, vehicles, personal property, businesses, or inventory as a result of a federally declared disaster may apply for disaster assistance.rnDisaster assistance may include grants to help pay for temporary housing, emergency home repairs, uninsured and underinsured personal property losses, medical, dental, and funeral expenses caused by the disaster, along with other serious disaster-related expenses.rnDisaster assistance grants are not taxable income and will not affect eligibility for Social Security, Medicaid, medical waiver programs, welfare assistance, Temporary Assistance for Needy Families, food stamps, Supplemental Security Income, or Social Security Disability Insurance.rnThis dataset contains detailed non-PII data on the Individuals and Households Program (IHP). FEMA provides assistance to individuals and households through the IA program, comprised of two categories of assistance: Housing Assistance (HA) and Other Needs Assistance (ONA). For more information read FEMA's IHP unified guidance: https://www.fema.gov/sites/default/files/2020-05/IHP_Unified_Guidance_FINAL_09272016_0.pdfrnThis dataset is scheduled to be superceded by Valid Registrations V2 by early CY 2024.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v1/OpenFemaDataSetFields"
+                    "accessURL": "https://www.fema.gov/api/open/v1/IndividualAssistanceHousingRegistrantsLargeDisasters"
                 }
-            ]
-        },
-        {
-            "title": "Individual Assistance Housing Registrants - Large Disasters",
-            "description": "Individual Assistance (IA) is provided by the Federal Emergency Management Agency (FEMA) to individuals and families who have sustained losses due to disasters.rnHomeowners, renters, and business owners in designated counties who sustained damage to their homes, vehicles, personal property, businesses, or inventory as a result of a federally declared disaster may apply for disaster assistance.rnDisaster assistance may include grants to help pay for temporary housing, emergency home repairs, uninsured and underinsured personal property losses, medical, dental, and funeral expenses caused by the disaster, along with other serious disaster-related expenses.rnDisaster assistance grants are not taxable income and will not affect eligibility for Social Security, Medicaid, medical waiver programs, welfare assistance, Temporary Assistance for Needy Families, food stamps, Supplemental Security Income, or Social Security Disability Insurance.rnThis dataset contains detailed non-PII data on the Individuals and Households Program (IHP). FEMA provides assistance to individuals and households through the IA program, comprised of two categories of assistance: Housing Assistance (HA) and Other Needs Assistance (ONA). For more information read FEMA's IHP unified guidance: https://www.fema.gov/sites/default/files/2020-05/IHP_Unified_Guidance_FINAL_09272016_0.pdfrnThis dataset is scheduled to be superceded by Valid Registrations V2 by early CY 2024.",
+            ],
+            "identifier": "FEMA-0389",
             "keyword": [
                 "Incidents"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-12-02T10:48:00-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Response and Recovery/Recovery Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Individual Assistance Housing Registrants - Large Disasters"
         },
-            "identifier": "FEMA-0389",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "FEMA provides supplemental Federal disaster grant assistance for debris removal, emergency protective measures, and the repair, replacement, or restoration of disaster-damaged, publicly owned facilities and the facilities of certain Private Non-Profit (PNP) organizations through the Public Assistance (PA) Program (CDFA Number 97.036). The PA Program also encourages protection of these damaged facilities from future events by providing assistance for 406 hazard mitigation measures during the recovery process.rnThis dataset lists all public assistance applicants (subrecipients) and a summary of the funded program support. This is raw, unedited data from FEMA's Emergency Management Mission Integrated Environment (EMMIE) and as such is subject to a small percentage of human error. The financial information is derived from EMMIE and not FEMA's official financial systems.rnDue to differences in reporting periods, status of obligations, and application of business rules, this financial information may differ slightly from official publication on public websites such as usaspending.gov. This dataset is not intended to be used for any official federal reporting.rnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v1/IndividualAssistanceHousingRegistrantsLargeDisasters"
+                    "accessURL": "https://www.fema.gov/api/open/v1/PublicAssistanceFundedProjectsSummaries"
                 }
-            ]
-        },
-        {
-            "title": "Public Assistance Funded Project Summaries",
-            "description": "FEMA provides supplemental Federal disaster grant assistance for debris removal, emergency protective measures, and the repair, replacement, or restoration of disaster-damaged, publicly owned facilities and the facilities of certain Private Non-Profit (PNP) organizations through the Public Assistance (PA) Program (CDFA Number 97.036). The PA Program also encourages protection of these damaged facilities from future events by providing assistance for 406 hazard mitigation measures during the recovery process.rnThis dataset lists all public assistance applicants (subrecipients) and a summary of the funded program support. This is raw, unedited data from FEMA's Emergency Management Mission Integrated Environment (EMMIE) and as such is subject to a small percentage of human error. The financial information is derived from EMMIE and not FEMA's official financial systems.rnDue to differences in reporting periods, status of obligations, and application of business rules, this financial information may differ slightly from official publication on public websites such as usaspending.gov. This dataset is not intended to be used for any official federal reporting.rnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0390",
             "keyword": [
                 "Incidents"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-12-02T10:48:00-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Response and Recovery/Recovery Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Public Assistance Funded Project Summaries"
         },
-            "identifier": "FEMA-0390",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "This dataset contains data on Public Assistance (PA) project awards (obligations), including the project obligation date(s); dollar amount of Federal Share Obligated for each project and its obligation date(s); FEMA region; state; disaster declaration number; descriptive cause of the declaration (incident type); entity requesting public assistance (applicant name); and distinct name for the repair, replacement or mitigation work listed for assistance (Project Title). The PA Grant Awards Activities dataset does not collect, maintain, use, or disseminate any Personally Identifiable Information (PII).rnrnAs part of Congressional bill HR 152 - the Sandy Recovery Improvement Act of 2013, FEMA is providing the following information for our stakeholders:rn\u2022 Regionrn\u2022 Disaster Declaration Numberrn\u2022 Disaster Typern\u2022 Statern\u2022 Applicantrn\u2022 Countyrn\u2022 Damage Category Codern\u2022 Federal Share Obligatedrn\u2022 Date ObligatedrnrnFEMA obligates funding for a project directly to the Recipient (State or Tribe). It is the Recipient's responsibility to ensure that the eligible subrecipient (listed in the dataset as Applicant Name) receives the award funding.rnThis dataset lists details about project versions. Versions occur when the scope/cost changes for a project.  Versions adjust the cost of the project  with positive additions called obligations and subtractions called deobligations.  Combined, they reconcile to reflect the Total Federal Share Obligation, but reconciliation occurs over the life of the project, sometimes years after the declaration date.  The dataset represents project obligations within a seven-day period prior to the listed date but does not include obligations uploaded on the same day as the publication.  Open projects still under pre-obligation processing are not represented.rnFor more information on the Public Assistance process see: https://www.fema.gov/assistance/public/process.rnThis is raw, unedited data from FEMA's Emergency Management Mission Integrated Environment (EMMIE) system and as such is subject to a small percentage of human error. The financial information is derived from EMMIE and not FEMA's official financial systems. Due to differences in reporting periods, status of obligations and application of business rules, this financial information may differ slightly from official publication on public websites such as usaspending.gov. This dataset is not intended to be used for any official federal reporting.rnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v1/PublicAssistanceFundedProjectsSummaries"
+                    "accessURL": "https://www.fema.gov/openfema-data-page/public-assistance-grant-award-activities-v1"
                 }
-            ]
-        },
-        {
-            "title": "Public Assistance Grant Award Activities (EMMIE)",
-            "description": "This dataset contains data on Public Assistance (PA) project awards (obligations), including the project obligation date(s); dollar amount of Federal Share Obligated for each project and its obligation date(s); FEMA region; state; disaster declaration number; descriptive cause of the declaration (incident type); entity requesting public assistance (applicant name); and distinct name for the repair, replacement or mitigation work listed for assistance (Project Title). The PA Grant Awards Activities dataset does not collect, maintain, use, or disseminate any Personally Identifiable Information (PII).rnrnAs part of Congressional bill HR 152 - the Sandy Recovery Improvement Act of 2013, FEMA is providing the following information for our stakeholders:rn\u2022 Regionrn\u2022 Disaster Declaration Numberrn\u2022 Disaster Typern\u2022 Statern\u2022 Applicantrn\u2022 Countyrn\u2022 Damage Category Codern\u2022 Federal Share Obligatedrn\u2022 Date ObligatedrnrnFEMA obligates funding for a project directly to the Recipient (State or Tribe). It is the Recipient's responsibility to ensure that the eligible subrecipient (listed in the dataset as Applicant Name) receives the award funding.rnThis dataset lists details about project versions. Versions occur when the scope/cost changes for a project.  Versions adjust the cost of the project  with positive additions called obligations and subtractions called deobligations.  Combined, they reconcile to reflect the Total Federal Share Obligation, but reconciliation occurs over the life of the project, sometimes years after the declaration date.  The dataset represents project obligations within a seven-day period prior to the listed date but does not include obligations uploaded on the same day as the publication.  Open projects still under pre-obligation processing are not represented.rnFor more information on the Public Assistance process see: https://www.fema.gov/assistance/public/process.rnThis is raw, unedited data from FEMA's Emergency Management Mission Integrated Environment (EMMIE) system and as such is subject to a small percentage of human error. The financial information is derived from EMMIE and not FEMA's official financial systems. Due to differences in reporting periods, status of obligations and application of business rules, this financial information may differ slightly from official publication on public websites such as usaspending.gov. This dataset is not intended to be used for any official federal reporting.rnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0391",
             "keyword": [
                 "Incidents"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-07-01T07:47:18-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Response and Recovery/Recovery Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Public Assistance Grant Award Activities (EMMIE)"
         },
-            "identifier": "FEMA-0391",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "The Public Assistance (PA) Funded Projects Details dataset contains a list of funded (obligated) PA projects, called project worksheets. Unobligated projects (still in formulation) are not represented.  The Applicant ID is provided for this dataset to be used with the OpenFEMA \u201cPublic Assistance Applicants - v1\u201d dataset.rnFEMA provides supplemental Federal disaster grant assistance for debris removal, emergency protective measures, and the repair, replacement, or restoration of disaster-damaged, publicly owned facilities and the facilities of certain Private Non-Profit (PNP) organizations through the PA Program (CDFA Number 97.036). The PA Program also encourages protection of these damaged facilities from future events by providing assistance for 406 hazard mitigation measures during the recovery process.rnThis is raw, unedited data from FEMA's Emergency Management Mission Integrated Environment (EMMIE) and as such is subject to a small percentage of human error. The financial information is derived from EMMIE and not FEMA's official financial systems. Due to differences in reporting periods, status of obligations, and application of business rules, this financial information may differ slightly from official publication on public websites such as www.usaspending.gov . This dataset is not intended to be used for any official federal reporting.rnThe data has been incorporated into a graphic visualization at Public Assistance Program Summary of Obligations: https://www.fema.gov/data-visualization/public-assistance-program-summary-obligations. Questions pertaining to the data visualizations should be addressed to EnterpriseAnalytics@fema.dhs.gov.rnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/openfema-data-page/public-assistance-grant-award-activities-v1"
+                    "accessURL": "https://www.fema.gov/api/open/v1/PublicAssistanceFundedProjectsDetails"
                 }
-            ]
-        },
-        {
-            "title": "Public Assistance Funded Projects Details",
-            "description": "The Public Assistance (PA) Funded Projects Details dataset contains a list of funded (obligated) PA projects, called project worksheets. Unobligated projects (still in formulation) are not represented.  The Applicant ID is provided for this dataset to be used with the OpenFEMA \u201cPublic Assistance Applicants - v1\u201d dataset.rnFEMA provides supplemental Federal disaster grant assistance for debris removal, emergency protective measures, and the repair, replacement, or restoration of disaster-damaged, publicly owned facilities and the facilities of certain Private Non-Profit (PNP) organizations through the PA Program (CDFA Number 97.036). The PA Program also encourages protection of these damaged facilities from future events by providing assistance for 406 hazard mitigation measures during the recovery process.rnThis is raw, unedited data from FEMA's Emergency Management Mission Integrated Environment (EMMIE) and as such is subject to a small percentage of human error. The financial information is derived from EMMIE and not FEMA's official financial systems. Due to differences in reporting periods, status of obligations, and application of business rules, this financial information may differ slightly from official publication on public websites such as www.usaspending.gov . This dataset is not intended to be used for any official federal reporting.rnThe data has been incorporated into a graphic visualization at Public Assistance Program Summary of Obligations: https://www.fema.gov/data-visualization/public-assistance-program-summary-obligations. Questions pertaining to the data visualizations should be addressed to EnterpriseAnalytics@fema.dhs.gov.rnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0392",
             "keyword": [
                 "Incidents"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-12-02T10:48:00-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Response and Recovery/Recovery Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Public Assistance Funded Projects Details"
         },
-            "identifier": "FEMA-0392",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "The dataset contains disaster level financial information for FEMA's Hazard Mitigation Grant Program (HMGP). The purpose of HMGP is to help communities implement hazard mitigation measures following a Presidential Major Disaster Declaration in the areas of the State, Tribe, or Territory requested by the Governor or Tribal Executive. For more information on the Hazard Mitigation Grant Program, please visit: https://www.fema.gov/grants/mitigationrnrnAdditional disaster level information can be found here: https://www.fema.gov/openfema-data-page/disaster-declarations-summaries-v2rnrnInformation on projects funded under the Hazard Mitigation Grant Program can found here: https://www.fema.gov/openfema-data-page/hazard-mitigation-assistance-projects-v2rnrnThis is raw, unedited data from FEMA's National Emergency Management Information System (NEMIS) and as such is subject to a small percentage of human error. The financial information is derived from NEMIS and not FEMA's official financial systems. Due to differences in reporting periods, status of obligations and how business rules are applied, this financial information may differ slightly from official publication on public websites such as usaspending.gov; this dataset is not intended to be used for any official federal financial reporting.rnrnMissing values - In some cases data was not provided by the subgrantee (subrecipient), grantee (recipient) and/or entered into the FEMA mitigation grant systems. The information is likely available as part of the paper file which is considered the file of record.rnrnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v1/PublicAssistanceFundedProjectsDetails"
+                    "accessURL": "https://www.fema.gov/api/open/v2/HazardMitigationGrantProgramDisasterSummaries"
                 }
-            ]
-        },
-        {
-            "title": "Hazard Mitigation Grant Program - Disaster Summaries",
-            "description": "The dataset contains disaster level financial information for FEMA's Hazard Mitigation Grant Program (HMGP). The purpose of HMGP is to help communities implement hazard mitigation measures following a Presidential Major Disaster Declaration in the areas of the State, Tribe, or Territory requested by the Governor or Tribal Executive. For more information on the Hazard Mitigation Grant Program, please visit: https://www.fema.gov/grants/mitigationrnrnAdditional disaster level information can be found here: https://www.fema.gov/openfema-data-page/disaster-declarations-summaries-v2rnrnInformation on projects funded under the Hazard Mitigation Grant Program can found here: https://www.fema.gov/openfema-data-page/hazard-mitigation-assistance-projects-v2rnrnThis is raw, unedited data from FEMA's National Emergency Management Information System (NEMIS) and as such is subject to a small percentage of human error. The financial information is derived from NEMIS and not FEMA's official financial systems. Due to differences in reporting periods, status of obligations and how business rules are applied, this financial information may differ slightly from official publication on public websites such as usaspending.gov; this dataset is not intended to be used for any official federal financial reporting.rnrnMissing values - In some cases data was not provided by the subgrantee (subrecipient), grantee (recipient) and/or entered into the FEMA mitigation grant systems. The information is likely available as part of the paper file which is considered the file of record.rnrnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0393",
             "keyword": [
                 "Threats and Hazards"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-12-02T10:48:00-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Federal Insurance Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Hazard Mitigation Grant Program - Disaster Summaries"
         },
-            "identifier": "FEMA-0393",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "The data found on this page comes from the Hazard Mitigation Planning Program's Mitigation Planning Portal (MPP). The MPP is an online platform for tracking and reporting on mitigation plans and related data elements across all ten Federal Emergency Management Agency (FEMA) Regions. MPP data provides insight into which jurisdictions are participating in mitigation plans across the country and what the status of those plans are. Additionally, MPP data provides dates to support tracking of when plans are approved and when they are set to expire which FEMA uses to monitor and support disaster preparedness and resilience.rnHazard mitigation planning reduces loss of life and property by minimizing the impact of disasters. It begins with state, tribal, territorial and local governments identifying natural disaster risks and vulnerabilities that are common in their area. After identifying these risks, they develop long-term strategies for protecting people and property from similar events. Mitigation plans are key to breaking the cycle of disaster damage and reconstruction. When applying for certain types of non-emergency disaster assistance, FEMA requires a hazard mitigation plan. These requirements are part of the laws, regulations and policy surrounding hazard mitigation planning. For more information, visit Hazard Mitigation Planning (https://www.fema.gov/emergency-managers/risk-management/hazard-mitigation-planning)rnrnHazard mitigation plans enable state, tribal, territorial, and local governments to: rnulli Increase education and awareness around threats, hazards, risk, and vulnerabilities/liliBuild partnerships for risk reduction with governments, organizations, businesses, and the public/liliIdentify long-term strategies that seek to reduce risk/liliAlign risk reduction with other state, tribal, territorial or local objectives/liliIdentify implementation actions to focus resources on the greatest risks and vulnerabilities/liliConnect priorities to potential funding sources/liliIncrease investment in mitigation actions/li/ulrnrnA FEMA-approved hazard mitigation plan is needed to receive certain types of non-emergency disaster assistance.rnrnrnPlease note that jurisdictions may participate in multiple plans. This is raw, unedited data that is dependent on Regional entry, as such it is subject to human error and delayed entry of plan information. The data is updated from authoritative sources and has a minimum 24 hour delay.rnCitation: The Agency's preferred citation for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page, Citing Data section: https://www.fema.gov/about/openfema/terms-conditions. rnPlace name may differ from official naming standard referenced in update organization documents (i.e. Tribal name under BIA list or other authoritative source Village of, City of, etc.).rnrnIf you have media inquiries about this dataset, please email the FEMA News Desk FEMA-News-Desk@dhs.gov or call (202) 646-3272.  For inquiries about FEMA's data and Open government program please contact the OpenFEMA team via email OpenFEMA@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v2/HazardMitigationGrantProgramDisasterSummaries"
+                    "accessURL": "https://www.fema.gov/api/open/v1/HazardMitigationPlanStatuses"
                 }
-            ]
-        },
-        {
-            "title": "Hazard Mitigation Plan Statuses (OpenFEMA)",
-            "description": "The data found on this page comes from the Hazard Mitigation Planning Program's Mitigation Planning Portal (MPP). The MPP is an online platform for tracking and reporting on mitigation plans and related data elements across all ten Federal Emergency Management Agency (FEMA) Regions. MPP data provides insight into which jurisdictions are participating in mitigation plans across the country and what the status of those plans are. Additionally, MPP data provides dates to support tracking of when plans are approved and when they are set to expire which FEMA uses to monitor and support disaster preparedness and resilience.rnHazard mitigation planning reduces loss of life and property by minimizing the impact of disasters. It begins with state, tribal, territorial and local governments identifying natural disaster risks and vulnerabilities that are common in their area. After identifying these risks, they develop long-term strategies for protecting people and property from similar events. Mitigation plans are key to breaking the cycle of disaster damage and reconstruction. When applying for certain types of non-emergency disaster assistance, FEMA requires a hazard mitigation plan. These requirements are part of the laws, regulations and policy surrounding hazard mitigation planning. For more information, visit Hazard Mitigation Planning (https://www.fema.gov/emergency-managers/risk-management/hazard-mitigation-planning)rnrnHazard mitigation plans enable state, tribal, territorial, and local governments to: rnulli Increase education and awareness around threats, hazards, risk, and vulnerabilities/liliBuild partnerships for risk reduction with governments, organizations, businesses, and the public/liliIdentify long-term strategies that seek to reduce risk/liliAlign risk reduction with other state, tribal, territorial or local objectives/liliIdentify implementation actions to focus resources on the greatest risks and vulnerabilities/liliConnect priorities to potential funding sources/liliIncrease investment in mitigation actions/li/ulrnrnA FEMA-approved hazard mitigation plan is needed to receive certain types of non-emergency disaster assistance.rnrnrnPlease note that jurisdictions may participate in multiple plans. This is raw, unedited data that is dependent on Regional entry, as such it is subject to human error and delayed entry of plan information. The data is updated from authoritative sources and has a minimum 24 hour delay.rnCitation: The Agency's preferred citation for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page, Citing Data section: https://www.fema.gov/about/openfema/terms-conditions. rnPlace name may differ from official naming standard referenced in update organization documents (i.e. Tribal name under BIA list or other authoritative source Village of, City of, etc.).rnrnIf you have media inquiries about this dataset, please email the FEMA News Desk FEMA-News-Desk@dhs.gov or call (202) 646-3272.  For inquiries about FEMA's data and Open government program please contact the OpenFEMA team via email OpenFEMA@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0394",
             "keyword": [
                 "Assessments"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-12-02T10:48:00-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Risk Management Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Hazard Mitigation Plan Statuses (OpenFEMA)"
         },
-            "identifier": "FEMA-0394",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "This dataset contains FEMA applicant-level data for the Individuals and Households Program (IHP). All PII information has been removed. The location is represented by county, city, and zip code. This dataset contains Individual Assistance (IA) applications from DR1439 (declared in 2002) to those declared over 30 days ago. The full data set is refreshed on an annual basis and refreshed weekly to update disasters declared in the last 18 months. This dataset includes all major disasters and includes only valid registrants (applied in a declared county, within the registration period, having damage due to the incident and damage within the incident period). Information about individual data elements and descriptions are listed in the metadata information within the dataset.rnValid registrants may be eligible for IA assistance, which is intended to meet basic needs and supplement disaster recovery efforts. IA assistance is not intended to return disaster-damaged property to its pre-disaster condition. Disaster damage to secondary or vacation homes does not qualify for IHP assistance.rnData comes from FEMA's National Emergency Management Information System (NEMIS) with raw, unedited, self-reported content and subject to a small percentage of human error.rnAny financial information is derived from NEMIS and not FEMA's official financial systems. Due to differences in reporting periods, status of obligations and application of business rules, this financial information may differ slightly from official publication on public websites such as usaspending.gov. This dataset is not intended to be used for any official federal reporting. rnCitation: The Agency\u2019s preferred citation for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page, Citing Data section: https://www.fema.gov/about/openfema/terms-conditions.rnDue to the size of this file, tools other than a spreadsheet may be required to analyze, visualize, and manipulate the data. MS Excel will not be able to process files this large without data loss. It is recommended that a database (e.g., MS Access, MySQL, PostgreSQL, etc.) be used to store and manipulate data. Other programming tools such as R, Apache Spark, and Python can also be used to analyze and visualize data. Further, basic Linux/Unix tools can be used to manipulate, search, and modify large files.rnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.rnThis dataset is scheduled to be superceded by Valid Registrations Version 2 by early CY 2024.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v1/HazardMitigationPlanStatuses"
+                    "accessURL": "https://www.fema.gov/api/open/v1/IndividualsAndHouseholdsProgramValidRegistrations"
                 }
-            ]
-        },
-        {
-            "title": "Individuals and Households Program - Valid Registrations",
-            "description": "This dataset contains FEMA applicant-level data for the Individuals and Households Program (IHP). All PII information has been removed. The location is represented by county, city, and zip code. This dataset contains Individual Assistance (IA) applications from DR1439 (declared in 2002) to those declared over 30 days ago. The full data set is refreshed on an annual basis and refreshed weekly to update disasters declared in the last 18 months. This dataset includes all major disasters and includes only valid registrants (applied in a declared county, within the registration period, having damage due to the incident and damage within the incident period). Information about individual data elements and descriptions are listed in the metadata information within the dataset.rnValid registrants may be eligible for IA assistance, which is intended to meet basic needs and supplement disaster recovery efforts. IA assistance is not intended to return disaster-damaged property to its pre-disaster condition. Disaster damage to secondary or vacation homes does not qualify for IHP assistance.rnData comes from FEMA's National Emergency Management Information System (NEMIS) with raw, unedited, self-reported content and subject to a small percentage of human error.rnAny financial information is derived from NEMIS and not FEMA's official financial systems. Due to differences in reporting periods, status of obligations and application of business rules, this financial information may differ slightly from official publication on public websites such as usaspending.gov. This dataset is not intended to be used for any official federal reporting. rnCitation: The Agency\u2019s preferred citation for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page, Citing Data section: https://www.fema.gov/about/openfema/terms-conditions.rnDue to the size of this file, tools other than a spreadsheet may be required to analyze, visualize, and manipulate the data. MS Excel will not be able to process files this large without data loss. It is recommended that a database (e.g., MS Access, MySQL, PostgreSQL, etc.) be used to store and manipulate data. Other programming tools such as R, Apache Spark, and Python can also be used to analyze and visualize data. Further, basic Linux/Unix tools can be used to manipulate, search, and modify large files.rnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.rnThis dataset is scheduled to be superceded by Valid Registrations Version 2 by early CY 2024.",
+            ],
+            "identifier": "FEMA-0395",
             "keyword": [
                 "Incidents"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-12-02T10:48:00-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Response and Recovery/Recovery Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Individuals and Households Program - Valid Registrations"
         },
-            "identifier": "FEMA-0395",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Metadata for the OpenFEMA API data sets. It contains attributes regarding the published datasets including but not limited to update frequency, description, version, and deprecation status.rnrnIf you have media inquiries about this dataset please email the FEMA News Desk FEMA-News-Desk@dhs.gov or call (202) 646-3272.  For inquiries about FEMA's data and Open government program please contact the OpenFEMA team via email OpenFEMA@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v1/IndividualsAndHouseholdsProgramValidRegistrations"
+                    "accessURL": "https://www.fema.gov/api/open/v1/OpenFemaDataSets"
                 }
-            ]
-        },
-        {
-            "title": "OpenFEMA Data Sets",
-            "description": "Metadata for the OpenFEMA API data sets. It contains attributes regarding the published datasets including but not limited to update frequency, description, version, and deprecation status.rnrnIf you have media inquiries about this dataset please email the FEMA News Desk FEMA-News-Desk@dhs.gov or call (202) 646-3272.  For inquiries about FEMA's data and Open government program please contact the OpenFEMA team via email OpenFEMA@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0396",
             "keyword": [
                 "External Coordination"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-12-02T10:48:00-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Mission Support/Office of Chief Information Officer"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "OpenFEMA Data Sets"
         },
-            "identifier": "FEMA-0396",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Mission Assignment, as defined in the 44 Code of Federal Regulations, is a work order issued by FEMA to another Federal agency directing completion of a specified task and citing funding, other managerial controls, and guidance. rnMission Assignments are essential and powerful tools for federal emergency management under the Stafford Act.  Mission Assignments are distinct because they allow for deployment, employment, and assistance from the full range of federal resources to support disaster needs.rnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v1/OpenFemaDataSets"
+                    "accessURL": "https://www.fema.gov/api/open/v2/MissionAssignments"
                 }
-            ]
-        },
-        {
-            "title": "Mission Assignments",
-            "description": "Mission Assignment, as defined in the 44 Code of Federal Regulations, is a work order issued by FEMA to another Federal agency directing completion of a specified task and citing funding, other managerial controls, and guidance. rnMission Assignments are essential and powerful tools for federal emergency management under the Stafford Act.  Mission Assignments are distinct because they allow for deployment, employment, and assistance from the full range of federal resources to support disaster needs.rnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0399",
             "keyword": [
                 "External Coordination"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-12-02T10:48:00-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Response and Recovery/Response Directorate"
             },
+            "rights": null,
+            "title": "Mission Assignments"
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "024:056"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Open Data (MGMT)",
                 "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-            "identifier": "FEMA-0399",
-            "accessLevel": "public",
-            "bureauCode": [
-                "024:070"
-            ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "description": "The Freedom of Information Act (FOIA) requires FOIA reading Rooms contain four distinct categories of records. The four categories of Reading Room records are: 1) final opinions and orders made in the adjudication of cases; 2) specific agency policy statements; 3) administrative staff manuals and instructions to staff that affect a member of the public; and 4) records disclosed in response to a FOIA request that the agency determines have become or are likely to become the subject of subsequent requests for substantially the same records. Freedom of Information Act Archive includes TSA FOIA documents prior to May 2017.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v2/MissionAssignments"
+                    "accessURL": "https://www.dhs.gov/tsa-foia-library"
                 }
-            ]
-        },
-        {
-            "title": "TSA FOIA Archive",
-            "description": "The Freedom of Information Act (FOIA) requires FOIA reading Rooms contain four distinct categories of records. The four categories of Reading Room records are: 1) final opinions and orders made in the adjudication of cases; 2) specific agency policy statements; 3) administrative staff manuals and instructions to staff that affect a member of the public; and 4) records disclosed in response to a FOIA request that the agency determines have become or are likely to become the subject of subsequent requests for substantially the same records. Freedom of Information Act Archive includes TSA FOIA documents prior to May 2017.",
+            ],
+            "identifier": "TSA-b9bfcb94-631a-4719-97da-a9f57f3f6d10",
             "keyword": [
                 "Archive",
                 "FOIA",
                 "Freedom of Information Act"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-22T12:25:28-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
+            "rights": null,
+            "title": "TSA FOIA Archive"
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "024:070"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Open Data (MGMT)",
                 "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-            "identifier": "TSA-b9bfcb94-631a-4719-97da-a9f57f3f6d10",
-            "accessLevel": "public",
-            "bureauCode": [
-                "024:056"
-            ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "description": "Mitigation Best Practices are stories, articles or case studies about individuals, businesses or communities that undertook successful efforts to reduce or eliminate disaster risks.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.dhs.gov/tsa-foia-library"
+                    "accessURL": "https://www.fema.gov/emergency-managers/risk/hazard-mitigation-planning/best-practices"
                 }
-            ]
-        },
-        {
-            "title": "MP Web Content (Drupal/Diamond)",
-            "description": "Mitigation Best Practices are stories, articles or case studies about individuals, businesses or communities that undertook successful efforts to reduce or eliminate disaster risks.",
+            ],
+            "identifier": "FEMA-0200",
             "keyword": [
                 "Communications"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-10-02T14:25:01-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Federal Insurance Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "MP Web Content (Drupal/Diamond)"
         },
-            "identifier": "FEMA-0200",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Per the Federal Digital Government Strategy, the Department of Homeland Security Metrics Plan, and the Open FEMA Initiative, FEMA is providing the following web performance metrics with regards to FEMA.gov.rnrnInformation in this dataset includes total visits, avg visit duration, pageviews, unique visitors, avg pages/visit, avg time/page, bounce ratevisits by source, visits by Social Media Platform, and metrics on new vs returning visitors.rnrnExternal Affairs strives to make all communications accessible. If you have any challenges accessing this information, please contact FEMAWebTeam@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/emergency-managers/risk/hazard-mitigation-planning/best-practices"
+                    "accessURL": "https://www.fema.gov/about/website-information/metrics"
                 }
-            ]
-        },
-        {
-            "title": "Website Metrics",
-            "description": "Per the Federal Digital Government Strategy, the Department of Homeland Security Metrics Plan, and the Open FEMA Initiative, FEMA is providing the following web performance metrics with regards to FEMA.gov.rnrnInformation in this dataset includes total visits, avg visit duration, pageviews, unique visitors, avg pages/visit, avg time/page, bounce ratevisits by source, visits by Social Media Platform, and metrics on new vs returning visitors.rnrnExternal Affairs strives to make all communications accessible. If you have any challenges accessing this information, please contact FEMAWebTeam@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0307",
             "keyword": [
                 "Information Technology"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-09-09T07:52:37-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Office of External Affairs/Communication Division"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Website Metrics"
         },
-            "identifier": "FEMA-0307",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "FEMA Advance Contracts for goods and services are competed and awarded in advance of major disaster declarations to provide efficient, cost-effective means for rapid delivery of supplies and services for recurring disaster response and recovery requirements.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/about/website-information/metrics"
+                    "accessURL": "https://www.fema.gov/businesses-organizations/doing-business/advanced-contracts"
                 }
-            ]
-        },
-        {
-            "title": "Advance Contracts of Goods and Services",
-            "description": "FEMA Advance Contracts for goods and services are competed and awarded in advance of major disaster declarations to provide efficient, cost-effective means for rapid delivery of supplies and services for recurring disaster response and recovery requirements.",
+            ],
+            "identifier": "FEMA-0310",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-07-01T07:47:17-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Advance Contracts of Goods and Services"
         },
-            "identifier": "FEMA-0310",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "The primary goal of the Assistance to Firefighters Grant (AFG) is to meet the firefighting and emergency response needs of fire departments and non-affiliated emergency medical service organizations.rnrnSince 2001, AFG has helped firefighters and other first responders obtain critically needed equipment, protective gear, emergency vehicles, training and other resources necessary for protecting the public and emergency personnel from fire and related hazards.rnrnDataset contains information on the organization that received the grant, the total amount of grant award, when the grant was awarded, category and program related to the grant, and the state the awardee resides in.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/businesses-organizations/doing-business/advanced-contracts"
+                    "accessURL": "https://www.fema.gov/grants/preparedness/firefighters/assistance-grants"
                 }
-            ]
-        },
-        {
-            "title": "Assistance To Firefighters Grants",
-            "description": "The primary goal of the Assistance to Firefighters Grant (AFG) is to meet the firefighting and emergency response needs of fire departments and non-affiliated emergency medical service organizations.rnrnSince 2001, AFG has helped firefighters and other first responders obtain critically needed equipment, protective gear, emergency vehicles, training and other resources necessary for protecting the public and emergency personnel from fire and related hazards.rnrnDataset contains information on the organization that received the grant, the total amount of grant award, when the grant was awarded, category and program related to the grant, and the state the awardee resides in.",
+            ],
+            "identifier": "FEMA-0314",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2025-01-02T13:11:38-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Grants Programs Director"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Assistance To Firefighters Grants"
         },
-            "identifier": "FEMA-0314",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:fema-datainventoryprogram@fema.dhs.gov"
+            },
+            "description": "This dataset contains past congressional testimony and speeches from FEMA administration officials,\u00a0in PDF format.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/grants/preparedness/firefighters/assistance-grants"
+                    "accessURL": "https://www.fema.gov/about/offices/external-affairs/congressional-testimony"
                 }
-            ]
-        },
-        {
-            "title": "Congressional Testimony",
-            "description": "This dataset contains past congressional testimony and speeches from FEMA administration officials,\u00a0in PDF format.",
+            ],
+            "identifier": "FEMA-0317",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-06-28T15:17:16-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Office of External Affairs/Communication Division"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:fema-datainventoryprogram@fema.dhs.gov"
+            "rights": null,
+            "title": "Congressional Testimony"
         },
-            "identifier": "FEMA-0317",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "FEMA\u00e2\u20ac\u2122s Coordinated Needs Management Strategy (CNMS) uses a geospatial database to identify and track flood hazard study lifecycle and mapping needs within the flood hazard mapping program. CNMS supports community officials and FEMA personnel in analyzing and depicting the validity of flood studies to enhance the understanding of flood hazard risk and make informed decisions on community planning and flood mitigation.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/about/offices/external-affairs/congressional-testimony"
+                    "accessURL": "https://www.fema.gov/flood-maps/tools-resources/risk-map/coordinated-needs-management-strategy"
                 }
-            ]
-        },
-        {
-            "title": "Coordinated Needs Management Strategy",
-            "description": "FEMA\u00e2\u20ac\u2122s Coordinated Needs Management Strategy (CNMS) uses a geospatial database to identify and track flood hazard study lifecycle and mapping needs within the flood hazard mapping program. CNMS supports community officials and FEMA personnel in analyzing and depicting the validity of flood studies to enhance the understanding of flood hazard risk and make informed decisions on community planning and flood mitigation.",
+            ],
+            "identifier": "FEMA-0318",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-05-01T10:30:19-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Federal Insurance and Mitigation Administration"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Coordinated Needs Management Strategy"
         },
-            "identifier": "FEMA-0318",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Provides details on total number of applications and funding dispersed by FEMA by state for Funeral Assistance related to the COVID pandemic.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/flood-maps/tools-resources/risk-map/coordinated-needs-management-strategy"
+                    "accessURL": "https://www.fema.gov/disaster/coronavirus/economic/funeral-assistance"
                 }
-            ]
-        },
-        {
-            "title": "COVID-19 Funeral Assistance",
-            "description": "Provides details on total number of applications and funding dispersed by FEMA by state for Funeral Assistance related to the COVID pandemic.",
+            ],
+            "identifier": "FEMA-0321",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-05-01T10:30:19-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Response and Recovery/Response Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "COVID-19 Funeral Assistance"
         },
-            "identifier": "FEMA-0321",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Before a grant can be awarded, a state must demonstrate that total eligible costs for the declared fire meet or exceed the fire cost thresholds. This datset includes breakdown of individual and commulative thresholds by state for the year.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/disaster/coronavirus/economic/funeral-assistance"
+                    "accessURL": "https://www.fema.gov/assistance/public/fire-management-assistance/fire-cost-thresholds"
                 }
-            ]
-        },
-        {
-            "title": "Fire Cost Thresholds",
-            "description": "Before a grant can be awarded, a state must demonstrate that total eligible costs for the declared fire meet or exceed the fire cost thresholds. This datset includes breakdown of individual and commulative thresholds by state for the year.",
+            ],
+            "identifier": "FEMA-0328",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-05-01T10:30:19-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Response and Recovery/Associate Administrator"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Fire Cost Thresholds"
         },
-            "identifier": "FEMA-0328",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "The Fire Prevention and Safety (FP&S) Grants are part of the Assistance to Firefighters Grants (AFG) and support projects that enhance the safety of the public and firefighters from fire and related hazards. The primary goal is to reduce injury and prevent death among high-risk populations. In 2005, Congress reauthorized funding for FP&S and expanded the eligible uses of funds to include Firefighter Safety Research and Development.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/assistance/public/fire-management-assistance/fire-cost-thresholds"
+                    "accessURL": "https://www.fema.gov/grants/preparedness/firefighters/safety-awards"
                 }
-            ]
-        },
-        {
-            "title": "Fire Prevention And Safety",
-            "description": "The Fire Prevention and Safety (FP&S) Grants are part of the Assistance to Firefighters Grants (AFG) and support projects that enhance the safety of the public and firefighters from fire and related hazards. The primary goal is to reduce injury and prevent death among high-risk populations. In 2005, Congress reauthorized funding for FP&S and expanded the eligible uses of funds to include Firefighter Safety Research and Development.",
+            ],
+            "identifier": "FEMA-0329",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2025-01-02T13:11:38-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Grants Programs Director"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Fire Prevention And Safety"
         },
-            "identifier": "FEMA-0329",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "The Office of the Flood Insurance Advocate (OFIA) publishes its periodic report to provide the public and industry professionals an insight into trends affecting National Flood Insurance Program (NFIP) customers and property owners.rnrnData in these reports includes; Casework Highlights, Casework Trends, and Casework Spotlights",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/grants/preparedness/firefighters/safety-awards"
+                    "accessURL": "https://www.fema.gov/flood-insurance/advocate/periodic-reports"
                 }
-            ]
-        },
-        {
-            "title": "Flood Insurance Advocate Periodic Reports",
-            "description": "The Office of the Flood Insurance Advocate (OFIA) publishes its periodic report to provide the public and industry professionals an insight into trends affecting National Flood Insurance Program (NFIP) customers and property owners.rnrnData in these reports includes; Casework Highlights, Casework Trends, and Casework Spotlights",
+            ],
+            "identifier": "FEMA-0330",
             "keyword": [
                 "Communications"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-07-01T07:47:17-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Office of the Flood Insurance Advocate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Flood Insurance Advocate Periodic Reports"
         },
-            "identifier": "FEMA-0330",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "An Alerting Authority is a jurisdiction with the designated authority to alert and warn the public when there is an impending natural or human-made disaster, threat, or dangerous or missing person. Today, there are more than 1,800 federal, state, local, tribal and territorial Alerting Authorities using IPAWS to issue critical public alerts and warnings in their jurisdictions.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/flood-insurance/advocate/periodic-reports"
+                    "accessURL": "https://www.fema.gov/emergency-managers/practitioners/integrated-public-alert-warning-system/public-safety-officials/alerting-authorities/agencies-organizations"
                 }
-            ]
-        },
-        {
-            "title": "IPAWS Alerting Authorities: Agencies and Organizations",
-            "description": "An Alerting Authority is a jurisdiction with the designated authority to alert and warn the public when there is an impending natural or human-made disaster, threat, or dangerous or missing person. Today, there are more than 1,800 federal, state, local, tribal and territorial Alerting Authorities using IPAWS to issue critical public alerts and warnings in their jurisdictions.",
+            ],
+            "identifier": "FEMA-0333",
             "keyword": [
                 "Information Technology"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-07-01T07:47:17-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/National Preparedness Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "IPAWS Alerting Authorities: Agencies and Organizations"
         },
-            "identifier": "FEMA-0333",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "A Letter of Final Determination (LFD) is a letter FEMA mails to the Chief Executive Officer of a community stating that a new or updated Flood Insurance Rate Map (FIRM) or Digital Flood Insurance Rate Map (DFIRM) will become effective in six months. The letter also notifies each affected flood-prone community participating in the National Flood Insurance Program (NFIP) that it must adopt a compliant floodplain management ordinance by the map effective date to remain participants in good standing in the NFIP.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/emergency-managers/practitioners/integrated-public-alert-warning-system/public-safety-officials/alerting-authorities/agencies-organizations"
+                    "accessURL": "https://www.fema.gov/flood-maps/change-your-flood-zone/letter-final-determination"
                 }
-            ]
-        },
-        {
-            "title": "Letter of Final Determination",
-            "description": "A Letter of Final Determination (LFD) is a letter FEMA mails to the Chief Executive Officer of a community stating that a new or updated Flood Insurance Rate Map (FIRM) or Digital Flood Insurance Rate Map (DFIRM) will become effective in six months. The letter also notifies each affected flood-prone community participating in the National Flood Insurance Program (NFIP) that it must adopt a compliant floodplain management ordinance by the map effective date to remain participants in good standing in the NFIP.",
+            ],
+            "identifier": "FEMA-0335",
             "keyword": [
                 "Communications"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-09-09T07:52:37-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Risk Management Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Letter of Final Determination"
         },
-            "identifier": "FEMA-0335",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "The national-level referral list provides a listing of government and non-government disaster recovery services in the following categories:rnAccess & DisabilityrnEnvironmentrnMissing PersonsrnAging ServicesrnEssential NeedsrnRoadside AssistancernAgricultural AidrnFamily & Protective ServicesrnSocial SecurityrnAmerican Red CrossrnFinancial AssistancernStudentsrnAnimals/PetsrnFraudrnTax PreparationrnCitizenshiprnHealth Care ServicesrnTreasury ServicesrnConsumer ServicesrnHousingrnUnited States Postal ServicernContractorsrnIdentity TheftrnVeterans ServicesrnCrisis CounselingrnInsurancernVital StatisticsrnDisaster Unemployment AssistancernLegal ServicesrnVolunteer",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/flood-maps/change-your-flood-zone/letter-final-determination"
+                    "accessURL": "https://www.fema.gov/assistance/individual/disaster-survivors/national-referral-list"
                 }
-            ]
-        },
-        {
-            "title": "National Referral List",
-            "description": "The national-level referral list provides a listing of government and non-government disaster recovery services in the following categories:rnAccess & DisabilityrnEnvironmentrnMissing PersonsrnAging ServicesrnEssential NeedsrnRoadside AssistancernAgricultural AidrnFamily & Protective ServicesrnSocial SecurityrnAmerican Red CrossrnFinancial AssistancernStudentsrnAnimals/PetsrnFraudrnTax PreparationrnCitizenshiprnHealth Care ServicesrnTreasury ServicesrnConsumer ServicesrnHousingrnUnited States Postal ServicernContractorsrnIdentity TheftrnVeterans ServicesrnCrisis CounselingrnInsurancernVital StatisticsrnDisaster Unemployment AssistancernLegal ServicesrnVolunteer",
+            ],
+            "identifier": "FEMA-0342",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2025-01-02T13:11:38-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Response and Recovery/Associate Administrator"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "National Referral List"
         },
-            "identifier": "FEMA-0342",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Provides a list of supplemental National Qualification System (NQS) documents pertaining to National Incident Management System (NIMS).rnrnSupportingin Documentation includes:rnrnThe NIMS Guideline for the National Qualification System (NQS), which describes the components of a qualification and certification system, defines a process for certifying the qualifications of incident personnel, describes how to stand up and implement a peer review process, and provides an introduction to the process of credentialing personnel.rnrnTwo NIMS NQS Supplemental Guides that provide processes, procedures, and tools to assist authorities having jurisdiction develop and maintain their qualification, certification, and credentialing programs.rnrnThe NIMS Guideline for Mutual Aid, which provides an overview of common mutual aid practices; defines common terminology and processes; and describes an approach for creating legal agreements and operational plans.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/assistance/individual/disaster-survivors/national-referral-list"
+                    "accessURL": "https://www.fema.gov/emergency-managers/nims/components/nqs-supplemental-documents"
                 }
-            ]
-        },
-        {
-            "title": "National Qualification System Supplemental Documents",
-            "description": "Provides a list of supplemental National Qualification System (NQS) documents pertaining to National Incident Management System (NIMS).rnrnSupportingin Documentation includes:rnrnThe NIMS Guideline for the National Qualification System (NQS), which describes the components of a qualification and certification system, defines a process for certifying the qualifications of incident personnel, describes how to stand up and implement a peer review process, and provides an introduction to the process of credentialing personnel.rnrnTwo NIMS NQS Supplemental Guides that provide processes, procedures, and tools to assist authorities having jurisdiction develop and maintain their qualification, certification, and credentialing programs.rnrnThe NIMS Guideline for Mutual Aid, which provides an overview of common mutual aid practices; defines common terminology and processes; and describes an approach for creating legal agreements and operational plans.",
+            ],
+            "identifier": "FEMA-0343",
             "keyword": [
                 "Authorities"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2025-01-02T13:11:38-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/National Preparedness Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "National Qualification System Supplemental Documents"
         },
-            "identifier": "FEMA-0343",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "This collection contains a set of NQS Job Titles/Position Qualifications, which define minimum qualifications criteria for personnel serving in defined incident management and support positions.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/emergency-managers/nims/components/nqs-supplemental-documents"
+                    "accessURL": "https://www.fema.gov/emergency-managers/nims/components/positions"
                 }
-            ]
-        },
-        {
-            "title": "National Qualification System Job Titles and Position Qualifications",
-            "description": "This collection contains a set of NQS Job Titles/Position Qualifications, which define minimum qualifications criteria for personnel serving in defined incident management and support positions.",
+            ],
+            "identifier": "FEMA-0344",
             "keyword": [
                 "Authorities"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-07-01T07:47:17-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/National Preparedness Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "National Qualification System Job Titles and Position Qualifications"
         },
-            "identifier": "FEMA-0344",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "This collection contains a set of NQS Position Task Books (PTBs), which identify the competencies, behaviors, and tasks that personnel should demonstrate to become qualified for a defined incident management and support position.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/emergency-managers/nims/components/positions"
+                    "accessURL": "https://www.fema.gov/emergency-managers/nims/components/position-task-books"
                 }
-            ]
-        },
-        {
-            "title": "National Qualification System Position Task Books",
-            "description": "This collection contains a set of NQS Position Task Books (PTBs), which identify the competencies, behaviors, and tasks that personnel should demonstrate to become qualified for a defined incident management and support position.",
+            ],
+            "identifier": "FEMA-0345",
             "keyword": [
                 "Authorities"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-07-01T07:47:17-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/National Preparedness Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "National Qualification System Position Task Books"
         },
-            "identifier": "FEMA-0345",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "In 2002, President George W. Bush signed the Notification and Federal Employee Anti-discrimination and Retaliation Act, Public Law 107-174, Title I, General Provisions, Section 101(1), requires each federal agency to provide written notification of the rights and protections available to federal employees, former federal employees and applicants for federal employment under federal antidiscrimination and whistleblower laws listed in the No FEAR Act. The No FEAR Act increases the accountability of federal departments and agencies for acts of discrimination or reprisal against employees.rnrnThe No FEAR Act requires that federal agencies be accountable for violations of anti-discrimination and whistleblower protection laws. To comply with Title III of the No FEAR Act, FEMA must, among other requirements, post a summary of the statistical data relating to the Equal Employment Opportunity complaints filed with the agency. This data is updated on this website quarterly.rnrnFor further information regarding the No FEAR Act regulations, refer to 5 CFR Part 724, as well as the DHS Office for Civil Rights and Civil Liberties. Additional information regarding federal antidiscrimination, whistleblower protection and retaliation laws can be found at www.eeoc.gov and www.osc.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/emergency-managers/nims/components/position-task-books"
+                    "accessURL": "https://www.fema.gov/about/organization/equal-rights/no-fear-act"
                 }
-            ]
-        },
-        {
-            "title": "No FEAR Act Data (FEMA Statistics)",
-            "description": "In 2002, President George W. Bush signed the Notification and Federal Employee Anti-discrimination and Retaliation Act, Public Law 107-174, Title I, General Provisions, Section 101(1), requires each federal agency to provide written notification of the rights and protections available to federal employees, former federal employees and applicants for federal employment under federal antidiscrimination and whistleblower laws listed in the No FEAR Act. The No FEAR Act increases the accountability of federal departments and agencies for acts of discrimination or reprisal against employees.rnrnThe No FEAR Act requires that federal agencies be accountable for violations of anti-discrimination and whistleblower protection laws. To comply with Title III of the No FEAR Act, FEMA must, among other requirements, post a summary of the statistical data relating to the Equal Employment Opportunity complaints filed with the agency. This data is updated on this website quarterly.rnrnFor further information regarding the No FEAR Act regulations, refer to 5 CFR Part 724, as well as the DHS Office for Civil Rights and Civil Liberties. Additional information regarding federal antidiscrimination, whistleblower protection and retaliation laws can be found at www.eeoc.gov and www.osc.gov.",
+            ],
+            "identifier": "FEMA-0346",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-05-01T10:30:19-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Office of Equal Rights/Business Management Unit"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "No FEAR Act Data (FEMA Statistics)"
         },
-            "identifier": "FEMA-0346",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Since 2014, FEMA has provided a monthly summary to Congress providing details on flood risk mapping milestones reached in the previous month and an estimated schedule of specific flood risk mapping activities anticipated in the next three months.rnrnThe Biggert-Waters Flood Insurance Reform Act of 2012, as revised, and the Homeowner Flood Insurance Affordability Act of 2014 direct FEMA to notify Members of Congress when constituents in their district will be affected by a flood mapping update.rnrnThrough Risk MAP, FEMA continuously releases updated flood maps and data, giving communities access to helpful, authoritative data that they can use to make decisions about flood risk.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/about/organization/equal-rights/no-fear-act"
+                    "accessURL": "https://www.fema.gov/flood-maps/guidance-reports/congress-notice"
                 }
-            ]
-        },
-        {
-            "title": "Notices to Congress",
-            "description": "Since 2014, FEMA has provided a monthly summary to Congress providing details on flood risk mapping milestones reached in the previous month and an estimated schedule of specific flood risk mapping activities anticipated in the next three months.rnrnThe Biggert-Waters Flood Insurance Reform Act of 2012, as revised, and the Homeowner Flood Insurance Affordability Act of 2014 direct FEMA to notify Members of Congress when constituents in their district will be affected by a flood mapping update.rnrnThrough Risk MAP, FEMA continuously releases updated flood maps and data, giving communities access to helpful, authoritative data that they can use to make decisions about flood risk.",
+            ],
+            "identifier": "FEMA-0347",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-05-01T10:30:19-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Federal Insurance and Mitigation Administration"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Notices to Congress"
         },
-            "identifier": "FEMA-0347",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "State- and county-wide public assistance per capita impact indicators and the minimum and maximum project cost thresholds for small projects.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/flood-maps/guidance-reports/congress-notice"
+                    "accessURL": "https://www.fema.gov/assistance/public/tools-resources/per-capita-impact-indicator"
                 }
-            ]
-        },
-        {
-            "title": "Per Capita Impact Indicator and Project Thresholds",
-            "description": "State- and county-wide public assistance per capita impact indicators and the minimum and maximum project cost thresholds for small projects.",
+            ],
+            "identifier": "FEMA-0348",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-05-01T10:30:19-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Response and Recovery/Response Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Per Capita Impact Indicator and Project Thresholds"
         },
-            "identifier": "FEMA-0348",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Preliminary Damage Assessments (PDAs) are conducted to enable FEMA \u2014 as well as state, local, tribal, and territorial partners \u2014 to determine the magnitude of damage and impact of disasters.rnrnDataset containts Preliminary Damage Assessment (PDA) Reports for Major Disaster Declaration Requests (DR) beginning with Fiscal Year 2008 (October 1, 2007).  These reports contain information gathered during the Preliminary Damage Assessment process and published here 30 days after a determination is made on a request or an appeal.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/assistance/public/tools-resources/per-capita-impact-indicator"
+                    "accessURL": "https://www.fema.gov/disaster/how-declared/preliminary-damage-assessments/reports"
                 }
-            ]
-        },
-        {
-            "title": "Preliminary Damage Assessments",
-            "description": "Preliminary Damage Assessments (PDAs) are conducted to enable FEMA \u2014 as well as state, local, tribal, and territorial partners \u2014 to determine the magnitude of damage and impact of disasters.rnrnDataset containts Preliminary Damage Assessment (PDA) Reports for Major Disaster Declaration Requests (DR) beginning with Fiscal Year 2008 (October 1, 2007).  These reports contain information gathered during the Preliminary Damage Assessment process and published here 30 days after a determination is made on a request or an appeal.",
+            ],
+            "identifier": "FEMA-0349",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2025-01-02T13:11:38-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Response and Recovery/Response Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Preliminary Damage Assessments"
         },
-            "identifier": "FEMA-0349",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "FEMA has a statutory responsibility to clearly communicate flood risk. Risk Rating 2.0 allows FEMA to provide rnindividuals and communities with information to make more informed decisions on purchasing flood insurance, rninitiating, and informing appropriate mitigation options to help lower flood insurance rates. The current rating rnmethodology has not changed since the 1970s. Over the years, technology has evolved and so has FEMA\u00e2\u20ac\u2122s rnunderstanding of flood risk. Risk Rating 2.0 allows FEMA to calculate premiums more equitably across all rnpolicyholders based on the value of their home and individual property\u00e2\u20ac\u2122s flood risk.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/disaster/how-declared/preliminary-damage-assessments/reports"
+                    "accessURL": "https://www.fema.gov/flood-insurance/risk-rating/profiles"
                 }
-            ]
-        },
-        {
-            "title": "Risk Rating 2.0 State Profiles",
-            "description": "FEMA has a statutory responsibility to clearly communicate flood risk. Risk Rating 2.0 allows FEMA to provide rnindividuals and communities with information to make more informed decisions on purchasing flood insurance, rninitiating, and informing appropriate mitigation options to help lower flood insurance rates. The current rating rnmethodology has not changed since the 1970s. Over the years, technology has evolved and so has FEMA\u00e2\u20ac\u2122s rnunderstanding of flood risk. Risk Rating 2.0 allows FEMA to calculate premiums more equitably across all rnpolicyholders based on the value of their home and individual property\u00e2\u20ac\u2122s flood risk.",
+            ],
+            "identifier": "FEMA-0358",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-05-01T10:30:19-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Federal Insurance and Mitigation Administration"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Risk Rating 2.0 State Profiles"
         },
-            "identifier": "FEMA-0358",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "The rates on this Schedule of Equipment Rates are for applicant-owned equipment in good mechanical condition, complete with all required attachments. Each rate covers all costs eligible under the Robert T. Stafford Disaster Relief and Emergency Assistance Act, 42 U.S.C. \u00a7 5121, et seq., for ownership and operation of equipment, including depreciation, overhead, all maintenance, field repairs, fuel, lubricants, tires, OSHA equipment and other costs incidental to operation. Standby equipment costs are not eligible.rnrnEquipment must be in actual operation performing eligible work in order for reimbursement to be eligible. Labor costs of the operator are not included in the rates and should be approved separately from equipment costs.rnrnInformation regarding the use of the Schedule is contained in 44 CFR \u00a7 206.228 Allowable Costs. Rates for equipment not listed will be furnished by FEMA upon request. Any appeals shall be in accordance with 44 CFR \u00a7 206.206 Appeals.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/flood-insurance/risk-rating/profiles"
+                    "accessURL": "https://www.fema.gov/assistance/public/tools-resources/schedule-equipment-rates"
                 }
-            ]
-        },
-        {
-            "title": "Schedule of Equipment Rates",
-            "description": "The rates on this Schedule of Equipment Rates are for applicant-owned equipment in good mechanical condition, complete with all required attachments. Each rate covers all costs eligible under the Robert T. Stafford Disaster Relief and Emergency Assistance Act, 42 U.S.C. \u00a7 5121, et seq., for ownership and operation of equipment, including depreciation, overhead, all maintenance, field repairs, fuel, lubricants, tires, OSHA equipment and other costs incidental to operation. Standby equipment costs are not eligible.rnrnEquipment must be in actual operation performing eligible work in order for reimbursement to be eligible. Labor costs of the operator are not included in the rates and should be approved separately from equipment costs.rnrnInformation regarding the use of the Schedule is contained in 44 CFR \u00a7 206.228 Allowable Costs. Rates for equipment not listed will be furnished by FEMA upon request. Any appeals shall be in accordance with 44 CFR \u00a7 206.206 Appeals.",
+            ],
+            "identifier": "FEMA-0359",
             "keyword": [
                 "Authorities"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2025-01-02T13:11:38-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Response and Recovery/Response Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Schedule of Equipment Rates"
         },
-            "identifier": "FEMA-0359",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "The Staffing for Adequate Fire and Emergency Response Grants (SAFER) was created to provide funding directly to fire departments and volunteer firefighter interest organizations to help them increase or maintain the number of trained, front line firefighters available in their communities.rnrnThe goal of SAFER is to enhance the local fire departments' abilities to comply with staffing, response and operational standards established by the NFPA (NFPA 1710 and/or NFPA 1720).rnrnThis dataset includes information on grant recipients including; organization name, state, program, award amount and award date.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/assistance/public/tools-resources/schedule-equipment-rates"
+                    "accessURL": "https://www.fema.gov/grants/preparedness/firefighters/safer"
                 }
-            ]
-        },
-        {
-            "title": "Staffing For Adequate Fire And Emergency Response (SAFER) Grant Recipients",
-            "description": "The Staffing for Adequate Fire and Emergency Response Grants (SAFER) was created to provide funding directly to fire departments and volunteer firefighter interest organizations to help them increase or maintain the number of trained, front line firefighters available in their communities.rnrnThe goal of SAFER is to enhance the local fire departments' abilities to comply with staffing, response and operational standards established by the NFPA (NFPA 1710 and/or NFPA 1720).rnrnThis dataset includes information on grant recipients including; organization name, state, program, award amount and award date.",
+            ],
+            "identifier": "FEMA-0360",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2025-01-02T13:11:38-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Grants Programs Director"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Staffing For Adequate Fire And Emergency Response (SAFER) Grant Recipients"
         },
-            "identifier": "FEMA-0360",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Provides details on local and state resources available for disaster assitance. Information is grouped by state, and includes details such as category of resource support, the name of the entity providing the assistance, the type of assistance provided, and the telephone number.rnrnAreas of support include:rnrnAccess & DisabilitiesrnAging ServicesrnAgricultural AidrnAnimals/PetsrnCitizenshiprnConsumer ServicesrnContractorsrnCrisis CounselingrnDisaster UnemploymentrnEnvironmentrnEssential NeedsrnFamily & Protective ServicesrnFinancial AssistancernHealth Care ServicesrnHousingrnIdentity TheftrnInsurancernLegal ServicesrnRoadside AssistancernStudentsrnTax PreparationrnVeterans ServicesrnVital StatisticsrnVolunteer",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/grants/preparedness/firefighters/safer"
+                    "accessURL": "https://www.fema.gov/assistance/individual/disaster-survivors/state-local-referral-lists"
                 }
-            ]
-        },
-        {
-            "title": "State & Local Level Referral Lists",
-            "description": "Provides details on local and state resources available for disaster assitance. Information is grouped by state, and includes details such as category of resource support, the name of the entity providing the assistance, the type of assistance provided, and the telephone number.rnrnAreas of support include:rnrnAccess & DisabilitiesrnAging ServicesrnAgricultural AidrnAnimals/PetsrnCitizenshiprnConsumer ServicesrnContractorsrnCrisis CounselingrnDisaster UnemploymentrnEnvironmentrnEssential NeedsrnFamily & Protective ServicesrnFinancial AssistancernHealth Care ServicesrnHousingrnIdentity TheftrnInsurancernLegal ServicesrnRoadside AssistancernStudentsrnTax PreparationrnVeterans ServicesrnVital StatisticsrnVolunteer",
+            ],
+            "identifier": "FEMA-0361",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2025-01-02T13:11:38-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Response and Recovery/Response Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "State & Local Level Referral Lists"
         },
-            "identifier": "FEMA-0361",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Provides information on participating reinsurance copanies by year as part of the National Flood Insurance Program (NFIP).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/assistance/individual/disaster-survivors/state-local-referral-lists"
+                    "accessURL": "https://www.fema.gov/flood-insurance/work-with-nfip/reinsurance/traditional"
                 }
-            ]
-        },
-        {
-            "title": "Traditional Reinsurance Details",
-            "description": "Provides information on participating reinsurance copanies by year as part of the National Flood Insurance Program (NFIP).",
+            ],
+            "identifier": "FEMA-0363",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-05-01T10:30:19-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Federal Insurance and Mitigation Administration"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Traditional Reinsurance Details"
         },
-            "identifier": "FEMA-0363",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Public engagement files for the public",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/flood-insurance/work-with-nfip/reinsurance/traditional"
+                    "accessURL": "https://fema.gov"
                 }
-            ]
-        },
-        {
-            "title": "Public Engagement",
-            "description": "Public engagement files for the public",
+            ],
+            "identifier": "FEMA-0172",
             "keyword": [
                 "Threats and Hazards"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-08-01T07:58:54-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Risk Management Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Public Engagement"
         },
-            "identifier": "FEMA-0172",
+        {
             "accessLevel": "public",
             "bureauCode": [
-                "024:070"
-            ],
-            "programCode": [
-                "024:000"
+                "024:010"
             ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://fema.gov"
-                }
-            ]
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Human Resources Services Center Employee Performance Management (EPM) ",
             "description": "OCHCO custom built performance management instance within the ServiceNow Service Automation Government Cloud Suite (SNOW SAGC)",
+            "identifier": "MGMT-OCHCO-SNOW-Employee_Performance_Management",
             "keyword": [
                 "Performance Management",
                 "ServiceNow Service Automation Government Cloud Suite"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-06-25T14:24:49-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Human Resources Services Center Employee Performance Management (EPM) "
         },
-            "identifier": "MGMT-OCHCO-SNOW-Employee_Performance_Management",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "HQ Online Learning Management and Education System (HOLMES).",
             "description": "OCHCO built Learning Management System (LMS) instance within the ServiceNow Service Automation Government Cloud Suite (SNOW SAGC).",
+            "identifier": "MGMT-OCHCO-SNOW-HOLMES",
             "keyword": [
                 "Learning",
                 "Training",
                 "Development"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-08-19T14:18:21-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "HQ Online Learning Management and Education System (HOLMES)."
         },
-            "identifier": "MGMT-OCHCO-SNOW-HOLMES",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Human Resources Services Center Knowledge Management Catalogs ",
             "description": "This is an OCHCO Knowledge Management instance within the ServiceNow Service Automation Government Cloud Suite (SNOW SAGC) that leverage HR Services Center as a Digital Front door to HR Self Service and provides knowledge management self-service functionality.  ",
+            "identifier": "MGMT-OCHCO-SNOW-Knowledge_Management",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-05-21T10:22:24-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Human Resources Services Center Knowledge Management Catalogs "
         },
-            "identifier": "MGMT-OCHCO-SNOW-Knowledge_Management",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Human Resources Services Center to submit requests for Awards, HRIT Services, Teleworking & Remote Agreements, Employee Relations, Pay & Incentives and Workforce Administration. ",
             "description": "This is an OCHCO custom-built HR Service Center instance within the ServiceNow Service Automation Government Cloud Suite (SNOW SAGC) that provides functionality to submit requests for Awards, HRIT Services, Teleworking & Remote Agreements, Employee Relations, Pay & Incentives and Workforce Administrative tasks. Capabilities include Employee Performance Management, Telework/Remote Work Agreements, HRMS Pay and Incentive Flexibilities, tEmployee Relations Consultation. n",
+            "identifier": "MGMT-OCHCO-SNOW-HRSC",
             "keyword": [
                 "DHS OCHCO",
                 "Human Resources Service Center",
                 "HR",
                 "ServiceNow"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-12-18T09:58:57-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Human Resources Services Center to submit requests for Awards, HRIT Services, Teleworking & Remote Agreements, Employee Relations, Pay & Incentives and Workforce Administration. "
         },
-            "identifier": "MGMT-OCHCO-SNOW-HRSC",
+        {
             "accessLevel": "public",
             "bureauCode": [
-                "024:010"
-            ],
-            "programCode": [
-                "024:000"
+                "024:070"
             ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "NFIP Community Layer No Overlaps Whole",
             "description": "This dataset is flattened and multicounty communities are unsplit by county lines. Flattened means that there are no overlaps; larger shapes like counties are punched out or clipped where smaller communities are contained within them. This allows for choropleth shading and other mapping techniques such as calculating unincorporated county land area.  Multicounty cities like Houston are a single feature, undivided by counties.  This layer is derived from Census, State of Maine, and National Flood Hazard Layer political boundaries.rnrnThe Community Layer datasets contain geospatial community boundaries associated with Census and NFIP data. The dataset does not contain personal identifiable information (PII). The Community Layer can be used to tie Community ID numbers (CID) to jurisdiction, tribal, and special land use area boundaries.rnrnA geodatabase (GDB) link is Included in the Full Data section below. The compressed file contains a collection of files that can store, query, and manage both spatial and nonspatial data using software that can read such a file. It bcontains all of the community layers/b, not just the layer for which this dataset page describes. rnThis layer can also be accessed from the FEMA ArcGIS viewer online: https://fema.maps.arcgis.com/home/item.html?id=8dcf28fc5b97404bbd9d1bc6d3c9b3cfrnrnrnCitation: FEMA's citation requirements for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page, Citing Data section: https://www.fema.gov/about/openfema/terms-conditions.rnrnFor answers to Frequently Asked Questions (FAQs) about the OpenFEMA program, API, and publicly available datasets, please visit: https://www.fema.gov/about/openfema/faq.rnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.fema.gov/api/open/v1/NfipCommunityLayerNoOverlapsWhole"
+                }
+            ],
+            "identifier": "FEMA-0594",
             "keyword": [
                 "Threats and Hazards"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-10-02T14:25:02-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Federal Insurance Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NFIP Community Layer No Overlaps Whole"
         },
-            "identifier": "FEMA-0594",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "This dataset is flattened and multicounty communities are split by county lines. Flattened means that there are no overlaps; larger shapes like counties are punched out or clipped where smaller communities are contained within them. This allows for choropleth shading and other mapping techniques such as calculating unincorporated county land area. Multicounty cities like Houston are split by county lines, allowing easier county summarization and alignment with certain NFIP statistics.  This layer is derived from Census, State of Maine, and National Flood Hazard Layer political boundaries.rnrnThe Community Layer datasets contain geospatial community boundaries associated with Census and NFIP data. The dataset does not contain personal identifiable information (PII). The Community Layer can be used to tie Community ID numbers (CID) to jurisdiction, tribal, and special land use area boundaries.rnrnA geodatabase (GDB) link is Included in the Full Data section below. The compressed file contains a collection of files that can store, query, and manage both spatial and nonspatial data using software that can read such a file. It bcontains all of the community layers/b, not just the layer for which this dataset page describes. rnrnCitation: FEMA's citation requirements for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page, Citing Data section: https://www.fema.gov/about/openfema/terms-conditions.rnrnFor answers to Frequently Asked Questions (FAQs) about the OpenFEMA program, API, and publicly available datasets, please visit: https://www.fema.gov/about/openfema/faq.rnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v1/NfipCommunityLayerNoOverlapsWhole"
+                    "accessURL": "https://www.fema.gov/api/open/v1/NfipCommunityLayerNoOverlapsSplit"
                 }
-            ]
-        },
-        {
-            "title": "NFIP Community Layer No Overlaps Split",
-            "description": "This dataset is flattened and multicounty communities are split by county lines. Flattened means that there are no overlaps; larger shapes like counties are punched out or clipped where smaller communities are contained within them. This allows for choropleth shading and other mapping techniques such as calculating unincorporated county land area. Multicounty cities like Houston are split by county lines, allowing easier county summarization and alignment with certain NFIP statistics.  This layer is derived from Census, State of Maine, and National Flood Hazard Layer political boundaries.rnrnThe Community Layer datasets contain geospatial community boundaries associated with Census and NFIP data. The dataset does not contain personal identifiable information (PII). The Community Layer can be used to tie Community ID numbers (CID) to jurisdiction, tribal, and special land use area boundaries.rnrnA geodatabase (GDB) link is Included in the Full Data section below. The compressed file contains a collection of files that can store, query, and manage both spatial and nonspatial data using software that can read such a file. It bcontains all of the community layers/b, not just the layer for which this dataset page describes. rnrnCitation: FEMA's citation requirements for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page, Citing Data section: https://www.fema.gov/about/openfema/terms-conditions.rnrnFor answers to Frequently Asked Questions (FAQs) about the OpenFEMA program, API, and publicly available datasets, please visit: https://www.fema.gov/about/openfema/faq.rnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0595",
             "keyword": [
                 "Threats and Hazards"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-10-02T14:25:02-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Federal Insurance Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NFIP Community Layer No Overlaps Split"
         },
-            "identifier": "FEMA-0595",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "This dataset contains data on Public Assistance project awards (obligations), including the project obligation date(s); dollar amount of Federal Share Obligated for each project and its obligation date(s); FEMA Region; State; Disaster Declaration Number; descriptive cause of the declaration (Incident Type); Entity requesting public assistance (Applicant Name); and distinct name for the repair, replacement or mitigation work listed for assistance (Project Title).  rnrnAs part of disaster declarations, the President can make federal funding (Public Assistance) available through FEMA to eligible state, local and tribal governments and certain private nonprofit organizations. This is done on a cost-sharing basis for emergency work and the repair, replacement, or mitigation work for facilities damaged by the disaster event. rnrnAs part of Congressional bill HR 152 - the Sandy Recovery Improvement Act of 2013, FEMA is providing the following information for our stakeholders: Region, Disaster Declaration Number, Disaster Type, State, Applicant, County, Damage Category Code, Federal Share Obligated, and Date Obligated.rnrnNote: FEMA obligates funding for a project directly to the Recipient (State or Tribe). It is the Recipient's responsibility to ensure that the eligible subrecipient (listed in the dataset as Applicant Name) receives the award funding.rnrnThis dataset lists details about project versions (occurring when the scope/cost changes for a project). Versions adjust the cost of the project  with positive additions called obligations and subtractions called deobligations. Combined, they reconcile to reflect the Total Federal Share Obligation, but reconciliation occurs over the life of the project - sometimes years after the declaration date. The dataset represents project obligations within a seven-day period prior to the listed date but does not include obligations uploaded on the same day as the publication. Open projects still under pre-obligation processing are not represented. For more information on the Public Assistance process see: https://www.fema.gov/assistance/public/processrnrnThis is raw, unedited data from FEMA's Emergency Management Mission Integrated Environment (EMMIE) system and as such is subject to a small percentage of human error. The financial information is derived from EMMIE and not FEMA's official financial systems. Due to differences in reporting periods, status of obligations and how business rules are applied, this financial information may differ slightly from official publication on public websites such as usaspending.gov. This dataset is not intended to be used for any official federal financial reporting.rnrnFEMA's terms and conditions and citation requirements for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page: https://www.fema.gov/about/openfema/terms-conditionsrnrnFor answers to Frequently Asked Questions (FAQs) about the OpenFEMA program, API, and publicly available datasets, please visit: https://www.fema.gov/about/openfema/faqrnrnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v1/NfipCommunityLayerNoOverlapsSplit"
+                    "accessURL": "https://www.fema.gov/api/open/v1/PublicAssistanceGrantAwardActivities"
                 }
-            ]
-        },
-        {
-            "title": "Public Assistance Grant Award Activities",
-            "description": "This dataset contains data on Public Assistance project awards (obligations), including the project obligation date(s); dollar amount of Federal Share Obligated for each project and its obligation date(s); FEMA Region; State; Disaster Declaration Number; descriptive cause of the declaration (Incident Type); Entity requesting public assistance (Applicant Name); and distinct name for the repair, replacement or mitigation work listed for assistance (Project Title).  rnrnAs part of disaster declarations, the President can make federal funding (Public Assistance) available through FEMA to eligible state, local and tribal governments and certain private nonprofit organizations. This is done on a cost-sharing basis for emergency work and the repair, replacement, or mitigation work for facilities damaged by the disaster event. rnrnAs part of Congressional bill HR 152 - the Sandy Recovery Improvement Act of 2013, FEMA is providing the following information for our stakeholders: Region, Disaster Declaration Number, Disaster Type, State, Applicant, County, Damage Category Code, Federal Share Obligated, and Date Obligated.rnrnNote: FEMA obligates funding for a project directly to the Recipient (State or Tribe). It is the Recipient's responsibility to ensure that the eligible subrecipient (listed in the dataset as Applicant Name) receives the award funding.rnrnThis dataset lists details about project versions (occurring when the scope/cost changes for a project). Versions adjust the cost of the project  with positive additions called obligations and subtractions called deobligations. Combined, they reconcile to reflect the Total Federal Share Obligation, but reconciliation occurs over the life of the project - sometimes years after the declaration date. The dataset represents project obligations within a seven-day period prior to the listed date but does not include obligations uploaded on the same day as the publication. Open projects still under pre-obligation processing are not represented. For more information on the Public Assistance process see: https://www.fema.gov/assistance/public/processrnrnThis is raw, unedited data from FEMA's Emergency Management Mission Integrated Environment (EMMIE) system and as such is subject to a small percentage of human error. The financial information is derived from EMMIE and not FEMA's official financial systems. Due to differences in reporting periods, status of obligations and how business rules are applied, this financial information may differ slightly from official publication on public websites such as usaspending.gov. This dataset is not intended to be used for any official federal financial reporting.rnrnFEMA's terms and conditions and citation requirements for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page: https://www.fema.gov/about/openfema/terms-conditionsrnrnFor answers to Frequently Asked Questions (FAQs) about the OpenFEMA program, API, and publicly available datasets, please visit: https://www.fema.gov/about/openfema/faqrnrnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0601",
             "keyword": [
                 "Finance"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-10-02T14:25:02-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Response and Recovery/Recovery Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Public Assistance Grant Award Activities"
         },
-            "identifier": "FEMA-0601",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "This dataset provides information on structures that have had multiple National Flood Insurance (NFIP) claims across the history of the program. The data contains NFIP-insured structures that fall within the four categories of Repetitive Loss and Severe Repetitive Loss that FEMA tracks. Definitions of these categories are provided in the field descriptions. There are also fields to show whether a structure is currently NFIP-insured, has been mitigated, and other characteristics. The data includes properties that have since been mitigated or demolished and may no longer considered to be in any of the listed categories.rnLocation information has been redacted to protect personal privacy. Location information is derived from reported address, geocoding of that address, and reported NFIP community. Because NFIP insurance claims data spans the history of the NFIP, many of the structures have poor address information resulting in poor or missing coordinates and additional location fields that rely on those coordinates. An effort has been made to fill in missing data and resolve conflicts between state, county, community, and census block group. Because of this effort, emstatistics derived from this data may differ from those reported elsewhere by FEMA or others/em.rnThere is a lot of interest in this data as it touches many program areas of the NFIP and serves as an indicator of flood risk and mitigation need.rnrnFEMA's terms and conditions and citation requirements for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page: https://www.fema.gov/about/openfema/terms-conditions.rnrnFor answers to Frequently Asked Questions (FAQs) about the OpenFEMA program, API, and publicly available datasets, please visit: https://www.fema.gov/about/openfema/faq.rnrnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v1/PublicAssistanceGrantAwardActivities"
+                    "accessURL": "https://www.fema.gov/api/open/v1/NfipMultipleLossProperties"
                 }
-            ]
-        },
-        {
-            "title": "NFIP Multiple Loss Properties",
-            "description": "This dataset provides information on structures that have had multiple National Flood Insurance (NFIP) claims across the history of the program. The data contains NFIP-insured structures that fall within the four categories of Repetitive Loss and Severe Repetitive Loss that FEMA tracks. Definitions of these categories are provided in the field descriptions. There are also fields to show whether a structure is currently NFIP-insured, has been mitigated, and other characteristics. The data includes properties that have since been mitigated or demolished and may no longer considered to be in any of the listed categories.rnLocation information has been redacted to protect personal privacy. Location information is derived from reported address, geocoding of that address, and reported NFIP community. Because NFIP insurance claims data spans the history of the NFIP, many of the structures have poor address information resulting in poor or missing coordinates and additional location fields that rely on those coordinates. An effort has been made to fill in missing data and resolve conflicts between state, county, community, and census block group. Because of this effort, emstatistics derived from this data may differ from those reported elsewhere by FEMA or others/em.rnThere is a lot of interest in this data as it touches many program areas of the NFIP and serves as an indicator of flood risk and mitigation need.rnrnFEMA's terms and conditions and citation requirements for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page: https://www.fema.gov/about/openfema/terms-conditions.rnrnFor answers to Frequently Asked Questions (FAQs) about the OpenFEMA program, API, and publicly available datasets, please visit: https://www.fema.gov/about/openfema/faq.rnrnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0596",
             "keyword": [
                 "Threats and Hazards"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-10-02T14:25:02-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Federal Insurance Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NFIP Multiple Loss Properties"
         },
-            "identifier": "FEMA-0596",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "This dataset contains EMPG recipients as reported by their State and a summary of rnthe funded program support as reported by the Recipient in the GRT.rnrnThe EMPG Program provides resources to assist state, local, tribal and territorial governments in preparing for all hazards, as authorized by Section 662 of the Post Katrina Emergency Management Reform Act (6 U.S.C \u00a7 762) and the Robert T. Stafford Disaster Relief and Emergency Assistance Act, as amended (42 U.S.C. \u00a7\u00a7 5121 et seq.). Title VI of the Stafford Act authorizes FEMA to make grants for the purpose of providing a system of emergency preparedness for the protection of life and property in the United States from hazards, and to vest responsibility for emergency preparedness jointly in the federal government and the states and their political subdivisions. The EMPG, from FY 2016 to the present FY,provides federal funds to assist state, local, tribal and territorial emergency management agencies to obtain the resources required to support the National Preparedness Goal's (NPG's) associated mission areas and core capabilities. The Federal Government, through the EMPG Program, provides necessary direction, coordination, and guidance, and provides necessary assistance, as authorized in this title to support a comprehensive all hazards emergency preparedness system. rnrnThe EMPG is to support a comprehensive, all-hazard emergency preparedness system by building and sustaining the core capabilities contained in the NPG\u2019s. Examples include: rnrn\u2022 Completing the Threat and Hazard Identification and Risk Assessment (THIRA)process.rn\u2022 Strengthening a state or community's emergency management governance structure.rn\u2022 Updating and approving specific emergency plans.rn\u2022 Designing and conducting exercises that enable whole community stakeholders to examine and validate core capabilities and the plans needed to deliver them to the targets identified through the THIRA.rn\u2022 Targeting training and verifying identified capabilities.rn\u2022 Initiating or achieving a whole community approach to security and emergency management. rnrnThis dataset was first made public on 10/31/2016 and will be updated twice a year. rnrnFor additional details on the EMPG program visit: https://www.fema.gov/grants/preparedness/emergency-management-performance.rnrnThis dataset is not intended to be an official federal report, and should not be considered an official federal report. rn rnCitation: The Agency\u2019s preferred citation for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page, Citing Data section: https://www.fema.gov/about/openfema/terms-conditions.rnrnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v1/NfipMultipleLossProperties"
+                    "accessURL": "https://www.fema.gov/api/open/v2/EmergencyManagementPerformanceGrants"
                 }
-            ]
-        },
-        {
-            "title": "Emergency Management Performance Grants",
-            "description": "This dataset contains EMPG recipients as reported by their State and a summary of rnthe funded program support as reported by the Recipient in the GRT.rnrnThe EMPG Program provides resources to assist state, local, tribal and territorial governments in preparing for all hazards, as authorized by Section 662 of the Post Katrina Emergency Management Reform Act (6 U.S.C \u00a7 762) and the Robert T. Stafford Disaster Relief and Emergency Assistance Act, as amended (42 U.S.C. \u00a7\u00a7 5121 et seq.). Title VI of the Stafford Act authorizes FEMA to make grants for the purpose of providing a system of emergency preparedness for the protection of life and property in the United States from hazards, and to vest responsibility for emergency preparedness jointly in the federal government and the states and their political subdivisions. The EMPG, from FY 2016 to the present FY,provides federal funds to assist state, local, tribal and territorial emergency management agencies to obtain the resources required to support the National Preparedness Goal's (NPG's) associated mission areas and core capabilities. The Federal Government, through the EMPG Program, provides necessary direction, coordination, and guidance, and provides necessary assistance, as authorized in this title to support a comprehensive all hazards emergency preparedness system. rnrnThe EMPG is to support a comprehensive, all-hazard emergency preparedness system by building and sustaining the core capabilities contained in the NPG\u2019s. Examples include: rnrn\u2022 Completing the Threat and Hazard Identification and Risk Assessment (THIRA)process.rn\u2022 Strengthening a state or community's emergency management governance structure.rn\u2022 Updating and approving specific emergency plans.rn\u2022 Designing and conducting exercises that enable whole community stakeholders to examine and validate core capabilities and the plans needed to deliver them to the targets identified through the THIRA.rn\u2022 Targeting training and verifying identified capabilities.rn\u2022 Initiating or achieving a whole community approach to security and emergency management. rnrnThis dataset was first made public on 10/31/2016 and will be updated twice a year. rnrnFor additional details on the EMPG program visit: https://www.fema.gov/grants/preparedness/emergency-management-performance.rnrnThis dataset is not intended to be an official federal report, and should not be considered an official federal report. rn rnCitation: The Agency\u2019s preferred citation for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page, Citing Data section: https://www.fema.gov/about/openfema/terms-conditions.rnrnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0597",
             "keyword": [
                 "Finance"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-10-02T14:25:02-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/National Preparedness Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Emergency Management Performance Grants"
         },
-            "identifier": "FEMA-0597",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "This dataset contains the Project Site Inventories from the Hazard Mitigation Assistance (HMA) subapplications/subgrants from the FEMA Grants Outcomes (FEMA GO) system (FEMA\u2019s new grants management system). FEMA GO started accepting Flood Mitigation Assistance (FMA) and Building Resilient Infrastructure and Communities (BRIC) subapplications in Fiscal Year 2020. FEMA GO is projected to support the Hazard Mitigation Grant Program (HMGP) in Calendar Year 2023. For details on HMA Project Site Inventories not captured in FEMA GO, visit https://www.fema.gov/openfema-data-page/hazard-mitigation-assistance-mitigated-properties-v3.rnrnThis dataset contains information on the Project Site Inventories identified in the HMA subapplications/subgrants that have been submitted to or awarded in FEMA GO, as well as amendments made to the awarded subgrants. The Project Site Inventory contains information regarding the Building, Infrastructure/Utility/other, and/or Vacant Land proposed to be mitigated by the subapplication/subgrant. Sensitive information, such as Personally Identifiable Information (PII), has been removed to protect privacy. The information in this dataset has been deemed appropriate for publication to empower public knowledge of mitigation activities and the nature of HMA grant programs. For more information on the HMA grant programs, visit: https://www.fema.gov/grants/mitigation. For more information on FEMA GO, visit: https://www.fema.gov/grants/guidance-tools/fema-go.rnrnThis dataset comes from the source system mentioned above and is subject to a small percentage of human error. In some cases, data was not provided by the subapplicant, applicant, and/or entered into FEMA GO. Due to the voluntary nature of the Hazard Mitigation Assistance Programs, not all Project Site Inventory in this dataset will be mitigated. As FEMA GO continues development, additional fields may be added to this dataset to indicate the final status of individual inventory. This dataset is not intended to be used for any official federal financial reporting.rnFEMA's terms and conditions and citation requirements for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page: https://www.fema.gov/about/openfema/terms-conditions.rnrnFor answers to Frequently Asked Questions (FAQs) about the OpenFEMA program, API, and publicly available datasets, please visit: https://www.fema.gov/about/openfema/faq.rnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v2/EmergencyManagementPerformanceGrants"
+                    "accessURL": "https://www.fema.gov/api/open/v1/HmaSubapplicationsProjectSiteInventories"
                 }
-            ]
-        },
-        {
-            "title": "HMA Subapplications Project Site Inventories",
-            "description": "This dataset contains the Project Site Inventories from the Hazard Mitigation Assistance (HMA) subapplications/subgrants from the FEMA Grants Outcomes (FEMA GO) system (FEMA\u2019s new grants management system). FEMA GO started accepting Flood Mitigation Assistance (FMA) and Building Resilient Infrastructure and Communities (BRIC) subapplications in Fiscal Year 2020. FEMA GO is projected to support the Hazard Mitigation Grant Program (HMGP) in Calendar Year 2023. For details on HMA Project Site Inventories not captured in FEMA GO, visit https://www.fema.gov/openfema-data-page/hazard-mitigation-assistance-mitigated-properties-v3.rnrnThis dataset contains information on the Project Site Inventories identified in the HMA subapplications/subgrants that have been submitted to or awarded in FEMA GO, as well as amendments made to the awarded subgrants. The Project Site Inventory contains information regarding the Building, Infrastructure/Utility/other, and/or Vacant Land proposed to be mitigated by the subapplication/subgrant. Sensitive information, such as Personally Identifiable Information (PII), has been removed to protect privacy. The information in this dataset has been deemed appropriate for publication to empower public knowledge of mitigation activities and the nature of HMA grant programs. For more information on the HMA grant programs, visit: https://www.fema.gov/grants/mitigation. For more information on FEMA GO, visit: https://www.fema.gov/grants/guidance-tools/fema-go.rnrnThis dataset comes from the source system mentioned above and is subject to a small percentage of human error. In some cases, data was not provided by the subapplicant, applicant, and/or entered into FEMA GO. Due to the voluntary nature of the Hazard Mitigation Assistance Programs, not all Project Site Inventory in this dataset will be mitigated. As FEMA GO continues development, additional fields may be added to this dataset to indicate the final status of individual inventory. This dataset is not intended to be used for any official federal financial reporting.rnFEMA's terms and conditions and citation requirements for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page: https://www.fema.gov/about/openfema/terms-conditions.rnrnFor answers to Frequently Asked Questions (FAQs) about the OpenFEMA program, API, and publicly available datasets, please visit: https://www.fema.gov/about/openfema/faq.rnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0600",
             "keyword": [
                 "Threats and Hazards"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-10-02T14:25:02-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Federal Insurance Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "HMA Subapplications Project Site Inventories"
         },
-            "identifier": "FEMA-0600",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "This dataset contains the communities identified in the Hazard Mitigation Assistance (HMA) subapplications/subgrants from the FEMA Grants Outcomes (FEMA GO) system (FEMA\u2019s new grants management system). FEMA GO started accepting Flood Mitigation Assistance (FMA) and Building Resilient Infrastructure and Communities (BRIC) subapplications in Fiscal Year 2020. FEMA GO is projected to support the Hazard Mitigation Grant Program (HMGP) in Calendar Year 2023. For details on HMA communities not captured in FEMA GO, visit https://www.fema.gov/openfema-data-page/hazard-mitigation-assistance-projects-nfip-crs-communities-v1 .rnrnThis dataset contains information on the communities participating in the National Flood Insurance Program (NFIP) Community Rating System (CRS) identified in the HMA subapplication/subgrants that have been submitted to or awarded in FEMA GO, as well as amendments made to the awarded subgrants. The information in this dataset has been deemed appropriate for publication to empower public knowledge of mitigation activities and the nature of HMA grant programs. For more information on the HMA grant programs, visit: https://www.fema.gov/grants/mitigation. For more information on FEMA GO, visit: https://www.fema.gov/grants/guidance-tools/fema-go.rnrnrnThis dataset comes from the source system mentioned above and is subject to a small percentage of human error. In some cases, data was not provided by the subapplicant, applicant, and/or entered into FEMA GO. Due to the voluntary nature of the Hazard Mitigation Assistance Programs, not all communities in this dataset will be mitigated. This dataset is not intended to be used for any official federal financial reporting.rnFEMA's terms and conditions and citation requirements for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page: https://www.fema.gov/about/openfema/terms-conditions.rnrnrnrnFor answers to Frequently Asked Questions (FAQs) about the OpenFEMA program, API, and publicly available datasets, please visit: https://www.fema.gov/about/openfema/faq.rnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v1/HmaSubapplicationsProjectSiteInventories"
+                    "accessURL": "https://www.fema.gov/api/open/v1/HmaSubapplicationsByNfipCrsCommunities"
                 }
-            ]
-        },
-        {
-            "title": "HMA Subapplications By NFIP CRS Communities",
-            "description": "This dataset contains the communities identified in the Hazard Mitigation Assistance (HMA) subapplications/subgrants from the FEMA Grants Outcomes (FEMA GO) system (FEMA\u2019s new grants management system). FEMA GO started accepting Flood Mitigation Assistance (FMA) and Building Resilient Infrastructure and Communities (BRIC) subapplications in Fiscal Year 2020. FEMA GO is projected to support the Hazard Mitigation Grant Program (HMGP) in Calendar Year 2023. For details on HMA communities not captured in FEMA GO, visit https://www.fema.gov/openfema-data-page/hazard-mitigation-assistance-projects-nfip-crs-communities-v1 .rnrnThis dataset contains information on the communities participating in the National Flood Insurance Program (NFIP) Community Rating System (CRS) identified in the HMA subapplication/subgrants that have been submitted to or awarded in FEMA GO, as well as amendments made to the awarded subgrants. The information in this dataset has been deemed appropriate for publication to empower public knowledge of mitigation activities and the nature of HMA grant programs. For more information on the HMA grant programs, visit: https://www.fema.gov/grants/mitigation. For more information on FEMA GO, visit: https://www.fema.gov/grants/guidance-tools/fema-go.rnrnrnThis dataset comes from the source system mentioned above and is subject to a small percentage of human error. In some cases, data was not provided by the subapplicant, applicant, and/or entered into FEMA GO. Due to the voluntary nature of the Hazard Mitigation Assistance Programs, not all communities in this dataset will be mitigated. This dataset is not intended to be used for any official federal financial reporting.rnFEMA's terms and conditions and citation requirements for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page: https://www.fema.gov/about/openfema/terms-conditions.rnrnrnrnFor answers to Frequently Asked Questions (FAQs) about the OpenFEMA program, API, and publicly available datasets, please visit: https://www.fema.gov/about/openfema/faq.rnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0598",
             "keyword": [
                 "Threats and Hazards"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-10-02T14:25:02-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Federal Insurance Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "HMA Subapplications By NFIP CRS Communities"
         },
-            "identifier": "FEMA-0598",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "This dataset contains the financial transactions for Hazard Mitigation Assistance (HMA) subgrants from the FEMA Grants Outcomes (FEMA GO) system (FEMA\u2019s new grants management system). FEMA GO started accepting Flood Mitigation Assistance (FMA) and Building Resilient Infrastructure and Communities (BRIC) subapplications in Fiscal Year 2020. FEMA GO is projected to support the Hazard Mitigation Grant Program (HMGP) in Calendar Year 2023. For details on HMA subgrants not captured in FEMA GO, visit https://www.fema.gov/openfema-data-page/hazard-mitigation-assistance-projects-v3.rnrnThis dataset contains information on the HMA subgrants that have recieved financial transactions in FEMA GO. Sensitive information, such as Personally Identifiable Information (PII), has been removed to protect privacy. The information in this dataset has been deemed appropriate for publication to empower public knowledge of mitigation activities and the nature of HMA grant programs. For more information on the HMA grant programs, visit: https://www.fema.gov/grants/mitigation. For more information on FEMA GO, visit: https://www.fema.gov/grants/guidance-tools/fema-go.rnrnThis dataset comes from the source system mentioned above and is subject to a small percentage of human error. In some cases, data was not provided by the subapplicant, applicant, and/or entered into FEMA GO. The financial information in this dataset is not derived from FEMA's official financial systems. Due to differences in reporting periods, status of obligations, and how business rules are applied, this financial information may differ slightly from official publication on public websites such as https://www.usaspending.gov. This dataset is not intended to be used for any official federal financial reporting.rnFEMA's terms and conditions and citation requirements for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page: https://www.fema.gov/about/openfema/terms-conditions.rnrnFor answers to Frequently Asked Questions (FAQs) about the OpenFEMA program, API, and publicly available datasets, please visit: https://www.fema.gov/about/openfema/faq.rnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v1/HmaSubapplicationsByNfipCrsCommunities"
+                    "accessURL": "https://www.fema.gov/api/open/v1/HmaSubapplicationsFinancialTransactions"
                 }
-            ]
-        },
-        {
-            "title": "HMA Subapplications Financial Transactions",
-            "description": "This dataset contains the financial transactions for Hazard Mitigation Assistance (HMA) subgrants from the FEMA Grants Outcomes (FEMA GO) system (FEMA\u2019s new grants management system). FEMA GO started accepting Flood Mitigation Assistance (FMA) and Building Resilient Infrastructure and Communities (BRIC) subapplications in Fiscal Year 2020. FEMA GO is projected to support the Hazard Mitigation Grant Program (HMGP) in Calendar Year 2023. For details on HMA subgrants not captured in FEMA GO, visit https://www.fema.gov/openfema-data-page/hazard-mitigation-assistance-projects-v3.rnrnThis dataset contains information on the HMA subgrants that have recieved financial transactions in FEMA GO. Sensitive information, such as Personally Identifiable Information (PII), has been removed to protect privacy. The information in this dataset has been deemed appropriate for publication to empower public knowledge of mitigation activities and the nature of HMA grant programs. For more information on the HMA grant programs, visit: https://www.fema.gov/grants/mitigation. For more information on FEMA GO, visit: https://www.fema.gov/grants/guidance-tools/fema-go.rnrnThis dataset comes from the source system mentioned above and is subject to a small percentage of human error. In some cases, data was not provided by the subapplicant, applicant, and/or entered into FEMA GO. The financial information in this dataset is not derived from FEMA's official financial systems. Due to differences in reporting periods, status of obligations, and how business rules are applied, this financial information may differ slightly from official publication on public websites such as https://www.usaspending.gov. This dataset is not intended to be used for any official federal financial reporting.rnFEMA's terms and conditions and citation requirements for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page: https://www.fema.gov/about/openfema/terms-conditions.rnrnFor answers to Frequently Asked Questions (FAQs) about the OpenFEMA program, API, and publicly available datasets, please visit: https://www.fema.gov/about/openfema/faq.rnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0599",
             "keyword": [
                 "Finance"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-10-02T14:25:02-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Hazard Mitigation Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "HMA Subapplications Financial Transactions"
         },
-            "identifier": "FEMA-0599",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "This dataset is also known as the 3d layer and contains a fairly comprehensive set of unaltered source geometry polygons that overlap.  It is derived from Census, State of Maine, and National Flood Hazard Layer political boundaries.rnrnThe Community Layer datasets contain geospatial community boundaries associated with Census and NFIP data. The dataset does not contain personal identifiable information (PII). The Community Layer can be used to tie Community ID numbers (CID) to jurisdiction, tribal, and special land use area boundaries.rnrnA geodatabase (GDB) link is Included in the Full Data section below. The compressed file contains a collection of files that can store, query, and manage both spatial and nonspatial data using software that can read such a file. It bcontains all of the community layers/b, not just the layer for which this dataset page describes. rnrnCitation: FEMA's citation requirements for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page, Citing Data section: https://www.fema.gov/about/openfema/terms-conditions.rnrnFor answers to Frequently Asked Questions (FAQs) about the OpenFEMA program, API, and publicly available datasets, please visit: https://www.fema.gov/about/openfema/faq.rnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v1/HmaSubapplicationsFinancialTransactions"
+                    "accessURL": "https://www.fema.gov/api/open/v1/NfipCommunityLayerComprehensive"
                 }
-            ]
-        },
-        {
-            "title": "NFIP Community Layer Comprehensive",
-            "description": "This dataset is also known as the 3d layer and contains a fairly comprehensive set of unaltered source geometry polygons that overlap.  It is derived from Census, State of Maine, and National Flood Hazard Layer political boundaries.rnrnThe Community Layer datasets contain geospatial community boundaries associated with Census and NFIP data. The dataset does not contain personal identifiable information (PII). The Community Layer can be used to tie Community ID numbers (CID) to jurisdiction, tribal, and special land use area boundaries.rnrnA geodatabase (GDB) link is Included in the Full Data section below. The compressed file contains a collection of files that can store, query, and manage both spatial and nonspatial data using software that can read such a file. It bcontains all of the community layers/b, not just the layer for which this dataset page describes. rnrnCitation: FEMA's citation requirements for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page, Citing Data section: https://www.fema.gov/about/openfema/terms-conditions.rnrnFor answers to Frequently Asked Questions (FAQs) about the OpenFEMA program, API, and publicly available datasets, please visit: https://www.fema.gov/about/openfema/faq.rnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0602",
             "keyword": [
                 "Threats and Hazards"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-10-02T14:25:02-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Federal Insurance Directorate"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NFIP Community Layer Comprehensive"
         },
-            "identifier": "FEMA-0602",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "This dataset contains Hazard Mitigation Assistance (HMA) subapplications/subgrants from the FEMA Grants Outcomes (FEMA GO) system (FEMA\u2019s new grants management system). FEMA GO started accepting Flood Mitigation Assistance (FMA) and Building Resilient Infrastructure and Communities (BRIC) subapplications in Fiscal Year 2020. FEMA GO is projected to support the Hazard Mitigation Grant Program (HMGP) in Calendar Year 2023. For details on HMA subgrants not captured in FEMA GO, visit https://www.fema.gov/openfema-data-page/hazard-mitigation-assistance-projects-v3.rnrnThis dataset contains information on the HMA subapplications/subgrants that have been submitted to or awarded in FEMA GO, as well as amendments made to the awarded subgrants. Sensitive information, such as Personally Identifiable Information (PII), has been removed to protect privacy. The information in this dataset has been deemed appropriate for publication to empower public knowledge of mitigation activities and the nature of HMA grant programs. For more information on the HMA grant programs, visit: https://www.fema.gov/grants/mitigation. For more information on FEMA GO, visit: https://www.fema.gov/grants/guidance-tools/fema-go.rnrnThis dataset comes from the source system mentioned above and is subject to a small percentage of human error. In some cases, data was not provided by the subapplicant, applicant, and/or entered into FEMA GO. The financial information in this dataset is not derived from FEMA's official financial systems. Due to differences in reporting periods, status of obligations, and how business rules are applied, this financial information may differ slightly from official publication on public websites such as https://www.usaspending.gov. This dataset is not intended to be used for any official federal financial reporting.rnFEMA's terms and conditions and citation requirements for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page: https://www.fema.gov/about/openfema/terms-conditions.rnrnFor answers to Frequently Asked Questions (FAQs) about the OpenFEMA program, API, and publicly available datasets, please visit: https://www.fema.gov/about/openfema/faq.rnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v1/NfipCommunityLayerComprehensive"
+                    "accessURL": "https://www.fema.gov/api/open/v2/HmaSubapplications"
                 }
-            ]
-        },
-        {
-            "title": "HMA Subapplications",
-            "description": "This dataset contains Hazard Mitigation Assistance (HMA) subapplications/subgrants from the FEMA Grants Outcomes (FEMA GO) system (FEMA\u2019s new grants management system). FEMA GO started accepting Flood Mitigation Assistance (FMA) and Building Resilient Infrastructure and Communities (BRIC) subapplications in Fiscal Year 2020. FEMA GO is projected to support the Hazard Mitigation Grant Program (HMGP) in Calendar Year 2023. For details on HMA subgrants not captured in FEMA GO, visit https://www.fema.gov/openfema-data-page/hazard-mitigation-assistance-projects-v3.rnrnThis dataset contains information on the HMA subapplications/subgrants that have been submitted to or awarded in FEMA GO, as well as amendments made to the awarded subgrants. Sensitive information, such as Personally Identifiable Information (PII), has been removed to protect privacy. The information in this dataset has been deemed appropriate for publication to empower public knowledge of mitigation activities and the nature of HMA grant programs. For more information on the HMA grant programs, visit: https://www.fema.gov/grants/mitigation. For more information on FEMA GO, visit: https://www.fema.gov/grants/guidance-tools/fema-go.rnrnThis dataset comes from the source system mentioned above and is subject to a small percentage of human error. In some cases, data was not provided by the subapplicant, applicant, and/or entered into FEMA GO. The financial information in this dataset is not derived from FEMA's official financial systems. Due to differences in reporting periods, status of obligations, and how business rules are applied, this financial information may differ slightly from official publication on public websites such as https://www.usaspending.gov. This dataset is not intended to be used for any official federal financial reporting.rnFEMA's terms and conditions and citation requirements for datasets (API usage or file downloads) can be found on the OpenFEMA Terms and Conditions page: https://www.fema.gov/about/openfema/terms-conditions.rnrnFor answers to Frequently Asked Questions (FAQs) about the OpenFEMA program, API, and publicly available datasets, please visit: https://www.fema.gov/about/openfema/faq.rnIf you have media inquiries about this dataset, please email the FEMA News Desk at FEMA-News-Desk@fema.dhs.gov or call (202) 646-3272. For inquiries about FEMA's data and Open Government program, please email the OpenFEMA team at OpenFEMA@fema.dhs.gov.",
+            ],
+            "identifier": "FEMA-0603",
             "keyword": [
                 "Finance"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-10-02T14:25:02-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FEMA/Resilience/Hazard Mitigation Directorate"
             },
+            "rights": null,
+            "title": "HMA Subapplications"
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "024:056"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Open Data (MGMT)",
                 "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-            "identifier": "FEMA-0603",
-            "accessLevel": "public",
-            "bureauCode": [
-                "024:070"
-            ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "description": "Contains the web survey results data from TSA.gov visitors.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.fema.gov/api/open/v2/HmaSubapplications"
+                    "accessURL": "https://www.tsa.gov/web-metrics"
                 }
-            ]
-        },
-        {
-            "title": "TSA.gov Customer Satisfaction Survey",
-            "description": "Contains the web survey results data from TSA.gov visitors.",
+            ],
+            "identifier": "TSA-9eeb659a-72b1-4a43-8fd0-c4ace95b5a56",
             "keyword": [
                 "Web",
                 "Survey Results"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2023-05-25T14:27:18-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "TSA.GOV Public Website"
             },
+            "rights": null,
+            "title": "TSA.gov Customer Satisfaction Survey"
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "024:010"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Open Data (MGMT)",
                 "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-            "identifier": "TSA-9eeb659a-72b1-4a43-8fd0-c4ace95b5a56",
-            "accessLevel": "public",
-            "bureauCode": [
-                "024:056"
-            ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "description": "This repository presents explanations and fully functioning code examples of several semi and fully automated open source accessibility test tools. These tools fall into multiple technical and strategic categories of use for assessing ICT for Section 508/accessibility conformance in the Software Engineering Life Cycle.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.tsa.gov/web-metrics"
+                    "accessURL": "https://github.com/Section508Coordinators/Dev-Automation"
                 }
-            ]
-        },
-        {
-            "title": "Dev-Automation",
-            "description": "This repository presents explanations and fully functioning code examples of several semi and fully automated open source accessibility test tools. These tools fall into multiple technical and strategic categories of use for assessing ICT for Section 508/accessibility conformance in the Software Engineering Life Cycle.",
+            ],
+            "identifier": "MGMT/OCIO/CDOD/OAST10",
             "keyword": [
                 "508/accessibility in test automation",
                 "Axe Core",
                 "Pa11y test engine",
                 "Google Lighthouse test engine"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-09-15T14:10:28-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT/OCIO/CDOD/OAST"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Dev-Automation"
         },
-            "identifier": "MGMT/OCIO/CDOD/OAST10",
+        {
             "accessLevel": "public",
-            "bureauCode": [
-                "024:010"
-            ],
-            "programCode": [
-                "024:000"
+            "bureauCode": [
+                "024:010"
             ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "This is the introductory GitHub repository for supporting the Section 508 Playbook series. It contains the introductory landing page that serves as the roadmap to examples and other support artifacts on the Section508Coordinators site.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://github.com/Section508Coordinators/Dev-Automation"
+                    "accessURL": "https://github.com/Section508Coordinators/Dev-Intro"
                 }
-            ]
-        },
-        {
-            "title": "Dev-Intro",
-            "description": "This is the introductory GitHub repository for supporting the Section 508 Playbook series. It contains the introductory landing page that serves as the roadmap to examples and other support artifacts on the Section508Coordinators site.",
+            ],
+            "identifier": "MGMT/OCIO/CDOD/OAST11",
             "keyword": [
                 "playbook"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-09-15T14:10:28-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT/OCIO/CDOD/OAST"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Dev-Intro"
         },
-            "identifier": "MGMT/OCIO/CDOD/OAST11",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Accessibility Test Automation Repository: This repository contains test automation scripts and related code arranged in examples for the integration of Section 508/accessibility in test automation activities within the Software Engineering Life Cycle.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://github.com/Section508Coordinators/Dev-Intro"
+                    "accessURL": "https://github.com/Section508Coordinators/Dev-Auto-Pipeline-Ex"
                 }
-            ]
-        },
-        {
-            "title": "Dev-Auto-Pipeline-Ex",
-            "description": "Accessibility Test Automation Repository: This repository contains test automation scripts and related code arranged in examples for the integration of Section 508/accessibility in test automation activities within the Software Engineering Life Cycle.",
+            ],
+            "identifier": "MGMT/OCIO/CDOD/OAST12",
             "keyword": [
                 "Test Automation CI/CD Pipeline"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-09-15T14:10:28-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT/OCIO/CDOD/OAST"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Dev-Auto-Pipeline-Ex"
         },
-            "identifier": "MGMT/OCIO/CDOD/OAST12",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "In browser JavaScript Bookmarklets or favlets related to accessibility inspection.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://github.com/Section508Coordinators/Dev-Auto-Pipeline-Ex"
+                    "accessURL": "https://github.com/Section508Coordinators/a11ybookmarklets"
                 }
-            ]
-        },
-        {
-            "title": "a11ybookmarklets",
-            "description": "In browser JavaScript Bookmarklets or favlets related to accessibility inspection.",
+            ],
+            "identifier": "MGMT/OCIO/CDOD/OAST13",
             "keyword": [
                 "a11ybookmarklets"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-09-15T14:10:28-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT/OCIO/CDOD/OAST"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "a11ybookmarklets"
         },
-            "identifier": "MGMT/OCIO/CDOD/OAST13",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "A Simple JavaScript/Node.js CSV to Markdown Table Converter",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://github.com/Section508Coordinators/a11ybookmarklets"
+                    "accessURL": "https://github.com/Section508Coordinators/CsvToMarkdownTable"
                 }
-            ]
-        },
-        {
-            "title": "CsvToMarkdownTable",
-            "description": "A Simple JavaScript/Node.js CSV to Markdown Table Converter",
+            ],
+            "identifier": "MGMT/OCIO/CDOD/OAST14",
             "keyword": [
                 "CSV to Markdown Table Converter"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-09-15T14:10:28-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT/OCIO/CDOD/OAST"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "CsvToMarkdownTable"
         },
-            "identifier": "MGMT/OCIO/CDOD/OAST14",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Purely for tracking issues related to the Trusted Tester - Training for Web on Windows course",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://github.com/Section508Coordinators/CsvToMarkdownTable"
+                    "accessURL": "https://github.com/Section508Coordinators/DHSA-TT-200-A"
                 }
-            ]
-        },
-        {
-            "title": "DHSA-TT-200-A",
-            "description": "Purely for tracking issues related to the Trusted Tester - Training for Web on Windows course",
+            ],
+            "identifier": "MGMT/OCIO/CDOD/OAST15",
             "keyword": [
                 "Trusted Tester issue"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-09-15T14:10:28-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT/OCIO/CDOD/OAST"
             },
+            "rights": null,
+            "title": "DHSA-TT-200-A"
+        },
+        {
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "024:010"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Open Data (MGMT)",
                 "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-            "identifier": "MGMT/OCIO/CDOD/OAST15",
-            "accessLevel": "public",
-            "bureauCode": [
-                "024:010"
-            ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "description": "Knowledge Articles for ACMS services",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://github.com/Section508Coordinators/DHSA-TT-200-A"
+                    "accessURL": "https://dhs.servicenowservices.com/oast?id=dhs_kb"
                 }
-            ]
-        },
-        {
-            "title": "Knowledge Article (ACMS)",
-            "description": "Knowledge Articles for ACMS services",
+            ],
+            "identifier": "MGMT/OCIO/CDOD/OAST2",
             "keyword": [
                 "Accessibility",
                 "Compliance",
@@ -8754,36 +8769,36 @@
                 "Outreach",
                 "ICT Review Request"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-09-15T14:10:28-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT/OCIO/CDOD/OAST"
             },
+            "rights": null,
+            "title": "Knowledge Article (ACMS)"
+        },
+        {
+            "accessLevel": "restricted public",
+            "bureauCode": [
+                "024:010"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Open Data (MGMT)",
                 "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-            "identifier": "MGMT/OCIO/CDOD/OAST2",
-            "accessLevel": "non-public",
-            "bureauCode": [
-                "024:010"
-            ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "description": "The OAST Training portal is the Moodle LMS used by OAST to provide online accessible training to the general public, Federal, State, and local agencies.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://dhs.servicenowservices.com/oast?id=dhs_kb"
+                    "accessURL": "https://training.section508testing.net/"
                 }
-            ]
-        },
-        {
-            "title": "OAST Training Portal (Moodle)",
-            "description": "The OAST Training portal is the Moodle LMS used by OAST to provide online accessible training to the general public, Federal, State, and local agencies.",
+            ],
+            "identifier": "MGMT/OCIO/CDOD/OAST3",
             "keyword": [
                 "Training",
                 "Section 508",
@@ -8792,36 +8807,36 @@
                 "Trusted Tester",
                 "Testing"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-09-15T14:10:28-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT/OCIO/CDOD/OAST"
             },
+            "rights": null,
+            "title": "OAST Training Portal (Moodle)"
+        },
+        {
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "024:010"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Open Data (MGMT)",
                 "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-            "identifier": "MGMT/OCIO/CDOD/OAST3",
-            "accessLevel": "restricted public",
-            "bureauCode": [
-                "024:010"
-            ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "description": "The OAST website provides information about guidelines, best practices, and other resource.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://training.section508testing.net/"
+                    "accessURL": "https://dhsconnect.dhs.gov/org/comp/mgmt/ocio/oast/"
                 }
-            ]
-        },
-        {
-            "title": "DHS Connect OAST Website",
-            "description": "The OAST website provides information about guidelines, best practices, and other resource.",
+            ],
+            "identifier": "MGMT/OCIO/CDOD/OAST4",
             "keyword": [
                 "OAST",
                 "Internal Resources",
@@ -8831,36 +8846,36 @@
                 "Instructions",
                 "Internal Office Website"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-09-15T14:10:28-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT/OCIO/CDOD/OAST"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "DHS Connect OAST Website"
         },
-            "identifier": "MGMT/OCIO/CDOD/OAST4",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "DART is an online self-service tool provided by the OAST to help procurement officials obtain tailored Section 508 requirements language for their solicitations. DART can also be used by project teams to obtain a detailed list of potential applicable Section 508 Standards for project deliverables to support project planning and design activities, and suggested questions to include in Request for Information to support market research activities. This system is managed by the Office of Accessible Systems and Technology (OAST) under the HQ CIO Office and is deployed on DHS Connect.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://dhsconnect.dhs.gov/org/comp/mgmt/ocio/oast/"
-                }
-            ]
-        },
-        {
-            "title": "DHS Accessibility Requirement Tool (DART)",
-            "description": "DART is an online self-service tool provided by the OAST to help procurement officials obtain tailored Section 508 requirements language for their solicitations. DART can also be used by project teams to obtain a detailed list of potential applicable Section 508 Standards for project deliverables to support project planning and design activities, and suggested questions to include in Request for Information to support market research activities. This system is managed by the Office of Accessible Systems and Technology (OAST) under the HQ CIO Office and is deployed on DHS Connect.",
+                    "accessURL": "https://www.dhs.gov/DART"
+                }
+            ],
+            "identifier": "MGMT/OCIO/CDOD/OAST5",
             "keyword": [
                 "Accessibility",
                 "Soliciation",
@@ -8869,36 +8884,36 @@
                 "Project Planning",
                 "Market Research"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-09-15T14:10:28-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT/OCIO/CDOD/OAST"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "DHS Accessibility Requirement Tool (DART)"
         },
-            "identifier": "MGMT/OCIO/CDOD/OAST5",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "The playbook provides guidelines, best practices, and other resources to help integrate accessibility into IT projects throughout the entire lifecycle. The playbook includes resources for IT Project Managers, Acquisition Teams, Developers, Testers, and 508 PMs and SMEs.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.dhs.gov/DART"
+                    "accessURL": "https://dhsconnect.dhs.gov/org/comp/mgmt/ocio/oast/playbook/index.html"
                 }
-            ]
-        },
-        {
-            "title": "DHS Section 508 Playbook",
-            "description": "The playbook provides guidelines, best practices, and other resources to help integrate accessibility into IT projects throughout the entire lifecycle. The playbook includes resources for IT Project Managers, Acquisition Teams, Developers, Testers, and 508 PMs and SMEs.",
+            ],
+            "identifier": "MGMT/OCIO/CDOD/OAST6",
             "keyword": [
                 "Section 508",
                 "Trusted Tester",
@@ -8914,36 +8929,36 @@
                 "SME",
                 "PM"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-09-15T14:10:28-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT/OCIO/CDOD/OAST"
             },
+            "rights": null,
+            "title": "DHS Section 508 Playbook"
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "024:010"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Open Data (MGMT)",
                 "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-            "identifier": "MGMT/OCIO/CDOD/OAST6",
-            "accessLevel": "non-public",
-            "bureauCode": [
-                "024:010"
-            ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "description": "ACRT is a browser-based standalone application for recording accessibility test results from Trusted Testers. All input data will be stored as JSON &/or html files in the local machine which can be shared as needed. Information in the JSON file can be further manipulated for analytics and reporting purposes as needed.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://dhsconnect.dhs.gov/org/comp/mgmt/ocio/oast/playbook/index.html"
+                    "accessURL": "https://github.com/Section508Coordinators/ACRT"
                 }
-            ]
-        },
-        {
-            "title": "Accessibility Conformance Reporting Tool (ACRT) tool",
-            "description": "ACRT is a browser-based standalone application for recording accessibility test results from Trusted Testers. All input data will be stored as JSON &/or html files in the local machine which can be shared as needed. Information in the JSON file can be further manipulated for analytics and reporting purposes as needed.",
+            ],
+            "identifier": "MGMT/OCIO/CDOD/OAST7",
             "keyword": [
                 "Trusted Tester",
                 "test result",
@@ -8953,212 +8968,206 @@
                 "analytics",
                 "html"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-09-15T14:10:28-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT/OCIO/CDOD/OAST"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Accessibility Conformance Reporting Tool (ACRT) tool"
         },
-            "identifier": "MGMT/OCIO/CDOD/OAST7",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "The Trusted Tester process provides a standardized approach for manual inspection of Web and software content for conformance with the Revised Section 508 Standards.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://github.com/Section508Coordinators/ACRT"
+                    "accessURL": "https://github.com/Section508Coordinators/TrustedTester"
                 }
-            ]
-        },
-        {
-            "title": "Trusted Tester Process",
-            "description": "The Trusted Tester process provides a standardized approach for manual inspection of Web and software content for conformance with the Revised Section 508 Standards.",
+            ],
+            "identifier": "MGMT/OCIO/CDOD/OAST8",
             "keyword": [
                 "Trusted tester 5.0",
                 "Trusted tester 5.1"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-09-15T14:10:28-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT/OCIO/CDOD/OAST"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Trusted Tester Process"
         },
-            "identifier": "MGMT/OCIO/CDOD/OAST8",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Strictly for training and certification exam purposes, DHS hosts a version of ANDI that is updated only in conjunction with updates to the Trusted Tester training course content. Do not use this version of ANDI for production web testing.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://github.com/Section508Coordinators/TrustedTester"
+                    "accessURL": "https://www.dhs.gov/xlibrary/oast/ANDI/andi.js"
                 }
-            ]
-        },
-        {
-            "title": "ANDI Bookmarklet for DHS Trusted Tester Training",
-            "description": "Strictly for training and certification exam purposes, DHS hosts a version of ANDI that is updated only in conjunction with updates to the Trusted Tester training course content. Do not use this version of ANDI for production web testing.",
+            ],
+            "identifier": "MGMT/OCIO/CDOD/OAST9",
             "keyword": [
                 "ANDI",
                 "Accessible Name and Description Inspector"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-09-15T14:10:28-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT/OCIO/CDOD/OAST"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "ANDI Bookmarklet for DHS Trusted Tester Training"
         },
-            "identifier": "MGMT/OCIO/CDOD/OAST9",
+        {
             "accessLevel": "public",
             "bureauCode": [
-                "024:010"
-            ],
-            "programCode": [
-                "024:000"
+                "024:070"
             ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://www.dhs.gov/xlibrary/oast/ANDI/andi.js"
-                }
-            ]
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Emergency Management Institute Course Schedule Dataset",
             "description": "Schedule of EMI courses being offered for current and upcoming fiscal year.",
+            "identifier": "FEMA-10480",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-29T14:00:03-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Emergency Management Institute Course Schedule Dataset"
         },
-            "identifier": "FEMA-10480",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Emergency Management Institute Independent Study Courses Dataset",
             "description": "The Emergency Management Institute (EMI) Independent Study Program (ISP) provides web-based training related to all aspects of emergency management for the whole community. The EMI ISP is a distance learning program that offers training free of charge via the public-facing web site  training.fema.gov. It serves as both classroom alternative to delivering valuable training to the professional and volunteer emergency management community  and an opportunity to improve public awareness and promote disaster preparedness nationally. The EMI ISP offers more than 195 training courses.",
+            "identifier": "FEMA-10482",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-29T14:00:03-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Emergency Management Institute Independent Study Courses Dataset"
         },
-            "identifier": "FEMA-10482",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Emergency Management Institute Training Catalog Dataset",
             "description": "Descriptions of all EMI courses as well as other EMI training information.",
+            "identifier": "FEMA-10479",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-29T14:00:03-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Emergency Management Institute Training Catalog Dataset"
         },
-            "identifier": "FEMA-10479",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:070"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "USFA Learning Management System Self Study Dataset",
             "description": "An externally hosted LMS environment to include: application and database software support  hosting services  Tier 1  2  3 support and course content development/update and migration support",
+            "identifier": "FEMA-10396",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-29T14:00:03-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "USFA Learning Management System Self Study Dataset"
         },
-            "identifier": "FEMA-10396",
+        {
             "accessLevel": "public",
             "bureauCode": [
-                "024:070"
-            ],
-            "programCode": [
-                "024:000"
+                "024:010"
             ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Office of Chief Human Capital Office (OCHCO) Virtual Production Environment (VPE) Human Capital Business Solutions (HCBS) EIE",
             "description": "OCHCO VPE is a repository of DHS-wide HR data including payroll, time & attendance, organization, personal action, etc., it contains current as well as historical information. OCHCO VPE provides standardized DHS enterprise HR reporting. EIE provides O&M support, vendor management & customer service across DHS for enterprise-wide systems & services and the Enterprise Information Environment (EIE). The goal of HCBS - EIE is to develop a data repository from the combine data from the independent systems that can be used to: Establish authoritative source for each data element that is common across the enterprise. Develop an integrated data model for the HR Enterprise. Provide a central mechanism for data interchange between the component systems to improve data integrity and availability. Establish a platform to support common reporting capabilities for all applications within the HR Enterprise. Establish a platform to support Enterprise HR Reporting, allowing reporting to transcend application domains.",
+            "identifier": "MGMT-OCHCO-VPE-EIE",
             "keyword": [
                 "repository",
                 "EIE",
@@ -9169,286 +9178,286 @@
                 "HR",
                 "Data"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-03-06T14:05:42-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Office of Chief Human Capital Office (OCHCO) Virtual Production Environment (VPE) Human Capital Business Solutions (HCBS) EIE"
         },
-            "identifier": "MGMT-OCHCO-VPE-EIE",
+        {
             "accessLevel": "public",
-            "bureauCode": [
-                "024:010"
-            ],
-            "programCode": [
-                "024:000"
+            "bureauCode": [
+                "024:010"
             ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Commercially Available Staffing Solution (CASS) - Award - Monster Hiring Management Enterprise (MHME) - Personnel Action Request (PAR) Processing",
             "description": "The Personnel Action Request (PAR) module within the CASS provides the ability for personnel action request processing by an HR Specialist to process employee actions throughout their career.",
+            "identifier": "MGMT-OCHCO-MHME-CASSPAR",
             "keyword": [
                 "Employee",
                 "Personnel Action"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Commercially Available Staffing Solution (CASS) - Award - Monster Hiring Management Enterprise (MHME) - Personnel Action Request (PAR) Processing"
         },
-            "identifier": "MGMT-OCHCO-MHME-CASSPAR",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "DHS Career Mapping System",
             "description": "Career Development for certain job series",
+            "identifier": "MGMT-OCHCO-OPM-CAREERPATHTOOL",
             "keyword": [
                 "Employee"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "OPM"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "DHS Career Mapping System"
         },
-            "identifier": "MGMT-OCHCO-OPM-CAREERPATHTOOL",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Employment Verification and Unemployment Compensation",
             "description": "Used to verify employment",
+            "identifier": "MGMT-OCHCO-EVUC-EMPLOYMENT_VERIFY",
             "keyword": [
                 "Verify",
                 "employment",
                 "unemployment",
                 "compensation"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:53:43-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Employment Verification and Unemployment Compensation"
         },
-            "identifier": "MGMT-OCHCO-EVUC-EMPLOYMENT_VERIFY",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "EIE Change Detection",
             "description": "Log records of data changes",
+            "identifier": "MGMT-OCHCO-EIE-CHANGEDETECTION",
             "keyword": [
                 "changelog",
                 "log",
                 "change"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "EIE Change Detection"
         },
-            "identifier": "MGMT-OCHCO-EIE-CHANGEDETECTION",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "NFCBear",
             "description": "Bi-weekly Examination Analysis and Reporting System in USDA National Finance Center (NFC)",
+            "identifier": "MGMT-OCHCO-EIE-NFCBear",
             "keyword": [
                 "NFC",
                 "USDA",
                 "reporting"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NFCBear"
         },
-            "identifier": "MGMT-OCHCO-EIE-NFCBear",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "NFCPerHis",
             "description": "PERHIS contains data elements populated from NFC biweekly payroll EMPLOYEE PERSONNEL ACTIONS",
+            "identifier": "MGMT-OCHCO-EIE-NFCPerHis",
             "keyword": [
                 "NFC",
                 "USDA",
                 "personnel"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NFCPerHis"
         },
-            "identifier": "MGMT-OCHCO-EIE-NFCPerHis",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "NFC Table102",
             "description": "TABLE102 contains data elements populated from NFC biweekly payroll such as EMPLOYEE name, bio, work, residence, and other details.",
+            "identifier": "MGMT-OCHCO-EIE-NFCTable102",
             "keyword": [
                 "NFC",
                 "USDA",
                 "payroll"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "USDA/NFC"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NFC Table102"
         },
-            "identifier": "MGMT-OCHCO-EIE-NFCTable102",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "PMSO",
             "description": "Position Management data from Office of Chief Financial Officer",
+            "identifier": "MGMT-OCHCO-EIE-PMSO",
             "keyword": [
                 "Position"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T14:26:04-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "PMSO"
         },
-            "identifier": "MGMT-OCHCO-EIE-PMSO",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "USAStaffing Onboarding",
             "description": "Employee onboarding data from USA Staffing",
+            "identifier": "MGMT-OCHCO-EIE-USAStaffingOnboarding",
             "keyword": [
                 "onboarding",
                 "USA Staffing"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "USAStaffing Onboarding"
         },
-            "identifier": "MGMT-OCHCO-EIE-USAStaffingOnboarding",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "WebTA",
             "description": "Data contained within WebTA",
+            "identifier": "MGMT-OCHCO-WebTA",
             "keyword": [
                 "WebTA",
                 "NFC",
@@ -9457,1020 +9466,1020 @@
                 "Attendance",
                 "T&A"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NFC"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "WebTA"
         },
-            "identifier": "MGMT-OCHCO-WebTA",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "TALX",
             "description": "This system allows employees to grant authorized access to lending institutions in order to verify employment.",
+            "identifier": "MGMT-OCHCO-EQUIFAX-TALX",
             "keyword": [
                 "Verify",
                 "employment",
                 "unemployment",
                 "compensation"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-03-06T15:05:52-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "TALX"
         },
-            "identifier": "MGMT-OCHCO-EQUIFAX-TALX",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "IdeaFactory",
             "description": "an internet web-based tool that uses social media concepts to enable innovation and organizational collaboration within DHS. Enables all DHS employees to develop, rate, and improve innovative ideas for programs, processes, and technologies.",
+            "identifier": "MGMT-OCHCO-IDEAFACTORY-IDEAFACTORY",
             "keyword": [
                 "collaboration",
                 "social media",
                 "innovate"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "IdeaFactory"
         },
-            "identifier": "MGMT-OCHCO-IDEAFACTORY-IDEAFACTORY",
+        {
             "accessLevel": "public",
-            "bureauCode": [
-                "024:010"
-            ],
-            "programCode": [
-                "024:000"
+            "bureauCode": [
+                "024:010"
             ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Information Research Inquiry System (IRIS)",
             "description": "An inquiry only NFC system which allows agencies to research payroll/personnel inquiries from employees and other sources. Provides access to at least 1 year of current personnel and at least 5 years of data for historical personnel and payroll files.",
+            "identifier": "MGMT-OCHCO-IRIS-IRIS",
             "keyword": [
                 "NFC",
                 "IRIS"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NFC"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Information Research Inquiry System (IRIS)"
         },
-            "identifier": "MGMT-OCHCO-IRIS-IRIS",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Commercially Available Staffing Solution (CASS) - Award - Monster Hiring Management Enterprise (MHME) - Applicant Tracking System (ATS) and Assessment",
             "description": "Provides Applicant Tracking solution to streamline process and ensure regulatory compliance. Monster Applicant Assessment provides a comprehensive catalog of selection tests to measure a wide variety of factors critical for successful job performance.",
+            "identifier": "MGMT-OCHCO-MHME-ATS",
             "keyword": [
                 "Applicant"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Commercially Available Staffing Solution (CASS) - Award - Monster Hiring Management Enterprise (MHME) - Applicant Tracking System (ATS) and Assessment"
         },
-            "identifier": "MGMT-OCHCO-MHME-ATS",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Commercially Available Staffing Solution (CASS) - Award - Monster Hiring Management Enterprise (MHME) - Performance Ratings and Awards",
             "description": "Provides performance ratings and awards system",
+            "identifier": "MGMT-OCHCO-MHME-AWARDS",
             "keyword": [
                 "Performance",
                 "ratings",
                 "awards"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Commercially Available Staffing Solution (CASS) - Award - Monster Hiring Management Enterprise (MHME) - Performance Ratings and Awards"
         },
-            "identifier": "MGMT-OCHCO-MHME-AWARDS",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Commercially Available Staffing Solution (CASS) - Award - Monster Hiring Management Enterprise (MHME) - Benefits and Retirement Tracking",
             "description": "Provide benefits management and retirement tracking",
+            "identifier": "MGMT-OCHCO-MHME-BENEFITS",
             "keyword": [
                 "Benefits",
                 "retirement"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Commercially Available Staffing Solution (CASS) - Award - Monster Hiring Management Enterprise (MHME) - Benefits and Retirement Tracking"
         },
-            "identifier": "MGMT-OCHCO-MHME-BENEFITS",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Commercially Available Staffing Solution (CASS) - Award - Monster Hiring Management Enterprise (MHME) - Business Intelligence and Data Analytics",
             "description": "Provides business intelligence reports and data analysis of hiring trends",
+            "identifier": "MGMT-OCHCO-MHME-BI",
             "keyword": [
                 "Business Intelligence",
                 "reports"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Commercially Available Staffing Solution (CASS) - Award - Monster Hiring Management Enterprise (MHME) - Business Intelligence and Data Analytics"
         },
-            "identifier": "MGMT-OCHCO-MHME-BI",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Commercially Available Staffing Solution (CASS) - Award - Monster Hiring Management Enterprise (MHME) - Offboarding",
             "description": "Provide offboarding functions",
+            "identifier": "MGMT-OCHCO-MHME-OFFBOARD",
             "keyword": [
                 "Offboarding",
                 "processing"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Commercially Available Staffing Solution (CASS) - Award - Monster Hiring Management Enterprise (MHME) - Offboarding"
         },
-            "identifier": "MGMT-OCHCO-MHME-OFFBOARD",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Commercially Available Staffing Solution (CASS) - Award - Monster Hiring Management Enterprise (MHME) - Onboarding",
             "description": "Uses previously collected new-hire data to quickly and accurately pre-populate and route emails, letters, and forms to selected candidates.",
+            "identifier": "MGMT-OCHCO-MHME-ONBOARD",
             "keyword": [
                 "processing",
                 "Onboarding"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Commercially Available Staffing Solution (CASS) - Award - Monster Hiring Management Enterprise (MHME) - Onboarding"
         },
-            "identifier": "MGMT-OCHCO-MHME-ONBOARD",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Commercially Available Staffing Solution (CASS) - Award - Monster Hiring Management Enterprise (MHME) - Position Description (PD) Library",
             "description": "Automates position description development, approval, and reporting workflows",
+            "identifier": "MGMT-OCHCO-MHME-PD_LIBRARY",
             "keyword": [
                 "Position",
                 "Library"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Commercially Available Staffing Solution (CASS) - Award - Monster Hiring Management Enterprise (MHME) - Position Description (PD) Library"
         },
-            "identifier": "MGMT-OCHCO-MHME-PD_LIBRARY",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Commercially Available Staffing Solution (CASS) - Award - Monster Hiring Management Enterprise (MHME) - Position Classification",
             "description": "Position Classification features an intuitive step-by-step wizard and an extensive library of customizable position descriptions and cover letters that comply with OPM guidelines.",
+            "identifier": "MGMT-OCHCO-MHME-POSITION_CLASSIFICATION",
             "keyword": [
                 "Position"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Commercially Available Staffing Solution (CASS) - Award - Monster Hiring Management Enterprise (MHME) - Position Classification"
         },
-            "identifier": "MGMT-OCHCO-MHME-POSITION_CLASSIFICATION",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "NFC - EmpowHR Benefits Management",
             "description": "Employee Benefits Administration",
+            "identifier": "MGMT-OCHCO-NFC-EMPOWHR_BENEFITS",
             "keyword": [
                 "Employee",
                 "NFC",
                 "USDA",
                 "EmpowHR"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NFC"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NFC - EmpowHR Benefits Management"
         },
-            "identifier": "MGMT-OCHCO-NFC-EMPOWHR_BENEFITS",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "NFC - EmpowHR Position Classification",
             "description": "Position Classification",
+            "identifier": "MGMT-OCHCO-NFC-EMPOWHR_CLASSIFICATION",
             "keyword": [
                 "Employee",
                 "NFC",
                 "USDA",
                 "EmpowHR"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NFC"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NFC - EmpowHR Position Classification"
         },
-            "identifier": "MGMT-OCHCO-NFC-EMPOWHR_CLASSIFICATION",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "NFC - EmpowHR Employee Development",
             "description": "Training and Employee Development",
+            "identifier": "MGMT-OCHCO-NFC-EMPOWHR_DEVELOPMENT",
             "keyword": [
                 "Employee",
                 "NFC",
                 "USDA",
                 "EmpowHR"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NFC"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NFC - EmpowHR Employee Development"
         },
-            "identifier": "MGMT-OCHCO-NFC-EMPOWHR_DEVELOPMENT",
+        {
             "accessLevel": "public",
-            "bureauCode": [
-                "024:010"
-            ],
-            "programCode": [
-                "024:000"
+            "bureauCode": [
+                "024:010"
             ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "NFC - EmpowHR Employee and Labor Relations",
             "description": "EmpowHR- Employee and Labor Relations",
+            "identifier": "MGMT-OCHCO-NFC-EMPOWHR_LABOR",
             "keyword": [
                 "Employee",
                 "NFC",
                 "USDA",
                 "EmpowHR"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NFC"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NFC - EmpowHR Employee and Labor Relations"
         },
-            "identifier": "MGMT-OCHCO-NFC-EMPOWHR_LABOR",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "NFC - EmpowHR Employee Performance Management",
             "description": "Employee Performance and Accountability",
+            "identifier": "MGMT-OCHCO-NFC-EMPOWHR_PERFORMANCE",
             "keyword": [
                 "Employee",
                 "NFC",
                 "USDA",
                 "EmpowHR"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NFC"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NFC - EmpowHR Employee Performance Management"
         },
-            "identifier": "MGMT-OCHCO-NFC-EMPOWHR_PERFORMANCE",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "NFC - EmpowHR HR action Processing",
             "description": "EmpowHR- HR Processing",
+            "identifier": "MGMT-OCHCO-NFC-EMPOWHR_PROCESSING",
             "keyword": [
                 "Employee",
                 "NFC",
                 "USDA",
                 "EmpowHR"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NFC"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NFC - EmpowHR HR action Processing"
         },
-            "identifier": "MGMT-OCHCO-NFC-EMPOWHR_PROCESSING",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "NFC - EmpowHR Sourcing and Recruitment",
             "description": "Recruitment",
+            "identifier": "MGMT-OCHCO-NFC-EMPOWHR_RECRUIT",
             "keyword": [
                 "Employee",
                 "NFC",
                 "USDA",
                 "EmpowHR"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NFC"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NFC - EmpowHR Sourcing and Recruitment"
         },
-            "identifier": "MGMT-OCHCO-NFC-EMPOWHR_RECRUIT",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "NFC - EmpowHR Workforce Planning",
             "description": "Succession Planning, Organizational Management",
+            "identifier": "MGMT-OCHCO-NFC-EMPOWHR_WORKFORCEPLAN",
             "keyword": [
                 "Employee",
                 "NFC",
                 "USDA",
                 "EmpowHR"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NFC"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NFC - EmpowHR Workforce Planning"
         },
-            "identifier": "MGMT-OCHCO-NFC-EMPOWHR_WORKFORCEPLAN",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "NFC - EmpowHR Workforce Reporting",
             "description": "Strategic Workforce Reporting",
+            "identifier": "MGMT-OCHCO-NFC-EMPOWHR_WORKFORCEREPORT",
             "keyword": [
                 "Employee",
                 "NFC",
                 "USDA",
                 "EmpowHR"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NFC"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NFC - EmpowHR Workforce Reporting"
         },
-            "identifier": "MGMT-OCHCO-NFC-EMPOWHR_WORKFORCEREPORT",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "NFC - Entry, Processing, Inquiry, and Corrections System (EPICWEB)",
             "description": "EPIC is an internet based payroll/personnel database entry, processing, correction, and inquiry application of the National Finance Center (NFC). Payroll and Personnel Actions are entered for processing by the National Finance Center",
+            "identifier": "MGMT-OCHCO-NFC-EPIC",
             "keyword": [
                 "NFC",
                 "USDA",
                 "employee"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NFC"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NFC - Entry, Processing, Inquiry, and Corrections System (EPICWEB)"
         },
-            "identifier": "MGMT-OCHCO-NFC-EPIC",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "NFC - Entry, Processing, Inquiry and Corrections System (EPICWEB) employee records recordkeeping",
             "description": "Modify, delete employee transactions, and create, modify or delete history records.",
+            "identifier": "MGMT-OCHCO-NFC-EPICWEB",
             "keyword": [
                 "NFC",
                 "USDA",
                 "employee"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NFC"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NFC - Entry, Processing, Inquiry and Corrections System (EPICWEB) employee records recordkeeping"
         },
-            "identifier": "MGMT-OCHCO-NFC-EPICWEB",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "OPM USA Hire",
             "description": "USA Hire",
+            "identifier": "MGMT-OCHCO-OPM-USAHIRE",
             "keyword": [
                 "OPM",
                 "Hire"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-03-06T14:56:48-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "OPM"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "OPM USA Hire"
         },
-            "identifier": "MGMT-OCHCO-OPM-USAHIRE",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "NFC - Entry, Processing, Inquiry and Corrections System (EPICWEB) employee records disclosure",
             "description": "Roll back applied documents",
+            "identifier": "MGMT-OCHCO-NFC-EPICWEB_DISCLOSE",
             "keyword": [
                 "NFC",
                 "USDA",
                 "employee"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NFC"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NFC - Entry, Processing, Inquiry and Corrections System (EPICWEB) employee records disclosure"
         },
-            "identifier": "MGMT-OCHCO-NFC-EPICWEB_DISCLOSE",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "NFC - Entry, Processing, Inquiry and Corrections System (EPICWEB) Payroll",
             "description": "Enter payroll and personnel actions for processing by the National Finance Center PPS",
+            "identifier": "MGMT-OCHCO-NFC-EPICWEB_PAYROLL",
             "keyword": [
                 "NFC",
                 "USDA",
                 "payroll",
                 "employee"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NFC"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NFC - Entry, Processing, Inquiry and Corrections System (EPICWEB) Payroll"
         },
-            "identifier": "MGMT-OCHCO-NFC-EPICWEB_PAYROLL",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "NFC - Entry, Processing, Inquiry, and Corrections System (EPICWEB) employee records reporting",
             "description": "Execute status and suspense reports",
+            "identifier": "MGMT-OCHCO-NFC-EPICWEB_REPORT",
             "keyword": [
                 "NFC",
                 "USDA",
                 "reports",
                 "employee"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NFC"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NFC - Entry, Processing, Inquiry, and Corrections System (EPICWEB) employee records reporting"
         },
-            "identifier": "MGMT-OCHCO-NFC-EPICWEB_REPORT",
+        {
             "accessLevel": "public",
-            "bureauCode": [
-                "024:010"
-            ],
-            "programCode": [
-                "024:000"
+            "bureauCode": [
+                "024:010"
             ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "NFC - Entry, Processing, Inquiry and Corrections System (EPICWEB) workforce reporting",
             "description": "View future and current payroll/personnel documents to be processed",
+            "identifier": "MGMT-OCHCO-NFC-EPICWEB_WORKREPORT",
             "keyword": [
                 "NFC",
                 "USDA",
                 "employee"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NFC"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NFC - Entry, Processing, Inquiry and Corrections System (EPICWEB) workforce reporting"
         },
-            "identifier": "MGMT-OCHCO-NFC-EPICWEB_WORKREPORT",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "NFC - Employee Personal Page (EPP)",
             "description": "Allow DHS users to review their HR related information such as Pay, Leave, Heath Insurance, Life Insurance, Flexible Spending Account, Travel, W-2. Self service option allows users to maintain the following information: direct deposit, Health Insurance, W-4, Financial Allotments, Home Address, Savings Bond, State Tax Withholding, Thrift Savings Plan. Financial disclosure support allows users to maintain and print Forms SF-278 and OGE-450 online.",
+            "identifier": "MGMT-OCHCO-NFC-EPP",
             "keyword": [
                 "NFC",
                 "USDA"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NFC"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NFC - Employee Personal Page (EPP)"
         },
-            "identifier": "MGMT-OCHCO-NFC-EPP",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "NFC - Employee Personal Page (EPP) Insurance management",
             "description": "Health and Life insurance management",
+            "identifier": "MGMT-OCHCO-NFC-EPP_INSURE",
             "keyword": [
                 "Employee",
                 "NFC",
                 "USDA",
                 "personal page"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NFC"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NFC - Employee Personal Page (EPP) Insurance management"
         },
-            "identifier": "MGMT-OCHCO-NFC-EPP_INSURE",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "NFC - Employee Personal Page (EPP) Leave management",
             "description": "Leave management, earning and leave statements",
+            "identifier": "MGMT-OCHCO-NFC-EPP_LEAVE",
             "keyword": [
                 "Employee",
                 "NFC",
                 "USDA",
                 "personal page"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NFC"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NFC - Employee Personal Page (EPP) Leave management"
         },
-            "identifier": "MGMT-OCHCO-NFC-EPP_LEAVE",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "NFC - Employee Personal Page (EPP) Payroll",
             "description": "Direct Deposit, Tax management, financial allotments",
+            "identifier": "MGMT-OCHCO-NFC-EPP_PAYROLL",
             "keyword": [
                 "Employee",
                 "NFC",
                 "USDA",
                 "personal page"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NFC"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NFC - Employee Personal Page (EPP) Payroll"
         },
-            "identifier": "MGMT-OCHCO-NFC-EPP_PAYROLL",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "NFC - Employee Personal Page (EPP) Retirement planning",
             "description": "Thrift Savings Plan management",
+            "identifier": "MGMT-OCHCO-NFC-EPP_RETIRE",
             "keyword": [
                 "Employee",
                 "NFC",
                 "USDA",
                 "personal page"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NFC"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NFC - Employee Personal Page (EPP) Retirement planning"
         },
-            "identifier": "MGMT-OCHCO-NFC-EPP_RETIRE",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "NFC - Focus/Insight Reporting",
             "description": "FOCUS Reporting System FOCUSRPT is an enhanced reporting system used to create reports. Insight is a comprehensive, enterprise-wide data warehouse with advanced reporting and business intelligence capabilities.",
+            "identifier": "MGMT-OCHCO-NFC-FOCUSRPT",
             "keyword": [
                 "NFC",
                 "USDA",
                 "employee"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NFC"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NFC - Focus/Insight Reporting"
         },
-            "identifier": "MGMT-OCHCO-NFC-FOCUSRPT",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "MyEPP",
             "description": "Data contained within MyEPP",
+            "identifier": "MGMT-OCHCO-NFC-MYEPP",
             "keyword": [
                 "Employee",
                 "NFC",
                 "EPP"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NFC"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "MyEPP"
         },
-            "identifier": "MGMT-OCHCO-NFC-MYEPP",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "OPM USAJOBS Agency Talent Portal (ATP)",
             "description": "Discover qualified job seekers who have made their resumes searchable in their USAJOBS account with Resume Mining and use Campaigns to collect, track, and organize job seekers of interest in ATP.",
+            "identifier": "MGMT-OCHCO-OPM-ATP",
             "keyword": [
                 "OPM",
                 "USAJobs",
@@ -10478,172 +10487,172 @@
                 "Candidates",
                 "Resumes"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "OPM"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "OPM USAJOBS Agency Talent Portal (ATP)"
         },
-            "identifier": "MGMT-OCHCO-OPM-ATP",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Passport, Mid-Level Leadership Development Program",
             "description": "Collects, tracks and reports on individual development plan completion rates, 180 Degree Assessment and Post 180 Degree Assessment data, and other program completion data.",
+            "identifier": "MGMT-OCHCO-PASSPORT-LEADERSHIP",
             "keyword": [
                 "Employee Development",
                 "Leadership"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Passport, Mid-Level Leadership Development Program"
         },
-            "identifier": "MGMT-OCHCO-PASSPORT-LEADERSHIP",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Position Description Library",
             "description": "Used for Suitability and Fitness Adjudication for civilian employees and assists in determining the level of risk and sensitivity of positions in the competitive service, positions in the excepted service where the incumbent can be noncompetitively converted to competitive service, and initial career appointments in the SES SharePoint based system that stores PDs online and allows them to be viewed and downloaded.",
+            "identifier": "MGMT-OCHCO-PDLIBRARY-LIBRARY",
             "keyword": [
                 "Employee",
                 "Library",
                 "Position Description",
                 "PD"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Position Description Library"
         },
-            "identifier": "MGMT-OCHCO-PDLIBRARY-LIBRARY",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "QuestionMark and Varint Survey Software",
             "description": "Is a COTS product and has two layers: the Questionmark Perception and the Questionmark Secure. Perception is an assessment management system which enables educators and trainers to author, schedule, deliver, and report on surveys, quizzes, tests and exams. Secure is the freeware download to allow for a more secure environment for taking exams and tests.",
+            "identifier": "MGMT-OCHCO-QUESTIONMARK-SURVEY",
             "keyword": [
                 "Survey",
                 "tests",
                 "quizzes"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "QuestionMark and Varint Survey Software"
         },
-            "identifier": "MGMT-OCHCO-QUESTIONMARK-SURVEY",
+        {
             "accessLevel": "public",
-            "bureauCode": [
-                "024:010"
-            ],
-            "programCode": [
-                "024:000"
+            "bureauCode": [
+                "024:010"
             ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "SkillSoft Content Library",
             "description": "DHS Contracted Training courses. Subsystem of LMS used to provide content for classroom training.",
+            "identifier": "MGMT-OCHCO-SKILLSOFT-LIBRARY",
             "keyword": [
                 "Skillsoft"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "SkillSoft Content Library"
         },
-            "identifier": "MGMT-OCHCO-SKILLSOFT-LIBRARY",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "WebOPUS Case Management Software - Workers Compensation Case Management System (WCCMS)",
             "description": "IT System used for Nurse Case Management Services Contract.  System provided by contractor.",
+            "identifier": "MGMT-OCHCO-WC-WCCMS",
             "keyword": [
                 "Worker's Compensation",
                 "nurse"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "WebOPUS Case Management Software - Workers Compensation Case Management System (WCCMS)"
         },
-            "identifier": "MGMT-OCHCO-WC-WCCMS",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "HireVue",
             "description": "The HireVue platform provides a virtual capability component to support face-to face interviews, online messaging capabilities, video chat recording, virtual informational booth areas for components/offices, and candidate scheduling options to support real-time cybersecurity recruitment initiatives.",
+            "identifier": "MGMT-OCHCO-HIREVUE-HIREVIEW",
             "keyword": [
                 "Applicant",
                 "hiring",
@@ -10653,30 +10662,30 @@
                 "Interview",
                 "Video"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-03-06T15:32:38-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "HireVue"
         },
-            "identifier": "MGMT-OCHCO-HIREVUE-HIREVIEW",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Commercially Available Staffing Solution (CASS) - Award - Monster Hiring Management Enterprise (MHME)",
             "description": "CASS provides the full employee lifecycle of human capital functions as described in the OPM Human Capital Business Reference Model (BRM). These functions represent the responsibilities, processes, and activities required to manage employees from hire to retire. BRM functions include position classification and management, recruitment and placement; personnel action processing, employee benefits, retirement, and reporting and analytics.",
+            "identifier": "MGMT-OCHCO-MHME-CASS",
             "keyword": [
                 "Employee",
                 "Monster",
@@ -10684,66 +10693,66 @@
                 "classification",
                 "benefits"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Commercially Available Staffing Solution (CASS) - Award - Monster Hiring Management Enterprise (MHME)"
         },
-            "identifier": "MGMT-OCHCO-MHME-CASS",
+        {
             "accessLevel": "public",
             "bureauCode": [
-                "024:010"
-            ],
-            "programCode": [
-                "024:000"
+                "024:054"
             ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "pqwt01",
             "description": "Contains the historical preclearance queue wait times (in minutes)for the selected Airport and Date range. This information can be downloaded to a pdf file.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "http://pqt.cbp.gov/"
+                }
+            ],
+            "identifier": "CBP-000162",
             "keyword": [
                 "Airport",
                 "Preclearance",
                 "Queue",
                 "Wait Times"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:24-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "BEMSD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "pqwt01"
         },
-            "identifier": "CBP-000162",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:054"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "http://pqt.cbp.gov/"
-                }
-            ]
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "U.S. Customs and Border Protection Import Trade Trends - FY 2010, Year-End Report",
             "description": "U.S. Customs and Border Protection is pleased to present the Import Trade Trends Report. This report is produced semiannually and features graphical analysis and trade highlights. While U.S. Census Bureau has been producing monthly trade statistics at the aggregate level, this report is designed to trace major trade patterns and their impact on CBP workload and initiatives.",
+            "identifier": "CBP-000208",
             "keyword": [
                 "Access",
                 "Admission",
@@ -10769,57 +10778,57 @@
                 "Trademark",
                 "Transactions"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-11-08T10:31:31-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "CSPD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "U.S. Customs and Border Protection Import Trade Trends - FY 2010, Year-End Report"
         },
-            "identifier": "CBP-000208",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:054"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Mapping",
             "description": "Microsoft Bing Maps consisting of Satellite images, Road Maps, and Address Queries",
+            "identifier": "CBP-000232",
             "keyword": [
                 "Map"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:24-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Microsoft"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Mapping"
         },
-            "identifier": "CBP-000232",
-            "accessLevel": "public",
+        {
+            "accessLevel": "restricted public",
             "bureauCode": [
                 "024:054"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "CBP Revenue Collection Common Integration Framework Master Dataset",
             "description": "Port Point of Sale data including Vessels, Broker Agents, credit card information, and maritime commercial enterprises.",
+            "identifier": "CBP-000062",
             "keyword": [
                 "Port of Entry",
                 "Revenue",
@@ -10836,2074 +10845,2074 @@
                 "Revenue Collection",
                 "Vessel Arrival"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-10-12T10:11:11-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "BEMSD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "CBP Revenue Collection Common Integration Framework Master Dataset"
         },
-            "identifier": "CBP-000062",
-            "accessLevel": "restricted public",
+        {
+            "accessLevel": "public",
             "bureauCode": [
                 "024:054"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Customs Trade Partnership Against Terrorism (C-TPAT) Training Registration",
             "description": "C-TPAT Training Registration web application that is tailored to support C-TPAT training seminars specifically targeted for CTPAT members. CTPAT partners improve the security of their supply chains pursuant to C-TPAT security criteria and provide incentives and benefits to include expedited processing of C-TPAT shipments to C-TPAT partners",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://apps.cbp.gov/ctpat_training_registration"
+                }
+            ],
+            "identifier": "CBP-000085",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:25-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "BEMSD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Customs Trade Partnership Against Terrorism (C-TPAT) Training Registration"
         },
-            "identifier": "CBP-000085",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:054"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "This dataset contains the online agreement information needs to share Trade information via a Trade VPN. When submitted, the data is sent in an email to the business owner.  The data is sent via SMTP.  Trade Internet Virtual Private Network (TVPN) is password protected software and documentation download area",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://apps.cbp.gov/ctpat_training_registration"
+                    "accessURL": "https://apps.cbp.gov/tvpn/tvpn.asp"
                 }
-            ]
-        },
-        {
-            "title": "eISA Acceptance Form",
-            "description": "This dataset contains the online agreement information needs to share Trade information via a Trade VPN. When submitted, the data is sent in an email to the business owner.  The data is sent via SMTP.  Trade Internet Virtual Private Network (TVPN) is password protected software and documentation download area",
+            ],
+            "identifier": "CBP-000091",
             "keyword": [
                 "Trade",
                 "Agreement",
                 "EISA",
                 "VPN"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-30T14:03:25-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "BEMSD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "eISA Acceptance Form"
         },
-            "identifier": "CBP-000091",
+        {
             "accessLevel": "public",
             "bureauCode": [
-                "024:054"
-            ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
-            "distribution": [
-                {
-                    "@type": "dcat:Distribution",
-                    "accessURL": "https://apps.cbp.gov/tvpn/tvpn.asp"
-                }
-            ]
+                "024:058"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "FLETC Mobile Application",
             "description": "This dataset provides a convenient source of aggregated information valuable to FLETC students, visitors, and staff during their stay at the FLETC. This includes information such as, student handbook, dining hall menus, bus routes, local information, and recreation schedules.",
+            "identifier": "FLETC-07616-MAPP-DIR01",
             "keyword": [
                 "meals schedules routes handbook"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-03-01T11:54:41-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
+            "rights": null,
+            "title": "FLETC Mobile Application"
+        },
+        {
+            "accessLevel": "non-public",
+            "bureauCode": [
+                "024:010"
+            ],
             "contactPoint": {
                 "@type": "vcard:Contact",
                 "fn": "Open Data (MGMT)",
                 "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-            "identifier": "FLETC-07616-MAPP-DIR01",
-            "accessLevel": "public",
-            "bureauCode": [
-                "024:058"
-            ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
-        },
-        {
-            "title": "ANSI Standards",
             "description": "Standards from the American National Standards Institute and other organizations whose standards have been adopted by ANSI.",
+            "identifier": "SDD-1",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "ANSI"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "ANSI Standards"
         },
-            "identifier": "SDD-1",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "EBSCO Business Source Complete",
             "description": "The world's definitive scholarly business database, that provides acces to a leading collection of bibliographic and full text business content.",
+            "identifier": "SDD-10",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "EBSCO"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "EBSCO Business Source Complete"
         },
-            "identifier": "SDD-10",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "EBSCO CINAHL Complete",
             "description": "The world\u2019s most comprehensive source of full-text for nursing and allied health journals. It's a definitive research tool for all areas of nursing and allied health literature.",
+            "identifier": "SDD-11",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "EBSCO"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "EBSCO CINAHL Complete"
         },
-            "identifier": "SDD-11",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "EBSCO Criminal Justice",
             "description": "Criminal Justice is the leading bibliographic database for criminal justice and criminology research. It provides cover-to-cover indexing and abstracts for hundreds of journals covering all related subjects, including forensic sciences, corrections, policing, criminal law and investigation.",
+            "identifier": "SDD-12",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "EBSCO"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "EBSCO Criminal Justice"
         },
-            "identifier": "SDD-12",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "EBSCO GreenFILE",
             "description": "Covers all aspects of human impact to the environment. Its collection of scholarly, government and general-interest titles includes content on global warming, green building, pollution, sustainable agriculture, renewable energy, recycling, and more.",
+            "identifier": "SDD-13",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "EBSCO"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "EBSCO GreenFILE"
         },
-            "identifier": "SDD-13",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "EBSCO Legal Collection",
             "description": "Contains full text for more than 250 of the world's most respected, scholarly law journals. Legal Collection is an authoritative source for information on current issues, studies, thoughts and trends of the legal world.",
+            "identifier": "SDD-14",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "EBSCO"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "EBSCO Legal Collection"
         },
-            "identifier": "SDD-14",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "EBSCO MEDLINE Complete",
             "description": "Provides authoritative medical information on medicine, nursing, dentistry, veterinary medicine, the health care system, pre-clinical sciences, and much more.",
+            "identifier": "SDD-15",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "EBSCO"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "EBSCO MEDLINE Complete"
         },
-            "identifier": "SDD-15",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "EBSCO Regional Business News",
             "description": "Provides comprehensive full text coverage for regional business publications.",
+            "identifier": "SDD-16",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "EBSCO"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "EBSCO Regional Business News"
         },
-            "identifier": "SDD-16",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "EBSCO Discovery Service",
             "description": "Provides a platform for users to search and access the DHS Library resources.",
+            "identifier": "SDD-17",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "EBSCO"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "EBSCO Discovery Service"
         },
-            "identifier": "SDD-17",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Gale Virtual Reference Library",
             "description": "Leadership, Diversity & Inclusion and Cyber Security eBook Collections.",
+            "identifier": "SDD-18",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Gale"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Gale Virtual Reference Library"
         },
-            "identifier": "SDD-18",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Health Security Journal",
             "description": "Health Security is a peer-reviewed journal that explores the issues posed by disease outbreaks and epidemics; natural disasters; biological, chemical, and nuclear accidents or deliberate threats; foodborne outbreaks; and other health emergencies.",
+            "identifier": "SDD-19",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Mary Ann Liebert, Inc."
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Health Security Journal"
         },
-            "identifier": "SDD-19",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
-                "024:010"
-            ],
-            "programCode": [
-                "024:000"
+                "024:010"
             ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Associated Press Stylebook",
             "description": "AP Styleguide is a must-have reference for writers, editors, students, and professionals.  It provides fundamental guidelines for spelling, language, punctuation, usage, and journalistic style.",
+            "identifier": "SDD-2",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Associated Press"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Associated Press Stylebook"
         },
-            "identifier": "SDD-2",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "IEEE Explore Electronic Library",
             "description": "The IEEE Electronic Library (IEL) provides fulltext access to all IEEE-sponsored conference proceedings, journals, transactions as well as active IEEE standards.",
+            "identifier": "SDD-20",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "IEEE"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "IEEE Explore Electronic Library"
         },
-            "identifier": "SDD-20",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "IHS Engineering Workbench",
             "description": "World's largest collection of continuously updated engineering and technical reference documents from over 400 standards developing organizations and publishers.",
+            "identifier": "SDD-21",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "IHS Markit"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "IHS Engineering Workbench"
         },
-            "identifier": "SDD-21",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Janes",
             "description": "Janes digital collection that provides \u200baccess to: Fighting Ships,  Military and Security Assessments, Terrorism and Insurgency Centre,  Intelligence Events,  Data Analytics, Defence News, Security News and Transportation Library.",
+            "identifier": "SDD-22",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Janes"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Janes"
         },
-            "identifier": "SDD-22",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Leadership Connect",
             "description": "Congressional, Federal, State and Municipal Yellow Books online has transitioned to a new online platform called Leadership Connect. The new platform provides an easier search experience, more detailed profiles, weekly briefings, and a robust networking tool.",
+            "identifier": "SDD-23",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Unspecified"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Leadership Connect"
         },
-            "identifier": "SDD-23",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "NFPA Codes",
             "description": "National Fire Protection Association provides online access to more than 3000 consensus codes and facility standards in the areas of electrical safety, fire alarms and sprinkler systems.",
+            "identifier": "SDD-24",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "NFPA"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NFPA Codes"
         },
-            "identifier": "SDD-24",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "ProQuest Congressional",
             "description": "The single most comprehensive database for federal legislative history research. We recommend using the Advanced Search or if you want to search using citations to public laws, bills, or legislative history documents -- using the very precise Search by Number feature.",
+            "identifier": "SDD-25",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "ProQuest"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "ProQuest Congressional"
         },
-            "identifier": "SDD-25",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "ProQuest Digital National Security Archive",
             "description": "ProQuest, in partnership with The National Security Archive produces the Digital National Security Archive, the most comprehensive collection available of significant primary documents central to U.S. foreign and military policy since 1945. Collections cover the most critical world events, countries, and U.S. policy decisions from post-World War II through the 21st century.",
+            "identifier": "SDD-26",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "ProQuest"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "ProQuest Digital National Security Archive"
         },
-            "identifier": "SDD-26",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "ProQuest Legislative Insight 1789-2012",
             "description": "Select collections of U.S. government documents 1789 -2012 with workflow functionality to facilitate research, and learning involving historic and current legislative, judicial, and executive branch materials. Content is made accessible through a user-friendly, dynamic workspace allowing for easy, in-depth discovery.",
+            "identifier": "SDD-27",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "ProQuest"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "ProQuest Legislative Insight 1789-2012"
         },
-            "identifier": "SDD-27",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "ProQuest Legislative Insight 2013-forward",
             "description": "Comprehensive database of legislative histories. Each history includes the full text of the public law itself, all versions of related bills, law-specific Congressional Record excerpts, committee hearings, reports, and prints.",
+            "identifier": "SDD-28",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "ProQuest"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "ProQuest Legislative Insight 2013-forward"
         },
-            "identifier": "SDD-28",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "ProQuest Military Database",
             "description": "Specialized database that focuses on Homeland Security and terrorism topics across all government and military branches, including international relations, political science, criminology, defense, aeronautics and space flight, communications, civil engineering, and more.",
+            "identifier": "SDD-29",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "ProQuest"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "ProQuest Military Database"
         },
-            "identifier": "SDD-29",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "ASTM International",
             "description": "ASTM provides access to industry consensus standards ranging from aviation safety to fiber optic cable installations in underground utilities.",
+            "identifier": "SDD-3",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "ASTM"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "ASTM International"
         },
-            "identifier": "SDD-3",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "ProQuest Trends & Policy: U.S. Immigration",
             "description": "Trends and Policy: U.S. Immigration simplifies the discovery process by providing a single location to cross-search relevant documents from 1790-today. These include U.S. immigration laws and other content from the legislative branch, reports and statistics from the executive and judicial branches and news content to provide additional information and context.",
+            "identifier": "SDD-30",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "ProQuest"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "ProQuest Trends & Policy: U.S. Immigration"
         },
-            "identifier": "SDD-30",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Proquest US Newsstream",
             "description": "Content features newspapers, newswires, blogs, and news sites which are considered key national and regional news sources. Users can search the most recent premium U.S. news content, as well as archives back to the 1980s.",
+            "identifier": "SDD-31",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "ProQuest"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Proquest US Newsstream"
         },
-            "identifier": "SDD-31",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "ScienceDirect",
             "description": "Built on the widest range of trusted, high-quality, interdisciplinary research, ScienceDirect helps you find answers to your most pressing research questions, and stay on top of your field.",
+            "identifier": "SDD-32",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "ScienceDirect"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "ScienceDirect"
         },
-            "identifier": "SDD-32",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "SPIE Digital Library",
             "description": "SPIE, the international society for optics and photonics, was founded in 1955 as a non-profit organization to advance research in  light-based technologies.  This database calls itself the largest collection of applied optics & photonics research, and includes access to SPIE proceedings, journals, and eBooks.  It also has topic collections for those who prefer to browse for information on a particular research subject rather than search. http://spiedigitallibrary.org/index.aspx",
+            "identifier": "SDD-33",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "SPIE"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "SPIE Digital Library"
         },
-            "identifier": "SDD-33",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "SpringerLink",
             "description": "Provides researchers with access to millions of scientific documents from journals, books, series, protocols, reference works and proceedings.",
+            "identifier": "SDD-34",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Springer"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "SpringerLink"
         },
-            "identifier": "SDD-34",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Underwriters Laboratories (UL)",
             "description": "Provides UL Standards and related documents in PDF and/or HTML format. Related documents are Outlines of Investigations, Bulletins, CSDS Proposals, Certification Requirement Decisions and Practical Application Guidelines. To request an account, please go to https://dhs.servicenowservices.com/aal.",
+            "identifier": "SDD-35",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "UL"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Underwriters Laboratories (UL)"
         },
-            "identifier": "SDD-35",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "USCG Incorporation by Reference (IBR) Library",
             "description": "The United States Coast Guard (USCG) Incorporation by Reference (IBR) Library provides users with access to standards that are currently incorporated by reference in USCG regulations found in Titles 33 and 46 of the Code of Federal Regulations (CFR). Organized by CFR Title and Part, the IBR Library houses IBR standards in one place, allowing users to quickly and easily locate these mission-critical standards.",
+            "identifier": "SDD-36",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS Library"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "USCG Incorporation by Reference (IBR) Library"
         },
-            "identifier": "SDD-36",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Westlaw",
             "description": "Comprehensive legal, tax, public records and business information. Includes Personnet, a service covering all up-to-date laws, rules and regulations specific to human capital. http://legalsolutions.thomsonreuters.com/law-products/ns/government/homeland-security/westlaw",
+            "identifier": "SDD-37",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Thomson Reuters West Publishing"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Westlaw"
         },
-            "identifier": "SDD-37",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Worldcat OCLC",
             "description": "WorldCat is the world\u2019s most comprehensive database of information about library collections.",
+            "identifier": "SDD-38",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Worldcat"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Worldcat OCLC"
         },
-            "identifier": "SDD-38",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "New audio & e-books Research Guide",
             "description": "Discover the DHS Library's new audio and e-Books.",
+            "identifier": "SDD-39",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS Library"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "New audio & e-books Research Guide"
         },
-            "identifier": "SDD-39",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Big Data Journal",
             "description": "\u200bThe leading peer-reviewed journal covering the challenges and opportunities in collecting, analyzing, and disseminating vast amounts of data.",
+            "identifier": "SDD-4",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Mary Ann Liebert, Inc."
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Big Data Journal"
         },
-            "identifier": "SDD-4",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Chemical, Biological, Radiological, and Nuclear (CBRN) Research Guide",
             "description": "This guide will provide resources on Chemical, Biological, Radiological and Nuclear Warfare. This research guide is not a comprehensive listing of sources, but is intended to be a starting point from which employees can begin their research according to their specific needs. It is intended to serve those interested in CBRN.",
+            "identifier": "SDD-40",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS Library"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Chemical, Biological, Radiological, and Nuclear (CBRN) Research Guide"
         },
-            "identifier": "SDD-40",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "COVID-19 Research Guide",
             "description": "This is a collection of information and resources relating to the novel coronavirus. This guide is dynamic \u200band will be updated as new resources become available\u200b.  It is intended to serve those interested in the illness caused by the novel coronavirus, Covid-19, or SARS-CoV-2. The selected sources are not comprehensive, they are a quick guide intended to help you get started with your research.",
+            "identifier": "SDD-41",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS Library"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "COVID-19 Research Guide"
         },
-            "identifier": "SDD-41",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Supply Chain Research Guide",
             "description": "Guide to approaches and secondary resources for researching supply chains.",
+            "identifier": "SDD-42",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS Library"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Supply Chain Research Guide"
         },
-            "identifier": "SDD-42",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Visa Waiver Program (VWP) Research Guide",
             "description": "Resources specific to Visa Waiver Program Countries. The Visa Waiver Program (VWP), administered by the Department of Homeland Security (DHS) in consultation with the State Department, permits citizens of 40 countries to travel to the United States for business or tourism for stays of up to 90 days without a visa.  In return, those 40 countries must permit U.S. citizens and nationals to travel to their countries for a similar length of time without a visa for business or tourism purposes.",
+            "identifier": "SDD-43",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS Library"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Visa Waiver Program (VWP) Research Guide"
         },
-            "identifier": "SDD-43",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Mindfulness Research Guide",
             "description": "Resources for meditation and mindfulness practices.",
+            "identifier": "SDD-44",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS Library"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Mindfulness Research Guide"
         },
-            "identifier": "SDD-44",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Inclusive Diversity Research Guide",
             "description": "Commitment to Inclusive DiversityrnThe DHS Library, along with the DHS Strategic Recruitment Diversity and Inclusion Office, has developed a collection of resources focused specifically on diversity, equity, and inclusion. DHS is committed to providing an inclusive and diverse work place and we hope to provide you with starting points for your research as well as some of the key resources that should allow you to find books, articles, primary sources, and data.",
+            "identifier": "SDD-45",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS Library"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Inclusive Diversity Research Guide"
         },
-            "identifier": "SDD-45",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Leadership Research Guide",
             "description": "This guide will provide resources on Leadership and Communication. This research guide is not a comprehensive listing of sources, but is intended to be a starting point from which employees can begin their research according to their specific needs. https://dhs-gov.libguides.com/c.php?g=1047434",
+            "identifier": "SDD-46",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS Library"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Leadership Research Guide"
         },
-            "identifier": "SDD-46",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Finding Government Information Research Guide",
             "description": "This guide brings together online resources that contain U.S. government documents. Some are freely available to anyone with Internet access. Others include subscription databases accessible with a DHS device.",
+            "identifier": "SDD-47",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS Library"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Finding Government Information Research Guide"
         },
-            "identifier": "SDD-47",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Artificial Intelligence Research Guide",
             "description": "This is a collection of information and resources relating to artificial intelligence.",
+            "identifier": "SDD-48",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS Library"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Artificial Intelligence Research Guide"
         },
-            "identifier": "SDD-48",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "National Library Week 2022 Guide",
             "description": "This guide is your one-stop-shop for everything National Library Week. NLW is a time to highlight the essential role libraries, librarians and library workers play in strengthening communities and connecting users with essential information.",
+            "identifier": "SDD-49",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS Library"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "National Library Week 2022 Guide"
         },
-            "identifier": "SDD-49",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "CLEAR",
             "description": "CLEAR has public record information and is also used for law enforcement and investigations, including personal identification and financial records, police reports, and credential verification services.",
+            "identifier": "SDD-5",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Thomson Reuters West Publishing"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "CLEAR"
         },
-            "identifier": "SDD-5",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "AskaLibrarian Service Portal",
             "description": "This portal, hosted by ServiceNow and managed by the DHS Library, allows users to submit and track requests for assistance.",
+            "identifier": "SDD-50",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS Library"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "AskaLibrarian Service Portal"
         },
-            "identifier": "SDD-50",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "SDD Compliance Documentation Repository",
             "description": "A reference repository of all compliance documentation for SDD programs, including privacy threshold analyses (PTAs), privacy impact analyses (PIAs), Systems of Record Notices (SORN), etc. For use by SDD programs; not the record copies.",
+            "identifier": "SDD-51",
             "keyword": [
                 "compliance",
                 "PTA",
                 "PIA",
                 "SORN"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "SGD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "SDD Compliance Documentation Repository"
         },
-            "identifier": "SDD-51",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "DHS Libraries Catalog",
             "description": "Find books, journals, and other materials held by libraries within DHS.  After clicking the link, please select the option DHS group catalog from the IN drop-down menu to search the DHS Catalog.",
+            "identifier": "SDD-6",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS Library"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "DHS Libraries Catalog"
         },
-            "identifier": "SDD-6",
-            "accessLevel": "non-public",
+        {
+            "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "DHS.gov",
             "description": "DHS.gov hosts websites for the DHS enterprise, including all administrative and operational components.",
+            "identifier": "SDD-64",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS.gov Team"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "DHS.gov"
         },
-            "identifier": "SDD-64",
-            "accessLevel": "public",
+        {
+            "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "DHS Precheck",
             "description": "Enables DHS employees to opt in to join the TSA Precheck program and receive expedited screening\u2014at no additional cost to employees\u2014for both their official and personal air travel.",
+            "identifier": "SDD-65",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "DHS Precheck Team"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "DHS Precheck"
         },
-            "identifier": "SDD-65",
-            "accessLevel": "non-public",
+        {
+            "accessLevel": "restricted public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Emerald",
             "description": "Enterprise Media Repository and Library for Distribution (EMERALD) is the DHS-wide enterprise solution for public affairs imagery.",
+            "identifier": "SDD-66",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Emerald Team"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Emerald"
         },
-            "identifier": "SDD-66",
+        {
             "accessLevel": "restricted public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "GovDelivery",
             "description": "GovDelivery is a web-based e-mail subscription management system that allows a member of the public (user) to subscribe to news and information on DHS websites.",
+            "identifier": "SDD-67",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "GovDelivery Team"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "GovDelivery"
         },
-            "identifier": "SDD-67",
-            "accessLevel": "restricted public",
+        {
+            "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Web Content Management as a Service",
             "description": "Hosts web space and provides WCMaaS support to the DHS enterprise.",
+            "identifier": "SDD-68",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Web Content Management as a Service Program"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Web Content Management as a Service"
         },
-            "identifier": "SDD-68",
-            "accessLevel": "non-public",
+        {
+            "accessLevel": "restricted public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Ideascale",
             "description": "Idea community - open government initiative; run dialogs",
+            "identifier": "SDD-69",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Ideascale Team"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Ideascale"
         },
-            "identifier": "SDD-69",
-            "accessLevel": "restricted public",
+        {
+            "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Dun and Bradstreet",
             "description": "Information on 75 million firms around the world.",
+            "identifier": "SDD-7",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "Dun and Bradstreet"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Dun and Bradstreet"
         },
-            "identifier": "SDD-7",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "EBSCO Academic Search Complete",
             "description": "Academic Search Complete is the world's most valuable and comprehensive scholarly, multi-disciplinary full-text database, with more than 8,500 full-text periodicals, including more than 7,300 peer-reviewed journals.",
+            "identifier": "SDD-8",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "EBSCO"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "EBSCO Academic Search Complete"
         },
-            "identifier": "SDD-8",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "ServiceNow",
             "description": "Platform service that enables teams to manage digital workflows for enterprise operations.",
+            "identifier": "SDD-83",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "BSD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "ServiceNow"
         },
-            "identifier": "SDD-83",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "CATT",
             "description": "Manage your organization's Correspondence and Tasks with this turn-key solution. Use built-in business intelligence capabilities to visualize your data. Find and extract data. Create charts, dashboards, and reports. Drill down using interactive views and filters to support your business decisions.",
+            "identifier": "SDD-84",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "BSD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "CATT"
         },
-            "identifier": "SDD-84",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "J-TIMS (Joint Threat Information Management System)",
             "description": "DHS case management system, known as the Joint Threat Information Management System (J-TIMS) to track the full lifecycle of an allegation from intake, through DHS OIG referral, investigation, and eventual case disposition",
+            "identifier": "SDD-85",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "BSD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "J-TIMS (Joint Threat Information Management System)"
         },
-            "identifier": "SDD-85",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Enterprise Portfolio Tracker (EPT)",
             "description": "Manage your portfolio of project through the full lifecycle with Portfolio Tracker's Intake, MOA, and Project modules. In addition, track your organization's Risks and Issues and their impact on your projects. Reporting and analysis are a breeze with the tailored views, charts, graphs, and quad report.",
+            "identifier": "SDD-86",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "BSD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Enterprise Portfolio Tracker (EPT)"
         },
-            "identifier": "SDD-86",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Operation Vaccinate Our Workforce (OVOW)",
             "description": "The OVOW system was developed to identify and prioritize COVID-19 vaccine allocations for DHS frontline personnel for whom teleworking is not an option.",
+            "identifier": "SDD-87",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "BSD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Operation Vaccinate Our Workforce (OVOW)"
         },
-            "identifier": "SDD-87",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Vaccination Status System (VSS)",
             "description": "The VSS system provides federal civilian employees the ability to report their vaccination status and provide proof of vaccination.",
+            "identifier": "SDD-88",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "BSD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Vaccination Status System (VSS)"
         },
-            "identifier": "SDD-88",
-            "accessLevel": "non-public",
+        {
+            "accessLevel": "restricted public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Family Reunification Task Force (FRTF)",
             "description": "Application to to identify and reunite certain families who were separated by the United States (U.S.) government between January 20, 2017 and January 20, 2021.",
+            "identifier": "SDD-89",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "BSD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Family Reunification Task Force (FRTF)"
         },
-            "identifier": "SDD-89",
-            "accessLevel": "restricted public",
+        {
+            "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "EBSCO Applied Science & Technology Source Ultimate",
             "description": "Provides STEM students and researchers with the resources they need to succeed. Provides coverage of a wide range of topics: artificial intelligence, applied mathematics, plastics, hydroponics, computer science, chemical engineering, energy resources and robotics, as well as the business and social implications of new technologies.",
+            "identifier": "SDD-9",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "EBSCO"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "EBSCO Applied Science & Technology Source Ultimate"
         },
-            "identifier": "SDD-9",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Hummingbird",
             "description": "Hummingbird (HB) is a ServiceNow case management custom application being used to manage Afghan refugee processing and resettlement activities.  HB acts as a Check list/ status tool helping to ensure all required steps are taken in the process.",
+            "identifier": "SDD-90",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "BSD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Hummingbird"
         },
-            "identifier": "SDD-90",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "IDP",
             "description": "Gym access waiver data",
+            "identifier": "SDD-91",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "BSD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "IDP"
         },
-            "identifier": "SDD-91",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Migrant Protection Protocol (MPP)",
             "description": "The MPP application is an intake system of record. The submissions from the Public facing interface will generate records. These records will provide the necessary information for individual cases for consideration for re-evaluation. Records will follow a life cycle of review based on qualifying conditions reported.",
+            "identifier": "SDD-92",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "BSD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Migrant Protection Protocol (MPP)"
         },
-            "identifier": "SDD-92",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Insight",
             "description": "Atlassian database personnel list and customer list",
+            "identifier": "SDD-93",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "PMD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Insight"
         },
-            "identifier": "SDD-93",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Business Solutions Tool",
             "description": "Collection of Solutions Development Directorate (SDD) Memoranda of Agreement (MOAs), Cost models, spend plans, contracts, purchase requisitions",
+            "identifier": "SDD-94",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "PMD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Business Solutions Tool"
         },
-            "identifier": "SDD-94",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Identity Services DHS Access ALM Training Site",
             "description": "Training resources for access lifecycle management; available to all administrative and operational components.",
+            "identifier": "SDD-95",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "ISB"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Identity Services DHS Access ALM Training Site"
         },
-            "identifier": "SDD-95",
+        {
             "accessLevel": "non-public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "PMD Resources SharePoint",
             "description": "SDD Front Office standard operating procedures, employee performance work plans, and templates",
+            "identifier": "SDD-96",
             "keyword": [
                 "none"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-03-31T12:47:43-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "PMD"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "PMD Resources SharePoint"
         },
-            "identifier": "SDD-96",
-            "accessLevel": "non-public",
+        {
+            "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Integrated Federal Employees' Compensation System (iFECS)",
             "description": "The integrated Federal Employees' Compensation System (iFECS) is a mission-critical steady state system that supports the Office of Workers' Compensation Programs' (OWCP) Division of Federal Employees' Compensation (DFEC). System capabilities include: processing injury claims, paying workers' compensation benefits, and supporting other financial and administrative activities for DFEC.",
+            "identifier": "MGMT-OCHCO-DOL-IFECS",
             "keyword": [
                 "DOL ECOMP",
                 "iFECS"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Integrated Federal Employees' Compensation System (iFECS)"
         },
-            "identifier": "MGMT-OCHCO-DOL-IFECS",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "National Finance Center Reporting Center",
             "description": "Generate custom reports from NFC",
+            "identifier": "MGMT-OCHCO-NFC-REPORTING_CENTER",
             "keyword": [
                 "Employee",
                 "NFC",
@@ -12911,404 +12920,410 @@
                 "EPP",
                 "Reporting"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "USDA"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "National Finance Center Reporting Center"
         },
-            "identifier": "MGMT-OCHCO-NFC-REPORTING_CENTER",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "OPM USAJobs",
             "description": "USAJobs is the official job site of the United States Federal Government. This website is the centralized site for most Federal agencies to post vacancy announcements.",
+            "identifier": "MGMT-OCHCO-OPM-USAJOBS",
             "keyword": [
                 "USAJobs"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-01-31T13:32:49-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "OPM"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "OPM USAJobs"
         },
-            "identifier": "MGMT-OCHCO-OPM-USAJOBS",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Workers Compensation - Medical Case Management Services (WC-MCMS)",
             "description": "Provides access to work on cases with nurses involved in workers compensation projects. The WC MCMS application is a case management system used for workers compensation claims. WC-MCMS is used by medical case workers for the processing of claims.",
+            "identifier": "MGMT-OCHCO-WC-MCMS",
             "keyword": [
                 "compensation",
                 "Medical Cases",
                 "nurses"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-03-06T14:55:05-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Workers Compensation - Medical Case Management Services (WC-MCMS)"
         },
-            "identifier": "MGMT-OCHCO-WC-MCMS",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:010"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "DHS - OCHCO Cybersecurity Talent Management Systems (CTMS)",
             "description": "To implement the Secretary's authority in 6 U.S.C. 658 which allows for the Cybersecurity Talent Management Systems (CTMS), the Department of Homeland Security (DHS) must build and maintain a team with technical knowledge related to Federal human capital policy, compensation design and administration, labor market analysis, psychometric research, assessment development, and agency-wide workforce change management. As reinforced by Executive Order 13800: Strengthening the Cybersecurity of Federal Networks and Critical Infrastructure, DHS has a lead role in securing the Federal Government and the Nation against cybersecurity threats. CTMS reimagines Federal human capital management to allow DHS to compete for top talent in the ever-changing field of cybersecurity and to execute the Department's cybersecurity mission.",
+            "identifier": "MGMT-OCHCO-CTMS-CYBERTALENT",
             "keyword": [
                 "Cyber",
                 "Talent",
                 "Management",
                 "System"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-06-13T15:08:13-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "MGMT"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "DHS - OCHCO Cybersecurity Talent Management Systems (CTMS)"
         },
-            "identifier": "MGMT-OCHCO-CTMS-CYBERTALENT",
+        {
             "accessLevel": "public",
             "bureauCode": [
-                "024:010"
-            ],
-            "programCode": [
-                "024:000"
+                "000:000"
             ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Federal Agency Bureau Codes",
             "description": "A list of 4-digit GSA federal agency bureau codes used to identify federal agencies. The primary source is the GSA published list.",
+            "identifier": "FPS-13000",
             "keyword": [
                 "agency codes",
                 "agency bureau codes"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-04-27T08:06:59-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "GSA"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Federal Agency Bureau Codes"
         },
-            "identifier": "FPS-13000",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "000:000"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Buildings/Federal Facilities",
             "description": "Information for GSA owned or leased federal facilities and tenant agencies across the United States.",
+            "identifier": "FPS-13001",
             "keyword": [
                 "buildings",
                 "GSA buildings",
                 "facilities",
                 "GSA facilities"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-04-27T08:06:59-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "GSA"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Buildings/Federal Facilities"
         },
-            "identifier": "FPS-13001",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "000:000"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Federal Agency Bureau Codes",
             "description": "A list of 4-digit GSA federal agency bureau codes used to identify federal agencies. The primary source is the GSA published list.",
+            "identifier": "FPS-14000",
             "keyword": [
                 "agency codes",
                 "agency bureau codes"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-04-27T08:09:16-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "GSA"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Federal Agency Bureau Codes"
         },
-            "identifier": "FPS-14000",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "000:000"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Buildings/Federal Facilities",
             "description": "Information for GSA owned or leased federal facilities and tenant agencies across the United States.  Includes FPS District and FPS Area of building location provided by FPS.",
+            "identifier": "FPS-14001",
             "keyword": [
                 "buildings",
                 "GSA buildings",
                 "facilities",
                 "GSA facilities"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-04-27T08:09:16-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "GSA"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Buildings/Federal Facilities"
         },
-            "identifier": "FPS-14001",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "000:000"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "GSA Regions",
             "description": "A GSA designated geographical segment of the United States represented by a number 1-11.  Federal Facilities are geographically grouped by regions.",
+            "identifier": "FPS-14003",
             "keyword": [
                 "region"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-04-27T08:09:16-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "GSA"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "GSA Regions"
         },
-            "identifier": "FPS-14003",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "000:000"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "Buildings/Federal Facilities",
             "description": "Information for GSA owned or leased federal facilities and tenant agencies across the United States.",
+            "identifier": "FPS-12001",
             "keyword": [
                 "buildings",
                 "GSA buildings",
                 "facilities",
                 "GSA facilities"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-04-27T08:13:56-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "GSA"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "Buildings/Federal Facilities"
         },
-            "identifier": "FPS-12001",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "000:000"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "NIBRS Codes",
             "description": "National Incident-Based Reporting System (NIBRS) codes used to adequately categorize criminal offenses with details needed to meet national law enforcement criminal reporting requirements across all law enforcement agencies.",
+            "identifier": "FPS-12033",
             "keyword": [
                 "NIBRS"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-04-27T08:13:56-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "CJIS"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "NIBRS Codes"
         },
-            "identifier": "FPS-12033",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "000:000"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "GSA Regions",
             "description": "A GSA designated geographical segment of the United States represented by a number 1-11.  Federal Facilities are geographically grouped by regions.",
+            "identifier": "FPS-12003",
             "keyword": [
                 "region"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-04-27T08:13:56-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "GSA"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "GSA Regions"
         },
-            "identifier": "FPS-12003",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "000:000"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "GSA Service Centers",
             "description": "List of GSA Service Centers who manage groups of federal facilities.",
+            "identifier": "FPS-12006",
             "keyword": [
                 "GSA Service Centers"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2022-04-27T08:13:56-04:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "GSA"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "GSA Service Centers"
         },
-            "identifier": "FPS-12006",
+        {
             "accessLevel": "public",
             "bureauCode": [
-                "000:000"
-            ],
-            "programCode": [
-                "024:000"
+                "024:056"
             ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
             },
-        {
-            "title": "TSA Confirmed COVID-19 Cases",
             "description": "Dataset contains total number of confirmed COVID-19 cases for all employees to include screening and non-screening employees at each airport.",
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "accessURL": "https://www.tsa.gov/coronavirus#c19table"
+                }
+            ],
+            "identifier": "TSA-11d97804-7d62-4620-83e7-f0bbaca57c5b",
             "keyword": [
                 "Airport",
                 "COVID-19 Cases"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-22T12:25:28-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "TSA.GOV Public Website"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "TSA Confirmed COVID-19 Cases"
         },
-            "identifier": "TSA-11d97804-7d62-4620-83e7-f0bbaca57c5b",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Dataset contains statements, press releases, testimonies, and factsheets produced by the Office of Strategic Communications & Public Affairs.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.tsa.gov/coronavirus#c19table"
+                    "accessURL": "https://www.tsa.gov/news/press/releases"
                 }
-            ]
-        },
-        {
-            "title": "TSA Press Releases",
-            "description": "Dataset contains statements, press releases, testimonies, and factsheets produced by the Office of Strategic Communications & Public Affairs.",
+            ],
+            "identifier": "TSA-7a95dae1-44b8-4e61-9f27-065219de01d3",
             "keyword": [
                 "PR",
                 "Press Releases",
@@ -13317,918 +13332,912 @@
                 "Factsheets",
                 "Statements"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-22T12:25:28-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "TSA.GOV Public Website"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "TSA Press Releases"
         },
-            "identifier": "TSA-7a95dae1-44b8-4e61-9f27-065219de01d3",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "The TSA.gov site map dataset contains all publicly accessible URLs within tsa.gov in XML representation. The dataset is intended to assist search engine crawlers in indexing all pages within a website and includes the URLs, update interval, last modification date, and a link to any images associated with a page or article.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.tsa.gov/news/press/releases"
+                    "accessURL": "https://www.tsa.gov/sitemap.xml"
                 }
-            ]
-        },
-        {
-            "title": "TSA.gov Site Map",
-            "description": "The TSA.gov site map dataset contains all publicly accessible URLs within tsa.gov in XML representation. The dataset is intended to assist search engine crawlers in indexing all pages within a website and includes the URLs, update interval, last modification date, and a link to any images associated with a page or article.",
+            ],
+            "identifier": "TSA-513b330b-171f-43c6-9ed4-e0ff60e1d697",
             "keyword": [
                 "Sitemaps",
                 "XML"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-22T12:25:28-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "TSA.GOV Public Website"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "TSA.gov Site Map"
         },
-            "identifier": "TSA-513b330b-171f-43c6-9ed4-e0ff60e1d697",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Contains the number of firearm discoveries at the top 10 airports nationwide for 2020.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.tsa.gov/sitemap.xml"
+                    "accessURL": "https://www.tsa.gov/news/press/releases/2021/01/26/tsa-firearm-catch-rate-doubles-2020-highest-agencys-19-year-history"
                 }
-            ]
-        },
-        {
-            "title": "TSA Firearm Catches by Airport 2020",
-            "description": "Contains the number of firearm discoveries at the top 10 airports nationwide for 2020.",
+            ],
+            "identifier": "TSA-336009e4-7d32-4c58-b865-93f5ae944455",
             "keyword": [
                 "Firearms",
                 "Guns"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-22T12:25:28-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "TSA.GOV Public Website"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "TSA Firearm Catches by Airport 2020"
         },
-            "identifier": "TSA-336009e4-7d32-4c58-b865-93f5ae944455",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Contains the number of firearm discoveries at the top 10 airports nationwide for 2019.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.tsa.gov/news/press/releases/2021/01/26/tsa-firearm-catch-rate-doubles-2020-highest-agencys-19-year-history"
+                    "accessURL": "https://www.tsa.gov/blog/2020/01/15/tsa-year-review-2019"
                 }
-            ]
-        },
-        {
-            "title": "TSA Firearm Catches by Airport 2019",
-            "description": "Contains the number of firearm discoveries at the top 10 airports nationwide for 2019.",
+            ],
+            "identifier": "TSA-58ddee9f-14b6-40de-8fc7-8755709bbd7b",
             "keyword": [
                 "Firearms",
                 "Guns"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-22T12:25:28-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "TSA.GOV Public Website"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "TSA Firearm Catches by Airport 2019"
         },
-            "identifier": "TSA-58ddee9f-14b6-40de-8fc7-8755709bbd7b",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Contains the number of firearm discoveries at the top 10 airports nationwide for 2018.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.tsa.gov/blog/2020/01/15/tsa-year-review-2019"
+                    "accessURL": "https://www.tsa.gov/blog/2019/02/07/tsa-year-review-record-setting-2018"
                 }
-            ]
-        },
-        {
-            "title": "TSA Firearm Catches by Airport 2018",
-            "description": "Contains the number of firearm discoveries at the top 10 airports nationwide for 2018.",
+            ],
+            "identifier": "TSA-cad2e96e-f6e7-4234-be75-f6bec7d0fb3a",
             "keyword": [
                 "Firearms",
                 "Guns"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-22T12:25:28-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "TSA.GOV Public Website"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "TSA Firearm Catches by Airport 2018"
         },
-            "identifier": "TSA-cad2e96e-f6e7-4234-be75-f6bec7d0fb3a",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Contains the number of firearm discoveries at the top 10 airports nationwide for 2017.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.tsa.gov/blog/2019/02/07/tsa-year-review-record-setting-2018"
+                    "accessURL": "https://www.tsa.gov/blog/2018/01/29/tsa-year-review-record-amount-firearms-discovered-2017"
                 }
-            ]
-        },
-        {
-            "title": "TSA Firearm Catches by Airport 2017",
-            "description": "Contains the number of firearm discoveries at the top 10 airports nationwide for 2017.",
+            ],
+            "identifier": "TSA-96418ed5-d19a-4384-a4e8-f8dee69218a0",
             "keyword": [
                 "Firearms",
                 "Guns"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-22T12:25:28-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "TSA.GOV Public Website"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "TSA Firearm Catches by Airport 2017"
         },
-            "identifier": "TSA-96418ed5-d19a-4384-a4e8-f8dee69218a0",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "Contains the number of firearm discoveries at the top 10 airports nationwide for 2016.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.tsa.gov/blog/2018/01/29/tsa-year-review-record-amount-firearms-discovered-2017"
+                    "accessURL": "https://www.tsa.gov/blog/2017/01/12/tsa-year-review-record-amount-firearms-discovered-2016"
                 }
-            ]
-        },
-        {
-            "title": "TSA Firearm Catches by Airport 2016",
-            "description": "Contains the number of firearm discoveries at the top 10 airports nationwide for 2016.",
+            ],
+            "identifier": "TSA-76ce1d54-ee29-4357-bde1-26326cb5cd87",
             "keyword": [
                 "Firearms",
                 "Guns"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-22T12:25:28-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "TSA.GOV Public Website"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "TSA Firearm Catches by Airport 2016"
         },
-            "identifier": "TSA-76ce1d54-ee29-4357-bde1-26326cb5cd87",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "This is the collection of data sets for the Freedom of Information Act - TSA Contact Center Traveler Complaints from February 2019 to present. FOIA requests posted to the FOIA electronic reading room for the TSA Contact Center Traveler Complaints category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "accessURL": "https://www.tsa.gov/blog/2017/01/12/tsa-year-review-record-amount-firearms-discovered-2016"
+                    "accessURL": "https://www.tsa.gov/foia/readingroom"
                 }
-            ]
-        },
-        {
-            "title": "FOIA - TSA Contact Center Traveler Complaints Data Asset",
-            "description": "This is the collection of data sets for the Freedom of Information Act - TSA Contact Center Traveler Complaints from February 2019 to present. FOIA requests posted to the FOIA electronic reading room for the TSA Contact Center Traveler Complaints category.",
+            ],
+            "identifier": "TSA-142a1d3d-ccb7-4827-9183-25b57a357354",
             "keyword": [
                 "Airport",
                 "FOIA",
                 "TCC",
                 "Complaints"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-22T12:25:27-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FOIA Electronic Reading Room"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "FOIA - TSA Contact Center Traveler Complaints Data Asset"
         },
-            "identifier": "TSA-142a1d3d-ccb7-4827-9183-25b57a357354",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "FOIA requests posted to the FOIA electronic reading room for the TSA Contact Center Quarterly Reports from FY 2017 Quarter 1 to present.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.tsa.gov/foia/readingroom"
                 }
-            ]
-        },
-        {
-            "title": "FOIA - TSA Contact Center Quarterly Reports",
-            "description": "FOIA requests posted to the FOIA electronic reading room for the TSA Contact Center Quarterly Reports from FY 2017 Quarter 1 to present.",
+            ],
+            "identifier": "TSA-b45e7a14-666e-444f-ac25-f45ddb95611f",
             "keyword": [
                 "Airport",
                 "TCC Complaints",
                 "Quarterly",
                 "TSA Contact Center"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-22T12:25:27-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FOIA Electronic Reading Room"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "FOIA - TSA Contact Center Quarterly Reports"
         },
-            "identifier": "TSA-b45e7a14-666e-444f-ac25-f45ddb95611f",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "FOIA requests posted to the FOIA electronic reading room for the TSA Contact Center Annual Reports from FY 2018 to present.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.tsa.gov/foia/readingroom"
                 }
-            ]
-        },
-        {
-            "title": "FOIA - TSA Contact Center Fiscal Year Reports",
-            "description": "FOIA requests posted to the FOIA electronic reading room for the TSA Contact Center Annual Reports from FY 2018 to present.",
+            ],
+            "identifier": "TSA-7671b3a2-00c4-4d1a-8e32-cf4cb5540440",
             "keyword": [
                 "Airports",
                 "TCC",
                 "Complaints",
                 "Year"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-22T12:25:27-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FOIA Electronic Reading Room"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "FOIA - TSA Contact Center Fiscal Year Reports"
         },
-            "identifier": "TSA-7671b3a2-00c4-4d1a-8e32-cf4cb5540440",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "FOIA requests posted to the FOIA electronic reading room for TSA Throughput from February 5, 2017 to present.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.tsa.gov/foia/readingroom"
                 }
-            ]
-        },
-        {
-            "title": "FOIA - TSA Throughput",
-            "description": "FOIA requests posted to the FOIA electronic reading room for TSA Throughput from February 5, 2017 to present.",
+            ],
+            "identifier": "TSA-151f2c4e-64ed-4ce5-86ce-4fbee3d3e449",
             "keyword": [
                 "PMIS",
                 "FOIA",
                 "Throughput"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-22T12:25:27-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FOIA Electronic Reading Room"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "FOIA - TSA Throughput"
         },
-            "identifier": "TSA-151f2c4e-64ed-4ce5-86ce-4fbee3d3e449",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "FOIA requests posted to the FOIA electronic reading room for the FOIA requests about airports from August 2018 to present.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.tsa.gov/foia/readingroom"
                 }
-            ]
-        },
-        {
-            "title": "FOIA - Airports",
-            "description": "FOIA requests posted to the FOIA electronic reading room for the FOIA requests about airports from August 2018 to present.",
+            ],
+            "identifier": "TSA-d2c0f7d1-6ec1-43a9-9421-99f263f6eae6",
             "keyword": [
                 "Airports",
                 "FOIA",
                 "Freedom of Information Act"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-22T12:25:27-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FOIA Electronic Reading Room"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "FOIA - Airports"
         },
-            "identifier": "TSA-d2c0f7d1-6ec1-43a9-9421-99f263f6eae6",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "FOIA requests posted to the FOIA electronic reading room for the  Checkpoint category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.tsa.gov/foia/readingroom"
                 }
-            ]
-        },
-        {
-            "title": "FOIA - Checkpoint Requests",
-            "description": "FOIA requests posted to the FOIA electronic reading room for the  Checkpoint category.",
+            ],
+            "identifier": "TSA-740416db-ab9b-4837-a7cd-c85370aecebf",
             "keyword": [
                 "FOIA",
                 "Checkpoints"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-22T12:25:27-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FOIA Electronic Reading Room"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "FOIA - Checkpoint Requests"
         },
-            "identifier": "TSA-740416db-ab9b-4837-a7cd-c85370aecebf",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "FOIA requests posted to the FOIA electronic reading room for the Civil Enforcement Final Agency Decisions category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.tsa.gov/foia/readingroom"
                 }
-            ]
-        },
-        {
-            "title": "FOIA - Civil Enforcement Final Agency Decisions",
-            "description": "FOIA requests posted to the FOIA electronic reading room for the Civil Enforcement Final Agency Decisions category.",
+            ],
+            "identifier": "TSA-e3bd3bc3-0017-4ef7-87bf-0a564595493c",
             "keyword": [
                 "FOIA",
                 "Civil Rights",
                 "Civil Liberties"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-22T12:25:27-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FOIA Electronic Reading Room"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "FOIA - Civil Enforcement Final Agency Decisions"
         },
-            "identifier": "TSA-e3bd3bc3-0017-4ef7-87bf-0a564595493c",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
+            "description": "FOIA requests posted to the FOIA electronic reading room for the Civil Penalty and Civil Penalty Assessment Order category.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "https://www.tsa.gov/foia/readingroom"
                 }
-            ]
-        },
-        {
-            "title": "FOIA - Civil Penalty and Civil Penalty Assessment Order",
-            "description": "FOIA requests posted to the FOIA electronic reading room for the Civil Penalty and Civil Penalty Assessment Order category.",
+            ],
+            "identifier": "TSA-8c5cdca0-37cf-48d6-beec-be8a8aa0b123",
             "keyword": [
                 "FOIA",
                 "Civil Rights",
                 "Civil Liberties",
                 "Assessment"
             ],
+            "license": "https://www.usa.gov/government-works",
             "modified": "2024-02-22T12:25:27-05:00",
+            "programCode": [
+                "024:000"
+            ],
             "publisher": {
                 "@type": "org:Organization",
                 "name": "FOIA Electronic Reading Room"
             },
-            "contactPoint": {
-                "@type": "vcard:Contact",
-                "fn": "Open Data (MGMT)",
-                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            "rights": null,
+            "title": "FOIA - Civil Penalty and Civil Penalty Assessment Order"
         },
-            "identifier": "TSA-8c5cdca0-37cf-48d6-beec-be8a8aa0b123",
+        {
             "accessLevel": "public",
             "bureauCode": [
                 "024:056"
             ],
-            "programCode": [
-                "024:000"
-            ],
-            "license": "https://www.usa.gov/government-works",
-            "rights": null,
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Open Data (MGMT)",
+                "hasEmail": "mailto:edmo@hq.dhs.gov"
+            },
```

