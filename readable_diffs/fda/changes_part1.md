# Change History for fda.json

### Changes from b8668a8 to dd2190f
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
diff --git a/fda.json b/fda.json
index d66333c..da0db10 100644
--- a/fda.json
+++ b/fda.json
@@ -1,9 +1,10 @@
 {
-    "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
     "as_of_date": "Tuesday, August 18, 2015",
+    "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
     "dataset": [
         {
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:10"
             ],
@@ -14,17 +15,17 @@
             "description": "This list includes human and pet food subject to recall in the United States since January 2009 related to peanut products distributed by Peanut Corporation of America. ",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/peanutbutterrecall/PeanutButterProducts2009.xml",
-                    "mediaType": "application/xml",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/peanutbutterrecall/PeanutButterProducts2009.xml",
-                    "format": "XML"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/peanutbutterrecall/PeanutButterProducts2009.xml",
+                    "format": "XML",
+                    "mediaType": "application/xml"
                 }
             ],
-            "accrualPeriodicity": "irregular",
             "identifier": "5d4b366c-07ca-4358-a783-01aa2fe59684",
             "keyword": [
                 "recalls"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/peanutbutterrecall/PeanutButterProducts2009.xml",
             "modified": "1900-01-01",
             "programCode": [
                 "009:001"
@@ -35,11 +36,11 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Peanut Product Recalls",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/peanutbutterrecall/PeanutButterProducts2009.xml"
+            "title": "Peanut Product Recalls"
         },
         {
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:10"
             ],
@@ -50,17 +51,17 @@
             "description": "This list includes food subject to recall in the United States since March 2009 related to pistachios distributed by Setton Pistachio of Terra Bella, Inc. The FDA has completed its inspection of Salmonella contamination in pistachios and pistachio products involved in this recall. ",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/pistachiorecall/Pistachio2009.xml",
-                    "mediaType": "application/xml",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/pistachiorecall/Pistachio2009.xml",
-                    "format": "XML"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/pistachiorecall/Pistachio2009.xml",
+                    "format": "XML",
+                    "mediaType": "application/xml"
                 }
             ],
-            "accrualPeriodicity": "irregular",
             "identifier": "8acf8bd4-3c2b-4697-a2be-3d5006fbfc91",
             "keyword": [
                 "ora"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/pistachiorecall/Pistachio2009.xml",
             "modified": "1900-01-01",
             "programCode": [
                 "009:001"
@@ -71,11 +72,11 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Pistachio Product Recalls",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/pistachiorecall/Pistachio2009.xml"
+            "title": "Pistachio Product Recalls"
         },
         {
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:10"
             ],
@@ -86,17 +87,17 @@
             "description": "This list includes products subject to recall in the United States since February 2010 related to hydrolyzed vegetable protein (HVP) paste and powder distributed by Basic Food Flavors, Inc. HVP is a flavor enhancer used in a wide variety of processed food products such as soups, sauces, chilis, stews, hot dogs, gravies, seasoned snack foods, dips, and dressings. ",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/HVPCP/HydrolyzedVegetableProteinProductsList2010.xml",
-                    "mediaType": "application/xml",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/HVPCP/HydrolyzedVegetableProteinProductsList2010.xml",
-                    "format": "XML"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/HVPCP/HydrolyzedVegetableProteinProductsList2010.xml",
+                    "format": "XML",
+                    "mediaType": "application/xml"
                 }
             ],
-            "accrualPeriodicity": "irregular",
             "identifier": "0a235bac-418f-4fa9-81b7-1af3259a54b1",
             "keyword": [
                 "recalls"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/HVPCP/HydrolyzedVegetableProteinProductsList2010.xml",
             "modified": "1900-01-01",
             "programCode": [
                 "009:001"
@@ -107,11 +108,11 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Hydrolyzed Vegetable Protein Containing Products Recalls",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/HVPCP/HydrolyzedVegetableProteinProductsList2010.xml"
+            "title": "Hydrolyzed Vegetable Protein Containing Products Recalls"
         },
         {
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:10"
             ],
@@ -122,17 +123,17 @@
             "description": "Epidemiologic investigations conducted by health officials in California, Colorado, and Minnesota revealed several restaurants or events where more than one person who fell ill with Salmonella Enteriditis had eaten. Information from these investigations suggested that shell eggs were the likely source of infections in many of these restaurants or events. And on August 13, 2010, Wright County Egg of Galt, Iowa, conducted a nationwide voluntary recalls of shell eggs that it had shipped since May 19, 2010. ",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/shelleggsrecall/ShellEggsRecallList2010.xml",
-                    "mediaType": "application/xml",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/shelleggsrecall/ShellEggsRecallList2010.xml",
-                    "format": "XML"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/shelleggsrecall/ShellEggsRecallList2010.xml",
+                    "format": "XML",
+                    "mediaType": "application/xml"
                 }
             ],
-            "accrualPeriodicity": "irregular",
             "identifier": "2e20dcb3-74a1-46e1-a7bd-900b78dd0355",
             "keyword": [
                 "recalls"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/shelleggsrecall/ShellEggsRecallList2010.xml",
             "modified": "1900-01-01",
             "programCode": [
                 "009:001"
@@ -143,8 +144,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Shell Egg Recalls",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/shelleggsrecall/ShellEggsRecallList2010.xml"
+            "title": "Shell Egg Recalls"
         },
         {
             "accessLevel": "public",
@@ -158,9 +158,9 @@
             "description": "The Food Code Reference System (FCRS) is a searchable database that provides access to FDA\ufffds interpretative positions and responses to questions related to the FDA Food Code.  Users of the FCRS can search the database using dropdown menus, keywords and date. This system is a searchable repository of food code interpretations.  There are no exportable data sets.  All reports are in PDF format.",
             "distribution": [
                 {
+                    "accessURL": "http://www.accessdata.fda.gov/scripts/fcrs/",
                     "description": "This system is a searchable repository of food code interpretations.  There are no exportable data sets.  All reports are in PDF format.  ",
-                    "mediaType": "text/html",
-                    "accessURL": "http://www.accessdata.fda.gov/scripts/fcrs/"
+                    "mediaType": "text/html"
                 }
             ],
             "identifier": "9B9C0AD1-73D2-4280-A1DE-45D15DDB7386",
@@ -196,9 +196,9 @@
             "description": "This system shares public data that can be downloaded.  ",
             "distribution": [
                 {
+                    "accessURL": "http://www.accessdata.fda.gov/scripts/fdcc/",
                     "description": "This system shares public data that can be downloaded.  ",
-                    "mediaType": "text/html",
-                    "accessURL": "http://www.accessdata.fda.gov/scripts/fdcc/"
+                    "mediaType": "text/html"
                 }
             ],
             "identifier": "8DFE05EA-9FA0-4DB8-B803-D3AA70564592",
@@ -250,6 +250,7 @@
         },
         {
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:10"
             ],
@@ -260,17 +261,17 @@
             "description": "This list includes products subject to recall since September 2010 related to infant formula distributed by Abbott. This list will be updated with publicly available information as received. The information is current as of the date indicated. If we learn that any information is not accurate, we will revise the list as soon as possible. When available, this database also includes photos of recalled products that have been voluntarily submitted by recalling firms to the FDA to assist the public in identifying those products that are subject to recall.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/infantformula/InfantFormulaRecallList2010.xml",
-                    "mediaType": "application/xml",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/infantformula/InfantFormulaRecallList2010.xml",
-                    "format": "XML"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/infantformula/InfantFormulaRecallList2010.xml",
+                    "format": "XML",
+                    "mediaType": "application/xml"
                 }
             ],
-            "accrualPeriodicity": "irregular",
             "identifier": "cbb45912-ca03-4398-8d6d-607e335a8ed9",
             "keyword": [
                 "recalls"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/infantformula/InfantFormulaRecallList2010.xml",
             "modified": "1900-01-01",
             "programCode": [
                 "009:001"
@@ -281,11 +282,11 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Abbott Infant Formula Recall",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/infantformula/InfantFormulaRecallList2010.xml"
+            "title": "Abbott Infant Formula Recall"
         },
         {
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:10"
             ],
@@ -296,17 +297,17 @@
             "description": "MedWatch alerts provide timely new safety information on human drugs, medical devices, vaccines and other biologics, dietary supplements, and cosmetics. The alerts contain actionable information that may impact both treatment and diagnostic choices for healthcare professional and patient.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/downloads/Safety/MedWatch/SafetyInformation/UCM189811.zip",
-                    "mediaType": "application/zip",
                     "accessURL": "http://www.fda.gov/downloads/Safety/MedWatch/SafetyInformation/UCM189811.zip",
-                    "format": "ZIP"
+                    "downloadURL": "http://www.fda.gov/downloads/Safety/MedWatch/SafetyInformation/UCM189811.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
             "identifier": "2003711a-3d1c-4a0c-9928-09de5c42e2cf",
             "keyword": [
                 "definitions"
             ],
+            "landingPage": "http://www.fda.gov/Safety/MedWatch/SafetyInformation/SafetyAlertsforHumanMedicalProducts/default.htm",
             "modified": "R/P1Y",
             "programCode": [
                 "009:008"
@@ -317,8 +318,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "MedWatch Safety Alerts for Human Medical Products",
-            "landingPage": "http://www.fda.gov/Safety/MedWatch/SafetyInformation/SafetyAlertsforHumanMedicalProducts/default.htm"
+            "title": "MedWatch Safety Alerts for Human Medical Products"
         },
         {
             "accessLevel": "public",
@@ -332,11 +332,11 @@
             "description": "Public access  allowing for public search of the FDA Adverse Events Database",
             "distribution": [
                 {
+                    "accessURL": "http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/ucm082193",
                     "description": "Public access  allowing for public search of the FDA Adverse Events Database",
                     "downloadURL": "http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/ucm082193",
-                    "mediaType": "text/xml",
-                    "accessURL": "http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/ucm082193",
-                    "format": "XML"
+                    "format": "XML",
+                    "mediaType": "text/xml"
                 }
             ],
             "identifier": "901A022F-A9B2-4B0A-9A33-0F3D353DF3FD",
@@ -367,9 +367,9 @@
             "description": "The Approved Drug Products with Therapeutic Equivalence (Orange Book or OB) is a list of drugs approved under Section 505 of the Federal Food, Drug and Cosmetic Act and provides consumers timely updates on these products. In addition to these products (fo",
             "distribution": [
                 {
+                    "accessURL": "http://www.accessdata.fda.gov/scripts/cder/ob/",
                     "description": "The Approved Drug Products with Therapeutic Equivalence (Orange Book or OB) is a list of drugs approved under Section 505 of the Federal Food, Drug and Cosmetic Act and provides consumers timely updates on these products. In addition to these products (fo",
-                    "mediaType": "text/html",
-                    "accessURL": "http://www.accessdata.fda.gov/scripts/cder/ob/"
+                    "mediaType": "text/html"
                 }
             ],
             "identifier": "5E4326F3-B3EC-40C7-B5B9-1115F3394E94",
@@ -401,9 +401,9 @@
             "description": "The Global Unique Device Identification Database (GUDID) contains key device identification information submitted to the FDA about medical devices that have Unique Device Identifiers (UDI). Unique device identification is a system being established by the",
             "distribution": [
                 {
+                    "accessURL": "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/UniqueDeviceIdentification/GlobalUDIDatabaseGUDID/default.htm",
                     "description": "The Global Unique Device Identification Database (GUDID) contains key device identification information submitted to the FDA about medical devices that have Unique Device Identifiers (UDI). Unique device identification is a system being established by the",
-                    "mediaType": "text/html",
-                    "accessURL": "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/UniqueDeviceIdentification/GlobalUDIDatabaseGUDID/default.htm"
+                    "mediaType": "text/html"
                 }
             ],
             "identifier": "C37E5FDF-6717-4AB3-8585-1808C7BF3B3B",
@@ -436,9 +436,9 @@
             "description": "The FDA shall publish in a format that is understandable and not misleading to a lay person, and place on public display, a list of 93 harmful and potentially harmful constituents in each tobacco product and smoke established under section 904(e) of the TCA.  CTP has determined the best means to display the data is web-based on FDA.GOV.  The HPHC back-end database and template for industry will be created in a future release of eSubmissions.  The scope of this project is to: Phase 1 (Current POP): 1) build a website to support the display of the HPHC constituents, 2) allow the user to access educational information about the health effects of the chemicals; Phase 2 (next POP):  1) allow users of the website to perform a search by brand and sub-brand, 2) display a report on the HPHCs contained in that tobacco product, and 3) create an admin module to allow for an import of HPHC data via an Excel spreadsheet and to update the list of constituents.",
             "distribution": [
                 {
+                    "accessURL": "http://www.fda.gov/TobaccoProducts/GuidanceComplianceRegulatoryInformation/ucm297786.htm",
                     "description": "Website is still under development, not yet published to the public. Pre-Production L is: http://accessdata-preprod.fda.gov/scripts/hphc/",
-                    "mediaType": "text/html",
-                    "accessURL": "http://www.fda.gov/TobaccoProducts/GuidanceComplianceRegulatoryInformation/ucm297786.htm"
+                    "mediaType": "text/html"
                 }
             ],
             "identifier": "96E5B59F-286A-4127-A6E1-82EBA4981EFF",
@@ -471,16 +471,17 @@
             "description": "This application provides information for active, inactive, and pre-registered firms. Query options are by FEI, Applicant Name, Establishment Name, Other Names, Establishment Type, Establishment Status, City, State, Zip Code, Country and Reporting Official First Name or Last Name.",
             "distribution": [
                 {
-                    "downloadURL": "https://www.accessdata.fda.gov/scripts/cber/CFAppsPub/",
-                    "mediaType": "text/html",
                     "accessURL": "https://www.accessdata.fda.gov/scripts/cber/CFAppsPub/",
-                    "format": "Interactive on-screen"
+                    "downloadURL": "https://www.accessdata.fda.gov/scripts/cber/CFAppsPub/",
+                    "format": "Interactive on-screen",
+                    "mediaType": "text/html"
                 }
             ],
             "identifier": "a0710f78-0585-45c8-9320-7d252b291390",
             "keyword": [
                 "cber"
             ],
+            "landingPage": "https://www.accessdata.fda.gov/scripts/cber/CFAppsPub/",
             "modified": "2010-06-04",
             "programCode": [
                 "009:003"
@@ -491,8 +492,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Blood Establishment Registration Database",
-            "landingPage": "https://www.accessdata.fda.gov/scripts/cber/CFAppsPub/"
+            "title": "Blood Establishment Registration Database"
         },
         {
             "accessLevel": "public",
@@ -506,10 +506,10 @@
             "description": "Provides information to the public on postmarket requirements and commitments. The phrase postmarket requirements and commitments refers to studies and clinical trials that sponsors conduct after approval to gather additional information about a product's safety, efficacy, or optimal use. Some of the studies and clinical trials may be required; others may be studies or clinical trials a sponsor has committed to conduct.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/downloads/Drugs/GuidanceComplianceRegulatoryInformation/Post-marketingPhaseIVCommitments/UCM070783.zip",
-                    "mediaType": "application/zip",
                     "accessURL": "http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Post-marketingPhaseIVCommitments/ucm070777.htm",
-                    "format": "Zip"
+                    "downloadURL": "http://www.fda.gov/downloads/Drugs/GuidanceComplianceRegulatoryInformation/Post-marketingPhaseIVCommitments/UCM070783.zip",
+                    "format": "Zip",
+                    "mediaType": "application/zip"
                 }
             ],
             "identifier": "bf085673-ae08-4807-8ca7-aeb36dde83ed",
@@ -518,6 +518,7 @@
                 "postmarket",
                 "commitments"
             ],
+            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm142931.htm",
             "modified": "2011-02-10",
             "programCode": [
                 "009:002"
@@ -528,8 +529,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Postmarket Requirements and Commitments",
-            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm142931.htm"
+            "title": "Postmarket Requirements and Commitments"
         },
         {
             "accessLevel": "public",
@@ -540,13 +540,14 @@
                 "fn": "openFDA",
                 "hasEmail": "mailto:open@fda.hhs.gov"
             },
+            "describedBy": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm075230.htm",
             "description": "According to 21 CFR 210.3(b)(8), an inactive ingredient is any component of a drug product other than the active ingredient. Only inactive ingredients in the final dosage forms of drug products are in this database.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/downloads/Drugs/InformationOnDrugs/UCM080154.zip",
-                    "mediaType": "application/zip",
                     "accessURL": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm113978.htm",
-                    "format": "Zip"
+                    "downloadURL": "http://www.fda.gov/downloads/Drugs/InformationOnDrugs/UCM080154.zip",
+                    "format": "Zip",
+                    "mediaType": "application/zip"
                 }
             ],
             "identifier": "61f4a54b-daf5-4eb0-82fa-30dc89cd9699",
@@ -554,6 +555,7 @@
                 "cder",
                 "inactive ingredient"
             ],
+            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm080123.htm",
             "modified": "2013-01-02",
             "programCode": [
                 "009:002"
@@ -564,9 +566,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Inactive ingredient Search for Approved Drug Products",
-            "describedBy": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm075230.htm",
-            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm080123.htm"
+            "title": "Inactive ingredient Search for Approved Drug Products"
         },
         {
             "accessLevel": "public",
@@ -580,10 +580,10 @@
             "description": "The FDA Adverse Event Reporting System (FAERS) is a database that contains information on adverse event and medication error reports submitted to FDA. The database is designed to support the FDA's post-marketing safety surveillance program for drug and therapeutic biologic products.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/ucm082193.htm",
-                    "mediaType": "application/zip",
                     "accessURL": "http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/ucm082193.htm",
-                    "format": "Zip"
+                    "downloadURL": "http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/ucm082193.htm",
+                    "format": "Zip",
+                    "mediaType": "application/zip"
                 }
             ],
             "identifier": "c696c4f7-6de9-45db-988a-7195c2ade1d0",
@@ -594,6 +594,7 @@
                 "Adverse Event",
                 "Reporting System"
             ],
+            "landingPage": "http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/ucm082193.htm",
             "modified": "2013-08-16",
             "programCode": [
                 "009:002"
@@ -604,11 +605,11 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "FDA Adverse Event Reporting System (FAERS): Latest Quartely Data Files",
-            "landingPage": "http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/ucm082193.htm"
+            "title": "FDA Adverse Event Reporting System (FAERS): Latest Quartely Data Files"
         },
         {
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "009:10"
             ],
@@ -616,20 +617,21 @@
                 "fn": "FDA Enterprise Data Inventory",
                 "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
             },
+            "describedBy": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm079750.htm",
             "description": "Information about FDA-approved brand name and generic prescription and over-the-counter human drugs and biological therapeutic products. Drugs@FDA includes most of the drug products approved since 1939. The majority of patient information, labels, approval letters, reviews, and other information are available for drug products approved since 1998.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/downloads/Drugs/InformationOnDrugs/UCM054599.zip",
-                    "mediaType": "application/zip",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/cder/drugsatfda/index.cfm",
-                    "format": "ZIP"
+                    "downloadURL": "http://www.fda.gov/downloads/Drugs/InformationOnDrugs/UCM054599.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip"
                 }
             ],
-            "accrualPeriodicity": "R/P1D",
             "identifier": "f22c9b6a-e68a-445a-ae44-1441b2f698ab",
             "keyword": [
                 "cder"
             ],
+            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm135821.htm",
             "modified": "R/P1D",
             "programCode": [
                 "009:002"
@@ -640,12 +642,11 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Drugs@FDA Database",
-            "describedBy": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm079750.htm",
-            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm135821.htm"
+            "title": "Drugs@FDA Database"
         },
         {
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:10"
             ],
@@ -656,19 +657,19 @@
             "description": "The Drug Establishments Current Registration Site (DECRS) is a database of current information submitted by drug firms to register establishments (facilities) which manufacture, prepare, propagate, compound or process drugs that are commercially distributed in the U.S. or offered for import to the U.S.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/downloads/Drugs/InformationOnDrugs/UCM197817.zip",
-                    "mediaType": "application/zip",
                     "accessURL": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm135778.htm",
-                    "format": "ZIP"
+                    "downloadURL": "http://www.fda.gov/downloads/Drugs/InformationOnDrugs/UCM197817.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
             "identifier": "fa27e8ba-4b3c-4a2d-bb29-19eecffa0847",
             "keyword": [
                 "cder",
                 "establishments",
                 "registration"
             ],
+            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm135778.htm",
             "modified": "R/P3M",
             "programCode": [
                 "009:002"
@@ -679,11 +680,11 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Drug Establishments Current Registration Site",
-            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm135778.htm"
+            "title": "Drug Establishments Current Registration Site"
         },
         {
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:10"
             ],
@@ -694,18 +695,18 @@
             "description": "For a drug product that does not have a dissolution test method in the United States Pharmacopeia (USP), the FDA Dissolution Methods Database provides information on dissolution methods presently recommended by the Division of Bioequivalence, Office of Generic Drugs.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm135742.htm",
-                    "mediaType": "text/html",
                     "accessURL": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm135742.htm",
-                    "format": "Interactive on-screen"
+                    "downloadURL": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm135742.htm",
+                    "format": "Interactive on-screen",
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
             "identifier": "3f2b8dee-6c80-4230-8f8a-3f7c83920d42",
             "keyword": [
                 "cder",
                 "dissolution"
             ],
+            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm135742.htm",
             "modified": "R/P3M",
             "programCode": [
                 "009:002"
@@ -719,11 +720,11 @@
             "references": [
                 "http://www.accessdata.fda.gov/scripts/cder/dissolution/index.cfm"
             ],
-            "title": "Dissolution Methods Database",
-            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm135742.htm"
+            "title": "Dissolution Methods Database"
         },
         {
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:10"
             ],
@@ -731,21 +732,22 @@
                 "fn": "openFDA",
                 "hasEmail": "mailto:open@fda.hhs.gov"
             },
+            "describedBy": "http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/EnforcementActivitiesbyFDA/ucm073059.htm",
             "description": "The Clinical Investigator Inspection List (CLIIL) contains names, addresses, and other pertinent information gathered from inspections of clinical investigators who have performed studies with investigational new drugs. The list contains information on inspections that have been closed since July 1977.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/downloads/Drugs/InformationOnDrugs/UCM111343.zip",
-                    "mediaType": "application/zip",
                     "accessURL": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm135198.htm",
-                    "format": "Zipped TXT"
+                    "downloadURL": "http://www.fda.gov/downloads/Drugs/InformationOnDrugs/UCM111343.zip",
+                    "format": "Zipped TXT",
+                    "mediaType": "application/zip"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
             "identifier": "9dcfa54e-3b0c-40c8-b2fe-754820bed30f",
             "keyword": [
                 "cder",
                 "clinical investigator"
             ],
+            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm135198.htm",
             "modified": "R/P3M",
             "programCode": [
                 "009:002"
@@ -756,9 +758,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Clinical Investigator Inspector List (CLIIL)",
-            "describedBy": "http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/EnforcementActivitiesbyFDA/ucm073059.htm",
-            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm135198.htm"
+            "title": "Clinical Investigator Inspector List (CLIIL)"
         },
         {
             "accessLevel": "public",
@@ -772,16 +772,17 @@
             "description": "Food producers recall their products from the marketplace when the products are mislabeled or when the food may present a health hazard to consumers because the food is contaminated or has caused a foodborne illness outbreak. ",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/Food/RecallsOutbreaksEmergencies/Recalls/default.htm",
-                    "mediaType": "text/html",
                     "accessURL": "http://www.fda.gov/Food/RecallsOutbreaksEmergencies/Recalls/default.htm",
-                    "format": "On-screen text"
+                    "downloadURL": "http://www.fda.gov/Food/RecallsOutbreaksEmergencies/Recalls/default.htm",
+                    "format": "On-screen text",
+                    "mediaType": "text/html"
                 }
             ],
             "identifier": "7268c3d7-607f-452c-a54c-2ac89d7b6b65",
             "keyword": [
                 "cfsan"
             ],
+            "landingPage": "http://www.fda.gov/Food/RecallsOutbreaksEmergencies/Recalls/default.htm",
             "modified": "2013-06-06",
             "programCode": [
                 "009:001"
@@ -792,8 +793,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Recalls of Food and Dietary Supplements",
-            "landingPage": "http://www.fda.gov/Food/RecallsOutbreaksEmergencies/Recalls/default.htm"
+            "title": "Recalls of Food and Dietary Supplements"
         },
         {
             "accessLevel": "public",
@@ -807,10 +807,10 @@
             "description": "The Food and Drug Administration Amendments Act of 2007 gave FDA the authority to require a Risk Evaluation and Mitigation Strategy (REMS) from manufacturers to ensure that the benefits of a drug or biological product outweigh its risks. ",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/Drugs/DrugSafety/PostmarketDrugSafetyInformationforPatientsandProviders/ucm111350.htm",
-                    "mediaType": "application/pdf",
                     "accessURL": "http://www.fda.gov/Drugs/DrugSafety/PostmarketDrugSafetyInformationforPatientsandProviders/ucm111350.htm",
-                    "format": "PDF"
+                    "downloadURL": "http://www.fda.gov/Drugs/DrugSafety/PostmarketDrugSafetyInformationforPatientsandProviders/ucm111350.htm",
+                    "format": "PDF",
+                    "mediaType": "application/pdf"
                 }
             ],
             "identifier": "6c697267-fe17-4c66-8c6d-da38ab9b723b",
@@ -818,6 +818,7 @@
                 "cder",
                 "REMS"
             ],
+            "landingPage": "http://www.fda.gov/Drugs/DrugSafety/PostmarketDrugSafetyInformationforPatientsandProviders/ucm111350.htm",
             "modified": "2013-11-12",
             "programCode": [
                 "009:002"
@@ -828,8 +829,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Approved Risk Evaluation and Mitigation Strategies",
-            "landingPage": "http://www.fda.gov/Drugs/DrugSafety/PostmarketDrugSafetyInformationforPatientsandProviders/ucm111350.htm"
+            "title": "Approved Risk Evaluation and Mitigation Strategies"
         },
         {
             "accessLevel": "public",
@@ -843,10 +843,10 @@
             "description": "Companies are required under Section 506C of the Federal Food, Drug, and Cosmetic Act (FD&C Act) (as amended by the Food and Drug Administration Safety and Innovation Act) to notify FDA of a permanent discontinuance of certain drug products, six months in advance, or if that is not possible, as soon as practicable. These drugs include those that are life-supporting, life-sustaining or for use in the prevention or treatment of a debilitating disease or condition, including any such drug used in emergency medical care or during surgery). The discontinuations provided below reflect information received from manufacturers, and are for informational purposes only.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/Drugs/DrugSafety/DrugShortages/ucm050794.htm",
-                    "mediaType": "application/unknown",
                     "accessURL": "http://www.fda.gov/Drugs/DrugSafety/DrugShortages/ucm050794.htm",
-                    "format": "application/unknown"
+                    "downloadURL": "http://www.fda.gov/Drugs/DrugSafety/DrugShortages/ucm050794.htm",
+                    "format": "application/unknown",
+                    "mediaType": "application/unknown"
                 }
             ],
             "identifier": "6e72c239-0510-49f4-8404-d3d7d50351ec",
@@ -854,6 +854,7 @@
                 "cder",
                 "discontinued drugs"
             ],
+            "landingPage": "http://www.fda.gov/Drugs/DrugSafety/DrugShortages/ucm050794.htm",
             "modified": "2013-09-26",
             "programCode": [
                 "009:002"
@@ -864,11 +865,11 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Drugs to be Discontinued",
-            "landingPage": "http://www.fda.gov/Drugs/DrugSafety/DrugShortages/ucm050794.htm"
+            "title": "Drugs to be Discontinued"
         },
         {
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "009:10"
             ],
@@ -879,17 +880,17 @@
             "description": "Information provided to FDA by manufacturers about current drugs in shortage, resolved shortages, and discontinuations of specific drug products.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/drugshortages/default.cfm",
-                    "mediaType": "text/html",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/drugshortages/default.cfm",
-                    "format": "Interactive on-screen"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/drugshortages/default.cfm",
+                    "format": "Interactive on-screen",
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1W",
             "identifier": "520f8f0d-b519-4ad9-8597-14d517f00987",
             "keyword": [
                 "cder"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/drugshortages/default.cfm",
             "modified": "R/P1D",
             "programCode": [
                 "009:002"
@@ -900,8 +901,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Current and Resolved Drug Shortages and Discontinuations Reported to FDA",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/drugshortages/default.cfm"
+            "title": "Current and Resolved Drug Shortages and Discontinuations Reported to FDA"
         },
         {
             "accessLevel": "public",
@@ -915,16 +915,17 @@
             "description": "This database contains a list of classified medical device recalls since November 1, 2002",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRES/res.cfm",
-                    "mediaType": "text/html",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRES/res.cfm",
-                    "format": "Interactive on-screen"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRES/res.cfm",
+                    "format": "Interactive on-screen",
+                    "mediaType": "text/html"
                 }
             ],
             "identifier": "c2420fb3-2c71-4a09-80a9-5fc2f3a459f5",
             "keyword": [
                 "cdrh"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRES/res.cfm",
             "modified": "2013-11-13",
             "programCode": [
                 "009:005"
@@ -938,8 +939,7 @@
             "references": [
                 "http://www.fda.gov/MedicalDevices/Safety/ListofRecalls/ucm329946.htm"
             ],
-            "title": "Medical and Radiation Emitting Device Recalls",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRES/res.cfm"
+            "title": "Medical and Radiation Emitting Device Recalls"
         },
         {
             "accessLevel": "public",
@@ -953,16 +953,17 @@
             "description": "The 522 Postmarket Surveillance Studies Program encompasses design, tracking, oversight, and review responsibilities for studies mandated under section 522 of the Federal Food, Drug and Cosmetic Act. The program helps ensure that well-designed 522 postmarket surveillance (PS) studies are conducted effectively and efficiently and in the least burdensome manner.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMA/pss_excel.cfm",
-                    "mediaType": "application/vnd.ms-excel",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMA/pss_excel.cfm",
-                    "format": "XLS"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMA/pss_excel.cfm",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel"
                 }
             ],
             "identifier": "3d55fceb-5248-4475-b675-503312202d0d",
             "keyword": [
                 "cdrh"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMA/pss.cfm",
             "modified": "2013-11-01",
             "programCode": [
                 "009:005"
@@ -977,8 +978,7 @@
                 "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/PostmarketRequirements/PostmarketSurveillance/ucm134497.htm",
                 "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/GuidanceDocuments/ucm268064.htm"
             ],
-            "title": "522 Postmarket Surveillance Studies",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMA/pss.cfm"
+            "title": "522 Postmarket Surveillance Studies"
         },
         {
             "accessLevel": "public",
@@ -992,16 +992,17 @@
             "description": "The CDRH Post-Approval Studies Program encompasses design, tracking, oversight, and review responsibilities for studies mandated as a condition of approval of a premarket approval (PMA) application, protocol development product (PDP) application, or humanitarian device exemption (HDE) application. The program helps ensure that well-designed post-approval studies (PAS) are conducted effectively and efficiently and in the least burdensome manner.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMA/pma_pas_Excel.cfm",
-                    "mediaType": "application/vnd.ms-excel",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMA/pma_pas_Excel.cfm",
-                    "format": "XLS"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMA/pma_pas_Excel.cfm",
+                    "format": "XLS",
+                    "mediaType": "application/vnd.ms-excel"
                 }
             ],
             "identifier": "910c9a83-0447-4c05-b418-c2f49dd83b1b",
             "keyword": [
                 "cdrh"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMA/pma_pas.cfm",
             "modified": "2013-11-01",
             "programCode": [
                 "009:005"
@@ -1012,8 +1013,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Post-Approval Studies",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMA/pma_pas.cfm"
+            "title": "Post-Approval Studies"
         },
         {
             "accessLevel": "public",
@@ -1025,13 +1025,12 @@
                 "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
             },
             "description": "On September 22, 2010, Abbott issued a voluntary recall of certain Similac powdered infant formula after identifying a common warehouse beetle (both larvae and adults) in the finished product at their Sturgis, Michigan plant. The company immediately put all product manufactured at the Michigan plant on hold and ceased manufacturing at that location. FDA has advised against consumption of the recalled product and urged consumers to follow the manufacturer's instructions for reporting and returning the formula.",
-            "temporal": "2010-01-01/2010-12-31",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/infantformula/InfantFormulaRecallList2010.xls",
-                    "mediaType": "application/vnd.ms-excel",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/infantformula/InfantFormulaRecallList2010.xls",
-                    "format": "Excel"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/infantformula/InfantFormulaRecallList2010.xls",
+                    "format": "Excel",
+                    "mediaType": "application/vnd.ms-excel"
                 }
             ],
             "identifier": "141bcfb1-fd5c-4abc-9e81-0e07cc3c8ca4",
@@ -1046,6 +1045,7 @@
                 "recalls",
                 "safety"
             ],
+            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm227485.htm",
             "modified": "2010-10-01",
             "programCode": [
                 "009:001"
@@ -1056,11 +1056,12 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "FDA Abbott Infant Formula Recall",
-            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm227485.htm"
+            "temporal": "2010-01-01/2010-12-31",
+            "title": "FDA Abbott Infant Formula Recall"
         },
         {
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:10"
             ],
@@ -1069,16 +1070,14 @@
                 "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
             },
             "description": "This list is intended to alert consumers about Web sites that are or were illegally marketing unapproved, uncleared, or unauthorized products in relation to the 2009 H1N1 Flu Virus (sometimes referred to as the 'swine flu' virus).",
-            "temporal": "2009-01-01/2009-12-31",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/h1n1flu/FraudulentH1N1ProductsList2009.xml",
-                    "mediaType": "application/xml",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/h1n1flu/FraudulentH1N1ProductsList2009.xls",
-                    "format": "XML"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/h1n1flu/FraudulentH1N1ProductsList2009.xml",
+                    "format": "XML",
+                    "mediaType": "application/xml"
                 }
             ],
-            "accrualPeriodicity": "irregular",
             "identifier": "8b366073-48df-4c87-9120-9878f4875373",
             "keyword": [
                 "community health",
@@ -1091,6 +1090,7 @@
                 "safety",
                 "ora"
             ],
+            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225441.htm",
             "modified": "1900-01-01",
             "programCode": [
                 "009:000"
@@ -1101,8 +1101,8 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Fraudulent 2009 H1N1 Influenza Products",
-            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225441.htm"
+            "temporal": "2009-01-01/2009-12-31",
+            "title": "Fraudulent 2009 H1N1 Influenza Products"
         },
         {
             "accessLevel": "public",
@@ -1116,10 +1116,10 @@
             "description": "This feed provides new health and safety updates related to FDA approved products",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/AboutFDA/ContactFDA/StayInformed/RSSFeeds/Consumers/rss.xml",
-                    "mediaType": "application/rss+xml",
                     "accessURL": "http://www.fda.gov/AboutFDA/ContactFDA/StayInformed/RSSFeeds/Consumers/rss.xml",
-                    "format": "RSS+XML"
+                    "downloadURL": "http://www.fda.gov/AboutFDA/ContactFDA/StayInformed/RSSFeeds/Consumers/rss.xml",
+                    "format": "RSS+XML",
+                    "mediaType": "application/rss+xml"
                 }
             ],
             "identifier": "82319f7a-9d6e-4b9e-b67f-cf8ff1a4980e",
@@ -1134,6 +1134,7 @@
                 "safety",
                 "updates"
             ],
+            "landingPage": "http://www.fda.gov/AboutFDA/ContactFDA/StayInformed/RSSFeeds/Consumers/rss.xml",
             "modified": "2012-05-30",
             "programCode": [
                 "009:000"
@@ -1144,8 +1145,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Health Information Updates",
-            "landingPage": "http://www.fda.gov/AboutFDA/ContactFDA/StayInformed/RSSFeeds/Consumers/rss.xml"
+            "title": "Health Information Updates"
         },
         {
             "accessLevel": "public",
@@ -1159,10 +1159,10 @@
             "description": "Contains data for FDA pet food recalls since January 1, 2006.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/newpetfoodrecalls/PetFoodRecallProductsList2009.xls",
-                    "mediaType": "application/vnd.ms-excel",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/newpetfoodrecalls/PetFoodRecallProductsList2009.xls",
-                    "format": "Excel"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/newpetfoodrecalls/PetFoodRecallProductsList2009.xls",
+                    "format": "Excel",
+                    "mediaType": "application/vnd.ms-excel"
                 }
             ],
             "identifier": "617db889-3907-4429-aa64-b4747156d437",
@@ -1175,6 +1175,7 @@
                 "recalls",
                 "safety"
             ],
+            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225435.htm",
             "modified": "2010-10-01",
             "programCode": [
                 "009:000"
@@ -1185,8 +1186,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "FDA Pet Food Recalls",
-            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225435.htm"
+            "title": "FDA Pet Food Recalls"
         },
         {
             "accessLevel": "public",
@@ -1200,10 +1200,10 @@
             "description": "This file contains the data elements used for searching the FDA Online Data Repository including proprietary name, active ingredients, marketing application number or regulatory citation, National Drug Code, and company name.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/downloads/ForIndustry/DataStandards/StructuredProductLabeling/ucm241597.zip",
-                    "mediaType": "text/csv",
                     "accessURL": "http://www.fda.gov/downloads/ForIndustry/DataStandards/StructuredProductLabeling/ucm241597.zip",
-                    "format": "text/csv"
+                    "downloadURL": "http://www.fda.gov/downloads/ForIndustry/DataStandards/StructuredProductLabeling/ucm241597.zip",
+                    "format": "text/csv",
+                    "mediaType": "text/csv"
                 }
             ],
             "identifier": "c447002d-51df-46d9-a105-dda94dfd6083",
@@ -1215,6 +1215,7 @@
                 "label repository",
                 "labels fda gov"
             ],
+            "landingPage": "http://www.fda.gov/ForIndustry/DataStandards/StructuredProductLabeling/ucm240580.htm",
             "modified": "2011-02-01",
             "programCode": [
                 "009:000"
@@ -1225,8 +1226,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "FDA Drug Label Data",
-            "landingPage": "http://www.fda.gov/ForIndustry/DataStandards/StructuredProductLabeling/ucm240580.htm"
+            "title": "FDA Drug Label Data"
         },
         {
             "accessLevel": "public",
@@ -1240,10 +1240,10 @@
             "description": "Contains data for FDA peanut product recalls since January 2009.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/peanutbutterrecall/PeanutButterProducts2009.xls",
-                    "mediaType": "application/vnd.ms-excel",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/peanutbutterrecall/PeanutButterProducts2009.xls",
-                    "format": "Excel"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/peanutbutterrecall/PeanutButterProducts2009.xls",
+                    "format": "Excel",
+                    "mediaType": "application/vnd.ms-excel"
                 }
             ],
             "identifier": "1fce6941-625f-4dac-ae3b-6664fcfeea6d",
@@ -1257,6 +1257,7 @@
                 "recalls",
                 "safety"
             ],
+            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225439.htm",
             "modified": "2010-10-01",
             "programCode": [
                 "009:000"
@@ -1267,8 +1268,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "FDA Peanut Product Recalls",
-            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225439.htm"
+            "title": "FDA Peanut Product Recalls"
         },
         {
             "accessLevel": "public",
@@ -1282,10 +1282,10 @@
             "description": "Contains data for FDA recalls from 2009 through the present.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/DataSets/Recalls/RecallsDataSet.xml",
-                    "mediaType": "application/xml",
                     "accessURL": "http://www.fda.gov/DataSets/Recalls/RecallsDataSet.xml",
-                    "format": "XML"
+                    "downloadURL": "http://www.fda.gov/DataSets/Recalls/RecallsDataSet.xml",
+                    "format": "XML",
+                    "mediaType": "application/xml"
                 }
             ],
             "identifier": "d4959928-1229-4fff-a32e-704245f42cb6",
@@ -1302,6 +1302,7 @@
                 "recalls",
                 "safety"
             ],
+            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225433.htm",
             "modified": "2010-10-01",
             "programCode": [
                 "009:000"
@@ -1312,8 +1313,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "All FDA Recalls",
-            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225433.htm"
+            "title": "All FDA Recalls"
         },
         {
             "accessLevel": "public",
@@ -1327,10 +1327,10 @@
             "description": "The FDA Peanut-Containing Product Recall widget allows you to browse the Food and Drug Administration (FDA) database of peanut butter and peanut-containing products subject to recall. This database makes it easier for you to determine whether any of the products you have at home are subject to recent recalls, and will be updated as new information becomes available.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.cdc.gov/Widgets/",
-                    "mediaType": "application/vnd.pmi.widget",
                     "accessURL": "http://www.cdc.gov/Widgets/",
-                    "format": "widget"
+                    "downloadURL": "http://www.cdc.gov/Widgets/",
+                    "format": "widget",
+                    "mediaType": "application/vnd.pmi.widget"
                 }
             ],
             "identifier": "ece9c52a-ba02-4615-b441-fa0d2f8b9722",
@@ -1354,6 +1354,7 @@
                 "salmonella",
                 "snack bars"
             ],
+            "landingPage": "http://www.cdc.gov/Widgets/",
             "modified": "2012-05-30",
             "programCode": [
                 "009:000"
@@ -1364,8 +1365,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "FDA Peanut-Containing Product Recall",
-            "landingPage": "http://www.cdc.gov/Widgets/"
+            "title": "FDA Peanut-Containing Product Recall"
         },
         {
             "accessLevel": "public",
@@ -1379,10 +1379,10 @@
             "description": "This feed describes all new items that are being recalled by the FDA.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/AboutFDA/ContactFDA/StayInformed/RSSFeeds/Recalls/rss.xml",
-                    "mediaType": "application/rss+xml",
                     "accessURL": "http://www.fda.gov/AboutFDA/ContactFDA/StayInformed/RSSFeeds/Recalls/rss.xml",
-                    "format": "rss+xml"
+                    "downloadURL": "http://www.fda.gov/AboutFDA/ContactFDA/StayInformed/RSSFeeds/Recalls/rss.xml",
+                    "format": "rss+xml",
+                    "mediaType": "application/rss+xml"
                 }
             ],
             "identifier": "e9412021-e775-4c64-9c04-98d6f666786f",
@@ -1395,6 +1395,7 @@
                 "recalls",
                 "safety"
             ],
+            "landingPage": "http://www.fda.gov/AboutFDA/ContactFDA/StayInformed/RSSFeeds/Recalls/rss.xml",
             "modified": "2004-01-01",
             "programCode": [
                 "009:000"
@@ -1405,11 +1406,11 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Food and Drug Administration--Recalls",
-            "landingPage": "http://www.fda.gov/AboutFDA/ContactFDA/StayInformed/RSSFeeds/Recalls/rss.xml"
+            "title": "Food and Drug Administration--Recalls"
         },
         {
             "accessLevel": "public",
+            "accrualPeriodicity": "R/PT1S",
             "bureauCode": [
                 "009:10"
             ],
@@ -1420,17 +1421,17 @@
             "description": "Press Releases of food recalls from industry",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/DataSets/Recalls/Food/Food.xml",
-                    "mediaType": "application/xml",
                     "accessURL": "http://www.fda.gov/DataSets/Recalls/Food/Food.xml",
-                    "format": "XML"
+                    "downloadURL": "http://www.fda.gov/DataSets/Recalls/Food/Food.xml",
+                    "format": "XML",
+                    "mediaType": "application/xml"
                 }
             ],
-            "accrualPeriodicity": "R/PT1S",
             "identifier": "cdaa413b-325f-4f81-a78e-f8e55ac77098",
             "keyword": [
                 "recalls"
             ],
+            "landingPage": "http://www.fda.gov/DataSets/Recalls/Food/Food.xml",
             "modified": "R/PT1S",
             "programCode": [
                 "009:001"
@@ -1441,11 +1442,11 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Food Recalls",
-            "landingPage": "http://www.fda.gov/DataSets/Recalls/Food/Food.xml"
+            "title": "Food Recalls"
         },
         {
             "accessLevel": "public",
+            "accrualPeriodicity": "irregular",
             "bureauCode": [
                 "009:10"
             ],
@@ -1456,17 +1457,17 @@
             "description": "This list includes products subject to recall in the United States since June 2009 related to products manufactured by Plainview Milk Products Cooperative. ",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/Milk/MilkRecallProducts2009.xml",
-                    "mediaType": "application/xml",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/Milk/MilkRecallProducts2009.xml",
-                    "format": "XML"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/Milk/MilkRecallProducts2009.xml",
+                    "format": "XML",
+                    "mediaType": "application/xml"
                 }
             ],
-            "accrualPeriodicity": "irregular",
             "identifier": "703b0166-e4c2-4c1e-b5d7-46f5f21acb12",
             "keyword": [
                 "recalls"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/Milk/MilkRecallProducts2009.xml",
             "modified": "1900-01-01",
             "programCode": [
                 "009:001"
@@ -1477,8 +1478,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Plainview Milk Cooperative Ingredient Recall",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/Milk/MilkRecallProducts2009.xml"
+            "title": "Plainview Milk Cooperative Ingredient Recall"
         },
         {
             "accessLevel": "public",
@@ -1492,16 +1492,17 @@
             "description": "The Total Product Life Cycle (TPLC) database integrates premarket and postmarket data about medical devices. It includes information pulled from CDRH databases including Premarket Approvals (PMA), Premarket Notifications (510[k]), Adverse Events, and Recalls. You can search the TPLC database by device name or procode to receive a full report about a particular product line.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfTPLC/tplc.cfm",
-                    "mediaType": "text/html",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfTPLC/tplc.cfm",
-                    "format": "Interactive on-screen"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfTPLC/tplc.cfm",
+                    "format": "Interactive on-screen",
+                    "mediaType": "text/html"
                 }
             ],
             "identifier": "db8a6684-bf00-48a8-af05-c493e6dfcb4c",
             "keyword": [
                 "cdrh"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfTPLC/tplc.cfm",
             "modified": "2013-11-01",
             "programCode": [
                 "009:005"
@@ -1515,11 +1516,11 @@
             "references": [
                 "http://www.fda.gov/AboutFDA/CentersOffices/OfficeofMedicalProductsandTobacco/CDRH/CDRHTransparency/ucm199906.htm"
             ],
-            "title": "Total Product Life Cycle (TPLC)",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfTPLC/tplc.cfm"
+            "title": "Total Product Life Cycle (TPLC)"
         },
         {
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "009:10"
             ],
@@ -1527,20 +1528,21 @@
                 "fn": "openFDA",
                 "hasEmail": "mailto:open@fda.hhs.gov"
             },
+            "describedBy": "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/HowtoMarketYourDevice/RegistrationandListing/ucm134495.htm",
             "description": "This searchable database contains establishments (engaged in the manufacture, preparation, propagation, compounding, assembly, or processing of medical devices intended for human use and commercial distribution) and listings of medical devices in commercial distribution by both domestic and foreign manufacturers. Note: This database is updated once a week.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRL/rl.cfm",
-                    "mediaType": "text/html",
                     "accessURL": "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/HowtoMarketYourDevice/RegistrationandListing/ucm134495.htm",
-                    "format": "Interactive on-screen"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRL/rl.cfm",
+                    "format": "Interactive on-screen",
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1W",
             "identifier": "7138583c-afe2-4e52-843b-a0665c75714d",
             "keyword": [
                 "cdrh"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRL/rl.cfm",
             "modified": "R/P1W",
             "programCode": [
                 "009:005"
@@ -1554,9 +1556,7 @@
             "references": [
                 "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/HowtoMarketYourDevice/RegistrationandListing/ucm134495.htm"
             ],
-            "title": "Establishment Registration & Device Listing",
-            "describedBy": "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/HowtoMarketYourDevice/RegistrationandListing/ucm134495.htm",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRL/rl.cfm"
+            "title": "Establishment Registration & Device Listing"
         },
         {
             "accessLevel": "public",
@@ -1568,19 +1568,19 @@
                 "hasEmail": "mailto:open@fda.hhs.gov"
             },
             "description": "This database contains a list of classified medical device recalls since November 1, 2002",
-            "temporal": "2002-11-01/2013-11-01",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRES/res.cfm",
-                    "mediaType": "text/html",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRES/res.cfm",
-                    "format": "Interactive on-screen"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRES/res.cfm",
+                    "format": "Interactive on-screen",
+                    "mediaType": "text/html"
                 }
             ],
             "identifier": "5291f6b2-f62a-4498-a640-0639d94ec3c6",
             "keyword": [
                 "cdrh"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRES/res.cfm",
             "modified": "2013-11-01",
             "programCode": [
                 "009:005"
@@ -1594,8 +1594,8 @@
             "references": [
                 "http://www.fda.gov/MedicalDevices/Safety/ListofRecalls/ucm329946.htm"
             ],
-            "title": "Recalls of Medical Devices",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfRES/res.cfm"
+            "temporal": "2002-11-01/2013-11-01",
+            "title": "Recalls of Medical Devices"
         },
         {
             "accessLevel": "public",
@@ -1609,16 +1609,17 @@
             "description": "This database provides descriptions of radiation-emitting products that have been recalled under an approved corrective action plan to remove defective and noncompliant products from the market. Searches may be done by manufacturer name, performance standard, product name, description, or date range.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPCD_RH/rh_res.cfm",
-                    "mediaType": "text/html",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPCD_RH/rh_res.cfm",
-                    "format": "Interactive on-screen"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPCD_RH/rh_res.cfm",
+                    "format": "Interactive on-screen",
+                    "mediaType": "text/html"
                 }
             ],
             "identifier": "4a439dda-f8d4-4461-ba4c-082abab102d4",
             "keyword": [
                 "cdrh"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPCD_RH/rh_res.cfm",
             "modified": "2013-11-01",
             "programCode": [
                 "009:005"
@@ -1629,8 +1630,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Radiation Emitting Product Corrective Actions and Recalls",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPCD_RH/rh_res.cfm"
+            "title": "Radiation Emitting Product Corrective Actions and Recalls"
         },
         {
             "accessLevel": "public",
@@ -1641,19 +1641,21 @@
                 "fn": "openFDA",
                 "hasEmail": "mailto:open@fda.hhs.gov"
             },
+            "describedBy": "http://www.fda.gov/Radiation-EmittingProducts/ElectronicProductRadiationControlProgram/GettingaProducttoMarket/PerformanceStandards/ucm135508.htm",
             "description": "This database contains product names and associated information developed by the Center for all products, both medical and non-medical, which emit radiation. It includes a three letter product code, a descriptor for radiation type, applicable performance standard(s), and a definition for the code.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPCD_rh/TextSearch.cfm",
-                    "mediaType": "text/html",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPCD_rh/TextSearch.cfm",
-                    "format": "Interactive on-screen"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPCD_rh/TextSearch.cfm",
+                    "format": "Interactive on-screen",
+                    "mediaType": "text/html"
                 }
             ],
             "identifier": "7e7f6062-5270-4e09-81c9-ff22261232ac",
             "keyword": [
                 "cdrh"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPCD_rh/TextSearch.cfm",
             "modified": "2013-11-01",
             "programCode": [
                 "009:005"
@@ -1667,9 +1669,7 @@
             "references": [
                 "http://www.fda.gov/Radiation-EmittingProducts/ElectronicProductRadiationControlProgram/GettingaProducttoMarket/PerformanceStandards/ucm135509.htm"
             ],
-            "title": "Radiation-emitting Electronic Product Codes",
-            "describedBy": "http://www.fda.gov/Radiation-EmittingProducts/ElectronicProductRadiationControlProgram/GettingaProducttoMarket/PerformanceStandards/ucm135508.htm",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPCD_rh/TextSearch.cfm"
+            "title": "Radiation-emitting Electronic Product Codes"
         },
         {
             "accessLevel": "public",
@@ -1680,19 +1680,21 @@
                 "fn": "openFDA",
                 "hasEmail": "mailto:open@fda.hhs.gov"
             },
+            "describedBy": "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/Overview/ClassifyYourDevice/ucm2005371.htm",
             "description": "This database contains medical device names and associated information developed by the Center. It includes a three letter device product code and a Device Class that refers to the level of CDRH regulation of a given device.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/premarket/ftparea/foiclass.zip",
-                    "mediaType": "application/zip",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPCD/PCDSimpleSearch.cfm",
-                    "format": "ZIP"
+                    "downloadURL": "http://www.accessdata.fda.gov/premarket/ftparea/foiclass.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip"
                 }
             ],
             "identifier": "3286eac6-86ad-4236-9281-8d09ad04e816",
             "keyword": [
                 "cdrh"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPCD/PCDSimpleSearch.cfm",
             "modified": "R/P1M",
             "programCode": [
                 "009:005"
@@ -1706,12 +1708,11 @@
             "references": [
                 "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/Overview/ClassifyYourDevice/ucm051668.htm"
             ],
-            "title": "Product Classification",
-            "describedBy": "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/Overview/ClassifyYourDevice/ucm2005371.htm",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPCD/PCDSimpleSearch.cfm"
+            "title": "Product Classification"
         },
         {
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "009:10"
             ],
@@ -1720,20 +1721,19 @@
                 "hasEmail": "mailto:open@fda.hhs.gov"
             },
             "description": "Medical device manufacturers are required to submit a premarket notification or 510(k) if they intend to introduce a device into commercial distribution for the first time or reintroduce a device that will be significantly changed or modified to the extent that its safety or effectiveness could be affected. This database of releasable 510(k)s can be searched by 510(k) number, applicant, device name or FDA product code. Summaries of safety and effectiveness information is available via the web interface for more recent records. ",
-            "temporal": "1976-01-01/2013-12-31",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/premarket/ftparea/pmn96cur.zip",
-                    "mediaType": "application/zip",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMN/pmn.cfm",
-                    "format": "ZIP"
+                    "downloadURL": "http://www.accessdata.fda.gov/premarket/ftparea/pmn96cur.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
             "identifier": "142e5da1-24f6-4215-83e5-18a7cd813889",
             "keyword": [
                 "cdrh"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMN/pmn.cfm",
             "modified": "2013-11-01",
             "programCode": [
                 "009:005"
@@ -1747,11 +1747,12 @@
             "references": [
                 "http://www.fda.gov/MedicalDevices/ProductsandMedicalProcedures/DeviceApprovalsandClearances/510kClearances/ucm089428.htm"
             ],
-            "title": "Premarket Notifications (510(k)s)",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMN/pmn.cfm"
+            "temporal": "1976-01-01/2013-12-31",
+            "title": "Premarket Notifications (510(k)s)"
         },
         {
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "009:10"
             ],
@@ -1762,17 +1763,17 @@
             "description": "A 180-day supplement is a request for a significant change in components, materials, design, specification, software, color additive, and labeling to an approved premarket application or premarket report. As a pilot program under the CDRH Transparency Initiative, FDA has begun releasing some summary review memos for 180-day PMA supplements relating to design changes.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpma/pmamemos.cfm",
-                    "mediaType": "text/html",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpma/pmamemos.cfm",
-                    "format": "Interactive on-screen"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpma/pmamemos.cfm",
+                    "format": "Interactive on-screen",
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1W",
             "identifier": "8dabbf7e-0e4a-4e1c-a0d2-982d97398a10",
             "keyword": [
                 "cdrh"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpma/pmamemos.cfm",
             "modified": "R/P1W",
             "programCode": [
                 "009:005"
@@ -1783,8 +1784,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Premarket Approval (PMA) Summary Review Memos for 180-Day Design Changes",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpma/pmamemos.cfm"
+            "title": "Premarket Approval (PMA) Summary Review Memos for 180-Day Design Changes"
         },
         {
             "accessLevel": "public",
@@ -1795,12 +1795,13 @@
                 "fn": "openFDA",
                 "hasEmail": "mailto:open@fda.hhs.gov"
             },
+            "describedBy": "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/Databases/ucm135279.htm",
             "description": "Premarket approval by FDA is the required process of scientific review to ensure the safety and effectiveness of all devices classified as Class III devices. An approved Premarket Approval Application (PMA) is, in effect, a private license granted to the applicant for marketing a particular medical device. This database may be searched by a variety of fields and is updated on a monthly basis.",
             "distribution": [
                 {
-                    "mediaType": "text/html",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMA/pma.cfm",
-                    "format": "Interactive on-screen"
+                    "format": "Interactive on-screen",
+                    "mediaType": "text/html"
                 }
             ],
             "identifier": "475907fb-6a5d-4ad8-90c0-b276edc05227",
@@ -1821,8 +1822,7 @@
                 "http://www.fda.gov/medicaldevices/productsandmedicalprocedures/deviceapprovalsandclearances/pmaapprovals/default.htm",
                 "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfPMA/pma.cfm"
             ],
-            "title": "Premarket Approvals (PMA)",
-            "describedBy": "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/Databases/ucm135279.htm"
+            "title": "Premarket Approvals (PMA)"
         },
         {
             "accessLevel": "public",
@@ -1836,16 +1836,17 @@
             "description": "The National Health Related Items Code (NHRIC) is a system for identification and numbering of marketed device packages that is compatible with other numbering systems such as the National Drug Code (NDC) or Universal Product Code (UPC). Those manufacturers who desire to use the NHRIC number for unique product identification may apply to FDA for a labeler code. This database contains NHRIC data retrieved from records that date back 20 years.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfNHRIC/nhric.cfm",
-                    "mediaType": "text/html",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfNHRIC/nhric.cfm",
-                    "format": "Interactive on-screen"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfNHRIC/nhric.cfm",
+                    "format": "Interactive on-screen",
+                    "mediaType": "text/html"
                 }
             ],
             "identifier": "72b6e176-fd0a-48eb-b373-38812dd98baa",
             "keyword": [
                 "cdrh"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfNHRIC/nhric.cfm",
             "modified": "2013-11-01",
             "programCode": [
                 "009:005"
@@ -1859,8 +1860,7 @@
             "references": [
                 "http://www.fda.gov/medicaldevices/deviceregulationandguidance/databases/ucm161456.htm"
             ],
-            "title": "NHRIC (National Health Related Items Code)",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfNHRIC/nhric.cfm"
+            "title": "NHRIC (National Health Related Items Code)"
         },
         {
             "accessLevel": "public",
@@ -1872,19 +1872,19 @@
                 "hasEmail": "mailto:open@fda.hhs.gov"
             },
             "description": "This database allows you to search the CDRH's database information on medical devices which may have malfunctioned or caused a death or serious injury during the years 1992 through 1996.",
-            "temporal": "1992-01-01/1996-07-31",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfmdr/search.CFM",
-                    "mediaType": "text/html",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfmdr/search.CFM",
-                    "format": "Interactive on-screen"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfmdr/search.CFM",
+                    "format": "Interactive on-screen",
+                    "mediaType": "text/html"
                 }
             ],
             "identifier": "290bc7d6-538c-4889-823f-2ec60b6d3b6a",
             "keyword": [
                 "cdrh"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfmdr/search.CFM",
             "modified": "1996-07-31",
             "programCode": [
                 "009:005"
@@ -1898,8 +1898,8 @@
             "references": [
                 "http://www.fda.gov/MedicalDevices/Safety/ReportaProblem/ucm124073.htm"
             ],
-            "title": "MDR (Medical Device Reporting)",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfmdr/search.CFM"
+            "temporal": "1992-01-01/1996-07-31",
+            "title": "MDR (Medical Device Reporting)"
         },
         {
             "accessLevel": "public",
@@ -1911,19 +1911,19 @@
                 "hasEmail": "mailto:open@fda.hhs.gov"
             },
             "description": "MAUDE data represents reports of adverse events involving medical devices. The data consists of all voluntary reports since June, 1993, user facility reports since 1991, distributor reports since 1993, and manufacturer reports since August, 1996.",
-            "temporal": "1991-01-01/2013-10-31",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfMAUDE/search.CFM",
-                    "mediaType": "text/html",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfMAUDE/search.CFM",
-                    "format": "Interactive on-screen"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfMAUDE/search.CFM",
+                    "format": "Interactive on-screen",
+                    "mediaType": "text/html"
                 }
             ],
             "identifier": "1327f116-da9f-40b9-babd-c893ab2ceacd",
             "keyword": [
                 "cdrh"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfMAUDE/search.CFM",
             "modified": "2013-10-31",
             "programCode": [
                 "009:005"
@@ -1937,8 +1937,8 @@
             "references": [
                 "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/PostmarketRequirements/ReportingAdverseEvents/ucm127891.htm"
             ],
-            "title": "MAUDE (Manufacturer and User Facility Device Experience)",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfMAUDE/search.CFM"
+            "temporal": "1991-01-01/2013-10-31",
+            "title": "MAUDE (Manufacturer and User Facility Device Experience)"
         },
         {
             "accessLevel": "public",
@@ -1952,16 +1952,17 @@
             "description": "Searchable listing of Over-the-Counter tests (OTC) and collection kits that have been cleared or approved by the FDA",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfIVD/Search.cfm",
-                    "mediaType": "text/html",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfIVD/Search.cfm",
-                    "format": "Interactive on-screen"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfIVD/Search.cfm",
+                    "format": "Interactive on-screen",
+                    "mediaType": "text/html"
                 }
             ],
             "identifier": "abf2baea-8af9-4507-8d28-641ed80f2021",
             "keyword": [
                 "cdrh"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfIVD/Search.cfm",
             "modified": "2013-11-01",
             "programCode": [
                 "009:005"
@@ -1972,8 +1973,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "IVD Home Use Lab Tests (Over The Counter) Tests",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfIVD/Search.cfm"
+            "title": "IVD Home Use Lab Tests (Over The Counter) Tests"
         },
         {
             "accessLevel": "public",
@@ -1987,16 +1987,17 @@
             "description": "The Mammography Facility Database is updated periodically based on information received from the four FDA-approved accreditation bodies: the American College of Radiology (ACR), and the States of Arkansas, Iowa, and Texas. Information received by FDA or Certifying State from accreditation bodies does not specify if the facility is mobile or stationary. In many instances, but not all, the accreditation body notes Mobile following the name of the facility. The certification status of facilities may change, so FDA suggests that you check the facility's current status and look for the MQSA certificate.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfMQSA/mqsa.cfm",
-                    "mediaType": "text/html",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfMQSA/mqsa.cfm",
-                    "format": "Interactive on-screen"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfMQSA/mqsa.cfm",
+                    "format": "Interactive on-screen",
+                    "mediaType": "text/html"
                 }
             ],
             "identifier": "705ec42c-0f47-4afd-9096-a73b28958348",
             "keyword": [
                 "cdrh"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfMQSA/mqsa.cfm",
             "modified": "2013-11-01",
             "programCode": [
                 "009:005"
@@ -2007,8 +2008,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Mammography Facilities",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfMQSA/mqsa.cfm"
+            "title": "Mammography Facilities"
         },
         {
             "accessLevel": "public",
@@ -2022,16 +2022,17 @@
             "description": "This database contains the commercially marketed in vitro test systems categorized as CLIA waived by the FDA since January 31, 2000, and by the Centers for Disease Control and Prevention (CDC) prior to that date. CLIA waived test systems are waived from certain CLIA laboratory requirements (42 CFR Part 493). ",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfClia/analyteswaived.cfm",
-                    "mediaType": "text/html",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfClia/analyteswaived.cfm",
-                    "format": "Interactive on-screen"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfClia/analyteswaived.cfm",
+                    "format": "Interactive on-screen",
+                    "mediaType": "text/html"
                 }
             ],
             "identifier": "3f3f0bb7-1c03-415a-90ca-400bfc08f096",
             "keyword": [
                 "cdrh"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfClia/analyteswaived.cfm",
             "modified": "2013-11-01",
             "programCode": [
                 "009:005"
@@ -2042,8 +2043,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "CLIA Currently Waived Analytes",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfClia/analyteswaived.cfm"
+            "title": "CLIA Currently Waived Analytes"
         },
         {
             "accessLevel": "public",
@@ -2057,16 +2057,17 @@
             "description": "This database contains the commercially marketed in vitro test systems categorized by the FDA since January 31, 2000, and tests categorized by the Centers for Disease Control and Prevention (CDC) prior to that date.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfCLIA/clia.cfm",
-                    "mediaType": "text/html",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfCLIA/clia.cfm",
-                    "format": "Interactive on-screen"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfCLIA/clia.cfm",
+                    "format": "Interactive on-screen",
+                    "mediaType": "text/html"
                 }
             ],
             "identifier": "c13343cf-eda1-425d-b346-6186c92e3992",
             "keyword": [
                 "cdrh"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfCLIA/clia.cfm",
             "modified": "2013-11-01",
             "programCode": [
                 "009:005"
@@ -2077,8 +2078,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Clinical Laboratory Improvement Amendments ",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfCLIA/clia.cfm"
+            "title": "Clinical Laboratory Improvement Amendments "
         },
         {
             "accessLevel": "public",
@@ -2092,10 +2092,10 @@
             "description": "This database contains the most recent revision from the Government Printing Office (GPO) of the Code of Federal Regulations (CFR) Title 21 - Food and Drugs.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfcfr/cfrsearch.cfm",
-                    "mediaType": "text/html",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfcfr/cfrsearch.cfm",
-                    "format": "Interactive on-screen"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfcfr/cfrsearch.cfm",
+                    "format": "Interactive on-screen",
+                    "mediaType": "text/html"
                 }
             ],
             "identifier": "f1b5d989-b06e-46b6-a992-4b753912656b",
@@ -2103,6 +2103,7 @@
                 "cdrh",
                 "regulations"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfcfr/cfrsearch.cfm",
             "modified": "2013-04-01",
             "programCode": [
                 "009:005"
@@ -2113,11 +2114,11 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Code of Federal Regulations Title 21",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfcfr/cfrsearch.cfm"
+            "title": "Code of Federal Regulations Title 21"
         },
         {
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "009:10"
             ],
@@ -2128,17 +2129,17 @@
             "description": "The CDRH Inspections Database provides information about medical device inspections that were the responsibility of CDRH from 2008 to the present.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfTPLC/inspect.cfm",
-                    "mediaType": "text/html",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfTPLC/inspect.cfm",
-                    "format": "Interactive on-line"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfTPLC/inspect.cfm",
+                    "format": "Interactive on-line",
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1W",
             "identifier": "fe84d43d-cad9-4dce-93d8-919358244618",
             "keyword": [
                 "cdrh"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfTPLC/inspect.cfm",
             "modified": "R/P1Y",
             "programCode": [
                 "009:005"
@@ -2149,8 +2150,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "CDRH Inspections Database",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfTPLC/inspect.cfm"
+            "title": "CDRH Inspections Database"
         },
         {
             "accessLevel": "public",
@@ -2162,19 +2162,19 @@
                 "hasEmail": "mailto:open@fda.hhs.gov"
             },
             "description": "This database contains historical information about CDRH Advisory Committees and Panel meetings through 2008, including summaries and transcripts. ",
-            "temporal": "2001-01-01/2009-12-31",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfAdvisory/search.cfm",
-                    "mediaType": "text/html",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfAdvisory/search.cfm",
-                    "format": "Interactive on-line"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfAdvisory/search.cfm",
+                    "format": "Interactive on-line",
+                    "mediaType": "text/html"
                 }
             ],
             "identifier": "a76c0c50-76f5-42bc-911c-703287648b52",
             "keyword": [
                 "labeling"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfAdvisory/search.cfm",
             "modified": "2009-12-31",
             "programCode": [
                 "009:005"
@@ -2185,8 +2185,8 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "CDRH Advisory Meeting Materials Archive",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfAdvisory/search.cfm"
+            "temporal": "2001-01-01/2009-12-31",
+            "title": "CDRH Advisory Meeting Materials Archive"
         },
         {
             "accessLevel": "public",
@@ -2198,13 +2198,12 @@
                 "hasEmail": "mailto:open@fda.hhs.gov"
             },
             "description": "An inventory of all FDA Datasets",
-            "temporal": "1900-01-01/2013-12-31",
             "distribution": [
                 {
-                    "downloadURL": "http://open.fda.gov/data.json",
-                    "mediaType": "application/json",
                     "accessURL": "http://open.fda.gov/data.json",
-                    "format": "JSON"
+                    "downloadURL": "http://open.fda.gov/data.json",
+                    "format": "JSON",
+                    "mediaType": "application/json"
                 }
             ],
             "identifier": "38fda70b-9734-4df0-ada6-897455bb7f7b",
@@ -2212,6 +2211,7 @@
                 "data-json",
                 "inventory"
             ],
+            "landingPage": "http://open.fda.gov/data.json",
             "modified": "2013-12-20",
             "programCode": [
                 "009:005"
@@ -2222,8 +2222,8 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "FDA Data Inventory",
-            "landingPage": "http://open.fda.gov/data.json"
+            "temporal": "1900-01-01/2013-12-31",
+            "title": "FDA Data Inventory"
         },
         {
             "accessLevel": "public",
@@ -2235,13 +2235,12 @@
                 "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
             },
             "description": "The Adverse Event Reporting System (AERS) is a computerized information database designed to support the FDA's post-marketing safety surveillance program for all approved drug and therapeutic biologic products. The FDA uses AERS to monitor for new adverse events and medication errors that might occur with these marketed products. Reporting of adverse events from the point of care is voluntary in the United States. FDA receives some adverse event and medication error reports directly from health care professionals (such as physicians, pharmacists, nurses and others) and consumers (such as patients, family members, lawyers and others). Healthcare professionals and consumers may also report these events to the products' manufacturers. If a manufacturer receives an adverse event report, it is required to send the report to FDA as specified by regulations.  The files listed on this page contain raw data extracted from the AERS database for the indicated time ranges and are not cumulative. Users of these files need to be familiar with creation of relational databases using applications such as ORACLE, Microsoft Office Access, MySQL and IBM DB2 or the use of ASCII files with SAS analytic tools. A simple search of AERS data cannot be performed with these files by persons who are not familiar with creation of relational databases.",
-            "temporal": "2004-01-01/2012-12-31",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/ucm082193.htm",
-                    "mediaType": "application/zip",
                     "accessURL": "http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/default.htm",
-                    "format": "Zip"
+                    "downloadURL": "http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/ucm082193.htm",
+                    "format": "Zip",
+                    "mediaType": "application/zip"
                 }
             ],
             "identifier": "b454bed2-730a-4e06-becb-0f599f2ad62a",
@@ -2249,6 +2248,7 @@
                 "adverse event",
                 "human drugs"
             ],
+            "landingPage": "http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/default.htm",
             "modified": "2004-01-01",
             "programCode": [
                 "009:000"
@@ -2259,8 +2259,8 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Adverse Event Reporting System (AERS)",
-            "landingPage": "http://www.fda.gov/Drugs/GuidanceComplianceRegulatoryInformation/Surveillance/AdverseDrugEffects/default.htm"
+            "temporal": "2004-01-01/2012-12-31",
+            "title": "Adverse Event Reporting System (AERS)"
         },
         {
             "accessLevel": "public",
@@ -2272,13 +2272,12 @@
                 "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
             },
             "description": "This list is intended to alert consumers about Web sites that are or were illegally marketing unapproved, uncleared, or unauthorized products in relation to the 2009 H1N1 Flu Virus (sometimes referred to as the 'swine flu' virus).",
-            "temporal": "2009-01-01/2009-12-31",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225441.htm",
-                    "mediaType": "application/vnd.ms-excel",
                     "accessURL": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225441.htm",
-                    "format": "Excel"
+                    "downloadURL": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225441.htm",
+                    "format": "Excel",
+                    "mediaType": "application/vnd.ms-excel"
                 }
             ],
             "identifier": "9cc0d11d-dbcd-41a7-8947-02774d10ce2e",
@@ -2291,6 +2290,7 @@
                 "recalls",
                 "safety"
             ],
+            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225441.htm",
             "modified": "2010-10-01",
             "programCode": [
                 "009:000"
@@ -2301,8 +2301,8 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Fraudulent 2009 H1N1 Influenza Products Widget",
-            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225441.htm"
+            "temporal": "2009-01-01/2009-12-31",
+            "title": "Fraudulent 2009 H1N1 Influenza Products Widget"
         },
         {
             "accessLevel": "public",
@@ -2316,9 +2316,9 @@
             "description": "POCA is a software that produces a data set used internally to assess the  safety, and feasibility of proposed proprietary drug names.  FDA product name safety evaluators have access to an internal version of the POCA system behind the FDA firewall.   Source code to develop external non-FDA instances of POCA are available at http://www.fda.gov/Drugs/ResourcesForYou/Industry/ucm400127.htm",
             "distribution": [
                 {
-                    "mediaType": "application/pdf",
                     "accessURL": "http://www.fda.gov/Drugs/ResourcesForYou/Industry/ucm400127.htm",
-                    "format": "Interactive on-line"
+                    "format": "Interactive on-line",
+                    "mediaType": "application/pdf"
                 }
             ],
             "identifier": "78e2c44a-948a-4f20-a810-6f1e60cee0d1",
@@ -2342,6 +2342,7 @@
         },
         {
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "009:10"
             ],
@@ -2352,18 +2353,18 @@
             "description": "Whereas not all recalls are announced in the media or on our Recalls press release page, all recalls montiored by FDA are included in FDA's weekly Enforcement Report once they are classified according to the level of hazard involved. ",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/Safety/Recalls/EnforcementReports/default.htm",
-                    "mediaType": "text/html",
                     "accessURL": "http://www.fda.gov/Safety/Recalls/EnforcementReports/default.htm",
-                    "format": "Interactive on-screen"
+                    "downloadURL": "http://www.fda.gov/Safety/Recalls/EnforcementReports/default.htm",
+                    "format": "Interactive on-screen",
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1W",
             "identifier": "99f89749-f77f-4d0f-a415-8c7b633bac1f",
             "keyword": [
                 "ora",
                 "regulations"
             ],
+            "landingPage": "http://www.fda.gov/Safety/Recalls/EnforcementReports/default.htm",
             "modified": "R/P1W",
             "programCode": [
                 "009:008"
@@ -2374,11 +2375,11 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Enforcement Reports",
-            "landingPage": "http://www.fda.gov/Safety/Recalls/EnforcementReports/default.htm"
+            "title": "Enforcement Reports"
         },
         {
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1W",
             "bureauCode": [
                 "009:10"
             ],
@@ -2389,18 +2390,18 @@
             "description": "An index of FDA warning letters issued to companies operating in the United States.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/DataSets/WarningLetters/WarningLettersDataSet.xml",
-                    "mediaType": "application/xml",
                     "accessURL": "http://www.fda.gov/DataSets/WarningLetters/WarningLettersDataSet.xml",
-                    "format": "XML"
+                    "downloadURL": "http://www.fda.gov/DataSets/WarningLetters/WarningLettersDataSet.xml",
+                    "format": "XML",
+                    "mediaType": "application/xml"
                 }
             ],
-            "accrualPeriodicity": "R/P1W",
             "identifier": "8ab03039-617f-469d-bf37-b4f844372945",
             "keyword": [
                 "ora",
                 "regulations"
             ],
+            "landingPage": "http://www.fda.gov/ICECI/EnforcementActions/WarningLetters/2013/default.htm",
             "modified": "R/P1W",
             "programCode": [
                 "009:008"
@@ -2411,8 +2412,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Warning Letters",
-            "landingPage": "http://www.fda.gov/ICECI/EnforcementActions/WarningLetters/2013/default.htm"
+            "title": "Warning Letters"
         },
         {
             "accessLevel": "public",
@@ -2426,16 +2426,17 @@
             "description": "FDA is disclosing the final inspection classification for inspections related to currently marketed FDA-regulated products. The disclosure of this information is not intended to interfere with planned enforcement actions, therefore some information may be withheld from posting until such action is taken.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/downloads/ICECI/EnforcementActions/UCM224485.xls",
-                    "mediaType": "application/vnd.ms-excel",
                     "accessURL": "http://www.fda.gov/downloads/ICECI/EnforcementActions/UCM224485.xls",
-                    "format": "Excel"
+                    "downloadURL": "http://www.fda.gov/downloads/ICECI/EnforcementActions/UCM224485.xls",
+                    "format": "Excel",
+                    "mediaType": "application/vnd.ms-excel"
                 }
             ],
             "identifier": "7731ca41-583e-45b1-b810-2caf33000e39",
             "keyword": [
                 "ora"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/inspsearch/",
             "modified": "2013-08-31",
             "programCode": [
                 "009:008"
@@ -2446,11 +2447,11 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Inspection Database",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/inspsearch/"
+            "title": "Inspection Database"
         },
         {
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1M",
             "bureauCode": [
                 "009:10"
             ],
@@ -2461,17 +2462,17 @@
             "description": "Disclosure of reporting citations provide the public with a rationale for the Agency\ufffds enforcement actions and will also help to inform public and industry decision-making, allowing them to make more informed marketplace choices and help to encourage compliance.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/ICECI/EnforcementActions/ucm346077.htm",
-                    "mediaType": "application/vnd.ms-excel",
                     "accessURL": "http://www.fda.gov/ICECI/EnforcementActions/ucm346077.htm",
-                    "format": "Excel"
+                    "downloadURL": "http://www.fda.gov/ICECI/EnforcementActions/ucm346077.htm",
+                    "format": "Excel",
+                    "mediaType": "application/vnd.ms-excel"
                 }
             ],
-            "accrualPeriodicity": "R/P1M",
             "identifier": "74aed734-91b4-41f2-8418-a0aae396f9ef",
             "keyword": [
                 "ora"
             ],
+            "landingPage": "http://www.fda.gov/ICECI/EnforcementActions/ucm346077.htm",
             "modified": "R/P1M",
             "programCode": [
                 "009:008"
@@ -2482,11 +2483,11 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Inspection Citations",
-            "landingPage": "http://www.fda.gov/ICECI/EnforcementActions/ucm346077.htm"
+            "title": "Inspection Citations"
         },
         {
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1D",
             "bureauCode": [
                 "009:10"
             ],
@@ -2497,18 +2498,18 @@
             "description": "The Electronic Animal Drug Product Listing Directory is a directory of all animal drug products that have been listed electronically since June 1, 2009, to comply with changes enacted as part of the FDA Amendments Act of 2007.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/downloads/ForIndustry/DataStandards/StructuredProductLabeling/UCM362817.zip",
-                    "mediaType": "application/zip",
                     "accessURL": "http://www.fda.gov/downloads/ForIndustry/DataStandards/StructuredProductLabeling/UCM362817.zip",
-                    "format": "ZIP"
+                    "downloadURL": "http://www.fda.gov/downloads/ForIndustry/DataStandards/StructuredProductLabeling/UCM362817.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip"
                 }
             ],
-            "accrualPeriodicity": "R/P1D",
             "identifier": "e3b58aa4-eb31-406f-a766-1a4f2da87565",
             "keyword": [
                 "cvm",
                 "labeling"
             ],
+            "landingPage": "http://www.fda.gov/ForIndustry/DataStandards/StructuredProductLabeling/ucm191015.htm",
             "modified": "R/P1D",
             "programCode": [
                 "009:004"
@@ -2519,11 +2520,11 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Electronic Animal Drug Product Listing Directory",
-            "landingPage": "http://www.fda.gov/ForIndustry/DataStandards/StructuredProductLabeling/ucm191015.htm"
+            "title": "Electronic Animal Drug Product Listing Directory"
         },
         {
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:10"
             ],
@@ -2534,18 +2535,18 @@
             "description": "On November 16, 1988, the President of the United States signed into law the Generic Animal Drug and Patent Restoration Act (GADPTRA). Among its major provisions, the Act extends eligibility for submission of Abbreviated New Animal Drug Applications (ANADAs) to all animal drug products approved for safety and effectiveness under the Federal Food, Drug, and Cosmetic Act. The Act also requires that each sponsor of an approved animal drug product submit to the FDA certain information regarding patents held for the animal drug or its method of use. The Act requires that this information, as well as a list of all animal drug products approved for safety and effectiveness, be made available to the public. This list must be updated monthly under the provisions of the Act. This publication, which is known as the \ufffdGreen Book\ufffd, was first published in January of 1989. Updates have been added monthly since then. The list is published in its entirety each January. ",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/animaldrugsatfda/index.cfm",
-                    "mediaType": "text/html",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/animaldrugsatfda/index.cfm",
-                    "format": "Interactive on-screen"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/animaldrugsatfda/index.cfm",
+                    "format": "Interactive on-screen",
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
             "identifier": "ee7073db-55c0-46b0-b831-1c659fe7137d",
             "keyword": [
                 "cvm",
                 "labeling"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/animaldrugsatfda/index.cfm",
             "modified": "R/P1Y",
             "programCode": [
                 "009:004"
@@ -2556,8 +2557,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Approved Animal Drug Products (Green Book)",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/animaldrugsatfda/index.cfm"
+            "title": "Approved Animal Drug Products (Green Book)"
         },
         {
             "accessLevel": "public",
@@ -2571,10 +2571,10 @@
             "description": "The drug labels and other drug-specific information on this Web site represent the most recent drug listing information companies have submitted to the Food and Drug Administration (FDA). (See 21 CFR part 207.) The drug labeling and other information has been reformatted to make it easier to read but its content has neither been altered nor verified by FDA. The drug labeling on this Web site may not be the labeling on currently distributed products or identical to the labeling that is approved. Most OTC drugs are not reviewed and approved by FDA, however they may be marketed if they comply with applicable regulations and policies described in monographs. Drugs marked 'OTC monograph final' or OTC monograph not final' are not checked for conformance to the monograph. Drugs marked 'unapproved medical gas', 'unapproved homeopathic' or 'unapproved drug other' on this Web site have not been evaluated by FDA for safety and efficacy and their labeling has not been approved. In addition, FDA is not aware of scientific evidence to support homeopathy as effective.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/ForIndustry/DataStandards/StructuredProductLabeling/ucm240580.htm",
-                    "mediaType": "application/zip",
                     "accessURL": "http://dailymed.nlm.nih.gov/dailymed/downloadLabels.cfm",
-                    "format": "ZIP"
+                    "downloadURL": "http://www.fda.gov/ForIndustry/DataStandards/StructuredProductLabeling/ucm240580.htm",
+                    "format": "ZIP",
+                    "mediaType": "application/zip"
                 }
             ],
             "identifier": "ff9c9ee2-8c73-4142-b21f-2b694db8f783",
@@ -2587,6 +2587,7 @@
                 "labels fda gov",
                 "labeling"
             ],
+            "landingPage": "http://labels.fda.gov/",
             "modified": "2013-11-26",
             "programCode": [
                 "009:002"
@@ -2597,8 +2598,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "FDA Online Label Repository",
-            "landingPage": "http://labels.fda.gov/"
+            "title": "FDA Online Label Repository"
         },
         {
             "accessLevel": "public",
@@ -2612,16 +2612,17 @@
             "description": "This application provides Human Cell and Tissue registration information for registered, inactive, and pre-registered firms. Query options are by Establishment Name, Establishment Function, Product, Establishment Status, State, Zip Code, and Country.",
             "distribution": [
                 {
-                    "downloadURL": "https://www.accessdata.fda.gov/scripts/cber/CFAppsPub/tiss/index.cfm",
-                    "mediaType": "text/html",
                     "accessURL": "https://www.accessdata.fda.gov/scripts/cber/CFAppsPub/tiss/index.cfm",
-                    "format": "Interactive on-screen"
+                    "downloadURL": "https://www.accessdata.fda.gov/scripts/cber/CFAppsPub/tiss/index.cfm",
+                    "format": "Interactive on-screen",
+                    "mediaType": "text/html"
                 }
             ],
             "identifier": "dc73689d-c8cc-4c9f-b3ee-c293483dbdb7",
             "keyword": [
                 "cber"
             ],
+            "landingPage": "https://www.accessdata.fda.gov/scripts/cber/CFAppsPub/tiss/index.cfm",
             "modified": "2008-04-10",
             "programCode": [
                 "009:003"
@@ -2632,8 +2633,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Human Cell and Tissue Establishment Registration Public Query",
-            "landingPage": "https://www.accessdata.fda.gov/scripts/cber/CFAppsPub/tiss/index.cfm"
+            "title": "Human Cell and Tissue Establishment Registration Public Query"
         },
         {
             "accessLevel": "public",
@@ -2647,10 +2647,10 @@
             "description": "This contains information that identifies clinical investigators, contract research organizations, and institutional review boards involved in the conduct of Investigational New Drug (IND) studies with human investigational drugs and therapeutic biologics.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/downloads/Drugs/InformationOnDrugs/UCM135169.zip",
-                    "mediaType": "application/zip",
                     "accessURL": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm135162.htm",
-                    "format": "Zipped TXT"
+                    "downloadURL": "http://www.fda.gov/downloads/Drugs/InformationOnDrugs/UCM135169.zip",
+                    "format": "Zipped TXT",
+                    "mediaType": "application/zip"
                 }
             ],
             "identifier": "8d346d8d-33c7-47f8-890d-a4ced16e45dd",
@@ -2658,6 +2658,7 @@
                 "cder",
                 "BMIS"
             ],
+            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm135162.htm",
             "modified": "2013-08-29",
             "programCode": [
                 "009:002"
@@ -2668,8 +2669,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "Bioresearch Monitonoring Information System (BMIS)",
-            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm135162.htm"
+            "title": "Bioresearch Monitonoring Information System (BMIS)"
         },
         {
             "accessLevel": "public",
@@ -2683,10 +2683,10 @@
             "description": "The publication Approved Drug Products with Therapeutic Equivalence Evaluations (the List, commonly known as the Orange Book) identifies drug products approved on the basis of safety and effectiveness by the Food and Drug Administration (FDA) under the Federal Food, Drug, and Cosmetic Act (the Act). (For more information, see the Orange Book Preface.)",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/downloads/Drugs/InformationOnDrugs/UCM163762.zip",
-                    "mediaType": "application/zip",
                     "accessURL": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm129662.htm",
-                    "format": "Zipped TXT"
+                    "downloadURL": "http://www.fda.gov/downloads/Drugs/InformationOnDrugs/UCM163762.zip",
+                    "format": "Zipped TXT",
+                    "mediaType": "application/zip"
                 }
             ],
             "identifier": "c7b84420-8e01-44eb-92de-c5e7f975ab28",
@@ -2694,6 +2694,7 @@
                 "cder",
                 "orange book"
             ],
+            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm129662.htm",
             "modified": "2013-10-31",
             "programCode": [
                 "009:002"
@@ -2707,8 +2708,7 @@
             "references": [
                 "http://www.accessdata.fda.gov/scripts/cder/ob/default.cfm"
             ],
-            "title": "Approved Drug Products with Therapuetic Equivalence Evaluations (Orange Book)",
-            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm129662.htm"
+            "title": "Approved Drug Products with Therapuetic Equivalence Evaluations (Orange Book)"
         },
         {
             "accessLevel": "public",
@@ -2722,16 +2722,17 @@
             "description": "The FDA Acronyms and Abbreviations database provides a quick reference to acronyms and abbreviations related to Food and Drug Administration (FDA) activities",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/AboutFDA/FDAAcronymsAbbreviations/ucm070296.htm",
-                    "mediaType": "application/zip",
                     "accessURL": "http://www.fda.gov/AboutFDA/FDAAcronymsAbbreviations/ucm070296.htm",
-                    "format": "Zipped text"
+                    "downloadURL": "http://www.fda.gov/AboutFDA/FDAAcronymsAbbreviations/ucm070296.htm",
+                    "format": "Zipped text",
+                    "mediaType": "application/zip"
                 }
             ],
             "identifier": "4dc9ed1a-1287-40e5-9c14-41011aac1308",
             "keyword": [
                 "definitions"
             ],
+            "landingPage": "http://www.fda.gov/AboutFDA/FDAAcronymsAbbreviations/default.htm",
             "modified": "2012-04-04",
             "programCode": [
                 "009:002"
@@ -2745,8 +2746,7 @@
             "references": [
                 "http://www.accessdata.fda.gov/scripts/cder/acronyms/index.cfm"
             ],
-            "title": "FDA Acronyms and Abbreviations",
-            "landingPage": "http://www.fda.gov/AboutFDA/FDAAcronymsAbbreviations/default.htm"
+            "title": "FDA Acronyms and Abbreviations"
         },
         {
             "accessLevel": "public",
@@ -2757,13 +2757,14 @@
                 "fn": "openFDA",
                 "hasEmail": "mailto:open@fda.hhs.gov"
             },
+            "describedBy": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm254527.htm",
             "description": "The Drug Listing Act of 1972 requires registered drug establishments to provide the Food and Drug Administration (FDA) with a current list of all drugs manufactured, prepared, propagated, compounded, or processed by it for commercial distribution. (See Section 510 of the Federal Food, Drug, and Cosmetic Act (Act) (21 U.S.C. \ufffd 360)). Drug products are identified and reported using a unique, three-segment number, called the National Drug Code (NDC), which serves as a universal product identifier for drugs. FDA publishes the listed NDC numbers and the information submitted as part of the listing information in the NDC Directory which is updated daily.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/downloads/Drugs/DevelopmentApprovalProcess/UCM070838.zip",
-                    "mediaType": "application/zip",
                     "accessURL": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm142438.htm",
-                    "format": "ZIP"
+                    "downloadURL": "http://www.fda.gov/downloads/Drugs/DevelopmentApprovalProcess/UCM070838.zip",
+                    "format": "ZIP",
+                    "mediaType": "application/zip"
                 }
             ],
             "identifier": "2b7ec03d-67dc-4544-b1d6-b9aa02f693c6",
@@ -2771,6 +2772,7 @@
                 "cder",
                 "NDC"
             ],
+            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm142438.htm",
             "modified": "2013-11-14",
             "programCode": [
                 "009:002"
@@ -2785,9 +2787,7 @@
                 "http://www.accessdata.fda.gov/scripts/cder/ndc/default.cfm",
                 "http://www.fda.gov/downloads/Drugs/InformationOnDrugs/UCM257244.zip"
             ],
-            "title": "National Drug Code Directory",
-            "describedBy": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm254527.htm",
-            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm142438.htm"
+            "title": "National Drug Code Directory"
         },
         {
             "accessLevel": "public",
@@ -2801,16 +2801,17 @@
             "description": "The Medical Product Safety Network (MedSun) is an adverse event reporting program launched in 2002. The primary goal for MedSun is to work collaboratively with the clinical community to identify, understand, and solve problems with the use of medical devices.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/Medsun/searchReportText.cfm",
-                    "mediaType": "text/html",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/Medsun/searchReportText.cfm",
-                    "format": "Interactive on-screen"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/Medsun/searchReportText.cfm",
+                    "format": "Interactive on-screen",
+                    "mediaType": "text/html"
                 }
             ],
             "identifier": "068aa9da-ef7e-419a-9de2-2a690dbec65b",
             "keyword": [
                 "cdrh"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/Medsun/searchReportText.cfm",
             "modified": "2013-11-13",
             "programCode": [
                 "009:005"
@@ -2821,8 +2822,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "MedSun Reports",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/Medsun/searchReportText.cfm"
+            "title": "MedSun Reports"
         },
         {
             "accessLevel": "public",
@@ -2836,16 +2836,17 @@
             "description": "The CDRH FOIA electronic reading room contains frequently requested information via the Freedom of Information Act from the Center for Devices and Radiological Health.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/devicesatfda/readingroom.cfm",
-                    "mediaType": "application/pdf",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/cdrh/devicesatfda/readingroom.cfm",
-                    "format": "PDF"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/devicesatfda/readingroom.cfm",
+                    "format": "PDF",
+                    "mediaType": "application/pdf"
                 }
             ],
             "identifier": "650b8214-c3a4-46f6-8a10-5d182339c0d6",
             "keyword": [
                 "cdrh"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/devicesatfda/readingroom.cfm",
             "modified": "2013-11-01",
             "programCode": [
                 "009:005"
@@ -2856,11 +2857,11 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "CDRH FOIA Electronic Reading Room",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/devicesatfda/readingroom.cfm"
+            "title": "CDRH FOIA Electronic Reading Room"
         },
         {
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P1Y",
             "bureauCode": [
                 "009:10"
             ],
@@ -2871,17 +2872,17 @@
             "description": "Federal regulations require that an assembler who installs one or more certified components of a diagnostic x-ray system submit a report of assembly. This database contains the releasable information submitted including Equipment Location, General Information and Component Information. Note: Data does not include dental system installations. ",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/Databases/ucm135419.htm",
-                    "mediaType": "application/zip",
                     "accessURL": "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/Databases/ucm135419.htm",
-                    "format": "Zip"
+                    "downloadURL": "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/Databases/ucm135419.htm",
+                    "format": "Zip",
+                    "mediaType": "application/zip"
                 }
             ],
-            "accrualPeriodicity": "R/P1Y",
             "identifier": "aae3533d-6b69-4648-833c-a73700e51f51",
             "keyword": [
                 "cdrh"
             ],
+            "landingPage": "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/Databases/ucm135419.htm",
             "modified": "R/P1Y",
             "programCode": [
                 "009:005"
@@ -2896,11 +2897,11 @@
                 "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/Databases/ucm135419.htm#zip",
                 "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfAssem/assembler.cfm"
             ],
-            "title": "X-Ray Assembler Data",
-            "landingPage": "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/Databases/ucm135419.htm"
+            "title": "X-Ray Assembler Data"
         },
         {
             "accessLevel": "public",
+            "accrualPeriodicity": "R/P3M",
             "bureauCode": [
                 "009:10"
             ],
@@ -2911,17 +2912,17 @@
             "description": "This database consists of those national and international standards recognized by FDA which manufacturers can declare conformity to and is part of the information the Center can use to make an appropriate decision regarding the clearance or approval of a submission. Information submitted on conformance with such standards will have a direct bearing on safety and effectiveness determinations made during the review of IDEs, HDEs, PMAs, and PDPs. Conformance with recognized consensus standards in and of itself, however, may not always be a sufficient basis for regulatory decisions.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfStandards/search.cfm",
-                    "mediaType": "text/html",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfStandards/search.cfm",
-                    "format": "Interactive on-screen"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfStandards/search.cfm",
+                    "format": "Interactive on-screen",
+                    "mediaType": "text/html"
                 }
             ],
-            "accrualPeriodicity": "R/P3M",
             "identifier": "4b318035-9f0e-4f7e-b4ff-c70fd57b4994",
             "keyword": [
                 "cdrh"
             ],
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfStandards/search.cfm",
             "modified": "R/P3M",
             "programCode": [
                 "009:005"
@@ -2935,8 +2936,7 @@
             "references": [
                 "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/Standards/default.htm"
             ],
-            "title": "FDA Recognized Consensus Standards",
-            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfStandards/search.cfm"
+            "title": "FDA Recognized Consensus Standards"
         },
         {
             "accessLevel": "public",
@@ -2950,10 +2950,10 @@
             "description": "Contains data for FDA pistachio product recalls since March 2009.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225438.htm",
-                    "mediaType": "application/vnd.ms-excel",
                     "accessURL": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225438.htm",
-                    "format": "Excel"
+                    "downloadURL": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225438.htm",
+                    "format": "Excel",
+                    "mediaType": "application/vnd.ms-excel"
                 }
             ],
             "identifier": "64ae1af7-2b25-4d00-9dbf-244269123d2f",
@@ -2966,6 +2966,7 @@
                 "recalls",
                 "safety"
             ],
+            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225438.htm",
             "modified": "2010-10-01",
             "programCode": [
                 "009:000"
@@ -2976,8 +2977,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "FDA Pistachio Product Recalls Widget",
-            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225438.htm"
+            "title": "FDA Pistachio Product Recalls Widget"
         },
         {
             "accessLevel": "public",
@@ -2991,10 +2991,10 @@
             "description": "Contains data for FDA Hydrolyzed Vegetable Protein (HVP) Containing Products recalls since February, 2010.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225437.htm",
-                    "mediaType": "application/vnd.ms-excel",
                     "accessURL": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225437.htm",
-                    "format": "Excel"
+                    "downloadURL": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225437.htm",
+                    "format": "Excel",
+                    "mediaType": "application/vnd.ms-excel"
                 }
             ],
             "identifier": "1281388f-93e7-4c1c-9369-5143ec0fdb8e",
@@ -3007,6 +3007,7 @@
                 "recalls",
                 "safety"
             ],
+            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225437.htm",
             "modified": "2010-10-01",
             "programCode": [
                 "009:000"
@@ -3017,8 +3018,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "FDA Hydrolyzed Vegetable Protein (HVP) Containing Products Recalls Widget",
-            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225437.htm"
+            "title": "FDA Hydrolyzed Vegetable Protein (HVP) Containing Products Recalls Widget"
         },
         {
             "accessLevel": "public",
@@ -3032,10 +3032,10 @@
             "description": "Contains data for FDA peanut product recalls since January 2009.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225439.htm",
-                    "mediaType": "application/vnd.ms-excel",
                     "accessURL": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225439.htm",
-                    "format": "Excel"
+                    "downloadURL": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225439.htm",
+                    "format": "Excel",
+                    "mediaType": "application/vnd.ms-excel"
                 }
             ],
             "identifier": "486663d1-b2cd-4ccc-b221-6f9a155675e9",
@@ -3048,6 +3048,7 @@
                 "recalls",
                 "safety"
             ],
+            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225439.htm",
             "modified": "2010-10-01",
             "programCode": [
                 "009:000"
@@ -3058,8 +3059,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "FDA Peanut Product Recalls Widget",
-            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225439.htm"
+            "title": "FDA Peanut Product Recalls Widget"
         },
         {
             "accessLevel": "public",
@@ -3073,10 +3073,10 @@
             "description": "Contains data for FDA pet food recalls since January 1, 2006.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225435.htm",
-                    "mediaType": "application/unknown",
                     "accessURL": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225435.htm",
-                    "format": "application/unknown"
+                    "downloadURL": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225435.htm",
+                    "format": "application/unknown",
+                    "mediaType": "application/unknown"
                 }
             ],
             "identifier": "6e4c0c94-6b71-49f8-b551-c70a9070867e",
@@ -3088,6 +3088,7 @@
                 "recalls",
                 "safety"
             ],
+            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225435.htm",
             "modified": "2010-10-01",
             "programCode": [
                 "009:000"
@@ -3098,8 +3099,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "FDA Pet Health and Safety Widget",
-            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225435.htm"
+            "title": "FDA Pet Health and Safety Widget"
         },
         {
             "accessLevel": "public",
@@ -3113,10 +3113,10 @@
             "description": "Contains data for the FDA Plainview Milk Cooperative Ingredient Recall since June 2009.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/Milk/MilkRecallProducts2009.xls",
-                    "mediaType": "application/vnd.ms-excel",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/Milk/MilkRecallProducts2009.xls",
-                    "format": "Excel"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/Milk/MilkRecallProducts2009.xls",
+                    "format": "Excel",
+                    "mediaType": "application/vnd.ms-excel"
                 }
             ],
             "identifier": "5d970911-f35f-4514-9ddf-b20bc32790ff",
@@ -3130,6 +3130,7 @@
                 "recalls",
                 "safety"
             ],
+            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225440.htm",
             "modified": "2010-10-01",
             "programCode": [
                 "009:000"
@@ -3140,8 +3141,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "FDA Plainview Milk Cooperative Ingredient Recall",
-            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225440.htm"
+            "title": "FDA Plainview Milk Cooperative Ingredient Recall"
         },
         {
             "accessLevel": "public",
@@ -3155,10 +3155,10 @@
             "description": "Contains data for FDA pistachio product recalls since March 2009.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/pistachiorecall/Pistachio2009.xls",
-                    "mediaType": "application/vnd.ms-excel",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/pistachiorecall/Pistachio2009.xls",
-                    "format": "Excel"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/pistachiorecall/Pistachio2009.xls",
+                    "format": "Excel",
+                    "mediaType": "application/vnd.ms-excel"
                 }
             ],
             "identifier": "a501b289-fe9f-4c20-980f-f95f34c81f30",
@@ -3172,6 +3172,7 @@
                 "recalls",
                 "safety"
             ],
+            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225438.htm",
             "modified": "2010-10-01",
             "programCode": [
                 "009:000"
@@ -3182,8 +3183,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "FDA Pistachio Product Recalls",
-            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225438.htm"
+            "title": "FDA Pistachio Product Recalls"
         },
         {
             "accessLevel": "public",
@@ -3195,13 +3195,12 @@
                 "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
             },
             "description": "Contains data for FDA shell egg recalls.",
-            "temporal": "2010-01-01/2010-12-31",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/shelleggsrecall/ShellEggsRecallList2010.xls",
-                    "mediaType": "application/vnd.ms-excel",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/shelleggsrecall/ShellEggsRecallList2010.xls",
-                    "format": "Excel"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/shelleggsrecall/ShellEggsRecallList2010.xls",
+                    "format": "Excel",
+                    "mediaType": "application/vnd.ms-excel"
                 }
             ],
             "identifier": "dc522ec9-a996-440b-b94e-972136ab80c0",
@@ -3214,6 +3213,7 @@
                 "recalls",
                 "safety"
             ],
+            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225434.htm",
             "modified": "2010-10-01",
             "programCode": [
                 "009:000"
@@ -3224,8 +3224,8 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "FDA Shell Egg Recalls",
-            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225434.htm"
+            "temporal": "2010-01-01/2010-12-31",
+            "title": "FDA Shell Egg Recalls"
         },
         {
             "accessLevel": "public",
@@ -3239,10 +3239,10 @@
             "description": "Contains data for FDA Hydrolyzed Vegetable Protein (HVP) Containing Products recalls since February, 2010.",
             "distribution": [
                 {
-                    "downloadURL": "http://www.accessdata.fda.gov/scripts/HVPCP/HydrolyzedVegetableProteinProductsList2010.xls",
-                    "mediaType": "application/vnd.ms-excel",
                     "accessURL": "http://www.accessdata.fda.gov/scripts/HVPCP/HydrolyzedVegetableProteinProductsList2010.xls",
-                    "format": "Excel"
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/HVPCP/HydrolyzedVegetableProteinProductsList2010.xls",
+                    "format": "Excel",
+                    "mediaType": "application/vnd.ms-excel"
                 }
             ],
             "identifier": "97f8facf-a2b8-47f0-847b-d7e7bc165c09",
@@ -3256,6 +3256,7 @@
                 "recalls",
                 "safety"
             ],
+            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225437.htm",
             "modified": "2010-10-01",
             "programCode": [
                 "009:000"
@@ -3266,8 +3267,7 @@
                     "name": "U.S. Food and Drug Administration"
                 }
             },
-            "title": "FDA Hydrolyzed Vegetable Protein (HVP) Containing Products Recalls",
-            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225437.htm"
+            "title": "FDA Hydrolyzed Vegetable Protein (HVP) Containing Products Recalls"
         }
     ]
 }
```

