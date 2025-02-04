# Change History for cms.json

### Changes from 31606f9 to dd2190f (Part 1/5)
**Author:** Automated

**Date:** 2025-02-01 15:02:16+00:00

**Message:** Updated data: Sat Feb  1 15:02:16 UTC 2025

```diff
diff --git a/cms.json b/cms.json
index 55e15dd..9b4a8b4 100644
--- a/cms.json
+++ b/cms.json
@@ -3,7 +3,6 @@
     "@id": "https://data.cms.gov/data.json",
     "@type": "dcat:Catalog",
     "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
-    "describedBy": "https://project-open-data.cio.gov/v1.1/schema/catalog.json",
     "dataset": [
         {
             "@type": "dcat:Dataset",
@@ -17,253 +16,253 @@
                 "fn": "Shared Savings Program - CM",
                 "hasEmail": "mailto:SharedSavingsProgram@cms.hhs.gov"
             },
-            "describedBy": "https://data.cms.gov/resources/accountable-care-organization-participants-data-dictionary",
             "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/accountable-care-organization-participants-data-dictionary",
             "description": "The Accountable Care Organization Participants data presents overview information on ACO participants in the Medicare Shared Savings Program (Shared Savings Program), including their name, track status, number of years in the program, and contact information of key personnel.\n\n\u00a0\n\nDISCLAIMER: This information is current as of the last update. Changes to ACO information occur periodically. Each ACO has the most up-to-date information about their organization. Consider contacting the ACO for the latest information.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/9767cb68-8ea9-4f0b-8179-9431abc89f11/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9767cb68-8ea9-4f0b-8179-9431abc89f11",
                     "description": "latest",
-                    "title": "Accountable Care Organization Participants : 2025-01-15",
+                    "format": "API",
                     "modified": "2025-01-15",
-                    "temporal": "2025-01-01/2025-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9767cb68-8ea9-4f0b-8179-9431abc89f11",
+                    "temporal": "2025-01-01/2025-12-31",
+                    "title": "Accountable Care Organization Participants : 2025-01-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/f7fefddf-238c-49ea-afa5-07cb0e0a0d2c/PY2025_Medicare_Shared_Savings_Program_Participants.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/597651f4-ed85-40b1-8008-d0a9ee4f4b7e",
-                    "title": "Accountable Care Organization Participants : 2025-01-15",
                     "modified": "2025-01-15",
-                    "temporal": "2025-01-01/2025-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/597651f4-ed85-40b1-8008-d0a9ee4f4b7e",
+                    "temporal": "2025-01-01/2025-12-31",
+                    "title": "Accountable Care Organization Participants : 2025-01-15"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/597651f4-ed85-40b1-8008-d0a9ee4f4b7e/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/597651f4-ed85-40b1-8008-d0a9ee4f4b7e",
-                    "title": "Accountable Care Organization Participants : 2025-01-15",
+                    "format": "API",
                     "modified": "2025-01-15",
-                    "temporal": "2025-01-01/2025-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/597651f4-ed85-40b1-8008-d0a9ee4f4b7e",
+                    "temporal": "2025-01-01/2025-12-31",
+                    "title": "Accountable Care Organization Participants : 2025-01-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/afc09855-5e4b-4baf-bdc4-88a4459a52e5/PY2024_Medicare_Shared_Savings_Program_Participants.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/42b86f46-d8be-4e6d-bd03-b0b32dafe2d5",
-                    "title": "Accountable Care Organization Participants : 2024-01-24",
                     "modified": "2024-01-29",
-                    "temporal": "2024-01-01/2024-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/42b86f46-d8be-4e6d-bd03-b0b32dafe2d5",
+                    "temporal": "2024-01-01/2024-12-31",
+                    "title": "Accountable Care Organization Participants : 2024-01-24"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/42b86f46-d8be-4e6d-bd03-b0b32dafe2d5/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/42b86f46-d8be-4e6d-bd03-b0b32dafe2d5",
-                    "title": "Accountable Care Organization Participants : 2024-01-24",
+                    "format": "API",
                     "modified": "2024-01-29",
-                    "temporal": "2024-01-01/2024-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/42b86f46-d8be-4e6d-bd03-b0b32dafe2d5",
+                    "temporal": "2024-01-01/2024-12-31",
+                    "title": "Accountable Care Organization Participants : 2024-01-24"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-01/95509a9d-0344-4a5d-9cbb-3adcedbe191f/SSP_ACO_Participants_2023_01_01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fd907586-71e8-4128-ad95-801ee1f4f6f0",
-                    "title": "Accountable Care Organization Participants : 2023-01-13",
                     "modified": "2023-03-06",
-                    "temporal": "2023-01-01/2023-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fd907586-71e8-4128-ad95-801ee1f4f6f0",
+                    "temporal": "2023-01-01/2023-12-31",
+                    "title": "Accountable Care Organization Participants : 2023-01-13"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/fd907586-71e8-4128-ad95-801ee1f4f6f0/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fd907586-71e8-4128-ad95-801ee1f4f6f0",
-                    "title": "Accountable Care Organization Participants : 2023-01-13",
+                    "format": "API",
                     "modified": "2023-03-06",
-                    "temporal": "2023-01-01/2023-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fd907586-71e8-4128-ad95-801ee1f4f6f0",
+                    "temporal": "2023-01-01/2023-12-31",
+                    "title": "Accountable Care Organization Participants : 2023-01-13"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-01/048c24ac-89f8-4ca4-8fd0-a5ed32dcb9b2/SSP_ACO_Participants_2022_01_01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5b678653-aa36-455b-9144-1d073ef7991b",
-                    "title": "Accountable Care Organization Participants : 2022-01-01",
                     "modified": "2022-01-26",
-                    "temporal": "2022-01-01/2022-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5b678653-aa36-455b-9144-1d073ef7991b",
+                    "temporal": "2022-01-01/2022-12-31",
+                    "title": "Accountable Care Organization Participants : 2022-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/5b678653-aa36-455b-9144-1d073ef7991b/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5b678653-aa36-455b-9144-1d073ef7991b",
-                    "title": "Accountable Care Organization Participants : 2022-01-01",
+                    "format": "API",
                     "modified": "2022-01-26",
-                    "temporal": "2022-01-01/2022-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5b678653-aa36-455b-9144-1d073ef7991b",
+                    "temporal": "2022-01-01/2022-12-31",
+                    "title": "Accountable Care Organization Participants : 2022-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/d3640f80-8b36-4ae2-acf3-b1eced28b314/SSP_ACO_Participants_2021_01_01.csv",
                     "mediaType": "application/vnd.ms-excel",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7b409bba-ca00-426e-9493-1dc10e5340cc",
-                    "title": "Accountable Care Organization Participants : 2021-01-11",
                     "modified": "2022-01-27",
-                    "temporal": "2021-01-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7b409bba-ca00-426e-9493-1dc10e5340cc",
+                    "temporal": "2021-01-01/2021-12-31",
+                    "title": "Accountable Care Organization Participants : 2021-01-11"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/7b409bba-ca00-426e-9493-1dc10e5340cc/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7b409bba-ca00-426e-9493-1dc10e5340cc",
-                    "title": "Accountable Care Organization Participants : 2021-01-11",
+                    "format": "API",
                     "modified": "2022-01-27",
-                    "temporal": "2021-01-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7b409bba-ca00-426e-9493-1dc10e5340cc",
+                    "temporal": "2021-01-01/2021-12-31",
+                    "title": "Accountable Care Organization Participants : 2021-01-11"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/0194cc38-7cf3-4584-a077-0f1e873c635e/SSP_ACO_Participants_2020_01_01.csv",
                     "mediaType": "application/vnd.ms-excel",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3870b29c-4312-4fb1-a956-71c148ae5b50",
-                    "title": "Accountable Care Organization Participants : 2020-01-15",
                     "modified": "2022-01-27",
-                    "temporal": "2020-01-01/2020-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3870b29c-4312-4fb1-a956-71c148ae5b50",
+                    "temporal": "2020-01-01/2020-12-31",
+                    "title": "Accountable Care Organization Participants : 2020-01-15"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/3870b29c-4312-4fb1-a956-71c148ae5b50/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3870b29c-4312-4fb1-a956-71c148ae5b50",
-                    "title": "Accountable Care Organization Participants : 2020-01-15",
+                    "format": "API",
                     "modified": "2022-01-27",
-                    "temporal": "2020-01-01/2020-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3870b29c-4312-4fb1-a956-71c148ae5b50",
+                    "temporal": "2020-01-01/2020-12-31",
+                    "title": "Accountable Care Organization Participants : 2020-01-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/0e4e117e-cd35-4719-9f0b-d62f1c96b84e/SSP_ACO_Participants_2019_07_01.csv",
                     "mediaType": "application/vnd.ms-excel",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2c209bdb-ed0c-42e0-b027-8a97024b8035",
-                    "title": "Accountable Care Organization Participants : 2019-07-31oc1",
                     "modified": "2024-01-29",
-                    "temporal": "2019-01-01/2019-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2c209bdb-ed0c-42e0-b027-8a97024b8035",
+                    "temporal": "2019-01-01/2019-12-31",
+                    "title": "Accountable Care Organization Participants : 2019-07-31oc1"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/2c209bdb-ed0c-42e0-b027-8a97024b8035/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2c209bdb-ed0c-42e0-b027-8a97024b8035",
-                    "title": "Accountable Care Organization Participants : 2019-07-31oc1",
+                    "format": "API",
                     "modified": "2024-01-29",
-                    "temporal": "2019-01-01/2019-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2c209bdb-ed0c-42e0-b027-8a97024b8035",
+                    "temporal": "2019-01-01/2019-12-31",
+                    "title": "Accountable Care Organization Participants : 2019-07-31oc1"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/5537ed12-0d9c-4213-9125-180d137ec5a0/SSP_ACO_Participants_2019_01_01.csv",
                     "mediaType": "application/vnd.ms-excel",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/017e6ab7-7e19-4e98-b4fa-30578b47e578",
-                    "title": "Accountable Care Organization Participants : 2019-01-01",
                     "modified": "2022-01-27",
-                    "temporal": "2019-01-01/2019-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/017e6ab7-7e19-4e98-b4fa-30578b47e578",
+                    "temporal": "2019-01-01/2019-12-31",
+                    "title": "Accountable Care Organization Participants : 2019-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/017e6ab7-7e19-4e98-b4fa-30578b47e578/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/017e6ab7-7e19-4e98-b4fa-30578b47e578",
-                    "title": "Accountable Care Organization Participants : 2019-01-01",
+                    "format": "API",
                     "modified": "2022-01-27",
-                    "temporal": "2019-01-01/2019-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/017e6ab7-7e19-4e98-b4fa-30578b47e578",
+                    "temporal": "2019-01-01/2019-12-31",
+                    "title": "Accountable Care Organization Participants : 2019-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/cd5b68e6-8e09-4866-8381-d34bc8db4220/SSP_ACO_Participants_2018_01_01.csv",
                     "mediaType": "application/vnd.ms-excel",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6ed410fb-5e7d-477f-90ed-a499e951c5d1",
-                    "title": "Accountable Care Organization Participants : 2018-01-01",
                     "modified": "2022-01-27",
-                    "temporal": "2018-01-01/2018-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6ed410fb-5e7d-477f-90ed-a499e951c5d1",
+                    "temporal": "2018-01-01/2018-12-31",
+                    "title": "Accountable Care Organization Participants : 2018-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/6ed410fb-5e7d-477f-90ed-a499e951c5d1/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6ed410fb-5e7d-477f-90ed-a499e951c5d1",
-                    "title": "Accountable Care Organization Participants : 2018-01-01",
+                    "format": "API",
                     "modified": "2022-01-27",
-                    "temporal": "2018-01-01/2018-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6ed410fb-5e7d-477f-90ed-a499e951c5d1",
+                    "temporal": "2018-01-01/2018-12-31",
+                    "title": "Accountable Care Organization Participants : 2018-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/41c6c604-30f3-439e-8460-3087cbab0344/SSP_ACO_Participants_2017_01_01.csv",
                     "mediaType": "application/vnd.ms-excel",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bbde17e0-01b1-46d2-b8bf-9949da11a448",
-                    "title": "Accountable Care Organization Participants : 2017-01-01",
                     "modified": "2022-01-27",
-                    "temporal": "2017-01-01/2017-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bbde17e0-01b1-46d2-b8bf-9949da11a448",
+                    "temporal": "2017-01-01/2017-12-31",
+                    "title": "Accountable Care Organization Participants : 2017-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/bbde17e0-01b1-46d2-b8bf-9949da11a448/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bbde17e0-01b1-46d2-b8bf-9949da11a448",
-                    "title": "Accountable Care Organization Participants : 2017-01-01",
+                    "format": "API",
                     "modified": "2022-01-27",
-                    "temporal": "2017-01-01/2017-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bbde17e0-01b1-46d2-b8bf-9949da11a448",
+                    "temporal": "2017-01-01/2017-12-31",
+                    "title": "Accountable Care Organization Participants : 2017-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/2087df69-afb4-43ed-b50a-cd13c7a46d9a/SSP_ACO_Participants_2016_01_01.csv",
                     "mediaType": "application/vnd.ms-excel",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d2b525f5-77b6-416e-858c-36c9c381eb33",
-                    "title": "Accountable Care Organization Participants : 2016-12-31",
                     "modified": "2022-01-27",
-                    "temporal": "2016-01-01/2016-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d2b525f5-77b6-416e-858c-36c9c381eb33",
+                    "temporal": "2016-01-01/2016-12-31",
+                    "title": "Accountable Care Organization Participants : 2016-12-31"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/d2b525f5-77b6-416e-858c-36c9c381eb33/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d2b525f5-77b6-416e-858c-36c9c381eb33",
-                    "title": "Accountable Care Organization Participants : 2016-12-31",
+                    "format": "API",
                     "modified": "2022-01-27",
-                    "temporal": "2016-01-01/2016-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d2b525f5-77b6-416e-858c-36c9c381eb33",
+                    "temporal": "2016-01-01/2016-12-31",
+                    "title": "Accountable Care Organization Participants : 2016-12-31"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/9f516f5c-6c08-4bab-947f-8d3f2c950db4/SSP_ACO_Participants_2015_01_01.csv",
                     "mediaType": "application/vnd.ms-excel",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4a743510-fbc3-4363-aab5-9d6c0fe3dea7",
-                    "title": "Accountable Care Organization Participants : 2015-12-31",
                     "modified": "2022-01-27",
-                    "temporal": "2015-01-01/2015-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4a743510-fbc3-4363-aab5-9d6c0fe3dea7",
+                    "temporal": "2015-01-01/2015-12-31",
+                    "title": "Accountable Care Organization Participants : 2015-12-31"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/4a743510-fbc3-4363-aab5-9d6c0fe3dea7/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4a743510-fbc3-4363-aab5-9d6c0fe3dea7",
-                    "title": "Accountable Care Organization Participants : 2015-12-31",
+                    "format": "API",
                     "modified": "2022-01-27",
-                    "temporal": "2015-01-01/2015-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4a743510-fbc3-4363-aab5-9d6c0fe3dea7",
+                    "temporal": "2015-01-01/2015-12-31",
+                    "title": "Accountable Care Organization Participants : 2015-12-31"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/d6084efd-ae4b-4633-8983-25485978717c/SSP_ACO_Participants_2014_01_01.csv",
                     "mediaType": "application/vnd.ms-excel",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5ebc6246-1861-4d9f-92b4-33c69b315d64",
-                    "title": "Accountable Care Organization Participants : 2014-12-31",
                     "modified": "2022-01-27",
-                    "temporal": "2014-01-01/2014-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5ebc6246-1861-4d9f-92b4-33c69b315d64",
+                    "temporal": "2014-01-01/2014-12-31",
+                    "title": "Accountable Care Organization Participants : 2014-12-31"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/5ebc6246-1861-4d9f-92b4-33c69b315d64/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5ebc6246-1861-4d9f-92b4-33c69b315d64",
-                    "title": "Accountable Care Organization Participants : 2014-12-31",
+                    "format": "API",
                     "modified": "2022-01-27",
-                    "temporal": "2014-01-01/2014-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5ebc6246-1861-4d9f-92b4-33c69b315d64",
+                    "temporal": "2014-01-01/2014-12-31",
+                    "title": "Accountable Care Organization Participants : 2014-12-31"
                 }
             ],
             "identifier": "https://data.cms.gov/data-api/v1/dataset/9767cb68-8ea9-4f0b-8179-9431abc89f11/data-viewer",
@@ -308,199 +307,199 @@
                 "fn": "Shared Savings Program - CM",
                 "hasEmail": "mailto:SharedSavingsProgram@cms.hhs.gov"
             },
-            "describedBy": "https://data.cms.gov/resources/aco-snf-affiliates-data-dictionary",
             "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/aco-snf-affiliates-data-dictionary",
             "description": "The Accountable Care Organization Skilled Nursing Facility Affiliates data presents overview information on ACO SNF affiliates in the Medicare Shared Savings Program (Shared Savings Program), including their name, track status, number of years in the program, and contact information of key personnel.\n\n\u00a0\n\nDISCLAIMER: This information is current as of the last update. Changes to ACO information occur periodically. Each ACO has the most up-to-date information about their organization. Consider contacting the ACO for the latest information.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/5b227bd9-82d4-4145-86fd-809e02ca7f18/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5b227bd9-82d4-4145-86fd-809e02ca7f18",
                     "description": "latest",
-                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2025-01-15",
+                    "format": "API",
                     "modified": "2025-01-15",
-                    "temporal": "2025-01-01/2025-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5b227bd9-82d4-4145-86fd-809e02ca7f18",
+                    "temporal": "2025-01-01/2025-12-31",
+                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2025-01-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/351ec09e-6f7f-4ae7-860f-50ba5e96c3fd/PY2025_Medicare_Shared_Savings_Program_SNF_Affiliates.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a408717e-6214-4e3c-bbe7-76833697172a",
-                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2025-01-15",
                     "modified": "2025-01-15",
-                    "temporal": "2025-01-01/2025-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a408717e-6214-4e3c-bbe7-76833697172a",
+                    "temporal": "2025-01-01/2025-12-31",
+                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2025-01-15"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/a408717e-6214-4e3c-bbe7-76833697172a/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a408717e-6214-4e3c-bbe7-76833697172a",
-                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2025-01-15",
+                    "format": "API",
                     "modified": "2025-01-15",
-                    "temporal": "2025-01-01/2025-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a408717e-6214-4e3c-bbe7-76833697172a",
+                    "temporal": "2025-01-01/2025-12-31",
+                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2025-01-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/06261ed8-4ad8-461c-ae4b-c0b48a289fb0/PY2024_Medicare_Shared_Savings_Program_SNF_Affiliates.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c8b07a5e-4b6a-4578-8e72-ecab0d712e4a",
-                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2024-01-24",
                     "modified": "2024-04-23",
-                    "temporal": "2024-01-01/2024-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c8b07a5e-4b6a-4578-8e72-ecab0d712e4a",
+                    "temporal": "2024-01-01/2024-12-31",
+                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2024-01-24"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/c8b07a5e-4b6a-4578-8e72-ecab0d712e4a/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c8b07a5e-4b6a-4578-8e72-ecab0d712e4a",
-                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2024-01-24",
+                    "format": "API",
                     "modified": "2024-04-23",
-                    "temporal": "2024-01-01/2024-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c8b07a5e-4b6a-4578-8e72-ecab0d712e4a",
+                    "temporal": "2024-01-01/2024-12-31",
+                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2024-01-24"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-01/7b0c52ea-924e-4c19-b887-619259918608/SSP_ACO_SNF_Affiliates_2023_01_01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3c1d3c97-ed6a-4caa-a8f9-9fe8994ead2c",
-                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2023-01-13",
                     "modified": "2023-03-06",
-                    "temporal": "2023-01-01/2023-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3c1d3c97-ed6a-4caa-a8f9-9fe8994ead2c",
+                    "temporal": "2023-01-01/2023-12-31",
+                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2023-01-13"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/3c1d3c97-ed6a-4caa-a8f9-9fe8994ead2c/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3c1d3c97-ed6a-4caa-a8f9-9fe8994ead2c",
-                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2023-01-13",
+                    "format": "API",
                     "modified": "2023-03-06",
-                    "temporal": "2023-01-01/2023-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3c1d3c97-ed6a-4caa-a8f9-9fe8994ead2c",
+                    "temporal": "2023-01-01/2023-12-31",
+                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2023-01-13"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-01/dd0a3f64-a470-4816-96e2-f00e2100e77f/SSP_ACO_SNF_Affiliates_2022_01_01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6e053921-7f8d-44df-aa61-2654e0f35ef3",
-                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2022-01-01",
                     "modified": "2022-01-26",
-                    "temporal": "2022-01-01/2022-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6e053921-7f8d-44df-aa61-2654e0f35ef3",
+                    "temporal": "2022-01-01/2022-12-31",
+                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2022-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/6e053921-7f8d-44df-aa61-2654e0f35ef3/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6e053921-7f8d-44df-aa61-2654e0f35ef3",
-                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2022-01-01",
+                    "format": "API",
                     "modified": "2022-01-26",
-                    "temporal": "2022-01-01/2022-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6e053921-7f8d-44df-aa61-2654e0f35ef3",
+                    "temporal": "2022-01-01/2022-12-31",
+                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2022-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/ac521b18-ed48-49c0-af05-a702ae8a2aa1/SSP_ACO_SNF_Affiliates_2021_01_01.csv",
                     "mediaType": "application/vnd.ms-excel",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1023231b-b26c-4342-a7c4-c6dd39d99a36",
-                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2021-01-11",
                     "modified": "2022-01-27",
-                    "temporal": "2021-01-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1023231b-b26c-4342-a7c4-c6dd39d99a36",
+                    "temporal": "2021-01-01/2021-12-31",
+                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2021-01-11"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/1023231b-b26c-4342-a7c4-c6dd39d99a36/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1023231b-b26c-4342-a7c4-c6dd39d99a36",
-                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2021-01-11",
+                    "format": "API",
                     "modified": "2022-01-27",
-                    "temporal": "2021-01-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1023231b-b26c-4342-a7c4-c6dd39d99a36",
+                    "temporal": "2021-01-01/2021-12-31",
+                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2021-01-11"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/52e8aaa3-4d9d-4f0a-9c97-ef2f7276f3aa/SSP_ACO_SNF_Affiliates_2020_01_01.csv",
                     "mediaType": "application/vnd.ms-excel",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/31012035-867f-445a-8ecc-eb01f630d3f7",
-                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2020-12-31",
                     "modified": "2022-01-27",
-                    "temporal": "2020-01-01/2020-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/31012035-867f-445a-8ecc-eb01f630d3f7",
+                    "temporal": "2020-01-01/2020-12-31",
+                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2020-12-31"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/31012035-867f-445a-8ecc-eb01f630d3f7/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/31012035-867f-445a-8ecc-eb01f630d3f7",
-                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2020-12-31",
+                    "format": "API",
                     "modified": "2022-01-27",
-                    "temporal": "2020-01-01/2020-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/31012035-867f-445a-8ecc-eb01f630d3f7",
+                    "temporal": "2020-01-01/2020-12-31",
+                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2020-12-31"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/ff99b802-b565-4b9d-833a-c0d7bb0d7e30/SSP_ACO_SNF_Affiliates_2019_07_01.csv",
                     "mediaType": "application/vnd.ms-excel",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3a998bd2-7e55-4c56-a240-a9b7de34b5a9",
-                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2019-07-31oc1",
                     "modified": "2024-01-29",
-                    "temporal": "2019-01-01/2019-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3a998bd2-7e55-4c56-a240-a9b7de34b5a9",
+                    "temporal": "2019-01-01/2019-12-31",
+                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2019-07-31oc1"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/3a998bd2-7e55-4c56-a240-a9b7de34b5a9/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3a998bd2-7e55-4c56-a240-a9b7de34b5a9",
-                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2019-07-31oc1",
+                    "format": "API",
                     "modified": "2024-01-29",
-                    "temporal": "2019-01-01/2019-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3a998bd2-7e55-4c56-a240-a9b7de34b5a9",
+                    "temporal": "2019-01-01/2019-12-31",
+                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2019-07-31oc1"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/a37d4125-95be-43e7-9db6-6510642eab83/SSP_ACO_SNF_Affiliates_2019_01_01.csv",
                     "mediaType": "application/vnd.ms-excel",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a6be7a5d-c345-444c-9449-708ee0f73617",
-                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2019-01-01",
                     "modified": "2022-01-27",
-                    "temporal": "2019-01-01/2019-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a6be7a5d-c345-444c-9449-708ee0f73617",
+                    "temporal": "2019-01-01/2019-12-31",
+                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2019-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/a6be7a5d-c345-444c-9449-708ee0f73617/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a6be7a5d-c345-444c-9449-708ee0f73617",
-                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2019-01-01",
+                    "format": "API",
                     "modified": "2022-01-27",
-                    "temporal": "2019-01-01/2019-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a6be7a5d-c345-444c-9449-708ee0f73617",
+                    "temporal": "2019-01-01/2019-12-31",
+                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2019-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/d375f1f2-aea9-47d3-b6bf-db7d3b23864e/SSP_ACO_SNF_Affiliates_2018_01_01.csv",
                     "mediaType": "application/vnd.ms-excel",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2fa21672-de7d-4157-a7ed-b2787f8a6fe1",
-                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2018-01-15",
                     "modified": "2022-01-27",
-                    "temporal": "2018-01-01/2018-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2fa21672-de7d-4157-a7ed-b2787f8a6fe1",
+                    "temporal": "2018-01-01/2018-12-31",
+                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2018-01-15"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/2fa21672-de7d-4157-a7ed-b2787f8a6fe1/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2fa21672-de7d-4157-a7ed-b2787f8a6fe1",
-                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2018-01-15",
+                    "format": "API",
                     "modified": "2022-01-27",
-                    "temporal": "2018-01-01/2018-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2fa21672-de7d-4157-a7ed-b2787f8a6fe1",
+                    "temporal": "2018-01-01/2018-12-31",
+                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2018-01-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/ca99b1f6-063a-40c4-9347-d18382efc76c/SSP_ACO_SNF_Affiliates_2017_01_01.csv",
                     "mediaType": "application/vnd.ms-excel",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/62d0d206-01f7-4ed3-9b45-8d692d0bd431",
-                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2017-01-15",
                     "modified": "2022-01-27",
-                    "temporal": "2017-01-01/2017-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/62d0d206-01f7-4ed3-9b45-8d692d0bd431",
+                    "temporal": "2017-01-01/2017-12-31",
+                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2017-01-15"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/62d0d206-01f7-4ed3-9b45-8d692d0bd431/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/62d0d206-01f7-4ed3-9b45-8d692d0bd431",
-                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2017-01-15",
+                    "format": "API",
                     "modified": "2022-01-27",
-                    "temporal": "2017-01-01/2017-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/62d0d206-01f7-4ed3-9b45-8d692d0bd431",
+                    "temporal": "2017-01-01/2017-12-31",
+                    "title": "Accountable Care Organization Skilled Nursing Facility Affiliates : 2017-01-15"
                 }
             ],
             "identifier": "https://data.cms.gov/data-api/v1/dataset/5b227bd9-82d4-4145-86fd-809e02ca7f18/data-viewer",
@@ -545,37 +544,37 @@
                 "fn": "ACO REACH - CMMI",
                 "hasEmail": "mailto:ACOREACH@cms.hhs.gov"
             },
-            "describedBy": "https://data.cms.gov/resources/aco-reach-aligned-beneficiaries-data-dictionary",
             "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/aco-reach-aligned-beneficiaries-data-dictionary",
             "description": "The Accountable Care Organization Realizing Equity, Access and Community Health (ACO REACH) Model Aligned Beneficiary Public Use File (PUF) data details Medicare Beneficiaries aligned to the ACO REACH Model, formerly Global and Professional Direct Contracting (GPDC) Model, including counties, eligibility months and total aligned beneficiaries. This data is redacted and does not include identifiable information.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/1cd9eded-d2c9-4215-a064-aac6dae3b714/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1cd9eded-d2c9-4215-a064-aac6dae3b714",
                     "description": "latest",
-                    "title": "ACO Realizing Equity, Access and Community Health Aligned Beneficiaries : 2021-12-31",
+                    "format": "API",
                     "modified": "2024-01-12",
-                    "temporal": "2021-01-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1cd9eded-d2c9-4215-a064-aac6dae3b714",
+                    "temporal": "2021-01-01/2021-12-31",
+                    "title": "ACO Realizing Equity, Access and Community Health Aligned Beneficiaries : 2021-12-31"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/1716ad9c-f5c8-43fd-936e-0c53e1f0ee64/ALGN_BENE_PUF_REDACT_UPDATE.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0775e970-9bc3-4e24-9693-4706ba5ff015",
-                    "title": "ACO Realizing Equity, Access and Community Health Aligned Beneficiaries : 2021-12-31",
                     "modified": "2024-01-12",
-                    "temporal": "2021-01-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0775e970-9bc3-4e24-9693-4706ba5ff015",
+                    "temporal": "2021-01-01/2021-12-31",
+                    "title": "ACO Realizing Equity, Access and Community Health Aligned Beneficiaries : 2021-12-31"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/0775e970-9bc3-4e24-9693-4706ba5ff015/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0775e970-9bc3-4e24-9693-4706ba5ff015",
-                    "title": "ACO Realizing Equity, Access and Community Health Aligned Beneficiaries : 2021-12-31",
+                    "format": "API",
                     "modified": "2024-01-12",
-                    "temporal": "2021-01-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0775e970-9bc3-4e24-9693-4706ba5ff015",
+                    "temporal": "2021-01-01/2021-12-31",
+                    "title": "ACO Realizing Equity, Access and Community Health Aligned Beneficiaries : 2021-12-31"
                 }
             ],
             "identifier": "https://data.cms.gov/data-api/v1/dataset/1cd9eded-d2c9-4215-a064-aac6dae3b714/data-viewer",
@@ -621,37 +620,37 @@
                 "fn": "ACO REACH - CMMI",
                 "hasEmail": "mailto:ACOREACH@cms.hhs.gov"
             },
-            "describedBy": "https://data.cms.gov/resources/aco-reach-eligible-beneficiary-data-dictionary",
             "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/aco-reach-eligible-beneficiary-data-dictionary",
             "description": "Accountable Care Organization Realizing Equity, Access and Community Health (ACO REACH) Model Eligible Beneficiary Public Use File (PUF) data details Medicare Beneficiaries who were used as the reference population for comparison to aligned to the ACO REACH Model, formerly Global and Professional Direct Contracting (GPDC) Model, including average risk scores and eligibility months. This data is redacted and does not include identifiable information.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/54551982-39a8-4744-90f6-c38bb4dd5108/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/54551982-39a8-4744-90f6-c38bb4dd5108",
                     "description": "latest",
-                    "title": "ACO Realizing Equity, Access and Community Health Eligible Beneficiaries : 2021-12-01",
+                    "format": "API",
                     "modified": "2024-01-12",
-                    "temporal": "2021-01-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/54551982-39a8-4744-90f6-c38bb4dd5108",
+                    "temporal": "2021-01-01/2021-12-31",
+                    "title": "ACO Realizing Equity, Access and Community Health Eligible Beneficiaries : 2021-12-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/ELIG_BENE_PUF_REDACT.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5941f9b8-9d72-44a1-a102-f8386c155290",
-                    "title": "ACO Realizing Equity, Access and Community Health Eligible Beneficiaries : 2021-12-01",
                     "modified": "2024-01-12",
-                    "temporal": "2021-01-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5941f9b8-9d72-44a1-a102-f8386c155290",
+                    "temporal": "2021-01-01/2021-12-31",
+                    "title": "ACO Realizing Equity, Access and Community Health Eligible Beneficiaries : 2021-12-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/5941f9b8-9d72-44a1-a102-f8386c155290/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5941f9b8-9d72-44a1-a102-f8386c155290",
-                    "title": "ACO Realizing Equity, Access and Community Health Eligible Beneficiaries : 2021-12-01",
+                    "format": "API",
                     "modified": "2024-01-12",
-                    "temporal": "2021-01-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5941f9b8-9d72-44a1-a102-f8386c155290",
+                    "temporal": "2021-01-01/2021-12-31",
+                    "title": "ACO Realizing Equity, Access and Community Health Eligible Beneficiaries : 2021-12-01"
                 }
             ],
             "identifier": "https://data.cms.gov/data-api/v1/dataset/54551982-39a8-4744-90f6-c38bb4dd5108/data-viewer",
@@ -697,37 +696,37 @@
                 "fn": "ACO REACH - CMMI",
                 "hasEmail": "mailto:ACOREACH@cms.hhs.gov"
             },
-            "describedBy": "https://data.cms.gov/resources/aco-reach-financial-and-quality-results-data-dictionary",
             "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/aco-reach-financial-and-quality-results-data-dictionary",
             "description": "The Accountable Care Organization Realizing Equity, Access and Community Health (ACO REACH) Model Financial and Quality Results Public Use File (PUF) details performance for the ACO REACH Model, formerly Global and Professional Direct Contracting (GPDC) Model, prior to settlement. This data includes information such as the ACOs risk arrangement, stop loss, capitation, savings rate, and quality results.\u00a0\n\n\u00a0\n\nThe expanded quality performance results are expected to be released in the fall.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/6c3532b3-8325-48fd-a939-12b41d2b126a/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6c3532b3-8325-48fd-a939-12b41d2b126a",
                     "description": "latest",
-                    "title": "ACO Realizing Equity, Access and Community Health Financial and Quality Results : 2021-12-31",
+                    "format": "API",
                     "modified": "2024-01-12",
-                    "temporal": "2021-01-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6c3532b3-8325-48fd-a939-12b41d2b126a",
+                    "temporal": "2021-01-01/2021-12-31",
+                    "title": "ACO Realizing Equity, Access and Community Health Financial and Quality Results : 2021-12-31"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/bb23b17f-a0f2-4da3-9a07-d499d7372d61/EXPND_FNCL_QLTY_PUF_REDACT_UPDATE.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/51206383-1bf2-4230-af28-6bd66a9f311c",
-                    "title": "ACO Realizing Equity, Access and Community Health Financial and Quality Results : 2021-12-31",
                     "modified": "2024-01-12",
-                    "temporal": "2021-01-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/51206383-1bf2-4230-af28-6bd66a9f311c",
+                    "temporal": "2021-01-01/2021-12-31",
+                    "title": "ACO Realizing Equity, Access and Community Health Financial and Quality Results : 2021-12-31"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/51206383-1bf2-4230-af28-6bd66a9f311c/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/51206383-1bf2-4230-af28-6bd66a9f311c",
-                    "title": "ACO Realizing Equity, Access and Community Health Financial and Quality Results : 2021-12-31",
+                    "format": "API",
                     "modified": "2024-01-12",
-                    "temporal": "2021-01-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/51206383-1bf2-4230-af28-6bd66a9f311c",
+                    "temporal": "2021-01-01/2021-12-31",
+                    "title": "ACO Realizing Equity, Access and Community Health Financial and Quality Results : 2021-12-31"
                 }
             ],
             "identifier": "https://data.cms.gov/data-api/v1/dataset/6c3532b3-8325-48fd-a939-12b41d2b126a/data-viewer",
@@ -773,37 +772,37 @@
                 "fn": "ACO REACH - CMMI",
                 "hasEmail": "mailto:ACOREACH@cms.hhs.gov"
             },
-            "describedBy": "https://data.cms.gov/resources/aco-reach-provider-data-dictionary",
             "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/aco-reach-provider-data-dictionary",
             "description": "The Accountable Care Organization Realizing Equity, Access and Community Health (ACO REACH) Model Providers Public Use File (PUF) data details Participant Providers and Preferred Providers in the ACO REACH Model, formerly Global and Professional Direct Contracting (GPDC) Model. This dataset includes information on each providers capitation arrangement, Advanced Payment Option and elected waivers.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/e0eba16f-ce0d-4037-96ce-2af70c718c98/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e0eba16f-ce0d-4037-96ce-2af70c718c98",
                     "description": "latest",
-                    "title": "ACO Realizing Equity, Access and Community Health Providers : 2021-12-31",
+                    "format": "API",
                     "modified": "2024-01-12",
-                    "temporal": "2021-01-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e0eba16f-ce0d-4037-96ce-2af70c718c98",
+                    "temporal": "2021-01-01/2021-12-31",
+                    "title": "ACO Realizing Equity, Access and Community Health Providers : 2021-12-31"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/PROVIDER_PUF.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e235bb4b-84ea-456a-a64e-b7c1b8a98ea7",
-                    "title": "ACO Realizing Equity, Access and Community Health Providers : 2021-12-31",
                     "modified": "2024-01-12",
-                    "temporal": "2021-01-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e235bb4b-84ea-456a-a64e-b7c1b8a98ea7",
+                    "temporal": "2021-01-01/2021-12-31",
+                    "title": "ACO Realizing Equity, Access and Community Health Providers : 2021-12-31"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/e235bb4b-84ea-456a-a64e-b7c1b8a98ea7/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e235bb4b-84ea-456a-a64e-b7c1b8a98ea7",
-                    "title": "ACO Realizing Equity, Access and Community Health Providers : 2021-12-31",
+                    "format": "API",
                     "modified": "2024-01-12",
-                    "temporal": "2021-01-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e235bb4b-84ea-456a-a64e-b7c1b8a98ea7",
+                    "temporal": "2021-01-01/2021-12-31",
+                    "title": "ACO Realizing Equity, Access and Community Health Providers : 2021-12-31"
                 }
             ],
             "identifier": "https://data.cms.gov/data-api/v1/dataset/e0eba16f-ce0d-4037-96ce-2af70c718c98/data-viewer",
@@ -849,37 +848,37 @@
                 "fn": "Shared Savings Program - CM",
                 "hasEmail": "mailto:SharedSavingsProgram@cms.hhs.gov"
             },
-            "describedBy": "https://data.cms.gov/resources/advance-investment-payment-spend-plan-data-dictionary",
             "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/advance-investment-payment-spend-plan-data-dictionary",
             "description": "The Advance Investment Payment Spend Plan data provides payment use, spending category, projected and actual spending of advanced investments payments by Accountable Care Organizations (ACOs).",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/a3d35ba1-3ff4-48dd-91b4-8e1f9e7a19b7/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a3d35ba1-3ff4-48dd-91b4-8e1f9e7a19b7",
                     "description": "latest",
-                    "title": "Advance Investment Payment Spend Plan : 2024-01-02",
+                    "format": "API",
                     "modified": "2024-01-29",
-                    "temporal": "2024-01-01/2024-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a3d35ba1-3ff4-48dd-91b4-8e1f9e7a19b7",
+                    "temporal": "2024-01-01/2024-12-31",
+                    "title": "Advance Investment Payment Spend Plan : 2024-01-02"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/AIP_PUF_12_13_2023.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/329394bc-b58c-4458-a028-33a00ae47a84",
-                    "title": "Advance Investment Payment Spend Plan : 2024-01-02",
                     "modified": "2024-01-29",
-                    "temporal": "2024-01-01/2024-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/329394bc-b58c-4458-a028-33a00ae47a84",
+                    "temporal": "2024-01-01/2024-12-31",
+                    "title": "Advance Investment Payment Spend Plan : 2024-01-02"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/329394bc-b58c-4458-a028-33a00ae47a84/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/329394bc-b58c-4458-a028-33a00ae47a84",
-                    "title": "Advance Investment Payment Spend Plan : 2024-01-02",
+                    "format": "API",
                     "modified": "2024-01-29",
-                    "temporal": "2024-01-01/2024-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/329394bc-b58c-4458-a028-33a00ae47a84",
+                    "temporal": "2024-01-01/2024-12-31",
+                    "title": "Advance Investment Payment Spend Plan : 2024-01-02"
                 }
             ],
             "identifier": "https://data.cms.gov/data-api/v1/dataset/a3d35ba1-3ff4-48dd-91b4-8e1f9e7a19b7/data-viewer",
@@ -926,55 +925,55 @@
                 "fn": "Deficit Reduction Act Hospital Acquired Conditions - CCSQ",
                 "hasEmail": "mailto:drahac@mathematica-mpr.com"
             },
-            "describedBy": "https://data.cms.gov/resources/agency-for-healthcare-research-and-quality-ahrq-patient-safety-indicator-11-psi-11-measure-rates-data-dictionary",
             "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/agency-for-healthcare-research-and-quality-ahrq-patient-safety-indicator-11-psi-11-measure-rates-data-dictionary",
             "description": "The Agency for Healthcare Research and Quality (AHRQ) Patient Safety Indicator 11 (PSI-11) Measure Rates dataset provides information on provider-level measure\u00a0rates regarding one preventable complication (postoperative respiratory failure) for Medicare fee-for-service discharges. The PSI-11 measure data is solely reported for providers\u2019 information and quality improvement purposes and are not a part of the Deficit Reduction Act (DRA) Hospital-Acquired Condition (HAC) Payment Provision or HAC Reduction Program.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/7cf9662e-7c5c-4fe0-a8c6-828edf81a23c/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7cf9662e-7c5c-4fe0-a8c6-828edf81a23c",
                     "description": "latest",
-                    "title": "Agency for Healthcare Research and Quality (AHRQ) Patient Safety Indicator 11 (PSI-11) Measure Rates : 2016-07-29",
+                    "format": "API",
                     "modified": "2020-12-08",
-                    "temporal": "2016-01-01/2016-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7cf9662e-7c5c-4fe0-a8c6-828edf81a23c",
+                    "temporal": "2016-01-01/2016-12-31",
+                    "title": "Agency for Healthcare Research and Quality (AHRQ) Patient Safety Indicator 11 (PSI-11) Measure Rates : 2016-07-29"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2020-09/Provider-Level_Measure_Rates_for_AHRQ_Patient_Safety_Indicator_11__PSI-11___-_2016.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bcf769c0-5bfc-433e-852e-730a6f8e899c",
-                    "title": "Agency for Healthcare Research and Quality (AHRQ) Patient Safety Indicator 11 (PSI-11) Measure Rates : 2016-07-29",
                     "modified": "2020-12-08",
-                    "temporal": "2016-01-01/2016-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bcf769c0-5bfc-433e-852e-730a6f8e899c",
+                    "temporal": "2016-01-01/2016-12-31",
+                    "title": "Agency for Healthcare Research and Quality (AHRQ) Patient Safety Indicator 11 (PSI-11) Measure Rates : 2016-07-29"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/bcf769c0-5bfc-433e-852e-730a6f8e899c/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bcf769c0-5bfc-433e-852e-730a6f8e899c",
-                    "title": "Agency for Healthcare Research and Quality (AHRQ) Patient Safety Indicator 11 (PSI-11) Measure Rates : 2016-07-29",
+                    "format": "API",
                     "modified": "2020-12-08",
-                    "temporal": "2016-01-01/2016-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bcf769c0-5bfc-433e-852e-730a6f8e899c",
+                    "temporal": "2016-01-01/2016-12-31",
+                    "title": "Agency for Healthcare Research and Quality (AHRQ) Patient Safety Indicator 11 (PSI-11) Measure Rates : 2016-07-29"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2020-09/Provider-Level_Measure_Rates_for_AHRQ_Patient_Safety_Indicator_11__PSI-11_.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/374c448f-4507-4949-bc5a-e59fdc6f0698",
-                    "title": "Agency for Healthcare Research and Quality (AHRQ) Patient Safety Indicator 11 (PSI-11) Measure Rates : 2015-08-19",
                     "modified": "2020-10-08",
-                    "temporal": "2015-01-01/2015-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/374c448f-4507-4949-bc5a-e59fdc6f0698",
+                    "temporal": "2015-01-01/2015-12-31",
+                    "title": "Agency for Healthcare Research and Quality (AHRQ) Patient Safety Indicator 11 (PSI-11) Measure Rates : 2015-08-19"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/374c448f-4507-4949-bc5a-e59fdc6f0698/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/374c448f-4507-4949-bc5a-e59fdc6f0698",
-                    "title": "Agency for Healthcare Research and Quality (AHRQ) Patient Safety Indicator 11 (PSI-11) Measure Rates : 2015-08-19",
+                    "format": "API",
                     "modified": "2020-10-08",
-                    "temporal": "2015-01-01/2015-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/374c448f-4507-4949-bc5a-e59fdc6f0698",
+                    "temporal": "2015-01-01/2015-12-31",
+                    "title": "Agency for Healthcare Research and Quality (AHRQ) Patient Safety Indicator 11 (PSI-11) Measure Rates : 2015-08-19"
                 }
             ],
             "identifier": "https://data.cms.gov/data-api/v1/dataset/7cf9662e-7c5c-4fe0-a8c6-828edf81a23c/data-viewer",
@@ -1020,63 +1019,63 @@
                 "fn": "CMS Program Statistics - OEDA",
                 "hasEmail": "mailto:IPAG_Data_Products@cms.hhs.gov"
             },
-            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
             "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
             "description": "The CMS Program Statistics \u2013 Medicare Advantage, Outpatient Facility tables provide utilization data for outpatient facilities, by Medicare Advantage beneficiaries.\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\nBelow is the list of tables:\n\n\n\tMDCR OUTPATIENT MA 1. \u00a0Medicare Outpatient Facilities: Utilization for Medicare Advantage Beneficiaries, by Type of Entitlement, Yearly Trend\n\tMDCR OUTPATIENT MA 2. \u00a0Medicare Outpatient Facilities: Utilization for Medicare Advantage Beneficiaries, by Demographic Characteristics and Medicare-Medicaid Enrollment Status\n\tMDCR OUTPATIENT MA 3. \u00a0Medicare Outpatient Facilities: Utilization for Medicare Advantage Beneficiaries, by Area of Residence",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/CPS%20MDCR%20OUTPT%20MA%202021%20FINAL.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ccfeb268-4e80-4886-8355-70e301738377",
-                    "title": "CMS Program Statistics - Medicare Advantage - Outpatient Facility : 2021-05-06",
                     "modified": "2024-05-16",
-                    "temporal": "2021-01-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ccfeb268-4e80-4886-8355-70e301738377",
+                    "temporal": "2021-01-01/2021-12-31",
+                    "title": "CMS Program Statistics - Medicare Advantage - Outpatient Facility : 2021-05-06"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/CPS%20MDCR%20OUTPT%20MA%202020%20FINAL.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/aa6de9d4-a517-4a30-8b66-d46db9a117b8",
-                    "title": "CMS Program Statistics - Medicare Advantage - Outpatient Facility : 2020-01-15",
                     "modified": "2024-05-16",
-                    "temporal": "2020-01-01/2020-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/aa6de9d4-a517-4a30-8b66-d46db9a117b8",
+                    "temporal": "2020-01-01/2020-12-31",
+                    "title": "CMS Program Statistics - Medicare Advantage - Outpatient Facility : 2020-01-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/CPS%20MDCR%20OUTPT%20MA%202019%20FINAL.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b20494d9-c4d1-442d-b215-93a142c25863",
-                    "title": "CMS Program Statistics - Medicare Advantage - Outpatient Facility : 2019-01-15",
                     "modified": "2024-05-16",
-                    "temporal": "2019-01-01/2019-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b20494d9-c4d1-442d-b215-93a142c25863",
+                    "temporal": "2019-01-01/2019-12-31",
+                    "title": "CMS Program Statistics - Medicare Advantage - Outpatient Facility : 2019-01-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/CPS%20MDCR%20OUTPT%20MA%202018%20FINAL.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/237486e5-3130-48f0-99dd-4cf2c0257ef5",
-                    "title": "CMS Program Statistics - Medicare Advantage - Outpatient Facility : 2018-01-15",
                     "modified": "2024-05-16",
-                    "temporal": "2018-01-01/2018-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/237486e5-3130-48f0-99dd-4cf2c0257ef5",
+                    "temporal": "2018-01-01/2018-12-31",
+                    "title": "CMS Program Statistics - Medicare Advantage - Outpatient Facility : 2018-01-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/CPS%20MDCR%20OUTPT%20MA%202017%20FINAL.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/348fae8b-3364-453f-8a1d-c1875d5bf5b3",
-                    "title": "CMS Program Statistics - Medicare Advantage - Outpatient Facility : 2017-01-15",
                     "modified": "2024-05-16",
-                    "temporal": "2017-01-01/2017-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/348fae8b-3364-453f-8a1d-c1875d5bf5b3",
+                    "temporal": "2017-01-01/2017-12-31",
+                    "title": "CMS Program Statistics - Medicare Advantage - Outpatient Facility : 2017-01-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/CPS%20MDCR%20OUTPT%20MA%202016%20FINAL.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c7b229a9-1c69-4b3e-a567-8a2a0179768e",
-                    "title": "CMS Program Statistics - Medicare Advantage - Outpatient Facility : 2016-01-15",
                     "modified": "2024-05-16",
-                    "temporal": "2016-01-01/2016-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c7b229a9-1c69-4b3e-a567-8a2a0179768e",
+                    "temporal": "2016-01-01/2016-12-31",
+                    "title": "CMS Program Statistics - Medicare Advantage - Outpatient Facility : 2016-01-15"
                 }
             ],
             "identifier": "https://data.cms.gov/data-api/v1/dataset/bbcffb70-4b07-4a0b-a783-0722b89315b5/data-viewer",
@@ -1124,63 +1123,63 @@
                 "fn": "CMS Program Statistics - OEDA",
                 "hasEmail": "mailto:IPAG_Data_Products@cms.hhs.gov"
             },
-            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
             "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
             "description": "The CMS Program Statistics \u2013 Medicare Advantage, Physician, Non-Physician Practitioner and Supplier tables provide utilization data for physician, non-physician practitioners, and suppliers, by Medicare Advantage beneficiaries.\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\nBelow is the list of tables:\n\n\n\tMDCR PHYSSUPP MA 1. \u00a0Medicare Physicians, Non-Physician Practitioners, and Suppliers: Utilization for Medicare Advantage Beneficiaries, by Type of Entitlement, Yearly Trend\n\tMDCR PHYSSUPP MA 2. \u00a0Medicare Physicians, Non-Physician Practitioners, and Suppliers: Utilization for Medicare Advantage Beneficiaries, by Demographic Characteristics and Medicare-Medicaid Enrollment Status\n\tMDCR PHYSSUPP MA 3. \u00a0Medicare Physicians, Non-Physician Practitioners, and Suppliers: Utilization for Medicare Advantage Beneficiaries, by Area of Residence\n\tMDCR PHYSSUPP MA 4. \u00a0Medicare Physicians, Non-Physician Practitioners, and Suppliers: \u00a0Utilization for Medicare Advantage Beneficiaries, by Place of Service\n\tMDCR PHYSSUPP MA 5. \u00a0Medicare Physicians, Non-Physician Practitioners, and Suppliers: \u00a0Utilization for Medicare Advantage Beneficiaries, by Restructured BETOS Classification System",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/CPS%20MDCR%20PHYSSUPP%20MA%202021%20FINAL.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6e25fb90-f405-406d-8f6c-ad5b71af3df9",
-                    "title": "CMS Program Statistics - Medicare Advantage - Physician, Non-Physician Practitioner & Supplier : 2021-05-06",
                     "modified": "2024-05-16",
-                    "temporal": "2021-01-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6e25fb90-f405-406d-8f6c-ad5b71af3df9",
+                    "temporal": "2021-01-01/2021-12-31",
+                    "title": "CMS Program Statistics - Medicare Advantage - Physician, Non-Physician Practitioner & Supplier : 2021-05-06"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/CPS%20MDCR%20PHYSSUPP%20MA%202020%20FINAL.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/97a3233e-ca2f-4400-9400-fb0f8b421a65",
-                    "title": "CMS Program Statistics - Medicare Advantage - Physician, Non-Physician Practitioner & Supplier : 2020-01-15",
                     "modified": "2024-05-16",
-                    "temporal": "2020-01-01/2020-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/97a3233e-ca2f-4400-9400-fb0f8b421a65",
+                    "temporal": "2020-01-01/2020-12-31",
+                    "title": "CMS Program Statistics - Medicare Advantage - Physician, Non-Physician Practitioner & Supplier : 2020-01-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/CPS%20MDCR%20PHYSSUPP%20MA%202019%20FINAL.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1bd4a4f0-9205-4c24-8f1f-1f196863759f",
-                    "title": "CMS Program Statistics - Medicare Advantage - Physician, Non-Physician Practitioner & Supplier : 2019-01-15",
                     "modified": "2024-05-16",
-                    "temporal": "2019-01-01/2019-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1bd4a4f0-9205-4c24-8f1f-1f196863759f",
+                    "temporal": "2019-01-01/2019-12-31",
+                    "title": "CMS Program Statistics - Medicare Advantage - Physician, Non-Physician Practitioner & Supplier : 2019-01-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/CPS%20MDCR%20PHYSSUPP%20MA%202018%20FINAL.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5e680f53-47bd-4ca6-947b-d3f045836e33",
-                    "title": "CMS Program Statistics - Medicare Advantage - Physician, Non-Physician Practitioner & Supplier : 2018-01-15",
                     "modified": "2024-05-16",
-                    "temporal": "2018-01-01/2018-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5e680f53-47bd-4ca6-947b-d3f045836e33",
+                    "temporal": "2018-01-01/2018-12-31",
+                    "title": "CMS Program Statistics - Medicare Advantage - Physician, Non-Physician Practitioner & Supplier : 2018-01-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/CPS%20MDCR%20PHYSSUPP%20MA%202017%20FINAL.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e5141c5a-11dd-4791-a1d1-f4c1fe0c3e9c",
-                    "title": "CMS Program Statistics - Medicare Advantage - Physician, Non-Physician Practitioner & Supplier : 2017-01-15",
                     "modified": "2024-05-16",
-                    "temporal": "2017-01-01/2017-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e5141c5a-11dd-4791-a1d1-f4c1fe0c3e9c",
+                    "temporal": "2017-01-01/2017-12-31",
+                    "title": "CMS Program Statistics - Medicare Advantage - Physician, Non-Physician Practitioner & Supplier : 2017-01-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/CPS%20MDCR%20PHYSSUPP%20MA%202016%20FINAL.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/077d0af1-eaa0-434c-823f-6a7d242680fb",
-                    "title": "CMS Program Statistics - Medicare Advantage - Physician, Non-Physician Practitioner & Supplier : 2016-01-15",
                     "modified": "2024-05-16",
-                    "temporal": "2016-01-01/2016-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/077d0af1-eaa0-434c-823f-6a7d242680fb",
+                    "temporal": "2016-01-01/2016-12-31",
+                    "title": "CMS Program Statistics - Medicare Advantage - Physician, Non-Physician Practitioner & Supplier : 2016-01-15"
                 }
             ],
             "identifier": "https://data.cms.gov/data-api/v1/dataset/900059a0-0a10-4f2f-8c3d-d8da432a421e/data-viewer",
@@ -1228,63 +1227,63 @@
                 "fn": "CMS Program Statistics - OEDA",
                 "hasEmail": "mailto:IPAG_Data_Products@cms.hhs.gov"
             },
-            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
             "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
             "description": "The CMS Program Statistics - Medicare Advantage, Inpatient Hospital tables provide utilization data for inpatient hospitals, including short-stay hospitals, critical access hospitals, long term care hospitals, inpatient psychiatric facilities, inpatient rehabilitation facilities, and other hospitals, by Medicare Advantage beneficiaries.\u00a0\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\u00a0\n\nBelow is the list of tables:\n\n\n\tMDCR INPT HOSP MA 4. \u00a0All Medicare Inpatient Hospital Types:\u00a0Utilization for Medicare Advantage Beneficiaries, by Type of Hospital\n\tMDCR INPT HOSP MA 5. \u00a0Medicare Short Stay Hospitals:\u00a0Utilization for Medicare Advantage Beneficiaries, by Type of Entitlement, Yearly Trend\n\tMDCR INPT HOSP MA 6. \u00a0Medicare Short Stay Hospitals: Utilization for Medicare Advantage Beneficiaries, by Demographic Characteristics and Medicare-Medicaid Enrollment Status\n\tMDCR INPT HOSP MA 7. \u00a0Medicare Short Stay Hospitals: Utilization for Medicare Advantage Beneficiaries, by Area of Residence\n\n\n\u00a0\n\nMDCR INPT HOSP MA 1 \u2013 MDCR INPT HOSP MA 3 are not available at this time.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/CPS%20MDCR%20INPT%20MA%202021%20FINAL_0.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ce3093ce-3185-4fad-a99d-a1b2929b7d1b",
-                    "title": "CMS Program Statistics - Medicare Advantage-Inpatient Hospital : 2021-12-01",
                     "modified": "2024-05-24",
-                    "temporal": "2021-01-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ce3093ce-3185-4fad-a99d-a1b2929b7d1b",
+                    "temporal": "2021-01-01/2021-12-31",
+                    "title": "CMS Program Statistics - Medicare Advantage-Inpatient Hospital : 2021-12-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/CPS%20MDCR%20INPT%20MA%202020%20FINAL_0.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/77a8ac7e-6dc7-4f48-a8d6-b7554e42be18",
-                    "title": "CMS Program Statistics - Medicare Advantage-Inpatient Hospital : 2020-12-01",
                     "modified": "2024-05-24",
-                    "temporal": "2020-01-01/2020-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/77a8ac7e-6dc7-4f48-a8d6-b7554e42be18",
+                    "temporal": "2020-01-01/2020-12-31",
+                    "title": "CMS Program Statistics - Medicare Advantage-Inpatient Hospital : 2020-12-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/CPS%20MDCR%20INPT%20MA%202019.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b93d05c0-5273-47c7-9262-66184aafbf4d",
-                    "title": "CMS Program Statistics - Medicare Advantage-Inpatient Hospital : 2019-12-01",
                     "modified": "2023-06-12",
-                    "temporal": "2019-01-01/2019-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b93d05c0-5273-47c7-9262-66184aafbf4d",
+                    "temporal": "2019-01-01/2019-12-31",
+                    "title": "CMS Program Statistics - Medicare Advantage-Inpatient Hospital : 2019-12-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/CPS%20MDCR%20INPT%20MA%202018.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/486be280-6cb7-42b3-916c-96e174efac13",
-                    "title": "CMS Program Statistics - Medicare Advantage-Inpatient Hospital : 2018-12-01",
                     "modified": "2023-06-12",
-                    "temporal": "2018-01-01/2018-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/486be280-6cb7-42b3-916c-96e174efac13",
+                    "temporal": "2018-01-01/2018-12-31",
+                    "title": "CMS Program Statistics - Medicare Advantage-Inpatient Hospital : 2018-12-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/CPS%20MDCR%20INPT%20MA%202017.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a2ec0aff-666e-4251-b89a-480c7da72c60",
-                    "title": "CMS Program Statistics - Medicare Advantage-Inpatient Hospital : 2017-12-01",
                     "modified": "2023-06-12",
-                    "temporal": "2017-01-01/2017-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a2ec0aff-666e-4251-b89a-480c7da72c60",
+                    "temporal": "2017-01-01/2017-12-31",
+                    "title": "CMS Program Statistics - Medicare Advantage-Inpatient Hospital : 2017-12-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/CPS%20MDCR%20INPT%20MA%202016.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a3547005-f18b-4917-8a52-f783128a78bf",
-                    "title": "CMS Program Statistics - Medicare Advantage-Inpatient Hospital : 2016-12-01",
                     "modified": "2023-06-12",
-                    "temporal": "2016-01-01/2016-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a3547005-f18b-4917-8a52-f783128a78bf",
+                    "temporal": "2016-01-01/2016-12-31",
+                    "title": "CMS Program Statistics - Medicare Advantage-Inpatient Hospital : 2016-12-01"
                 }
             ],
             "identifier": "https://data.cms.gov/data-api/v1/dataset/f7bc5d11-abce-4600-a680-a429f71e0653/data-viewer",
@@ -1332,63 +1331,63 @@
                 "fn": "CMS Program Statistics - OEDA",
                 "hasEmail": "mailto:IPAG_Data_Products@cms.hhs.gov"
             },
-            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
             "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
             "description": "The CMS Program Statistics - Medicare Advantage, Skilled Nursing Facility tables provide utilization data for skilled nursing facilities, by Medicare Advantage beneficiaries.\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. \u00a0Please use the download function to access the data.\n\n\u00a0\n\nBelow is the list of tables:\n\n\n\tMDCR SNF MA 1. \u00a0Medicare Skilled Nursing Facilities: Utilization for Medicare Advantage Beneficiaries, by Type of Entitlement, Yearly Trend\n\tMDCR SNF MA 2. \u00a0Medicare Skilled Nursing Facilities: Utilization for Medicare Advantage Beneficiaries, by Demographic Characteristics and Medicare-Medicaid Enrollment Status\n\tMDCR SNF MA 3. \u00a0Medicare Skilled Nursing Facilities: Utilization for Medicare Advantage Beneficiaries, by Area of Residence",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/CPS%20MDCR%20SNF%20MA%202021%20FINAL.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e01402ce-1bb1-42d8-84b2-4f6552466e9f",
-                    "title": "CMS Program Statistics - Medicare Advantage-Skilled Nursing Facility : 2021-12-01",
                     "modified": "2024-05-16",
-                    "temporal": "2021-01-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e01402ce-1bb1-42d8-84b2-4f6552466e9f",
+                    "temporal": "2021-01-01/2021-12-31",
+                    "title": "CMS Program Statistics - Medicare Advantage-Skilled Nursing Facility : 2021-12-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/CPS%20MDCR%20SNF%20MA%202020%20FINAL.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/35a53dde-7132-43be-a0a7-842e8f7fc59a",
-                    "title": "CMS Program Statistics - Medicare Advantage-Skilled Nursing Facility : 2020-12-01",
                     "modified": "2024-05-16",
-                    "temporal": "2020-01-01/2020-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/35a53dde-7132-43be-a0a7-842e8f7fc59a",
+                    "temporal": "2020-01-01/2020-12-31",
+                    "title": "CMS Program Statistics - Medicare Advantage-Skilled Nursing Facility : 2020-12-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/CPS%20MDCR%20SNF%20MA%202019.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bc6838eb-b5b2-4621-847a-25757385e8d3",
-                    "title": "CMS Program Statistics - Medicare Advantage-Skilled Nursing Facility : 2019-12-01",
                     "modified": "2023-06-12",
-                    "temporal": "2019-01-01/2019-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bc6838eb-b5b2-4621-847a-25757385e8d3",
+                    "temporal": "2019-01-01/2019-12-31",
+                    "title": "CMS Program Statistics - Medicare Advantage-Skilled Nursing Facility : 2019-12-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/CPS%20MDCR%20SNF%20MA%202018.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7e77b2ab-a4aa-4396-9df9-ed20408471e5",
-                    "title": "CMS Program Statistics - Medicare Advantage-Skilled Nursing Facility : 2018-12-01",
                     "modified": "2023-06-12",
-                    "temporal": "2018-01-01/2018-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7e77b2ab-a4aa-4396-9df9-ed20408471e5",
+                    "temporal": "2018-01-01/2018-12-31",
+                    "title": "CMS Program Statistics - Medicare Advantage-Skilled Nursing Facility : 2018-12-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/CPS%20MDCR%20SNF%20MA%202017.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a76ac577-31c6-40e1-aaf2-0422ee2e4b04",
-                    "title": "CMS Program Statistics - Medicare Advantage-Skilled Nursing Facility : 2017-12-01",
                     "modified": "2023-06-12",
-                    "temporal": "2017-01-01/2017-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a76ac577-31c6-40e1-aaf2-0422ee2e4b04",
+                    "temporal": "2017-01-01/2017-12-31",
+                    "title": "CMS Program Statistics - Medicare Advantage-Skilled Nursing Facility : 2017-12-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/CPS%20MDCR%20SNF%20MA%202016.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/39e40e7c-ff84-4777-bdd0-9a71ef794077",
-                    "title": "CMS Program Statistics - Medicare Advantage-Skilled Nursing Facility : 2016-12-01",
                     "modified": "2023-06-12",
-                    "temporal": "2016-01-01/2016-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/39e40e7c-ff84-4777-bdd0-9a71ef794077",
+                    "temporal": "2016-01-01/2016-12-31",
+                    "title": "CMS Program Statistics - Medicare Advantage-Skilled Nursing Facility : 2016-12-01"
                 }
             ],
             "identifier": "https://data.cms.gov/data-api/v1/dataset/81d7cb4c-9e7e-43ab-8858-0a2250291935/data-viewer",
@@ -1436,37 +1435,37 @@
                 "fn": "CMS Innovation Center - CMMI",
                 "hasEmail": "mailto:cmmi-dataset-support@cms.hhs.gov"
             },
-            "describedBy": "https://data.cms.gov/resources/comprehensive-care-for-joint-replacement-model-msa-data-dictionary",
             "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/comprehensive-care-for-joint-replacement-model-msa-data-dictionary",
             "description": "The Comprehensive Care for Joint Replacement Model: Metropolitan Statistical Areas (MSAs) dataset presents MSAs that are participating in the CMS Innovation Center Comprehensive Care for Joint Replacement Model, a model to support better and more efficient care for beneficiaries undergoing the most common inpatient surgery for Medicare beneficiaries: hip and knee replacements. Participation in this model is designated by geographic area, specifically MSAs. The information contained in the dataset can include MSA identification number, MSA geographic name and associated county or counties.\u00a0",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/62e490c0-9503-4b5f-9518-8e82fe20ccb6/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/62e490c0-9503-4b5f-9518-8e82fe20ccb6",
                     "description": "latest",
-                    "title": "Comprehensive Care for Joint Replacement Model: Metropolitan Statistical Areas : 2020-07-01",
+                    "format": "API",
                     "modified": "2021-01-04",
-                    "temporal": "2020-01-01/2020-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/62e490c0-9503-4b5f-9518-8e82fe20ccb6",
+                    "temporal": "2020-01-01/2020-12-31",
+                    "title": "Comprehensive Care for Joint Replacement Model: Metropolitan Statistical Areas : 2020-07-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2020-07/Comprehensive_Care_for_Joint_Replacement_Model__Metropolitan_Statistical_Areas__MSAs_.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a6076e90-62b4-4d61-8b54-f7b340797190",
-                    "title": "Comprehensive Care for Joint Replacement Model: Metropolitan Statistical Areas : 2020-07-01",
                     "modified": "2021-01-04",
-                    "temporal": "2020-01-01/2020-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a6076e90-62b4-4d61-8b54-f7b340797190",
+                    "temporal": "2020-01-01/2020-12-31",
+                    "title": "Comprehensive Care for Joint Replacement Model: Metropolitan Statistical Areas : 2020-07-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/a6076e90-62b4-4d61-8b54-f7b340797190/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a6076e90-62b4-4d61-8b54-f7b340797190",
-                    "title": "Comprehensive Care for Joint Replacement Model: Metropolitan Statistical Areas : 2020-07-01",
+                    "format": "API",
                     "modified": "2021-01-04",
-                    "temporal": "2020-01-01/2020-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a6076e90-62b4-4d61-8b54-f7b340797190",
+                    "temporal": "2020-01-01/2020-12-31",
+                    "title": "Comprehensive Care for Joint Replacement Model: Metropolitan Statistical Areas : 2020-07-01"
                 }
             ],
             "identifier": "https://data.cms.gov/data-api/v1/dataset/62e490c0-9503-4b5f-9518-8e82fe20ccb6/data-viewer",
@@ -1511,271 +1510,271 @@
                 "fn": "Shared Savings Program - CM",
                 "hasEmail": "mailto:SharedSavingsProgram@cms.hhs.gov"
             },
-            "describedBy": "https://data.cms.gov/resources/county-level-aggregate-expenditure-and-risk-score-data-on-assignable-beneficiaries-data-dictionary-0",
             "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/county-level-aggregate-expenditure-and-risk-score-data-on-assignable-beneficiaries-data-dictionary-0",
             "description": "The Shared Savings Program County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries Public Use File (PUF) for the Medicare Shared Savings Program (Shared Savings Program) provides aggregate data consisting of per capita Parts A and B FFS expenditures, average CMS-HCC prospective risk scores,\u00a0average demographic risk scores and total person-years for Shared Savings Program assignable beneficiaries by Medicare enrollment type (End Stage Renal Disease (ESRD), disabled, aged/dual eligible, aged/non-dual eligible).\n\n\u00a0\n\nDISCLAIMER: This information is current as of the last update. Changes to Shared Savings Program Accountable Care Organization (ACO) information occur periodically. Each Shared Savings Program ACO has the most up-to-date information about their organization. Consider contacting the Shared Savings Program ACO for the latest information. Contact information is available in the ACO PUF and the ACO Participants PUF.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/5f9f1216-6fd9-455d-bfbc-0efade687a4e/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5f9f1216-6fd9-455d-bfbc-0efade687a4e",
                     "description": "latest",
-                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2023-12-03oc2",
+                    "format": "API",
                     "modified": "2024-12-16",
-                    "temporal": "2023-01-01/2023-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5f9f1216-6fd9-455d-bfbc-0efade687a4e",
+                    "temporal": "2023-01-01/2023-12-31",
+                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2023-12-03oc2"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/61bd2a0f-62a0-4ef4-9580-56b5e3cb8ad0/County_Level_FFS_Data_for_Shared_Savings_Program_Benchmark_PUF_2023_Offest_Assignable_2024_Starters.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0b335816-649d-4a10-8c43-2ab47bf08852",
-                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2023-12-03oc2",
                     "modified": "2024-12-16",
-                    "temporal": "2023-01-01/2023-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0b335816-649d-4a10-8c43-2ab47bf08852",
+                    "temporal": "2023-01-01/2023-12-31",
+                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2023-12-03oc2"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/0b335816-649d-4a10-8c43-2ab47bf08852/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0b335816-649d-4a10-8c43-2ab47bf08852",
-                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2023-12-03oc2",
+                    "format": "API",
                     "modified": "2024-12-16",
-                    "temporal": "2023-01-01/2023-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0b335816-649d-4a10-8c43-2ab47bf08852",
+                    "temporal": "2023-01-01/2023-12-31",
+                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2023-12-03oc2"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/f2839854-b69f-4df5-b58b-217fd276ad8c/County_level_FFS_Data_for_Shared_Savings_Program_Benchmark_PUF_2023_Cal_Year_Assignable_2024_Starters.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4edf4a26-a014-409d-bd48-dab830f7f7bf",
-                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2023-12-02oc1",
                     "modified": "2024-12-16",
-                    "temporal": "2023-01-01/2023-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4edf4a26-a014-409d-bd48-dab830f7f7bf",
+                    "temporal": "2023-01-01/2023-12-31",
+                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2023-12-02oc1"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/4edf4a26-a014-409d-bd48-dab830f7f7bf/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4edf4a26-a014-409d-bd48-dab830f7f7bf",
-                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2023-12-02oc1",
+                    "format": "API",
                     "modified": "2024-12-16",
-                    "temporal": "2023-01-01/2023-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4edf4a26-a014-409d-bd48-dab830f7f7bf",
+                    "temporal": "2023-01-01/2023-12-31",
+                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2023-12-02oc1"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/a038f841-da53-4b89-b3f8-2876a2d50bee/County_Level%20FFS_Data_for_Shared_Savings_Program_Benchmark_PUF_2023_01_01_%20Cal_Year_Assignable_2019_2023_Starters.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/eeb048d0-aad6-42b9-988c-487c8da947e0",
-                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2023-12-01",
                     "modified": "2024-11-27",
-                    "temporal": "2023-01-01/2023-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/eeb048d0-aad6-42b9-988c-487c8da947e0",
+                    "temporal": "2023-01-01/2023-12-31",
+                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2023-12-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/eeb048d0-aad6-42b9-988c-487c8da947e0/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/eeb048d0-aad6-42b9-988c-487c8da947e0",
-                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2023-12-01",
+                    "format": "API",
                     "modified": "2024-11-27",
-                    "temporal": "2023-01-01/2023-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/eeb048d0-aad6-42b9-988c-487c8da947e0",
+                    "temporal": "2023-01-01/2023-12-31",
+                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2023-12-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/6a6ecadc-477b-4117-8368-7b4cd4a0ee45/County_Level_FFS_Data_for_Shared_Savings_Program_Benchmark_PUF_2022_Offest_Assignable_2024_starters.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3cbafed5-9147-43b3-bc2e-ee7795fce4a4",
-                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2022-12-19oc2",
                     "modified": "2024-12-16",
-                    "temporal": "2022-01-01/2022-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3cbafed5-9147-43b3-bc2e-ee7795fce4a4",
+                    "temporal": "2022-01-01/2022-12-31",
+                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2022-12-19oc2"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/3cbafed5-9147-43b3-bc2e-ee7795fce4a4/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3cbafed5-9147-43b3-bc2e-ee7795fce4a4",
-                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2022-12-19oc2",
+                    "format": "API",
                     "modified": "2024-12-16",
-                    "temporal": "2022-01-01/2022-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3cbafed5-9147-43b3-bc2e-ee7795fce4a4",
+                    "temporal": "2022-01-01/2022-12-31",
+                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2022-12-19oc2"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/9e8e9072-3195-4a6e-99fa-389adcf5457d/County_Level_FFS_Data_for_Shared_Savings_Program_Benchmark_PUF_2022_Cal_Year_Assignable_2024_Starters.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/21b7288e-02a3-4d5b-b1a0-5a2cfebb5c2f",
-                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2022-12-18oc1",
                     "modified": "2024-12-16",
-                    "temporal": "2022-01-01/2022-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/21b7288e-02a3-4d5b-b1a0-5a2cfebb5c2f",
+                    "temporal": "2022-01-01/2022-12-31",
+                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2022-12-18oc1"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/21b7288e-02a3-4d5b-b1a0-5a2cfebb5c2f/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/21b7288e-02a3-4d5b-b1a0-5a2cfebb5c2f",
-                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2022-12-18oc1",
+                    "format": "API",
                     "modified": "2024-12-16",
-                    "temporal": "2022-01-01/2022-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/21b7288e-02a3-4d5b-b1a0-5a2cfebb5c2f",
+                    "temporal": "2022-01-01/2022-12-31",
+                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2022-12-18oc1"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/325ab21c-3fd5-4dc0-82d8-6fff5f32852f/County_Level%20FFS_Data_for_Shared_Savings_Program_Benchmark_PUF_2022_01_01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ba11da80-56be-457d-af54-889733d0b413",
-                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2022-12-15",
                     "modified": "2024-12-06",
-                    "temporal": "2022-01-01/2022-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ba11da80-56be-457d-af54-889733d0b413",
+                    "temporal": "2022-01-01/2022-12-31",
+                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2022-12-15"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/ba11da80-56be-457d-af54-889733d0b413/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ba11da80-56be-457d-af54-889733d0b413",
-                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2022-12-15",
+                    "format": "API",
                     "modified": "2024-12-06",
-                    "temporal": "2022-01-01/2022-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ba11da80-56be-457d-af54-889733d0b413",
+                    "temporal": "2022-01-01/2022-12-31",
+                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2022-12-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/05b6760f-73ec-46e1-9747-7db5d0352dc3/County_Level%20FFS_Data_for_Shared_Savings_Program_Benchmark_PUF_2021_01_01_Offset_Assignable_2024_Starters.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/000ea270-0d91-4b2f-919a-7c0d78bcfc7e",
-                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2021-12-17oc2",
                     "modified": "2024-12-06",
-                    "temporal": "2021-01-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/000ea270-0d91-4b2f-919a-7c0d78bcfc7e",
+                    "temporal": "2021-01-01/2021-12-31",
+                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2021-12-17oc2"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/000ea270-0d91-4b2f-919a-7c0d78bcfc7e/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/000ea270-0d91-4b2f-919a-7c0d78bcfc7e",
-                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2021-12-17oc2",
+                    "format": "API",
                     "modified": "2024-12-06",
-                    "temporal": "2021-01-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/000ea270-0d91-4b2f-919a-7c0d78bcfc7e",
+                    "temporal": "2021-01-01/2021-12-31",
+                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2021-12-17oc2"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/86755826-2ecd-4aac-a19c-2e4bcdcc4977/County_Level%20FFS_Data_for_Shared_Savings_Program_Benchmark_PUF_2021_01_01_Cal_Year_Assignable_2024_Starters.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/54acabe4-aa6a-44f1-bd8c-55536bf6ea77",
-                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2021-12-16oc1",
                     "modified": "2024-12-06",
-                    "temporal": "2021-01-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/54acabe4-aa6a-44f1-bd8c-55536bf6ea77",
+                    "temporal": "2021-01-01/2021-12-31",
+                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2021-12-16oc1"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/54acabe4-aa6a-44f1-bd8c-55536bf6ea77/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/54acabe4-aa6a-44f1-bd8c-55536bf6ea77",
-                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2021-12-16oc1",
+                    "format": "API",
                     "modified": "2024-12-06",
-                    "temporal": "2021-01-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/54acabe4-aa6a-44f1-bd8c-55536bf6ea77",
+                    "temporal": "2021-01-01/2021-12-31",
+                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2021-12-16oc1"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/baf72a50-a6ab-431b-be00-c57785ad1d74/County_Level%20FFS_Data_for_Shared_Savings_Program_Benchmark_PUF_2021_01_01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a4154831-7934-4d7e-9b23-3441fee564d7",
-                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2021-12-15",
                     "modified": "2024-12-06",
-                    "temporal": "2021-01-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a4154831-7934-4d7e-9b23-3441fee564d7",
+                    "temporal": "2021-01-01/2021-12-31",
+                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2021-12-15"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/a4154831-7934-4d7e-9b23-3441fee564d7/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a4154831-7934-4d7e-9b23-3441fee564d7",
-                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2021-12-15",
+                    "format": "API",
                     "modified": "2024-12-06",
-                    "temporal": "2021-01-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a4154831-7934-4d7e-9b23-3441fee564d7",
+                    "temporal": "2021-01-01/2021-12-31",
+                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2021-12-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/b281a264-b4fe-4067-9b9e-9257abab4aca/County_Level%20FFS_Data_for_Shared_Savings_Program_Benchmark_PUF_2020_01_01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7b181182-828c-4fa4-91bd-641759f6eddd",
-                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2020-12-15",
                     "modified": "2024-12-06",
-                    "temporal": "2020-01-01/2020-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7b181182-828c-4fa4-91bd-641759f6eddd",
+                    "temporal": "2020-01-01/2020-12-31",
+                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2020-12-15"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/7b181182-828c-4fa4-91bd-641759f6eddd/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7b181182-828c-4fa4-91bd-641759f6eddd",
-                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2020-12-15",
+                    "format": "API",
                     "modified": "2024-12-06",
-                    "temporal": "2020-01-01/2020-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7b181182-828c-4fa4-91bd-641759f6eddd",
+                    "temporal": "2020-01-01/2020-12-31",
+                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2020-12-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/0023dd41-f80a-416c-8063-ff562e329611/County_Level%20FFS_Data_for_Shared_Savings_Program_Benchmark_PUF_2019_01_01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/28b6537c-c658-42bc-93b1-f2c32e8c00ae",
-                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2019-01-15",
                     "modified": "2024-12-06",
-                    "temporal": "2019-01-01/2019-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/28b6537c-c658-42bc-93b1-f2c32e8c00ae",
+                    "temporal": "2019-01-01/2019-12-31",
+                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2019-01-15"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/28b6537c-c658-42bc-93b1-f2c32e8c00ae/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/28b6537c-c658-42bc-93b1-f2c32e8c00ae",
-                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2019-01-15",
+                    "format": "API",
                     "modified": "2024-12-06",
-                    "temporal": "2019-01-01/2019-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/28b6537c-c658-42bc-93b1-f2c32e8c00ae",
+                    "temporal": "2019-01-01/2019-12-31",
+                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2019-01-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/dcb4a81d-9dcd-46ce-81c2-fcaa2fd09c89/County_Level%20FFS_Data_for_Shared_Savings_Program_Benchmark_PUF_2018_01_01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c78d06dc-816d-46e4-821c-25a022c1096f",
-                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2018-01-15",
                     "modified": "2024-12-06",
-                    "temporal": "2018-01-01/2018-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c78d06dc-816d-46e4-821c-25a022c1096f",
+                    "temporal": "2018-01-01/2018-12-31",
+                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2018-01-15"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/c78d06dc-816d-46e4-821c-25a022c1096f/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c78d06dc-816d-46e4-821c-25a022c1096f",
-                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2018-01-15",
+                    "format": "API",
                     "modified": "2024-12-06",
-                    "temporal": "2018-01-01/2018-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c78d06dc-816d-46e4-821c-25a022c1096f",
+                    "temporal": "2018-01-01/2018-12-31",
+                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2018-01-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/8700eb99-4430-4fae-9eb3-1649f96d99e1/County_Level%20FFS_Data_for_Shared_Savings_Program_Benchmark_PUF_2017_01_01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e60ff4ba-e1f3-4645-891e-bc5badf5e580",
-                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2017-01-15",
                     "modified": "2024-12-06",
-                    "temporal": "2017-01-01/2017-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e60ff4ba-e1f3-4645-891e-bc5badf5e580",
+                    "temporal": "2017-01-01/2017-12-31",
+                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2017-01-15"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/e60ff4ba-e1f3-4645-891e-bc5badf5e580/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e60ff4ba-e1f3-4645-891e-bc5badf5e580",
-                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2017-01-15",
+                    "format": "API",
                     "modified": "2024-12-06",
-                    "temporal": "2017-01-01/2017-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e60ff4ba-e1f3-4645-891e-bc5badf5e580",
+                    "temporal": "2017-01-01/2017-12-31",
+                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2017-01-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/eb5b1694-a3d2-4d8e-85b7-9925d5ff7f40/County_Level%20FFS_Data_for_Shared_Savings_Program_Benchmark_PUF_2016_01_01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fe7b9822-f528-44b6-9ee7-5f65b86e1027",
-                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2016-01-15",
                     "modified": "2024-04-10",
-                    "temporal": "2016-01-01/2016-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fe7b9822-f528-44b6-9ee7-5f65b86e1027",
+                    "temporal": "2016-01-01/2016-12-31",
+                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2016-01-15"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/fe7b9822-f528-44b6-9ee7-5f65b86e1027/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fe7b9822-f528-44b6-9ee7-5f65b86e1027",
-                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2016-01-15",
+                    "format": "API",
                     "modified": "2024-04-10",
-                    "temporal": "2016-01-01/2016-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fe7b9822-f528-44b6-9ee7-5f65b86e1027",
+                    "temporal": "2016-01-01/2016-12-31",
+                    "title": "County-level Aggregate Expenditure and Risk Score Data on Assignable Beneficiaries : 2016-01-15"
                 }
             ],
             "identifier": "https://data.cms.gov/data-api/v1/dataset/5f9f1216-6fd9-455d-bfbc-0efade687a4e/data-viewer",
@@ -1823,2144 +1822,2144 @@
                 "fn": "COVID-19 Nursing Home Data - CCSQ",
                 "hasEmail": "mailto:NH_COVID_Data@cms.hhs.gov"
             },
+            "dataQuality": true,
             "describedBy": "https://data.cms.gov/sites/default/files/2024-10/COVID-19%20Nursing%20Home%20Data%20Dictionary_0.pdf",
             "describedByType": "application/pdf",
-            "dataQuality": true,
             "description": "Submitted data as of the week ending 01/05/2025.\n\nThe Nursing Home COVID-19 Public File includes data reported by nursing homes to the CDC\u2019s National Healthcare Safety Network (NHSN) Long Term Care Facility (LTCF) COVID-19 Module.\u00a0For resources and ways to explore and visualize the data, please see the links to the left, as well as the buttons at the top of the page.\n\nUp to Date with COVID-19 Vaccines\n\nOn January 1, 2024, the Centers for Disease Control (CDC) changed the way it collects data to calculate the percent of staff who are up to date with their COVID-19 vaccination. It may take facilities some time to adapt to the new methodology. As a result, the reported percent of staff who are up to date with their COVID-19 vaccination should be viewed with caution over the next few weeks. Contact facilities directly for more information on their vaccination levels.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/137f90cb-ac53-4b3d-8358-e65cf64e03d3/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/137f90cb-ac53-4b3d-8358-e65cf64e03d3",
                     "description": "latest",
-                    "title": "COVID-19 Nursing Home Data : 2025-01-05",
+                    "format": "API",
                     "modified": "2025-01-16",
-                    "temporal": "2024-12-29/2025-01-04"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/137f90cb-ac53-4b3d-8358-e65cf64e03d3",
+                    "temporal": "2024-12-29/2025-01-04",
+                    "title": "COVID-19 Nursing Home Data : 2025-01-05"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/32199fe1-8845-4007-b9dc-1f5562bf3e80/COVID-19%20Nursing%20Home%20Data%2001.05.2025.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/64db7975-4f2e-4c8d-9c83-c50753c89cd2",
-                    "title": "COVID-19 Nursing Home Data : 2025-01-05",
                     "modified": "2025-01-16",
-                    "temporal": "2024-12-29/2025-01-04"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/64db7975-4f2e-4c8d-9c83-c50753c89cd2",
+                    "temporal": "2024-12-29/2025-01-04",
+                    "title": "COVID-19 Nursing Home Data : 2025-01-05"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/64db7975-4f2e-4c8d-9c83-c50753c89cd2/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/64db7975-4f2e-4c8d-9c83-c50753c89cd2",
-                    "title": "COVID-19 Nursing Home Data : 2025-01-05",
+                    "format": "API",
                     "modified": "2025-01-16",
-                    "temporal": "2024-12-29/2025-01-04"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/64db7975-4f2e-4c8d-9c83-c50753c89cd2",
+                    "temporal": "2024-12-29/2025-01-04",
+                    "title": "COVID-19 Nursing Home Data : 2025-01-05"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/772ffd8b-6e41-4a0e-a465-a2e6445c9a4e/COVID-19%20Nursing%20Home%20Data%20Dec%2029%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4c751ace-622b-4035-ae47-daae4a93d21b",
-                    "title": "COVID-19 Nursing Home Data : 2024-12-29",
                     "modified": "2025-01-16",
-                    "temporal": "2024-12-22/2024-12-28"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4c751ace-622b-4035-ae47-daae4a93d21b",
+                    "temporal": "2024-12-22/2024-12-28",
+                    "title": "COVID-19 Nursing Home Data : 2024-12-29"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/a8307994-ca6f-44dc-85d6-72cc36cd2029/COVID-19%20Nursing%20Home%20Data%20Dec%2008%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/54a00c2a-f73b-4820-baf3-f913c13bc500",
-                    "title": "COVID-19 Nursing Home Data : 2024-12-08",
                     "modified": "2025-01-08",
-                    "temporal": "2024-12-01/2024-12-07"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/54a00c2a-f73b-4820-baf3-f913c13bc500",
+                    "temporal": "2024-12-01/2024-12-07",
+                    "title": "COVID-19 Nursing Home Data : 2024-12-08"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/e8adf204-a740-45d3-8f6e-d9511bc43d59/COVID-19%20Nursing%20Home%20Data%20Dec%2001%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/dc991880-176c-415d-ba31-990863bb024f",
-                    "title": "COVID-19 Nursing Home Data : 2024-12-01",
                     "modified": "2024-12-19",
-                    "temporal": "2024-11-24/2024-11-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/dc991880-176c-415d-ba31-990863bb024f",
+                    "temporal": "2024-11-24/2024-11-30",
+                    "title": "COVID-19 Nursing Home Data : 2024-12-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/84d1d03a-4e1f-4045-9128-e048bcb241d5/COVID-19%20Nursing%20Home%20Data%20Nov%2024%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e3cdd0a5-4769-40e0-a637-7f32a6802c33",
-                    "title": "COVID-19 Nursing Home Data : 2024-11-24",
                     "modified": "2024-12-12",
-                    "temporal": "2024-11-17/2024-11-23"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e3cdd0a5-4769-40e0-a637-7f32a6802c33",
+                    "temporal": "2024-11-17/2024-11-23",
+                    "title": "COVID-19 Nursing Home Data : 2024-11-24"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/367f7065-f8d4-4f52-bcf0-8569df5a8d3d/COVID-19%20Nursing%20Home%20Data%20Nov%2010%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/126f75d7-e969-4318-8926-78bf2564d156",
-                    "title": "COVID-19 Nursing Home Data : 2024-11-10",
                     "modified": "2024-12-05",
-                    "temporal": "2024-11-03/2024-11-09"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/126f75d7-e969-4318-8926-78bf2564d156",
+                    "temporal": "2024-11-03/2024-11-09",
+                    "title": "COVID-19 Nursing Home Data : 2024-11-10"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/3a756717-8e5f-4eec-913f-44b58913269f/COVID-19%20Nursing%20Home%20Data%20Nov%2003%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bcff3b94-19ab-4ca3-8368-42a03810d519",
-                    "title": "COVID-19 Nursing Home Data : 2024-11-03",
                     "modified": "2024-11-21",
-                    "temporal": "2024-10-27/2024-11-02"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bcff3b94-19ab-4ca3-8368-42a03810d519",
+                    "temporal": "2024-10-27/2024-11-02",
+                    "title": "COVID-19 Nursing Home Data : 2024-11-03"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/ae78830e-f13f-4965-a589-9227a8244248/COVID-19%20Nursing%20Home%20Data%20Oct%2027%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/89355d7a-442d-4835-b5cd-b7958bd93ce0",
-                    "title": "COVID-19 Nursing Home Data : 2024-10-27",
                     "modified": "2024-11-14",
-                    "temporal": "2024-10-20/2024-10-26"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/89355d7a-442d-4835-b5cd-b7958bd93ce0",
+                    "temporal": "2024-10-20/2024-10-26",
+                    "title": "COVID-19 Nursing Home Data : 2024-10-27"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/60d48d89-517a-4185-aef4-b941d37f43cf/COVID-19%20Nursing%20Home%20Data%20Oct%2020%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/82442dbf-712e-4d18-b1d6-12f1db2d1840",
-                    "title": "COVID-19 Nursing Home Data : 2024-10-20",
                     "modified": "2024-11-07",
-                    "temporal": "2024-10-13/2024-10-19"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/82442dbf-712e-4d18-b1d6-12f1db2d1840",
+                    "temporal": "2024-10-13/2024-10-19",
+                    "title": "COVID-19 Nursing Home Data : 2024-10-20"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/a957243d-a3ad-45f2-9101-018a87583a53/COVID-19%20Nursing%20Home%20Data%20Oct%2013%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d9d78412-212a-450d-81af-5babde57f4a1",
-                    "title": "COVID-19 Nursing Home Data : 2024-10-13",
                     "modified": "2024-10-31",
-                    "temporal": "2024-10-06/2024-10-12"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d9d78412-212a-450d-81af-5babde57f4a1",
+                    "temporal": "2024-10-06/2024-10-12",
+                    "title": "COVID-19 Nursing Home Data : 2024-10-13"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/d9b4571c-d074-43bd-96c2-b99aa7193a7e/COVID-19%20Nursing%20Home%20Data%20Oct%2006%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/336e1546-413d-4001-a5ee-aa37c1ca7a4c",
-                    "title": "COVID-19 Nursing Home Data : 2024-10-06",
                     "modified": "2024-10-25",
-                    "temporal": "2024-09-29/2024-10-05"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/336e1546-413d-4001-a5ee-aa37c1ca7a4c",
+                    "temporal": "2024-09-29/2024-10-05",
+                    "title": "COVID-19 Nursing Home Data : 2024-10-06"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/e0929720-08ce-43be-922b-f7e980b1b962/COVID-19%20Nursing%20Home%20Data%20Sep%2029%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f6d30c56-1b1f-4353-b862-31382f2ffff5",
-                    "title": "COVID-19 Nursing Home Data : 2024-09-29",
                     "modified": "2024-10-17",
-                    "temporal": "2024-09-22/2024-09-28"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f6d30c56-1b1f-4353-b862-31382f2ffff5",
+                    "temporal": "2024-09-22/2024-09-28",
+                    "title": "COVID-19 Nursing Home Data : 2024-09-29"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/fb03cce5-3053-4536-a990-4599dd1cb0b1/COVID-19%20Nursing%20Home%20Data%20Sep%2022%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d5a15660-9c85-46d7-a906-54830cf0d246",
-                    "title": "COVID-19 Nursing Home Data : 2024-09-22",
                     "modified": "2024-10-10",
-                    "temporal": "2024-09-15/2024-09-21"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d5a15660-9c85-46d7-a906-54830cf0d246",
+                    "temporal": "2024-09-15/2024-09-21",
+                    "title": "COVID-19 Nursing Home Data : 2024-09-22"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/8bd6f9cb-e186-485e-87ee-ed463e613b94/COVID-19%20Nursing%20Home%20Data%20Sep%2015%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b734ebd5-0e19-4562-b500-31adddb31b62",
-                    "title": "COVID-19 Nursing Home Data : 2024-09-15",
                     "modified": "2024-10-03",
-                    "temporal": "2024-09-08/2024-09-14"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b734ebd5-0e19-4562-b500-31adddb31b62",
+                    "temporal": "2024-09-08/2024-09-14",
+                    "title": "COVID-19 Nursing Home Data : 2024-09-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/4694c3ab-ef18-4eac-9cc8-4c46dec70bf0/COVID-19%20Nursing%20Home%20Data%20Sep%2008%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/50602113-04df-459b-9fb0-f0954c8fd4fd",
-                    "title": "COVID-19 Nursing Home Data : 2024-09-08",
                     "modified": "2024-09-19",
-                    "temporal": "2024-09-01/2024-09-07"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/50602113-04df-459b-9fb0-f0954c8fd4fd",
+                    "temporal": "2024-09-01/2024-09-07",
+                    "title": "COVID-19 Nursing Home Data : 2024-09-08"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/054b24c0-0aab-4ed3-80ae-1876ffc7bf90/COVID-19%20Nursing%20Home%20Data%20Sep%2001%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b744be20-f214-4579-99a1-c042876ccf44",
-                    "title": "COVID-19 Nursing Home Data : 2024-09-01",
                     "modified": "2024-09-19",
-                    "temporal": "2024-08-25/2024-08-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b744be20-f214-4579-99a1-c042876ccf44",
+                    "temporal": "2024-08-25/2024-08-31",
+                    "title": "COVID-19 Nursing Home Data : 2024-09-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/ca4beb1e-be4d-45c1-a40e-ec19d8a4fba6/COVID-19%20Nursing%20Home%20Data%20Aug%2025%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2a131004-7b77-4639-a435-d275ba223e7f",
-                    "title": "COVID-19 Nursing Home Data : 2024-08-25",
                     "modified": "2024-09-12",
-                    "temporal": "2024-08-18/2024-08-24"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2a131004-7b77-4639-a435-d275ba223e7f",
+                    "temporal": "2024-08-18/2024-08-24",
+                    "title": "COVID-19 Nursing Home Data : 2024-08-25"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/75ad1acd-d79f-4052-9cfd-682de2aa527e/COVID-19%20Nursing%20Home%20Data%20Aug%2018%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ecb89327-c21c-4eee-868d-25bc4bb44cfc",
-                    "title": "COVID-19 Nursing Home Data : 2024-08-18",
                     "modified": "2024-09-05",
-                    "temporal": "2024-08-11/2024-08-17"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ecb89327-c21c-4eee-868d-25bc4bb44cfc",
+                    "temporal": "2024-08-11/2024-08-17",
+                    "title": "COVID-19 Nursing Home Data : 2024-08-18"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/d676bfd6-089d-4d52-b3d6-f05db220f198/COVID-19%20Nursing%20Home%20Data%20Aug%2011%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/99591979-7d3c-4f1f-bd4e-5d78b3a8b01a",
-                    "title": "COVID-19 Nursing Home Data : 2024-08-11",
                     "modified": "2024-08-29",
-                    "temporal": "2024-08-04/2024-08-10"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/99591979-7d3c-4f1f-bd4e-5d78b3a8b01a",
+                    "temporal": "2024-08-04/2024-08-10",
+                    "title": "COVID-19 Nursing Home Data : 2024-08-11"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/5402a992-16b4-4b8c-8b0e-b2e43a6a442e/COVID-19%20Nursing%20Home%20Data%20Aug%2004%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/727a1c0c-4a4b-48ec-b315-e7c10c20799b",
-                    "title": "COVID-19 Nursing Home Data : 2024-08-04",
                     "modified": "2024-08-22",
-                    "temporal": "2024-07-28/2024-08-03"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/727a1c0c-4a4b-48ec-b315-e7c10c20799b",
+                    "temporal": "2024-07-28/2024-08-03",
+                    "title": "COVID-19 Nursing Home Data : 2024-08-04"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/95b18965-eec0-4360-b63b-a0a60ed5d591/COVID-19%20Nursing%20Home%20Data%20Jul%2028%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f04a571a-fda9-4a42-bb6c-62acba3b93cf",
-                    "title": "COVID-19 Nursing Home Data : 2024-07-28",
                     "modified": "2024-08-15",
-                    "temporal": "2024-07-21/2024-07-27"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f04a571a-fda9-4a42-bb6c-62acba3b93cf",
+                    "temporal": "2024-07-21/2024-07-27",
+                    "title": "COVID-19 Nursing Home Data : 2024-07-28"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/5feafb25-aed9-4acd-8f51-666b38d4c07a/COVID-19%20Nursing%20Home%20Data%20Jul%2021%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b2b4c421-f884-4b7a-9e8a-8e462bf9b9c2",
-                    "title": "COVID-19 Nursing Home Data : 2024-07-21",
                     "modified": "2024-08-08",
-                    "temporal": "2024-07-14/2024-07-20"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b2b4c421-f884-4b7a-9e8a-8e462bf9b9c2",
+                    "temporal": "2024-07-14/2024-07-20",
+                    "title": "COVID-19 Nursing Home Data : 2024-07-21"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/776f201f-39e4-4622-a1f8-c45066d3288c/COVID-19%20Nursing%20Home%20Data%20Jul%2014%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f5ef9b1e-ac3f-4bd5-9ac3-591f4b7e252d",
-                    "title": "COVID-19 Nursing Home Data : 2024-07-14",
                     "modified": "2024-08-01",
-                    "temporal": "2024-07-07/2024-07-13"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f5ef9b1e-ac3f-4bd5-9ac3-591f4b7e252d",
+                    "temporal": "2024-07-07/2024-07-13",
+                    "title": "COVID-19 Nursing Home Data : 2024-07-14"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/527c376b-61f1-4c2f-86ee-e0f984f31ecf/COVID-19%20Nursing%20Home%20Data%20Jul%2007%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/10130ed3-8379-4894-94f8-5581808fc165",
-                    "title": "COVID-19 Nursing Home Data : 2024-07-07",
                     "modified": "2024-07-25",
-                    "temporal": "2024-06-30/2024-07-06"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/10130ed3-8379-4894-94f8-5581808fc165",
+                    "temporal": "2024-06-30/2024-07-06",
+                    "title": "COVID-19 Nursing Home Data : 2024-07-07"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/1eec351f-4f5d-48c8-853a-88f520975cdc/COVID-19%20Nursing%20Home%20Data%20Jun%2030%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d9bd7e64-cd45-45c0-ad52-3ec89d573fdf",
-                    "title": "COVID-19 Nursing Home Data : 2024-06-30",
                     "modified": "2024-07-18",
-                    "temporal": "2024-06-23/2024-06-29"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d9bd7e64-cd45-45c0-ad52-3ec89d573fdf",
+                    "temporal": "2024-06-23/2024-06-29",
+                    "title": "COVID-19 Nursing Home Data : 2024-06-30"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/00b2d193-5b33-4117-9782-5fa1c4040ebc/COVID-19%20Nursing%20Home%20Data%20Jun%2023%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5befeea5-71d8-4f19-b82a-36ea33663de6",
-                    "title": "COVID-19 Nursing Home Data : 2024-06-23",
                     "modified": "2024-07-11",
-                    "temporal": "2024-06-16/2024-06-22"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5befeea5-71d8-4f19-b82a-36ea33663de6",
+                    "temporal": "2024-06-16/2024-06-22",
+                    "title": "COVID-19 Nursing Home Data : 2024-06-23"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/61766e3a-a86c-4d74-acd5-5bf9b32dbf41/COVID-19%20Nursing%20Home%20Data%20Jun%2016%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5ebe7e5a-873c-400b-9ccb-640aec6cb722",
-                    "title": "COVID-19 Nursing Home Data : 2024-06-16",
                     "modified": "2024-07-03",
-                    "temporal": "2024-06-09/2024-06-15"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5ebe7e5a-873c-400b-9ccb-640aec6cb722",
+                    "temporal": "2024-06-09/2024-06-15",
+                    "title": "COVID-19 Nursing Home Data : 2024-06-16"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/2843f6b3-f9ec-4f14-aef8-094486251f21/COVID-19%20Nursing%20Home%20Data%20Jun%2009%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f955fcff-ec76-42d7-8756-e1889916dfb2",
-                    "title": "COVID-19 Nursing Home Data : 2024-06-09",
                     "modified": "2024-06-27",
-                    "temporal": "2024-06-02/2024-06-08"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f955fcff-ec76-42d7-8756-e1889916dfb2",
+                    "temporal": "2024-06-02/2024-06-08",
+                    "title": "COVID-19 Nursing Home Data : 2024-06-09"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/ee302769-b2f2-458d-ab8a-ac437ef8aed9/COVID-19%20Nursing%20Home%20Data%20Jun%2002%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9d41c844-6721-49f9-96fd-7cc6602164f6",
-                    "title": "COVID-19 Nursing Home Data : 2024-06-02",
                     "modified": "2024-06-20",
-                    "temporal": "2024-05-26/2024-06-01"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9d41c844-6721-49f9-96fd-7cc6602164f6",
+                    "temporal": "2024-05-26/2024-06-01",
+                    "title": "COVID-19 Nursing Home Data : 2024-06-02"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/a5729f7c-0534-4f78-8557-03f1373a0ffd/COVID-19%20Nursing%20Home%20Data%20May%2026%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2d8fced1-b0f3-48a5-9df1-1cafaca6e276",
-                    "title": "COVID-19 Nursing Home Data : 2024-05-26",
                     "modified": "2024-06-13",
-                    "temporal": "2024-05-19/2024-05-25"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2d8fced1-b0f3-48a5-9df1-1cafaca6e276",
+                    "temporal": "2024-05-19/2024-05-25",
+                    "title": "COVID-19 Nursing Home Data : 2024-05-26"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/a72aa146-d89c-45a4-82c4-efc1f3f779e0/COVID-19%20Nursing%20Home%20Data%20May%2019%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5b5fb277-8f6c-42cd-be68-032134861b51",
-                    "title": "COVID-19 Nursing Home Data : 2024-05-19",
                     "modified": "2024-06-06",
-                    "temporal": "2024-05-12/2024-05-18"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5b5fb277-8f6c-42cd-be68-032134861b51",
+                    "temporal": "2024-05-12/2024-05-18",
+                    "title": "COVID-19 Nursing Home Data : 2024-05-19"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/32f57561-dec5-489f-9102-611c0f3d17d6/COVID-19%20Nursing%20Home%20Data%20May%2012%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/63682322-00e0-42f0-b054-757484f38aa6",
-                    "title": "COVID-19 Nursing Home Data : 2024-05-12",
                     "modified": "2024-05-30",
-                    "temporal": "2024-05-05/2024-05-11"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/63682322-00e0-42f0-b054-757484f38aa6",
+                    "temporal": "2024-05-05/2024-05-11",
+                    "title": "COVID-19 Nursing Home Data : 2024-05-12"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/3eace1c8-a474-4477-a7cc-bf194efef7ae/COVID-19%20Nursing%20Home%20Data%20May%2005%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5b85e1f8-ed78-42c9-a29a-a9ef6fb71c73",
-                    "title": "COVID-19 Nursing Home Data : 2024-05-05",
                     "modified": "2024-05-23",
-                    "temporal": "2024-04-28/2024-05-04"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5b85e1f8-ed78-42c9-a29a-a9ef6fb71c73",
+                    "temporal": "2024-04-28/2024-05-04",
+                    "title": "COVID-19 Nursing Home Data : 2024-05-05"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/44d974ad-a28a-4902-94d1-0c79d8ab98a3/COVID-19%20Nursing%20Home%20Data%20Apr%2028%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b8cc675d-4f58-461b-8202-64b262cf34a7",
-                    "title": "COVID-19 Nursing Home Data : 2024-04-28",
                     "modified": "2024-05-16",
-                    "temporal": "2024-04-21/2024-04-27"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b8cc675d-4f58-461b-8202-64b262cf34a7",
+                    "temporal": "2024-04-21/2024-04-27",
+                    "title": "COVID-19 Nursing Home Data : 2024-04-28"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/c4bd805d-d2bb-4a4a-aad8-75c7e83b9d23/COVID-19%20Nursing%20Home%20Data%20Apr%2021%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6c43fe5e-687d-4147-9100-001fc6b646cc",
-                    "title": "COVID-19 Nursing Home Data : 2024-04-21",
                     "modified": "2024-05-09",
-                    "temporal": "2024-04-14/2024-04-20"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6c43fe5e-687d-4147-9100-001fc6b646cc",
+                    "temporal": "2024-04-14/2024-04-20",
+                    "title": "COVID-19 Nursing Home Data : 2024-04-21"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/af393da7-0b3c-4736-9c1a-48f28a4cda67/COVID-19%20Nursing%20Home%20Data%20Apr%2014%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/df55bb4d-4c62-4bbb-8990-0caa3c7a4326",
-                    "title": "COVID-19 Nursing Home Data : 2024-04-14",
                     "modified": "2024-04-25",
-                    "temporal": "2024-04-07/2024-04-13"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/df55bb4d-4c62-4bbb-8990-0caa3c7a4326",
+                    "temporal": "2024-04-07/2024-04-13",
+                    "title": "COVID-19 Nursing Home Data : 2024-04-14"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/7ab8a4f7-9450-4ac0-95f0-172cdeba3edb/COVID-19%20Nursing%20Home%20Data%20Apr%2007%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/329a4742-d3c4-4e39-9ff7-75aa81b18a13",
-                    "title": "COVID-19 Nursing Home Data : 2024-04-07",
                     "modified": "2024-04-18",
-                    "temporal": "2024-03-31/2024-04-06"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/329a4742-d3c4-4e39-9ff7-75aa81b18a13",
+                    "temporal": "2024-03-31/2024-04-06",
+                    "title": "COVID-19 Nursing Home Data : 2024-04-07"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/3d0588bb-fd85-4b2e-aa84-3348a9f7cfa3/COVID-19%20Nursing%20Home%20Data%20Mar%2031%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/174ce662-327b-4258-b867-97d3bfb97d51",
-                    "title": "COVID-19 Nursing Home Data : 2024-03-31",
                     "modified": "2024-04-18",
-                    "temporal": "2024-03-24/2024-03-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/174ce662-327b-4258-b867-97d3bfb97d51",
+                    "temporal": "2024-03-24/2024-03-30",
+                    "title": "COVID-19 Nursing Home Data : 2024-03-31"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/f49f73e1-b2b2-4dda-b654-667b891d1e62/COVID-19%20Nursing%20Home%20Data%20Mar%2024%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/40af9126-ba2b-4250-9728-0bf0d88af0c4",
-                    "title": "COVID-19 Nursing Home Data : 2024-03-24",
                     "modified": "2024-04-04",
-                    "temporal": "2024-03-17/2024-03-23"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/40af9126-ba2b-4250-9728-0bf0d88af0c4",
+                    "temporal": "2024-03-17/2024-03-23",
+                    "title": "COVID-19 Nursing Home Data : 2024-03-24"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/52c852da-9c38-4d0b-85e0-729145b3fd4c/COVID-19%20Nursing%20Home%20Data%20Mar%2017%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4115df5d-4f53-4e42-91d3-16a1e64b1205",
-                    "title": "COVID-19 Nursing Home Data : 2024-03-17",
                     "modified": "2024-03-28",
-                    "temporal": "2024-03-10/2024-03-16"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4115df5d-4f53-4e42-91d3-16a1e64b1205",
+                    "temporal": "2024-03-10/2024-03-16",
+                    "title": "COVID-19 Nursing Home Data : 2024-03-17"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/d648b602-fb69-4b86-b28c-af11acafcafc/COVID-19%20Nursing%20Home%20Data%20Mar%2010%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/eb16337c-9661-4756-82bd-c33e0be127a0",
-                    "title": "COVID-19 Nursing Home Data : 2024-03-10",
                     "modified": "2024-03-21",
-                    "temporal": "2024-03-03/2024-03-09"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/eb16337c-9661-4756-82bd-c33e0be127a0",
+                    "temporal": "2024-03-03/2024-03-09",
+                    "title": "COVID-19 Nursing Home Data : 2024-03-10"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/67c45c00-9f62-43c9-b94f-5ec4e5e23262/COVID-19%20Nursing%20Home%20Data%20Mar%2003%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/aaa0d7e6-3245-4f80-a5fb-a7a17d49f43c",
-                    "title": "COVID-19 Nursing Home Data : 2024-03-03",
                     "modified": "2024-03-14",
-                    "temporal": "2024-02-25/2024-03-02"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/aaa0d7e6-3245-4f80-a5fb-a7a17d49f43c",
+                    "temporal": "2024-02-25/2024-03-02",
+                    "title": "COVID-19 Nursing Home Data : 2024-03-03"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/f375bcb6-0882-4528-9362-5d83e3a51009/COVID-19%20Nursing%20Home%20Data%20Feb%2025%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2ad322bb-06e6-4564-815f-899a52137872",
-                    "title": "COVID-19 Nursing Home Data : 2024-02-25",
                     "modified": "2024-03-07",
-                    "temporal": "2024-02-18/2024-02-24"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2ad322bb-06e6-4564-815f-899a52137872",
+                    "temporal": "2024-02-18/2024-02-24",
+                    "title": "COVID-19 Nursing Home Data : 2024-02-25"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/86223cac-8213-4f7e-a489-d26a3a4ae323/COVID-19%20Nursing%20Home%20Data%20Feb%2018%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bdb738d2-a6c5-450d-9c41-4ccdcf307ec4",
-                    "title": "COVID-19 Nursing Home Data : 2024-02-18",
                     "modified": "2024-03-07",
-                    "temporal": "2024-02-11/2024-02-17"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bdb738d2-a6c5-450d-9c41-4ccdcf307ec4",
+                    "temporal": "2024-02-11/2024-02-17",
+                    "title": "COVID-19 Nursing Home Data : 2024-02-18"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/63f7d4c7-c331-47fa-901d-df94e81d37f8/COVID-19%20Nursing%20Home%20Data%20Feb%2011%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bad0fc93-8f91-4f17-bcc8-f756e7aae37c",
-                    "title": "COVID-19 Nursing Home Data : 2024-02-11",
                     "modified": "2024-02-22",
-                    "temporal": "2024-02-04/2024-02-10"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bad0fc93-8f91-4f17-bcc8-f756e7aae37c",
+                    "temporal": "2024-02-04/2024-02-10",
+                    "title": "COVID-19 Nursing Home Data : 2024-02-11"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/b9b705b5-0ec3-4fb2-ba6c-f5027123d34a/COVID-19%20Nursing%20Home%20Data%20Feb%2004%202024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/44d194e8-7c20-43e7-b0a4-1f03c5ce386f",
-                    "title": "COVID-19 Nursing Home Data : 2024-02-04",
                     "modified": "2024-02-15",
-                    "temporal": "2024-01-28/2024-02-03"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/44d194e8-7c20-43e7-b0a4-1f03c5ce386f",
+                    "temporal": "2024-01-28/2024-02-03",
+                    "title": "COVID-19 Nursing Home Data : 2024-02-04"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/110b0448-749e-46c6-83fe-6ba393ed94f6/COVID-19%20Nursing%20Home%20Data%2001.28.2024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/686dbbdb-e2fe-4bb9-93ab-ccce45d7e83d",
-                    "title": "COVID-19 Nursing Home Data : 2024-01-28",
                     "modified": "2024-02-08",
-                    "temporal": "2024-01-21/2024-01-27"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/686dbbdb-e2fe-4bb9-93ab-ccce45d7e83d",
+                    "temporal": "2024-01-21/2024-01-27",
+                    "title": "COVID-19 Nursing Home Data : 2024-01-28"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/820a7347-3c67-438a-9047-2546f154f29e/COVID-19%20Nursing%20Home%20Data%2001.21.2024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ebba178b-f0bc-4879-953f-a065db3743f5",
-                    "title": "COVID-19 Nursing Home Data : 2024-01-21",
                     "modified": "2024-02-01",
-                    "temporal": "2024-01-14/2024-01-20"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ebba178b-f0bc-4879-953f-a065db3743f5",
+                    "temporal": "2024-01-14/2024-01-20",
+                    "title": "COVID-19 Nursing Home Data : 2024-01-21"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/a375be1d-f2d0-456b-98b8-e5ec22577126/COVID-19%20Nursing%20Home%20Data%2001.14.2024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4d8a0ce7-b51d-42a1-a1f3-2163d9a56c37",
-                    "title": "COVID-19 Nursing Home Data : 2024-01-14",
                     "modified": "2024-01-25",
-                    "temporal": "2024-01-07/2024-01-13"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4d8a0ce7-b51d-42a1-a1f3-2163d9a56c37",
+                    "temporal": "2024-01-07/2024-01-13",
+                    "title": "COVID-19 Nursing Home Data : 2024-01-14"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/3e57bc94-4843-401f-bc09-0a78ae398428/COVID-19%20Nursing%20Home%20Data%2001.07.2024.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a4574968-01b5-48db-a7a8-13976feb09c7",
-                    "title": "COVID-19 Nursing Home Data : 2024-01-07",
                     "modified": "2024-01-18",
-                    "temporal": "2023-12-31/2024-01-06"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a4574968-01b5-48db-a7a8-13976feb09c7",
+                    "temporal": "2023-12-31/2024-01-06",
+                    "title": "COVID-19 Nursing Home Data : 2024-01-07"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/1dbd460e-2970-48bb-8c0c-fa52eeec0449/COVID-19%20Nursing%20Home%20Data%2012.31.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/be3ad676-5c4e-4b69-9b8c-00409455890e",
-                    "title": "COVID-19 Nursing Home Data : 2023-12-31",
                     "modified": "2024-01-11",
-                    "temporal": "2023-12-24/2023-12-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/be3ad676-5c4e-4b69-9b8c-00409455890e",
+                    "temporal": "2023-12-24/2023-12-30",
+                    "title": "COVID-19 Nursing Home Data : 2023-12-31"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/92dffa14-cc43-4226-949b-a880e4e251d4/COVID-19%20Nursing%20Home%20Data%2012.24.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8cc25146-7d89-446a-b604-f5fe008193b7",
-                    "title": "COVID-19 Nursing Home Data : 2023-12-24",
                     "modified": "2024-01-04",
-                    "temporal": "2023-12-17/2023-12-23"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8cc25146-7d89-446a-b604-f5fe008193b7",
+                    "temporal": "2023-12-17/2023-12-23",
+                    "title": "COVID-19 Nursing Home Data : 2023-12-24"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/bb22ca87-4928-4faa-bfa1-012d4b1347de/COVID-19%20Nursing%20Home%20Data%2012.10.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/07297ed1-94cb-47bb-989c-87f8183d70d6",
-                    "title": "COVID-19 Nursing Home Data : 2023-12-10",
                     "modified": "2023-12-21",
-                    "temporal": "2023-12-03/2023-12-09"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/07297ed1-94cb-47bb-989c-87f8183d70d6",
+                    "temporal": "2023-12-03/2023-12-09",
+                    "title": "COVID-19 Nursing Home Data : 2023-12-10"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/fef02581-13a1-4a86-905d-23079c268e09/COVID-19%20Nursing%20Home%20Data%2012.03.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/68551253-9c22-4b73-a335-c08d72b6707b",
-                    "title": "COVID-19 Nursing Home Data : 2023-12-03",
                     "modified": "2023-12-14",
-                    "temporal": "2023-11-26/2023-12-02"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/68551253-9c22-4b73-a335-c08d72b6707b",
+                    "temporal": "2023-11-26/2023-12-02",
+                    "title": "COVID-19 Nursing Home Data : 2023-12-03"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/794194cf-f6fb-4497-ae75-24cc3734a9b1/COVID-19%20Nursing%20Home%20Data%2011.26.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d05f42ea-13fb-45ed-81c7-4809541c8344",
-                    "title": "COVID-19 Nursing Home Data : 2023-11-26",
                     "modified": "2023-12-07",
-                    "temporal": "2023-11-19/2023-11-25"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d05f42ea-13fb-45ed-81c7-4809541c8344",
+                    "temporal": "2023-11-19/2023-11-25",
+                    "title": "COVID-19 Nursing Home Data : 2023-11-26"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/7cdc36ca-9996-45d4-addd-f3d510493aee/COVID-19%20Nursing%20Home%20Data%2011.19.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/be2f98ce-6ea6-4cab-ba13-8fd55fc4b54e",
-                    "title": "COVID-19 Nursing Home Data : 2023-11-19",
                     "modified": "2023-11-30",
-                    "temporal": "2023-11-12/2023-11-18"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/be2f98ce-6ea6-4cab-ba13-8fd55fc4b54e",
+                    "temporal": "2023-11-12/2023-11-18",
+                    "title": "COVID-19 Nursing Home Data : 2023-11-19"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/0d067c55-51f0-40b6-9c89-34396aa331e7/COVID-19%20Nursing%20Home%20Data%2011.05.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5ce5cd10-bbfb-4c77-93b3-dd3214825f4d",
-                    "title": "COVID-19 Nursing Home Data : 2023-11-05",
                     "modified": "2023-11-16",
-                    "temporal": "2023-10-29/2023-11-04"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5ce5cd10-bbfb-4c77-93b3-dd3214825f4d",
+                    "temporal": "2023-10-29/2023-11-04",
+                    "title": "COVID-19 Nursing Home Data : 2023-11-05"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/98ed3da9-925d-4116-9a1e-93898fa58509/COVID-19%20Nursing%20Home%20Data%2010.29.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a31998bc-e14f-4f8e-a36d-50fdf9b958df",
-                    "title": "COVID-19 Nursing Home Data : 2023-10-29",
                     "modified": "2023-11-16",
-                    "temporal": "2023-10-22/2023-10-28"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a31998bc-e14f-4f8e-a36d-50fdf9b958df",
+                    "temporal": "2023-10-22/2023-10-28",
+                    "title": "COVID-19 Nursing Home Data : 2023-10-29"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/f5a73e32-7f9c-4936-aa68-a7498b30d452/COVID-19%20Nursing%20Home%20Data%2010.22.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/91f1c0eb-2125-44de-9463-95b714959cb0",
-                    "title": "COVID-19 Nursing Home Data : 2023-10-22",
                     "modified": "2023-11-02",
-                    "temporal": "2023-10-15/2023-10-21"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/91f1c0eb-2125-44de-9463-95b714959cb0",
+                    "temporal": "2023-10-15/2023-10-21",
+                    "title": "COVID-19 Nursing Home Data : 2023-10-22"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/e15b5b6d-3d6a-4ba4-bd88-870b9e89f512/COVID-19%20Nursing%20Home%20Data%2010.15.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/90bccec7-5d68-4471-bbe7-60ec751a263a",
-                    "title": "COVID-19 Nursing Home Data : 2023-10-15",
                     "modified": "2023-11-02",
-                    "temporal": "2023-10-08/2023-10-14"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/90bccec7-5d68-4471-bbe7-60ec751a263a",
+                    "temporal": "2023-10-08/2023-10-14",
+                    "title": "COVID-19 Nursing Home Data : 2023-10-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/7f2aa034-bb83-418b-8a30-c26100fd5ada/COVID-19%20Nursing%20Home%20Data%2010.08.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e6f76844-ce6d-4f72-b466-d97aaf04c397",
-                    "title": "COVID-19 Nursing Home Data : 2023-10-08",
                     "modified": "2023-10-19",
-                    "temporal": "2023-10-01/2023-10-07"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e6f76844-ce6d-4f72-b466-d97aaf04c397",
+                    "temporal": "2023-10-01/2023-10-07",
+                    "title": "COVID-19 Nursing Home Data : 2023-10-08"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/ac1993ee-3e46-4b76-afcd-dff972d97258/COVID-19%20Nursing%20Home%20Data%2010.01.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fe10a4ed-3941-4522-80be-187117d9894f",
-                    "title": "COVID-19 Nursing Home Data : 2023-10-01",
                     "modified": "2023-10-12",
-                    "temporal": "2023-09-24/2023-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fe10a4ed-3941-4522-80be-187117d9894f",
+                    "temporal": "2023-09-24/2023-09-30",
+                    "title": "COVID-19 Nursing Home Data : 2023-10-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/1573c3b1-4f0f-4996-b8bd-06744f000d0f/COVID-19%20Nursing%20Home%20Data%2009.24.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/513cfdd2-8273-4206-a94b-463328f77e8c",
-                    "title": "COVID-19 Nursing Home Data : 2023-09-24",
                     "modified": "2023-10-05",
-                    "temporal": "2023-09-17/2023-09-23"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/513cfdd2-8273-4206-a94b-463328f77e8c",
+                    "temporal": "2023-09-17/2023-09-23",
+                    "title": "COVID-19 Nursing Home Data : 2023-09-24"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/56b153a6-e5d8-4cf3-807d-afd0f4b0254b/COVID-19%20Nursing%20Home%20Data%2009.17.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a80312d1-88d3-44a2-9e75-189884d54582",
-                    "title": "COVID-19 Nursing Home Data : 2023-09-17",
                     "modified": "2023-10-06",
-                    "temporal": "2023-09-10/2023-09-16"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a80312d1-88d3-44a2-9e75-189884d54582",
+                    "temporal": "2023-09-10/2023-09-16",
+                    "title": "COVID-19 Nursing Home Data : 2023-09-17"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/988e5ac5-d7de-4cd2-bf50-f2ad20538f19/COVID-19%20Nursing%20Home%20Data%2009.10.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bf2b28b8-d2b2-4d2f-ba0b-a4a62ea124d9",
-                    "title": "COVID-19 Nursing Home Data : 2023-09-10",
                     "modified": "2023-09-21",
-                    "temporal": "2023-09-03/2023-09-09"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bf2b28b8-d2b2-4d2f-ba0b-a4a62ea124d9",
+                    "temporal": "2023-09-03/2023-09-09",
+                    "title": "COVID-19 Nursing Home Data : 2023-09-10"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/e9a520b8-d7b0-43dc-9123-0830801db8aa/COVID-19%20Nursing%20Home%20Data%2009.03.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/38982bda-0693-453d-883c-7b7b07f3660d",
-                    "title": "COVID-19 Nursing Home Data : 2023-09-03",
                     "modified": "2023-09-21",
-                    "temporal": "2023-08-27/2023-09-02"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/38982bda-0693-453d-883c-7b7b07f3660d",
+                    "temporal": "2023-08-27/2023-09-02",
+                    "title": "COVID-19 Nursing Home Data : 2023-09-03"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/d0fcffb7-62f1-49c7-850b-2b6ba46b12f3/COVID-19%20Nursing%20Home%20Data%2008.27.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bb26981f-442e-4071-a8ac-ed1b1335b920",
-                    "title": "COVID-19 Nursing Home Data : 2023-08-27",
                     "modified": "2023-09-14",
-                    "temporal": "2023-08-20/2023-08-26"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bb26981f-442e-4071-a8ac-ed1b1335b920",
+                    "temporal": "2023-08-20/2023-08-26",
+                    "title": "COVID-19 Nursing Home Data : 2023-08-27"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/2a8bcae3-85c1-4e79-a419-47f1ffcc3b03/COVID-19%20Nursing%20Home%20Data%2008.20.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/96adccd7-24d3-422d-bb71-4e659c91c723",
-                    "title": "COVID-19 Nursing Home Data : 2023-08-20",
                     "modified": "2023-09-07",
-                    "temporal": "2023-08-13/2023-08-19"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/96adccd7-24d3-422d-bb71-4e659c91c723",
+                    "temporal": "2023-08-13/2023-08-19",
+                    "title": "COVID-19 Nursing Home Data : 2023-08-20"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/95d91d5d-49bb-4ac5-9ab9-94aac2a71a1a/COVID-19%20Nursing%20Home%20Data%2008.13.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/083564c0-a781-4937-a9e5-1b4472bcf4bb",
-                    "title": "COVID-19 Nursing Home Data : 2023-08-13",
                     "modified": "2023-09-01",
-                    "temporal": "2023-08-06/2023-08-12"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/083564c0-a781-4937-a9e5-1b4472bcf4bb",
+                    "temporal": "2023-08-06/2023-08-12",
+                    "title": "COVID-19 Nursing Home Data : 2023-08-13"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/695cd404-5cee-4d4e-a2ee-66e3682b62d5/COVID-19%20Nursing%20Home%20Data%2008.06.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/84e99b2f-e2b5-4986-9bfb-c225fde9a222",
-                    "title": "COVID-19 Nursing Home Data : 2023-08-06",
                     "modified": "2023-09-01",
-                    "temporal": "2023-07-30/2023-08-05"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/84e99b2f-e2b5-4986-9bfb-c225fde9a222",
+                    "temporal": "2023-07-30/2023-08-05",
+                    "title": "COVID-19 Nursing Home Data : 2023-08-06"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/8dbe45a5-8bd5-47b9-b093-14c9ff702cd9/COVID-19%20Nursing%20Home%20Data%2007.30.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e3d64413-9d6a-40d2-9416-15b93e4d0d9d",
-                    "title": "COVID-19 Nursing Home Data : 2023-07-30",
                     "modified": "2023-08-17",
-                    "temporal": "2023-07-23/2023-07-29"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e3d64413-9d6a-40d2-9416-15b93e4d0d9d",
+                    "temporal": "2023-07-23/2023-07-29",
+                    "title": "COVID-19 Nursing Home Data : 2023-07-30"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/b4df5430-8b70-4ec3-ac8e-498eae6dd14b/COVID-19%20Nursing%20Home%20Data%2007.23.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/eaccd5c5-9876-4e52-8596-4dda2435cb94",
-                    "title": "COVID-19 Nursing Home Data : 2023-07-23",
                     "modified": "2023-08-10",
-                    "temporal": "2023-07-16/2023-07-22"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/eaccd5c5-9876-4e52-8596-4dda2435cb94",
+                    "temporal": "2023-07-16/2023-07-22",
+                    "title": "COVID-19 Nursing Home Data : 2023-07-23"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/75d592c9-27b2-45bb-8350-0d4b3e131b77/COVID-19%20Nursing%20Home%20Data%2007.16.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/46a9119f-08b0-43a6-ad97-7c0cdcf12296",
-                    "title": "COVID-19 Nursing Home Data : 2023-07-16",
                     "modified": "2023-08-03",
-                    "temporal": "2023-07-09/2023-07-15"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/46a9119f-08b0-43a6-ad97-7c0cdcf12296",
+                    "temporal": "2023-07-09/2023-07-15",
+                    "title": "COVID-19 Nursing Home Data : 2023-07-16"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/079854a1-30b2-442f-a48f-692088128a41/COVID-19%20Nursing%20Home%20Data%2007.09.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1fb25c1c-cbf9-4572-8e8f-f4830cd64428",
-                    "title": "COVID-19 Nursing Home Data : 2023-07-09",
                     "modified": "2023-07-28",
-                    "temporal": "2023-07-02/2023-07-08"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1fb25c1c-cbf9-4572-8e8f-f4830cd64428",
+                    "temporal": "2023-07-02/2023-07-08",
+                    "title": "COVID-19 Nursing Home Data : 2023-07-09"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/29fadea6-2ef1-4c27-90e1-54946b990ecb/COVID-19%20Nursing%20Home%20Data%2007.02.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4200ba52-2440-43cb-91c4-bad4325c4460",
-                    "title": "COVID-19 Nursing Home Data : 2023-07-02",
                     "modified": "2023-07-13",
-                    "temporal": "2023-06-25/2023-07-01"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4200ba52-2440-43cb-91c4-bad4325c4460",
+                    "temporal": "2023-06-25/2023-07-01",
+                    "title": "COVID-19 Nursing Home Data : 2023-07-02"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/ad9ac043-c5d5-4368-a55f-dbd8bae7a9cb/COVID-19%20Nursing%20Home%20Data%2006.25.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2536f9c0-c34d-4a31-b621-2fed2f74f718",
-                    "title": "COVID-19 Nursing Home Data : 2023-06-25",
                     "modified": "2023-07-13",
-                    "temporal": "2023-06-18/2023-06-24"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2536f9c0-c34d-4a31-b621-2fed2f74f718",
+                    "temporal": "2023-06-18/2023-06-24",
+                    "title": "COVID-19 Nursing Home Data : 2023-06-25"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/207e597d-642b-42c6-860e-6802efcd84a8/COVID-19%20Nursing%20Home%20Data%2006.18.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9616e8a3-1a1d-4951-a9cd-7a52566343f7",
-                    "title": "COVID-19 Nursing Home Data : 2023-06-18",
                     "modified": "2023-06-29",
-                    "temporal": "2023-06-11/2023-06-17"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9616e8a3-1a1d-4951-a9cd-7a52566343f7",
+                    "temporal": "2023-06-11/2023-06-17",
+                    "title": "COVID-19 Nursing Home Data : 2023-06-18"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/9c688363-f4a1-417f-bf39-b313b987e9b6/COVID-19%20Nursing%20Home%20Data%2006.11.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/dc823ccd-5fb1-465e-92e0-ec05f72a831b",
-                    "title": "COVID-19 Nursing Home Data : 2023-06-11",
                     "modified": "2023-06-22",
-                    "temporal": "2023-06-04/2023-06-10"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/dc823ccd-5fb1-465e-92e0-ec05f72a831b",
+                    "temporal": "2023-06-04/2023-06-10",
+                    "title": "COVID-19 Nursing Home Data : 2023-06-11"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/2292aa7d-4144-4973-adef-f4fa1ede1489/COVID-19%20Nursing%20Home%20Data%2006.04.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f7460aa3-cabf-4070-963b-16ab500dd5c1",
-                    "title": "COVID-19 Nursing Home Data : 2023-06-04",
                     "modified": "2023-06-15",
-                    "temporal": "2023-05-28/2023-06-03"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f7460aa3-cabf-4070-963b-16ab500dd5c1",
+                    "temporal": "2023-05-28/2023-06-03",
+                    "title": "COVID-19 Nursing Home Data : 2023-06-04"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/2e3fa382-0a20-4813-a003-072fbbabcb96/COVID-19%20Nursing%20Home%20Data%2005.28.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2a426cae-5d9b-4a11-999c-4d00e8ab8e71",
-                    "title": "COVID-19 Nursing Home Data : 2023-05-28",
                     "modified": "2023-06-08",
-                    "temporal": "2023-05-21/2023-05-27"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2a426cae-5d9b-4a11-999c-4d00e8ab8e71",
+                    "temporal": "2023-05-21/2023-05-27",
+                    "title": "COVID-19 Nursing Home Data : 2023-05-28"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/46bf1e06-fe62-4b10-8a23-b17caae079a7/COVID-19%20Nursing%20Home%20Data%2005.21.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fa341c0c-627d-4bc0-8cd4-12193ddd51e3",
-                    "title": "COVID-19 Nursing Home Data : 2023-05-21",
                     "modified": "2023-06-08",
-                    "temporal": "2023-05-14/2023-05-20"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fa341c0c-627d-4bc0-8cd4-12193ddd51e3",
+                    "temporal": "2023-05-14/2023-05-20",
+                    "title": "COVID-19 Nursing Home Data : 2023-05-21"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/26228c7e-d1cd-4b25-9100-e6ac97e530ed/COVID-19%20Nursing%20Home%20Data%2005.14.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/28f52c9d-698a-47ef-bd03-3e750643939f",
-                    "title": "COVID-19 Nursing Home Data : 2023-05-14",
                     "modified": "2023-06-01",
-                    "temporal": "2023-05-07/2023-05-13"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/28f52c9d-698a-47ef-bd03-3e750643939f",
+                    "temporal": "2023-05-07/2023-05-13",
+                    "title": "COVID-19 Nursing Home Data : 2023-05-14"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/8e75cb19-15ea-42c7-9add-50506f4c6a5f/COVID-19%20Nursing%20Home%20Data%2005.07.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/02eeba3f-a687-4133-8f32-0669881508fc",
-                    "title": "COVID-19 Nursing Home Data : 2023-05-07",
                     "modified": "2023-05-18",
-                    "temporal": "2023-04-30/2023-05-06"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/02eeba3f-a687-4133-8f32-0669881508fc",
+                    "temporal": "2023-04-30/2023-05-06",
+                    "title": "COVID-19 Nursing Home Data : 2023-05-07"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/daf87409-03f5-4bef-b072-5ef2f46da895/COVID-19%20Nursing%20Home%20Data%2004.30.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f82b4fd6-5471-404c-97cb-088a95df8fca",
-                    "title": "COVID-19 Nursing Home Data : 2023-04-30",
                     "modified": "2023-05-11",
-                    "temporal": "2023-04-23/2023-04-29"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f82b4fd6-5471-404c-97cb-088a95df8fca",
+                    "temporal": "2023-04-23/2023-04-29",
+                    "title": "COVID-19 Nursing Home Data : 2023-04-30"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/17fdc765-6e27-4d5e-a882-af4768611435/COVID-19%20Nursing%20Home%20Data%2004.23.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/62b98bfb-6020-4b4d-a041-4bbac8eaf074",
-                    "title": "COVID-19 Nursing Home Data : 2023-04-23",
                     "modified": "2023-05-04",
-                    "temporal": "2023-04-16/2023-04-22"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/62b98bfb-6020-4b4d-a041-4bbac8eaf074",
+                    "temporal": "2023-04-16/2023-04-22",
+                    "title": "COVID-19 Nursing Home Data : 2023-04-23"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/e3cd9d79-e425-4dca-bb43-11df69741a9d/COVID-19%20Nursing%20Home%20Data%2004.16.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/85439fc5-21c9-49bf-a455-215837b62fd7",
-                    "title": "COVID-19 Nursing Home Data : 2023-04-16",
                     "modified": "2023-05-04",
-                    "temporal": "2023-04-09/2023-04-15"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/85439fc5-21c9-49bf-a455-215837b62fd7",
+                    "temporal": "2023-04-09/2023-04-15",
+                    "title": "COVID-19 Nursing Home Data : 2023-04-16"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/452dc811-5f3c-41dd-b1d2-bfd08b464118/COVID-19%20Nursing%20Home%20Data%2004.09.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9e4ba5fb-3cb4-46fd-8bec-a71aa1d74e6b",
-                    "title": "COVID-19 Nursing Home Data : 2023-04-09",
                     "modified": "2023-04-20",
-                    "temporal": "2023-04-02/2023-04-08"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9e4ba5fb-3cb4-46fd-8bec-a71aa1d74e6b",
+                    "temporal": "2023-04-02/2023-04-08",
+                    "title": "COVID-19 Nursing Home Data : 2023-04-09"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/e9c5d641-5c6e-42ac-b9bc-a8d4f83c46d7/COVID-19%20Nursing%20Home%20Data%2004.02.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d981886c-21a5-41ce-a78e-f5467393e4b4",
-                    "title": "COVID-19 Nursing Home Data : 2023-04-02",
                     "modified": "2023-04-13",
-                    "temporal": "2023-03-26/2023-04-01"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d981886c-21a5-41ce-a78e-f5467393e4b4",
+                    "temporal": "2023-03-26/2023-04-01",
+                    "title": "COVID-19 Nursing Home Data : 2023-04-02"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/2291de78-377a-45d2-b44e-d01f0c65bc52/COVID-19%20Nursing%20Home%20Data%2003.26.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2330e21c-82bb-481e-8ca0-53476fccfba4",
-                    "title": "COVID-19 Nursing Home Data : 2023-03-26",
                     "modified": "2023-04-06",
-                    "temporal": "2023-03-19/2023-03-25"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2330e21c-82bb-481e-8ca0-53476fccfba4",
+                    "temporal": "2023-03-19/2023-03-25",
+                    "title": "COVID-19 Nursing Home Data : 2023-03-26"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/16ec8e45-cb69-4976-aafd-300c81deac01/COVID-19%20Nursing%20Home%20Data%2003.19.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b68dd626-5683-4833-8357-bf6fd230f983",
-                    "title": "COVID-19 Nursing Home Data : 2023-03-19",
                     "modified": "2023-03-30",
-                    "temporal": "2023-03-12/2023-03-18"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b68dd626-5683-4833-8357-bf6fd230f983",
+                    "temporal": "2023-03-12/2023-03-18",
+                    "title": "COVID-19 Nursing Home Data : 2023-03-19"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-03/54ad1acb-21aa-46c5-bcfc-2272d3fc04a0/COVID-19%20Nursing%20Home%20Data%2003.12.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2692cde5-d0b7-4d32-bcb9-38afdf0d1020",
-                    "title": "COVID-19 Nursing Home Data : 2023-03-12",
                     "modified": "2023-03-30",
-                    "temporal": "2023-03-05/2023-03-11"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2692cde5-d0b7-4d32-bcb9-38afdf0d1020",
+                    "temporal": "2023-03-05/2023-03-11",
+                    "title": "COVID-19 Nursing Home Data : 2023-03-12"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-03/04017444-1483-4d1d-b368-2eedaf8e2ec9/COVID-19%20Nursing%20Home%20Data%2003.05.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1978972a-804f-4b81-9c4b-8db4bd79683e",
-                    "title": "COVID-19 Nursing Home Data : 2023-03-05",
                     "modified": "2023-03-16",
-                    "temporal": "2023-02-26/2023-03-04"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1978972a-804f-4b81-9c4b-8db4bd79683e",
+                    "temporal": "2023-02-26/2023-03-04",
+                    "title": "COVID-19 Nursing Home Data : 2023-03-05"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-03/9981a877-f52a-48e6-a09a-5368f9b9a12b/COVID-19%20Nursing%20Home%20Data%2002.26.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/89163e1e-827d-4da2-be8b-d9a60dfe4605",
-                    "title": "COVID-19 Nursing Home Data : 2023-02-26",
                     "modified": "2023-03-09",
-                    "temporal": "2023-02-19/2023-02-25"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/89163e1e-827d-4da2-be8b-d9a60dfe4605",
+                    "temporal": "2023-02-19/2023-02-25",
+                    "title": "COVID-19 Nursing Home Data : 2023-02-26"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-03/599d5470-f000-4102-9dc6-240a352c9b36/COVID-19%20Nursing%20Home%20Data%2002.19.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/79341f5a-3287-4119-ba6e-59122698b0bf",
-                    "title": "COVID-19 Nursing Home Data : 2023-02-19",
                     "modified": "2023-03-09",
-                    "temporal": "2023-02-12/2023-02-18"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/79341f5a-3287-4119-ba6e-59122698b0bf",
+                    "temporal": "2023-02-12/2023-02-18",
+                    "title": "COVID-19 Nursing Home Data : 2023-02-19"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-03/7b347b3f-064d-4525-90d1-e487f9eace13/COVID-19%20Nursing%20Home%20Data%2002.12.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fed999e5-b8b6-4d41-b6c1-f90349416558",
-                    "title": "COVID-19 Nursing Home Data : 2023-02-12",
                     "modified": "2023-03-06",
-                    "temporal": "2023-02-05/2023-02-11"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fed999e5-b8b6-4d41-b6c1-f90349416558",
+                    "temporal": "2023-02-05/2023-02-11",
+                    "title": "COVID-19 Nursing Home Data : 2023-02-12"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-02/1d1f839d-1b56-468a-8994-312761e76038/COVID-19%20Nursing%20Home%20Data%2002.05.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/10f7c1b6-af7a-4896-bb67-75fd055a74d8",
-                    "title": "COVID-19 Nursing Home Data : 2023-02-05",
                     "modified": "2023-03-06",
-                    "temporal": "2023-01-29/2023-02-04"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/10f7c1b6-af7a-4896-bb67-75fd055a74d8",
+                    "temporal": "2023-01-29/2023-02-04",
+                    "title": "COVID-19 Nursing Home Data : 2023-02-05"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-02/412f5937-c036-436b-9623-9d7183cb7ba5/COVID-19%20Nursing%20Home%20Data%2001.29.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/45be6750-b059-47b7-841d-f7de912740a0",
-                    "title": "COVID-19 Nursing Home Data : 2023-01-29",
                     "modified": "2023-03-06",
-                    "temporal": "2023-01-22/2023-01-28"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/45be6750-b059-47b7-841d-f7de912740a0",
+                    "temporal": "2023-01-22/2023-01-28",
+                    "title": "COVID-19 Nursing Home Data : 2023-01-29"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-02/4afc3c44-b8e1-48a4-ad7b-4190a9f01763/COVID-19%20Nursing%20Home%20Data%2001.22.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d118a339-a8f9-48aa-b64b-273f30af8bd9",
-                    "title": "COVID-19 Nursing Home Data : 2023-01-22",
                     "modified": "2023-03-06",
-                    "temporal": "2023-01-15/2023-01-21"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d118a339-a8f9-48aa-b64b-273f30af8bd9",
+                    "temporal": "2023-01-15/2023-01-21",
+                    "title": "COVID-19 Nursing Home Data : 2023-01-22"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-02/e2590f61-e62d-4111-a9a5-d51c08227598/COVID-19%20Nursing%20Home%20Data%2001.15.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4817517d-126f-4955-8af0-04be76f453e2",
-                    "title": "COVID-19 Nursing Home Data : 2023-01-15",
                     "modified": "2023-03-06",
-                    "temporal": "2023-01-08/2023-01-14"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4817517d-126f-4955-8af0-04be76f453e2",
+                    "temporal": "2023-01-08/2023-01-14",
+                    "title": "COVID-19 Nursing Home Data : 2023-01-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-01/24541725-693b-4f19-8b59-df273ff8e7df/COVID-19%20Nursing%20Home%20Data%2001.08.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/15dcc9c5-2a29-4792-a6bc-3591dec9f22f",
-                    "title": "COVID-19 Nursing Home Data : 2023-01-08",
                     "modified": "2023-03-06",
-                    "temporal": "2023-01-01/2023-01-07"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/15dcc9c5-2a29-4792-a6bc-3591dec9f22f",
+                    "temporal": "2023-01-01/2023-01-07",
+                    "title": "COVID-19 Nursing Home Data : 2023-01-08"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-01/872b4cf3-46db-4b77-9c87-4283210ec8c2/COVID-19%20Nursing%20Home%20Data%2001.01.2023.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a9e94001-fa39-47d5-9ad7-c615e5399756",
-                    "title": "COVID-19 Nursing Home Data : 2023-01-01",
                     "modified": "2023-03-06",
-                    "temporal": "2022-12-25/2022-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a9e94001-fa39-47d5-9ad7-c615e5399756",
+                    "temporal": "2022-12-25/2022-12-31",
+                    "title": "COVID-19 Nursing Home Data : 2023-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-01/6eeb4d5d-df8d-4a8d-93ea-fdb3dcfa73c6/COVID-19%20Nursing%20Home%20Data%2012.18.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/54df2d9a-ec01-4bed-a52a-ff9a2fc825da",
-                    "title": "COVID-19 Nursing Home Data : 2022-12-18",
                     "modified": "2023-03-06",
-                    "temporal": "2022-12-11/2022-12-17"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/54df2d9a-ec01-4bed-a52a-ff9a2fc825da",
+                    "temporal": "2022-12-11/2022-12-17",
+                    "title": "COVID-19 Nursing Home Data : 2022-12-18"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-12/dd1c56d7-a45c-4419-8bc2-bc5656b5cd8e/COVID-19%20Nursing%20Home%20Data%2012.11.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e07d377d-d31b-49da-a654-0eeaf76f558c",
-                    "title": "COVID-19 Nursing Home Data : 2022-12-11",
                     "modified": "2023-03-06",
-                    "temporal": "2022-12-04/2022-12-10"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e07d377d-d31b-49da-a654-0eeaf76f558c",
+                    "temporal": "2022-12-04/2022-12-10",
+                    "title": "COVID-19 Nursing Home Data : 2022-12-11"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-12/77f66cb5-2fd6-449c-af94-10aaf835eeb5/COVID-19%20Nursing%20Home%20Data%2012.04.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a3371812-a39f-4804-8105-7fc4bc19d57f",
-                    "title": "COVID-19 Nursing Home Data : 2022-12-04",
                     "modified": "2023-03-06",
-                    "temporal": "2022-11-27/2022-12-03"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a3371812-a39f-4804-8105-7fc4bc19d57f",
+                    "temporal": "2022-11-27/2022-12-03",
+                    "title": "COVID-19 Nursing Home Data : 2022-12-04"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-12/46a6d41a-efec-41f1-a79e-4497a249c530/COVID-19%20Nursing%20Home%20Data%2011.27.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e5bf0ec8-9e47-4175-8b83-cfe526b9c0bb",
-                    "title": "COVID-19 Nursing Home Data : 2022-11-27",
                     "modified": "2023-03-06",
-                    "temporal": "2022-11-20/2022-11-26"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e5bf0ec8-9e47-4175-8b83-cfe526b9c0bb",
+                    "temporal": "2022-11-20/2022-11-26",
+                    "title": "COVID-19 Nursing Home Data : 2022-11-27"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-12/9c2bafc0-b5a8-4087-9d2d-1e7c2833c1a3/COVID-19%20Nursing%20Home%20Data%2011.20.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b4aea53c-a3c3-4aa5-861e-e3985323644a",
-                    "title": "COVID-19 Nursing Home Data : 2022-11-20",
                     "modified": "2023-03-06",
-                    "temporal": "2022-11-13/2022-11-19"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b4aea53c-a3c3-4aa5-861e-e3985323644a",
+                    "temporal": "2022-11-13/2022-11-19",
+                    "title": "COVID-19 Nursing Home Data : 2022-11-20"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-12/73bacb6e-dd3d-4291-91e0-011131803dc3/COVID-19%20Nursing%20Home%20Data%2011.13.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7bc7c201-3845-434c-a5a4-d9d017f1b22c",
-                    "title": "COVID-19 Nursing Home Data : 2022-11-13",
                     "modified": "2023-03-06",
-                    "temporal": "2022-11-06/2022-11-12"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7bc7c201-3845-434c-a5a4-d9d017f1b22c",
+                    "temporal": "2022-11-06/2022-11-12",
+                    "title": "COVID-19 Nursing Home Data : 2022-11-13"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-11/d35843b9-766d-4a0a-ac27-e408efa20909/COVID-19%20Nursing%20Home%20Data%2011.06.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c4692d15-c65d-450f-8988-aaf1f2a7a69c",
-                    "title": "COVID-19 Nursing Home Data : 2022-11-06",
                     "modified": "2023-03-06",
-                    "temporal": "2022-10-30/2022-11-05"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c4692d15-c65d-450f-8988-aaf1f2a7a69c",
+                    "temporal": "2022-10-30/2022-11-05",
+                    "title": "COVID-19 Nursing Home Data : 2022-11-06"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-11/f44e3057-6a31-4740-98d7-d68eb815963f/COVID-19%20Nursing%20Home%20Data%2010.30.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3c78dd12-38e4-40da-8b93-fb1d0b70bd29",
-                    "title": "COVID-19 Nursing Home Data : 2022-10-30",
                     "modified": "2023-03-06",
-                    "temporal": "2022-10-23/2022-10-29"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3c78dd12-38e4-40da-8b93-fb1d0b70bd29",
+                    "temporal": "2022-10-23/2022-10-29",
+                    "title": "COVID-19 Nursing Home Data : 2022-10-30"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-11/1ab3a60f-60b2-4ebc-8e4f-0efc2ea8679e/COVID-19%20Nursing%20Home%20Data%2010.23.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ea16e000-86be-4677-9ca6-daa87b25ad47",
-                    "title": "COVID-19 Nursing Home Data : 2022-10-23",
                     "modified": "2023-03-06",
-                    "temporal": "2022-10-16/2022-10-22"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ea16e000-86be-4677-9ca6-daa87b25ad47",
+                    "temporal": "2022-10-16/2022-10-22",
+                    "title": "COVID-19 Nursing Home Data : 2022-10-23"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-11/eb951670-6cba-4738-afea-a534cbdfd022/COVID-19%20Nursing%20Home%20Data%2010.16.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c2460fab-a7ef-4a8b-8853-53f87325a31a",
-                    "title": "COVID-19 Nursing Home Data : 2022-10-16",
                     "modified": "2022-10-27",
-                    "temporal": "2022-10-09/2022-10-15"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c2460fab-a7ef-4a8b-8853-53f87325a31a",
+                    "temporal": "2022-10-09/2022-10-15",
+                    "title": "COVID-19 Nursing Home Data : 2022-10-16"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-10/9c487b05-42df-460e-8093-a7d15913abfa/COVID-19%20Nursing%20Home%20Data%2010.09.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7fbd914e-7242-4b01-82aa-f8213e35047a",
-                    "title": "COVID-19 Nursing Home Data : 2022-10-09",
                     "modified": "2022-10-27",
-                    "temporal": "2022-10-02/2022-10-08"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7fbd914e-7242-4b01-82aa-f8213e35047a",
+                    "temporal": "2022-10-02/2022-10-08",
+                    "title": "COVID-19 Nursing Home Data : 2022-10-09"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-10/5f8cffb5-369b-48a6-b1dc-8a62eb333b39/COVID-19%20Nursing%20Home%20Data%2010.02.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2212e462-2dee-45ed-8417-d0442192142a",
-                    "title": "COVID-19 Nursing Home Data : 2022-10-02",
                     "modified": "2022-10-13",
-                    "temporal": "2022-09-25/2022-10-01"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2212e462-2dee-45ed-8417-d0442192142a",
+                    "temporal": "2022-09-25/2022-10-01",
+                    "title": "COVID-19 Nursing Home Data : 2022-10-02"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-10/952673d0-d13c-466b-8a50-37bd7e93054f/COVID-19%20Nursing%20Home%20Data%2009.25.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/128d9a55-49d9-4be7-b33b-ce236bebdeca",
-                    "title": "COVID-19 Nursing Home Data : 2022-09-25",
                     "modified": "2022-10-06",
-                    "temporal": "2022-09-18/2022-09-24"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/128d9a55-49d9-4be7-b33b-ce236bebdeca",
+                    "temporal": "2022-09-18/2022-09-24",
+                    "title": "COVID-19 Nursing Home Data : 2022-09-25"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-10/b555e632-2c6b-4808-b5ef-3e2b803e5164/COVID-19%20Nursing%20Home%20Data%2009.18.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2d175df7-21de-446e-91cc-79e22a0d883d",
-                    "title": "COVID-19 Nursing Home Data : 2022-09-18",
                     "modified": "2022-09-29",
-                    "temporal": "2022-09-11/2022-09-17"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2d175df7-21de-446e-91cc-79e22a0d883d",
+                    "temporal": "2022-09-11/2022-09-17",
+                    "title": "COVID-19 Nursing Home Data : 2022-09-18"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-09/df439fa4-8fe2-4724-b906-bcf77c11d8b9/COVID-19%20Nursing%20Home%20Data%2009.11.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c43ae426-2d71-4dcd-9dca-4b16f0917c45",
-                    "title": "COVID-19 Nursing Home Data : 2022-09-11",
                     "modified": "2022-09-22",
-                    "temporal": "2022-09-04/2022-09-10"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c43ae426-2d71-4dcd-9dca-4b16f0917c45",
+                    "temporal": "2022-09-04/2022-09-10",
+                    "title": "COVID-19 Nursing Home Data : 2022-09-11"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-09/5bf58869-686c-40f7-b3fe-c15b3141b424/COVID-19%20Nursing%20Home%20Data%2009.04.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/70891227-7659-4472-abe7-92d03f264fc8",
-                    "title": "COVID-19 Nursing Home Data : 2022-09-04",
                     "modified": "2022-09-15",
-                    "temporal": "2022-08-28/2022-09-03"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/70891227-7659-4472-abe7-92d03f264fc8",
+                    "temporal": "2022-08-28/2022-09-03",
+                    "title": "COVID-19 Nursing Home Data : 2022-09-04"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-09/1349b7f0-dc65-4172-822c-e2c6c4b9c681/COVID-19%20Nursing%20Home%20Data%2008.28.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c9c68c7a-393b-4e1e-a2f6-2d833eb28fb3",
-                    "title": "COVID-19 Nursing Home Data : 2022-08-28",
                     "modified": "2022-09-08",
-                    "temporal": "2022-08-21/2022-08-27"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c9c68c7a-393b-4e1e-a2f6-2d833eb28fb3",
+                    "temporal": "2022-08-21/2022-08-27",
+                    "title": "COVID-19 Nursing Home Data : 2022-08-28"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-09/d7de4027-3c7d-41ae-b7a7-8e56ac929fb4/COVID-19%20Nursing%20Home%20Data%2008.21.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4a06fbca-0705-4082-abc8-c91f37653eb6",
-                    "title": "COVID-19 Nursing Home Data : 2022-08-21",
                     "modified": "2022-09-08",
-                    "temporal": "2022-08-14/2022-08-20"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4a06fbca-0705-4082-abc8-c91f37653eb6",
+                    "temporal": "2022-08-14/2022-08-20",
+                    "title": "COVID-19 Nursing Home Data : 2022-08-21"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-09/d070bc94-6fb9-4c5c-812f-069b318ee1f4/COVID-19%20Nursing%20Home%20Data%2008.14.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c8a139ee-9e31-444c-976f-bab6b287b871",
-                    "title": "COVID-19 Nursing Home Data : 2022-08-14",
                     "modified": "2022-09-01",
-                    "temporal": "2022-08-07/2022-08-13"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c8a139ee-9e31-444c-976f-bab6b287b871",
+                    "temporal": "2022-08-07/2022-08-13",
+                    "title": "COVID-19 Nursing Home Data : 2022-08-14"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-08/COVID-19%20Nursing%20Home%20Data%2008.07.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ad73e4d3-925b-4055-ad9b-7f0015e906c8",
-                    "title": "COVID-19 Nursing Home Data : 2022-08-07",
                     "modified": "2022-08-25",
-                    "temporal": "2022-07-31/2022-08-06"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ad73e4d3-925b-4055-ad9b-7f0015e906c8",
+                    "temporal": "2022-07-31/2022-08-06",
+                    "title": "COVID-19 Nursing Home Data : 2022-08-07"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-08/COVID-19%20Nursing%20Home%20Data%2007.31.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/183d9d98-7d61-4893-aa06-7c2a7bb47986",
-                    "title": "COVID-19 Nursing Home Data : 2022-07-31",
                     "modified": "2022-08-18",
-                    "temporal": "2022-07-24/2022-07-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/183d9d98-7d61-4893-aa06-7c2a7bb47986",
+                    "temporal": "2022-07-24/2022-07-30",
+                    "title": "COVID-19 Nursing Home Data : 2022-07-31"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-08/e6f2b907-df0a-47fc-8790-d281abf6fe70/COVID-19%20Nursing%20Home%20Data%2007.24.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8508ea50-7e79-4b0c-b022-266951f58cb7",
-                    "title": "COVID-19 Nursing Home Data : 2022-07-24",
                     "modified": "2022-08-11",
-                    "temporal": "2022-07-17/2022-07-23"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8508ea50-7e79-4b0c-b022-266951f58cb7",
+                    "temporal": "2022-07-17/2022-07-23",
+                    "title": "COVID-19 Nursing Home Data : 2022-07-24"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-08/COVID-19%20Nursing%20Home%20Data%2007.17.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/288588ac-d4d6-40bb-ba5b-697e7aa334bb",
-                    "title": "COVID-19 Nursing Home Data : 2022-07-17",
                     "modified": "2022-08-04",
-                    "temporal": "2022-07-10/2022-07-16"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/288588ac-d4d6-40bb-ba5b-697e7aa334bb",
+                    "temporal": "2022-07-10/2022-07-16",
+                    "title": "COVID-19 Nursing Home Data : 2022-07-17"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-07/COVID-19%20Nursing%20Home%20Data%2007.10.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5dbd3871-abbb-4131-a248-0e57a402b245",
-                    "title": "COVID-19 Nursing Home Data : 2022-07-10",
                     "modified": "2022-07-28",
-                    "temporal": "2022-07-03/2022-07-09"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5dbd3871-abbb-4131-a248-0e57a402b245",
+                    "temporal": "2022-07-03/2022-07-09",
+                    "title": "COVID-19 Nursing Home Data : 2022-07-10"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-07/384d6e58-ae9b-4381-be3a-6d116f919cfb/COVID-19%20Nursing%20Home%20Data%2007.03.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1f4545c1-bc79-4a58-b2cb-d92f1333b88c",
-                    "title": "COVID-19 Nursing Home Data : 2022-07-03",
                     "modified": "2022-07-21",
-                    "temporal": "2022-06-26/2022-07-02"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1f4545c1-bc79-4a58-b2cb-d92f1333b88c",
+                    "temporal": "2022-06-26/2022-07-02",
+                    "title": "COVID-19 Nursing Home Data : 2022-07-03"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-07/COVID-19%20Nursing%20Home%20Data%2006.26.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0768e8e9-d98f-4853-a14e-ebbd3fb36114",
-                    "title": "COVID-19 Nursing Home Data : 2022-06-26",
                     "modified": "2022-07-14",
-                    "temporal": "2022-06-19/2022-06-25"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0768e8e9-d98f-4853-a14e-ebbd3fb36114",
+                    "temporal": "2022-06-19/2022-06-25",
+                    "title": "COVID-19 Nursing Home Data : 2022-06-26"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-07/COVID-19%20Nursing%20Home%20Data%2006.19.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d22c7f45-dc9b-46a0-a3d0-6bff6c08ee72",
-                    "title": "COVID-19 Nursing Home Data : 2022-06-19",
                     "modified": "2022-07-07",
-                    "temporal": "2022-06-12/2022-06-18"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d22c7f45-dc9b-46a0-a3d0-6bff6c08ee72",
+                    "temporal": "2022-06-12/2022-06-18",
+                    "title": "COVID-19 Nursing Home Data : 2022-06-19"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-06/COVID-19%20Nursing%20Home%20Data%2006.12.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1d9b2985-18d2-4d68-88de-06b9ff64dd9c",
-                    "title": "COVID-19 Nursing Home Data : 2022-06-12",
                     "modified": "2022-06-30",
-                    "temporal": "2022-06-05/2022-06-11"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1d9b2985-18d2-4d68-88de-06b9ff64dd9c",
+                    "temporal": "2022-06-05/2022-06-11",
+                    "title": "COVID-19 Nursing Home Data : 2022-06-12"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-06/COVID-19%20Nursing%20Home%20Data%2006.05.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/78c75fc0-29c1-4b13-9ce2-159f7195a22e",
-                    "title": "COVID-19 Nursing Home Data : 2022-06-05",
                     "modified": "2022-06-23",
-                    "temporal": "2022-05-29/2022-06-04"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/78c75fc0-29c1-4b13-9ce2-159f7195a22e",
+                    "temporal": "2022-05-29/2022-06-04",
+                    "title": "COVID-19 Nursing Home Data : 2022-06-05"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-06/fdfb646a-d3c6-4995-8869-e791c7817d39/COVID-19%20Nursing%20Home%20Data%2005.29.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b4d57564-8111-4ee6-bad5-34c944f922eb",
-                    "title": "COVID-19 Nursing Home Data : 2022-05-29",
                     "modified": "2022-06-16",
-                    "temporal": "2022-05-22/2022-05-28"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b4d57564-8111-4ee6-bad5-34c944f922eb",
+                    "temporal": "2022-05-22/2022-05-28",
+                    "title": "COVID-19 Nursing Home Data : 2022-05-29"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-06/25c9a6e6-ca46-4576-810a-a27bfa0d90a0/COVID-19%20Nursing%20Home%20Data%2005.22.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2b27d7a7-db59-485c-8e12-265e967a6621",
-                    "title": "COVID-19 Nursing Home Data : 2022-05-22",
                     "modified": "2022-06-09",
-                    "temporal": "2022-05-15/2022-05-21"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2b27d7a7-db59-485c-8e12-265e967a6621",
+                    "temporal": "2022-05-15/2022-05-21",
+                    "title": "COVID-19 Nursing Home Data : 2022-05-22"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-06/COVID-19%20Nursing%20Home%20Data%2005.15.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1017829b-977d-40b4-9210-401bb6ef778a",
-                    "title": "COVID-19 Nursing Home Data : 2022-05-15",
                     "modified": "2022-06-02",
-                    "temporal": "2022-05-08/2022-05-14"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1017829b-977d-40b4-9210-401bb6ef778a",
+                    "temporal": "2022-05-08/2022-05-14",
+                    "title": "COVID-19 Nursing Home Data : 2022-05-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-05/COVID-19%20Nursing%20Home%20Data%2005.08.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c2fdab03-06c8-4125-9732-66a6706e4e94",
-                    "title": "COVID-19 Nursing Home Data : 2022-05-08",
                     "modified": "2022-05-26",
-                    "temporal": "2022-05-01/2022-05-07"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c2fdab03-06c8-4125-9732-66a6706e4e94",
+                    "temporal": "2022-05-01/2022-05-07",
+                    "title": "COVID-19 Nursing Home Data : 2022-05-08"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-05/COVID-19%20Nursing%20Home%20Data%2005.01.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f4bd74da-3dbc-4563-bca3-6a9da6810293",
-                    "title": "COVID-19 Nursing Home Data : 2022-05-01",
                     "modified": "2022-05-19",
-                    "temporal": "2022-04-24/2022-04-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f4bd74da-3dbc-4563-bca3-6a9da6810293",
+                    "temporal": "2022-04-24/2022-04-30",
+                    "title": "COVID-19 Nursing Home Data : 2022-05-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-05/COVID-19%20Nursing%20Home%20Data%2004.24.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4e72616a-33fb-43b7-aacd-1c56c64e18ca",
-                    "title": "COVID-19 Nursing Home Data : 2022-04-24",
                     "modified": "2022-05-12",
-                    "temporal": "2022-04-17/2022-04-23"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4e72616a-33fb-43b7-aacd-1c56c64e18ca",
+                    "temporal": "2022-04-17/2022-04-23",
+                    "title": "COVID-19 Nursing Home Data : 2022-04-24"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-05/COVID-19%20Nursing%20Home%20Data%2004.17.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c7bd21d6-29e5-4d80-a1ed-fc9cc3dcdc2d",
-                    "title": "COVID-19 Nursing Home Data : 2022-04-17",
                     "modified": "2022-05-05",
-                    "temporal": "2022-04-10/2022-04-16"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c7bd21d6-29e5-4d80-a1ed-fc9cc3dcdc2d",
+                    "temporal": "2022-04-10/2022-04-16",
+                    "title": "COVID-19 Nursing Home Data : 2022-04-17"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-04/COVID-19%20Nursing%20Home%20Data%2004.10.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ce6ce1a5-f941-4120-8754-a24295206bf4",
-                    "title": "COVID-19 Nursing Home Data : 2022-04-10",
                     "modified": "2022-04-28",
-                    "temporal": "2022-04-03/2022-04-09"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ce6ce1a5-f941-4120-8754-a24295206bf4",
+                    "temporal": "2022-04-03/2022-04-09",
+                    "title": "COVID-19 Nursing Home Data : 2022-04-10"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-04/COVID-19%20Nursing%20Home%20Data%2004.03.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d67e9790-5595-477d-9d60-7765aeb0a32b",
-                    "title": "COVID-19 Nursing Home Data : 2022-04-03",
                     "modified": "2022-04-21",
-                    "temporal": "2022-03-27/2022-04-02"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d67e9790-5595-477d-9d60-7765aeb0a32b",
+                    "temporal": "2022-03-27/2022-04-02",
+                    "title": "COVID-19 Nursing Home Data : 2022-04-03"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-04/COVID-19%20Nursing%20Home%20Data%2003.27.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/656918e3-3df0-4177-ae66-a8cb2d4ff094",
-                    "title": "COVID-19 Nursing Home Data : 2022-03-27",
                     "modified": "2022-04-14",
-                    "temporal": "2022-03-20/2022-03-26"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/656918e3-3df0-4177-ae66-a8cb2d4ff094",
+                    "temporal": "2022-03-20/2022-03-26",
+                    "title": "COVID-19 Nursing Home Data : 2022-03-27"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-04/COVID-19%20Nursing%20Home%20Data%2003.20.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0a3c1a11-f9f5-4c1f-bda0-038721b7febb",
-                    "title": "COVID-19 Nursing Home Data : 2022-03-20",
                     "modified": "2022-04-07",
-                    "temporal": "2022-03-13/2022-03-19"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0a3c1a11-f9f5-4c1f-bda0-038721b7febb",
+                    "temporal": "2022-03-13/2022-03-19",
+                    "title": "COVID-19 Nursing Home Data : 2022-03-20"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-03/COVID-19%20Nursing%20Home%20Data%2003.13.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6cdfb640-18cd-4283-9f06-99a19057fd5f",
-                    "title": "COVID-19 Nursing Home Data : 2022-03-13",
                     "modified": "2022-03-31",
-                    "temporal": "2022-03-06/2022-03-12"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6cdfb640-18cd-4283-9f06-99a19057fd5f",
+                    "temporal": "2022-03-06/2022-03-12",
+                    "title": "COVID-19 Nursing Home Data : 2022-03-13"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-03/adff9b9a-ee45-40b0-a37b-f2df4dbc7b5f/COVID-19%20Nursing%20Home%20Data%2003.06.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/35f2b763-c6d3-4348-bc99-98da62424c40",
-                    "title": "COVID-19 Nursing Home Data : 2022-03-06",
                     "modified": "2022-03-24",
-                    "temporal": "2022-02-27/2022-03-05"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/35f2b763-c6d3-4348-bc99-98da62424c40",
+                    "temporal": "2022-02-27/2022-03-05",
+                    "title": "COVID-19 Nursing Home Data : 2022-03-06"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-03/COVID-19%20Nursing%20Home%20Data%2002.27.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/83239029-e0c6-4097-976b-5ee1e2417f12",
-                    "title": "COVID-19 Nursing Home Data : 2022-02-27",
                     "modified": "2022-03-17",
-                    "temporal": "2022-02-20/2022-02-26"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/83239029-e0c6-4097-976b-5ee1e2417f12",
+                    "temporal": "2022-02-20/2022-02-26",
+                    "title": "COVID-19 Nursing Home Data : 2022-02-27"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-03/COVID-19%20Nursing%20Home%20Data%2002.20.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/04e85884-beb7-4fce-9a89-75ba55127fa5",
-                    "title": "COVID-19 Nursing Home Data : 2022-02-20",
                     "modified": "2022-03-10",
-                    "temporal": "2022-02-13/2022-02-19"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/04e85884-beb7-4fce-9a89-75ba55127fa5",
+                    "temporal": "2022-02-13/2022-02-19",
+                    "title": "COVID-19 Nursing Home Data : 2022-02-20"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-03/COVID-19%20Nursing%20Home%20Data%2002.13.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/88265caf-7f05-4f34-bf4d-e99ae6398492",
-                    "title": "COVID-19 Nursing Home Data : 2022-02-13",
                     "modified": "2022-03-03",
-                    "temporal": "2022-02-06/2022-02-12"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/88265caf-7f05-4f34-bf4d-e99ae6398492",
+                    "temporal": "2022-02-06/2022-02-12",
+                    "title": "COVID-19 Nursing Home Data : 2022-02-13"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-02/COVID-19%20Nursing%20Home%20Data%2002.06.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/567576a9-71d3-441e-a182-37c8232121be",
-                    "title": "COVID-19 Nursing Home Data : 2022-02-06",
                     "modified": "2022-02-24",
-                    "temporal": "2022-01-30/2022-02-05"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/567576a9-71d3-441e-a182-37c8232121be",
+                    "temporal": "2022-01-30/2022-02-05",
+                    "title": "COVID-19 Nursing Home Data : 2022-02-06"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-02/COVID-19%20Nursing%20Home%20Data%2001.30.2022%20FINAL.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/337c1271-771f-461a-bda9-ade5f2bc104e",
-                    "title": "COVID-19 Nursing Home Data : 2022-01-30",
                     "modified": "2022-02-17",
-                    "temporal": "2022-01-23/2022-01-29"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/337c1271-771f-461a-bda9-ade5f2bc104e",
+                    "temporal": "2022-01-23/2022-01-29",
+                    "title": "COVID-19 Nursing Home Data : 2022-01-30"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-02/COVID-19%20Nursing%20Home%20Data%2001.23.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8b46674e-a152-4e88-9307-a193c70ab03a",
-                    "title": "COVID-19 Nursing Home Data : 2022-01-23",
                     "modified": "2022-02-10",
-                    "temporal": "2022-01-16/2022-01-22"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8b46674e-a152-4e88-9307-a193c70ab03a",
+                    "temporal": "2022-01-16/2022-01-22",
+                    "title": "COVID-19 Nursing Home Data : 2022-01-23"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-02/COVID-19%20Nursing%20Home%20Data%2001.16.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ae89f796-f854-4489-992f-ea1db0b4353a",
-                    "title": "COVID-19 Nursing Home Data : 2022-01-16",
                     "modified": "2022-02-03",
-                    "temporal": "2022-01-09/2022-01-15"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ae89f796-f854-4489-992f-ea1db0b4353a",
+                    "temporal": "2022-01-09/2022-01-15",
+                    "title": "COVID-19 Nursing Home Data : 2022-01-16"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-01/COVID-19%20Nursing%20Home%20Data%2001.09.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1d93f14c-b005-4af7-a95d-6f93deaa3a6d",
-                    "title": "COVID-19 Nursing Home Data : 2022-01-09",
                     "modified": "2022-01-27",
-                    "temporal": "2022-01-02/2022-01-08"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1d93f14c-b005-4af7-a95d-6f93deaa3a6d",
+                    "temporal": "2022-01-02/2022-01-08",
+                    "title": "COVID-19 Nursing Home Data : 2022-01-09"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-01/COVID-19%20Nursing%20Home%20Data%2001.02.2022.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c7509d2c-dc1b-45db-9e44-19da3494ad90",
-                    "title": "COVID-19 Nursing Home Data : 2022-01-02",
                     "modified": "2022-01-20",
-                    "temporal": "2021-12-26/2022-01-01"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c7509d2c-dc1b-45db-9e44-19da3494ad90",
+                    "temporal": "2021-12-26/2022-01-01",
+                    "title": "COVID-19 Nursing Home Data : 2022-01-02"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-01/COVID-19%20Nursing%20Home%20Data%2012.26.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9ae8f60a-21e8-49f6-95e6-8fe9851df1be",
-                    "title": "COVID-19 Nursing Home Data : 2021-12-26",
                     "modified": "2022-01-13",
-                    "temporal": "2021-12-19/2021-12-25"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9ae8f60a-21e8-49f6-95e6-8fe9851df1be",
+                    "temporal": "2021-12-19/2021-12-25",
+                    "title": "COVID-19 Nursing Home Data : 2021-12-26"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-01/COVID-19%20Nursing%20Home%20Data%2012.19.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/de26d59d-d329-4851-a11e-bab4ba85842b",
-                    "title": "COVID-19 Nursing Home Data : 2021-12-19",
                     "modified": "2022-01-06",
-                    "temporal": "2021-12-12/2021-12-18"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/de26d59d-d329-4851-a11e-bab4ba85842b",
+                    "temporal": "2021-12-12/2021-12-18",
+                    "title": "COVID-19 Nursing Home Data : 2021-12-19"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-12/COVID-19%20Nursing%20Home%20Data%2012.12.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/572d5ae2-632d-4a6f-8692-62b1c28df8ee",
-                    "title": "COVID-19 Nursing Home Data : 2021-12-12",
                     "modified": "2021-12-30",
-                    "temporal": "2021-12-05/2021-12-11"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/572d5ae2-632d-4a6f-8692-62b1c28df8ee",
+                    "temporal": "2021-12-05/2021-12-11",
+                    "title": "COVID-19 Nursing Home Data : 2021-12-12"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-12/COVID-19%20Nursing%20Home%20Data%2012.05.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8dab1a53-ee5a-48cd-9f0a-0eb3c9890c02",
-                    "title": "COVID-19 Nursing Home Data : 2021-12-05",
                     "modified": "2021-12-23",
-                    "temporal": "2021-11-28/2021-12-04"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8dab1a53-ee5a-48cd-9f0a-0eb3c9890c02",
+                    "temporal": "2021-11-28/2021-12-04",
+                    "title": "COVID-19 Nursing Home Data : 2021-12-05"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-12/COVID-19%20Nursing%20Home%20Data%2011.28.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/22060d40-4783-495c-b2e2-bdd913bcda49",
-                    "title": "COVID-19 Nursing Home Data : 2021-11-28",
                     "modified": "2021-12-16",
-                    "temporal": "2021-11-21/2021-11-27"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/22060d40-4783-495c-b2e2-bdd913bcda49",
+                    "temporal": "2021-11-21/2021-11-27",
+                    "title": "COVID-19 Nursing Home Data : 2021-11-28"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-12/COVID-19%20Nursing%20Home%20Data%2011.21.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2534142f-b0e6-4e0c-baf7-7854adf909d7",
-                    "title": "COVID-19 Nursing Home Data : 2021-11-21",
                     "modified": "2021-12-10",
-                    "temporal": "2021-11-14/2021-11-20"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2534142f-b0e6-4e0c-baf7-7854adf909d7",
+                    "temporal": "2021-11-14/2021-11-20",
+                    "title": "COVID-19 Nursing Home Data : 2021-11-21"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-12/COVID-19%20Nursing%20Home%20Data%2011.14.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e57d50ca-334a-4327-966c-bce5d52bcb34",
-                    "title": "COVID-19 Nursing Home Data : 2021-11-14",
                     "modified": "2021-12-02",
-                    "temporal": "2021-11-07/2021-11-13"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e57d50ca-334a-4327-966c-bce5d52bcb34",
+                    "temporal": "2021-11-07/2021-11-13",
+                    "title": "COVID-19 Nursing Home Data : 2021-11-14"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/COVID-19%20Nursing%20Home%20Data%2011.07.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/65115db0-d703-4258-8426-1e5f902e5338",
-                    "title": "COVID-19 Nursing Home Data : 2021-11-07",
                     "modified": "2021-11-24",
-                    "temporal": "2021-10-31/2021-11-06"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/65115db0-d703-4258-8426-1e5f902e5338",
+                    "temporal": "2021-10-31/2021-11-06",
+                    "title": "COVID-19 Nursing Home Data : 2021-11-07"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/COVID-19%20Nursing%20Home%20Data%2010.31.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/180122f0-d08c-426f-b3ed-3f23b8c4e785",
-                    "title": "COVID-19 Nursing Home Data : 2021-10-31",
                     "modified": "2021-11-18",
-                    "temporal": "2021-10-24/2021-10-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/180122f0-d08c-426f-b3ed-3f23b8c4e785",
+                    "temporal": "2021-10-24/2021-10-30",
+                    "title": "COVID-19 Nursing Home Data : 2021-10-31"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/62cda09e-cbf0-4a35-bd92-a69e44753fe0/COVID-19%20Nursing%20Home%20Data%2010.24.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/09ea1e16-df2e-4b97-b467-b9dd0a26e890",
-                    "title": "COVID-19 Nursing Home Data : 2021-10-24",
                     "modified": "2021-11-10",
-                    "temporal": "2021-10-17/2021-10-23"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/09ea1e16-df2e-4b97-b467-b9dd0a26e890",
+                    "temporal": "2021-10-17/2021-10-23",
+                    "title": "COVID-19 Nursing Home Data : 2021-10-24"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/a4c16a95-eff2-43e5-b33f-95addfc69ac2/COVID-19%20Nursing%20Home%20Data%2010.17.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/080f12be-4f95-4d76-a457-821e36c0e2f5",
-                    "title": "COVID-19 Nursing Home Data : 2021-10-17",
                     "modified": "2021-11-04",
-                    "temporal": "2021-10-10/2021-10-16"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/080f12be-4f95-4d76-a457-821e36c0e2f5",
+                    "temporal": "2021-10-10/2021-10-16",
+                    "title": "COVID-19 Nursing Home Data : 2021-10-17"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-10/81407303-0c44-4c9c-ae7d-98753649eebd/COVID-19%20Nursing%20Home%20Data%2010.10.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/41aaefc2-53ce-4ef6-bc9d-546425ee7411",
-                    "title": "COVID-19 Nursing Home Data : 2021-10-10",
                     "modified": "2021-10-28",
-                    "temporal": "2021-10-03/2021-10-09"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/41aaefc2-53ce-4ef6-bc9d-546425ee7411",
+                    "temporal": "2021-10-03/2021-10-09",
+                    "title": "COVID-19 Nursing Home Data : 2021-10-10"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-10/e0c87c9b-4cfe-4db8-b77b-0bb62153ce20/COVID-19%20Nursing%20Home%20Data%2010.03.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ad75b4b0-6b0f-492a-9357-10ac29d5883e",
-                    "title": "COVID-19 Nursing Home Data : 2021-10-03",
                     "modified": "2021-10-21",
-                    "temporal": "2021-09-26/2021-10-02"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ad75b4b0-6b0f-492a-9357-10ac29d5883e",
+                    "temporal": "2021-09-26/2021-10-02",
+                    "title": "COVID-19 Nursing Home Data : 2021-10-03"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-03/c398cc42-55c4-409d-af8d-64681b17ae82/COVID-19%20Nursing%20Home%20Data%2009.26.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ca0b1244-cd75-49f8-a463-0332240a4d18",
-                    "title": "COVID-19 Nursing Home Data : 2021-09-26",
                     "modified": "2021-10-14",
-                    "temporal": "2021-09-19/2021-09-25"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ca0b1244-cd75-49f8-a463-0332240a4d18",
+                    "temporal": "2021-09-19/2021-09-25",
+                    "title": "COVID-19 Nursing Home Data : 2021-09-26"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-10/2ead78d8-fda8-4aec-8ed7-3f6ce83bfd1b/COVID-19%20Nursing%20Home%20Data%2009.19.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3caf9b17-1a18-477b-b122-632f9a1d2ff6",
-                    "title": "COVID-19 Nursing Home Data : 2021-09-19",
                     "modified": "2021-10-07",
-                    "temporal": "2021-09-12/2021-09-18"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3caf9b17-1a18-477b-b122-632f9a1d2ff6",
+                    "temporal": "2021-09-12/2021-09-18",
+                    "title": "COVID-19 Nursing Home Data : 2021-09-19"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-09/b3e1fdd5-0753-4453-88ca-5d0dc9627a5a/COVID-19%20Nursing%20Home%20Data%2009.12.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/35da9162-d09f-434d-83fd-5dfe6b2c6d77",
-                    "title": "COVID-19 Nursing Home Data : 2021-09-12",
                     "modified": "2021-09-30",
-                    "temporal": "2021-09-05/2021-09-11"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/35da9162-d09f-434d-83fd-5dfe6b2c6d77",
+                    "temporal": "2021-09-05/2021-09-11",
+                    "title": "COVID-19 Nursing Home Data : 2021-09-12"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-09/15d3a917-aada-4acb-b7fe-ba505cca9ca7/COVID-19%20Nursing%20Home%20Data%2009.05.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3fd78f4b-0a21-4acf-b90c-4fcd7d27d642",
-                    "title": "COVID-19 Nursing Home Data : 2021-09-05",
                     "modified": "2021-09-23",
-                    "temporal": "2021-08-29/2021-09-04"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3fd78f4b-0a21-4acf-b90c-4fcd7d27d642",
+                    "temporal": "2021-08-29/2021-09-04",
+                    "title": "COVID-19 Nursing Home Data : 2021-09-05"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-09/b7fe694d-1800-4806-b715-b9cf0195b273/COVID-19%20Nursing%20Home%20Data%2008.29.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/454d3dd0-e294-4238-950e-132f1bdb2fed",
-                    "title": "COVID-19 Nursing Home Data : 2021-08-29",
                     "modified": "2021-09-16",
-                    "temporal": "2021-08-22/2021-08-28"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/454d3dd0-e294-4238-950e-132f1bdb2fed",
+                    "temporal": "2021-08-22/2021-08-28",
+                    "title": "COVID-19 Nursing Home Data : 2021-08-29"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-09/a2a7b7d0-451f-4d79-981d-9c5043ade622/COVID-19%20Nursing%20Home%20Data%2008.22.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/28430192-dc41-49a1-bb18-a6558162479c",
-                    "title": "COVID-19 Nursing Home Data : 2021-08-22",
                     "modified": "2021-09-09",
-                    "temporal": "2021-08-15/2021-08-21"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/28430192-dc41-49a1-bb18-a6558162479c",
+                    "temporal": "2021-08-15/2021-08-21",
+                    "title": "COVID-19 Nursing Home Data : 2021-08-22"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-09/b941feb4-12a8-44d1-9d45-9a1add72001c/COVID-19%20Nursing%20Home%20Data%2008.15.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9840e2af-7398-43f7-9693-2f8b6ba27be1",
-                    "title": "COVID-19 Nursing Home Data : 2021-08-15",
                     "modified": "2021-09-02",
-                    "temporal": "2021-08-08/2021-08-14"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9840e2af-7398-43f7-9693-2f8b6ba27be1",
+                    "temporal": "2021-08-08/2021-08-14",
+                    "title": "COVID-19 Nursing Home Data : 2021-08-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-12/COVID-19%20Nursing%20Home%20Data%2008.08.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/91198975-4ce0-43a2-adde-e68df283a60e",
-                    "title": "COVID-19 Nursing Home Data : 2021-08-08",
                     "modified": "2023-03-06",
-                    "temporal": "2021-08-01/2021-08-07"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/91198975-4ce0-43a2-adde-e68df283a60e",
+                    "temporal": "2021-08-01/2021-08-07",
+                    "title": "COVID-19 Nursing Home Data : 2021-08-08"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-08/covid-19-nursing-home-data-08.01.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/81c44af8-44da-45a7-b182-78a51f3ed4b6",
-                    "title": "COVID-19 Nursing Home Data : 2021-08-01",
                     "modified": "2021-08-19",
-                    "temporal": "2021-07-25/2021-07-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/81c44af8-44da-45a7-b182-78a51f3ed4b6",
+                    "temporal": "2021-07-25/2021-07-31",
+                    "title": "COVID-19 Nursing Home Data : 2021-08-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-08/covid-19-nursing-home-data-07.25.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b290adc2-7646-4a4d-b54d-ee7765916f36",
-                    "title": "COVID-19 Nursing Home Data : 2021-07-25",
                     "modified": "2021-08-12",
-                    "temporal": "2021-07-18/2021-07-24"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b290adc2-7646-4a4d-b54d-ee7765916f36",
+                    "temporal": "2021-07-18/2021-07-24",
+                    "title": "COVID-19 Nursing Home Data : 2021-07-25"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-08/covid-19-nursing-home-data-07.18.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/79c806af-0121-42c4-a61c-b006e5e2632e",
-                    "title": "COVID-19 Nursing Home Data : 2021-07-18",
                     "modified": "2021-08-05",
-                    "temporal": "2021-07-11/2021-07-17"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/79c806af-0121-42c4-a61c-b006e5e2632e",
+                    "temporal": "2021-07-11/2021-07-17",
+                    "title": "COVID-19 Nursing Home Data : 2021-07-18"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-07.11.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ce0033b2-368c-4746-9538-e16c737668f0",
-                    "title": "COVID-19 Nursing Home Data : 2021-07-11",
                     "modified": "2021-07-29",
-                    "temporal": "2021-07-04/2021-07-10"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ce0033b2-368c-4746-9538-e16c737668f0",
+                    "temporal": "2021-07-04/2021-07-10",
+                    "title": "COVID-19 Nursing Home Data : 2021-07-11"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/COVID-19%20Nursing%20Home%20Data%2007.04.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4bb1b171-89fc-45a8-b3bc-888d8ba3dfa9",
-                    "title": "COVID-19 Nursing Home Data : 2021-07-04",
                     "modified": "2021-07-22",
-                    "temporal": "2021-06-27/2021-07-03"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4bb1b171-89fc-45a8-b3bc-888d8ba3dfa9",
+                    "temporal": "2021-06-27/2021-07-03",
+                    "title": "COVID-19 Nursing Home Data : 2021-07-04"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/COVID-19%20Nursing%20Home%20Data%2006%2027%2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c5923037-dc38-49db-8695-857d21a052a6",
-                    "title": "COVID-19 Nursing Home Data : 2021-06-27",
                     "modified": "2021-07-19",
-                    "temporal": "2021-06-20/2021-06-26"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c5923037-dc38-49db-8695-857d21a052a6",
+                    "temporal": "2021-06-20/2021-06-26",
+                    "title": "COVID-19 Nursing Home Data : 2021-06-27"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-06-20-21.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e5a47fb7-4ee0-416d-aef7-301c6d25e6c6",
-                    "title": "COVID-19 Nursing Home Data : 2021-06-20",
                     "modified": "2021-07-14",
-                    "temporal": "2021-06-13/2021-06-19"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e5a47fb7-4ee0-416d-aef7-301c6d25e6c6",
+                    "temporal": "2021-06-13/2021-06-19",
+                    "title": "COVID-19 Nursing Home Data : 2021-06-20"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-06-13-21.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/48d60fdb-c145-47e1-90fb-cb0d3d4f9897",
-                    "title": "COVID-19 Nursing Home Data : 2021-06-13",
                     "modified": "2021-07-13",
-                    "temporal": "2021-06-06/2021-06-12"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/48d60fdb-c145-47e1-90fb-cb0d3d4f9897",
+                    "temporal": "2021-06-06/2021-06-12",
+                    "title": "COVID-19 Nursing Home Data : 2021-06-13"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-06-06-21.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a2edf514-18cc-4d4c-9e1b-79357fd727cb",
-                    "title": "COVID-19 Nursing Home Data : 2021-06-06",
                     "modified": "2021-07-13",
-                    "temporal": "2021-05-30/2021-06-05"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a2edf514-18cc-4d4c-9e1b-79357fd727cb",
+                    "temporal": "2021-05-30/2021-06-05",
+                    "title": "COVID-19 Nursing Home Data : 2021-06-06"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-05-30-21.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/78a12e28-64cb-47d8-bd47-dcae0918b287",
-                    "title": "COVID-19 Nursing Home Data : 2021-05-30",
                     "modified": "2021-07-13",
-                    "temporal": "2021-05-23/2021-05-29"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/78a12e28-64cb-47d8-bd47-dcae0918b287",
+                    "temporal": "2021-05-23/2021-05-29",
+                    "title": "COVID-19 Nursing Home Data : 2021-05-30"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-05.23.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0b8fb893-28c6-4fa2-b002-4d041234aeca",
-                    "title": "COVID-19 Nursing Home Data : 2021-05-23",
                     "modified": "2021-07-13",
-                    "temporal": "2021-05-16/2021-05-22"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0b8fb893-28c6-4fa2-b002-4d041234aeca",
+                    "temporal": "2021-05-16/2021-05-22",
+                    "title": "COVID-19 Nursing Home Data : 2021-05-23"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-05.16.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f53f9d4b-a8a7-43b2-9e2b-6069e194bb8e",
-                    "title": "COVID-19 Nursing Home Data : 2021-05-16",
                     "modified": "2021-07-13",
-                    "temporal": "2021-05-09/2021-05-15"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f53f9d4b-a8a7-43b2-9e2b-6069e194bb8e",
+                    "temporal": "2021-05-09/2021-05-15",
+                    "title": "COVID-19 Nursing Home Data : 2021-05-16"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-05.09.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/082c93d6-253c-4e9f-bb42-49fd363f859e",
-                    "title": "COVID-19 Nursing Home Data : 2021-05-09",
                     "modified": "2021-07-13",
-                    "temporal": "2021-05-02/2021-05-08"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/082c93d6-253c-4e9f-bb42-49fd363f859e",
+                    "temporal": "2021-05-02/2021-05-08",
+                    "title": "COVID-19 Nursing Home Data : 2021-05-09"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-05.02.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b6f25e97-7723-4e15-9fb2-ce6dfeef47db",
-                    "title": "COVID-19 Nursing Home Data : 2021-05-02",
                     "modified": "2021-07-13",
-                    "temporal": "2021-04-25/2021-05-01"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b6f25e97-7723-4e15-9fb2-ce6dfeef47db",
+                    "temporal": "2021-04-25/2021-05-01",
+                    "title": "COVID-19 Nursing Home Data : 2021-05-02"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-04.25.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/01b9a5ea-3ea6-4723-9961-b7cfe6cbb19d",
-                    "title": "COVID-19 Nursing Home Data : 2021-04-25",
                     "modified": "2021-07-13",
-                    "temporal": "2021-04-18/2021-04-24"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/01b9a5ea-3ea6-4723-9961-b7cfe6cbb19d",
+                    "temporal": "2021-04-18/2021-04-24",
+                    "title": "COVID-19 Nursing Home Data : 2021-04-25"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-04.18.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e6d758c3-628f-4662-9577-ceba0024d430",
-                    "title": "COVID-19 Nursing Home Data : 2021-04-18",
                     "modified": "2021-07-13",
-                    "temporal": "2021-04-11/2021-04-17"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e6d758c3-628f-4662-9577-ceba0024d430",
+                    "temporal": "2021-04-11/2021-04-17",
+                    "title": "COVID-19 Nursing Home Data : 2021-04-18"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-04.11.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5023d6db-5146-48b5-8287-21ac91a7402e",
-                    "title": "COVID-19 Nursing Home Data : 2021-04-11",
                     "modified": "2021-07-13",
-                    "temporal": "2021-04-04/2021-04-10"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5023d6db-5146-48b5-8287-21ac91a7402e",
+                    "temporal": "2021-04-04/2021-04-10",
+                    "title": "COVID-19 Nursing Home Data : 2021-04-11"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-04.04.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c47e6425-c077-4696-8ca3-126e98c9494d",
-                    "title": "COVID-19 Nursing Home Data : 2021-04-04",
                     "modified": "2021-07-13",
-                    "temporal": "2021-03-28/2021-04-03"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c47e6425-c077-4696-8ca3-126e98c9494d",
+                    "temporal": "2021-03-28/2021-04-03",
+                    "title": "COVID-19 Nursing Home Data : 2021-04-04"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-03.28.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5ee7711c-1b19-43db-b938-b17315453549",
-                    "title": "COVID-19 Nursing Home Data : 2021-03-28",
                     "modified": "2021-07-13",
-                    "temporal": "2021-03-21/2021-03-27"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5ee7711c-1b19-43db-b938-b17315453549",
+                    "temporal": "2021-03-21/2021-03-27",
+                    "title": "COVID-19 Nursing Home Data : 2021-03-28"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-03.21.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/30ea836d-fd3f-4bd4-9474-45f21aa72abe",
-                    "title": "COVID-19 Nursing Home Data : 2021-03-21",
                     "modified": "2021-07-13",
-                    "temporal": "2021-03-14/2021-03-20"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/30ea836d-fd3f-4bd4-9474-45f21aa72abe",
+                    "temporal": "2021-03-14/2021-03-20",
+                    "title": "COVID-19 Nursing Home Data : 2021-03-21"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-03.14.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1c8ce066-8daa-49b5-b472-5ea540a0036a",
-                    "title": "COVID-19 Nursing Home Data : 2021-03-14",
                     "modified": "2021-07-13",
-                    "temporal": "2021-03-07/2021-03-13"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1c8ce066-8daa-49b5-b472-5ea540a0036a",
+                    "temporal": "2021-03-07/2021-03-13",
+                    "title": "COVID-19 Nursing Home Data : 2021-03-14"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-03.07.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ee4faa9d-0193-4a7f-b6da-4818e2bec2c7",
-                    "title": "COVID-19 Nursing Home Data : 2021-03-07",
                     "modified": "2021-07-13",
-                    "temporal": "2021-02-28/2021-03-06"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ee4faa9d-0193-4a7f-b6da-4818e2bec2c7",
+                    "temporal": "2021-02-28/2021-03-06",
+                    "title": "COVID-19 Nursing Home Data : 2021-03-07"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-02.28.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/52cca4d6-c13a-4013-97ff-a594f8c3aada",
-                    "title": "COVID-19 Nursing Home Data : 2021-02-28",
                     "modified": "2021-07-13",
-                    "temporal": "2021-02-21/2021-02-27"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/52cca4d6-c13a-4013-97ff-a594f8c3aada",
+                    "temporal": "2021-02-21/2021-02-27",
+                    "title": "COVID-19 Nursing Home Data : 2021-02-28"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-02.14.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ffe128b1-b603-4184-9768-7d9ef9a10cde",
-                    "title": "COVID-19 Nursing Home Data : 2021-02-21",
                     "modified": "2021-07-13",
-                    "temporal": "2021-02-14/2021-02-20"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ffe128b1-b603-4184-9768-7d9ef9a10cde",
+                    "temporal": "2021-02-14/2021-02-20",
+                    "title": "COVID-19 Nursing Home Data : 2021-02-21"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-02.14.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/797b2692-559b-4014-bc98-d031414139b0",
-                    "title": "COVID-19 Nursing Home Data : 2021-02-14",
                     "modified": "2021-07-13",
-                    "temporal": "2021-02-07/2021-02-13"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/797b2692-559b-4014-bc98-d031414139b0",
+                    "temporal": "2021-02-07/2021-02-13",
+                    "title": "COVID-19 Nursing Home Data : 2021-02-14"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-02.07.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/42e59fda-494c-4378-9675-66292a3b238b",
-                    "title": "COVID-19 Nursing Home Data : 2021-02-07",
                     "modified": "2021-07-13",
-                    "temporal": "2021-01-31/2021-02-06"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/42e59fda-494c-4378-9675-66292a3b238b",
+                    "temporal": "2021-01-31/2021-02-06",
+                    "title": "COVID-19 Nursing Home Data : 2021-02-07"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-01.31.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a7159fc6-d5d4-4eba-b0b6-1309d60a0a81",
-                    "title": "COVID-19 Nursing Home Data : 2021-01-31",
                     "modified": "2021-07-13",
-                    "temporal": "2021-01-24/2021-01-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a7159fc6-d5d4-4eba-b0b6-1309d60a0a81",
+                    "temporal": "2021-01-24/2021-01-30",
+                    "title": "COVID-19 Nursing Home Data : 2021-01-31"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-01.24.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/19de6348-40ba-48b4-ad7e-1b633bb86227",
-                    "title": "COVID-19 Nursing Home Data : 2021-01-24",
                     "modified": "2021-07-13",
-                    "temporal": "2021-01-17/2021-01-23"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/19de6348-40ba-48b4-ad7e-1b633bb86227",
+                    "temporal": "2021-01-17/2021-01-23",
+                    "title": "COVID-19 Nursing Home Data : 2021-01-24"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-01.17.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c6cf6494-6801-45ef-ba07-2f35a11a5d8e",
-                    "title": "COVID-19 Nursing Home Data : 2021-01-17",
                     "modified": "2021-07-13",
-                    "temporal": "2021-01-10/2021-01-16"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c6cf6494-6801-45ef-ba07-2f35a11a5d8e",
+                    "temporal": "2021-01-10/2021-01-16",
+                    "title": "COVID-19 Nursing Home Data : 2021-01-17"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-01.10.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/92b5529f-a45b-4c3c-909b-6a60897b314c",
-                    "title": "COVID-19 Nursing Home Data : 2021-01-10",
                     "modified": "2021-07-13",
-                    "temporal": "2021-01-03/2021-01-09"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/92b5529f-a45b-4c3c-909b-6a60897b314c",
+                    "temporal": "2021-01-03/2021-01-09",
+                    "title": "COVID-19 Nursing Home Data : 2021-01-10"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-01.03.2021.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/49d49e02-393b-4937-a2bf-710d1d3912b5",
-                    "title": "COVID-19 Nursing Home Data : 2021-01-03",
                     "modified": "2021-07-13",
-                    "temporal": "2020-12-27/2021-01-02"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/49d49e02-393b-4937-a2bf-710d1d3912b5",
+                    "temporal": "2020-12-27/2021-01-02",
+                    "title": "COVID-19 Nursing Home Data : 2021-01-03"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-12.27.2020.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c9981cf1-22ef-4ed8-abf9-0b8c935a5692",
-                    "title": "COVID-19 Nursing Home Data : 2020-12-27",
                     "modified": "2021-07-13",
-                    "temporal": "2020-12-20/2020-12-26"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c9981cf1-22ef-4ed8-abf9-0b8c935a5692",
+                    "temporal": "2020-12-20/2020-12-26",
+                    "title": "COVID-19 Nursing Home Data : 2020-12-27"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-12.20.2020.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6d65f3b8-5c14-4a05-a015-29160033c823",
-                    "title": "COVID-19 Nursing Home Data : 2020-12-20",
                     "modified": "2021-07-13",
-                    "temporal": "2020-12-13/2020-12-19"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6d65f3b8-5c14-4a05-a015-29160033c823",
+                    "temporal": "2020-12-13/2020-12-19",
+                    "title": "COVID-19 Nursing Home Data : 2020-12-20"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-12.13.2020.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9d24416c-8419-43c6-a0ed-996653cfc2c7",
-                    "title": "COVID-19 Nursing Home Data : 2020-12-13",
                     "modified": "2021-07-13",
-                    "temporal": "2020-12-06/2020-12-12"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9d24416c-8419-43c6-a0ed-996653cfc2c7",
+                    "temporal": "2020-12-06/2020-12-12",
+                    "title": "COVID-19 Nursing Home Data : 2020-12-13"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-12.06.2020.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9abae146-423c-4fe3-a471-f5a4a544f81b",
-                    "title": "COVID-19 Nursing Home Data : 2020-12-06",
                     "modified": "2021-07-13",
-                    "temporal": "2020-11-29/2020-12-05"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9abae146-423c-4fe3-a471-f5a4a544f81b",
+                    "temporal": "2020-11-29/2020-12-05",
+                    "title": "COVID-19 Nursing Home Data : 2020-12-06"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-11.29.2020.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bfe23217-4943-4ac6-9655-698af00bd9a8",
-                    "title": "COVID-19 Nursing Home Data : 2020-11-29",
                     "modified": "2021-07-13",
-                    "temporal": "2020-11-22/2020-11-28"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bfe23217-4943-4ac6-9655-698af00bd9a8",
+                    "temporal": "2020-11-22/2020-11-28",
+                    "title": "COVID-19 Nursing Home Data : 2020-11-29"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-11.22.2020.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ff3f183b-3517-4edf-a8cd-e6df98537fd6",
-                    "title": "COVID-19 Nursing Home Data : 2020-11-22",
                     "modified": "2021-07-13",
-                    "temporal": "2020-11-15/2020-11-21"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ff3f183b-3517-4edf-a8cd-e6df98537fd6",
+                    "temporal": "2020-11-15/2020-11-21",
+                    "title": "COVID-19 Nursing Home Data : 2020-11-22"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-11.15.2020.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d28c34b1-ce6e-473a-95c4-932d550a608d",
-                    "title": "COVID-19 Nursing Home Data : 2020-11-15",
                     "modified": "2021-07-13",
-                    "temporal": "2020-11-08/2020-11-14"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d28c34b1-ce6e-473a-95c4-932d550a608d",
+                    "temporal": "2020-11-08/2020-11-14",
+                    "title": "COVID-19 Nursing Home Data : 2020-11-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-11.08.2020.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ffacb2ad-c604-4cf1-be49-c6fbf53edeef",
-                    "title": "COVID-19 Nursing Home Data : 2020-11-08",
                     "modified": "2021-07-13",
-                    "temporal": "2020-11-01/2020-11-07"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ffacb2ad-c604-4cf1-be49-c6fbf53edeef",
+                    "temporal": "2020-11-01/2020-11-07",
+                    "title": "COVID-19 Nursing Home Data : 2020-11-08"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-11.01.2020.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/735c3ece-0113-4cee-b54c-f49933886be4",
-                    "title": "COVID-19 Nursing Home Data : 2020-11-01",
                     "modified": "2021-07-13",
-                    "temporal": "2020-10-25/2020-10-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/735c3ece-0113-4cee-b54c-f49933886be4",
+                    "temporal": "2020-10-25/2020-10-31",
+                    "title": "COVID-19 Nursing Home Data : 2020-11-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-10.25.2020.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6f18db51-fc26-43b3-9030-cf5a79fa8b18",
-                    "title": "COVID-19 Nursing Home Data : 2020-10-25",
                     "modified": "2021-07-13",
-                    "temporal": "2020-10-18/2020-10-24"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6f18db51-fc26-43b3-9030-cf5a79fa8b18",
+                    "temporal": "2020-10-18/2020-10-24",
+                    "title": "COVID-19 Nursing Home Data : 2020-10-25"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-10.18.2020.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5ab9d437-daa0-424d-beeb-5085661610ec",
-                    "title": "COVID-19 Nursing Home Data : 2020-10-18",
                     "modified": "2021-07-13",
-                    "temporal": "2020-10-11/2020-10-17"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5ab9d437-daa0-424d-beeb-5085661610ec",
+                    "temporal": "2020-10-11/2020-10-17",
+                    "title": "COVID-19 Nursing Home Data : 2020-10-18"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-10.11.2020.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/59ff0b22-5382-4380-8b28-fd52745f19e0",
-                    "title": "COVID-19 Nursing Home Data : 2020-10-11",
                     "modified": "2021-07-13",
-                    "temporal": "2020-10-04/2020-10-10"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/59ff0b22-5382-4380-8b28-fd52745f19e0",
+                    "temporal": "2020-10-04/2020-10-10",
+                    "title": "COVID-19 Nursing Home Data : 2020-10-11"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-10.04.2020.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/091acc4d-26cc-4df7-bf00-0ef2767adb9a",
-                    "title": "COVID-19 Nursing Home Data : 2020-10-04",
                     "modified": "2021-07-13",
-                    "temporal": "2020-09-27/2020-10-03"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/091acc4d-26cc-4df7-bf00-0ef2767adb9a",
+                    "temporal": "2020-09-27/2020-10-03",
+                    "title": "COVID-19 Nursing Home Data : 2020-10-04"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-09.27.2020.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c66403ed-a480-400f-9aa7-d437fc3f82e2",
-                    "title": "COVID-19 Nursing Home Data : 2020-09-27",
                     "modified": "2021-07-13",
-                    "temporal": "2020-09-20/2020-09-26"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c66403ed-a480-400f-9aa7-d437fc3f82e2",
+                    "temporal": "2020-09-20/2020-09-26",
+                    "title": "COVID-19 Nursing Home Data : 2020-09-27"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-09.20.2020.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/924aa75f-ac81-4cb9-9b17-d658b9da0f1b",
-                    "title": "COVID-19 Nursing Home Data : 2020-09-20",
                     "modified": "2021-07-13",
-                    "temporal": "2020-09-13/2020-09-19"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/924aa75f-ac81-4cb9-9b17-d658b9da0f1b",
+                    "temporal": "2020-09-13/2020-09-19",
+                    "title": "COVID-19 Nursing Home Data : 2020-09-20"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-09.13.2020.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d3c436e5-78d9-4b2a-8168-840fbbeff5ec",
-                    "title": "COVID-19 Nursing Home Data : 2020-09-13",
                     "modified": "2021-07-13",
-                    "temporal": "2020-09-06/2020-09-12"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d3c436e5-78d9-4b2a-8168-840fbbeff5ec",
+                    "temporal": "2020-09-06/2020-09-12",
+                    "title": "COVID-19 Nursing Home Data : 2020-09-13"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-09.06.2020.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5c9d9814-6046-416b-9be9-f01a0792a715",
-                    "title": "COVID-19 Nursing Home Data : 2020-09-06",
                     "modified": "2021-07-13",
-                    "temporal": "2020-08-30/2020-09-05"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5c9d9814-6046-416b-9be9-f01a0792a715",
+                    "temporal": "2020-08-30/2020-09-05",
+                    "title": "COVID-19 Nursing Home Data : 2020-09-06"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-08.30.2020.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/20f40eba-a4ce-483c-9e96-8744b7ccc4e7",
-                    "title": "COVID-19 Nursing Home Data : 2020-08-30",
                     "modified": "2021-07-13",
-                    "temporal": "2020-08-23/2020-08-29"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/20f40eba-a4ce-483c-9e96-8744b7ccc4e7",
+                    "temporal": "2020-08-23/2020-08-29",
+                    "title": "COVID-19 Nursing Home Data : 2020-08-30"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-08.23.2020.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b45f3585-1122-4053-9c1e-708a25ce310f",
-                    "title": "COVID-19 Nursing Home Data : 2020-08-23",
                     "modified": "2021-07-13",
-                    "temporal": "2020-08-16/2020-08-22"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b45f3585-1122-4053-9c1e-708a25ce310f",
+                    "temporal": "2020-08-16/2020-08-22",
+                    "title": "COVID-19 Nursing Home Data : 2020-08-23"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-08.16.2020.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fdf84fee-f3fb-4789-80f1-ffe85db721ce",
-                    "title": "COVID-19 Nursing Home Data : 2020-08-16",
                     "modified": "2021-07-13",
-                    "temporal": "2020-08-09/2020-08-15"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fdf84fee-f3fb-4789-80f1-ffe85db721ce",
+                    "temporal": "2020-08-09/2020-08-15",
+                    "title": "COVID-19 Nursing Home Data : 2020-08-16"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-08.09.2020.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/783e17f6-bbae-4445-8ba2-d71a6d8efaca",
-                    "title": "COVID-19 Nursing Home Data : 2020-08-09",
                     "modified": "2021-07-13",
-                    "temporal": "2020-08-02/2020-08-08"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/783e17f6-bbae-4445-8ba2-d71a6d8efaca",
+                    "temporal": "2020-08-02/2020-08-08",
+                    "title": "COVID-19 Nursing Home Data : 2020-08-09"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-08.02.2020.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/75a2b003-03ff-43df-8b03-64d7207cbac1",
-                    "title": "COVID-19 Nursing Home Data : 2020-08-02",
                     "modified": "2021-07-13",
-                    "temporal": "2020-07-26/2020-08-01"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/75a2b003-03ff-43df-8b03-64d7207cbac1",
+                    "temporal": "2020-07-26/2020-08-01",
+                    "title": "COVID-19 Nursing Home Data : 2020-08-02"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-07.26.2020.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a25d2a27-a2e7-4287-94db-21825c9876aa",
-                    "title": "COVID-19 Nursing Home Data : 2020-07-26",
                     "modified": "2021-07-13",
-                    "temporal": "2020-07-19/2020-07-25"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a25d2a27-a2e7-4287-94db-21825c9876aa",
+                    "temporal": "2020-07-19/2020-07-25",
+                    "title": "COVID-19 Nursing Home Data : 2020-07-26"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-07.19.2020.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d2955db6-948e-45f4-afd3-09556294f009",
-                    "title": "COVID-19 Nursing Home Data : 2020-07-19",
                     "modified": "2021-07-13",
-                    "temporal": "2020-07-12/2020-07-18"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d2955db6-948e-45f4-afd3-09556294f009",
+                    "temporal": "2020-07-12/2020-07-18",
+                    "title": "COVID-19 Nursing Home Data : 2020-07-19"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-07.12.2020.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/56552ab3-2bb0-47ac-9ea0-14e2fa350421",
-                    "title": "COVID-19 Nursing Home Data : 2020-07-12",
                     "modified": "2021-07-13",
-                    "temporal": "2020-07-05/2020-07-11"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/56552ab3-2bb0-47ac-9ea0-14e2fa350421",
+                    "temporal": "2020-07-05/2020-07-11",
+                    "title": "COVID-19 Nursing Home Data : 2020-07-12"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-07.05.2020.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d749da52-37fe-45d1-bb42-37e4178e6726",
-                    "title": "COVID-19 Nursing Home Data : 2020-07-05",
                     "modified": "2021-07-13",
-                    "temporal": "2020-06-28/2020-07-04"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d749da52-37fe-45d1-bb42-37e4178e6726",
+                    "temporal": "2020-06-28/2020-07-04",
+                    "title": "COVID-19 Nursing Home Data : 2020-07-05"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-06.28.2020.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/67675670-cb64-4a66-9dc6-266a4cf30a9e",
-                    "title": "COVID-19 Nursing Home Data : 2020-06-28",
                     "modified": "2021-07-13",
-                    "temporal": "2020-06-21/2020-06-27"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/67675670-cb64-4a66-9dc6-266a4cf30a9e",
+                    "temporal": "2020-06-21/2020-06-27",
+                    "title": "COVID-19 Nursing Home Data : 2020-06-28"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-06.21.2020.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/054f1f67-fc46-4fad-b768-2231f2272f6b",
-                    "title": "COVID-19 Nursing Home Data : 2020-06-21",
                     "modified": "2021-07-13",
-                    "temporal": "2020-06-14/2020-06-20"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/054f1f67-fc46-4fad-b768-2231f2272f6b",
+                    "temporal": "2020-06-14/2020-06-20",
+                    "title": "COVID-19 Nursing Home Data : 2020-06-21"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-06.14.2020.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e2093d75-5fa3-4a81-90bb-17063bf386ec",
-                    "title": "COVID-19 Nursing Home Data : 2020-06-14",
                     "modified": "2021-07-13",
-                    "temporal": "2020-06-07/2020-06-13"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e2093d75-5fa3-4a81-90bb-17063bf386ec",
+                    "temporal": "2020-06-07/2020-06-13",
+                    "title": "COVID-19 Nursing Home Data : 2020-06-14"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-06.07.2020.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f2c0f204-ae0c-4987-bc6c-b45095066f72",
-                    "title": "COVID-19 Nursing Home Data : 2020-06-07",
                     "modified": "2021-07-13",
-                    "temporal": "2020-05-31/2020-06-06"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f2c0f204-ae0c-4987-bc6c-b45095066f72",
+                    "temporal": "2020-05-31/2020-06-06",
+                    "title": "COVID-19 Nursing Home Data : 2020-06-07"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-05.31.2020.zip",
                     "mediaType": "application/zip",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/45879379-e341-4019-81f1-ddd19bc46491",
-                    "title": "COVID-19 Nursing Home Data : 2020-05-31",
                     "modified": "2021-07-13",
-                    "temporal": "2020-05-24/2020-05-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/45879379-e341-4019-81f1-ddd19bc46491",
+                    "temporal": "2020-05-24/2020-05-30",
+                    "title": "COVID-19 Nursing Home Data : 2020-05-31"
                 }
             ],
             "identifier": "https://data.cms.gov/data-api/v1/dataset/137f90cb-ac53-4b3d-8358-e65cf64e03d3/data-viewer",
@@ -4009,37 +4008,37 @@
                 "fn": "CMS Innovation Center - CMMI",
                 "hasEmail": "mailto:cmmi-dataset-support@cms.hhs.gov"
             },
-            "describedBy": "https://data.cms.gov/resources/cpc-initiative-participating-primary-care-practices-data-dictionary",
             "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/cpc-initiative-participating-primary-care-practices-data-dictionary",
             "description": "The CPC Initiative - Participating Primary Care Practices dataset provides a list of practices involved in a multi-payer initiative which fosters collaboration between public and private health care payers to strengthen primary care.\u00a0",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/24da2642-7269-4c75-9a62-0dc3a195b205/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/24da2642-7269-4c75-9a62-0dc3a195b205",
                     "description": "latest",
-                    "title": "CPC Initiative - Participating Primary Care Practices : 2017-09-25",
+                    "format": "API",
                     "modified": "2020-12-11",
-                    "temporal": "2017-01-01/2017-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/24da2642-7269-4c75-9a62-0dc3a195b205",
+                    "temporal": "2017-01-01/2017-12-31",
+                    "title": "CPC Initiative - Participating Primary Care Practices : 2017-09-25"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2020-07/CPC_Initiative__Participating_Primary_Care_Practices.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8a099a4e-3bac-4ce2-bb17-b99b488d4440",
-                    "title": "CPC Initiative - Participating Primary Care Practices : 2017-09-25",
                     "modified": "2020-12-11",
-                    "temporal": "2017-01-01/2017-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8a099a4e-3bac-4ce2-bb17-b99b488d4440",
+                    "temporal": "2017-01-01/2017-12-31",
+                    "title": "CPC Initiative - Participating Primary Care Practices : 2017-09-25"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/8a099a4e-3bac-4ce2-bb17-b99b488d4440/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8a099a4e-3bac-4ce2-bb17-b99b488d4440",
-                    "title": "CPC Initiative - Participating Primary Care Practices : 2017-09-25",
+                    "format": "API",
                     "modified": "2020-12-11",
-                    "temporal": "2017-01-01/2017-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8a099a4e-3bac-4ce2-bb17-b99b488d4440",
+                    "temporal": "2017-01-01/2017-12-31",
+                    "title": "CPC Initiative - Participating Primary Care Practices : 2017-09-25"
                 }
             ],
             "identifier": "https://data.cms.gov/data-api/v1/dataset/24da2642-7269-4c75-9a62-0dc3a195b205/data-viewer",
@@ -4083,199 +4082,199 @@
                 "fn": "Deficit Reduction Act Hospital Acquired Conditions - CCSQ",
                 "hasEmail": "mailto:drahac@mathematica-mpr.com"
             },
-            "describedBy": "https://data.cms.gov/resources/deficit-reduction-act-dra-hospital-acquired-condition-hac-measures-data-dictionary",
             "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/deficit-reduction-act-dra-hospital-acquired-condition-hac-measures-data-dictionary",
             "description": "The Publicly Reported Deficit Reduction Act (DRA) Hospital-Acquired Condition (HAC) Measures data provides information on hospital-level measures rates for four of the HACs included in the DRA HAC payment provision \u2013 foreign object retained after surgery, blood incompatibility, air embolism, and falls and trauma \u2013 for Medicare fee-for-service discharges. The Publicly Reported DRA HAC Measures are reported only for informational and quality improvement purposes; the results of the measure calculations do not affect payment and are not a part of the HAC Reduction Program.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/01edb62e-5c45-4f43-8c91-16cba21cbb74/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/01edb62e-5c45-4f43-8c91-16cba21cbb74",
                     "description": "latest",
-                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2024-01-01",
+                    "format": "API",
                     "modified": "2024-08-29",
-                    "temporal": "2024-01-01/2024-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/01edb62e-5c45-4f43-8c91-16cba21cbb74",
+                    "temporal": "2024-01-01/2024-12-31",
+                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2024-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/17fde1a0-9199-422c-8d6c-f9155ff47efb/HAC_MEASURE_PROVIDER_FILE_2024.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4992c1c4-db78-466c-93cc-b796076e9686",
-                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2024-01-01",
                     "modified": "2024-08-29",
-                    "temporal": "2024-01-01/2024-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4992c1c4-db78-466c-93cc-b796076e9686",
+                    "temporal": "2024-01-01/2024-12-31",
+                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2024-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/4992c1c4-db78-466c-93cc-b796076e9686/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4992c1c4-db78-466c-93cc-b796076e9686",
-                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2024-01-01",
+                    "format": "API",
                     "modified": "2024-08-29",
-                    "temporal": "2024-01-01/2024-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4992c1c4-db78-466c-93cc-b796076e9686",
+                    "temporal": "2024-01-01/2024-12-31",
+                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2024-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/116deee9-20d3-48a4-96e8-80cf7480510e/HAC_MEASURE_PROVIDER_FILE_2023.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a15892f9-ee64-4fb6-9436-a11ad00a01b8",
-                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2023-01-01",
                     "modified": "2023-08-29",
-                    "temporal": "2023-01-01/2023-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a15892f9-ee64-4fb6-9436-a11ad00a01b8",
+                    "temporal": "2023-01-01/2023-12-31",
+                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2023-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/a15892f9-ee64-4fb6-9436-a11ad00a01b8/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a15892f9-ee64-4fb6-9436-a11ad00a01b8",
-                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2023-01-01",
+                    "format": "API",
                     "modified": "2023-08-29",
-                    "temporal": "2023-01-01/2023-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a15892f9-ee64-4fb6-9436-a11ad00a01b8",
+                    "temporal": "2023-01-01/2023-12-31",
+                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2023-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-09/fb709238-ba0b-41b6-9654-89ad88117283/HAC_MEASURE_PROVIDER_FILE_2022.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/dca0e636-de68-4902-af94-0ec30b3f2894",
-                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2022-12-31",
                     "modified": "2022-09-26",
-                    "temporal": "2022-01-01/2022-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/dca0e636-de68-4902-af94-0ec30b3f2894",
+                    "temporal": "2022-01-01/2022-12-31",
+                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2022-12-31"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/dca0e636-de68-4902-af94-0ec30b3f2894/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/dca0e636-de68-4902-af94-0ec30b3f2894",
-                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2022-12-31",
+                    "format": "API",
                     "modified": "2022-09-26",
-                    "temporal": "2022-01-01/2022-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/dca0e636-de68-4902-af94-0ec30b3f2894",
+                    "temporal": "2022-01-01/2022-12-31",
+                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2022-12-31"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2021-09/60484f55-da92-4172-b00d-d8b5582eea44/HAC_MEASURE_PROVIDER_FILE_2021.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3d467162-df90-46f1-801b-6d5fc796521c",
-                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2021-12-31",
                     "modified": "2021-09-20",
-                    "temporal": "2021-01-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3d467162-df90-46f1-801b-6d5fc796521c",
+                    "temporal": "2021-01-01/2021-12-31",
+                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2021-12-31"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/3d467162-df90-46f1-801b-6d5fc796521c/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3d467162-df90-46f1-801b-6d5fc796521c",
-                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2021-12-31",
+                    "format": "API",
                     "modified": "2021-09-20",
-                    "temporal": "2021-01-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3d467162-df90-46f1-801b-6d5fc796521c",
+                    "temporal": "2021-01-01/2021-12-31",
+                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2021-12-31"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2020-09/Deficit_Reduction_Act__DRA__Hospital-Acquired_Condition__HAC__Provider-Level_Measure_Rates_for_Four_Conditions_-_2020.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e44ef8de-3ac4-451a-bc92-5aae04aeed41",
-                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2020-08-12",
                     "modified": "2021-05-20",
-                    "temporal": "2020-01-01/2020-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e44ef8de-3ac4-451a-bc92-5aae04aeed41",
+                    "temporal": "2020-01-01/2020-12-31",
+                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2020-08-12"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/e44ef8de-3ac4-451a-bc92-5aae04aeed41/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e44ef8de-3ac4-451a-bc92-5aae04aeed41",
-                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2020-08-12",
+                    "format": "API",
                     "modified": "2021-05-20",
-                    "temporal": "2020-01-01/2020-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e44ef8de-3ac4-451a-bc92-5aae04aeed41",
+                    "temporal": "2020-01-01/2020-12-31",
+                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2020-08-12"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2020-09/Deficit_Reduction_Act__DRA__Hospital-Acquired_Condition__HAC__Provider-Level_Measure_Rates_for_Four_Conditions_-_2019.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3c2e3f06-2be2-49f0-92e4-0dc48b880746",
-                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2019-07-31",
                     "modified": "2020-10-08",
-                    "temporal": "2019-01-01/2019-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3c2e3f06-2be2-49f0-92e4-0dc48b880746",
+                    "temporal": "2019-01-01/2019-12-31",
+                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2019-07-31"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/3c2e3f06-2be2-49f0-92e4-0dc48b880746/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3c2e3f06-2be2-49f0-92e4-0dc48b880746",
-                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2019-07-31",
+                    "format": "API",
                     "modified": "2020-10-08",
-                    "temporal": "2019-01-01/2019-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3c2e3f06-2be2-49f0-92e4-0dc48b880746",
+                    "temporal": "2019-01-01/2019-12-31",
+                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2019-07-31"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2020-09/Deficit_Reduction_Act__DRA__Hospital-Acquired_Condition__HAC__Provider-Level_Measure_Rates_for_Four_Conditions_-_2018.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/705b4fb5-1f6f-4d66-86c5-4acc3bf74218",
-                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2018-08-22",
                     "modified": "2020-10-08",
-                    "temporal": "2018-01-01/2018-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/705b4fb5-1f6f-4d66-86c5-4acc3bf74218",
+                    "temporal": "2018-01-01/2018-12-31",
+                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2018-08-22"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/705b4fb5-1f6f-4d66-86c5-4acc3bf74218/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/705b4fb5-1f6f-4d66-86c5-4acc3bf74218",
-                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2018-08-22",
+                    "format": "API",
                     "modified": "2020-10-08",
-                    "temporal": "2018-01-01/2018-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/705b4fb5-1f6f-4d66-86c5-4acc3bf74218",
+                    "temporal": "2018-01-01/2018-12-31",
+                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2018-08-22"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2020-09/Deficit_Reduction_Act__DRA__Hospital-Acquired_Condition__HAC__Provider-Level_Measure_Rates_for_Four_Conditions_-_2017.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6dcdc8a1-8dab-4a89-ae1d-bbb324cba3f8",
-                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2017-08-07",
                     "modified": "2020-10-08",
-                    "temporal": "2017-01-01/2017-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6dcdc8a1-8dab-4a89-ae1d-bbb324cba3f8",
+                    "temporal": "2017-01-01/2017-12-31",
+                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2017-08-07"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/6dcdc8a1-8dab-4a89-ae1d-bbb324cba3f8/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6dcdc8a1-8dab-4a89-ae1d-bbb324cba3f8",
-                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2017-08-07",
+                    "format": "API",
                     "modified": "2020-10-08",
-                    "temporal": "2017-01-01/2017-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6dcdc8a1-8dab-4a89-ae1d-bbb324cba3f8",
+                    "temporal": "2017-01-01/2017-12-31",
+                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2017-08-07"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2020-09/Deficit_Reduction_Act__DRA__Hospital-Acquired_Condition__HAC__Provider-Level_Measure_Rates_for_Four_Conditions_-_2016.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/94c8f101-e873-4688-85a5-3e2ecd9ce320",
-                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2016-07-29",
                     "modified": "2020-10-08",
-                    "temporal": "2016-01-01/2016-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/94c8f101-e873-4688-85a5-3e2ecd9ce320",
+                    "temporal": "2016-01-01/2016-12-31",
+                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2016-07-29"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/94c8f101-e873-4688-85a5-3e2ecd9ce320/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/94c8f101-e873-4688-85a5-3e2ecd9ce320",
-                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2016-07-29",
+                    "format": "API",
                     "modified": "2020-10-08",
-                    "temporal": "2016-01-01/2016-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/94c8f101-e873-4688-85a5-3e2ecd9ce320",
+                    "temporal": "2016-01-01/2016-12-31",
+                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2016-07-29"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2020-09/Deficit_Reduction_Act__DRA__Hospital-Acquired_Condition__HAC__Provider-Level_Measure_Rates_for_Four_Conditions.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d5c2ce96-a45a-4205-8f1a-597d7d3b6557",
-                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2015-08-16",
                     "modified": "2020-10-08",
-                    "temporal": "2015-01-01/2015-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d5c2ce96-a45a-4205-8f1a-597d7d3b6557",
+                    "temporal": "2015-01-01/2015-12-31",
+                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2015-08-16"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/d5c2ce96-a45a-4205-8f1a-597d7d3b6557/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d5c2ce96-a45a-4205-8f1a-597d7d3b6557",
-                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2015-08-16",
+                    "format": "API",
                     "modified": "2020-10-08",
-                    "temporal": "2015-01-01/2015-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d5c2ce96-a45a-4205-8f1a-597d7d3b6557",
+                    "temporal": "2015-01-01/2015-12-31",
+                    "title": "Deficit Reduction Act Hospital-Acquired Condition Measures : 2015-08-16"
                 }
             ],
             "identifier": "https://data.cms.gov/data-api/v1/dataset/01edb62e-5c45-4f43-8c91-16cba21cbb74/data-viewer",
@@ -4319,91 +4318,91 @@
                 "fn": "ETC Model - CMMI",
                 "hasEmail": "mailto:ETC-CMMI@cms.hhs.gov"
             },
-            "describedBy": "https://data.cms.gov/resources/esrd-facility-aggregation-group-performance-data-dictionary",
             "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/esrd-facility-aggregation-group-performance-data-dictionary",
             "description": "The End-Stage Renal Disease (ESRD) Facility Aggregation Group Performance dataset provides performance information in the End-Stage Renal Disease (ESRD) Treatment Choices (ETC) Model. The dataset includes information on Performance Payment Adjustment (PPA), Modality Performance Score (MPS), home dialysis rate, and transplant rate, as well as the individual components of each rate for each model participant ESRD facility aggregation group.\n\n\u00a0\n\nAll ESRD facilities\u00a0within the same aggregation group share the same performance information. The supplementary aggregation group crosswalk file may be used to map aggregation groups to individual ETC Participant ESRD facilities.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/4bae4223-a1dc-4b9c-bd7e-d9622461be35/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4bae4223-a1dc-4b9c-bd7e-d9622461be35",
                     "description": "latest",
-                    "title": "End-Stage Renal Disease Facility Aggregation Group Performance : 2023-06-01",
+                    "format": "API",
                     "modified": "2024-08-09",
-                    "temporal": "2023-06-01/2023-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4bae4223-a1dc-4b9c-bd7e-d9622461be35",
+                    "temporal": "2023-06-01/2023-06-30",
+                    "title": "End-Stage Renal Disease Facility Aggregation Group Performance : 2023-06-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/245da9ee-780e-41d3-8262-55a3c93c7f4a/ETC-MY4-DF-ModelDetailedResults.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e06cdea4-526d-436b-815e-612c22cec061",
-                    "title": "End-Stage Renal Disease Facility Aggregation Group Performance : 2023-06-01",
                     "modified": "2024-08-09",
-                    "temporal": "2023-06-01/2023-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e06cdea4-526d-436b-815e-612c22cec061",
+                    "temporal": "2023-06-01/2023-06-30",
+                    "title": "End-Stage Renal Disease Facility Aggregation Group Performance : 2023-06-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/e06cdea4-526d-436b-815e-612c22cec061/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e06cdea4-526d-436b-815e-612c22cec061",
-                    "title": "End-Stage Renal Disease Facility Aggregation Group Performance : 2023-06-01",
+                    "format": "API",
                     "modified": "2024-08-09",
-                    "temporal": "2023-06-01/2023-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e06cdea4-526d-436b-815e-612c22cec061",
+                    "temporal": "2023-06-01/2023-06-30",
+                    "title": "End-Stage Renal Disease Facility Aggregation Group Performance : 2023-06-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/de6e1f2d-3744-4959-ac06-befff5370f9f/ETC-MY3-DF-ModelDetailedResults.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f56b3953-76ba-4b3a-a76a-725ac6a78ae7",
-                    "title": "End-Stage Renal Disease Facility Aggregation Group Performance : 2022-12-31",
                     "modified": "2024-02-20",
-                    "temporal": "2022-12-01/2022-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f56b3953-76ba-4b3a-a76a-725ac6a78ae7",
+                    "temporal": "2022-12-01/2022-12-31",
+                    "title": "End-Stage Renal Disease Facility Aggregation Group Performance : 2022-12-31"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/f56b3953-76ba-4b3a-a76a-725ac6a78ae7/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f56b3953-76ba-4b3a-a76a-725ac6a78ae7",
-                    "title": "End-Stage Renal Disease Facility Aggregation Group Performance : 2022-12-31",
+                    "format": "API",
                     "modified": "2024-02-20",
-                    "temporal": "2022-12-01/2022-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f56b3953-76ba-4b3a-a76a-725ac6a78ae7",
+                    "temporal": "2022-12-01/2022-12-31",
+                    "title": "End-Stage Renal Disease Facility Aggregation Group Performance : 2022-12-31"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/edfa49cc-2565-4180-a418-87853dc650f1/ETC-MY2-DF-ModelDetailedResults.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a587a99b-4669-485d-99a5-68050ba8b3fe",
-                    "title": "End-Stage Renal Disease Facility Aggregation Group Performance : 2022-06-30",
                     "modified": "2023-11-30",
-                    "temporal": "2022-06-01/2022-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a587a99b-4669-485d-99a5-68050ba8b3fe",
+                    "temporal": "2022-06-01/2022-06-30",
+                    "title": "End-Stage Renal Disease Facility Aggregation Group Performance : 2022-06-30"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/a587a99b-4669-485d-99a5-68050ba8b3fe/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a587a99b-4669-485d-99a5-68050ba8b3fe",
-                    "title": "End-Stage Renal Disease Facility Aggregation Group Performance : 2022-06-30",
+                    "format": "API",
                     "modified": "2023-11-30",
-                    "temporal": "2022-06-01/2022-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a587a99b-4669-485d-99a5-68050ba8b3fe",
+                    "temporal": "2022-06-01/2022-06-30",
+                    "title": "End-Stage Renal Disease Facility Aggregation Group Performance : 2022-06-30"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/ETC-MY1-DF-ModelDetailedResults.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ef13fb2d-d276-42c5-8c81-400cfcb089e5",
-                    "title": "End-Stage Renal Disease Facility Aggregation Group Performance : 2021-12-31",
                     "modified": "2023-11-30",
-                    "temporal": "2021-12-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ef13fb2d-d276-42c5-8c81-400cfcb089e5",
+                    "temporal": "2021-12-01/2021-12-31",
+                    "title": "End-Stage Renal Disease Facility Aggregation Group Performance : 2021-12-31"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/ef13fb2d-d276-42c5-8c81-400cfcb089e5/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ef13fb2d-d276-42c5-8c81-400cfcb089e5",
-                    "title": "End-Stage Renal Disease Facility Aggregation Group Performance : 2021-12-31",
+                    "format": "API",
                     "modified": "2023-11-30",
-                    "temporal": "2021-12-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ef13fb2d-d276-42c5-8c81-400cfcb089e5",
+                    "temporal": "2021-12-01/2021-12-31",
+                    "title": "End-Stage Renal Disease Facility Aggregation Group Performance : 2021-12-31"
                 }
             ],
             "identifier": "https://data.cms.gov/data-api/v1/dataset/4bae4223-a1dc-4b9c-bd7e-d9622461be35/data-viewer",
@@ -4452,91 +4451,91 @@
                 "fn": "NH Facility - CCSQ",
                 "hasEmail": "mailto:NursingHomeData@cms.hhs.gov"
             },
-            "describedBy": "https://data.cms.gov/resources/facility-level-minimum-data-set-frequency-data-dictionary",
             "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/facility-level-minimum-data-set-frequency-data-dictionary",
             "description": "The Facility-Level Minimum Data Set (MDS) Frequency\u00a0dataset provides information for active nursing home residents on topics, such as race/ethnicity, age, or marital status; discharge dispositions; hearing, speech, and vision; cognitive patterns; mood; functional abilities and goals; bladder and bowel; active diagnoses; health conditions; swallowing/nutritional status; oral/dental status; skin conditions; medications; special treatments, procedures, and programs; restraints and alarms; and participation in assessment and goal setting.\n\n\u00a0\n\nNote: The MDS dataset contains more records than most spreadsheet programs can handle. The use of a database or statistical software is generally required. The dataset can be filtered to a more manageable size for use in a spreadsheet program by clicking on the \u201cView Data\u201d button. Additional filter information can be found in the methodology, if needed.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/d086edc0-4953-4fb9-a663-b35526371add/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d086edc0-4953-4fb9-a663-b35526371add",
                     "description": "latest",
-                    "title": "Facility-Level Minimum Data Set Frequency : 2024-07-01",
+                    "format": "API",
                     "modified": "2024-11-04",
-                    "temporal": "2024-07-01/2024-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d086edc0-4953-4fb9-a663-b35526371add",
+                    "temporal": "2024-07-01/2024-09-30",
+                    "title": "Facility-Level Minimum Data Set Frequency : 2024-07-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/05c9444c-b7ac-4bcd-8efa-e266222c5670/MDS_Facility_Level_2024_Q3.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/184a3e9c-6757-4cb1-ba98-4fd43803c557",
-                    "title": "Facility-Level Minimum Data Set Frequency : 2024-07-01",
                     "modified": "2024-11-04",
-                    "temporal": "2024-07-01/2024-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/184a3e9c-6757-4cb1-ba98-4fd43803c557",
+                    "temporal": "2024-07-01/2024-09-30",
+                    "title": "Facility-Level Minimum Data Set Frequency : 2024-07-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/184a3e9c-6757-4cb1-ba98-4fd43803c557/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/184a3e9c-6757-4cb1-ba98-4fd43803c557",
-                    "title": "Facility-Level Minimum Data Set Frequency : 2024-07-01",
+                    "format": "API",
                     "modified": "2024-11-04",
-                    "temporal": "2024-07-01/2024-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/184a3e9c-6757-4cb1-ba98-4fd43803c557",
+                    "temporal": "2024-07-01/2024-09-30",
+                    "title": "Facility-Level Minimum Data Set Frequency : 2024-07-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/16d52e37-246c-4c49-aaf3-ed5aae90c364/MDS_Facility_Level_2024_Q2.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/450425c3-5b81-454e-88b7-9902739ecb12",
-                    "title": "Facility-Level Minimum Data Set Frequency : 2024-04-01",
                     "modified": "2024-11-04",
-                    "temporal": "2024-04-01/2024-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/450425c3-5b81-454e-88b7-9902739ecb12",
+                    "temporal": "2024-04-01/2024-06-30",
+                    "title": "Facility-Level Minimum Data Set Frequency : 2024-04-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/450425c3-5b81-454e-88b7-9902739ecb12/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/450425c3-5b81-454e-88b7-9902739ecb12",
-                    "title": "Facility-Level Minimum Data Set Frequency : 2024-04-01",
+                    "format": "API",
                     "modified": "2024-11-04",
-                    "temporal": "2024-04-01/2024-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/450425c3-5b81-454e-88b7-9902739ecb12",
+                    "temporal": "2024-04-01/2024-06-30",
+                    "title": "Facility-Level Minimum Data Set Frequency : 2024-04-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/3a7ea82a-8869-4760-9123-7d536cdce951/MDS_Facility_Level_2024_Q1_Final.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f6a42f70-af9a-497f-91eb-ddc9dd89c6a9",
-                    "title": "Facility-Level Minimum Data Set Frequency : 2024-01-02",
                     "modified": "2024-08-01",
-                    "temporal": "2024-01-01/2024-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f6a42f70-af9a-497f-91eb-ddc9dd89c6a9",
+                    "temporal": "2024-01-01/2024-03-31",
+                    "title": "Facility-Level Minimum Data Set Frequency : 2024-01-02"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/f6a42f70-af9a-497f-91eb-ddc9dd89c6a9/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f6a42f70-af9a-497f-91eb-ddc9dd89c6a9",
-                    "title": "Facility-Level Minimum Data Set Frequency : 2024-01-02",
+                    "format": "API",
                     "modified": "2024-08-01",
-                    "temporal": "2024-01-01/2024-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f6a42f70-af9a-497f-91eb-ddc9dd89c6a9",
+                    "temporal": "2024-01-01/2024-03-31",
+                    "title": "Facility-Level Minimum Data Set Frequency : 2024-01-02"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/97a6f62e-eb7c-4921-90f3-09321c683379/MDS_Facility_Level_2023_Q4_Final.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/460c94f3-7f7f-4a3e-bd25-33ad8343a66e",
-                    "title": "Facility-Level Minimum Data Set Frequency : 2023-12-01",
                     "modified": "2024-07-31",
-                    "temporal": "2023-10-01/2023-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/460c94f3-7f7f-4a3e-bd25-33ad8343a66e",
+                    "temporal": "2023-10-01/2023-12-31",
+                    "title": "Facility-Level Minimum Data Set Frequency : 2023-12-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/460c94f3-7f7f-4a3e-bd25-33ad8343a66e/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/460c94f3-7f7f-4a3e-bd25-33ad8343a66e",
-                    "title": "Facility-Level Minimum Data Set Frequency : 2023-12-01",
+                    "format": "API",
                     "modified": "2024-07-31",
-                    "temporal": "2023-10-01/2023-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/460c94f3-7f7f-4a3e-bd25-33ad8343a66e",
+                    "temporal": "2023-10-01/2023-12-31",
+                    "title": "Facility-Level Minimum Data Set Frequency : 2023-12-01"
                 }
             ],
             "identifier": "https://data.cms.gov/data-api/v1/dataset/d086edc0-4953-4fb9-a663-b35526371add/data-viewer",
@@ -4579,128 +4578,128 @@
                 "fn": "Provider Enrollment Data Requests - CPI",
                 "hasEmail": "mailto:ProviderEnrollmentDataRequests@cms.hhs.gov"
             },
+            "dataQuality": true,
             "describedBy": "https://data.cms.gov/sites/default/files/2024-10/FQHC_All_Owners_Data_Dictionary.pdf",
             "describedByType": "application/pdf",
-            "dataQuality": true,
             "description": "The\u00a0Federally Qualified Health Center (FQHC) All Owners dataset provides ownership information on all\u00a0FQHCs currently enrolled in Medicare. This data includes ownership information such as ownership name, ownership type, ownership address and ownership effective date.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/ed289c89-0bb8-4221-a20a-85776066381b/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ed289c89-0bb8-4221-a20a-85776066381b",
                     "description": "latest",
-                    "title": "Federally Qualified Health Center All Owners : 2025-01-01",
+                    "format": "API",
                     "modified": "2025-01-15",
-                    "temporal": "2025-01-01/2025-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ed289c89-0bb8-4221-a20a-85776066381b",
+                    "temporal": "2025-01-01/2025-03-31",
+                    "title": "Federally Qualified Health Center All Owners : 2025-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/02441a9f-3380-4438-a1a0-be365d433ed9/FQHC_All_Owners_2025.01.02.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6e1ca8c8-5d98-449a-a7b1-8b29b995f904",
-                    "title": "Federally Qualified Health Center All Owners : 2025-01-01",
                     "modified": "2025-01-15",
-                    "temporal": "2025-01-01/2025-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6e1ca8c8-5d98-449a-a7b1-8b29b995f904",
+                    "temporal": "2025-01-01/2025-03-31",
+                    "title": "Federally Qualified Health Center All Owners : 2025-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/6e1ca8c8-5d98-449a-a7b1-8b29b995f904/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6e1ca8c8-5d98-449a-a7b1-8b29b995f904",
-                    "title": "Federally Qualified Health Center All Owners : 2025-01-01",
+                    "format": "API",
                     "modified": "2025-01-15",
-                    "temporal": "2025-01-01/2025-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6e1ca8c8-5d98-449a-a7b1-8b29b995f904",
+                    "temporal": "2025-01-01/2025-03-31",
+                    "title": "Federally Qualified Health Center All Owners : 2025-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/cfc8ade9-53a2-4ffe-9564-5ef4c5fdb322/FQHC_All_Owners_2024.10.07.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c6a864cc-5dde-417a-825b-823e8b6a5d03",
-                    "title": "Federally Qualified Health Center All Owners : 2024-10-01",
                     "modified": "2024-10-15",
-                    "temporal": "2024-10-01/2024-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c6a864cc-5dde-417a-825b-823e8b6a5d03",
+                    "temporal": "2024-10-01/2024-12-31",
+                    "title": "Federally Qualified Health Center All Owners : 2024-10-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/c6a864cc-5dde-417a-825b-823e8b6a5d03/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c6a864cc-5dde-417a-825b-823e8b6a5d03",
-                    "title": "Federally Qualified Health Center All Owners : 2024-10-01",
+                    "format": "API",
                     "modified": "2024-10-15",
-                    "temporal": "2024-10-01/2024-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c6a864cc-5dde-417a-825b-823e8b6a5d03",
+                    "temporal": "2024-10-01/2024-12-31",
+                    "title": "Federally Qualified Health Center All Owners : 2024-10-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/6b07ca66-1191-4e63-87bf-3cbf637ad83f/FQHC_All_Owners_2024.07.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b9eb73e8-7fdc-421a-9e02-4a4112ef7620",
-                    "title": "Federally Qualified Health Center All Owners : 2024-07-01",
                     "modified": "2024-07-15",
-                    "temporal": "2024-07-01/2024-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b9eb73e8-7fdc-421a-9e02-4a4112ef7620",
+                    "temporal": "2024-07-01/2024-09-30",
+                    "title": "Federally Qualified Health Center All Owners : 2024-07-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/b9eb73e8-7fdc-421a-9e02-4a4112ef7620/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b9eb73e8-7fdc-421a-9e02-4a4112ef7620",
-                    "title": "Federally Qualified Health Center All Owners : 2024-07-01",
+                    "format": "API",
                     "modified": "2024-07-15",
-                    "temporal": "2024-07-01/2024-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b9eb73e8-7fdc-421a-9e02-4a4112ef7620",
+                    "temporal": "2024-07-01/2024-09-30",
+                    "title": "Federally Qualified Health Center All Owners : 2024-07-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/26a82e11-1986-48e5-92f3-74033409217b/FQHC_All_Owners_2024.04.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c8bfbf21-82fb-4100-a904-55595ace6745",
-                    "title": "Federally Qualified Health Center All Owners : 2024-04-01",
                     "modified": "2024-04-15",
-                    "temporal": "2024-04-01/2024-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c8bfbf21-82fb-4100-a904-55595ace6745",
+                    "temporal": "2024-04-01/2024-06-30",
+                    "title": "Federally Qualified Health Center All Owners : 2024-04-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/c8bfbf21-82fb-4100-a904-55595ace6745/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c8bfbf21-82fb-4100-a904-55595ace6745",
-                    "title": "Federally Qualified Health Center All Owners : 2024-04-01",
+                    "format": "API",
                     "modified": "2024-04-15",
-                    "temporal": "2024-04-01/2024-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c8bfbf21-82fb-4100-a904-55595ace6745",
+                    "temporal": "2024-04-01/2024-06-30",
+                    "title": "Federally Qualified Health Center All Owners : 2024-04-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/48691aa9-36d1-4e10-87db-f69ad84aaf0b/FQHC_All_Owners_2024.01.05.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c0f15553-d8e3-4cec-a543-344dc16b710a",
-                    "title": "Federally Qualified Health Center All Owners : 2024-01-05",
                     "modified": "2024-01-19",
-                    "temporal": "2024-01-01/2024-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c0f15553-d8e3-4cec-a543-344dc16b710a",
+                    "temporal": "2024-01-01/2024-03-31",
+                    "title": "Federally Qualified Health Center All Owners : 2024-01-05"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/c0f15553-d8e3-4cec-a543-344dc16b710a/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c0f15553-d8e3-4cec-a543-344dc16b710a",
-                    "title": "Federally Qualified Health Center All Owners : 2024-01-05",
+                    "format": "API",
                     "modified": "2024-01-19",
-                    "temporal": "2024-01-01/2024-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c0f15553-d8e3-4cec-a543-344dc16b710a",
+                    "temporal": "2024-01-01/2024-03-31",
+                    "title": "Federally Qualified Health Center All Owners : 2024-01-05"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/138ec038-3e83-4355-9d6e-274e9d481833/FQHC_All_Owners_2023.11.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/02138ebf-9179-40e4-af52-487274dc982f",
-                    "title": "Federally Qualified Health Center All Owners : 2023-10-28",
                     "modified": "2023-12-07",
-                    "temporal": "2023-10-01/2023-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/02138ebf-9179-40e4-af52-487274dc982f",
+                    "temporal": "2023-10-01/2023-12-31",
+                    "title": "Federally Qualified Health Center All Owners : 2023-10-28"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/02138ebf-9179-40e4-af52-487274dc982f/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/02138ebf-9179-40e4-af52-487274dc982f",
-                    "title": "Federally Qualified Health Center All Owners : 2023-10-28",
+                    "format": "API",
                     "modified": "2023-12-07",
-                    "temporal": "2023-10-01/2023-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/02138ebf-9179-40e4-af52-487274dc982f",
+                    "temporal": "2023-10-01/2023-12-31",
+                    "title": "Federally Qualified Health Center All Owners : 2023-10-28"
                 }
             ],
             "identifier": "https://data.cms.gov/data-api/v1/dataset/ed289c89-0bb8-4221-a20a-85776066381b/data-viewer",
@@ -4745,128 +4744,128 @@
                 "fn": "Provider Enrollment Data Requests - CPI",
                 "hasEmail": "mailto:ProviderEnrollmentDataRequests@cms.hhs.gov"
             },
+            "dataQuality": true,
             "describedBy": "https://data.cms.gov/sites/default/files/2023-09/FQHC_Enrollments_Data_Dictionary.pdf",
             "describedByType": "application/pdf",
-            "dataQuality": true,
             "description": "The Federally Qualified Health Center (FQHC) Enrollments dataset provides enrollment information on all FQHCs currently enrolled in Medicare. This data includes information on the FQHC's legal business name, doing business as name, organization type, and address.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/4bcae866-3411-439a-b762-90a6187c194b/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4bcae866-3411-439a-b762-90a6187c194b",
                     "description": "latest",
-                    "title": "Federally Qualified Health Center Enrollments : 2025-01-01",
+                    "format": "API",
                     "modified": "2025-01-15",
-                    "temporal": "2025-01-01/2025-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4bcae866-3411-439a-b762-90a6187c194b",
+                    "temporal": "2025-01-01/2025-03-31",
+                    "title": "Federally Qualified Health Center Enrollments : 2025-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/472db45d-c7ce-4b0b-8251-0470e625e521/FQHC_Enrollments_2025.01.02.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/376a6172-0b62-4c47-88bb-9c9732ea42eb",
-                    "title": "Federally Qualified Health Center Enrollments : 2025-01-01",
                     "modified": "2025-01-15",
-                    "temporal": "2025-01-01/2025-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/376a6172-0b62-4c47-88bb-9c9732ea42eb",
+                    "temporal": "2025-01-01/2025-03-31",
+                    "title": "Federally Qualified Health Center Enrollments : 2025-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/376a6172-0b62-4c47-88bb-9c9732ea42eb/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/376a6172-0b62-4c47-88bb-9c9732ea42eb",
-                    "title": "Federally Qualified Health Center Enrollments : 2025-01-01",
+                    "format": "API",
                     "modified": "2025-01-15",
-                    "temporal": "2025-01-01/2025-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/376a6172-0b62-4c47-88bb-9c9732ea42eb",
+                    "temporal": "2025-01-01/2025-03-31",
+                    "title": "Federally Qualified Health Center Enrollments : 2025-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/aaa3ac6d-2ce2-4fd5-9708-9e88a3fd1ebf/FQHC_Enrollments_2024.10.07.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1c2ec7dd-56c1-4b04-ba73-dcc978049181",
-                    "title": "Federally Qualified Health Center Enrollments : 2024-10-01",
                     "modified": "2024-10-15",
-                    "temporal": "2024-10-01/2024-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1c2ec7dd-56c1-4b04-ba73-dcc978049181",
+                    "temporal": "2024-10-01/2024-12-31",
+                    "title": "Federally Qualified Health Center Enrollments : 2024-10-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/1c2ec7dd-56c1-4b04-ba73-dcc978049181/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1c2ec7dd-56c1-4b04-ba73-dcc978049181",
-                    "title": "Federally Qualified Health Center Enrollments : 2024-10-01",
+                    "format": "API",
                     "modified": "2024-10-15",
-                    "temporal": "2024-10-01/2024-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1c2ec7dd-56c1-4b04-ba73-dcc978049181",
+                    "temporal": "2024-10-01/2024-12-31",
+                    "title": "Federally Qualified Health Center Enrollments : 2024-10-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/bbfda66b-17f2-4f9f-b925-a04ade860d03/FQHC_Enrollments_2024.07.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/81be797a-03bd-4498-92a0-4ebeb4939030",
-                    "title": "Federally Qualified Health Center Enrollments : 2024-07-01",
                     "modified": "2024-07-15",
-                    "temporal": "2024-07-01/2024-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/81be797a-03bd-4498-92a0-4ebeb4939030",
+                    "temporal": "2024-07-01/2024-09-30",
+                    "title": "Federally Qualified Health Center Enrollments : 2024-07-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/81be797a-03bd-4498-92a0-4ebeb4939030/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/81be797a-03bd-4498-92a0-4ebeb4939030",
-                    "title": "Federally Qualified Health Center Enrollments : 2024-07-01",
+                    "format": "API",
                     "modified": "2024-07-15",
-                    "temporal": "2024-07-01/2024-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/81be797a-03bd-4498-92a0-4ebeb4939030",
+                    "temporal": "2024-07-01/2024-09-30",
+                    "title": "Federally Qualified Health Center Enrollments : 2024-07-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/eeb6e419-6f57-41d6-97d3-3f57aca24efc/FQHC_Enrollments_2024.04.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fee5c58a-9c36-421f-970b-80f5efca33d3",
-                    "title": "Federally Qualified Health Center Enrollments : 2024-04-01",
                     "modified": "2024-04-15",
-                    "temporal": "2024-04-01/2024-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fee5c58a-9c36-421f-970b-80f5efca33d3",
+                    "temporal": "2024-04-01/2024-06-30",
+                    "title": "Federally Qualified Health Center Enrollments : 2024-04-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/fee5c58a-9c36-421f-970b-80f5efca33d3/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fee5c58a-9c36-421f-970b-80f5efca33d3",
-                    "title": "Federally Qualified Health Center Enrollments : 2024-04-01",
+                    "format": "API",
                     "modified": "2024-04-15",
-                    "temporal": "2024-04-01/2024-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fee5c58a-9c36-421f-970b-80f5efca33d3",
+                    "temporal": "2024-04-01/2024-06-30",
+                    "title": "Federally Qualified Health Center Enrollments : 2024-04-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/ccc48ded-e404-491a-bbbb-7983ce547417/FQHC_Enrollments_2024.01.05.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/dc4defb6-1b1d-4b49-8188-1718c96c7f85",
-                    "title": "Federally Qualified Health Center Enrollments : 2024-01-05",
                     "modified": "2024-01-19",
-                    "temporal": "2024-01-01/2024-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/dc4defb6-1b1d-4b49-8188-1718c96c7f85",
+                    "temporal": "2024-01-01/2024-03-31",
+                    "title": "Federally Qualified Health Center Enrollments : 2024-01-05"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/dc4defb6-1b1d-4b49-8188-1718c96c7f85/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/dc4defb6-1b1d-4b49-8188-1718c96c7f85",
-                    "title": "Federally Qualified Health Center Enrollments : 2024-01-05",
+                    "format": "API",
                     "modified": "2024-01-19",
-                    "temporal": "2024-01-01/2024-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/dc4defb6-1b1d-4b49-8188-1718c96c7f85",
+                    "temporal": "2024-01-01/2024-03-31",
+                    "title": "Federally Qualified Health Center Enrollments : 2024-01-05"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/e8963e3f-f1cd-4709-86e4-a74b9a1ca694/FQHC_Enrollments_2023.11.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ba0c506c-a269-402d-baa9-4941b36c71b1",
-                    "title": "Federally Qualified Health Center Enrollments : 2023-10-28",
                     "modified": "2023-12-07",
-                    "temporal": "2023-10-01/2023-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ba0c506c-a269-402d-baa9-4941b36c71b1",
+                    "temporal": "2023-10-01/2023-12-31",
+                    "title": "Federally Qualified Health Center Enrollments : 2023-10-28"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/ba0c506c-a269-402d-baa9-4941b36c71b1/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ba0c506c-a269-402d-baa9-4941b36c71b1",
-                    "title": "Federally Qualified Health Center Enrollments : 2023-10-28",
+                    "format": "API",
                     "modified": "2023-12-07",
-                    "temporal": "2023-10-01/2023-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ba0c506c-a269-402d-baa9-4941b36c71b1",
+                    "temporal": "2023-10-01/2023-12-31",
+                    "title": "Federally Qualified Health Center Enrollments : 2023-10-28"
                 }
             ],
             "identifier": "https://data.cms.gov/data-api/v1/dataset/4bcae866-3411-439a-b762-90a6187c194b/data-viewer",
@@ -4911,3097 +4910,3097 @@
                 "fn": "Provider Enrollment Data Requests - CPI",
                 "hasEmail": "mailto:ProviderEnrollmentDataRequests@cms.hhs.gov"
             },
-            "describedBy": "https://data.cms.gov/resources/fiscal-intermediary-shared-system-attending-and-rendering-data-dictionary",
             "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/fiscal-intermediary-shared-system-attending-and-rendering-data-dictionary",
             "description": "The Fiscal Intermediary Shared System (FISS) Attending and Rendering dataset provides a list of those attending and rendering physicians for the FISS. FISS edits require that the Line Item Rendering Physician information be transmitted when providers submit a combined claim. Claims that include both facility and professional components, need to report the rendering physician or other practitioner at the line level if it differs from the rendering physician/practitioner reported at the claim level.\n\n\u00a0\n\nNote: This full dataset contains more records than most spreadsheet programs can handle, which will result in an incomplete load of data. Use of a database or statistical software is required.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/75e8dcb2-78eb-4a7d-a377-9108441966db/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/75e8dcb2-78eb-4a7d-a377-9108441966db",
                     "description": "latest",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-21",
+                    "format": "API",
                     "modified": "2025-01-21",
-                    "temporal": "2025-01-12/2025-01-18"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/75e8dcb2-78eb-4a7d-a377-9108441966db",
+                    "temporal": "2025-01-12/2025-01-18",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-21"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/09f329ea-ac43-452b-9e01-6a0410170a2c/FISS_AR_20250121.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7eb8e1a2-573c-43cf-8b2e-92a02fc2af12",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-21",
                     "modified": "2025-01-21",
-                    "temporal": "2025-01-12/2025-01-18"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7eb8e1a2-573c-43cf-8b2e-92a02fc2af12",
+                    "temporal": "2025-01-12/2025-01-18",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-21"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/7eb8e1a2-573c-43cf-8b2e-92a02fc2af12/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7eb8e1a2-573c-43cf-8b2e-92a02fc2af12",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-21",
+                    "format": "API",
                     "modified": "2025-01-21",
-                    "temporal": "2025-01-12/2025-01-18"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7eb8e1a2-573c-43cf-8b2e-92a02fc2af12",
+                    "temporal": "2025-01-12/2025-01-18",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-21"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/474c5d07-9311-4ed0-a1be-cc86bb06edd3/FISS_AR_20250117.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f0acdba9-686b-4624-88ff-fd5b3da9a493",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-17",
                     "modified": "2025-01-17",
-                    "temporal": "2025-01-05/2025-01-11"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f0acdba9-686b-4624-88ff-fd5b3da9a493",
+                    "temporal": "2025-01-05/2025-01-11",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-17"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/f0acdba9-686b-4624-88ff-fd5b3da9a493/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f0acdba9-686b-4624-88ff-fd5b3da9a493",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-17",
+                    "format": "API",
                     "modified": "2025-01-17",
-                    "temporal": "2025-01-05/2025-01-11"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f0acdba9-686b-4624-88ff-fd5b3da9a493",
+                    "temporal": "2025-01-05/2025-01-11",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-17"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/83364b8c-b003-4aac-890d-929c5c3970c7/FISS_AR_20250113.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/45754bc3-7ec9-41ed-98bf-0b7ba533b9ab",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-14",
                     "modified": "2025-01-14",
-                    "temporal": "2025-01-05/2025-01-11"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/45754bc3-7ec9-41ed-98bf-0b7ba533b9ab",
+                    "temporal": "2025-01-05/2025-01-11",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-14"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/45754bc3-7ec9-41ed-98bf-0b7ba533b9ab/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/45754bc3-7ec9-41ed-98bf-0b7ba533b9ab",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-14",
+                    "format": "API",
                     "modified": "2025-01-14",
-                    "temporal": "2025-01-05/2025-01-11"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/45754bc3-7ec9-41ed-98bf-0b7ba533b9ab",
+                    "temporal": "2025-01-05/2025-01-11",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-14"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/00de2339-1960-4faf-8c0e-958d1d6588dd/FISS_AR_20250109.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/15fc4c7e-7b0d-4d40-9ee7-764617b88314",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-10",
                     "modified": "2025-01-10",
-                    "temporal": "2024-12-29/2025-01-04"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/15fc4c7e-7b0d-4d40-9ee7-764617b88314",
+                    "temporal": "2024-12-29/2025-01-04",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-10"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/15fc4c7e-7b0d-4d40-9ee7-764617b88314/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/15fc4c7e-7b0d-4d40-9ee7-764617b88314",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-10",
+                    "format": "API",
                     "modified": "2025-01-10",
-                    "temporal": "2024-12-29/2025-01-04"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/15fc4c7e-7b0d-4d40-9ee7-764617b88314",
+                    "temporal": "2024-12-29/2025-01-04",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-10"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/4343a52f-bcd4-4a7b-80df-62ae1843c5bc/FISS_AR_20250106.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/72c2f88a-119d-46e6-93a6-53f51df70322",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-07",
                     "modified": "2025-01-07",
-                    "temporal": "2024-12-29/2025-01-04"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/72c2f88a-119d-46e6-93a6-53f51df70322",
+                    "temporal": "2024-12-29/2025-01-04",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-07"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/72c2f88a-119d-46e6-93a6-53f51df70322/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/72c2f88a-119d-46e6-93a6-53f51df70322",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-07",
+                    "format": "API",
                     "modified": "2025-01-07",
-                    "temporal": "2024-12-29/2025-01-04"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/72c2f88a-119d-46e6-93a6-53f51df70322",
+                    "temporal": "2024-12-29/2025-01-04",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-07"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/2dc247ec-959e-404c-9429-3c9c89b2d29a/FISS_AR_20250102.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6690cab2-a02b-4e71-9f9e-217a8b1fa1c8",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-06",
                     "modified": "2025-01-06",
-                    "temporal": "2024-12-29/2025-01-04"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6690cab2-a02b-4e71-9f9e-217a8b1fa1c8",
+                    "temporal": "2024-12-29/2025-01-04",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-06"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/6690cab2-a02b-4e71-9f9e-217a8b1fa1c8/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6690cab2-a02b-4e71-9f9e-217a8b1fa1c8",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-06",
+                    "format": "API",
                     "modified": "2025-01-06",
-                    "temporal": "2024-12-29/2025-01-04"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6690cab2-a02b-4e71-9f9e-217a8b1fa1c8",
+                    "temporal": "2024-12-29/2025-01-04",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-06"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/426fa31d-24f7-4ec1-a27b-5616333e7bfb/FISS_AR_20241230.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b5fc06b1-1985-46aa-8d2d-e1b978b1ebe4",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-31",
                     "modified": "2024-12-31",
-                    "temporal": "2024-12-22/2024-12-28"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b5fc06b1-1985-46aa-8d2d-e1b978b1ebe4",
+                    "temporal": "2024-12-22/2024-12-28",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-31"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/b5fc06b1-1985-46aa-8d2d-e1b978b1ebe4/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b5fc06b1-1985-46aa-8d2d-e1b978b1ebe4",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-31",
+                    "format": "API",
                     "modified": "2024-12-31",
-                    "temporal": "2024-12-22/2024-12-28"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b5fc06b1-1985-46aa-8d2d-e1b978b1ebe4",
+                    "temporal": "2024-12-22/2024-12-28",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-31"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/dbad4a20-990e-4804-ac21-46e8d3ac1b33/FISS_AR_20241226.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a0ac8443-e8c3-488e-b723-bf38ca8fc5f0",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-30",
                     "modified": "2024-12-30",
-                    "temporal": "2024-12-22/2024-12-28"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a0ac8443-e8c3-488e-b723-bf38ca8fc5f0",
+                    "temporal": "2024-12-22/2024-12-28",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-30"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/a0ac8443-e8c3-488e-b723-bf38ca8fc5f0/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a0ac8443-e8c3-488e-b723-bf38ca8fc5f0",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-30",
+                    "format": "API",
                     "modified": "2024-12-30",
-                    "temporal": "2024-12-22/2024-12-28"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a0ac8443-e8c3-488e-b723-bf38ca8fc5f0",
+                    "temporal": "2024-12-22/2024-12-28",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-30"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/014325b1-1bb2-4f34-b322-b9021bb1f56f/FISS_AR_20241223.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b360845d-eae3-4075-9a22-c920d4ca5a28",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-23",
                     "modified": "2024-12-23",
-                    "temporal": "2024-12-15/2024-12-21"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b360845d-eae3-4075-9a22-c920d4ca5a28",
+                    "temporal": "2024-12-15/2024-12-21",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-23"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/b360845d-eae3-4075-9a22-c920d4ca5a28/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b360845d-eae3-4075-9a22-c920d4ca5a28",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-23",
+                    "format": "API",
                     "modified": "2024-12-23",
-                    "temporal": "2024-12-15/2024-12-21"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b360845d-eae3-4075-9a22-c920d4ca5a28",
+                    "temporal": "2024-12-15/2024-12-21",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-23"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/85e3eee3-b208-4f07-8afa-340859a8ced7/FISS_AR_20241219.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f4721857-9285-49df-9c50-59828c62e8f9",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-20",
                     "modified": "2024-12-20",
-                    "temporal": "2024-12-08/2024-12-14"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f4721857-9285-49df-9c50-59828c62e8f9",
+                    "temporal": "2024-12-08/2024-12-14",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-20"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/f4721857-9285-49df-9c50-59828c62e8f9/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f4721857-9285-49df-9c50-59828c62e8f9",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-20",
+                    "format": "API",
                     "modified": "2024-12-20",
-                    "temporal": "2024-12-08/2024-12-14"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f4721857-9285-49df-9c50-59828c62e8f9",
+                    "temporal": "2024-12-08/2024-12-14",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-20"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/d2c014ca-f2cf-40e2-9ee3-86403a7f5f4f/FISS_AR_20241216.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ec7ceec5-237f-43ae-a67b-d5a85e40eaec",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-17",
                     "modified": "2024-12-17",
-                    "temporal": "2024-12-08/2024-12-14"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ec7ceec5-237f-43ae-a67b-d5a85e40eaec",
+                    "temporal": "2024-12-08/2024-12-14",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-17"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/ec7ceec5-237f-43ae-a67b-d5a85e40eaec/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ec7ceec5-237f-43ae-a67b-d5a85e40eaec",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-17",
+                    "format": "API",
                     "modified": "2024-12-17",
-                    "temporal": "2024-12-08/2024-12-14"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ec7ceec5-237f-43ae-a67b-d5a85e40eaec",
+                    "temporal": "2024-12-08/2024-12-14",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-17"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/099bdb31-063f-4396-8bec-513f500f55c0/FISS_AR_20241212.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f2149601-fbaa-43eb-97ac-7078e0d980ed",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-13",
                     "modified": "2024-12-13",
-                    "temporal": "2024-12-01/2024-12-07"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f2149601-fbaa-43eb-97ac-7078e0d980ed",
+                    "temporal": "2024-12-01/2024-12-07",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-13"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/f2149601-fbaa-43eb-97ac-7078e0d980ed/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f2149601-fbaa-43eb-97ac-7078e0d980ed",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-13",
+                    "format": "API",
                     "modified": "2024-12-13",
-                    "temporal": "2024-12-01/2024-12-07"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f2149601-fbaa-43eb-97ac-7078e0d980ed",
+                    "temporal": "2024-12-01/2024-12-07",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-13"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/5744e19f-5baa-4da7-a583-6b868ee6730f/FISS_AR_20241209.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/61001003-0443-474e-aa30-1529f19f8e08",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-10",
                     "modified": "2024-12-10",
-                    "temporal": "2024-12-01/2024-12-07"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/61001003-0443-474e-aa30-1529f19f8e08",
+                    "temporal": "2024-12-01/2024-12-07",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-10"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/61001003-0443-474e-aa30-1529f19f8e08/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/61001003-0443-474e-aa30-1529f19f8e08",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-10",
+                    "format": "API",
                     "modified": "2024-12-10",
-                    "temporal": "2024-12-01/2024-12-07"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/61001003-0443-474e-aa30-1529f19f8e08",
+                    "temporal": "2024-12-01/2024-12-07",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-10"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/341796c3-a235-403f-97d4-2900c0194d12/FISS_AR_20241205.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f073c4b6-27d9-4c94-8bf5-d9e453e73835",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-06",
                     "modified": "2024-12-06",
-                    "temporal": "2024-11-24/2024-11-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f073c4b6-27d9-4c94-8bf5-d9e453e73835",
+                    "temporal": "2024-11-24/2024-11-30",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-06"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/f073c4b6-27d9-4c94-8bf5-d9e453e73835/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f073c4b6-27d9-4c94-8bf5-d9e453e73835",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-06",
+                    "format": "API",
                     "modified": "2024-12-06",
-                    "temporal": "2024-11-24/2024-11-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f073c4b6-27d9-4c94-8bf5-d9e453e73835",
+                    "temporal": "2024-11-24/2024-11-30",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-06"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/47594677-d992-41fd-b35d-3308881ce3bd/FISS_AR_20241202.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/140ded17-df75-4182-a591-95430259374c",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-03",
                     "modified": "2024-12-03",
-                    "temporal": "2024-11-24/2024-11-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/140ded17-df75-4182-a591-95430259374c",
+                    "temporal": "2024-11-24/2024-11-30",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-03"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/140ded17-df75-4182-a591-95430259374c/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/140ded17-df75-4182-a591-95430259374c",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-03",
+                    "format": "API",
                     "modified": "2024-12-03",
-                    "temporal": "2024-11-24/2024-11-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/140ded17-df75-4182-a591-95430259374c",
+                    "temporal": "2024-11-24/2024-11-30",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-03"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/2d550efb-e0d4-446f-8cbd-fdb22ab95043/FISS_AR_20241129.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/550e9016-eef0-49a1-ab44-f4a531844ac6",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-29",
                     "modified": "2024-11-29",
-                    "temporal": "2024-11-17/2024-11-23"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/550e9016-eef0-49a1-ab44-f4a531844ac6",
+                    "temporal": "2024-11-17/2024-11-23",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-29"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/550e9016-eef0-49a1-ab44-f4a531844ac6/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/550e9016-eef0-49a1-ab44-f4a531844ac6",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-29",
+                    "format": "API",
                     "modified": "2024-11-29",
-                    "temporal": "2024-11-17/2024-11-23"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/550e9016-eef0-49a1-ab44-f4a531844ac6",
+                    "temporal": "2024-11-17/2024-11-23",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-29"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/1c26b1de-a9ba-46be-b932-de94beddcaad/FISS_AR_20241125.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/806921ea-04d0-4105-8286-ce1079a0e883",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-26",
                     "modified": "2024-11-26",
-                    "temporal": "2024-11-17/2024-11-23"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/806921ea-04d0-4105-8286-ce1079a0e883",
+                    "temporal": "2024-11-17/2024-11-23",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-26"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/806921ea-04d0-4105-8286-ce1079a0e883/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/806921ea-04d0-4105-8286-ce1079a0e883",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-26",
+                    "format": "API",
                     "modified": "2024-11-26",
-                    "temporal": "2024-11-17/2024-11-23"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/806921ea-04d0-4105-8286-ce1079a0e883",
+                    "temporal": "2024-11-17/2024-11-23",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-26"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/4c631191-30fd-46fd-82d6-f6ce500fcc7c/FISS_AR_20241121.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6463d5d5-3d98-474c-9c84-fd2c02166574",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-21",
                     "modified": "2024-11-21",
-                    "temporal": "2024-11-10/2024-11-16"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6463d5d5-3d98-474c-9c84-fd2c02166574",
+                    "temporal": "2024-11-10/2024-11-16",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-21"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/6463d5d5-3d98-474c-9c84-fd2c02166574/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6463d5d5-3d98-474c-9c84-fd2c02166574",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-21",
+                    "format": "API",
                     "modified": "2024-11-21",
-                    "temporal": "2024-11-10/2024-11-16"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6463d5d5-3d98-474c-9c84-fd2c02166574",
+                    "temporal": "2024-11-10/2024-11-16",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-21"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/c6bd5230-1c49-4d93-a679-28688e809fab/FISS_AR_20241118.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d0eb0f87-f9f7-4cc6-aa81-2334974f81bf",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-19",
                     "modified": "2024-11-19",
-                    "temporal": "2024-11-10/2024-11-16"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d0eb0f87-f9f7-4cc6-aa81-2334974f81bf",
+                    "temporal": "2024-11-10/2024-11-16",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-19"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/d0eb0f87-f9f7-4cc6-aa81-2334974f81bf/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d0eb0f87-f9f7-4cc6-aa81-2334974f81bf",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-19",
+                    "format": "API",
                     "modified": "2024-11-19",
-                    "temporal": "2024-11-10/2024-11-16"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d0eb0f87-f9f7-4cc6-aa81-2334974f81bf",
+                    "temporal": "2024-11-10/2024-11-16",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-19"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/14a91ecd-dab9-40a7-8d8a-2b299334151e/FISS_AR_20241114.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fcb7637d-8cf5-4abe-8d54-e15c195ba124",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-15",
                     "modified": "2024-11-15",
-                    "temporal": "2024-11-03/2024-11-09"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fcb7637d-8cf5-4abe-8d54-e15c195ba124",
+                    "temporal": "2024-11-03/2024-11-09",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-15"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/fcb7637d-8cf5-4abe-8d54-e15c195ba124/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fcb7637d-8cf5-4abe-8d54-e15c195ba124",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-15",
+                    "format": "API",
                     "modified": "2024-11-15",
-                    "temporal": "2024-11-03/2024-11-09"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fcb7637d-8cf5-4abe-8d54-e15c195ba124",
+                    "temporal": "2024-11-03/2024-11-09",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/6760109e-2e4a-4ce1-a88d-08d79c4ed142/FISS_AR_20241112.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/aa96d2f5-5be4-47f5-bae0-c9189f58d049",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-13",
                     "modified": "2024-11-13",
-                    "temporal": "2024-11-03/2024-11-09"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/aa96d2f5-5be4-47f5-bae0-c9189f58d049",
+                    "temporal": "2024-11-03/2024-11-09",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-13"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/aa96d2f5-5be4-47f5-bae0-c9189f58d049/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/aa96d2f5-5be4-47f5-bae0-c9189f58d049",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-13",
+                    "format": "API",
                     "modified": "2024-11-13",
-                    "temporal": "2024-11-03/2024-11-09"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/aa96d2f5-5be4-47f5-bae0-c9189f58d049",
+                    "temporal": "2024-11-03/2024-11-09",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-13"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/f2975682-597e-4e70-aeb0-365681d70365/FISS_AR_20241107.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e42de85e-4265-47c8-8534-ce49f20d7ea6",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-08",
                     "modified": "2024-11-08",
-                    "temporal": "2024-10-27/2024-11-02"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e42de85e-4265-47c8-8534-ce49f20d7ea6",
+                    "temporal": "2024-10-27/2024-11-02",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-08"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/e42de85e-4265-47c8-8534-ce49f20d7ea6/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e42de85e-4265-47c8-8534-ce49f20d7ea6",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-08",
+                    "format": "API",
                     "modified": "2024-11-08",
-                    "temporal": "2024-10-27/2024-11-02"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e42de85e-4265-47c8-8534-ce49f20d7ea6",
+                    "temporal": "2024-10-27/2024-11-02",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-08"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/f5fda85e-b208-4e98-b50d-91387875e750/FISS_AR_20241104.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f3148bfb-8410-4fd5-85c9-fe2e5e7fa2b2",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-05",
                     "modified": "2024-11-05",
-                    "temporal": "2024-10-27/2024-11-02"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f3148bfb-8410-4fd5-85c9-fe2e5e7fa2b2",
+                    "temporal": "2024-10-27/2024-11-02",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-05"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/f3148bfb-8410-4fd5-85c9-fe2e5e7fa2b2/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f3148bfb-8410-4fd5-85c9-fe2e5e7fa2b2",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-05",
+                    "format": "API",
                     "modified": "2024-11-05",
-                    "temporal": "2024-10-27/2024-11-02"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f3148bfb-8410-4fd5-85c9-fe2e5e7fa2b2",
+                    "temporal": "2024-10-27/2024-11-02",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-05"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/38c30221-e9f5-4abc-a1d5-e3954fea2397/FISS_AR_20241031.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7ae39053-2d53-4f1f-9569-63e310de7554",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-01",
                     "modified": "2024-11-01",
-                    "temporal": "2024-10-20/2024-10-26"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7ae39053-2d53-4f1f-9569-63e310de7554",
+                    "temporal": "2024-10-20/2024-10-26",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/7ae39053-2d53-4f1f-9569-63e310de7554/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7ae39053-2d53-4f1f-9569-63e310de7554",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-01",
+                    "format": "API",
                     "modified": "2024-11-01",
-                    "temporal": "2024-10-20/2024-10-26"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7ae39053-2d53-4f1f-9569-63e310de7554",
+                    "temporal": "2024-10-20/2024-10-26",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/b84ebcaf-78e1-4f0c-bc68-23a83ae7b90f/FISS_AR_20241028.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5689e659-88a7-4240-baa3-48225b12eae1",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-29",
                     "modified": "2024-10-29",
-                    "temporal": "2024-10-20/2024-10-26"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5689e659-88a7-4240-baa3-48225b12eae1",
+                    "temporal": "2024-10-20/2024-10-26",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-29"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/5689e659-88a7-4240-baa3-48225b12eae1/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5689e659-88a7-4240-baa3-48225b12eae1",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-29",
+                    "format": "API",
                     "modified": "2024-10-29",
-                    "temporal": "2024-10-20/2024-10-26"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5689e659-88a7-4240-baa3-48225b12eae1",
+                    "temporal": "2024-10-20/2024-10-26",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-29"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/97cbaebc-79aa-4bed-b9a3-e8545c9a16ac/FISS_AR_20241024.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7fd350d0-0e68-4f59-9a7c-6fff0345f181",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-25",
                     "modified": "2024-10-25",
-                    "temporal": "2024-10-13/2024-10-19"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7fd350d0-0e68-4f59-9a7c-6fff0345f181",
+                    "temporal": "2024-10-13/2024-10-19",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-25"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/7fd350d0-0e68-4f59-9a7c-6fff0345f181/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7fd350d0-0e68-4f59-9a7c-6fff0345f181",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-25",
+                    "format": "API",
                     "modified": "2024-10-25",
-                    "temporal": "2024-10-13/2024-10-19"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7fd350d0-0e68-4f59-9a7c-6fff0345f181",
+                    "temporal": "2024-10-13/2024-10-19",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-25"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/d9e537db-5649-449c-94cc-47cc13b12a74/FISS_AR_20241021.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/733dc123-cd57-47bc-a4aa-7c87a5781934",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-22",
                     "modified": "2024-10-22",
-                    "temporal": "2024-10-13/2024-10-19"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/733dc123-cd57-47bc-a4aa-7c87a5781934",
+                    "temporal": "2024-10-13/2024-10-19",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-22"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/733dc123-cd57-47bc-a4aa-7c87a5781934/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/733dc123-cd57-47bc-a4aa-7c87a5781934",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-22",
+                    "format": "API",
                     "modified": "2024-10-22",
-                    "temporal": "2024-10-13/2024-10-19"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/733dc123-cd57-47bc-a4aa-7c87a5781934",
+                    "temporal": "2024-10-13/2024-10-19",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-22"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/6b45df61-2b99-4798-8f1a-98b88236e4c8/FISS_AR_20241017.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d4b9b67b-7c15-4617-897a-9bcfb23280ce",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-18",
                     "modified": "2024-10-18",
-                    "temporal": "2024-10-06/2024-10-12"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d4b9b67b-7c15-4617-897a-9bcfb23280ce",
+                    "temporal": "2024-10-06/2024-10-12",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-18"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/d4b9b67b-7c15-4617-897a-9bcfb23280ce/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d4b9b67b-7c15-4617-897a-9bcfb23280ce",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-18",
+                    "format": "API",
                     "modified": "2024-10-18",
-                    "temporal": "2024-10-06/2024-10-12"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d4b9b67b-7c15-4617-897a-9bcfb23280ce",
+                    "temporal": "2024-10-06/2024-10-12",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-18"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/0d54ef8c-cf19-4f65-8592-5cc10ba0d9b8/FISS_AR_20241015.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a438db1f-57b9-4d63-bc78-fd648ca908b3",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-15",
                     "modified": "2024-10-15",
-                    "temporal": "2024-10-06/2024-10-12"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a438db1f-57b9-4d63-bc78-fd648ca908b3",
+                    "temporal": "2024-10-06/2024-10-12",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-15"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/a438db1f-57b9-4d63-bc78-fd648ca908b3/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a438db1f-57b9-4d63-bc78-fd648ca908b3",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-15",
+                    "format": "API",
                     "modified": "2024-10-15",
-                    "temporal": "2024-10-06/2024-10-12"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a438db1f-57b9-4d63-bc78-fd648ca908b3",
+                    "temporal": "2024-10-06/2024-10-12",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/153b4397-9dfc-4bb0-917f-a26b8a3ddb7c/FISS_AR_20241010.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f8d0352e-2670-4aaa-a150-f51a074bc336",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-11",
                     "modified": "2024-10-11",
-                    "temporal": "2024-09-29/2024-10-05"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f8d0352e-2670-4aaa-a150-f51a074bc336",
+                    "temporal": "2024-09-29/2024-10-05",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-11"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/f8d0352e-2670-4aaa-a150-f51a074bc336/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f8d0352e-2670-4aaa-a150-f51a074bc336",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-11",
+                    "format": "API",
                     "modified": "2024-10-11",
-                    "temporal": "2024-09-29/2024-10-05"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f8d0352e-2670-4aaa-a150-f51a074bc336",
+                    "temporal": "2024-09-29/2024-10-05",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-11"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/4b6eb3b2-b9f5-4c7d-b64e-9f5997202808/FISS_AR_20241007.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d0ec72d9-f705-4c79-9efb-e603f3470d71",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-08",
                     "modified": "2024-10-08",
-                    "temporal": "2024-09-29/2024-10-05"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d0ec72d9-f705-4c79-9efb-e603f3470d71",
+                    "temporal": "2024-09-29/2024-10-05",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-08"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/d0ec72d9-f705-4c79-9efb-e603f3470d71/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d0ec72d9-f705-4c79-9efb-e603f3470d71",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-08",
+                    "format": "API",
                     "modified": "2024-10-08",
-                    "temporal": "2024-09-29/2024-10-05"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d0ec72d9-f705-4c79-9efb-e603f3470d71",
+                    "temporal": "2024-09-29/2024-10-05",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-08"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/f615cbb5-38ec-44e5-b44a-2f1adea533b2/FISS_AR_20241003.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b761e361-b2b4-4778-aa87-6c9550714b85",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-04",
                     "modified": "2024-10-04",
-                    "temporal": "2024-09-22/2024-09-28"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b761e361-b2b4-4778-aa87-6c9550714b85",
+                    "temporal": "2024-09-22/2024-09-28",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-04"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/b761e361-b2b4-4778-aa87-6c9550714b85/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b761e361-b2b4-4778-aa87-6c9550714b85",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-04",
+                    "format": "API",
                     "modified": "2024-10-04",
-                    "temporal": "2024-09-22/2024-09-28"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b761e361-b2b4-4778-aa87-6c9550714b85",
+                    "temporal": "2024-09-22/2024-09-28",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-04"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/40fcff68-2524-4045-af19-65c2fcea54ab/FISS_AR_20240930.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/76600c23-89d5-4cdf-b667-7a398d9cf567",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-01",
                     "modified": "2024-10-01",
-                    "temporal": "2024-09-22/2024-09-28"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/76600c23-89d5-4cdf-b667-7a398d9cf567",
+                    "temporal": "2024-09-22/2024-09-28",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/76600c23-89d5-4cdf-b667-7a398d9cf567/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/76600c23-89d5-4cdf-b667-7a398d9cf567",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-01",
+                    "format": "API",
                     "modified": "2024-10-01",
-                    "temporal": "2024-09-22/2024-09-28"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/76600c23-89d5-4cdf-b667-7a398d9cf567",
+                    "temporal": "2024-09-22/2024-09-28",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/2949d8c0-ff22-43c0-a87e-b892e8f5b5cb/FISS_AR_20240926.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7e8d18c1-60e6-4672-9a14-900d36d1aebf",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-27",
                     "modified": "2024-09-27",
-                    "temporal": "2024-09-15/2024-09-21"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7e8d18c1-60e6-4672-9a14-900d36d1aebf",
+                    "temporal": "2024-09-15/2024-09-21",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-27"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/7e8d18c1-60e6-4672-9a14-900d36d1aebf/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7e8d18c1-60e6-4672-9a14-900d36d1aebf",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-27",
+                    "format": "API",
                     "modified": "2024-09-27",
-                    "temporal": "2024-09-15/2024-09-21"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7e8d18c1-60e6-4672-9a14-900d36d1aebf",
+                    "temporal": "2024-09-15/2024-09-21",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-27"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/c7fd8a1e-7768-406a-b481-8d4cbaeafc1a/FISS_AR_20240923.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8736defb-6eaa-4bf9-8d1a-720431a76571",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-24",
                     "modified": "2024-09-24",
-                    "temporal": "2024-09-15/2024-09-21"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8736defb-6eaa-4bf9-8d1a-720431a76571",
+                    "temporal": "2024-09-15/2024-09-21",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-24"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/8736defb-6eaa-4bf9-8d1a-720431a76571/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8736defb-6eaa-4bf9-8d1a-720431a76571",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-24",
+                    "format": "API",
                     "modified": "2024-09-24",
-                    "temporal": "2024-09-15/2024-09-21"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8736defb-6eaa-4bf9-8d1a-720431a76571",
+                    "temporal": "2024-09-15/2024-09-21",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-24"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/6e36cb23-3085-4b1c-8ab8-e80d9cf514bb/FISS_AR_20240919.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/134d1783-60cd-436a-a33e-98a369b844d4",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-20",
                     "modified": "2024-09-20",
-                    "temporal": "2024-09-08/2024-09-14"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/134d1783-60cd-436a-a33e-98a369b844d4",
+                    "temporal": "2024-09-08/2024-09-14",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-20"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/134d1783-60cd-436a-a33e-98a369b844d4/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/134d1783-60cd-436a-a33e-98a369b844d4",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-20",
+                    "format": "API",
                     "modified": "2024-09-20",
-                    "temporal": "2024-09-08/2024-09-14"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/134d1783-60cd-436a-a33e-98a369b844d4",
+                    "temporal": "2024-09-08/2024-09-14",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-20"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/024ea43e-70cd-4ea9-9d6f-e9c82b638dee/FISS_AR_20240916.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/01ead372-97d2-427b-bb06-52b64cd674a8",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-17",
                     "modified": "2024-09-17",
-                    "temporal": "2024-09-08/2024-09-14"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/01ead372-97d2-427b-bb06-52b64cd674a8",
+                    "temporal": "2024-09-08/2024-09-14",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-17"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/01ead372-97d2-427b-bb06-52b64cd674a8/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/01ead372-97d2-427b-bb06-52b64cd674a8",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-17",
+                    "format": "API",
                     "modified": "2024-09-17",
-                    "temporal": "2024-09-08/2024-09-14"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/01ead372-97d2-427b-bb06-52b64cd674a8",
+                    "temporal": "2024-09-08/2024-09-14",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-17"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/f4e3e21b-44a2-4c41-9c69-cdb139ab35c3/FISS_AR_20240912.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/36cbbf42-33a9-4dad-8f62-9936ee3b78d0",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-13",
                     "modified": "2024-09-13",
-                    "temporal": "2024-09-01/2024-09-07"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/36cbbf42-33a9-4dad-8f62-9936ee3b78d0",
+                    "temporal": "2024-09-01/2024-09-07",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-13"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/36cbbf42-33a9-4dad-8f62-9936ee3b78d0/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/36cbbf42-33a9-4dad-8f62-9936ee3b78d0",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-13",
+                    "format": "API",
                     "modified": "2024-09-13",
-                    "temporal": "2024-09-01/2024-09-07"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/36cbbf42-33a9-4dad-8f62-9936ee3b78d0",
+                    "temporal": "2024-09-01/2024-09-07",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-13"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/995cb12a-e855-47d0-b084-2333ff1f6881/FISS_AR_20240909.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/afb2dc1a-0828-4e9f-8678-eb180d0c34e6",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-10",
                     "modified": "2024-09-10",
-                    "temporal": "2024-09-01/2024-09-07"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/afb2dc1a-0828-4e9f-8678-eb180d0c34e6",
+                    "temporal": "2024-09-01/2024-09-07",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-10"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/afb2dc1a-0828-4e9f-8678-eb180d0c34e6/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/afb2dc1a-0828-4e9f-8678-eb180d0c34e6",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-10",
+                    "format": "API",
                     "modified": "2024-09-10",
-                    "temporal": "2024-09-01/2024-09-07"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/afb2dc1a-0828-4e9f-8678-eb180d0c34e6",
+                    "temporal": "2024-09-01/2024-09-07",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-10"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/8fc6ec5a-ea70-4bed-83f3-bb5931df815d/FISS_AR_20240905.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/726981dd-4854-4c11-bd2f-776507bd276b",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-06",
                     "modified": "2024-09-06",
-                    "temporal": "2024-08-25/2024-08-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/726981dd-4854-4c11-bd2f-776507bd276b",
+                    "temporal": "2024-08-25/2024-08-31",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-06"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/726981dd-4854-4c11-bd2f-776507bd276b/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/726981dd-4854-4c11-bd2f-776507bd276b",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-06",
+                    "format": "API",
                     "modified": "2024-09-06",
-                    "temporal": "2024-08-25/2024-08-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/726981dd-4854-4c11-bd2f-776507bd276b",
+                    "temporal": "2024-08-25/2024-08-31",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-06"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/0af84e0e-d29c-403f-bba4-da1e6f6bc238/FISS_AR_20240903.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c28f7040-1817-4455-9301-2958e9cd26d2",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-04",
                     "modified": "2024-09-04",
-                    "temporal": "2024-08-25/2024-08-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c28f7040-1817-4455-9301-2958e9cd26d2",
+                    "temporal": "2024-08-25/2024-08-31",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-04"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/c28f7040-1817-4455-9301-2958e9cd26d2/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c28f7040-1817-4455-9301-2958e9cd26d2",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-04",
+                    "format": "API",
                     "modified": "2024-09-04",
-                    "temporal": "2024-08-25/2024-08-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c28f7040-1817-4455-9301-2958e9cd26d2",
+                    "temporal": "2024-08-25/2024-08-31",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-04"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/c4263f08-8500-4ce5-b9a4-1aa6f4e7447f/FISS_AR_20240829.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/01118d40-b93e-41af-97e9-93d644edaf9f",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-30",
                     "modified": "2024-08-30",
-                    "temporal": "2024-08-18/2024-08-24"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/01118d40-b93e-41af-97e9-93d644edaf9f",
+                    "temporal": "2024-08-18/2024-08-24",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-30"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/01118d40-b93e-41af-97e9-93d644edaf9f/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/01118d40-b93e-41af-97e9-93d644edaf9f",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-30",
+                    "format": "API",
                     "modified": "2024-08-30",
-                    "temporal": "2024-08-18/2024-08-24"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/01118d40-b93e-41af-97e9-93d644edaf9f",
+                    "temporal": "2024-08-18/2024-08-24",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-30"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/3d82538a-c4fa-4ea0-ad06-39bd3728f392/FISS_AR_20240826.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/be79731c-5eef-48c4-a55f-829e143098d6",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-27",
                     "modified": "2024-08-27",
-                    "temporal": "2024-08-18/2024-08-24"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/be79731c-5eef-48c4-a55f-829e143098d6",
+                    "temporal": "2024-08-18/2024-08-24",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-27"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/be79731c-5eef-48c4-a55f-829e143098d6/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/be79731c-5eef-48c4-a55f-829e143098d6",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-27",
+                    "format": "API",
                     "modified": "2024-08-27",
-                    "temporal": "2024-08-18/2024-08-24"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/be79731c-5eef-48c4-a55f-829e143098d6",
+                    "temporal": "2024-08-18/2024-08-24",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-27"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/9538b51c-9d08-4ed7-9f0e-88bc46df01a5/FISS_AR_20240822.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5798cc0a-ffe0-456d-8b0f-780d4fe7b8bc",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-23",
                     "modified": "2024-08-23",
-                    "temporal": "2024-08-11/2024-08-17"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5798cc0a-ffe0-456d-8b0f-780d4fe7b8bc",
+                    "temporal": "2024-08-11/2024-08-17",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-23"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/5798cc0a-ffe0-456d-8b0f-780d4fe7b8bc/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5798cc0a-ffe0-456d-8b0f-780d4fe7b8bc",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-23",
+                    "format": "API",
                     "modified": "2024-08-23",
-                    "temporal": "2024-08-11/2024-08-17"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5798cc0a-ffe0-456d-8b0f-780d4fe7b8bc",
+                    "temporal": "2024-08-11/2024-08-17",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-23"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/e2748d2f-752f-4f79-9b3d-ca4ef5e3e570/FISS_AR_20240819.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0063124a-af45-45c2-8b8e-5f91b67648d0",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-20",
                     "modified": "2024-08-20",
-                    "temporal": "2024-08-11/2024-08-17"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0063124a-af45-45c2-8b8e-5f91b67648d0",
+                    "temporal": "2024-08-11/2024-08-17",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-20"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/0063124a-af45-45c2-8b8e-5f91b67648d0/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0063124a-af45-45c2-8b8e-5f91b67648d0",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-20",
+                    "format": "API",
                     "modified": "2024-08-20",
-                    "temporal": "2024-08-11/2024-08-17"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0063124a-af45-45c2-8b8e-5f91b67648d0",
+                    "temporal": "2024-08-11/2024-08-17",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-20"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/47cee078-a858-44a3-98ac-484f9e2cf9ba/FISS_AR_20240815.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/29d06a31-ddd9-4b52-b678-31355217a9fa",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-16",
                     "modified": "2024-08-16",
-                    "temporal": "2024-08-04/2024-08-10"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/29d06a31-ddd9-4b52-b678-31355217a9fa",
+                    "temporal": "2024-08-04/2024-08-10",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-16"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/29d06a31-ddd9-4b52-b678-31355217a9fa/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/29d06a31-ddd9-4b52-b678-31355217a9fa",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-16",
+                    "format": "API",
                     "modified": "2024-08-16",
-                    "temporal": "2024-08-04/2024-08-10"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/29d06a31-ddd9-4b52-b678-31355217a9fa",
+                    "temporal": "2024-08-04/2024-08-10",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-16"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/f1f8d277-b2ac-46d2-9121-794f71804f87/FISS_AR_20240812.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/839d9042-a39f-41fb-bbc4-88c3d9f4c3b9",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-13",
                     "modified": "2024-08-13",
-                    "temporal": "2024-08-04/2024-08-10"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/839d9042-a39f-41fb-bbc4-88c3d9f4c3b9",
+                    "temporal": "2024-08-04/2024-08-10",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-13"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/839d9042-a39f-41fb-bbc4-88c3d9f4c3b9/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/839d9042-a39f-41fb-bbc4-88c3d9f4c3b9",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-13",
+                    "format": "API",
                     "modified": "2024-08-13",
-                    "temporal": "2024-08-04/2024-08-10"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/839d9042-a39f-41fb-bbc4-88c3d9f4c3b9",
+                    "temporal": "2024-08-04/2024-08-10",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-13"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/6cc20ca2-534a-486c-b322-51947883ffea/FISS_AR_20240808.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fce0228b-16b0-404a-872b-a34e8d01ada1",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-09",
                     "modified": "2024-08-09",
-                    "temporal": "2024-07-28/2024-08-03"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fce0228b-16b0-404a-872b-a34e8d01ada1",
+                    "temporal": "2024-07-28/2024-08-03",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-09"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/fce0228b-16b0-404a-872b-a34e8d01ada1/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fce0228b-16b0-404a-872b-a34e8d01ada1",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-09",
+                    "format": "API",
                     "modified": "2024-08-09",
-                    "temporal": "2024-07-28/2024-08-03"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fce0228b-16b0-404a-872b-a34e8d01ada1",
+                    "temporal": "2024-07-28/2024-08-03",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-09"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/1edc801f-5e93-4071-886f-72fbd4869a98/FISS_AR_20240805.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/10a01a39-36cb-4510-96e3-0f6ff0e585d1",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-06",
                     "modified": "2024-08-06",
-                    "temporal": "2024-07-28/2024-08-03"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/10a01a39-36cb-4510-96e3-0f6ff0e585d1",
+                    "temporal": "2024-07-28/2024-08-03",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-06"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/10a01a39-36cb-4510-96e3-0f6ff0e585d1/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/10a01a39-36cb-4510-96e3-0f6ff0e585d1",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-06",
+                    "format": "API",
                     "modified": "2024-08-06",
-                    "temporal": "2024-07-28/2024-08-03"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/10a01a39-36cb-4510-96e3-0f6ff0e585d1",
+                    "temporal": "2024-07-28/2024-08-03",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-06"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/d28629a9-8bd3-4bd9-b410-e743901a93eb/FISS_AR_20240801.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c8bf9741-5a2e-460e-9d0e-c8e7254c850f",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-02",
                     "modified": "2024-08-02",
-                    "temporal": "2024-07-21/2024-07-27"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c8bf9741-5a2e-460e-9d0e-c8e7254c850f",
+                    "temporal": "2024-07-21/2024-07-27",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-02"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/c8bf9741-5a2e-460e-9d0e-c8e7254c850f/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c8bf9741-5a2e-460e-9d0e-c8e7254c850f",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-02",
+                    "format": "API",
                     "modified": "2024-08-02",
-                    "temporal": "2024-07-21/2024-07-27"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c8bf9741-5a2e-460e-9d0e-c8e7254c850f",
+                    "temporal": "2024-07-21/2024-07-27",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-02"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/f3f4d6ea-eeff-4b8b-b3d4-60ec86f5573b/FISS_AR_20240729.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/56e31267-840a-4b95-aa28-c7ecc8377664",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-30",
                     "modified": "2024-07-30",
-                    "temporal": "2024-07-21/2024-07-27"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/56e31267-840a-4b95-aa28-c7ecc8377664",
+                    "temporal": "2024-07-21/2024-07-27",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-30"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/56e31267-840a-4b95-aa28-c7ecc8377664/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/56e31267-840a-4b95-aa28-c7ecc8377664",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-30",
+                    "format": "API",
                     "modified": "2024-07-30",
-                    "temporal": "2024-07-21/2024-07-27"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/56e31267-840a-4b95-aa28-c7ecc8377664",
+                    "temporal": "2024-07-21/2024-07-27",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-30"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/49069c44-008a-4174-908f-0cd0a4fa6558/FISS_AR_20240725.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5f397310-01d9-48a0-a89f-560198c03523",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-26",
                     "modified": "2024-07-26",
-                    "temporal": "2024-07-14/2024-07-20"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5f397310-01d9-48a0-a89f-560198c03523",
+                    "temporal": "2024-07-14/2024-07-20",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-26"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/5f397310-01d9-48a0-a89f-560198c03523/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5f397310-01d9-48a0-a89f-560198c03523",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-26",
+                    "format": "API",
                     "modified": "2024-07-26",
-                    "temporal": "2024-07-14/2024-07-20"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5f397310-01d9-48a0-a89f-560198c03523",
+                    "temporal": "2024-07-14/2024-07-20",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-26"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/07a37ec9-1642-4212-8c51-b0200fd57303/FISS_AR_20240722.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/76b42075-bc48-4898-a0c0-b9c1a4a9516f",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-23",
                     "modified": "2024-07-23",
-                    "temporal": "2024-07-14/2024-07-20"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/76b42075-bc48-4898-a0c0-b9c1a4a9516f",
+                    "temporal": "2024-07-14/2024-07-20",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-23"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/76b42075-bc48-4898-a0c0-b9c1a4a9516f/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/76b42075-bc48-4898-a0c0-b9c1a4a9516f",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-23",
+                    "format": "API",
                     "modified": "2024-07-23",
-                    "temporal": "2024-07-14/2024-07-20"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/76b42075-bc48-4898-a0c0-b9c1a4a9516f",
+                    "temporal": "2024-07-14/2024-07-20",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-23"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/98daa63b-1982-4bbb-8452-f1b653a50134/FISS_AR_20240718.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/82a7baaf-2e2f-4a56-97df-6ea1d0c998c7",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-19",
                     "modified": "2024-07-19",
-                    "temporal": "2024-07-07/2024-07-13"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/82a7baaf-2e2f-4a56-97df-6ea1d0c998c7",
+                    "temporal": "2024-07-07/2024-07-13",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-19"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/82a7baaf-2e2f-4a56-97df-6ea1d0c998c7/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/82a7baaf-2e2f-4a56-97df-6ea1d0c998c7",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-19",
+                    "format": "API",
                     "modified": "2024-07-19",
-                    "temporal": "2024-07-07/2024-07-13"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/82a7baaf-2e2f-4a56-97df-6ea1d0c998c7",
+                    "temporal": "2024-07-07/2024-07-13",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-19"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/61a3e1b5-39d4-40a7-a31d-925510ee6c7d/FISS_AR_20240715.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b0ec6284-cab7-47b5-9401-9d2ee550c31f",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-16",
                     "modified": "2024-07-16",
-                    "temporal": "2024-07-07/2024-07-13"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b0ec6284-cab7-47b5-9401-9d2ee550c31f",
+                    "temporal": "2024-07-07/2024-07-13",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-16"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/b0ec6284-cab7-47b5-9401-9d2ee550c31f/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b0ec6284-cab7-47b5-9401-9d2ee550c31f",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-16",
+                    "format": "API",
                     "modified": "2024-07-16",
-                    "temporal": "2024-07-07/2024-07-13"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b0ec6284-cab7-47b5-9401-9d2ee550c31f",
+                    "temporal": "2024-07-07/2024-07-13",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-16"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/fe268742-36d9-4979-bd59-8c8891e50c1e/FISS_AR_20240711.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3ba38bb3-9024-4246-b101-1794132c8c3b",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-15",
                     "modified": "2024-07-15",
-                    "temporal": "2024-07-07/2024-07-13"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3ba38bb3-9024-4246-b101-1794132c8c3b",
+                    "temporal": "2024-07-07/2024-07-13",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-15"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/3ba38bb3-9024-4246-b101-1794132c8c3b/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3ba38bb3-9024-4246-b101-1794132c8c3b",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-15",
+                    "format": "API",
                     "modified": "2024-07-15",
-                    "temporal": "2024-07-07/2024-07-13"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3ba38bb3-9024-4246-b101-1794132c8c3b",
+                    "temporal": "2024-07-07/2024-07-13",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/2f21ce07-5fca-445a-9a5f-56464b00b149/FISS_AR_20240708.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a5732418-2c2d-4c78-a418-c92eb19d56f0",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-09",
                     "modified": "2024-07-09",
-                    "temporal": "2024-06-30/2024-07-06"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a5732418-2c2d-4c78-a418-c92eb19d56f0",
+                    "temporal": "2024-06-30/2024-07-06",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-09"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/a5732418-2c2d-4c78-a418-c92eb19d56f0/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a5732418-2c2d-4c78-a418-c92eb19d56f0",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-09",
+                    "format": "API",
                     "modified": "2024-07-09",
-                    "temporal": "2024-06-30/2024-07-06"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a5732418-2c2d-4c78-a418-c92eb19d56f0",
+                    "temporal": "2024-06-30/2024-07-06",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-09"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/2440b8de-4fed-48a2-84ad-16e46f80c600/FISS_AR_20240705.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6d302b6f-2388-455f-af86-022ed1b1dbe2",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-05",
                     "modified": "2024-07-05",
-                    "temporal": "2024-06-23/2024-06-29"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6d302b6f-2388-455f-af86-022ed1b1dbe2",
+                    "temporal": "2024-06-23/2024-06-29",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-05"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/6d302b6f-2388-455f-af86-022ed1b1dbe2/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6d302b6f-2388-455f-af86-022ed1b1dbe2",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-05",
+                    "format": "API",
                     "modified": "2024-07-05",
-                    "temporal": "2024-06-23/2024-06-29"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6d302b6f-2388-455f-af86-022ed1b1dbe2",
+                    "temporal": "2024-06-23/2024-06-29",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-05"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/28f34db0-711f-4ba0-8650-cb1b14233b20/FISS_AR_20240701.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ce1a7f2d-a86b-497f-9c36-5401106b60b6",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-02",
                     "modified": "2024-07-02",
-                    "temporal": "2024-06-23/2024-06-29"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ce1a7f2d-a86b-497f-9c36-5401106b60b6",
+                    "temporal": "2024-06-23/2024-06-29",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-02"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/ce1a7f2d-a86b-497f-9c36-5401106b60b6/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ce1a7f2d-a86b-497f-9c36-5401106b60b6",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-02",
+                    "format": "API",
                     "modified": "2024-07-02",
-                    "temporal": "2024-06-23/2024-06-29"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ce1a7f2d-a86b-497f-9c36-5401106b60b6",
+                    "temporal": "2024-06-23/2024-06-29",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-02"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/2095c686-3dd1-4fe6-811b-eba03efe576b/FISS_AR_20240627.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4f0ffaeb-5d29-43f1-903e-1e72ff380735",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-28",
                     "modified": "2024-06-28",
-                    "temporal": "2024-06-16/2024-06-22"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4f0ffaeb-5d29-43f1-903e-1e72ff380735",
+                    "temporal": "2024-06-16/2024-06-22",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-28"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/4f0ffaeb-5d29-43f1-903e-1e72ff380735/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4f0ffaeb-5d29-43f1-903e-1e72ff380735",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-28",
+                    "format": "API",
                     "modified": "2024-06-28",
-                    "temporal": "2024-06-16/2024-06-22"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4f0ffaeb-5d29-43f1-903e-1e72ff380735",
+                    "temporal": "2024-06-16/2024-06-22",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-28"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/47120d82-d767-4da3-8914-e71d95d4d06b/FISS_AR_20240624.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/119273f5-f6cb-420e-9194-3a2ab1d8f1f3",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-25",
                     "modified": "2024-06-25",
-                    "temporal": "2024-06-16/2024-06-22"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/119273f5-f6cb-420e-9194-3a2ab1d8f1f3",
+                    "temporal": "2024-06-16/2024-06-22",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-25"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/119273f5-f6cb-420e-9194-3a2ab1d8f1f3/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/119273f5-f6cb-420e-9194-3a2ab1d8f1f3",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-25",
+                    "format": "API",
                     "modified": "2024-06-25",
-                    "temporal": "2024-06-16/2024-06-22"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/119273f5-f6cb-420e-9194-3a2ab1d8f1f3",
+                    "temporal": "2024-06-16/2024-06-22",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-25"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/53480c18-5c65-4216-8ff9-4e1f9c6847a6/FISS_AR_20240620.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/00d8a926-7a71-49e8-ad22-f37c8141e2f6",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-21",
                     "modified": "2024-06-21",
-                    "temporal": "2024-06-09/2024-06-15"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/00d8a926-7a71-49e8-ad22-f37c8141e2f6",
+                    "temporal": "2024-06-09/2024-06-15",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-21"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/00d8a926-7a71-49e8-ad22-f37c8141e2f6/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/00d8a926-7a71-49e8-ad22-f37c8141e2f6",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-21",
+                    "format": "API",
                     "modified": "2024-06-21",
-                    "temporal": "2024-06-09/2024-06-15"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/00d8a926-7a71-49e8-ad22-f37c8141e2f6",
+                    "temporal": "2024-06-09/2024-06-15",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-21"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/99842d5a-aa43-4912-b319-1631cfccfedc/FISS_AR_20240617.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2eb0dd30-df9c-4a08-8ca8-f9b6c95c6da6",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-18",
                     "modified": "2024-06-18",
-                    "temporal": "2024-06-09/2024-06-15"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2eb0dd30-df9c-4a08-8ca8-f9b6c95c6da6",
+                    "temporal": "2024-06-09/2024-06-15",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-18"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/2eb0dd30-df9c-4a08-8ca8-f9b6c95c6da6/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2eb0dd30-df9c-4a08-8ca8-f9b6c95c6da6",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-18",
+                    "format": "API",
                     "modified": "2024-06-18",
-                    "temporal": "2024-06-09/2024-06-15"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2eb0dd30-df9c-4a08-8ca8-f9b6c95c6da6",
+                    "temporal": "2024-06-09/2024-06-15",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-18"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/80016f6c-aac6-40e1-a3f9-6119bde49d97/FISS_AR_20240613.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1ea6c61a-73c4-4ecf-a655-87f72fc49081",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-14",
                     "modified": "2024-06-14",
-                    "temporal": "2024-06-02/2024-06-08"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1ea6c61a-73c4-4ecf-a655-87f72fc49081",
+                    "temporal": "2024-06-02/2024-06-08",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-14"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/1ea6c61a-73c4-4ecf-a655-87f72fc49081/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1ea6c61a-73c4-4ecf-a655-87f72fc49081",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-14",
+                    "format": "API",
                     "modified": "2024-06-14",
-                    "temporal": "2024-06-02/2024-06-08"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1ea6c61a-73c4-4ecf-a655-87f72fc49081",
+                    "temporal": "2024-06-02/2024-06-08",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-14"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/bd6f30ae-92cf-4af8-bf91-ef962af9bcef/FISS_AR_20240610.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6655da6e-bbc5-45bc-8cf5-76085f127d32",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-11",
                     "modified": "2024-06-11",
-                    "temporal": "2024-06-02/2024-06-08"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6655da6e-bbc5-45bc-8cf5-76085f127d32",
+                    "temporal": "2024-06-02/2024-06-08",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-11"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/6655da6e-bbc5-45bc-8cf5-76085f127d32/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6655da6e-bbc5-45bc-8cf5-76085f127d32",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-11",
+                    "format": "API",
                     "modified": "2024-06-11",
-                    "temporal": "2024-06-02/2024-06-08"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6655da6e-bbc5-45bc-8cf5-76085f127d32",
+                    "temporal": "2024-06-02/2024-06-08",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-11"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/62a8b94b-a642-4fb3-9572-74fcbef36c43/FISS_AR_20240606.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e25efd14-237a-4f72-ba70-d383009210df",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-07",
                     "modified": "2024-06-07",
-                    "temporal": "2024-05-26/2024-06-01"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e25efd14-237a-4f72-ba70-d383009210df",
+                    "temporal": "2024-05-26/2024-06-01",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-07"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/e25efd14-237a-4f72-ba70-d383009210df/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e25efd14-237a-4f72-ba70-d383009210df",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-07",
+                    "format": "API",
                     "modified": "2024-06-07",
-                    "temporal": "2024-05-26/2024-06-01"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e25efd14-237a-4f72-ba70-d383009210df",
+                    "temporal": "2024-05-26/2024-06-01",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-07"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/73666b24-e4a6-493f-9366-d5acfb462eae/FISS_AR_20240603.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6032266f-38f7-4c5a-9d24-b5b5d78a768c",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-04",
                     "modified": "2024-06-04",
-                    "temporal": "2024-05-26/2024-06-01"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6032266f-38f7-4c5a-9d24-b5b5d78a768c",
+                    "temporal": "2024-05-26/2024-06-01",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-04"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/6032266f-38f7-4c5a-9d24-b5b5d78a768c/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6032266f-38f7-4c5a-9d24-b5b5d78a768c",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-04",
+                    "format": "API",
                     "modified": "2024-06-04",
-                    "temporal": "2024-05-26/2024-06-01"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6032266f-38f7-4c5a-9d24-b5b5d78a768c",
+                    "temporal": "2024-05-26/2024-06-01",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-04"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/8146601e-f8cc-4c18-bed9-f82191dd9071/FISS_AR_20240530.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/12ddd8ee-2610-4bdf-9a2d-3715321e8dc0",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-31",
                     "modified": "2024-05-31",
-                    "temporal": "2024-05-19/2024-05-25"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/12ddd8ee-2610-4bdf-9a2d-3715321e8dc0",
+                    "temporal": "2024-05-19/2024-05-25",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-31"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/12ddd8ee-2610-4bdf-9a2d-3715321e8dc0/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/12ddd8ee-2610-4bdf-9a2d-3715321e8dc0",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-31",
+                    "format": "API",
                     "modified": "2024-05-31",
-                    "temporal": "2024-05-19/2024-05-25"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/12ddd8ee-2610-4bdf-9a2d-3715321e8dc0",
+                    "temporal": "2024-05-19/2024-05-25",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-31"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/26aa1c3e-fec2-443e-b014-461681a42f18/FISS_AR_20240528.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/207e4bdd-2208-44b2-bccd-cd893272d524",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-29",
                     "modified": "2024-05-29",
-                    "temporal": "2024-05-19/2024-05-25"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/207e4bdd-2208-44b2-bccd-cd893272d524",
+                    "temporal": "2024-05-19/2024-05-25",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-29"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/207e4bdd-2208-44b2-bccd-cd893272d524/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/207e4bdd-2208-44b2-bccd-cd893272d524",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-29",
+                    "format": "API",
                     "modified": "2024-05-29",
-                    "temporal": "2024-05-19/2024-05-25"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/207e4bdd-2208-44b2-bccd-cd893272d524",
+                    "temporal": "2024-05-19/2024-05-25",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-29"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/6e2e4960-c2cc-44d0-9787-d3dd66276eaa/FISS_AR_20240523.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/243f8795-b01d-4b75-aa53-24447db9809b",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-28",
                     "modified": "2024-05-28",
-                    "temporal": "2024-05-19/2024-05-25"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/243f8795-b01d-4b75-aa53-24447db9809b",
+                    "temporal": "2024-05-19/2024-05-25",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-28"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/243f8795-b01d-4b75-aa53-24447db9809b/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/243f8795-b01d-4b75-aa53-24447db9809b",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-28",
+                    "format": "API",
                     "modified": "2024-05-28",
-                    "temporal": "2024-05-19/2024-05-25"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/243f8795-b01d-4b75-aa53-24447db9809b",
+                    "temporal": "2024-05-19/2024-05-25",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-28"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/e3d903e4-f090-434e-93e5-5d724769157f/FISS_AR_20240520.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bb50957d-5f42-43e6-baa2-97732d270559",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-21",
                     "modified": "2024-05-21",
-                    "temporal": "2024-05-12/2024-05-18"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bb50957d-5f42-43e6-baa2-97732d270559",
+                    "temporal": "2024-05-12/2024-05-18",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-21"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/bb50957d-5f42-43e6-baa2-97732d270559/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bb50957d-5f42-43e6-baa2-97732d270559",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-21",
+                    "format": "API",
                     "modified": "2024-05-21",
-                    "temporal": "2024-05-12/2024-05-18"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bb50957d-5f42-43e6-baa2-97732d270559",
+                    "temporal": "2024-05-12/2024-05-18",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-21"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/21971043-4460-4e4f-8c33-bfa662c3bb3d/FISS_AR_20240516.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5273263b-438e-4790-8708-76c5b77e71f7",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-17",
                     "modified": "2024-05-17",
-                    "temporal": "2024-05-05/2024-05-11"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5273263b-438e-4790-8708-76c5b77e71f7",
+                    "temporal": "2024-05-05/2024-05-11",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-17"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/5273263b-438e-4790-8708-76c5b77e71f7/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5273263b-438e-4790-8708-76c5b77e71f7",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-17",
+                    "format": "API",
                     "modified": "2024-05-17",
-                    "temporal": "2024-05-05/2024-05-11"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5273263b-438e-4790-8708-76c5b77e71f7",
+                    "temporal": "2024-05-05/2024-05-11",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-17"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/84ce3651-e545-46e9-86de-3b310e927285/FISS_AR_20240513.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7358d903-e410-4ff0-8d47-2f90004e6d68",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-14",
                     "modified": "2024-05-14",
-                    "temporal": "2024-05-05/2024-05-11"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7358d903-e410-4ff0-8d47-2f90004e6d68",
+                    "temporal": "2024-05-05/2024-05-11",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-14"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/7358d903-e410-4ff0-8d47-2f90004e6d68/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7358d903-e410-4ff0-8d47-2f90004e6d68",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-14",
+                    "format": "API",
                     "modified": "2024-05-14",
-                    "temporal": "2024-05-05/2024-05-11"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7358d903-e410-4ff0-8d47-2f90004e6d68",
+                    "temporal": "2024-05-05/2024-05-11",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-14"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/646706c4-6d8c-40ed-90a0-fcc03e0857b9/FISS_AR_20240509.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/01ad7b7f-5e87-4a8d-80e9-b74ddda0ee34",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-10",
                     "modified": "2024-05-10",
-                    "temporal": "2024-04-28/2024-05-04"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/01ad7b7f-5e87-4a8d-80e9-b74ddda0ee34",
+                    "temporal": "2024-04-28/2024-05-04",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-10"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/01ad7b7f-5e87-4a8d-80e9-b74ddda0ee34/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/01ad7b7f-5e87-4a8d-80e9-b74ddda0ee34",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-10",
+                    "format": "API",
                     "modified": "2024-05-10",
-                    "temporal": "2024-04-28/2024-05-04"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/01ad7b7f-5e87-4a8d-80e9-b74ddda0ee34",
+                    "temporal": "2024-04-28/2024-05-04",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-10"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/de2cb741-8742-49f7-91a6-8ab3c499751d/FISS_AR_20240506.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4049fe60-811c-48e1-a93a-92964940e2d3",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-07",
                     "modified": "2024-05-07",
-                    "temporal": "2024-04-28/2024-05-04"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4049fe60-811c-48e1-a93a-92964940e2d3",
+                    "temporal": "2024-04-28/2024-05-04",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-07"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/4049fe60-811c-48e1-a93a-92964940e2d3/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4049fe60-811c-48e1-a93a-92964940e2d3",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-07",
+                    "format": "API",
                     "modified": "2024-05-07",
-                    "temporal": "2024-04-28/2024-05-04"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4049fe60-811c-48e1-a93a-92964940e2d3",
+                    "temporal": "2024-04-28/2024-05-04",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-07"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/4a67eac5-cb96-4085-b319-b78549d69bd9/FISS_AR_20240502.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/49031519-53af-4bf2-b370-73641b046296",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-03",
                     "modified": "2024-05-03",
-                    "temporal": "2024-04-21/2024-04-27"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/49031519-53af-4bf2-b370-73641b046296",
+                    "temporal": "2024-04-21/2024-04-27",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-03"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/49031519-53af-4bf2-b370-73641b046296/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/49031519-53af-4bf2-b370-73641b046296",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-03",
+                    "format": "API",
                     "modified": "2024-05-03",
-                    "temporal": "2024-04-21/2024-04-27"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/49031519-53af-4bf2-b370-73641b046296",
+                    "temporal": "2024-04-21/2024-04-27",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-03"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/efc05f60-389d-4f9c-a011-17bd27524274/FISS_AR_20240429.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/daa70c47-280b-4ea8-80ed-eee7e7d854e5",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-30",
                     "modified": "2024-04-30",
-                    "temporal": "2024-04-21/2024-04-27"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/daa70c47-280b-4ea8-80ed-eee7e7d854e5",
+                    "temporal": "2024-04-21/2024-04-27",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-30"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/daa70c47-280b-4ea8-80ed-eee7e7d854e5/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/daa70c47-280b-4ea8-80ed-eee7e7d854e5",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-30",
+                    "format": "API",
                     "modified": "2024-04-30",
-                    "temporal": "2024-04-21/2024-04-27"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/daa70c47-280b-4ea8-80ed-eee7e7d854e5",
+                    "temporal": "2024-04-21/2024-04-27",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-30"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/09dea68b-78d2-4b3f-ac56-5131c3c7d738/FISS_AR_20240425.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6e148086-b09a-4be5-afd0-c88500f889ea",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-26",
                     "modified": "2024-04-26",
-                    "temporal": "2024-04-14/2024-04-20"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6e148086-b09a-4be5-afd0-c88500f889ea",
+                    "temporal": "2024-04-14/2024-04-20",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-26"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/6e148086-b09a-4be5-afd0-c88500f889ea/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6e148086-b09a-4be5-afd0-c88500f889ea",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-26",
+                    "format": "API",
                     "modified": "2024-04-26",
-                    "temporal": "2024-04-14/2024-04-20"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6e148086-b09a-4be5-afd0-c88500f889ea",
+                    "temporal": "2024-04-14/2024-04-20",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-26"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/4b7b8b7d-37c8-4e21-81ef-1efd631e8b25/FISS_AR_20240422.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a15b8f30-0e10-48ac-ae06-974df43aa567",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-23",
                     "modified": "2024-04-23",
-                    "temporal": "2024-04-14/2024-04-20"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a15b8f30-0e10-48ac-ae06-974df43aa567",
+                    "temporal": "2024-04-14/2024-04-20",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-23"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/a15b8f30-0e10-48ac-ae06-974df43aa567/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a15b8f30-0e10-48ac-ae06-974df43aa567",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-23",
+                    "format": "API",
                     "modified": "2024-04-23",
-                    "temporal": "2024-04-14/2024-04-20"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a15b8f30-0e10-48ac-ae06-974df43aa567",
+                    "temporal": "2024-04-14/2024-04-20",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-23"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/1a270571-1903-4301-ae89-fded1e7ab0b0/FISS_AR_20240418.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4889910f-06d7-4c8c-9d7b-8069b9be8907",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-19",
                     "modified": "2024-04-19",
-                    "temporal": "2024-04-07/2024-04-13"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4889910f-06d7-4c8c-9d7b-8069b9be8907",
+                    "temporal": "2024-04-07/2024-04-13",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-19"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/4889910f-06d7-4c8c-9d7b-8069b9be8907/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4889910f-06d7-4c8c-9d7b-8069b9be8907",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-19",
+                    "format": "API",
                     "modified": "2024-04-19",
-                    "temporal": "2024-04-07/2024-04-13"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4889910f-06d7-4c8c-9d7b-8069b9be8907",
+                    "temporal": "2024-04-07/2024-04-13",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-19"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/71e5d150-0a7b-415c-8292-2cae6e4b8632/FISS_AR_20240415.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/65d6de54-53b3-4088-94a8-d9f658b0662c",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-16",
                     "modified": "2024-04-16",
-                    "temporal": "2024-04-07/2024-04-13"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/65d6de54-53b3-4088-94a8-d9f658b0662c",
+                    "temporal": "2024-04-07/2024-04-13",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-16"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/65d6de54-53b3-4088-94a8-d9f658b0662c/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/65d6de54-53b3-4088-94a8-d9f658b0662c",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-16",
+                    "format": "API",
                     "modified": "2024-04-16",
-                    "temporal": "2024-04-07/2024-04-13"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/65d6de54-53b3-4088-94a8-d9f658b0662c",
+                    "temporal": "2024-04-07/2024-04-13",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-16"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/e88c06da-384e-4214-99a7-88138b619306/FISS_AR_20240411.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e43701de-6010-454c-a580-faac98366a82",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-12",
                     "modified": "2024-04-12",
-                    "temporal": "2024-03-31/2024-04-06"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e43701de-6010-454c-a580-faac98366a82",
+                    "temporal": "2024-03-31/2024-04-06",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-12"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/e43701de-6010-454c-a580-faac98366a82/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e43701de-6010-454c-a580-faac98366a82",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-12",
+                    "format": "API",
                     "modified": "2024-04-12",
-                    "temporal": "2024-03-31/2024-04-06"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e43701de-6010-454c-a580-faac98366a82",
+                    "temporal": "2024-03-31/2024-04-06",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-12"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/36ba7388-e6b0-4249-91c6-b714eb2003b6/FISS_AR_20240408.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3997a8e1-5710-4448-8066-7e6474be0458",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-09",
                     "modified": "2024-04-09",
-                    "temporal": "2024-03-31/2024-04-06"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3997a8e1-5710-4448-8066-7e6474be0458",
+                    "temporal": "2024-03-31/2024-04-06",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-09"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/3997a8e1-5710-4448-8066-7e6474be0458/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3997a8e1-5710-4448-8066-7e6474be0458",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-09",
+                    "format": "API",
                     "modified": "2024-04-09",
-                    "temporal": "2024-03-31/2024-04-06"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3997a8e1-5710-4448-8066-7e6474be0458",
+                    "temporal": "2024-03-31/2024-04-06",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-09"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/47225ab9-f424-4c67-a286-869f47a08ea5/FISS_AR_20240404.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/20dee1c9-c321-4557-bb6d-7c0892fb8fa0",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-05",
                     "modified": "2024-04-05",
-                    "temporal": "2024-03-24/2024-03-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/20dee1c9-c321-4557-bb6d-7c0892fb8fa0",
+                    "temporal": "2024-03-24/2024-03-30",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-05"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/20dee1c9-c321-4557-bb6d-7c0892fb8fa0/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/20dee1c9-c321-4557-bb6d-7c0892fb8fa0",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-05",
+                    "format": "API",
                     "modified": "2024-04-05",
-                    "temporal": "2024-03-24/2024-03-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/20dee1c9-c321-4557-bb6d-7c0892fb8fa0",
+                    "temporal": "2024-03-24/2024-03-30",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-05"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/29350c78-dbeb-41b8-8295-bd2f57f7c5d4/FISS_AR_20240401.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0eea222d-6d27-44f2-bf71-61b1f77ee53f",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-02",
                     "modified": "2024-04-02",
-                    "temporal": "2024-03-24/2024-03-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0eea222d-6d27-44f2-bf71-61b1f77ee53f",
+                    "temporal": "2024-03-24/2024-03-30",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-02"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/0eea222d-6d27-44f2-bf71-61b1f77ee53f/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0eea222d-6d27-44f2-bf71-61b1f77ee53f",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-02",
+                    "format": "API",
                     "modified": "2024-04-02",
-                    "temporal": "2024-03-24/2024-03-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0eea222d-6d27-44f2-bf71-61b1f77ee53f",
+                    "temporal": "2024-03-24/2024-03-30",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-02"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/674f8851-f28d-4211-9ecc-ce0b9c9fbc71/FISS_AR_20240328.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ec3e4892-bfcd-42fd-adb7-21cd0b693fe5",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-29",
                     "modified": "2024-03-29",
-                    "temporal": "2024-03-17/2024-03-23"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ec3e4892-bfcd-42fd-adb7-21cd0b693fe5",
+                    "temporal": "2024-03-17/2024-03-23",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-29"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/ec3e4892-bfcd-42fd-adb7-21cd0b693fe5/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ec3e4892-bfcd-42fd-adb7-21cd0b693fe5",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-29",
+                    "format": "API",
                     "modified": "2024-03-29",
-                    "temporal": "2024-03-17/2024-03-23"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ec3e4892-bfcd-42fd-adb7-21cd0b693fe5",
+                    "temporal": "2024-03-17/2024-03-23",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-29"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/f4c56758-a1f1-4786-88dd-b4bd55cf62bb/FISS_AR_20240325.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/eb191fc1-81ba-46f3-bfa6-bde5bb53df8a",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-26",
                     "modified": "2024-03-26",
-                    "temporal": "2024-03-17/2024-03-23"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/eb191fc1-81ba-46f3-bfa6-bde5bb53df8a",
+                    "temporal": "2024-03-17/2024-03-23",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-26"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/eb191fc1-81ba-46f3-bfa6-bde5bb53df8a/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/eb191fc1-81ba-46f3-bfa6-bde5bb53df8a",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-26",
+                    "format": "API",
                     "modified": "2024-03-26",
-                    "temporal": "2024-03-17/2024-03-23"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/eb191fc1-81ba-46f3-bfa6-bde5bb53df8a",
+                    "temporal": "2024-03-17/2024-03-23",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-26"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/a12729f5-994a-4a6f-98a7-f18a6dae8f02/FISS_AR_20240321.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/573d1ead-92c8-418b-a2f0-17b3dd79049a",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-22",
                     "modified": "2024-03-22",
-                    "temporal": "2024-03-10/2024-03-16"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/573d1ead-92c8-418b-a2f0-17b3dd79049a",
+                    "temporal": "2024-03-10/2024-03-16",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-22"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/573d1ead-92c8-418b-a2f0-17b3dd79049a/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/573d1ead-92c8-418b-a2f0-17b3dd79049a",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-22",
+                    "format": "API",
                     "modified": "2024-03-22",
-                    "temporal": "2024-03-10/2024-03-16"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/573d1ead-92c8-418b-a2f0-17b3dd79049a",
+                    "temporal": "2024-03-10/2024-03-16",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-22"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/c5d80789-22d2-4a66-abb9-99d3fb1639d1/FISS_AR_20240318.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ff87c616-dd2e-4e4d-ab23-62d1c16ad16b",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-19",
                     "modified": "2024-03-19",
-                    "temporal": "2024-03-10/2024-03-16"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ff87c616-dd2e-4e4d-ab23-62d1c16ad16b",
+                    "temporal": "2024-03-10/2024-03-16",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-19"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/ff87c616-dd2e-4e4d-ab23-62d1c16ad16b/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ff87c616-dd2e-4e4d-ab23-62d1c16ad16b",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-19",
+                    "format": "API",
                     "modified": "2024-03-19",
-                    "temporal": "2024-03-10/2024-03-16"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ff87c616-dd2e-4e4d-ab23-62d1c16ad16b",
+                    "temporal": "2024-03-10/2024-03-16",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-19"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/cbdc1069-10da-4cb0-85ef-56b89f1bd9c2/FISS_AR_20240314.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d4e7a5a7-95b6-46eb-8ee9-23f51df42cd6",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-15",
                     "modified": "2024-03-15",
-                    "temporal": "2024-03-03/2024-03-09"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d4e7a5a7-95b6-46eb-8ee9-23f51df42cd6",
+                    "temporal": "2024-03-03/2024-03-09",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-15"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/d4e7a5a7-95b6-46eb-8ee9-23f51df42cd6/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d4e7a5a7-95b6-46eb-8ee9-23f51df42cd6",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-15",
+                    "format": "API",
                     "modified": "2024-03-15",
-                    "temporal": "2024-03-03/2024-03-09"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d4e7a5a7-95b6-46eb-8ee9-23f51df42cd6",
+                    "temporal": "2024-03-03/2024-03-09",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/f9caaef4-c904-4863-96a8-13be57e27b67/FISS_AR_20240311.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f84b09ad-b3a1-412d-a5ed-b9c3743027a8",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-12",
                     "modified": "2024-03-12",
-                    "temporal": "2024-03-03/2024-03-09"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f84b09ad-b3a1-412d-a5ed-b9c3743027a8",
+                    "temporal": "2024-03-03/2024-03-09",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-12"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/f84b09ad-b3a1-412d-a5ed-b9c3743027a8/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f84b09ad-b3a1-412d-a5ed-b9c3743027a8",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-12",
+                    "format": "API",
                     "modified": "2024-03-12",
-                    "temporal": "2024-03-03/2024-03-09"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f84b09ad-b3a1-412d-a5ed-b9c3743027a8",
+                    "temporal": "2024-03-03/2024-03-09",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-12"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/f6de1ecd-f63d-4d45-8fca-21cc49dcde98/FISS_AR_20240307.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4d502a4d-0be6-44c7-a1f5-d3e23a74e4f1",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-08",
                     "modified": "2024-03-08",
-                    "temporal": "2024-02-25/2024-03-02"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4d502a4d-0be6-44c7-a1f5-d3e23a74e4f1",
+                    "temporal": "2024-02-25/2024-03-02",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-08"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/4d502a4d-0be6-44c7-a1f5-d3e23a74e4f1/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4d502a4d-0be6-44c7-a1f5-d3e23a74e4f1",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-08",
+                    "format": "API",
                     "modified": "2024-03-08",
-                    "temporal": "2024-02-25/2024-03-02"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4d502a4d-0be6-44c7-a1f5-d3e23a74e4f1",
+                    "temporal": "2024-02-25/2024-03-02",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-08"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/442ecb71-b990-4766-8d7f-81bf42e57bed/FISS_AR_20240304.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c6a80c91-e507-43f1-8903-192e25b6ce31",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-05",
                     "modified": "2024-03-05",
-                    "temporal": "2024-02-25/2024-03-02"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c6a80c91-e507-43f1-8903-192e25b6ce31",
+                    "temporal": "2024-02-25/2024-03-02",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-05"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/c6a80c91-e507-43f1-8903-192e25b6ce31/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c6a80c91-e507-43f1-8903-192e25b6ce31",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-05",
+                    "format": "API",
                     "modified": "2024-03-05",
-                    "temporal": "2024-02-25/2024-03-02"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c6a80c91-e507-43f1-8903-192e25b6ce31",
+                    "temporal": "2024-02-25/2024-03-02",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-05"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/782673b2-6877-4f1b-b3ce-7d0594dee84a/FISS_AR_20240229.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/027f07ad-9b98-4f80-8f79-c21e408b5ebc",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-01",
                     "modified": "2024-03-01",
-                    "temporal": "2024-02-18/2024-02-24"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/027f07ad-9b98-4f80-8f79-c21e408b5ebc",
+                    "temporal": "2024-02-18/2024-02-24",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/027f07ad-9b98-4f80-8f79-c21e408b5ebc/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/027f07ad-9b98-4f80-8f79-c21e408b5ebc",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-01",
+                    "format": "API",
                     "modified": "2024-03-01",
-                    "temporal": "2024-02-18/2024-02-24"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/027f07ad-9b98-4f80-8f79-c21e408b5ebc",
+                    "temporal": "2024-02-18/2024-02-24",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/75d2b77e-1b1a-47c5-b56b-a4a7bc14509e/FISS_AR_20240226.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5fb5b043-4030-487c-8fc7-f4ccdf9483eb",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-27",
                     "modified": "2024-02-27",
-                    "temporal": "2024-02-18/2024-02-24"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5fb5b043-4030-487c-8fc7-f4ccdf9483eb",
+                    "temporal": "2024-02-18/2024-02-24",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-27"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/5fb5b043-4030-487c-8fc7-f4ccdf9483eb/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5fb5b043-4030-487c-8fc7-f4ccdf9483eb",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-27",
+                    "format": "API",
                     "modified": "2024-02-27",
-                    "temporal": "2024-02-18/2024-02-24"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5fb5b043-4030-487c-8fc7-f4ccdf9483eb",
+                    "temporal": "2024-02-18/2024-02-24",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-27"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/930d6e59-b7f2-45bd-b8ab-87e9ca0e4686/FISS_AR_20240222.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/525ce3e3-1e30-4311-b9ad-41b7bdb44860",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-23",
                     "modified": "2024-02-23",
-                    "temporal": "2024-02-11/2024-02-17"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/525ce3e3-1e30-4311-b9ad-41b7bdb44860",
+                    "temporal": "2024-02-11/2024-02-17",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-23"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/525ce3e3-1e30-4311-b9ad-41b7bdb44860/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/525ce3e3-1e30-4311-b9ad-41b7bdb44860",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-23",
+                    "format": "API",
                     "modified": "2024-02-23",
-                    "temporal": "2024-02-11/2024-02-17"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/525ce3e3-1e30-4311-b9ad-41b7bdb44860",
+                    "temporal": "2024-02-11/2024-02-17",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-23"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/34614b33-c9b6-4f7f-87cd-6f5038fa3c5f/FISS_AR_20240220.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2c60e94f-862c-488a-99c4-ed7e56d5d6e0",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-21",
                     "modified": "2024-02-21",
-                    "temporal": "2024-02-11/2024-02-17"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2c60e94f-862c-488a-99c4-ed7e56d5d6e0",
+                    "temporal": "2024-02-11/2024-02-17",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-21"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/2c60e94f-862c-488a-99c4-ed7e56d5d6e0/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2c60e94f-862c-488a-99c4-ed7e56d5d6e0",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-21",
+                    "format": "API",
                     "modified": "2024-02-21",
-                    "temporal": "2024-02-11/2024-02-17"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2c60e94f-862c-488a-99c4-ed7e56d5d6e0",
+                    "temporal": "2024-02-11/2024-02-17",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-21"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/c854c01a-c63a-4cce-9eae-13261295c6fc/FISS_AR_20240215.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d27b01b0-f266-4665-a33d-1b9c0a740aed",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-16",
                     "modified": "2024-02-16",
-                    "temporal": "2024-02-04/2024-02-10"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d27b01b0-f266-4665-a33d-1b9c0a740aed",
+                    "temporal": "2024-02-04/2024-02-10",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-16"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/d27b01b0-f266-4665-a33d-1b9c0a740aed/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d27b01b0-f266-4665-a33d-1b9c0a740aed",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-16",
+                    "format": "API",
                     "modified": "2024-02-16",
-                    "temporal": "2024-02-04/2024-02-10"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d27b01b0-f266-4665-a33d-1b9c0a740aed",
+                    "temporal": "2024-02-04/2024-02-10",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-16"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/f705f608-f082-47e5-97f5-c8e6dc9d8715/FISS_AR_20240212.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/40535bb5-6033-4edd-91bc-8a874670028e",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-13",
                     "modified": "2024-02-13",
-                    "temporal": "2024-02-04/2024-02-10"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/40535bb5-6033-4edd-91bc-8a874670028e",
+                    "temporal": "2024-02-04/2024-02-10",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-13"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/40535bb5-6033-4edd-91bc-8a874670028e/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/40535bb5-6033-4edd-91bc-8a874670028e",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-13",
+                    "format": "API",
                     "modified": "2024-02-13",
-                    "temporal": "2024-02-04/2024-02-10"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/40535bb5-6033-4edd-91bc-8a874670028e",
+                    "temporal": "2024-02-04/2024-02-10",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-13"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/2a8cc37b-8d66-4c6c-99c2-735c44a7252f/FISS_AR_20240208.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/333a55b5-2c6a-4d4f-9ff2-27752fb618ba",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-09",
                     "modified": "2024-02-09",
-                    "temporal": "2024-01-28/2024-02-03"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/333a55b5-2c6a-4d4f-9ff2-27752fb618ba",
+                    "temporal": "2024-01-28/2024-02-03",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-09"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/333a55b5-2c6a-4d4f-9ff2-27752fb618ba/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/333a55b5-2c6a-4d4f-9ff2-27752fb618ba",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-09",
+                    "format": "API",
                     "modified": "2024-02-09",
-                    "temporal": "2024-01-28/2024-02-03"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/333a55b5-2c6a-4d4f-9ff2-27752fb618ba",
+                    "temporal": "2024-01-28/2024-02-03",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-09"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/4d295a3e-7742-4fde-ad3f-12bc46d03da1/FISS_AR_20240205.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/676c46d4-9dd1-4c3e-a2d7-7a821e3fcade",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-06",
                     "modified": "2024-02-06",
-                    "temporal": "2024-01-28/2024-02-03"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/676c46d4-9dd1-4c3e-a2d7-7a821e3fcade",
+                    "temporal": "2024-01-28/2024-02-03",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-06"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/676c46d4-9dd1-4c3e-a2d7-7a821e3fcade/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/676c46d4-9dd1-4c3e-a2d7-7a821e3fcade",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-06",
+                    "format": "API",
                     "modified": "2024-02-06",
-                    "temporal": "2024-01-28/2024-02-03"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/676c46d4-9dd1-4c3e-a2d7-7a821e3fcade",
+                    "temporal": "2024-01-28/2024-02-03",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-06"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/8a20dbe9-c9c5-4293-bc50-1c31410f73b0/FISS_AR_20240202.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/005caef9-888c-48de-bedd-fd277ed99b16",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-02",
                     "modified": "2024-02-02",
-                    "temporal": "2024-01-21/2024-01-27"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/005caef9-888c-48de-bedd-fd277ed99b16",
+                    "temporal": "2024-01-21/2024-01-27",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-02"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/005caef9-888c-48de-bedd-fd277ed99b16/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/005caef9-888c-48de-bedd-fd277ed99b16",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-02",
+                    "format": "API",
                     "modified": "2024-02-02",
-                    "temporal": "2024-01-21/2024-01-27"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/005caef9-888c-48de-bedd-fd277ed99b16",
+                    "temporal": "2024-01-21/2024-01-27",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-02"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/15a6984f-1f54-4438-82b5-26fc66cc4557/FISS_AR_20240129.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/74c4ef9a-204a-4b8e-80a0-5597652e9336",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-30",
                     "modified": "2024-01-30",
-                    "temporal": "2024-01-21/2024-01-27"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/74c4ef9a-204a-4b8e-80a0-5597652e9336",
+                    "temporal": "2024-01-21/2024-01-27",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-30"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/74c4ef9a-204a-4b8e-80a0-5597652e9336/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/74c4ef9a-204a-4b8e-80a0-5597652e9336",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-30",
+                    "format": "API",
                     "modified": "2024-01-30",
-                    "temporal": "2024-01-21/2024-01-27"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/74c4ef9a-204a-4b8e-80a0-5597652e9336",
+                    "temporal": "2024-01-21/2024-01-27",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-30"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/08ef4657-4669-468b-836e-15a407817a55/FISS_AR_20240126.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4631bbb6-3924-421d-9f2d-f16d6b2526b4",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-26",
                     "modified": "2024-01-26",
-                    "temporal": "2024-01-14/2024-01-20"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4631bbb6-3924-421d-9f2d-f16d6b2526b4",
+                    "temporal": "2024-01-14/2024-01-20",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-26"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/4631bbb6-3924-421d-9f2d-f16d6b2526b4/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4631bbb6-3924-421d-9f2d-f16d6b2526b4",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-26",
+                    "format": "API",
                     "modified": "2024-01-26",
-                    "temporal": "2024-01-14/2024-01-20"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4631bbb6-3924-421d-9f2d-f16d6b2526b4",
+                    "temporal": "2024-01-14/2024-01-20",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-26"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/1bdf9b0b-386b-4f7f-b9dc-3b48ab94c887/FISS_AR_20240122.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bd0bb369-dbe6-40ab-8729-7113f1ac64c0",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-23",
                     "modified": "2024-01-23",
-                    "temporal": "2024-01-14/2024-01-20"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bd0bb369-dbe6-40ab-8729-7113f1ac64c0",
+                    "temporal": "2024-01-14/2024-01-20",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-23"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/bd0bb369-dbe6-40ab-8729-7113f1ac64c0/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bd0bb369-dbe6-40ab-8729-7113f1ac64c0",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-23",
+                    "format": "API",
                     "modified": "2024-01-23",
-                    "temporal": "2024-01-14/2024-01-20"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bd0bb369-dbe6-40ab-8729-7113f1ac64c0",
+                    "temporal": "2024-01-14/2024-01-20",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-23"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/65a06865-4edc-4e8d-a151-a5bfa953c314/FISS_AR_20240119.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/93f797c5-3a27-44ba-9a35-16fa1b9f19b1",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-19",
                     "modified": "2024-01-19",
-                    "temporal": "2024-01-07/2024-01-13"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/93f797c5-3a27-44ba-9a35-16fa1b9f19b1",
+                    "temporal": "2024-01-07/2024-01-13",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-19"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/93f797c5-3a27-44ba-9a35-16fa1b9f19b1/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/93f797c5-3a27-44ba-9a35-16fa1b9f19b1",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-19",
+                    "format": "API",
                     "modified": "2024-01-19",
-                    "temporal": "2024-01-07/2024-01-13"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/93f797c5-3a27-44ba-9a35-16fa1b9f19b1",
+                    "temporal": "2024-01-07/2024-01-13",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-19"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/5d2895e2-4c32-4a1c-a320-058b4ebdd919/FISS_AR_20240115.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a4213a34-e7db-4e7b-9f3b-ade91b81d957",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-16",
                     "modified": "2024-01-16",
-                    "temporal": "2024-01-07/2024-01-13"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a4213a34-e7db-4e7b-9f3b-ade91b81d957",
+                    "temporal": "2024-01-07/2024-01-13",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-16"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/a4213a34-e7db-4e7b-9f3b-ade91b81d957/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a4213a34-e7db-4e7b-9f3b-ade91b81d957",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-16",
+                    "format": "API",
                     "modified": "2024-01-16",
-                    "temporal": "2024-01-07/2024-01-13"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a4213a34-e7db-4e7b-9f3b-ade91b81d957",
+                    "temporal": "2024-01-07/2024-01-13",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-16"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/19dbdb50-117e-4aec-918b-f21da3d8d471/FISS_AR_20240111.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e1e0c962-89ea-4452-8576-74b166309bcd",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-12",
                     "modified": "2024-01-12",
-                    "temporal": "2023-12-31/2024-01-06"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e1e0c962-89ea-4452-8576-74b166309bcd",
+                    "temporal": "2023-12-31/2024-01-06",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-12"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/e1e0c962-89ea-4452-8576-74b166309bcd/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e1e0c962-89ea-4452-8576-74b166309bcd",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-12",
+                    "format": "API",
                     "modified": "2024-01-12",
-                    "temporal": "2023-12-31/2024-01-06"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e1e0c962-89ea-4452-8576-74b166309bcd",
+                    "temporal": "2023-12-31/2024-01-06",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-12"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/665557d7-32f6-438b-bb89-a2f490832ad4/FISS_AR_20240108.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b11141bc-9352-4692-9215-6269c40c686d",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-09",
                     "modified": "2024-01-09",
-                    "temporal": "2023-12-31/2024-01-06"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b11141bc-9352-4692-9215-6269c40c686d",
+                    "temporal": "2023-12-31/2024-01-06",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-09"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/b11141bc-9352-4692-9215-6269c40c686d/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b11141bc-9352-4692-9215-6269c40c686d",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-09",
+                    "format": "API",
                     "modified": "2024-01-09",
-                    "temporal": "2023-12-31/2024-01-06"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b11141bc-9352-4692-9215-6269c40c686d",
+                    "temporal": "2023-12-31/2024-01-06",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-09"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/a78aa3e4-42d0-4c74-8ea6-2bed183c931e/FISS_AR_20240104.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ed5f8ef0-66a4-4afd-9980-4bf529c541ea",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-05",
                     "modified": "2024-01-05",
-                    "temporal": "2023-12-24/2023-12-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ed5f8ef0-66a4-4afd-9980-4bf529c541ea",
+                    "temporal": "2023-12-24/2023-12-30",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-05"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/ed5f8ef0-66a4-4afd-9980-4bf529c541ea/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ed5f8ef0-66a4-4afd-9980-4bf529c541ea",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-05",
+                    "format": "API",
                     "modified": "2024-01-05",
-                    "temporal": "2023-12-24/2023-12-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ed5f8ef0-66a4-4afd-9980-4bf529c541ea",
+                    "temporal": "2023-12-24/2023-12-30",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-05"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/63cb649d-d0a9-4c31-a6e1-882a2b262a08/FISS_AR_20240102.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5d1a8be3-1d4e-4d49-870d-fdcf2ca27846",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-03",
                     "modified": "2024-01-03",
-                    "temporal": "2023-12-24/2023-12-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5d1a8be3-1d4e-4d49-870d-fdcf2ca27846",
+                    "temporal": "2023-12-24/2023-12-30",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-03"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/5d1a8be3-1d4e-4d49-870d-fdcf2ca27846/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5d1a8be3-1d4e-4d49-870d-fdcf2ca27846",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-03",
+                    "format": "API",
                     "modified": "2024-01-03",
-                    "temporal": "2023-12-24/2023-12-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5d1a8be3-1d4e-4d49-870d-fdcf2ca27846",
+                    "temporal": "2023-12-24/2023-12-30",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-03"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/3c512f2a-e2cd-41af-a988-d41b48cec9bf/FISS_AR_20231228.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/14ddd928-dbe5-470a-8a5a-55183b13494d",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-29",
                     "modified": "2023-12-29",
-                    "temporal": "2023-12-17/2023-12-23"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/14ddd928-dbe5-470a-8a5a-55183b13494d",
+                    "temporal": "2023-12-17/2023-12-23",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-29"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/14ddd928-dbe5-470a-8a5a-55183b13494d/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/14ddd928-dbe5-470a-8a5a-55183b13494d",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-29",
+                    "format": "API",
                     "modified": "2023-12-29",
-                    "temporal": "2023-12-17/2023-12-23"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/14ddd928-dbe5-470a-8a5a-55183b13494d",
+                    "temporal": "2023-12-17/2023-12-23",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-29"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/ca45f782-f275-44b1-9dcb-568aa8d21862/FISS_AR_20231226.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4041b8f9-b70b-4c82-94db-244bf7c123b3",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-27",
                     "modified": "2023-12-27",
-                    "temporal": "2023-12-17/2023-12-23"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4041b8f9-b70b-4c82-94db-244bf7c123b3",
+                    "temporal": "2023-12-17/2023-12-23",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-27"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/4041b8f9-b70b-4c82-94db-244bf7c123b3/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4041b8f9-b70b-4c82-94db-244bf7c123b3",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-27",
+                    "format": "API",
                     "modified": "2023-12-27",
-                    "temporal": "2023-12-17/2023-12-23"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4041b8f9-b70b-4c82-94db-244bf7c123b3",
+                    "temporal": "2023-12-17/2023-12-23",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-27"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/416e9ade-3624-4a17-a833-6253d0602458/FISS_AR_20231221.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/65ade0ce-5255-40ea-8e22-b9dc790e406a",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-22",
                     "modified": "2023-12-22",
-                    "temporal": "2023-12-10/2023-12-16"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/65ade0ce-5255-40ea-8e22-b9dc790e406a",
+                    "temporal": "2023-12-10/2023-12-16",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-22"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/65ade0ce-5255-40ea-8e22-b9dc790e406a/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/65ade0ce-5255-40ea-8e22-b9dc790e406a",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-22",
+                    "format": "API",
                     "modified": "2023-12-22",
-                    "temporal": "2023-12-10/2023-12-16"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/65ade0ce-5255-40ea-8e22-b9dc790e406a",
+                    "temporal": "2023-12-10/2023-12-16",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-22"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/df86c744-b2c4-49c0-ba4f-ef6a245f0763/FISS_AR_20231218.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6709c6b9-5457-410d-a792-5797d7161e93",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-19",
                     "modified": "2023-12-19",
-                    "temporal": "2023-12-10/2023-12-16"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6709c6b9-5457-410d-a792-5797d7161e93",
+                    "temporal": "2023-12-10/2023-12-16",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-19"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/6709c6b9-5457-410d-a792-5797d7161e93/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6709c6b9-5457-410d-a792-5797d7161e93",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-19",
+                    "format": "API",
                     "modified": "2023-12-19",
-                    "temporal": "2023-12-10/2023-12-16"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6709c6b9-5457-410d-a792-5797d7161e93",
+                    "temporal": "2023-12-10/2023-12-16",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-19"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/6d665cdb-a8bc-486f-ae1e-4872e5db13c8/FISS_AR_20231214.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/02cb5188-011c-4093-ae92-3570c287d7cc",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-15",
                     "modified": "2023-12-15",
-                    "temporal": "2023-12-03/2023-12-09"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/02cb5188-011c-4093-ae92-3570c287d7cc",
+                    "temporal": "2023-12-03/2023-12-09",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-15"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/02cb5188-011c-4093-ae92-3570c287d7cc/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/02cb5188-011c-4093-ae92-3570c287d7cc",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-15",
+                    "format": "API",
                     "modified": "2023-12-15",
-                    "temporal": "2023-12-03/2023-12-09"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/02cb5188-011c-4093-ae92-3570c287d7cc",
+                    "temporal": "2023-12-03/2023-12-09",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/2606f0c8-8c44-49d4-9b5b-12fbfeb3aa11/FISS_AR_20231211.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1043fa1a-421c-40c1-ab63-0e087633823e",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-11",
                     "modified": "2023-12-11",
-                    "temporal": "2023-12-03/2023-12-09"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1043fa1a-421c-40c1-ab63-0e087633823e",
+                    "temporal": "2023-12-03/2023-12-09",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-11"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/1043fa1a-421c-40c1-ab63-0e087633823e/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1043fa1a-421c-40c1-ab63-0e087633823e",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-11",
+                    "format": "API",
                     "modified": "2023-12-11",
-                    "temporal": "2023-12-03/2023-12-09"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1043fa1a-421c-40c1-ab63-0e087633823e",
+                    "temporal": "2023-12-03/2023-12-09",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-11"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/22ad40b0-f3b4-4762-8152-c6cf1ff3cc91/FISS_AR_20231207.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b23c7720-893d-4e27-a961-f2738ffc8b3e",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-08",
                     "modified": "2023-12-08",
-                    "temporal": "2023-11-26/2023-12-02"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b23c7720-893d-4e27-a961-f2738ffc8b3e",
+                    "temporal": "2023-11-26/2023-12-02",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-08"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/b23c7720-893d-4e27-a961-f2738ffc8b3e/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b23c7720-893d-4e27-a961-f2738ffc8b3e",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-08",
+                    "format": "API",
                     "modified": "2023-12-08",
-                    "temporal": "2023-11-26/2023-12-02"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b23c7720-893d-4e27-a961-f2738ffc8b3e",
+                    "temporal": "2023-11-26/2023-12-02",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-08"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/0d4f43c1-d87a-4d5a-bad3-f0fe4ddb3de4/FISS_AR_20231204.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4c00c6df-9ac6-4377-85b8-09d9c6b3dfe9",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-05",
                     "modified": "2023-12-05",
-                    "temporal": "2023-11-26/2023-12-02"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4c00c6df-9ac6-4377-85b8-09d9c6b3dfe9",
+                    "temporal": "2023-11-26/2023-12-02",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-05"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/4c00c6df-9ac6-4377-85b8-09d9c6b3dfe9/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4c00c6df-9ac6-4377-85b8-09d9c6b3dfe9",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-05",
+                    "format": "API",
                     "modified": "2023-12-05",
-                    "temporal": "2023-11-26/2023-12-02"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4c00c6df-9ac6-4377-85b8-09d9c6b3dfe9",
+                    "temporal": "2023-11-26/2023-12-02",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-05"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/866d1d67-350b-4eb5-afcc-c064fdfbdf3e/FISS_AR_20231130.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/82e77c44-333c-4628-beaf-91d4c07ef86c",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-01",
                     "modified": "2023-12-01",
-                    "temporal": "2023-11-19/2023-11-25"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/82e77c44-333c-4628-beaf-91d4c07ef86c",
+                    "temporal": "2023-11-19/2023-11-25",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/82e77c44-333c-4628-beaf-91d4c07ef86c/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/82e77c44-333c-4628-beaf-91d4c07ef86c",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-01",
+                    "format": "API",
                     "modified": "2023-12-01",
-                    "temporal": "2023-11-19/2023-11-25"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/82e77c44-333c-4628-beaf-91d4c07ef86c",
+                    "temporal": "2023-11-19/2023-11-25",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/2ecb70a1-ba79-44cc-90ef-90b6da511bfa/FISS_AR_20231127.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2d579af6-7f56-4dec-b704-2354643adc63",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-28",
                     "modified": "2023-11-28",
-                    "temporal": "2023-11-19/2023-11-25"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2d579af6-7f56-4dec-b704-2354643adc63",
+                    "temporal": "2023-11-19/2023-11-25",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-28"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/2d579af6-7f56-4dec-b704-2354643adc63/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2d579af6-7f56-4dec-b704-2354643adc63",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-28",
+                    "format": "API",
                     "modified": "2023-11-28",
-                    "temporal": "2023-11-19/2023-11-25"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2d579af6-7f56-4dec-b704-2354643adc63",
+                    "temporal": "2023-11-19/2023-11-25",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-28"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/3e5e7c31-815b-4f1d-9b4f-75332dc8ab33/FISS_AR_20231122.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1639daa6-6aba-47f2-bf13-74342b9ff295",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-24",
                     "modified": "2023-11-24",
-                    "temporal": "2023-11-12/2023-11-18"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1639daa6-6aba-47f2-bf13-74342b9ff295",
+                    "temporal": "2023-11-12/2023-11-18",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-24"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/1639daa6-6aba-47f2-bf13-74342b9ff295/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1639daa6-6aba-47f2-bf13-74342b9ff295",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-24",
+                    "format": "API",
                     "modified": "2023-11-24",
-                    "temporal": "2023-11-12/2023-11-18"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1639daa6-6aba-47f2-bf13-74342b9ff295",
+                    "temporal": "2023-11-12/2023-11-18",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-24"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/44288098-b7f0-4c08-a859-eb414aae30cc/FISS_AR_20231120.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/46d2b756-d8db-40db-8813-e2ac9699414d",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-21",
                     "modified": "2023-11-21",
-                    "temporal": "2023-11-12/2023-11-18"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/46d2b756-d8db-40db-8813-e2ac9699414d",
+                    "temporal": "2023-11-12/2023-11-18",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-21"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/46d2b756-d8db-40db-8813-e2ac9699414d/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/46d2b756-d8db-40db-8813-e2ac9699414d",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-21",
+                    "format": "API",
                     "modified": "2023-11-21",
-                    "temporal": "2023-11-12/2023-11-18"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/46d2b756-d8db-40db-8813-e2ac9699414d",
+                    "temporal": "2023-11-12/2023-11-18",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-21"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/0b26df43-a784-46bd-9c4b-343695a4ef46/FISS_AR_20231116.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5e5934d3-450e-4879-8f25-a3c43f95f3ef",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-16",
                     "modified": "2023-11-16",
-                    "temporal": "2023-11-05/2023-11-11"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5e5934d3-450e-4879-8f25-a3c43f95f3ef",
+                    "temporal": "2023-11-05/2023-11-11",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-16"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/5e5934d3-450e-4879-8f25-a3c43f95f3ef/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5e5934d3-450e-4879-8f25-a3c43f95f3ef",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-16",
+                    "format": "API",
                     "modified": "2023-11-16",
-                    "temporal": "2023-11-05/2023-11-11"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5e5934d3-450e-4879-8f25-a3c43f95f3ef",
+                    "temporal": "2023-11-05/2023-11-11",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-16"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/5369862b-10cd-4e8a-830a-f18400874712/FISS_AR_20231113.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6058c157-5c7b-4900-b88c-fc24a5680b11",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-14",
                     "modified": "2023-11-14",
-                    "temporal": "2023-11-05/2023-11-11"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6058c157-5c7b-4900-b88c-fc24a5680b11",
+                    "temporal": "2023-11-05/2023-11-11",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-14"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/6058c157-5c7b-4900-b88c-fc24a5680b11/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6058c157-5c7b-4900-b88c-fc24a5680b11",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-14",
+                    "format": "API",
                     "modified": "2023-11-14",
-                    "temporal": "2023-11-05/2023-11-11"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6058c157-5c7b-4900-b88c-fc24a5680b11",
+                    "temporal": "2023-11-05/2023-11-11",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-14"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/7bea4994-86eb-4358-8d19-8f4e904baa15/FISS_AR_20231109.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2001b9c2-40e3-48b8-b607-4442ba0a5ee5",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-09",
                     "modified": "2023-11-09",
-                    "temporal": "2023-10-29/2023-11-04"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2001b9c2-40e3-48b8-b607-4442ba0a5ee5",
+                    "temporal": "2023-10-29/2023-11-04",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-09"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/2001b9c2-40e3-48b8-b607-4442ba0a5ee5/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2001b9c2-40e3-48b8-b607-4442ba0a5ee5",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-09",
+                    "format": "API",
                     "modified": "2023-11-09",
-                    "temporal": "2023-10-29/2023-11-04"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2001b9c2-40e3-48b8-b607-4442ba0a5ee5",
+                    "temporal": "2023-10-29/2023-11-04",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-09"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/60386412-33a8-4a3c-a3de-1168e4864d7b/FISS_AR_20231106.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/cbf0011d-1dcc-408c-a529-8392391ec3af",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-07",
                     "modified": "2023-11-07",
-                    "temporal": "2023-10-29/2023-11-04"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/cbf0011d-1dcc-408c-a529-8392391ec3af",
+                    "temporal": "2023-10-29/2023-11-04",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-07"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/cbf0011d-1dcc-408c-a529-8392391ec3af/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/cbf0011d-1dcc-408c-a529-8392391ec3af",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-07",
+                    "format": "API",
                     "modified": "2023-11-07",
-                    "temporal": "2023-10-29/2023-11-04"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/cbf0011d-1dcc-408c-a529-8392391ec3af",
+                    "temporal": "2023-10-29/2023-11-04",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-07"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/7e8b6d0c-ce01-4e1a-83db-2f0d42ad9fa0/FISS_AR_20231102.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e23c7d89-6145-4b28-a3a6-216168539210",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-03",
                     "modified": "2023-11-03",
-                    "temporal": "2023-10-22/2023-10-28"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e23c7d89-6145-4b28-a3a6-216168539210",
+                    "temporal": "2023-10-22/2023-10-28",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-03"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/e23c7d89-6145-4b28-a3a6-216168539210/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e23c7d89-6145-4b28-a3a6-216168539210",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-03",
+                    "format": "API",
                     "modified": "2023-11-03",
-                    "temporal": "2023-10-22/2023-10-28"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e23c7d89-6145-4b28-a3a6-216168539210",
+                    "temporal": "2023-10-22/2023-10-28",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-03"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/adb4e76c-e40b-436a-a07c-7fe98b68a905/FISS_AR_20231030.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4f64860a-4368-451f-a9d9-ab4e4457f068",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-31",
                     "modified": "2023-10-31",
-                    "temporal": "2023-10-22/2023-10-28"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4f64860a-4368-451f-a9d9-ab4e4457f068",
+                    "temporal": "2023-10-22/2023-10-28",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-31"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/4f64860a-4368-451f-a9d9-ab4e4457f068/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4f64860a-4368-451f-a9d9-ab4e4457f068",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-31",
+                    "format": "API",
                     "modified": "2023-10-31",
-                    "temporal": "2023-10-22/2023-10-28"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4f64860a-4368-451f-a9d9-ab4e4457f068",
+                    "temporal": "2023-10-22/2023-10-28",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-31"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/9c7f4293-3566-472e-9dc8-1700c29f6e9e/FISS_AR_20231026.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/07b5c392-bc7c-4b66-a137-cfe426bff5b1",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-27",
                     "modified": "2023-10-27",
-                    "temporal": "2023-10-15/2023-10-21"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/07b5c392-bc7c-4b66-a137-cfe426bff5b1",
+                    "temporal": "2023-10-15/2023-10-21",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-27"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/07b5c392-bc7c-4b66-a137-cfe426bff5b1/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/07b5c392-bc7c-4b66-a137-cfe426bff5b1",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-27",
+                    "format": "API",
                     "modified": "2023-10-27",
-                    "temporal": "2023-10-15/2023-10-21"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/07b5c392-bc7c-4b66-a137-cfe426bff5b1",
+                    "temporal": "2023-10-15/2023-10-21",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-27"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/11d68344-448e-441b-aae5-a94f9b125ef9/FISS_AR_20231023.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c05911e3-563a-4c9d-bee0-09cea59de406",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-24",
                     "modified": "2023-10-24",
-                    "temporal": "2023-10-15/2023-10-21"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c05911e3-563a-4c9d-bee0-09cea59de406",
+                    "temporal": "2023-10-15/2023-10-21",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-24"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/c05911e3-563a-4c9d-bee0-09cea59de406/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c05911e3-563a-4c9d-bee0-09cea59de406",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-24",
+                    "format": "API",
                     "modified": "2023-10-24",
-                    "temporal": "2023-10-15/2023-10-21"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c05911e3-563a-4c9d-bee0-09cea59de406",
+                    "temporal": "2023-10-15/2023-10-21",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-24"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/54f73849-e6ca-4b43-83f6-6a43a1751702/FISS_AR_20231019.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6300ac24-4179-4a28-a3f3-ed7b0a06b3c2",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-20",
                     "modified": "2023-10-20",
-                    "temporal": "2023-10-08/2023-10-14"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6300ac24-4179-4a28-a3f3-ed7b0a06b3c2",
+                    "temporal": "2023-10-08/2023-10-14",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-20"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/6300ac24-4179-4a28-a3f3-ed7b0a06b3c2/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6300ac24-4179-4a28-a3f3-ed7b0a06b3c2",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-20",
+                    "format": "API",
                     "modified": "2023-10-20",
-                    "temporal": "2023-10-08/2023-10-14"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6300ac24-4179-4a28-a3f3-ed7b0a06b3c2",
+                    "temporal": "2023-10-08/2023-10-14",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-20"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/7f55df95-06da-43dd-a6b1-83675b8374f2/FISS_AR_20231016.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d77776bb-62af-4922-858a-a82ba52e4246",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-17",
                     "modified": "2023-10-17",
-                    "temporal": "2023-10-08/2023-10-14"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d77776bb-62af-4922-858a-a82ba52e4246",
+                    "temporal": "2023-10-08/2023-10-14",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-17"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/d77776bb-62af-4922-858a-a82ba52e4246/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d77776bb-62af-4922-858a-a82ba52e4246",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-17",
+                    "format": "API",
                     "modified": "2023-10-17",
-                    "temporal": "2023-10-08/2023-10-14"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d77776bb-62af-4922-858a-a82ba52e4246",
+                    "temporal": "2023-10-08/2023-10-14",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-17"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/444e2e58-6e54-413b-ad82-1dc16799aa94/FISS_AR_20231012.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fade2ff9-e520-4884-8bb2-3b3c7be9c493",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-13",
                     "modified": "2023-10-13",
-                    "temporal": "2023-10-01/2023-10-07"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fade2ff9-e520-4884-8bb2-3b3c7be9c493",
+                    "temporal": "2023-10-01/2023-10-07",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-13"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/fade2ff9-e520-4884-8bb2-3b3c7be9c493/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fade2ff9-e520-4884-8bb2-3b3c7be9c493",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-13",
+                    "format": "API",
                     "modified": "2023-10-13",
-                    "temporal": "2023-10-01/2023-10-07"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fade2ff9-e520-4884-8bb2-3b3c7be9c493",
+                    "temporal": "2023-10-01/2023-10-07",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-13"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/d949a6e0-2b59-49f3-b7be-df365f5fe418/FISS_AR_20231010.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/da243d59-b3a9-476e-a5ee-dd5dbe4dc17e",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-11",
                     "modified": "2023-10-11",
-                    "temporal": "2023-10-01/2023-10-07"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/da243d59-b3a9-476e-a5ee-dd5dbe4dc17e",
+                    "temporal": "2023-10-01/2023-10-07",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-11"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/da243d59-b3a9-476e-a5ee-dd5dbe4dc17e/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/da243d59-b3a9-476e-a5ee-dd5dbe4dc17e",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-11",
+                    "format": "API",
                     "modified": "2023-10-11",
-                    "temporal": "2023-10-01/2023-10-07"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/da243d59-b3a9-476e-a5ee-dd5dbe4dc17e",
+                    "temporal": "2023-10-01/2023-10-07",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-11"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/26018faf-160e-4bd3-b4dc-3cd4a0dfdeb9/FISS_AR_20231005.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/deea52b2-15c9-4b1a-9fd6-c4341ebabffd",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-05",
                     "modified": "2023-10-10",
-                    "temporal": "2023-09-24/2023-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/deea52b2-15c9-4b1a-9fd6-c4341ebabffd",
+                    "temporal": "2023-09-24/2023-09-30",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-05"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/deea52b2-15c9-4b1a-9fd6-c4341ebabffd/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/deea52b2-15c9-4b1a-9fd6-c4341ebabffd",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-05",
+                    "format": "API",
                     "modified": "2023-10-10",
-                    "temporal": "2023-09-24/2023-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/deea52b2-15c9-4b1a-9fd6-c4341ebabffd",
+                    "temporal": "2023-09-24/2023-09-30",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-05"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/5722d2c3-4df5-4013-b6ee-ddd4b1408f35/FISS_AR_20231002.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3396dbb6-b1d7-45b1-a3c3-3630dbcceb10",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-03",
                     "modified": "2023-10-03",
-                    "temporal": "2023-09-24/2023-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3396dbb6-b1d7-45b1-a3c3-3630dbcceb10",
+                    "temporal": "2023-09-24/2023-09-30",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-03"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/3396dbb6-b1d7-45b1-a3c3-3630dbcceb10/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3396dbb6-b1d7-45b1-a3c3-3630dbcceb10",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-03",
+                    "format": "API",
                     "modified": "2023-10-03",
-                    "temporal": "2023-09-24/2023-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3396dbb6-b1d7-45b1-a3c3-3630dbcceb10",
+                    "temporal": "2023-09-24/2023-09-30",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-03"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/0480c8e1-24c3-43e1-b903-99c313fcae46/FISS_AR_20230928.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d70c976f-4230-4aec-9b78-3d0ff9198beb",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-28",
                     "modified": "2023-09-28",
-                    "temporal": "2023-09-17/2023-09-23"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d70c976f-4230-4aec-9b78-3d0ff9198beb",
+                    "temporal": "2023-09-17/2023-09-23",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-28"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/d70c976f-4230-4aec-9b78-3d0ff9198beb/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d70c976f-4230-4aec-9b78-3d0ff9198beb",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-28",
+                    "format": "API",
                     "modified": "2023-09-28",
-                    "temporal": "2023-09-17/2023-09-23"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d70c976f-4230-4aec-9b78-3d0ff9198beb",
+                    "temporal": "2023-09-17/2023-09-23",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-28"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/9e1f1758-68a3-403f-b2b4-7b324627a057/FISS_AR_20230925.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e935d254-2d9a-4c4c-a28d-a3b34a40e607",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-26",
                     "modified": "2023-09-27",
-                    "temporal": "2023-09-17/2023-09-23"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e935d254-2d9a-4c4c-a28d-a3b34a40e607",
+                    "temporal": "2023-09-17/2023-09-23",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-26"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/e935d254-2d9a-4c4c-a28d-a3b34a40e607/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e935d254-2d9a-4c4c-a28d-a3b34a40e607",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-26",
+                    "format": "API",
                     "modified": "2023-09-27",
-                    "temporal": "2023-09-17/2023-09-23"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e935d254-2d9a-4c4c-a28d-a3b34a40e607",
+                    "temporal": "2023-09-17/2023-09-23",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-26"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/1790b083-a74b-4384-a159-0ad27a7ec9a7/FISS_AR_20230922.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3c818122-9568-4d6a-baaa-a43daf2dc241",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-22",
                     "modified": "2023-09-22",
-                    "temporal": "2023-09-10/2023-09-16"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3c818122-9568-4d6a-baaa-a43daf2dc241",
+                    "temporal": "2023-09-10/2023-09-16",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-22"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/3c818122-9568-4d6a-baaa-a43daf2dc241/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3c818122-9568-4d6a-baaa-a43daf2dc241",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-22",
+                    "format": "API",
                     "modified": "2023-09-22",
-                    "temporal": "2023-09-10/2023-09-16"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3c818122-9568-4d6a-baaa-a43daf2dc241",
+                    "temporal": "2023-09-10/2023-09-16",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-22"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/77e071cc-85c0-4070-9356-290a06af2589/FISS_AR_20230918.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5b46146c-4c66-42e5-ad82-1ca04fb8c1b7",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-18",
                     "modified": "2023-09-19",
-                    "temporal": "2023-09-10/2023-09-16"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5b46146c-4c66-42e5-ad82-1ca04fb8c1b7",
+                    "temporal": "2023-09-10/2023-09-16",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-18"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/5b46146c-4c66-42e5-ad82-1ca04fb8c1b7/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5b46146c-4c66-42e5-ad82-1ca04fb8c1b7",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-18",
+                    "format": "API",
                     "modified": "2023-09-19",
-                    "temporal": "2023-09-10/2023-09-16"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5b46146c-4c66-42e5-ad82-1ca04fb8c1b7",
+                    "temporal": "2023-09-10/2023-09-16",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-18"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/d1723766-78c0-4728-8aeb-88f73914be25/FISS_AR_20230914.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ba7475b5-6d9b-46e2-89f9-6af3a6ecd744",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-14",
                     "modified": "2023-09-14",
-                    "temporal": "2023-09-03/2023-09-09"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ba7475b5-6d9b-46e2-89f9-6af3a6ecd744",
+                    "temporal": "2023-09-03/2023-09-09",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-14"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/ba7475b5-6d9b-46e2-89f9-6af3a6ecd744/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ba7475b5-6d9b-46e2-89f9-6af3a6ecd744",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-14",
+                    "format": "API",
                     "modified": "2023-09-14",
-                    "temporal": "2023-09-03/2023-09-09"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ba7475b5-6d9b-46e2-89f9-6af3a6ecd744",
+                    "temporal": "2023-09-03/2023-09-09",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-14"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/3a083201-d561-4ecf-99dd-65c699691057/FISS_AR_20230911.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7353bd93-8af0-42a5-afbd-c76bae3a54fc",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-11",
                     "modified": "2023-09-11",
-                    "temporal": "2023-09-03/2023-09-09"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7353bd93-8af0-42a5-afbd-c76bae3a54fc",
+                    "temporal": "2023-09-03/2023-09-09",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-11"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/7353bd93-8af0-42a5-afbd-c76bae3a54fc/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7353bd93-8af0-42a5-afbd-c76bae3a54fc",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-11",
+                    "format": "API",
                     "modified": "2023-09-11",
-                    "temporal": "2023-09-03/2023-09-09"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7353bd93-8af0-42a5-afbd-c76bae3a54fc",
+                    "temporal": "2023-09-03/2023-09-09",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-11"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/87e8d43d-2963-4da5-b87c-3f291b0a5ba5/FISS_AR_20230907.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b9e26fc2-6e71-4f80-8884-c25dabb74065",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-07",
                     "modified": "2023-09-08",
-                    "temporal": "2023-08-27/2023-09-02"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b9e26fc2-6e71-4f80-8884-c25dabb74065",
+                    "temporal": "2023-08-27/2023-09-02",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-07"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/b9e26fc2-6e71-4f80-8884-c25dabb74065/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b9e26fc2-6e71-4f80-8884-c25dabb74065",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-07",
+                    "format": "API",
                     "modified": "2023-09-08",
-                    "temporal": "2023-08-27/2023-09-02"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b9e26fc2-6e71-4f80-8884-c25dabb74065",
+                    "temporal": "2023-08-27/2023-09-02",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-07"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/5557a921-897f-4d0a-a25b-0dedbdf3e0dd/FISS_AR_20230905.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/cff94111-e355-42e3-a8d2-7e62e6e2106d",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-06",
                     "modified": "2023-09-06",
-                    "temporal": "2023-08-27/2023-09-02"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/cff94111-e355-42e3-a8d2-7e62e6e2106d",
+                    "temporal": "2023-08-27/2023-09-02",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-06"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/cff94111-e355-42e3-a8d2-7e62e6e2106d/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/cff94111-e355-42e3-a8d2-7e62e6e2106d",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-06",
+                    "format": "API",
                     "modified": "2023-09-06",
-                    "temporal": "2023-08-27/2023-09-02"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/cff94111-e355-42e3-a8d2-7e62e6e2106d",
+                    "temporal": "2023-08-27/2023-09-02",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-06"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/76727c8a-fc6a-463b-aec7-17d735e93030/FISS_AR_20230831.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b3492fcf-a0d6-4959-a0f5-6acbb2278e95",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-31",
                     "modified": "2023-09-01",
-                    "temporal": "2023-08-20/2023-08-26"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b3492fcf-a0d6-4959-a0f5-6acbb2278e95",
+                    "temporal": "2023-08-20/2023-08-26",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-31"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/b3492fcf-a0d6-4959-a0f5-6acbb2278e95/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b3492fcf-a0d6-4959-a0f5-6acbb2278e95",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-31",
+                    "format": "API",
                     "modified": "2023-09-01",
-                    "temporal": "2023-08-20/2023-08-26"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b3492fcf-a0d6-4959-a0f5-6acbb2278e95",
+                    "temporal": "2023-08-20/2023-08-26",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-31"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/6b133a86-3942-4389-8d1d-30731b5ca966/FISS_AR_20230828.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d9f12e5e-cabe-4d60-9ae8-fbf6a18aff47",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-29",
                     "modified": "2023-08-29",
-                    "temporal": "2023-08-20/2023-08-26"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d9f12e5e-cabe-4d60-9ae8-fbf6a18aff47",
+                    "temporal": "2023-08-20/2023-08-26",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-29"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/d9f12e5e-cabe-4d60-9ae8-fbf6a18aff47/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d9f12e5e-cabe-4d60-9ae8-fbf6a18aff47",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-29",
+                    "format": "API",
                     "modified": "2023-08-29",
-                    "temporal": "2023-08-20/2023-08-26"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d9f12e5e-cabe-4d60-9ae8-fbf6a18aff47",
+                    "temporal": "2023-08-20/2023-08-26",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-29"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/d2209779-b60d-4e3f-9ceb-bd1742e9f378/FISS_AR_20230824.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/11f057e9-b45c-4d70-8eef-5ccfe149542b",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-24",
                     "modified": "2023-08-25",
-                    "temporal": "2023-08-13/2023-08-19"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/11f057e9-b45c-4d70-8eef-5ccfe149542b",
+                    "temporal": "2023-08-13/2023-08-19",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-24"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/11f057e9-b45c-4d70-8eef-5ccfe149542b/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/11f057e9-b45c-4d70-8eef-5ccfe149542b",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-24",
+                    "format": "API",
                     "modified": "2023-08-25",
-                    "temporal": "2023-08-13/2023-08-19"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/11f057e9-b45c-4d70-8eef-5ccfe149542b",
+                    "temporal": "2023-08-13/2023-08-19",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-24"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/8032a92e-cd66-42ef-bf1d-4ffdcffd48e4/FISS_AR_20230821.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/27f9604f-1834-4a0c-8afe-75209d093134",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-22",
                     "modified": "2023-08-22",
-                    "temporal": "2023-08-13/2023-08-19"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/27f9604f-1834-4a0c-8afe-75209d093134",
+                    "temporal": "2023-08-13/2023-08-19",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-22"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/27f9604f-1834-4a0c-8afe-75209d093134/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/27f9604f-1834-4a0c-8afe-75209d093134",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-22",
+                    "format": "API",
                     "modified": "2023-08-22",
-                    "temporal": "2023-08-13/2023-08-19"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/27f9604f-1834-4a0c-8afe-75209d093134",
+                    "temporal": "2023-08-13/2023-08-19",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-22"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/b5e54be6-7197-470a-9f42-1ca548be71b6/FISS_AR_20230817.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/463f6d4a-fd18-481c-afc6-91d36324c94a",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-17",
                     "modified": "2023-08-18",
-                    "temporal": "2023-08-06/2023-08-12"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/463f6d4a-fd18-481c-afc6-91d36324c94a",
+                    "temporal": "2023-08-06/2023-08-12",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-17"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/463f6d4a-fd18-481c-afc6-91d36324c94a/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/463f6d4a-fd18-481c-afc6-91d36324c94a",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-17",
+                    "format": "API",
                     "modified": "2023-08-18",
-                    "temporal": "2023-08-06/2023-08-12"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/463f6d4a-fd18-481c-afc6-91d36324c94a",
+                    "temporal": "2023-08-06/2023-08-12",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-17"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/5eddf7e5-e5d6-4d27-99e9-b0c2d2c2345d/FISS_AR_20230814.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/cf9cc428-fc56-48bc-a9f8-2654f3e01328",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-15",
                     "modified": "2023-08-15",
-                    "temporal": "2023-08-06/2023-08-12"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/cf9cc428-fc56-48bc-a9f8-2654f3e01328",
+                    "temporal": "2023-08-06/2023-08-12",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-15"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/cf9cc428-fc56-48bc-a9f8-2654f3e01328/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/cf9cc428-fc56-48bc-a9f8-2654f3e01328",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-15",
+                    "format": "API",
                     "modified": "2023-08-15",
-                    "temporal": "2023-08-06/2023-08-12"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/cf9cc428-fc56-48bc-a9f8-2654f3e01328",
+                    "temporal": "2023-08-06/2023-08-12",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/9bb836a9-22bf-4c18-a0a9-877e6441a68f/FISS_AR_20230810.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ff182662-558a-473c-922e-a8511643e774",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-10",
                     "modified": "2023-08-11",
-                    "temporal": "2023-07-30/2023-08-05"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ff182662-558a-473c-922e-a8511643e774",
+                    "temporal": "2023-07-30/2023-08-05",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-10"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/ff182662-558a-473c-922e-a8511643e774/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ff182662-558a-473c-922e-a8511643e774",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-10",
+                    "format": "API",
                     "modified": "2023-08-11",
-                    "temporal": "2023-07-30/2023-08-05"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ff182662-558a-473c-922e-a8511643e774",
+                    "temporal": "2023-07-30/2023-08-05",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-10"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/77f10360-3e72-4f39-9ff0-2fcbef0a1070/FISS_AR_20230807.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f10f0d1b-ef01-4f1c-be1a-9701e08f5b0a",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-08",
                     "modified": "2023-08-08",
-                    "temporal": "2023-07-30/2023-08-05"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f10f0d1b-ef01-4f1c-be1a-9701e08f5b0a",
+                    "temporal": "2023-07-30/2023-08-05",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-08"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/f10f0d1b-ef01-4f1c-be1a-9701e08f5b0a/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f10f0d1b-ef01-4f1c-be1a-9701e08f5b0a",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-08",
+                    "format": "API",
                     "modified": "2023-08-08",
-                    "temporal": "2023-07-30/2023-08-05"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f10f0d1b-ef01-4f1c-be1a-9701e08f5b0a",
+                    "temporal": "2023-07-30/2023-08-05",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-08"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/303dae4e-0c48-4604-85f6-70e0a4a6759d/FISS_AR_20230803.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/095f84bf-4d74-461b-830b-5fcc5cae4144",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-03",
                     "modified": "2023-08-04",
-                    "temporal": "2023-07-23/2023-07-29"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/095f84bf-4d74-461b-830b-5fcc5cae4144",
+                    "temporal": "2023-07-23/2023-07-29",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-03"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/095f84bf-4d74-461b-830b-5fcc5cae4144/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/095f84bf-4d74-461b-830b-5fcc5cae4144",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-03",
+                    "format": "API",
                     "modified": "2023-08-04",
-                    "temporal": "2023-07-23/2023-07-29"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/095f84bf-4d74-461b-830b-5fcc5cae4144",
+                    "temporal": "2023-07-23/2023-07-29",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-03"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/f7034408-3ce3-445c-b192-80d4abc4462b/FISS_AR_20230731.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4e8a09af-97a2-4739-9588-cd47fd703872",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-01",
                     "modified": "2023-08-01",
-                    "temporal": "2023-07-23/2023-07-29"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4e8a09af-97a2-4739-9588-cd47fd703872",
+                    "temporal": "2023-07-23/2023-07-29",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/4e8a09af-97a2-4739-9588-cd47fd703872/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4e8a09af-97a2-4739-9588-cd47fd703872",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-01",
+                    "format": "API",
                     "modified": "2023-08-01",
-                    "temporal": "2023-07-23/2023-07-29"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4e8a09af-97a2-4739-9588-cd47fd703872",
+                    "temporal": "2023-07-23/2023-07-29",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/4f291e6d-ee49-47a8-9acf-e1906d706a04/FISS_AR_20230727.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/24057976-4d92-46a7-9915-b12608a3768a",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-27",
                     "modified": "2023-07-27",
-                    "temporal": "2023-07-16/2023-07-22"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/24057976-4d92-46a7-9915-b12608a3768a",
+                    "temporal": "2023-07-16/2023-07-22",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-27"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/24057976-4d92-46a7-9915-b12608a3768a/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/24057976-4d92-46a7-9915-b12608a3768a",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-27",
+                    "format": "API",
                     "modified": "2023-07-27",
-                    "temporal": "2023-07-16/2023-07-22"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/24057976-4d92-46a7-9915-b12608a3768a",
+                    "temporal": "2023-07-16/2023-07-22",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-27"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/ba60902a-fecc-4f2a-9581-2c284c748eb5/FISS_AR_20230724.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1fc70571-1bff-4836-b10e-54a99269b5ea",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-25",
                     "modified": "2023-07-25",
-                    "temporal": "2023-07-16/2023-07-22"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1fc70571-1bff-4836-b10e-54a99269b5ea",
+                    "temporal": "2023-07-16/2023-07-22",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-25"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/1fc70571-1bff-4836-b10e-54a99269b5ea/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1fc70571-1bff-4836-b10e-54a99269b5ea",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-25",
+                    "format": "API",
                     "modified": "2023-07-25",
-                    "temporal": "2023-07-16/2023-07-22"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1fc70571-1bff-4836-b10e-54a99269b5ea",
+                    "temporal": "2023-07-16/2023-07-22",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-25"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/5cdf7dbc-548b-4652-9779-9dff44498851/FISS_AR_20230720.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/cffa589a-598f-4317-92b6-2f1f112fd7db",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-21",
                     "modified": "2023-07-21",
-                    "temporal": "2023-07-09/2023-07-15"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/cffa589a-598f-4317-92b6-2f1f112fd7db",
+                    "temporal": "2023-07-09/2023-07-15",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-21"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/cffa589a-598f-4317-92b6-2f1f112fd7db/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/cffa589a-598f-4317-92b6-2f1f112fd7db",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-21",
+                    "format": "API",
                     "modified": "2023-07-21",
-                    "temporal": "2023-07-09/2023-07-15"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/cffa589a-598f-4317-92b6-2f1f112fd7db",
+                    "temporal": "2023-07-09/2023-07-15",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-21"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/f5af0694-c617-453e-b277-60b754ece3c4/FISS_AR_20230718.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/46bc04b7-cbe9-4157-a9b8-8fb1a0af5c30",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-19",
                     "modified": "2023-07-19",
-                    "temporal": "2023-07-09/2023-07-15"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/46bc04b7-cbe9-4157-a9b8-8fb1a0af5c30",
+                    "temporal": "2023-07-09/2023-07-15",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-19"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/46bc04b7-cbe9-4157-a9b8-8fb1a0af5c30/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/46bc04b7-cbe9-4157-a9b8-8fb1a0af5c30",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-19",
+                    "format": "API",
                     "modified": "2023-07-19",
-                    "temporal": "2023-07-09/2023-07-15"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/46bc04b7-cbe9-4157-a9b8-8fb1a0af5c30",
+                    "temporal": "2023-07-09/2023-07-15",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-19"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/2d8239db-85c1-4567-86a5-a8d80f240604/FISS_AR_20230713.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/158adc21-0ef1-48da-abc0-269e5935c0fd",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-14",
                     "modified": "2023-07-14",
-                    "temporal": "2023-07-02/2023-07-08"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/158adc21-0ef1-48da-abc0-269e5935c0fd",
+                    "temporal": "2023-07-02/2023-07-08",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-14"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/158adc21-0ef1-48da-abc0-269e5935c0fd/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/158adc21-0ef1-48da-abc0-269e5935c0fd",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-14",
+                    "format": "API",
                     "modified": "2023-07-14",
-                    "temporal": "2023-07-02/2023-07-08"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/158adc21-0ef1-48da-abc0-269e5935c0fd",
+                    "temporal": "2023-07-02/2023-07-08",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-14"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/ec598333-7833-4946-a38b-5895bd976aa8/FISS_AR_20230710.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9e8afcac-8727-4615-892c-f9c2133c62dd",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-11",
                     "modified": "2023-07-11",
-                    "temporal": "2023-07-02/2023-07-08"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9e8afcac-8727-4615-892c-f9c2133c62dd",
+                    "temporal": "2023-07-02/2023-07-08",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-11"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/9e8afcac-8727-4615-892c-f9c2133c62dd/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9e8afcac-8727-4615-892c-f9c2133c62dd",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-11",
+                    "format": "API",
                     "modified": "2023-07-11",
-                    "temporal": "2023-07-02/2023-07-08"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9e8afcac-8727-4615-892c-f9c2133c62dd",
+                    "temporal": "2023-07-02/2023-07-08",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-11"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/5971652b-0722-4a2b-8e83-362b3e95de09/FISS_AR_20230706.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/77ce886b-fcaf-4eef-8030-769e0ef55742",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-07",
                     "modified": "2023-07-07",
-                    "temporal": "2023-06-25/2023-07-01"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/77ce886b-fcaf-4eef-8030-769e0ef55742",
+                    "temporal": "2023-06-25/2023-07-01",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-07"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/77ce886b-fcaf-4eef-8030-769e0ef55742/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/77ce886b-fcaf-4eef-8030-769e0ef55742",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-07",
+                    "format": "API",
                     "modified": "2023-07-07",
-                    "temporal": "2023-06-25/2023-07-01"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/77ce886b-fcaf-4eef-8030-769e0ef55742",
+                    "temporal": "2023-06-25/2023-07-01",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-07"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/65af7fc2-99a0-4201-90e7-1ee069ae1a1b/FISS_AR_20230703.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/285e83bb-f153-4f8a-b386-5e6ad0a8aff2",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-05",
                     "modified": "2023-07-05",
-                    "temporal": "2023-06-25/2023-07-01"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/285e83bb-f153-4f8a-b386-5e6ad0a8aff2",
+                    "temporal": "2023-06-25/2023-07-01",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-05"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/285e83bb-f153-4f8a-b386-5e6ad0a8aff2/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/285e83bb-f153-4f8a-b386-5e6ad0a8aff2",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-05",
+                    "format": "API",
                     "modified": "2023-07-05",
-                    "temporal": "2023-06-25/2023-07-01"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/285e83bb-f153-4f8a-b386-5e6ad0a8aff2",
+                    "temporal": "2023-06-25/2023-07-01",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-05"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/4d551acd-94eb-4b94-a5c9-e28766e14f39/FISS_AR_20230629.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8934f94a-adaf-4192-b5ad-9d000e0e0a76",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-03",
                     "modified": "2023-07-03",
-                    "temporal": "2023-06-25/2023-07-01"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8934f94a-adaf-4192-b5ad-9d000e0e0a76",
+                    "temporal": "2023-06-25/2023-07-01",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-03"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/8934f94a-adaf-4192-b5ad-9d000e0e0a76/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8934f94a-adaf-4192-b5ad-9d000e0e0a76",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-03",
+                    "format": "API",
                     "modified": "2023-07-03",
-                    "temporal": "2023-06-25/2023-07-01"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8934f94a-adaf-4192-b5ad-9d000e0e0a76",
+                    "temporal": "2023-06-25/2023-07-01",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-03"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/90e8edcb-3a1e-4455-a550-1fe3a405b989/FISS_AR_20230626.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4235e93e-331a-4345-95cb-b2af561a2b8c",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-27",
                     "modified": "2023-06-27",
-                    "temporal": "2023-06-18/2023-06-24"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4235e93e-331a-4345-95cb-b2af561a2b8c",
+                    "temporal": "2023-06-18/2023-06-24",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-27"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/4235e93e-331a-4345-95cb-b2af561a2b8c/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4235e93e-331a-4345-95cb-b2af561a2b8c",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-27",
+                    "format": "API",
                     "modified": "2023-06-27",
-                    "temporal": "2023-06-18/2023-06-24"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4235e93e-331a-4345-95cb-b2af561a2b8c",
+                    "temporal": "2023-06-18/2023-06-24",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-27"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/746dc5f2-6fa0-4b3c-adc5-78b7cd98736b/FISS_AR_20230622.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/447ac2de-68bb-4364-a1e6-2d1449c69e42",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-23",
                     "modified": "2023-06-23",
-                    "temporal": "2023-06-11/2023-06-17"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/447ac2de-68bb-4364-a1e6-2d1449c69e42",
+                    "temporal": "2023-06-11/2023-06-17",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-23"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/447ac2de-68bb-4364-a1e6-2d1449c69e42/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/447ac2de-68bb-4364-a1e6-2d1449c69e42",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-23",
+                    "format": "API",
                     "modified": "2023-06-23",
-                    "temporal": "2023-06-11/2023-06-17"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/447ac2de-68bb-4364-a1e6-2d1449c69e42",
+                    "temporal": "2023-06-11/2023-06-17",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-23"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/130e8837-3776-4702-8bb3-0944979a9e66/FISS_AR_20230619.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8cb4c77e-c393-4841-a400-38e085a76f04",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-20",
                     "modified": "2023-06-20",
-                    "temporal": "2023-06-11/2023-06-17"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8cb4c77e-c393-4841-a400-38e085a76f04",
+                    "temporal": "2023-06-11/2023-06-17",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-20"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/8cb4c77e-c393-4841-a400-38e085a76f04/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8cb4c77e-c393-4841-a400-38e085a76f04",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-20",
+                    "format": "API",
                     "modified": "2023-06-20",
-                    "temporal": "2023-06-11/2023-06-17"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8cb4c77e-c393-4841-a400-38e085a76f04",
+                    "temporal": "2023-06-11/2023-06-17",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-20"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/937d5f63-f6c8-4051-b972-3aec85ba12e3/FISS_AR_20230615.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f08341c9-ee08-497d-8799-4b8f09c3c4c7",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-15",
                     "modified": "2023-06-16",
-                    "temporal": "2023-06-04/2023-06-10"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f08341c9-ee08-497d-8799-4b8f09c3c4c7",
+                    "temporal": "2023-06-04/2023-06-10",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-15"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/f08341c9-ee08-497d-8799-4b8f09c3c4c7/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f08341c9-ee08-497d-8799-4b8f09c3c4c7",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-15",
+                    "format": "API",
                     "modified": "2023-06-16",
-                    "temporal": "2023-06-04/2023-06-10"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f08341c9-ee08-497d-8799-4b8f09c3c4c7",
+                    "temporal": "2023-06-04/2023-06-10",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/d1042f3f-bf5d-410e-9e23-2bcdcb94fca6/FISS_AR_20230612.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5d281d1e-b906-4f5c-8c2f-4ab1bd97ea43",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-13",
                     "modified": "2023-06-13",
-                    "temporal": "2023-06-04/2023-06-10"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5d281d1e-b906-4f5c-8c2f-4ab1bd97ea43",
+                    "temporal": "2023-06-04/2023-06-10",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-13"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/5d281d1e-b906-4f5c-8c2f-4ab1bd97ea43/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5d281d1e-b906-4f5c-8c2f-4ab1bd97ea43",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-13",
+                    "format": "API",
                     "modified": "2023-06-13",
-                    "temporal": "2023-06-04/2023-06-10"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5d281d1e-b906-4f5c-8c2f-4ab1bd97ea43",
+                    "temporal": "2023-06-04/2023-06-10",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-13"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/4d080649-e36d-490b-b4d6-15ec8e64d8b9/FISS_AR_20230608.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/01307335-54cb-4ee2-aa3e-944a61c80128",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-08",
                     "modified": "2023-06-09",
-                    "temporal": "2023-05-28/2023-06-03"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/01307335-54cb-4ee2-aa3e-944a61c80128",
+                    "temporal": "2023-05-28/2023-06-03",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-08"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/01307335-54cb-4ee2-aa3e-944a61c80128/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/01307335-54cb-4ee2-aa3e-944a61c80128",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-08",
+                    "format": "API",
                     "modified": "2023-06-09",
-                    "temporal": "2023-05-28/2023-06-03"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/01307335-54cb-4ee2-aa3e-944a61c80128",
+                    "temporal": "2023-05-28/2023-06-03",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-08"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/4b82df1a-619b-4f0c-a2f6-b4314697af6d/FISS_AR_20230601.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3a59aa8b-46fb-4a5e-a255-c28494d53194",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-01",
                     "modified": "2023-06-02",
-                    "temporal": "2023-05-21/2023-05-27"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3a59aa8b-46fb-4a5e-a255-c28494d53194",
+                    "temporal": "2023-05-21/2023-05-27",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/3a59aa8b-46fb-4a5e-a255-c28494d53194/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3a59aa8b-46fb-4a5e-a255-c28494d53194",
-                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-01",
+                    "format": "API",
                     "modified": "2023-06-02",
-                    "temporal": "2023-05-21/2023-05-27"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3a59aa8b-46fb-4a5e-a255-c28494d53194",
+                    "temporal": "2023-05-21/2023-05-27",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-01"
                 }
             ],
             "identifier": "https://data.cms.gov/data-api/v1/dataset/75e8dcb2-78eb-4a7d-a377-9108441966db/data-viewer",
@@ -8044,164 +8043,164 @@
                 "fn": "Provider Enrollment Data Requests - CPI",
                 "hasEmail": "mailto:ProviderEnrollmentDataRequests@cms.hhs.gov"
             },
+            "dataQuality": true,
             "describedBy": "https://data.cms.gov/sites/default/files/2024-10/HHA_All_Owners_Data_Dictionary.pdf",
             "describedByType": "application/pdf",
-            "dataQuality": true,
             "description": "The Home Health Agency (HHA) All Owners dataset provides ownership information on all HHAs currently enrolled in Medicare. This data includes ownership information such as ownership name, ownership type, ownership address and ownership effective date.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/fc009b2d-7846-44b1-b4a1-692f0c143879/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fc009b2d-7846-44b1-b4a1-692f0c143879",
                     "description": "latest",
-                    "title": "Home Health Agency All Owners : 2025-01-01",
+                    "format": "API",
                     "modified": "2025-01-15",
-                    "temporal": "2025-01-01/2025-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/fc009b2d-7846-44b1-b4a1-692f0c143879",
+                    "temporal": "2025-01-01/2025-03-31",
+                    "title": "Home Health Agency All Owners : 2025-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/a0443d0f-247e-481e-8d62-cdd0621238d4/HHA_All_Owners_2025.01.02.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a338d79f-d7fc-4503-91f9-ae2696742830",
-                    "title": "Home Health Agency All Owners : 2025-01-01",
                     "modified": "2025-01-15",
-                    "temporal": "2025-01-01/2025-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a338d79f-d7fc-4503-91f9-ae2696742830",
+                    "temporal": "2025-01-01/2025-03-31",
+                    "title": "Home Health Agency All Owners : 2025-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/a338d79f-d7fc-4503-91f9-ae2696742830/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a338d79f-d7fc-4503-91f9-ae2696742830",
-                    "title": "Home Health Agency All Owners : 2025-01-01",
+                    "format": "API",
                     "modified": "2025-01-15",
-                    "temporal": "2025-01-01/2025-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a338d79f-d7fc-4503-91f9-ae2696742830",
+                    "temporal": "2025-01-01/2025-03-31",
+                    "title": "Home Health Agency All Owners : 2025-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/64509ec7-b479-4b46-bd26-0dcbd7d73e81/HHA_All_Owners_2024.10.07.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/dfa40c06-c5cf-43aa-a70c-15b95ae240b9",
-                    "title": "Home Health Agency All Owners : 2024-10-01",
                     "modified": "2024-10-15",
-                    "temporal": "2024-10-01/2024-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/dfa40c06-c5cf-43aa-a70c-15b95ae240b9",
+                    "temporal": "2024-10-01/2024-12-31",
+                    "title": "Home Health Agency All Owners : 2024-10-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/dfa40c06-c5cf-43aa-a70c-15b95ae240b9/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/dfa40c06-c5cf-43aa-a70c-15b95ae240b9",
-                    "title": "Home Health Agency All Owners : 2024-10-01",
+                    "format": "API",
                     "modified": "2024-10-15",
-                    "temporal": "2024-10-01/2024-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/dfa40c06-c5cf-43aa-a70c-15b95ae240b9",
+                    "temporal": "2024-10-01/2024-12-31",
+                    "title": "Home Health Agency All Owners : 2024-10-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/bc041dea-adee-47a0-8c8c-bf0140182588/HHA_All_Owners_2024.07.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/539fa7db-5720-438d-ae94-555c156e17fd",
-                    "title": "Home Health Agency All Owners : 2024-07-01",
                     "modified": "2024-07-15",
-                    "temporal": "2024-07-01/2024-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/539fa7db-5720-438d-ae94-555c156e17fd",
+                    "temporal": "2024-07-01/2024-09-30",
+                    "title": "Home Health Agency All Owners : 2024-07-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/539fa7db-5720-438d-ae94-555c156e17fd/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/539fa7db-5720-438d-ae94-555c156e17fd",
-                    "title": "Home Health Agency All Owners : 2024-07-01",
+                    "format": "API",
                     "modified": "2024-07-15",
-                    "temporal": "2024-07-01/2024-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/539fa7db-5720-438d-ae94-555c156e17fd",
+                    "temporal": "2024-07-01/2024-09-30",
+                    "title": "Home Health Agency All Owners : 2024-07-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/7755410d-7688-4d0f-9647-dc5c530375ef/HHA_All_Owners_2024.04.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c745e6c8-795f-4b3e-89df-12e85264a892",
-                    "title": "Home Health Agency All Owners : 2024-04-01",
                     "modified": "2024-04-15",
-                    "temporal": "2024-04-01/2024-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c745e6c8-795f-4b3e-89df-12e85264a892",
+                    "temporal": "2024-04-01/2024-06-30",
+                    "title": "Home Health Agency All Owners : 2024-04-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/c745e6c8-795f-4b3e-89df-12e85264a892/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c745e6c8-795f-4b3e-89df-12e85264a892",
-                    "title": "Home Health Agency All Owners : 2024-04-01",
+                    "format": "API",
                     "modified": "2024-04-15",
-                    "temporal": "2024-04-01/2024-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c745e6c8-795f-4b3e-89df-12e85264a892",
+                    "temporal": "2024-04-01/2024-06-30",
+                    "title": "Home Health Agency All Owners : 2024-04-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/7fc04d2a-a6c3-437d-878d-77692dc8c12e/HHA_All_Owners_2024.01.05.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c1b3a866-2efa-416c-8f7b-6f17e553dbf1",
-                    "title": "Home Health Agency All Owners : 2024-01-05",
                     "modified": "2024-01-19",
-                    "temporal": "2024-01-01/2024-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c1b3a866-2efa-416c-8f7b-6f17e553dbf1",
+                    "temporal": "2024-01-01/2024-03-31",
+                    "title": "Home Health Agency All Owners : 2024-01-05"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/c1b3a866-2efa-416c-8f7b-6f17e553dbf1/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c1b3a866-2efa-416c-8f7b-6f17e553dbf1",
-                    "title": "Home Health Agency All Owners : 2024-01-05",
+                    "format": "API",
                     "modified": "2024-01-19",
-                    "temporal": "2024-01-01/2024-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c1b3a866-2efa-416c-8f7b-6f17e553dbf1",
+                    "temporal": "2024-01-01/2024-03-31",
+                    "title": "Home Health Agency All Owners : 2024-01-05"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/2e7c7a07-c96a-42d1-ba9b-e898ec55dce3/HHA_All_Owners_2023.10.02.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8f1a6139-8df2-4bfd-9e95-8ce4adec6488",
-                    "title": "Home Health Agency All Owners : 2023-10-02",
                     "modified": "2023-10-16",
-                    "temporal": "2023-10-01/2023-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8f1a6139-8df2-4bfd-9e95-8ce4adec6488",
+                    "temporal": "2023-10-01/2023-12-31",
+                    "title": "Home Health Agency All Owners : 2023-10-02"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/8f1a6139-8df2-4bfd-9e95-8ce4adec6488/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8f1a6139-8df2-4bfd-9e95-8ce4adec6488",
-                    "title": "Home Health Agency All Owners : 2023-10-02",
+                    "format": "API",
                     "modified": "2023-10-16",
-                    "temporal": "2023-10-01/2023-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8f1a6139-8df2-4bfd-9e95-8ce4adec6488",
+                    "temporal": "2023-10-01/2023-12-31",
+                    "title": "Home Health Agency All Owners : 2023-10-02"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/988040ed-3766-4b8f-862c-e15d07dbe430/HHA_All_Owners_2023.07.06.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/94c1d434-bdad-47e5-b301-6bcf8634af6b",
-                    "title": "Home Health Agency All Owners : 2023-07-17",
                     "modified": "2023-07-17",
-                    "temporal": "2023-07-01/2023-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/94c1d434-bdad-47e5-b301-6bcf8634af6b",
+                    "temporal": "2023-07-01/2023-09-30",
+                    "title": "Home Health Agency All Owners : 2023-07-17"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/94c1d434-bdad-47e5-b301-6bcf8634af6b/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/94c1d434-bdad-47e5-b301-6bcf8634af6b",
-                    "title": "Home Health Agency All Owners : 2023-07-17",
+                    "format": "API",
                     "modified": "2023-07-17",
-                    "temporal": "2023-07-01/2023-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/94c1d434-bdad-47e5-b301-6bcf8634af6b",
+                    "temporal": "2023-07-01/2023-09-30",
+                    "title": "Home Health Agency All Owners : 2023-07-17"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/cfb66ea6-604a-4eaf-b50e-f991a3922731/HHA_All_Owners_2023.03.31.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/84a40ec7-d315-48e4-b2ed-ec00878cfec5",
-                    "title": "Home Health Agency All Owners : 2023-04-01",
                     "modified": "2023-04-19",
-                    "temporal": "2023-04-01/2023-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/84a40ec7-d315-48e4-b2ed-ec00878cfec5",
+                    "temporal": "2023-04-01/2023-06-30",
+                    "title": "Home Health Agency All Owners : 2023-04-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/84a40ec7-d315-48e4-b2ed-ec00878cfec5/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/84a40ec7-d315-48e4-b2ed-ec00878cfec5",
-                    "title": "Home Health Agency All Owners : 2023-04-01",
+                    "format": "API",
                     "modified": "2023-04-19",
-                    "temporal": "2023-04-01/2023-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/84a40ec7-d315-48e4-b2ed-ec00878cfec5",
+                    "temporal": "2023-04-01/2023-06-30",
+                    "title": "Home Health Agency All Owners : 2023-04-01"
                 }
             ],
             "identifier": "https://data.cms.gov/data-api/v1/dataset/fc009b2d-7846-44b1-b4a1-692f0c143879/data-viewer",
@@ -8247,73 +8246,73 @@
                 "fn": "PDAG Data Products - OEDA",
                 "hasEmail": "mailto:PDAG_Data_Products@cms.hhs.gov"
             },
-            "describedBy": "https://data.cms.gov/resources/home-health-agency-cost-report-data-dictionary",
             "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/home-health-agency-cost-report-data-dictionary",
             "description": "The Home Health Agency Provider Cost Report dataset provides select measures from the home health agency annual cost report. This data includes provider information such as facility characteristics, utilization data, cost and charges by cost center (in total and for Medicare), Medicare settlement data, and financial statement data organized by CMS Certification Number.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/4999da74-1d8d-4a6f-934e-2d7ea470cc63/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4999da74-1d8d-4a6f-934e-2d7ea470cc63",
                     "description": "latest",
-                    "title": "Home Health Agency Cost Report : 2022-12-01",
+                    "format": "API",
                     "modified": "2024-10-25",
-                    "temporal": "2022-01-01/2022-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4999da74-1d8d-4a6f-934e-2d7ea470cc63",
+                    "temporal": "2022-01-01/2022-12-31",
+                    "title": "Home Health Agency Cost Report : 2022-12-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/19db07e2-b626-480a-8554-8cb2ea64f5df/CostReporthha_Final_22.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1adf48d9-9ff2-4641-ac51-d827aabf791c",
-                    "title": "Home Health Agency Cost Report : 2022-12-01",
                     "modified": "2024-10-25",
-                    "temporal": "2022-01-01/2022-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1adf48d9-9ff2-4641-ac51-d827aabf791c",
+                    "temporal": "2022-01-01/2022-12-31",
+                    "title": "Home Health Agency Cost Report : 2022-12-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/1adf48d9-9ff2-4641-ac51-d827aabf791c/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1adf48d9-9ff2-4641-ac51-d827aabf791c",
-                    "title": "Home Health Agency Cost Report : 2022-12-01",
+                    "format": "API",
                     "modified": "2024-10-25",
-                    "temporal": "2022-01-01/2022-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1adf48d9-9ff2-4641-ac51-d827aabf791c",
+                    "temporal": "2022-01-01/2022-12-31",
+                    "title": "Home Health Agency Cost Report : 2022-12-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/e5f655dd-d6e9-466b-8669-5aec4bd2f76d/CostReporthha_Final_21.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a02a324e-a8ad-4933-8bcd-e6a10ab28c8e",
-                    "title": "Home Health Agency Cost Report : 2021-12-02",
                     "modified": "2024-10-25",
-                    "temporal": "2021-01-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a02a324e-a8ad-4933-8bcd-e6a10ab28c8e",
+                    "temporal": "2021-01-01/2021-12-31",
+                    "title": "Home Health Agency Cost Report : 2021-12-02"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/a02a324e-a8ad-4933-8bcd-e6a10ab28c8e/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a02a324e-a8ad-4933-8bcd-e6a10ab28c8e",
-                    "title": "Home Health Agency Cost Report : 2021-12-02",
+                    "format": "API",
                     "modified": "2024-10-25",
-                    "temporal": "2021-01-01/2021-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a02a324e-a8ad-4933-8bcd-e6a10ab28c8e",
+                    "temporal": "2021-01-01/2021-12-31",
+                    "title": "Home Health Agency Cost Report : 2021-12-02"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/2864363c-e84f-4cde-9042-f55590b750b7/CostReporthha_Final_20.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2914a2e4-6d60-4b46-8806-9e9c56ca2f39",
-                    "title": "Home Health Agency Cost Report : 2020-12-02",
                     "modified": "2024-10-25",
-                    "temporal": "2020-01-01/2020-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2914a2e4-6d60-4b46-8806-9e9c56ca2f39",
+                    "temporal": "2020-01-01/2020-12-31",
+                    "title": "Home Health Agency Cost Report : 2020-12-02"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/2914a2e4-6d60-4b46-8806-9e9c56ca2f39/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2914a2e4-6d60-4b46-8806-9e9c56ca2f39",
-                    "title": "Home Health Agency Cost Report : 2020-12-02",
+                    "format": "API",
                     "modified": "2024-10-25",
-                    "temporal": "2020-01-01/2020-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2914a2e4-6d60-4b46-8806-9e9c56ca2f39",
+                    "temporal": "2020-01-01/2020-12-31",
+                    "title": "Home Health Agency Cost Report : 2020-12-02"
                 }
             ],
             "identifier": "https://data.cms.gov/data-api/v1/dataset/4999da74-1d8d-4a6f-934e-2d7ea470cc63/data-viewer",
@@ -8359,164 +8358,164 @@
                 "fn": "Provider Enrollment Data Requests - CPI",
                 "hasEmail": "mailto:ProviderEnrollmentDataRequests@cms.hhs.gov"
             },
+            "dataQuality": true,
             "describedBy": "https://data.cms.gov/sites/default/files/2024-10/HHA_Enrollments_Data_Dictionary.pdf",
             "describedByType": "application/pdf",
-            "dataQuality": true,
             "description": "The Home Health Agency (HHA) Enrollments dataset provides enrollment information on all HHAs currently enrolled in Medicare. This data includes information on the HHA's legal business name, doing business as name, organization type and address.\u00a0",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/15f64ab4-3172-4a27-b589-ebd67a6d28aa/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/15f64ab4-3172-4a27-b589-ebd67a6d28aa",
                     "description": "latest",
-                    "title": "Home Health Agency Enrollments : 2025-01-01",
+                    "format": "API",
                     "modified": "2025-01-15",
-                    "temporal": "2025-01-01/2025-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/15f64ab4-3172-4a27-b589-ebd67a6d28aa",
+                    "temporal": "2025-01-01/2025-03-31",
+                    "title": "Home Health Agency Enrollments : 2025-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/c133f82f-5635-47d3-b85f-364b379a322a/HHA_Enrollments_2025.01.02.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e9278ca0-fd12-4e20-9a21-9d5cd733cc1d",
-                    "title": "Home Health Agency Enrollments : 2025-01-01",
                     "modified": "2025-01-15",
-                    "temporal": "2025-01-01/2025-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e9278ca0-fd12-4e20-9a21-9d5cd733cc1d",
+                    "temporal": "2025-01-01/2025-03-31",
+                    "title": "Home Health Agency Enrollments : 2025-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/e9278ca0-fd12-4e20-9a21-9d5cd733cc1d/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e9278ca0-fd12-4e20-9a21-9d5cd733cc1d",
-                    "title": "Home Health Agency Enrollments : 2025-01-01",
+                    "format": "API",
                     "modified": "2025-01-15",
-                    "temporal": "2025-01-01/2025-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e9278ca0-fd12-4e20-9a21-9d5cd733cc1d",
+                    "temporal": "2025-01-01/2025-03-31",
+                    "title": "Home Health Agency Enrollments : 2025-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/6f0ae716-79df-45e0-8fcf-5ef1d12727b3/HHA_Enrollments_2024.10.07.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/115ccf0e-4312-4229-84e9-2b35267b106c",
-                    "title": "Home Health Agency Enrollments : 2024-10-01",
                     "modified": "2024-10-15",
-                    "temporal": "2024-10-01/2024-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/115ccf0e-4312-4229-84e9-2b35267b106c",
+                    "temporal": "2024-10-01/2024-12-31",
+                    "title": "Home Health Agency Enrollments : 2024-10-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/115ccf0e-4312-4229-84e9-2b35267b106c/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/115ccf0e-4312-4229-84e9-2b35267b106c",
-                    "title": "Home Health Agency Enrollments : 2024-10-01",
+                    "format": "API",
                     "modified": "2024-10-15",
-                    "temporal": "2024-10-01/2024-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/115ccf0e-4312-4229-84e9-2b35267b106c",
+                    "temporal": "2024-10-01/2024-12-31",
+                    "title": "Home Health Agency Enrollments : 2024-10-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/b8e87685-b941-4e88-aa45-b2cfe3db42a4/HHA_Enrollments_2024.07.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3a842f3f-2d77-43dc-b92c-078977a8c102",
-                    "title": "Home Health Agency Enrollments : 2024-07-01",
                     "modified": "2024-07-15",
-                    "temporal": "2024-07-01/2024-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3a842f3f-2d77-43dc-b92c-078977a8c102",
+                    "temporal": "2024-07-01/2024-09-30",
+                    "title": "Home Health Agency Enrollments : 2024-07-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/3a842f3f-2d77-43dc-b92c-078977a8c102/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3a842f3f-2d77-43dc-b92c-078977a8c102",
-                    "title": "Home Health Agency Enrollments : 2024-07-01",
+                    "format": "API",
                     "modified": "2024-07-15",
-                    "temporal": "2024-07-01/2024-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3a842f3f-2d77-43dc-b92c-078977a8c102",
+                    "temporal": "2024-07-01/2024-09-30",
+                    "title": "Home Health Agency Enrollments : 2024-07-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/85f0a6c7-c068-40fa-962d-dbf05aa93944/HHA_Enrollments_2024.04.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4410b442-fff1-4b05-bd49-3a90c9cac114",
-                    "title": "Home Health Agency Enrollments : 2024-04-01",
                     "modified": "2024-04-15",
-                    "temporal": "2024-04-01/2024-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4410b442-fff1-4b05-bd49-3a90c9cac114",
+                    "temporal": "2024-04-01/2024-06-30",
+                    "title": "Home Health Agency Enrollments : 2024-04-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/4410b442-fff1-4b05-bd49-3a90c9cac114/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4410b442-fff1-4b05-bd49-3a90c9cac114",
-                    "title": "Home Health Agency Enrollments : 2024-04-01",
+                    "format": "API",
                     "modified": "2024-04-15",
-                    "temporal": "2024-04-01/2024-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4410b442-fff1-4b05-bd49-3a90c9cac114",
+                    "temporal": "2024-04-01/2024-06-30",
+                    "title": "Home Health Agency Enrollments : 2024-04-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/00ea617a-7f11-45ef-a49c-89ed8dff5945/HHA_Enrollments_2024.01.05.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/089ee308-8d5c-4ab5-afbf-a82c14b3f3b6",
-                    "title": "Home Health Agency Enrollments : 2024-01-05",
                     "modified": "2024-01-19",
-                    "temporal": "2024-01-01/2024-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/089ee308-8d5c-4ab5-afbf-a82c14b3f3b6",
+                    "temporal": "2024-01-01/2024-03-31",
+                    "title": "Home Health Agency Enrollments : 2024-01-05"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/089ee308-8d5c-4ab5-afbf-a82c14b3f3b6/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/089ee308-8d5c-4ab5-afbf-a82c14b3f3b6",
-                    "title": "Home Health Agency Enrollments : 2024-01-05",
+                    "format": "API",
                     "modified": "2024-01-19",
-                    "temporal": "2024-01-01/2024-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/089ee308-8d5c-4ab5-afbf-a82c14b3f3b6",
+                    "temporal": "2024-01-01/2024-03-31",
+                    "title": "Home Health Agency Enrollments : 2024-01-05"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/82964b76-66b6-463a-aef1-dff4ae766f9a/HHA_Enrollments_2023.10.02.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6e53ed2f-c967-4661-b566-a2cbcd7996f1",
-                    "title": "Home Health Agency Enrollments : 2023-10-02",
                     "modified": "2023-10-16",
-                    "temporal": "2023-10-01/2023-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6e53ed2f-c967-4661-b566-a2cbcd7996f1",
+                    "temporal": "2023-10-01/2023-12-31",
+                    "title": "Home Health Agency Enrollments : 2023-10-02"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/6e53ed2f-c967-4661-b566-a2cbcd7996f1/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6e53ed2f-c967-4661-b566-a2cbcd7996f1",
-                    "title": "Home Health Agency Enrollments : 2023-10-02",
+                    "format": "API",
                     "modified": "2023-10-16",
-                    "temporal": "2023-10-01/2023-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6e53ed2f-c967-4661-b566-a2cbcd7996f1",
+                    "temporal": "2023-10-01/2023-12-31",
+                    "title": "Home Health Agency Enrollments : 2023-10-02"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/45afd42e-9416-41e3-b2d0-0e70ce793a52/HHA_Enrollments_2023.07.06.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d998c103-6d16-48a1-b58a-51e5848c6939",
-                    "title": "Home Health Agency Enrollments : 2023-07-17",
                     "modified": "2023-07-17",
-                    "temporal": "2023-07-01/2023-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d998c103-6d16-48a1-b58a-51e5848c6939",
+                    "temporal": "2023-07-01/2023-09-30",
+                    "title": "Home Health Agency Enrollments : 2023-07-17"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/d998c103-6d16-48a1-b58a-51e5848c6939/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d998c103-6d16-48a1-b58a-51e5848c6939",
-                    "title": "Home Health Agency Enrollments : 2023-07-17",
+                    "format": "API",
                     "modified": "2023-07-17",
-                    "temporal": "2023-07-01/2023-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d998c103-6d16-48a1-b58a-51e5848c6939",
+                    "temporal": "2023-07-01/2023-09-30",
+                    "title": "Home Health Agency Enrollments : 2023-07-17"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/f719af15-7eab-42c6-a28e-6fd960193edb/HHA_Enrollments_2023.03.31.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f48bb755-bd9f-42e3-87b9-b88c562cb981",
-                    "title": "Home Health Agency Enrollments : 2023-04-01",
                     "modified": "2023-04-19",
-                    "temporal": "2023-04-01/2023-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f48bb755-bd9f-42e3-87b9-b88c562cb981",
+                    "temporal": "2023-04-01/2023-06-30",
+                    "title": "Home Health Agency Enrollments : 2023-04-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/f48bb755-bd9f-42e3-87b9-b88c562cb981/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f48bb755-bd9f-42e3-87b9-b88c562cb981",
-                    "title": "Home Health Agency Enrollments : 2023-04-01",
+                    "format": "API",
                     "modified": "2023-04-19",
-                    "temporal": "2023-04-01/2023-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f48bb755-bd9f-42e3-87b9-b88c562cb981",
+                    "temporal": "2023-04-01/2023-06-30",
+                    "title": "Home Health Agency Enrollments : 2023-04-01"
                 }
             ],
             "identifier": "https://data.cms.gov/data-api/v1/dataset/15f64ab4-3172-4a27-b589-ebd67a6d28aa/data-viewer",
@@ -8562,775 +8561,775 @@
                 "fn": "Provider Enrollment Data Requests - CPI",
                 "hasEmail": "mailto:ProviderEnrollmentDataRequests@cms.hhs.gov"
             },
-            "describedBy": "https://data.cms.gov/resources/home-infusion-therapy-providers-data-dictionary",
             "dataQuality": true,
+            "describedBy": "https://data.cms.gov/resources/home-infusion-therapy-providers-data-dictionary",
             "description": "The Home Infusion Therapy Providers dataset provides information on the Providers in Medicare who specialize in Home Infusion Therapy.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/31f25ab6-2fe3-4bad-ac5a-90635ed79935/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/31f25ab6-2fe3-4bad-ac5a-90635ed79935",
                     "description": "latest",
-                    "title": "Home Infusion Therapy Providers : 2025-01-07",
+                    "format": "API",
                     "modified": "2025-01-07",
-                    "temporal": "2024-12-22/2025-01-04"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/31f25ab6-2fe3-4bad-ac5a-90635ed79935",
+                    "temporal": "2024-12-22/2025-01-04",
+                    "title": "Home Infusion Therapy Providers : 2025-01-07"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/ab9ed0b6-73d6-4023-969b-bfad85b2ddcd/Home%20Infusion%20Therapy%201.6.2025.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8596aa47-d4d4-4149-bc80-eb52e2d3a761",
-                    "title": "Home Infusion Therapy Providers : 2025-01-07",
                     "modified": "2025-01-07",
-                    "temporal": "2024-12-22/2025-01-04"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8596aa47-d4d4-4149-bc80-eb52e2d3a761",
+                    "temporal": "2024-12-22/2025-01-04",
+                    "title": "Home Infusion Therapy Providers : 2025-01-07"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/8596aa47-d4d4-4149-bc80-eb52e2d3a761/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8596aa47-d4d4-4149-bc80-eb52e2d3a761",
-                    "title": "Home Infusion Therapy Providers : 2025-01-07",
+                    "format": "API",
                     "modified": "2025-01-07",
-                    "temporal": "2024-12-22/2025-01-04"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8596aa47-d4d4-4149-bc80-eb52e2d3a761",
+                    "temporal": "2024-12-22/2025-01-04",
+                    "title": "Home Infusion Therapy Providers : 2025-01-07"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/51dac38c-b579-4141-baf5-7e5aec7924fd/Home%20Infusion%20Therapy%2012.23.2024.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7e14f5b0-1bc6-4b07-952e-786711893997",
-                    "title": "Home Infusion Therapy Providers : 2024-12-23",
                     "modified": "2024-12-23",
-                    "temporal": "2024-12-08/2024-12-21"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7e14f5b0-1bc6-4b07-952e-786711893997",
+                    "temporal": "2024-12-08/2024-12-21",
+                    "title": "Home Infusion Therapy Providers : 2024-12-23"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/7e14f5b0-1bc6-4b07-952e-786711893997/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7e14f5b0-1bc6-4b07-952e-786711893997",
-                    "title": "Home Infusion Therapy Providers : 2024-12-23",
+                    "format": "API",
                     "modified": "2024-12-23",
-                    "temporal": "2024-12-08/2024-12-21"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7e14f5b0-1bc6-4b07-952e-786711893997",
+                    "temporal": "2024-12-08/2024-12-21",
+                    "title": "Home Infusion Therapy Providers : 2024-12-23"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/8ba0ca11-14e1-4dcf-84df-5e589af8f62f/Home%20Infusion%20Therapy%2012.9.2024.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b045ef18-e306-4f1d-b710-04cd335a7895",
-                    "title": "Home Infusion Therapy Providers : 2024-12-10",
                     "modified": "2024-12-10",
-                    "temporal": "2024-11-24/2024-12-07"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b045ef18-e306-4f1d-b710-04cd335a7895",
+                    "temporal": "2024-11-24/2024-12-07",
+                    "title": "Home Infusion Therapy Providers : 2024-12-10"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/b045ef18-e306-4f1d-b710-04cd335a7895/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b045ef18-e306-4f1d-b710-04cd335a7895",
-                    "title": "Home Infusion Therapy Providers : 2024-12-10",
+                    "format": "API",
                     "modified": "2024-12-10",
-                    "temporal": "2024-11-24/2024-12-07"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b045ef18-e306-4f1d-b710-04cd335a7895",
+                    "temporal": "2024-11-24/2024-12-07",
+                    "title": "Home Infusion Therapy Providers : 2024-12-10"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/56a56562-678f-4b3d-b6d7-12e97c5c3d67/Home%20Infusion%20Therapy%2011.25.2024.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/edda6a20-cae6-41b9-8594-ec90ab0edf3f",
-                    "title": "Home Infusion Therapy Providers : 2024-11-26",
                     "modified": "2024-11-26",
-                    "temporal": "2024-11-10/2024-11-23"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/edda6a20-cae6-41b9-8594-ec90ab0edf3f",
+                    "temporal": "2024-11-10/2024-11-23",
+                    "title": "Home Infusion Therapy Providers : 2024-11-26"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/edda6a20-cae6-41b9-8594-ec90ab0edf3f/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/edda6a20-cae6-41b9-8594-ec90ab0edf3f",
-                    "title": "Home Infusion Therapy Providers : 2024-11-26",
+                    "format": "API",
                     "modified": "2024-11-26",
-                    "temporal": "2024-11-10/2024-11-23"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/edda6a20-cae6-41b9-8594-ec90ab0edf3f",
+                    "temporal": "2024-11-10/2024-11-23",
+                    "title": "Home Infusion Therapy Providers : 2024-11-26"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/b24b7e90-8cc8-4091-a3c6-251a86c3e9f4/Home%20Infusion%20Therapy%2011.12.2024.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/86c2aadc-7836-45a3-9962-bb7f31d86877",
-                    "title": "Home Infusion Therapy Providers : 2024-11-13",
                     "modified": "2024-11-13",
-                    "temporal": "2024-10-27/2024-11-09"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/86c2aadc-7836-45a3-9962-bb7f31d86877",
+                    "temporal": "2024-10-27/2024-11-09",
+                    "title": "Home Infusion Therapy Providers : 2024-11-13"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/86c2aadc-7836-45a3-9962-bb7f31d86877/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/86c2aadc-7836-45a3-9962-bb7f31d86877",
-                    "title": "Home Infusion Therapy Providers : 2024-11-13",
+                    "format": "API",
                     "modified": "2024-11-13",
-                    "temporal": "2024-10-27/2024-11-09"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/86c2aadc-7836-45a3-9962-bb7f31d86877",
+                    "temporal": "2024-10-27/2024-11-09",
+                    "title": "Home Infusion Therapy Providers : 2024-11-13"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/76a5a885-2a94-4dd2-987c-41ffaa801730/Home%20Infusion%20Therapy%2010.28.2024.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/28835aba-de78-4e14-b76f-d9c880342b9a",
-                    "title": "Home Infusion Therapy Providers : 2024-10-29",
                     "modified": "2024-10-29",
-                    "temporal": "2024-10-13/2024-10-26"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/28835aba-de78-4e14-b76f-d9c880342b9a",
+                    "temporal": "2024-10-13/2024-10-26",
+                    "title": "Home Infusion Therapy Providers : 2024-10-29"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/28835aba-de78-4e14-b76f-d9c880342b9a/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/28835aba-de78-4e14-b76f-d9c880342b9a",
-                    "title": "Home Infusion Therapy Providers : 2024-10-29",
+                    "format": "API",
                     "modified": "2024-10-29",
-                    "temporal": "2024-10-13/2024-10-26"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/28835aba-de78-4e14-b76f-d9c880342b9a",
+                    "temporal": "2024-10-13/2024-10-26",
+                    "title": "Home Infusion Therapy Providers : 2024-10-29"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/a9a9c427-df93-4b30-9a58-e9897a661ff9/Home%20Infusion%20Therapy%2010.15.2024.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/11bee001-3af6-49f0-86cd-2ff3e372d6c0",
-                    "title": "Home Infusion Therapy Providers : 2024-10-15",
                     "modified": "2024-10-15",
-                    "temporal": "2024-09-29/2024-10-12"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/11bee001-3af6-49f0-86cd-2ff3e372d6c0",
+                    "temporal": "2024-09-29/2024-10-12",
+                    "title": "Home Infusion Therapy Providers : 2024-10-15"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/11bee001-3af6-49f0-86cd-2ff3e372d6c0/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/11bee001-3af6-49f0-86cd-2ff3e372d6c0",
-                    "title": "Home Infusion Therapy Providers : 2024-10-15",
+                    "format": "API",
                     "modified": "2024-10-15",
-                    "temporal": "2024-09-29/2024-10-12"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/11bee001-3af6-49f0-86cd-2ff3e372d6c0",
+                    "temporal": "2024-09-29/2024-10-12",
+                    "title": "Home Infusion Therapy Providers : 2024-10-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/3d133010-2bbd-425c-85f8-0923efffef7d/Home%20Infusion%20Therapy%209.30.2024.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4ef9fdd8-2543-4415-a4b4-a339c8b6ee36",
-                    "title": "Home Infusion Therapy Providers : 2024-10-01",
                     "modified": "2024-10-01",
-                    "temporal": "2024-09-15/2024-09-28"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4ef9fdd8-2543-4415-a4b4-a339c8b6ee36",
+                    "temporal": "2024-09-15/2024-09-28",
+                    "title": "Home Infusion Therapy Providers : 2024-10-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/4ef9fdd8-2543-4415-a4b4-a339c8b6ee36/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4ef9fdd8-2543-4415-a4b4-a339c8b6ee36",
-                    "title": "Home Infusion Therapy Providers : 2024-10-01",
+                    "format": "API",
                     "modified": "2024-10-01",
-                    "temporal": "2024-09-15/2024-09-28"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4ef9fdd8-2543-4415-a4b4-a339c8b6ee36",
+                    "temporal": "2024-09-15/2024-09-28",
+                    "title": "Home Infusion Therapy Providers : 2024-10-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/32cb6953-750c-4f35-ad2f-0c1fe9febe4b/Home%20Infusion%20Therapy%209.16.2024.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bb7bc7cb-86cc-405f-b379-b1783b8d4be2",
-                    "title": "Home Infusion Therapy Providers : 2024-09-17",
                     "modified": "2024-09-17",
-                    "temporal": "2024-09-01/2024-09-14"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bb7bc7cb-86cc-405f-b379-b1783b8d4be2",
+                    "temporal": "2024-09-01/2024-09-14",
+                    "title": "Home Infusion Therapy Providers : 2024-09-17"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/bb7bc7cb-86cc-405f-b379-b1783b8d4be2/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bb7bc7cb-86cc-405f-b379-b1783b8d4be2",
-                    "title": "Home Infusion Therapy Providers : 2024-09-17",
+                    "format": "API",
                     "modified": "2024-09-17",
-                    "temporal": "2024-09-01/2024-09-14"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/bb7bc7cb-86cc-405f-b379-b1783b8d4be2",
+                    "temporal": "2024-09-01/2024-09-14",
+                    "title": "Home Infusion Therapy Providers : 2024-09-17"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/7d90d08c-3faf-4ba7-b186-9f773a240d54/Home%20Infusion%20Therapy%209.3.2024.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/db8830fb-0de4-4ac0-97ee-f68d8fd700eb",
-                    "title": "Home Infusion Therapy Providers : 2024-09-03",
                     "modified": "2024-09-03",
-                    "temporal": "2024-08-18/2024-08-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/db8830fb-0de4-4ac0-97ee-f68d8fd700eb",
+                    "temporal": "2024-08-18/2024-08-31",
+                    "title": "Home Infusion Therapy Providers : 2024-09-03"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/db8830fb-0de4-4ac0-97ee-f68d8fd700eb/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/db8830fb-0de4-4ac0-97ee-f68d8fd700eb",
-                    "title": "Home Infusion Therapy Providers : 2024-09-03",
+                    "format": "API",
                     "modified": "2024-09-03",
-                    "temporal": "2024-08-18/2024-08-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/db8830fb-0de4-4ac0-97ee-f68d8fd700eb",
+                    "temporal": "2024-08-18/2024-08-31",
+                    "title": "Home Infusion Therapy Providers : 2024-09-03"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/981ac67a-f5b9-4e72-a88b-2b63285d7b00/Home%20Infusion%20Therapy%208.19.2024.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a89247df-5f9f-4b56-bdf3-14530b30de2c",
-                    "title": "Home Infusion Therapy Providers : 2024-08-20",
                     "modified": "2024-08-20",
-                    "temporal": "2024-08-04/2024-08-17"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a89247df-5f9f-4b56-bdf3-14530b30de2c",
+                    "temporal": "2024-08-04/2024-08-17",
+                    "title": "Home Infusion Therapy Providers : 2024-08-20"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/a89247df-5f9f-4b56-bdf3-14530b30de2c/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a89247df-5f9f-4b56-bdf3-14530b30de2c",
-                    "title": "Home Infusion Therapy Providers : 2024-08-20",
+                    "format": "API",
                     "modified": "2024-08-20",
-                    "temporal": "2024-08-04/2024-08-17"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a89247df-5f9f-4b56-bdf3-14530b30de2c",
+                    "temporal": "2024-08-04/2024-08-17",
+                    "title": "Home Infusion Therapy Providers : 2024-08-20"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/788614b8-fc39-480f-b262-bb40acc6ac84/Home%20Infusion%20Therapy%208.5.2024.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/18d04805-5e3a-4645-9b64-6a62d08ae5ee",
-                    "title": "Home Infusion Therapy Providers : 2024-08-06",
                     "modified": "2024-08-06",
-                    "temporal": "2024-07-21/2024-08-03"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/18d04805-5e3a-4645-9b64-6a62d08ae5ee",
+                    "temporal": "2024-07-21/2024-08-03",
+                    "title": "Home Infusion Therapy Providers : 2024-08-06"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/18d04805-5e3a-4645-9b64-6a62d08ae5ee/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/18d04805-5e3a-4645-9b64-6a62d08ae5ee",
-                    "title": "Home Infusion Therapy Providers : 2024-08-06",
+                    "format": "API",
                     "modified": "2024-08-06",
-                    "temporal": "2024-07-21/2024-08-03"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/18d04805-5e3a-4645-9b64-6a62d08ae5ee",
+                    "temporal": "2024-07-21/2024-08-03",
+                    "title": "Home Infusion Therapy Providers : 2024-08-06"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/00741270-45b8-4655-8fa4-f92f492afdde/Home%20Infusion%20Therapy%207.22.2024.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8451233d-0bc1-4ae5-a422-1ecfbd4414c5",
-                    "title": "Home Infusion Therapy Providers : 2024-07-23",
                     "modified": "2024-07-23",
-                    "temporal": "2024-07-07/2024-07-20"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8451233d-0bc1-4ae5-a422-1ecfbd4414c5",
+                    "temporal": "2024-07-07/2024-07-20",
+                    "title": "Home Infusion Therapy Providers : 2024-07-23"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/8451233d-0bc1-4ae5-a422-1ecfbd4414c5/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8451233d-0bc1-4ae5-a422-1ecfbd4414c5",
-                    "title": "Home Infusion Therapy Providers : 2024-07-23",
+                    "format": "API",
                     "modified": "2024-07-23",
-                    "temporal": "2024-07-07/2024-07-20"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/8451233d-0bc1-4ae5-a422-1ecfbd4414c5",
+                    "temporal": "2024-07-07/2024-07-20",
+                    "title": "Home Infusion Therapy Providers : 2024-07-23"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/e73b7a79-077b-4de1-9673-35f6ee2145b6/Home%20Infusion%20Therapy%207.8.2024.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/34b4d0d9-6127-44bc-9ba8-13006bcff99e",
-                    "title": "Home Infusion Therapy Providers : 2024-07-09",
                     "modified": "2024-07-09",
-                    "temporal": "2024-06-23/2024-07-06"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/34b4d0d9-6127-44bc-9ba8-13006bcff99e",
+                    "temporal": "2024-06-23/2024-07-06",
+                    "title": "Home Infusion Therapy Providers : 2024-07-09"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/34b4d0d9-6127-44bc-9ba8-13006bcff99e/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/34b4d0d9-6127-44bc-9ba8-13006bcff99e",
-                    "title": "Home Infusion Therapy Providers : 2024-07-09",
+                    "format": "API",
                     "modified": "2024-07-09",
-                    "temporal": "2024-06-23/2024-07-06"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/34b4d0d9-6127-44bc-9ba8-13006bcff99e",
+                    "temporal": "2024-06-23/2024-07-06",
+                    "title": "Home Infusion Therapy Providers : 2024-07-09"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/4d340e2d-abd5-4b4d-a2f3-1a28b44bf9b2/Home%20Infusion%20Therapy%206.24.2024.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/49ba4df7-1f31-4b68-979d-37a08440d65c",
-                    "title": "Home Infusion Therapy Providers : 2024-06-25",
                     "modified": "2024-06-25",
-                    "temporal": "2024-06-09/2024-06-22"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/49ba4df7-1f31-4b68-979d-37a08440d65c",
+                    "temporal": "2024-06-09/2024-06-22",
+                    "title": "Home Infusion Therapy Providers : 2024-06-25"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/49ba4df7-1f31-4b68-979d-37a08440d65c/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/49ba4df7-1f31-4b68-979d-37a08440d65c",
-                    "title": "Home Infusion Therapy Providers : 2024-06-25",
+                    "format": "API",
                     "modified": "2024-06-25",
-                    "temporal": "2024-06-09/2024-06-22"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/49ba4df7-1f31-4b68-979d-37a08440d65c",
+                    "temporal": "2024-06-09/2024-06-22",
+                    "title": "Home Infusion Therapy Providers : 2024-06-25"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/3a7b7834-be2c-487b-9857-d49593da1d01/Home%20Infusion%20Therapy%206.10.2024.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f984f522-3a5d-4fe0-ab1e-c42f8aa0107e",
-                    "title": "Home Infusion Therapy Providers : 2024-06-11",
                     "modified": "2024-06-11",
-                    "temporal": "2024-05-26/2024-06-08"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f984f522-3a5d-4fe0-ab1e-c42f8aa0107e",
+                    "temporal": "2024-05-26/2024-06-08",
+                    "title": "Home Infusion Therapy Providers : 2024-06-11"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/f984f522-3a5d-4fe0-ab1e-c42f8aa0107e/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f984f522-3a5d-4fe0-ab1e-c42f8aa0107e",
-                    "title": "Home Infusion Therapy Providers : 2024-06-11",
+                    "format": "API",
                     "modified": "2024-06-11",
-                    "temporal": "2024-05-26/2024-06-08"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f984f522-3a5d-4fe0-ab1e-c42f8aa0107e",
+                    "temporal": "2024-05-26/2024-06-08",
+                    "title": "Home Infusion Therapy Providers : 2024-06-11"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/f94db978-d795-47d9-b811-9251f59f65fa/Home%20Infusion%20Therapy%205.27.2024.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5fc05909-1f6c-4926-8002-61a0623351df",
-                    "title": "Home Infusion Therapy Providers : 2024-05-28",
                     "modified": "2024-05-28",
-                    "temporal": "2024-05-12/2024-05-25"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5fc05909-1f6c-4926-8002-61a0623351df",
+                    "temporal": "2024-05-12/2024-05-25",
+                    "title": "Home Infusion Therapy Providers : 2024-05-28"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/5fc05909-1f6c-4926-8002-61a0623351df/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5fc05909-1f6c-4926-8002-61a0623351df",
-                    "title": "Home Infusion Therapy Providers : 2024-05-28",
+                    "format": "API",
                     "modified": "2024-05-28",
-                    "temporal": "2024-05-12/2024-05-25"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5fc05909-1f6c-4926-8002-61a0623351df",
+                    "temporal": "2024-05-12/2024-05-25",
+                    "title": "Home Infusion Therapy Providers : 2024-05-28"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/14f4cdd6-6b3d-49c5-8c37-bed1f19c7ee8/Home%20Infusion%20Therapy%205.15.2024.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/71887189-9d27-48bd-a4a8-5864d667baf5",
-                    "title": "Home Infusion Therapy Providers : 2024-05-17",
                     "modified": "2024-05-17",
-                    "temporal": "2024-04-28/2024-05-11"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/71887189-9d27-48bd-a4a8-5864d667baf5",
+                    "temporal": "2024-04-28/2024-05-11",
+                    "title": "Home Infusion Therapy Providers : 2024-05-17"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/71887189-9d27-48bd-a4a8-5864d667baf5/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/71887189-9d27-48bd-a4a8-5864d667baf5",
-                    "title": "Home Infusion Therapy Providers : 2024-05-17",
+                    "format": "API",
                     "modified": "2024-05-17",
-                    "temporal": "2024-04-28/2024-05-11"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/71887189-9d27-48bd-a4a8-5864d667baf5",
+                    "temporal": "2024-04-28/2024-05-11",
+                    "title": "Home Infusion Therapy Providers : 2024-05-17"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/7e812996-009e-488f-916a-5897be832747/Home%20Infusion%20Therapy%205.6.2024.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b65b680d-aac2-4aea-bc51-fc5a3bdd0396",
-                    "title": "Home Infusion Therapy Providers : 2024-05-07",
                     "modified": "2024-05-07",
-                    "temporal": "2024-04-21/2024-05-04"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b65b680d-aac2-4aea-bc51-fc5a3bdd0396",
+                    "temporal": "2024-04-21/2024-05-04",
+                    "title": "Home Infusion Therapy Providers : 2024-05-07"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/b65b680d-aac2-4aea-bc51-fc5a3bdd0396/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b65b680d-aac2-4aea-bc51-fc5a3bdd0396",
-                    "title": "Home Infusion Therapy Providers : 2024-05-07",
+                    "format": "API",
                     "modified": "2024-05-07",
-                    "temporal": "2024-04-21/2024-05-04"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b65b680d-aac2-4aea-bc51-fc5a3bdd0396",
+                    "temporal": "2024-04-21/2024-05-04",
+                    "title": "Home Infusion Therapy Providers : 2024-05-07"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/3d81abd4-c352-4761-8672-d43ba76e6813/Home%20Infusion%20Therapy%204.22.2024.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/cd4db424-23ca-40fd-87e0-a8dfceb1b94e",
-                    "title": "Home Infusion Therapy Providers : 2024-04-22",
                     "modified": "2024-04-22",
-                    "temporal": "2024-04-07/2024-04-20"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/cd4db424-23ca-40fd-87e0-a8dfceb1b94e",
+                    "temporal": "2024-04-07/2024-04-20",
+                    "title": "Home Infusion Therapy Providers : 2024-04-22"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/cd4db424-23ca-40fd-87e0-a8dfceb1b94e/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/cd4db424-23ca-40fd-87e0-a8dfceb1b94e",
-                    "title": "Home Infusion Therapy Providers : 2024-04-22",
+                    "format": "API",
                     "modified": "2024-04-22",
-                    "temporal": "2024-04-07/2024-04-20"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/cd4db424-23ca-40fd-87e0-a8dfceb1b94e",
+                    "temporal": "2024-04-07/2024-04-20",
+                    "title": "Home Infusion Therapy Providers : 2024-04-22"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/bcb776ec-ee3e-4b41-9e93-e64b24a0e19c/Home%20Infusion%20Therapy%204.8.2024.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b22ad616-c507-4774-b2fb-77ae14b30ed3",
-                    "title": "Home Infusion Therapy Providers : 2024-04-09",
                     "modified": "2024-04-09",
-                    "temporal": "2024-03-24/2024-04-06"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b22ad616-c507-4774-b2fb-77ae14b30ed3",
+                    "temporal": "2024-03-24/2024-04-06",
+                    "title": "Home Infusion Therapy Providers : 2024-04-09"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/b22ad616-c507-4774-b2fb-77ae14b30ed3/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b22ad616-c507-4774-b2fb-77ae14b30ed3",
-                    "title": "Home Infusion Therapy Providers : 2024-04-09",
+                    "format": "API",
                     "modified": "2024-04-09",
-                    "temporal": "2024-03-24/2024-04-06"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b22ad616-c507-4774-b2fb-77ae14b30ed3",
+                    "temporal": "2024-03-24/2024-04-06",
+                    "title": "Home Infusion Therapy Providers : 2024-04-09"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/7dd8ecc0-27ff-4d3e-a7b7-6fc5a628e872/Home%20Infusion%20Therapy%203.25.2024.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1dba13c6-07b3-4687-9aca-78ffda9ffd9c",
-                    "title": "Home Infusion Therapy Providers : 2024-03-26",
                     "modified": "2024-03-26",
-                    "temporal": "2024-03-10/2024-03-23"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1dba13c6-07b3-4687-9aca-78ffda9ffd9c",
+                    "temporal": "2024-03-10/2024-03-23",
+                    "title": "Home Infusion Therapy Providers : 2024-03-26"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/1dba13c6-07b3-4687-9aca-78ffda9ffd9c/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1dba13c6-07b3-4687-9aca-78ffda9ffd9c",
-                    "title": "Home Infusion Therapy Providers : 2024-03-26",
+                    "format": "API",
                     "modified": "2024-03-26",
-                    "temporal": "2024-03-10/2024-03-23"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1dba13c6-07b3-4687-9aca-78ffda9ffd9c",
+                    "temporal": "2024-03-10/2024-03-23",
+                    "title": "Home Infusion Therapy Providers : 2024-03-26"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/a0645e94-4abe-41ce-87d6-faf616e105df/Home%20Infusion%20Therapy%203.11.2024.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9116e170-6df0-4e14-a8dd-26acae6486eb",
-                    "title": "Home Infusion Therapy Providers : 2024-03-11",
                     "modified": "2024-03-12",
-                    "temporal": "2024-02-25/2024-03-09"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9116e170-6df0-4e14-a8dd-26acae6486eb",
+                    "temporal": "2024-02-25/2024-03-09",
+                    "title": "Home Infusion Therapy Providers : 2024-03-11"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/9116e170-6df0-4e14-a8dd-26acae6486eb/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9116e170-6df0-4e14-a8dd-26acae6486eb",
-                    "title": "Home Infusion Therapy Providers : 2024-03-11",
+                    "format": "API",
                     "modified": "2024-03-12",
-                    "temporal": "2024-02-25/2024-03-09"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9116e170-6df0-4e14-a8dd-26acae6486eb",
+                    "temporal": "2024-02-25/2024-03-09",
+                    "title": "Home Infusion Therapy Providers : 2024-03-11"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/075e1ce7-a2fd-4fd6-8a0e-8396d181075c/Home%20Infusion%20Therapy%202.26.2024.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/20d8dfe6-a7bf-4e95-901b-12db792b8998",
-                    "title": "Home Infusion Therapy Providers : 2024-02-26",
                     "modified": "2024-02-26",
-                    "temporal": "2024-02-11/2024-02-24"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/20d8dfe6-a7bf-4e95-901b-12db792b8998",
+                    "temporal": "2024-02-11/2024-02-24",
+                    "title": "Home Infusion Therapy Providers : 2024-02-26"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/20d8dfe6-a7bf-4e95-901b-12db792b8998/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/20d8dfe6-a7bf-4e95-901b-12db792b8998",
-                    "title": "Home Infusion Therapy Providers : 2024-02-26",
+                    "format": "API",
                     "modified": "2024-02-26",
-                    "temporal": "2024-02-11/2024-02-24"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/20d8dfe6-a7bf-4e95-901b-12db792b8998",
+                    "temporal": "2024-02-11/2024-02-24",
+                    "title": "Home Infusion Therapy Providers : 2024-02-26"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/750fda9a-65f3-4421-bb6a-8ff768692880/Home%20Infusion%20Therapy%202.12.2024.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/db54201d-9c1e-4b05-bad4-766d5f1e2150",
-                    "title": "Home Infusion Therapy Providers : 2024-02-13",
                     "modified": "2024-02-13",
-                    "temporal": "2024-01-28/2024-02-10"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/db54201d-9c1e-4b05-bad4-766d5f1e2150",
+                    "temporal": "2024-01-28/2024-02-10",
+                    "title": "Home Infusion Therapy Providers : 2024-02-13"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/db54201d-9c1e-4b05-bad4-766d5f1e2150/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/db54201d-9c1e-4b05-bad4-766d5f1e2150",
-                    "title": "Home Infusion Therapy Providers : 2024-02-13",
+                    "format": "API",
                     "modified": "2024-02-13",
-                    "temporal": "2024-01-28/2024-02-10"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/db54201d-9c1e-4b05-bad4-766d5f1e2150",
+                    "temporal": "2024-01-28/2024-02-10",
+                    "title": "Home Infusion Therapy Providers : 2024-02-13"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/a49c47a3-1984-48f7-9a13-cc2e49f1ca5e/Home%20Infusion%20Therapy%201.29.2024.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e0fc2c94-d507-48a0-9023-a2b329587f26",
-                    "title": "Home Infusion Therapy Providers : 2024-01-30",
                     "modified": "2024-01-30",
-                    "temporal": "2024-01-14/2024-01-27"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e0fc2c94-d507-48a0-9023-a2b329587f26",
+                    "temporal": "2024-01-14/2024-01-27",
+                    "title": "Home Infusion Therapy Providers : 2024-01-30"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/e0fc2c94-d507-48a0-9023-a2b329587f26/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e0fc2c94-d507-48a0-9023-a2b329587f26",
-                    "title": "Home Infusion Therapy Providers : 2024-01-30",
+                    "format": "API",
                     "modified": "2024-01-30",
-                    "temporal": "2024-01-14/2024-01-27"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e0fc2c94-d507-48a0-9023-a2b329587f26",
+                    "temporal": "2024-01-14/2024-01-27",
+                    "title": "Home Infusion Therapy Providers : 2024-01-30"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/ccf2bd40-7060-4df3-b7ee-6bd5e1c172cd/Home%20Infusion%20Therapy%201.16.2024.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ffc5c501-5afc-475a-a3b9-e92434021129",
-                    "title": "Home Infusion Therapy Providers : 2024-01-16",
                     "modified": "2024-01-16",
-                    "temporal": "2023-12-31/2024-01-13"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ffc5c501-5afc-475a-a3b9-e92434021129",
+                    "temporal": "2023-12-31/2024-01-13",
+                    "title": "Home Infusion Therapy Providers : 2024-01-16"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/ffc5c501-5afc-475a-a3b9-e92434021129/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ffc5c501-5afc-475a-a3b9-e92434021129",
-                    "title": "Home Infusion Therapy Providers : 2024-01-16",
+                    "format": "API",
                     "modified": "2024-01-16",
-                    "temporal": "2023-12-31/2024-01-13"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ffc5c501-5afc-475a-a3b9-e92434021129",
+                    "temporal": "2023-12-31/2024-01-13",
+                    "title": "Home Infusion Therapy Providers : 2024-01-16"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/8c89d6f5-1975-426e-ab9e-bde671477a2d/Home%20Infusion%20Therapy%201.2.2024.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c3665883-a1a6-4079-b776-db16825fa9de",
-                    "title": "Home Infusion Therapy Providers : 2024-01-02",
                     "modified": "2024-01-02",
-                    "temporal": "2023-12-17/2023-12-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c3665883-a1a6-4079-b776-db16825fa9de",
+                    "temporal": "2023-12-17/2023-12-30",
+                    "title": "Home Infusion Therapy Providers : 2024-01-02"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/c3665883-a1a6-4079-b776-db16825fa9de/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c3665883-a1a6-4079-b776-db16825fa9de",
-                    "title": "Home Infusion Therapy Providers : 2024-01-02",
+                    "format": "API",
                     "modified": "2024-01-02",
-                    "temporal": "2023-12-17/2023-12-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c3665883-a1a6-4079-b776-db16825fa9de",
+                    "temporal": "2023-12-17/2023-12-30",
+                    "title": "Home Infusion Therapy Providers : 2024-01-02"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/b5412976-cd08-4594-aeed-1225611839d9/Home%20Infusion%20Therapy%2012.19.2023.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ee0b3463-6a97-444d-b81f-e59a8f067c16",
-                    "title": "Home Infusion Therapy Providers : 2023-12-20",
                     "modified": "2023-12-20",
-                    "temporal": "2023-12-03/2023-12-16"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ee0b3463-6a97-444d-b81f-e59a8f067c16",
+                    "temporal": "2023-12-03/2023-12-16",
+                    "title": "Home Infusion Therapy Providers : 2023-12-20"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/ee0b3463-6a97-444d-b81f-e59a8f067c16/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ee0b3463-6a97-444d-b81f-e59a8f067c16",
-                    "title": "Home Infusion Therapy Providers : 2023-12-20",
+                    "format": "API",
                     "modified": "2023-12-20",
-                    "temporal": "2023-12-03/2023-12-16"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ee0b3463-6a97-444d-b81f-e59a8f067c16",
+                    "temporal": "2023-12-03/2023-12-16",
+                    "title": "Home Infusion Therapy Providers : 2023-12-20"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/04ef54c0-0b86-47fd-801b-f20e8f383d38/Home%20Infusion%20Therapy%2011.22.2023.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/44c9c855-3308-42d2-882e-969f7d0168d3",
-                    "title": "Home Infusion Therapy Providers : 2023-11-22",
                     "modified": "2023-11-22",
-                    "temporal": "2023-11-05/2023-11-18"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/44c9c855-3308-42d2-882e-969f7d0168d3",
+                    "temporal": "2023-11-05/2023-11-18",
+                    "title": "Home Infusion Therapy Providers : 2023-11-22"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/44c9c855-3308-42d2-882e-969f7d0168d3/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/44c9c855-3308-42d2-882e-969f7d0168d3",
-                    "title": "Home Infusion Therapy Providers : 2023-11-22",
+                    "format": "API",
                     "modified": "2023-11-22",
-                    "temporal": "2023-11-05/2023-11-18"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/44c9c855-3308-42d2-882e-969f7d0168d3",
+                    "temporal": "2023-11-05/2023-11-18",
+                    "title": "Home Infusion Therapy Providers : 2023-11-22"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/70d01c6d-0761-4cae-8ef0-405e2f22d15b/Home%20Infusion%20Therapy%2010.27.2023.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e1b91378-0377-4deb-a3cf-663eb9544673",
-                    "title": "Home Infusion Therapy Providers : 2023-10-27",
                     "modified": "2023-10-27",
-                    "temporal": "2023-10-08/2023-10-21"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e1b91378-0377-4deb-a3cf-663eb9544673",
+                    "temporal": "2023-10-08/2023-10-21",
+                    "title": "Home Infusion Therapy Providers : 2023-10-27"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/e1b91378-0377-4deb-a3cf-663eb9544673/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e1b91378-0377-4deb-a3cf-663eb9544673",
-                    "title": "Home Infusion Therapy Providers : 2023-10-27",
+                    "format": "API",
                     "modified": "2023-10-27",
-                    "temporal": "2023-10-08/2023-10-21"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e1b91378-0377-4deb-a3cf-663eb9544673",
+                    "temporal": "2023-10-08/2023-10-21",
+                    "title": "Home Infusion Therapy Providers : 2023-10-27"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/68fbba81-f338-4e5e-8ee2-c9613832830a/Home%20Infusion%20Therapy%2010.12.2023.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c3aab410-1c04-42d5-ad97-a9fe9b916a73",
-                    "title": "Home Infusion Therapy Providers : 2023-10-12",
                     "modified": "2023-10-12",
-                    "temporal": "2023-09-24/2023-10-07"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c3aab410-1c04-42d5-ad97-a9fe9b916a73",
+                    "temporal": "2023-09-24/2023-10-07",
+                    "title": "Home Infusion Therapy Providers : 2023-10-12"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/c3aab410-1c04-42d5-ad97-a9fe9b916a73/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c3aab410-1c04-42d5-ad97-a9fe9b916a73",
-                    "title": "Home Infusion Therapy Providers : 2023-10-12",
+                    "format": "API",
                     "modified": "2023-10-12",
-                    "temporal": "2023-09-24/2023-10-07"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c3aab410-1c04-42d5-ad97-a9fe9b916a73",
+                    "temporal": "2023-09-24/2023-10-07",
+                    "title": "Home Infusion Therapy Providers : 2023-10-12"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/3160a3e2-526e-45c8-bb92-c0f17b99ce73/Home%20Infusion%20Therapy%2009.29.2023.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ddfb7fb3-86ba-40e1-979f-ddcbd9149677",
-                    "title": "Home Infusion Therapy Providers : 2023-09-29",
                     "modified": "2023-09-29",
-                    "temporal": "2023-09-10/2023-09-23"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ddfb7fb3-86ba-40e1-979f-ddcbd9149677",
+                    "temporal": "2023-09-10/2023-09-23",
+                    "title": "Home Infusion Therapy Providers : 2023-09-29"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/ddfb7fb3-86ba-40e1-979f-ddcbd9149677/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ddfb7fb3-86ba-40e1-979f-ddcbd9149677",
-                    "title": "Home Infusion Therapy Providers : 2023-09-29",
+                    "format": "API",
                     "modified": "2023-09-29",
-                    "temporal": "2023-09-10/2023-09-23"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ddfb7fb3-86ba-40e1-979f-ddcbd9149677",
+                    "temporal": "2023-09-10/2023-09-23",
+                    "title": "Home Infusion Therapy Providers : 2023-09-29"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/bc6da7c8-f327-44e0-ae76-c336efb7351d/Home%20Infusion%20Therapy%2009.14.2023.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d6e25ad2-598c-4ad9-9430-8eb596b1eeb3",
-                    "title": "Home Infusion Therapy Providers : 2023-09-14",
                     "modified": "2023-09-14",
-                    "temporal": "2023-08-27/2023-09-09"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d6e25ad2-598c-4ad9-9430-8eb596b1eeb3",
+                    "temporal": "2023-08-27/2023-09-09",
+                    "title": "Home Infusion Therapy Providers : 2023-09-14"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/d6e25ad2-598c-4ad9-9430-8eb596b1eeb3/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d6e25ad2-598c-4ad9-9430-8eb596b1eeb3",
-                    "title": "Home Infusion Therapy Providers : 2023-09-14",
+                    "format": "API",
                     "modified": "2023-09-14",
-                    "temporal": "2023-08-27/2023-09-09"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d6e25ad2-598c-4ad9-9430-8eb596b1eeb3",
+                    "temporal": "2023-08-27/2023-09-09",
+                    "title": "Home Infusion Therapy Providers : 2023-09-14"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/8c1ac232-330f-4853-9805-7417c3e81b20/Home%20Infusion%20Therapy%2008.31.2023.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/991a98b9-64d7-4a33-ac26-7c1a1471f435",
-                    "title": "Home Infusion Therapy Providers : 2023-08-31",
                     "modified": "2023-08-31",
-                    "temporal": "2023-08-13/2023-08-26"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/991a98b9-64d7-4a33-ac26-7c1a1471f435",
+                    "temporal": "2023-08-13/2023-08-26",
+                    "title": "Home Infusion Therapy Providers : 2023-08-31"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/991a98b9-64d7-4a33-ac26-7c1a1471f435/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/991a98b9-64d7-4a33-ac26-7c1a1471f435",
-                    "title": "Home Infusion Therapy Providers : 2023-08-31",
+                    "format": "API",
                     "modified": "2023-08-31",
-                    "temporal": "2023-08-13/2023-08-26"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/991a98b9-64d7-4a33-ac26-7c1a1471f435",
+                    "temporal": "2023-08-13/2023-08-26",
+                    "title": "Home Infusion Therapy Providers : 2023-08-31"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/bf9d90fc-dca3-47bc-9d22-a239ccbda4f9/Home%20Infusion%20Therapy%2008.18.2023.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/277b8532-670e-4f2b-bd7d-7a3921c296df",
-                    "title": "Home Infusion Therapy Providers : 2023-08-18",
                     "modified": "2023-08-18",
-                    "temporal": "2023-07-30/2023-08-12"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/277b8532-670e-4f2b-bd7d-7a3921c296df",
+                    "temporal": "2023-07-30/2023-08-12",
+                    "title": "Home Infusion Therapy Providers : 2023-08-18"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/277b8532-670e-4f2b-bd7d-7a3921c296df/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/277b8532-670e-4f2b-bd7d-7a3921c296df",
-                    "title": "Home Infusion Therapy Providers : 2023-08-18",
+                    "format": "API",
                     "modified": "2023-08-18",
-                    "temporal": "2023-07-30/2023-08-12"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/277b8532-670e-4f2b-bd7d-7a3921c296df",
+                    "temporal": "2023-07-30/2023-08-12",
+                    "title": "Home Infusion Therapy Providers : 2023-08-18"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/e3c3808b-84df-42c7-81fe-9d622cbd4199/Home%20Infusion%20Therapy%2008.04.2023.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e8ee2dbb-d135-45ba-8feb-03cddb0b0bf4",
-                    "title": "Home Infusion Therapy Providers : 2023-08-04",
                     "modified": "2023-08-04",
-                    "temporal": "2023-07-16/2023-07-29"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e8ee2dbb-d135-45ba-8feb-03cddb0b0bf4",
+                    "temporal": "2023-07-16/2023-07-29",
+                    "title": "Home Infusion Therapy Providers : 2023-08-04"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/e8ee2dbb-d135-45ba-8feb-03cddb0b0bf4/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e8ee2dbb-d135-45ba-8feb-03cddb0b0bf4",
-                    "title": "Home Infusion Therapy Providers : 2023-08-04",
+                    "format": "API",
                     "modified": "2023-08-04",
-                    "temporal": "2023-07-16/2023-07-29"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e8ee2dbb-d135-45ba-8feb-03cddb0b0bf4",
+                    "temporal": "2023-07-16/2023-07-29",
+                    "title": "Home Infusion Therapy Providers : 2023-08-04"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/e62afdc9-e5d2-4d70-bc87-d48d1739c992/Home%20Infusion%20Therapy%2007.20.2023.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/09ae777f-10cf-4790-acee-5b513482f801",
-                    "title": "Home Infusion Therapy Providers : 2023-07-21",
                     "modified": "2023-07-21",
-                    "temporal": "2023-07-02/2023-07-15"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/09ae777f-10cf-4790-acee-5b513482f801",
+                    "temporal": "2023-07-02/2023-07-15",
+                    "title": "Home Infusion Therapy Providers : 2023-07-21"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/09ae777f-10cf-4790-acee-5b513482f801/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/09ae777f-10cf-4790-acee-5b513482f801",
-                    "title": "Home Infusion Therapy Providers : 2023-07-21",
+                    "format": "API",
                     "modified": "2023-07-21",
-                    "temporal": "2023-07-02/2023-07-15"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/09ae777f-10cf-4790-acee-5b513482f801",
+                    "temporal": "2023-07-02/2023-07-15",
+                    "title": "Home Infusion Therapy Providers : 2023-07-21"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/3e4d46bf-c011-4baa-a075-1c4608db5622/Home%20Infusion%20Therapy%2007.07.2023.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3eb706ec-7494-4608-9b03-6dc374ce3ae8",
-                    "title": "Home Infusion Therapy Providers : 2023-07-07",
                     "modified": "2023-07-07",
-                    "temporal": "2023-06-18/2023-07-01"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3eb706ec-7494-4608-9b03-6dc374ce3ae8",
+                    "temporal": "2023-06-18/2023-07-01",
+                    "title": "Home Infusion Therapy Providers : 2023-07-07"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/3eb706ec-7494-4608-9b03-6dc374ce3ae8/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3eb706ec-7494-4608-9b03-6dc374ce3ae8",
-                    "title": "Home Infusion Therapy Providers : 2023-07-07",
+                    "format": "API",
                     "modified": "2023-07-07",
-                    "temporal": "2023-06-18/2023-07-01"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3eb706ec-7494-4608-9b03-6dc374ce3ae8",
+                    "temporal": "2023-06-18/2023-07-01",
+                    "title": "Home Infusion Therapy Providers : 2023-07-07"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/aec0d657-f330-498a-8383-4ce6ccb5014b/Home%20Infusion%20Therapy%2006.22.2023.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f424a96b-1288-4089-ac11-de6a8d2a46af",
-                    "title": "Home Infusion Therapy Providers : 2023-06-22",
                     "modified": "2023-06-22",
-                    "temporal": "2023-06-04/2023-06-17"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f424a96b-1288-4089-ac11-de6a8d2a46af",
+                    "temporal": "2023-06-04/2023-06-17",
+                    "title": "Home Infusion Therapy Providers : 2023-06-22"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/f424a96b-1288-4089-ac11-de6a8d2a46af/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f424a96b-1288-4089-ac11-de6a8d2a46af",
-                    "title": "Home Infusion Therapy Providers : 2023-06-22",
+                    "format": "API",
                     "modified": "2023-06-22",
-                    "temporal": "2023-06-04/2023-06-17"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f424a96b-1288-4089-ac11-de6a8d2a46af",
+                    "temporal": "2023-06-04/2023-06-17",
+                    "title": "Home Infusion Therapy Providers : 2023-06-22"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/73194870-bc08-41c5-8283-d954a812fd94/Home%20Infusion%20Therapy%2006.08.2023.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e1f868a9-a28f-4bd8-ac70-cfa1616039e8",
-                    "title": "Home Infusion Therapy Providers : 2023-06-08",
                     "modified": "2023-06-08",
-                    "temporal": "2023-05-21/2023-06-03"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e1f868a9-a28f-4bd8-ac70-cfa1616039e8",
+                    "temporal": "2023-05-21/2023-06-03",
+                    "title": "Home Infusion Therapy Providers : 2023-06-08"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/e1f868a9-a28f-4bd8-ac70-cfa1616039e8/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e1f868a9-a28f-4bd8-ac70-cfa1616039e8",
-                    "title": "Home Infusion Therapy Providers : 2023-06-08",
+                    "format": "API",
                     "modified": "2023-06-08",
-                    "temporal": "2023-05-21/2023-06-03"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e1f868a9-a28f-4bd8-ac70-cfa1616039e8",
+                    "temporal": "2023-05-21/2023-06-03",
+                    "title": "Home Infusion Therapy Providers : 2023-06-08"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/3283d350-5de4-4db2-8536-64abd6adaae3/Home%20Infusion%20Therapy%2005.25.2023.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4c81d8d9-b534-45d3-91e8-c72c90595152",
-                    "title": "Home Infusion Therapy Providers : 2023-05-25",
                     "modified": "2023-05-25",
-                    "temporal": "2023-05-07/2023-05-20"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4c81d8d9-b534-45d3-91e8-c72c90595152",
+                    "temporal": "2023-05-07/2023-05-20",
+                    "title": "Home Infusion Therapy Providers : 2023-05-25"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/4c81d8d9-b534-45d3-91e8-c72c90595152/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4c81d8d9-b534-45d3-91e8-c72c90595152",
-                    "title": "Home Infusion Therapy Providers : 2023-05-25",
+                    "format": "API",
                     "modified": "2023-05-25",
-                    "temporal": "2023-05-07/2023-05-20"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4c81d8d9-b534-45d3-91e8-c72c90595152",
+                    "temporal": "2023-05-07/2023-05-20",
+                    "title": "Home Infusion Therapy Providers : 2023-05-25"
                 }
             ],
             "identifier": "https://data.cms.gov/data-api/v1/dataset/31f25ab6-2fe3-4bad-ac5a-90635ed79935/data-viewer",
@@ -9379,164 +9378,164 @@
                 "fn": "Provider Enrollment Data Requests - CPI",
                 "hasEmail": "mailto:ProviderEnrollmentDataRequests@cms.hhs.gov"
             },
+            "dataQuality": true,
             "describedBy": "https://data.cms.gov/sites/default/files/2024-10/Hospice_All_Owners_Data_Dictionary.pdf",
             "describedByType": "application/pdf",
-            "dataQuality": true,
             "description": "The \u00a0Hospice All Owners dataset provides ownership information on all hospices currently enrolled in Medicare. This data includes ownership information such as ownership name, ownership type, ownership address and ownership effective date.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/e983965e-1603-4cb8-82b5-c40090e380d1/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e983965e-1603-4cb8-82b5-c40090e380d1",
                     "description": "latest",
-                    "title": "Hospice All Owners : 2025-01-01",
+                    "format": "API",
                     "modified": "2025-01-15",
-                    "temporal": "2025-01-01/2025-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e983965e-1603-4cb8-82b5-c40090e380d1",
+                    "temporal": "2025-01-01/2025-03-31",
+                    "title": "Hospice All Owners : 2025-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/662c8886-9074-4669-bbfb-3807ba85b484/Hospice_All_Owners_2025.01.02.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/31bebe15-6de5-496c-af31-65da426d03d2",
-                    "title": "Hospice All Owners : 2025-01-01",
                     "modified": "2025-01-15",
-                    "temporal": "2025-01-01/2025-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/31bebe15-6de5-496c-af31-65da426d03d2",
+                    "temporal": "2025-01-01/2025-03-31",
+                    "title": "Hospice All Owners : 2025-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/31bebe15-6de5-496c-af31-65da426d03d2/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/31bebe15-6de5-496c-af31-65da426d03d2",
-                    "title": "Hospice All Owners : 2025-01-01",
+                    "format": "API",
                     "modified": "2025-01-15",
-                    "temporal": "2025-01-01/2025-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/31bebe15-6de5-496c-af31-65da426d03d2",
+                    "temporal": "2025-01-01/2025-03-31",
+                    "title": "Hospice All Owners : 2025-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/135426ab-453d-424e-bba8-c89cd53d947f/Hospice_All_Owners_2024.10.07.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0d8d3a8b-21c0-4967-8df0-ad4032ad3d3d",
-                    "title": "Hospice All Owners : 2024-10-01",
                     "modified": "2024-10-15",
-                    "temporal": "2024-10-01/2024-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0d8d3a8b-21c0-4967-8df0-ad4032ad3d3d",
+                    "temporal": "2024-10-01/2024-12-31",
+                    "title": "Hospice All Owners : 2024-10-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/0d8d3a8b-21c0-4967-8df0-ad4032ad3d3d/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0d8d3a8b-21c0-4967-8df0-ad4032ad3d3d",
-                    "title": "Hospice All Owners : 2024-10-01",
+                    "format": "API",
                     "modified": "2024-10-15",
-                    "temporal": "2024-10-01/2024-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0d8d3a8b-21c0-4967-8df0-ad4032ad3d3d",
+                    "temporal": "2024-10-01/2024-12-31",
+                    "title": "Hospice All Owners : 2024-10-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/354ce286-5164-4722-8a43-6b8e90df3684/Hospice_All_Owners_2024.07.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f5f4be6a-49fb-43e4-bb02-b260f1011985",
-                    "title": "Hospice All Owners : 2024-07-01",
                     "modified": "2024-07-15",
-                    "temporal": "2024-07-01/2024-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f5f4be6a-49fb-43e4-bb02-b260f1011985",
+                    "temporal": "2024-07-01/2024-09-30",
+                    "title": "Hospice All Owners : 2024-07-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/f5f4be6a-49fb-43e4-bb02-b260f1011985/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f5f4be6a-49fb-43e4-bb02-b260f1011985",
-                    "title": "Hospice All Owners : 2024-07-01",
+                    "format": "API",
                     "modified": "2024-07-15",
-                    "temporal": "2024-07-01/2024-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f5f4be6a-49fb-43e4-bb02-b260f1011985",
+                    "temporal": "2024-07-01/2024-09-30",
+                    "title": "Hospice All Owners : 2024-07-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/06f1815a-c792-4888-90e0-141539f3f59b/Hospice_All_Owners_2024.04.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5d27cc83-31fc-41ba-a97c-c0302e93081e",
-                    "title": "Hospice All Owners : 2024-04-01",
                     "modified": "2024-04-15",
-                    "temporal": "2024-04-01/2024-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5d27cc83-31fc-41ba-a97c-c0302e93081e",
+                    "temporal": "2024-04-01/2024-06-30",
+                    "title": "Hospice All Owners : 2024-04-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/5d27cc83-31fc-41ba-a97c-c0302e93081e/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5d27cc83-31fc-41ba-a97c-c0302e93081e",
-                    "title": "Hospice All Owners : 2024-04-01",
+                    "format": "API",
                     "modified": "2024-04-15",
-                    "temporal": "2024-04-01/2024-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/5d27cc83-31fc-41ba-a97c-c0302e93081e",
+                    "temporal": "2024-04-01/2024-06-30",
+                    "title": "Hospice All Owners : 2024-04-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/78185aa4-ca7b-4746-9340-88631bc75341/Hospice_All_Owners_2024.01.05.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a53bdaf9-7650-4ec4-ad43-1cf9676afffb",
-                    "title": "Hospice All Owners : 2024-01-05",
                     "modified": "2024-01-19",
-                    "temporal": "2024-01-01/2024-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a53bdaf9-7650-4ec4-ad43-1cf9676afffb",
+                    "temporal": "2024-01-01/2024-03-31",
+                    "title": "Hospice All Owners : 2024-01-05"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/a53bdaf9-7650-4ec4-ad43-1cf9676afffb/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a53bdaf9-7650-4ec4-ad43-1cf9676afffb",
-                    "title": "Hospice All Owners : 2024-01-05",
+                    "format": "API",
                     "modified": "2024-01-19",
-                    "temporal": "2024-01-01/2024-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a53bdaf9-7650-4ec4-ad43-1cf9676afffb",
+                    "temporal": "2024-01-01/2024-03-31",
+                    "title": "Hospice All Owners : 2024-01-05"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/3902d572-c865-4ffe-a721-0c23782c0a5e/Hospice_All_Owners_2023.10.02.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/12e0cedf-6c91-4edc-bf85-85a249658f38",
-                    "title": "Hospice All Owners : 2023-10-02",
                     "modified": "2023-10-16",
-                    "temporal": "2023-10-01/2023-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/12e0cedf-6c91-4edc-bf85-85a249658f38",
+                    "temporal": "2023-10-01/2023-12-31",
+                    "title": "Hospice All Owners : 2023-10-02"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/12e0cedf-6c91-4edc-bf85-85a249658f38/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/12e0cedf-6c91-4edc-bf85-85a249658f38",
-                    "title": "Hospice All Owners : 2023-10-02",
+                    "format": "API",
                     "modified": "2023-10-16",
-                    "temporal": "2023-10-01/2023-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/12e0cedf-6c91-4edc-bf85-85a249658f38",
+                    "temporal": "2023-10-01/2023-12-31",
+                    "title": "Hospice All Owners : 2023-10-02"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/b37deb97-253b-4876-bd6c-22c9fe6ef0c3/Hospice_All_Owners_2023.07.06.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0445304f-7d1d-47f3-a438-da084816a3ce",
-                    "title": "Hospice All Owners : 2023-07-17",
                     "modified": "2023-07-17",
-                    "temporal": "2023-07-01/2023-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0445304f-7d1d-47f3-a438-da084816a3ce",
+                    "temporal": "2023-07-01/2023-09-30",
+                    "title": "Hospice All Owners : 2023-07-17"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/0445304f-7d1d-47f3-a438-da084816a3ce/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0445304f-7d1d-47f3-a438-da084816a3ce",
-                    "title": "Hospice All Owners : 2023-07-17",
+                    "format": "API",
                     "modified": "2023-07-17",
-                    "temporal": "2023-07-01/2023-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0445304f-7d1d-47f3-a438-da084816a3ce",
+                    "temporal": "2023-07-01/2023-09-30",
+                    "title": "Hospice All Owners : 2023-07-17"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/53590f19-716d-4cb9-8381-e8c755f32a2b/Hospice_All_Owners_2023.03.31.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f200545a-cd96-4806-91d6-6212b485e0f0",
-                    "title": "Hospice All Owners : 2023-04-01",
                     "modified": "2023-04-19",
-                    "temporal": "2023-04-01/2023-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f200545a-cd96-4806-91d6-6212b485e0f0",
+                    "temporal": "2023-04-01/2023-06-30",
+                    "title": "Hospice All Owners : 2023-04-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/f200545a-cd96-4806-91d6-6212b485e0f0/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f200545a-cd96-4806-91d6-6212b485e0f0",
-                    "title": "Hospice All Owners : 2023-04-01",
+                    "format": "API",
                     "modified": "2023-04-19",
-                    "temporal": "2023-04-01/2023-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f200545a-cd96-4806-91d6-6212b485e0f0",
+                    "temporal": "2023-04-01/2023-06-30",
+                    "title": "Hospice All Owners : 2023-04-01"
                 }
             ],
             "identifier": "https://data.cms.gov/data-api/v1/dataset/e983965e-1603-4cb8-82b5-c40090e380d1/data-viewer",
@@ -9582,164 +9581,164 @@
                 "fn": "Provider Enrollment Data Requests - CPI",
                 "hasEmail": "mailto:ProviderEnrollmentDataRequests@cms.hhs.gov"
             },
+            "dataQuality": true,
             "describedBy": "https://data.cms.gov/sites/default/files/2023-03/f736ce50-3d6b-4ee2-802f-2e5424ae71ac/Hospice_Enrollments_Data_Dictionary.pdf",
             "describedByType": "application/pdf",
-            "dataQuality": true,
             "description": "The Hospice Enrollments dataset provides enrollment information of all hospices currently enrolled in Medicare. This data includes information on the hospice's legal business name, doing business as name, organization type and address.\u00a0",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/25704213-e833-4b8b-9dbc-58dd17149209/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/25704213-e833-4b8b-9dbc-58dd17149209",
                     "description": "latest",
-                    "title": "Hospice Enrollments : 2025-01-01",
+                    "format": "API",
                     "modified": "2025-01-15",
-                    "temporal": "2025-01-01/2025-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/25704213-e833-4b8b-9dbc-58dd17149209",
+                    "temporal": "2025-01-01/2025-03-31",
+                    "title": "Hospice Enrollments : 2025-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/afd62e57-8a99-4c49-a0b5-358a25ce39dd/Hospice_Enrollments_2025.01.02.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/44a82a38-fdad-4b7b-b0cc-68fe22fb76b0",
-                    "title": "Hospice Enrollments : 2025-01-01",
                     "modified": "2025-01-15",
-                    "temporal": "2025-01-01/2025-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/44a82a38-fdad-4b7b-b0cc-68fe22fb76b0",
+                    "temporal": "2025-01-01/2025-03-31",
+                    "title": "Hospice Enrollments : 2025-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/44a82a38-fdad-4b7b-b0cc-68fe22fb76b0/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/44a82a38-fdad-4b7b-b0cc-68fe22fb76b0",
-                    "title": "Hospice Enrollments : 2025-01-01",
+                    "format": "API",
                     "modified": "2025-01-15",
-                    "temporal": "2025-01-01/2025-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/44a82a38-fdad-4b7b-b0cc-68fe22fb76b0",
+                    "temporal": "2025-01-01/2025-03-31",
+                    "title": "Hospice Enrollments : 2025-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/92a4fe1f-34a9-4d07-97d7-278bc2ca3f1a/Hospice_Enrollments_2024.10.07.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a6a063c5-3d7c-463c-b914-07b8409ca8fd",
-                    "title": "Hospice Enrollments : 2024-10-01",
                     "modified": "2024-10-15",
-                    "temporal": "2024-10-01/2024-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a6a063c5-3d7c-463c-b914-07b8409ca8fd",
+                    "temporal": "2024-10-01/2024-12-31",
+                    "title": "Hospice Enrollments : 2024-10-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/a6a063c5-3d7c-463c-b914-07b8409ca8fd/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a6a063c5-3d7c-463c-b914-07b8409ca8fd",
-                    "title": "Hospice Enrollments : 2024-10-01",
+                    "format": "API",
                     "modified": "2024-10-15",
-                    "temporal": "2024-10-01/2024-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a6a063c5-3d7c-463c-b914-07b8409ca8fd",
+                    "temporal": "2024-10-01/2024-12-31",
+                    "title": "Hospice Enrollments : 2024-10-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/e51b5573-9e8e-49ad-9a48-7d2425a70a50/Hospice_Enrollments_2024.07.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d52c6495-6369-4bd7-9b98-788d4f98d245",
-                    "title": "Hospice Enrollments : 2024-07-01",
                     "modified": "2024-07-15",
-                    "temporal": "2024-07-01/2024-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d52c6495-6369-4bd7-9b98-788d4f98d245",
+                    "temporal": "2024-07-01/2024-09-30",
+                    "title": "Hospice Enrollments : 2024-07-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/d52c6495-6369-4bd7-9b98-788d4f98d245/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d52c6495-6369-4bd7-9b98-788d4f98d245",
-                    "title": "Hospice Enrollments : 2024-07-01",
+                    "format": "API",
                     "modified": "2024-07-15",
-                    "temporal": "2024-07-01/2024-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d52c6495-6369-4bd7-9b98-788d4f98d245",
+                    "temporal": "2024-07-01/2024-09-30",
+                    "title": "Hospice Enrollments : 2024-07-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/072ab653-71b7-454c-b3ed-2c0ee7a8455b/Hospice_Enrollments_2024.04.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e88e5497-b0d4-453a-9069-dfbb2faf44ef",
-                    "title": "Hospice Enrollments : 2024-04-01",
                     "modified": "2024-04-15",
-                    "temporal": "2024-04-01/2024-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e88e5497-b0d4-453a-9069-dfbb2faf44ef",
+                    "temporal": "2024-04-01/2024-06-30",
+                    "title": "Hospice Enrollments : 2024-04-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/e88e5497-b0d4-453a-9069-dfbb2faf44ef/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e88e5497-b0d4-453a-9069-dfbb2faf44ef",
-                    "title": "Hospice Enrollments : 2024-04-01",
+                    "format": "API",
                     "modified": "2024-04-15",
-                    "temporal": "2024-04-01/2024-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e88e5497-b0d4-453a-9069-dfbb2faf44ef",
+                    "temporal": "2024-04-01/2024-06-30",
+                    "title": "Hospice Enrollments : 2024-04-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/071c9976-59e6-46d4-9809-53454a1ced07/Hospice_Enrollments_2024.01.05.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/194e710e-1eac-4b27-a539-0d2bb8de40ea",
-                    "title": "Hospice Enrollments : 2024-01-05",
                     "modified": "2024-01-19",
-                    "temporal": "2024-01-01/2024-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/194e710e-1eac-4b27-a539-0d2bb8de40ea",
+                    "temporal": "2024-01-01/2024-03-31",
+                    "title": "Hospice Enrollments : 2024-01-05"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/194e710e-1eac-4b27-a539-0d2bb8de40ea/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/194e710e-1eac-4b27-a539-0d2bb8de40ea",
-                    "title": "Hospice Enrollments : 2024-01-05",
+                    "format": "API",
                     "modified": "2024-01-19",
-                    "temporal": "2024-01-01/2024-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/194e710e-1eac-4b27-a539-0d2bb8de40ea",
+                    "temporal": "2024-01-01/2024-03-31",
+                    "title": "Hospice Enrollments : 2024-01-05"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/9df81161-c7ff-471b-8329-efb2c7d36929/Hospice_Enrollments_2023.10.02.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/df9b9c6e-9b8a-4c4d-993c-bc9541d72a49",
-                    "title": "Hospice Enrollments : 2023-10-02",
                     "modified": "2023-10-16",
-                    "temporal": "2023-10-01/2023-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/df9b9c6e-9b8a-4c4d-993c-bc9541d72a49",
+                    "temporal": "2023-10-01/2023-12-31",
+                    "title": "Hospice Enrollments : 2023-10-02"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/df9b9c6e-9b8a-4c4d-993c-bc9541d72a49/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/df9b9c6e-9b8a-4c4d-993c-bc9541d72a49",
-                    "title": "Hospice Enrollments : 2023-10-02",
+                    "format": "API",
                     "modified": "2023-10-16",
-                    "temporal": "2023-10-01/2023-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/df9b9c6e-9b8a-4c4d-993c-bc9541d72a49",
+                    "temporal": "2023-10-01/2023-12-31",
+                    "title": "Hospice Enrollments : 2023-10-02"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/85103729-a6b5-460d-93f7-20cd055a74d1/Hospice_Enrollments_2023.07.06.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/aa3df2b4-67e8-4c1b-a4dd-f35db8ece0fd",
-                    "title": "Hospice Enrollments : 2023-07-17",
                     "modified": "2023-07-17",
-                    "temporal": "2023-07-01/2023-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/aa3df2b4-67e8-4c1b-a4dd-f35db8ece0fd",
+                    "temporal": "2023-07-01/2023-09-30",
+                    "title": "Hospice Enrollments : 2023-07-17"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/aa3df2b4-67e8-4c1b-a4dd-f35db8ece0fd/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/aa3df2b4-67e8-4c1b-a4dd-f35db8ece0fd",
-                    "title": "Hospice Enrollments : 2023-07-17",
+                    "format": "API",
                     "modified": "2023-07-17",
-                    "temporal": "2023-07-01/2023-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/aa3df2b4-67e8-4c1b-a4dd-f35db8ece0fd",
+                    "temporal": "2023-07-01/2023-09-30",
+                    "title": "Hospice Enrollments : 2023-07-17"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/f8b05c50-76a4-4501-878e-a65fa9321f20/Hospice_Enrollments_2023.03.31.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/94c94f93-0ab8-4c23-889f-7162587bc9ee",
-                    "title": "Hospice Enrollments : 2023-04-01",
                     "modified": "2023-04-19",
-                    "temporal": "2023-04-01/2023-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/94c94f93-0ab8-4c23-889f-7162587bc9ee",
+                    "temporal": "2023-04-01/2023-06-30",
+                    "title": "Hospice Enrollments : 2023-04-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/94c94f93-0ab8-4c23-889f-7162587bc9ee/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/94c94f93-0ab8-4c23-889f-7162587bc9ee",
-                    "title": "Hospice Enrollments : 2023-04-01",
+                    "format": "API",
                     "modified": "2023-04-19",
-                    "temporal": "2023-04-01/2023-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/94c94f93-0ab8-4c23-889f-7162587bc9ee",
+                    "temporal": "2023-04-01/2023-06-30",
+                    "title": "Hospice Enrollments : 2023-04-01"
                 }
             ],
             "identifier": "https://data.cms.gov/data-api/v1/dataset/25704213-e833-4b8b-9dbc-58dd17149209/data-viewer",
@@ -9785,488 +9784,488 @@
                 "fn": "Provider Enrollment Data Requests - CPI",
                 "hasEmail": "mailto:ProviderEnrollmentDataRequests@cms.hhs.gov"
             },
+            "dataQuality": true,
             "describedBy": "https://data.cms.gov/sites/default/files/2024-10/Hospital_All_Owners_Data_Dictionary.pdf",
             "describedByType": "application/pdf",
-            "dataQuality": true,
             "description": "The Hospital All Owners Information dataset provides information on all owners of the hospitals. This data includes ownership information such as ownership name, ownership type, ownership address and ownership effective date.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/029c119f-f79c-49be-9100-344d31d10344/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/029c119f-f79c-49be-9100-344d31d10344",
                     "description": "latest",
-                    "title": "Hospital All Owners : 2025-01-01",
+                    "format": "API",
                     "modified": "2025-01-15",
-                    "temporal": "2025-01-01/2025-01-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/029c119f-f79c-49be-9100-344d31d10344",
+                    "temporal": "2025-01-01/2025-01-31",
+                    "title": "Hospital All Owners : 2025-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/d20ffa23-37f1-40ca-8ecd-03413f021acb/Hospital_All_Owners_2025.01.02.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6d33e473-6f4d-47cc-b76c-d79035f2cc47",
-                    "title": "Hospital All Owners : 2025-01-01",
                     "modified": "2025-01-15",
-                    "temporal": "2025-01-01/2025-01-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6d33e473-6f4d-47cc-b76c-d79035f2cc47",
+                    "temporal": "2025-01-01/2025-01-31",
+                    "title": "Hospital All Owners : 2025-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/6d33e473-6f4d-47cc-b76c-d79035f2cc47/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6d33e473-6f4d-47cc-b76c-d79035f2cc47",
-                    "title": "Hospital All Owners : 2025-01-01",
+                    "format": "API",
                     "modified": "2025-01-15",
-                    "temporal": "2025-01-01/2025-01-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6d33e473-6f4d-47cc-b76c-d79035f2cc47",
+                    "temporal": "2025-01-01/2025-01-31",
+                    "title": "Hospital All Owners : 2025-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/657b9373-e15b-4383-93a4-b68298007ef5/Hospital_All_Owners_2024.12.05.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/25d5589e-5539-4683-a06b-0b3c477a6133",
-                    "title": "Hospital All Owners : 2024-12-01",
                     "modified": "2024-12-16",
-                    "temporal": "2024-12-01/2024-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/25d5589e-5539-4683-a06b-0b3c477a6133",
+                    "temporal": "2024-12-01/2024-12-31",
+                    "title": "Hospital All Owners : 2024-12-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/25d5589e-5539-4683-a06b-0b3c477a6133/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/25d5589e-5539-4683-a06b-0b3c477a6133",
-                    "title": "Hospital All Owners : 2024-12-01",
+                    "format": "API",
                     "modified": "2024-12-16",
-                    "temporal": "2024-12-01/2024-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/25d5589e-5539-4683-a06b-0b3c477a6133",
+                    "temporal": "2024-12-01/2024-12-31",
+                    "title": "Hospital All Owners : 2024-12-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/75977bac-7588-41f1-9bbc-909108ef562d/Hospital_All_Owners_2024.11.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9cb92c29-9a6e-4ce7-b96d-45ab86563604",
-                    "title": "Hospital All Owners : 2024-11-01",
                     "modified": "2024-11-15",
-                    "temporal": "2024-11-01/2024-11-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9cb92c29-9a6e-4ce7-b96d-45ab86563604",
+                    "temporal": "2024-11-01/2024-11-30",
+                    "title": "Hospital All Owners : 2024-11-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/9cb92c29-9a6e-4ce7-b96d-45ab86563604/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9cb92c29-9a6e-4ce7-b96d-45ab86563604",
-                    "title": "Hospital All Owners : 2024-11-01",
+                    "format": "API",
                     "modified": "2024-11-15",
-                    "temporal": "2024-11-01/2024-11-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9cb92c29-9a6e-4ce7-b96d-45ab86563604",
+                    "temporal": "2024-11-01/2024-11-30",
+                    "title": "Hospital All Owners : 2024-11-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/6f616566-ca0d-4040-a637-f5865b8b4dbd/Hospital_All_Owners_2024.10.07.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a94b75bf-6c84-4b9f-9de7-8a15cb694359",
-                    "title": "Hospital All Owners : 2024-10-01",
                     "modified": "2024-10-15",
-                    "temporal": "2024-10-01/2024-10-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a94b75bf-6c84-4b9f-9de7-8a15cb694359",
+                    "temporal": "2024-10-01/2024-10-31",
+                    "title": "Hospital All Owners : 2024-10-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/a94b75bf-6c84-4b9f-9de7-8a15cb694359/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a94b75bf-6c84-4b9f-9de7-8a15cb694359",
-                    "title": "Hospital All Owners : 2024-10-01",
+                    "format": "API",
                     "modified": "2024-10-15",
-                    "temporal": "2024-10-01/2024-10-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/a94b75bf-6c84-4b9f-9de7-8a15cb694359",
+                    "temporal": "2024-10-01/2024-10-31",
+                    "title": "Hospital All Owners : 2024-10-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/bd673689-d3ea-4047-9661-47d1a4e8a74c/Hospital_All_Owners_2024.09.02.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2537547b-05af-4f7d-bc39-f9c1d4e9ea85",
-                    "title": "Hospital All Owners : 2024-09-01",
                     "modified": "2024-09-16",
-                    "temporal": "2024-09-01/2024-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2537547b-05af-4f7d-bc39-f9c1d4e9ea85",
+                    "temporal": "2024-09-01/2024-09-30",
+                    "title": "Hospital All Owners : 2024-09-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/2537547b-05af-4f7d-bc39-f9c1d4e9ea85/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2537547b-05af-4f7d-bc39-f9c1d4e9ea85",
-                    "title": "Hospital All Owners : 2024-09-01",
+                    "format": "API",
                     "modified": "2024-09-16",
-                    "temporal": "2024-09-01/2024-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2537547b-05af-4f7d-bc39-f9c1d4e9ea85",
+                    "temporal": "2024-09-01/2024-09-30",
+                    "title": "Hospital All Owners : 2024-09-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/83383a16-2754-45af-9eb7-437b89a29b14/Hospital_All_Owners_2024.08.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b677d60b-12fe-464b-8f0d-c6ae6ae7e37f",
-                    "title": "Hospital All Owners : 2024-08-01",
                     "modified": "2024-08-15",
-                    "temporal": "2024-08-01/2024-08-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b677d60b-12fe-464b-8f0d-c6ae6ae7e37f",
+                    "temporal": "2024-08-01/2024-08-31",
+                    "title": "Hospital All Owners : 2024-08-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/b677d60b-12fe-464b-8f0d-c6ae6ae7e37f/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b677d60b-12fe-464b-8f0d-c6ae6ae7e37f",
-                    "title": "Hospital All Owners : 2024-08-01",
+                    "format": "API",
                     "modified": "2024-08-15",
-                    "temporal": "2024-08-01/2024-08-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/b677d60b-12fe-464b-8f0d-c6ae6ae7e37f",
+                    "temporal": "2024-08-01/2024-08-31",
+                    "title": "Hospital All Owners : 2024-08-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/541283b8-3bb5-474f-a9e9-ee6fe66e749c/Hospital_All_Owners_2024.07.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ae5c92dd-3d5e-446c-9092-6644da7cb94e",
-                    "title": "Hospital All Owners : 2024-07-01",
                     "modified": "2024-07-15",
-                    "temporal": "2024-07-01/2024-07-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ae5c92dd-3d5e-446c-9092-6644da7cb94e",
+                    "temporal": "2024-07-01/2024-07-31",
+                    "title": "Hospital All Owners : 2024-07-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/ae5c92dd-3d5e-446c-9092-6644da7cb94e/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ae5c92dd-3d5e-446c-9092-6644da7cb94e",
-                    "title": "Hospital All Owners : 2024-07-01",
+                    "format": "API",
                     "modified": "2024-07-15",
-                    "temporal": "2024-07-01/2024-07-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ae5c92dd-3d5e-446c-9092-6644da7cb94e",
+                    "temporal": "2024-07-01/2024-07-31",
+                    "title": "Hospital All Owners : 2024-07-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/609f0676-3bbb-42fb-af1f-ae29be0a02b7/Hospital_All_Owners_2024.06.03.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3f495a07-3c06-4073-9eb9-1ed3623899a7",
-                    "title": "Hospital All Owners : 2024-06-03",
                     "modified": "2024-06-14",
-                    "temporal": "2024-06-01/2024-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3f495a07-3c06-4073-9eb9-1ed3623899a7",
+                    "temporal": "2024-06-01/2024-06-30",
+                    "title": "Hospital All Owners : 2024-06-03"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/3f495a07-3c06-4073-9eb9-1ed3623899a7/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3f495a07-3c06-4073-9eb9-1ed3623899a7",
-                    "title": "Hospital All Owners : 2024-06-03",
+                    "format": "API",
                     "modified": "2024-06-14",
-                    "temporal": "2024-06-01/2024-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3f495a07-3c06-4073-9eb9-1ed3623899a7",
+                    "temporal": "2024-06-01/2024-06-30",
+                    "title": "Hospital All Owners : 2024-06-03"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/8b98944e-a10c-4cb2-a193-5e230bb2f7a1/Hospital_All_Owners_2024.05.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e3271c0a-d7b3-444f-99a8-a854c34eba34",
-                    "title": "Hospital All Owners : 2024-05-01",
                     "modified": "2024-05-15",
-                    "temporal": "2024-05-01/2024-05-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e3271c0a-d7b3-444f-99a8-a854c34eba34",
+                    "temporal": "2024-05-01/2024-05-31",
+                    "title": "Hospital All Owners : 2024-05-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/e3271c0a-d7b3-444f-99a8-a854c34eba34/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e3271c0a-d7b3-444f-99a8-a854c34eba34",
-                    "title": "Hospital All Owners : 2024-05-01",
+                    "format": "API",
                     "modified": "2024-05-15",
-                    "temporal": "2024-05-01/2024-05-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e3271c0a-d7b3-444f-99a8-a854c34eba34",
+                    "temporal": "2024-05-01/2024-05-31",
+                    "title": "Hospital All Owners : 2024-05-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/cf2d94e2-e045-417e-99b9-ce87df631374/Hospital_All_Owners_2024.04.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/90ef425f-1a3b-4035-972f-d40381390375",
-                    "title": "Hospital All Owners : 2024-04-01",
                     "modified": "2024-04-15",
-                    "temporal": "2024-04-01/2024-04-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/90ef425f-1a3b-4035-972f-d40381390375",
+                    "temporal": "2024-04-01/2024-04-30",
+                    "title": "Hospital All Owners : 2024-04-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/90ef425f-1a3b-4035-972f-d40381390375/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/90ef425f-1a3b-4035-972f-d40381390375",
-                    "title": "Hospital All Owners : 2024-04-01",
+                    "format": "API",
                     "modified": "2024-04-15",
-                    "temporal": "2024-04-01/2024-04-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/90ef425f-1a3b-4035-972f-d40381390375",
+                    "temporal": "2024-04-01/2024-04-30",
+                    "title": "Hospital All Owners : 2024-04-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/892ea691-d3db-4322-a807-6db43723bbf4/Hospital_All_Owners_2024.03.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/22113cff-cfa1-4974-bcb6-67be29cde318",
-                    "title": "Hospital All Owners : 2024-03-01",
                     "modified": "2024-03-15",
-                    "temporal": "2024-03-01/2024-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/22113cff-cfa1-4974-bcb6-67be29cde318",
+                    "temporal": "2024-03-01/2024-03-31",
+                    "title": "Hospital All Owners : 2024-03-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/22113cff-cfa1-4974-bcb6-67be29cde318/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/22113cff-cfa1-4974-bcb6-67be29cde318",
-                    "title": "Hospital All Owners : 2024-03-01",
+                    "format": "API",
                     "modified": "2024-03-15",
-                    "temporal": "2024-03-01/2024-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/22113cff-cfa1-4974-bcb6-67be29cde318",
+                    "temporal": "2024-03-01/2024-03-31",
+                    "title": "Hospital All Owners : 2024-03-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/2b7a5a3c-ed29-4be4-b029-5713608d8f06/Hospital_All_Owners_2024.02.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e4a93e23-bb34-4852-a3b8-2b3f2077a4e2",
-                    "title": "Hospital All Owners : 2024-02-01",
                     "modified": "2024-02-15",
-                    "temporal": "2024-02-01/2024-02-29"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e4a93e23-bb34-4852-a3b8-2b3f2077a4e2",
+                    "temporal": "2024-02-01/2024-02-29",
+                    "title": "Hospital All Owners : 2024-02-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/e4a93e23-bb34-4852-a3b8-2b3f2077a4e2/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e4a93e23-bb34-4852-a3b8-2b3f2077a4e2",
-                    "title": "Hospital All Owners : 2024-02-01",
+                    "format": "API",
                     "modified": "2024-02-15",
-                    "temporal": "2024-02-01/2024-02-29"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/e4a93e23-bb34-4852-a3b8-2b3f2077a4e2",
+                    "temporal": "2024-02-01/2024-02-29",
+                    "title": "Hospital All Owners : 2024-02-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/b9ad5a39-98f4-4070-b790-a64f317d8f8b/Hospital_All_Owners_2024.01.05.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/28b046c1-0153-4682-8dec-270240779ced",
-                    "title": "Hospital All Owners : 2024-01-05",
                     "modified": "2024-01-17",
-                    "temporal": "2024-01-01/2024-01-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/28b046c1-0153-4682-8dec-270240779ced",
+                    "temporal": "2024-01-01/2024-01-31",
+                    "title": "Hospital All Owners : 2024-01-05"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/28b046c1-0153-4682-8dec-270240779ced/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/28b046c1-0153-4682-8dec-270240779ced",
-                    "title": "Hospital All Owners : 2024-01-05",
+                    "format": "API",
                     "modified": "2024-01-17",
-                    "temporal": "2024-01-01/2024-01-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/28b046c1-0153-4682-8dec-270240779ced",
+                    "temporal": "2024-01-01/2024-01-31",
+                    "title": "Hospital All Owners : 2024-01-05"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/d068d21c-7540-4271-bbbc-ae7f396b0570/Hospital_All_Owners_2023.12.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f5646e6d-78ca-4553-a842-a7d1e0573869",
-                    "title": "Hospital All Owners : 2023-12-01",
                     "modified": "2023-12-15",
-                    "temporal": "2023-12-01/2023-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f5646e6d-78ca-4553-a842-a7d1e0573869",
+                    "temporal": "2023-12-01/2023-12-31",
+                    "title": "Hospital All Owners : 2023-12-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/f5646e6d-78ca-4553-a842-a7d1e0573869/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f5646e6d-78ca-4553-a842-a7d1e0573869",
-                    "title": "Hospital All Owners : 2023-12-01",
+                    "format": "API",
                     "modified": "2023-12-15",
-                    "temporal": "2023-12-01/2023-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/f5646e6d-78ca-4553-a842-a7d1e0573869",
+                    "temporal": "2023-12-01/2023-12-31",
+                    "title": "Hospital All Owners : 2023-12-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/d83d03f7-b524-411e-ad9f-3992155a886f/Hospital_All_Owners_2023.11.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/419c8fdc-9ccc-4db1-8e3f-d37abdc96d59",
-                    "title": "Hospital All Owners : 2023-11-01",
                     "modified": "2023-11-15",
-                    "temporal": "2023-11-01/2023-11-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/419c8fdc-9ccc-4db1-8e3f-d37abdc96d59",
+                    "temporal": "2023-11-01/2023-11-30",
+                    "title": "Hospital All Owners : 2023-11-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/419c8fdc-9ccc-4db1-8e3f-d37abdc96d59/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/419c8fdc-9ccc-4db1-8e3f-d37abdc96d59",
-                    "title": "Hospital All Owners : 2023-11-01",
+                    "format": "API",
                     "modified": "2023-11-15",
-                    "temporal": "2023-11-01/2023-11-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/419c8fdc-9ccc-4db1-8e3f-d37abdc96d59",
+                    "temporal": "2023-11-01/2023-11-30",
+                    "title": "Hospital All Owners : 2023-11-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/960f6d1a-c84e-4ba4-ba42-89342af06661/Hospital_All_Owners_2023.10.02.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/133656c6-7654-4b32-8ae1-1779cbe0073c",
-                    "title": "Hospital All Owners : 2023-10-02",
                     "modified": "2023-10-16",
-                    "temporal": "2023-10-01/2023-10-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/133656c6-7654-4b32-8ae1-1779cbe0073c",
+                    "temporal": "2023-10-01/2023-10-31",
+                    "title": "Hospital All Owners : 2023-10-02"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/133656c6-7654-4b32-8ae1-1779cbe0073c/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/133656c6-7654-4b32-8ae1-1779cbe0073c",
-                    "title": "Hospital All Owners : 2023-10-02",
+                    "format": "API",
                     "modified": "2023-10-16",
-                    "temporal": "2023-10-01/2023-10-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/133656c6-7654-4b32-8ae1-1779cbe0073c",
+                    "temporal": "2023-10-01/2023-10-31",
+                    "title": "Hospital All Owners : 2023-10-02"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/0f490a5d-9ebd-4a5b-8ef7-c9c197d79367/Hospital_All_Owners_2023.09.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/52f957f7-aca1-4287-85c8-033d2996c3c8",
-                    "title": "Hospital All Owners : 2023-09-15",
                     "modified": "2023-09-28",
-                    "temporal": "2023-09-01/2023-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/52f957f7-aca1-4287-85c8-033d2996c3c8",
+                    "temporal": "2023-09-01/2023-09-30",
+                    "title": "Hospital All Owners : 2023-09-15"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/52f957f7-aca1-4287-85c8-033d2996c3c8/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/52f957f7-aca1-4287-85c8-033d2996c3c8",
-                    "title": "Hospital All Owners : 2023-09-15",
+                    "format": "API",
                     "modified": "2023-09-28",
-                    "temporal": "2023-09-01/2023-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/52f957f7-aca1-4287-85c8-033d2996c3c8",
+                    "temporal": "2023-09-01/2023-09-30",
+                    "title": "Hospital All Owners : 2023-09-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/1a622b1f-d58f-46b9-87e6-2b523f9af112/Hospital_All_Owners_2023.08.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/cf0de111-a036-4571-a43f-d90171c29435",
-                    "title": "Hospital All Owners : 2023-08-01",
                     "modified": "2023-08-15",
-                    "temporal": "2023-08-01/2023-08-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/cf0de111-a036-4571-a43f-d90171c29435",
+                    "temporal": "2023-08-01/2023-08-31",
+                    "title": "Hospital All Owners : 2023-08-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/cf0de111-a036-4571-a43f-d90171c29435/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/cf0de111-a036-4571-a43f-d90171c29435",
-                    "title": "Hospital All Owners : 2023-08-01",
+                    "format": "API",
                     "modified": "2023-08-15",
-                    "temporal": "2023-08-01/2023-08-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/cf0de111-a036-4571-a43f-d90171c29435",
+                    "temporal": "2023-08-01/2023-08-31",
+                    "title": "Hospital All Owners : 2023-08-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/699e6f31-2508-4e9c-ba56-a08a30da2859/Hospital_All_Owners_2023.07.06.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/03e2c61e-74e7-42e4-aa35-0f975b69efa5",
-                    "title": "Hospital All Owners : 2023-07-17",
                     "modified": "2023-07-17",
-                    "temporal": "2023-07-01/2023-07-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/03e2c61e-74e7-42e4-aa35-0f975b69efa5",
+                    "temporal": "2023-07-01/2023-07-31",
+                    "title": "Hospital All Owners : 2023-07-17"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/03e2c61e-74e7-42e4-aa35-0f975b69efa5/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/03e2c61e-74e7-42e4-aa35-0f975b69efa5",
-                    "title": "Hospital All Owners : 2023-07-17",
+                    "format": "API",
                     "modified": "2023-07-17",
-                    "temporal": "2023-07-01/2023-07-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/03e2c61e-74e7-42e4-aa35-0f975b69efa5",
+                    "temporal": "2023-07-01/2023-07-31",
+                    "title": "Hospital All Owners : 2023-07-17"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/5fffdd16-db09-4384-88ff-7c3bd62477fb/Hospital_All_Owners_2023.06.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/03811b6e-2808-457a-be0a-81f704f10b27",
-                    "title": "Hospital All Owners : 2023-06-15",
                     "modified": "2023-06-15",
-                    "temporal": "2023-06-01/2023-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/03811b6e-2808-457a-be0a-81f704f10b27",
+                    "temporal": "2023-06-01/2023-06-30",
+                    "title": "Hospital All Owners : 2023-06-15"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/03811b6e-2808-457a-be0a-81f704f10b27/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/03811b6e-2808-457a-be0a-81f704f10b27",
-                    "title": "Hospital All Owners : 2023-06-15",
+                    "format": "API",
                     "modified": "2023-06-15",
-                    "temporal": "2023-06-01/2023-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/03811b6e-2808-457a-be0a-81f704f10b27",
+                    "temporal": "2023-06-01/2023-06-30",
+                    "title": "Hospital All Owners : 2023-06-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/17197f79-951b-4de1-9ec8-abf6df0b1ee3/Hospital_All_Owners_2023.05.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d4ec5de6-b917-4f91-9d81-618ca54a82df",
-                    "title": "Hospital All Owners : 2023-05-01",
                     "modified": "2023-05-15",
-                    "temporal": "2023-05-01/2023-05-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d4ec5de6-b917-4f91-9d81-618ca54a82df",
+                    "temporal": "2023-05-01/2023-05-31",
+                    "title": "Hospital All Owners : 2023-05-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/d4ec5de6-b917-4f91-9d81-618ca54a82df/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d4ec5de6-b917-4f91-9d81-618ca54a82df",
-                    "title": "Hospital All Owners : 2023-05-01",
+                    "format": "API",
                     "modified": "2023-05-15",
-                    "temporal": "2023-05-01/2023-05-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d4ec5de6-b917-4f91-9d81-618ca54a82df",
+                    "temporal": "2023-05-01/2023-05-31",
+                    "title": "Hospital All Owners : 2023-05-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/65a9e5b4-e155-4530-9b7b-9f3ec19783aa/Hospital_All_Owners_2023.03.31.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/809d5848-26e3-4909-b96a-29cf33e74b36",
-                    "title": "Hospital All Owners : 2023-04-14",
                     "modified": "2023-04-18",
-                    "temporal": "2023-04-01/2023-04-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/809d5848-26e3-4909-b96a-29cf33e74b36",
+                    "temporal": "2023-04-01/2023-04-30",
+                    "title": "Hospital All Owners : 2023-04-14"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/809d5848-26e3-4909-b96a-29cf33e74b36/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/809d5848-26e3-4909-b96a-29cf33e74b36",
-                    "title": "Hospital All Owners : 2023-04-14",
+                    "format": "API",
                     "modified": "2023-04-18",
-                    "temporal": "2023-04-01/2023-04-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/809d5848-26e3-4909-b96a-29cf33e74b36",
+                    "temporal": "2023-04-01/2023-04-30",
+                    "title": "Hospital All Owners : 2023-04-14"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-03/c1cc6df4-aa1b-4f92-95a2-3313f881688b/Hospital_All_Owners_2023.03.10.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/42919067-8b0d-47bc-8fba-5dc9f79c634a",
-                    "title": "Hospital All Owners : 2023-03-15",
                     "modified": "2023-03-15",
-                    "temporal": "2023-03-01/2023-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/42919067-8b0d-47bc-8fba-5dc9f79c634a",
+                    "temporal": "2023-03-01/2023-03-31",
+                    "title": "Hospital All Owners : 2023-03-15"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/42919067-8b0d-47bc-8fba-5dc9f79c634a/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/42919067-8b0d-47bc-8fba-5dc9f79c634a",
-                    "title": "Hospital All Owners : 2023-03-15",
+                    "format": "API",
                     "modified": "2023-03-15",
-                    "temporal": "2023-03-01/2023-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/42919067-8b0d-47bc-8fba-5dc9f79c634a",
+                    "temporal": "2023-03-01/2023-03-31",
+                    "title": "Hospital All Owners : 2023-03-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-02/fce414c2-19ce-4a52-b18d-cd65118535b8/Hospital_All_Owners_2023.02.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/16043ada-7359-4146-b3ef-1902b7db0be8",
-                    "title": "Hospital All Owners : 2023-02-15",
                     "modified": "2023-03-06",
-                    "temporal": "2023-02-01/2023-02-28"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/16043ada-7359-4146-b3ef-1902b7db0be8",
+                    "temporal": "2023-02-01/2023-02-28",
+                    "title": "Hospital All Owners : 2023-02-15"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/16043ada-7359-4146-b3ef-1902b7db0be8/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/16043ada-7359-4146-b3ef-1902b7db0be8",
-                    "title": "Hospital All Owners : 2023-02-15",
+                    "format": "API",
                     "modified": "2023-03-06",
-                    "temporal": "2023-02-01/2023-02-28"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/16043ada-7359-4146-b3ef-1902b7db0be8",
+                    "temporal": "2023-02-01/2023-02-28",
+                    "title": "Hospital All Owners : 2023-02-15"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-01/b8ac932d-60c2-49ae-a338-3a3130fc9eeb/Hospital_All_Owners_2022.12.30.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/77849457-608d-4718-acb8-52a8e5e5cb4a",
-                    "title": "Hospital All Owners : 2023-01-01",
                     "modified": "2023-03-06",
-                    "temporal": "2023-01-01/2023-01-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/77849457-608d-4718-acb8-52a8e5e5cb4a",
+                    "temporal": "2023-01-01/2023-01-31",
+                    "title": "Hospital All Owners : 2023-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/77849457-608d-4718-acb8-52a8e5e5cb4a/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/77849457-608d-4718-acb8-52a8e5e5cb4a",
-                    "title": "Hospital All Owners : 2023-01-01",
+                    "format": "API",
                     "modified": "2023-03-06",
-                    "temporal": "2023-01-01/2023-01-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/77849457-608d-4718-acb8-52a8e5e5cb4a",
+                    "temporal": "2023-01-01/2023-01-31",
+                    "title": "Hospital All Owners : 2023-01-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-12/8adc6478-03b9-4f5c-bb53-96579cef2265/Hospital_All_Owners.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/dd7f766d-1a95-4286-bbd4-6421726b9a77",
-                    "title": "Hospital All Owners : 2022-11-13",
                     "modified": "2023-03-06",
-                    "temporal": "2022-11-01/2022-11-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/dd7f766d-1a95-4286-bbd4-6421726b9a77",
+                    "temporal": "2022-11-01/2022-11-30",
+                    "title": "Hospital All Owners : 2022-11-13"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/dd7f766d-1a95-4286-bbd4-6421726b9a77/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/dd7f766d-1a95-4286-bbd4-6421726b9a77",
-                    "title": "Hospital All Owners : 2022-11-13",
+                    "format": "API",
                     "modified": "2023-03-06",
-                    "temporal": "2022-11-01/2022-11-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/dd7f766d-1a95-4286-bbd4-6421726b9a77",
+                    "temporal": "2022-11-01/2022-11-30",
+                    "title": "Hospital All Owners : 2022-11-13"
                 }
             ],
             "identifier": "https://data.cms.gov/data-api/v1/dataset/029c119f-f79c-49be-9100-344d31d10344/data-viewer",
@@ -10311,236 +10310,236 @@
                 "fn": "Provider Enrollment Data Requests - CPI",
                 "hasEmail": "mailto:ProviderEnrollmentDataRequests@cms.hhs.gov"
             },
+            "dataQuality": true,
             "describedBy": "https://data.cms.gov/sites/default/files/2023-01/Hospital_CHOW_Data_Dictionary_2022.12.30.pdf",
             "describedByType": "application/pdf",
-            "dataQuality": true,
             "description": "The Hospital Change of Ownership (CHOW) dataset provides information on the hospital ownership changes that occurred on or after January 1, 2016. This data includes information on the buyer and seller organization\u2019s legal business name, provider type, change of ownership type (CHOW, Acquisition/Merger, or Consolidation) and the effective date of the change.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/c04031db-54ce-461c-85d1-d2613d71f167/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c04031db-54ce-461c-85d1-d2613d71f167",
                     "description": "latest",
-                    "title": "Hospital Change of Ownership : 2024-12-01",
+                    "format": "API",
                     "modified": "2025-01-15",
-                    "temporal": "2024-10-01/2024-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c04031db-54ce-461c-85d1-d2613d71f167",
+                    "temporal": "2024-10-01/2024-12-31",
+                    "title": "Hospital Change of Ownership : 2024-12-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/2e9ddac3-eb7e-4805-a3e0-9c52152af37a/Hospital_CHOW_2025.01.02.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/852a0391-86e0-4470-a56a-6b259984171c",
-                    "title": "Hospital Change of Ownership : 2024-12-01",
                     "modified": "2025-01-15",
-                    "temporal": "2024-10-01/2024-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/852a0391-86e0-4470-a56a-6b259984171c",
+                    "temporal": "2024-10-01/2024-12-31",
+                    "title": "Hospital Change of Ownership : 2024-12-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/852a0391-86e0-4470-a56a-6b259984171c/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/852a0391-86e0-4470-a56a-6b259984171c",
-                    "title": "Hospital Change of Ownership : 2024-12-01",
+                    "format": "API",
                     "modified": "2025-01-15",
-                    "temporal": "2024-10-01/2024-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/852a0391-86e0-4470-a56a-6b259984171c",
+                    "temporal": "2024-10-01/2024-12-31",
+                    "title": "Hospital Change of Ownership : 2024-12-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/e071c47e-8026-4f4d-a8fe-f254132d056c/Hospital_CHOW_2024.10.07.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c409dfea-0f37-41ff-b846-1e1435fcc0ff",
-                    "title": "Hospital Change of Ownership : 2024-09-01",
                     "modified": "2024-10-15",
-                    "temporal": "2024-07-01/2024-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c409dfea-0f37-41ff-b846-1e1435fcc0ff",
+                    "temporal": "2024-07-01/2024-09-30",
+                    "title": "Hospital Change of Ownership : 2024-09-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/c409dfea-0f37-41ff-b846-1e1435fcc0ff/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c409dfea-0f37-41ff-b846-1e1435fcc0ff",
-                    "title": "Hospital Change of Ownership : 2024-09-01",
+                    "format": "API",
                     "modified": "2024-10-15",
-                    "temporal": "2024-07-01/2024-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/c409dfea-0f37-41ff-b846-1e1435fcc0ff",
+                    "temporal": "2024-07-01/2024-09-30",
+                    "title": "Hospital Change of Ownership : 2024-09-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/e5c6a41d-8304-4043-ad0a-f5e5f2605649/Hospital_CHOW_2024.07.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/919e2896-182d-4e6c-9bb5-2e6f85de5fdf",
-                    "title": "Hospital Change of Ownership : 2024-06-01",
                     "modified": "2024-07-15",
-                    "temporal": "2024-04-01/2024-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/919e2896-182d-4e6c-9bb5-2e6f85de5fdf",
+                    "temporal": "2024-04-01/2024-06-30",
+                    "title": "Hospital Change of Ownership : 2024-06-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/919e2896-182d-4e6c-9bb5-2e6f85de5fdf/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/919e2896-182d-4e6c-9bb5-2e6f85de5fdf",
-                    "title": "Hospital Change of Ownership : 2024-06-01",
+                    "format": "API",
                     "modified": "2024-07-15",
-                    "temporal": "2024-04-01/2024-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/919e2896-182d-4e6c-9bb5-2e6f85de5fdf",
+                    "temporal": "2024-04-01/2024-06-30",
+                    "title": "Hospital Change of Ownership : 2024-06-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/942b0c0e-5560-4831-98cd-89433db6584c/Hospital_CHOW_2024.04.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3cba80db-046a-40b0-944d-22528595dcfe",
-                    "title": "Hospital Change of Ownership : 2024-03-31",
                     "modified": "2024-04-15",
-                    "temporal": "2024-01-01/2024-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3cba80db-046a-40b0-944d-22528595dcfe",
+                    "temporal": "2024-01-01/2024-03-31",
+                    "title": "Hospital Change of Ownership : 2024-03-31"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/3cba80db-046a-40b0-944d-22528595dcfe/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3cba80db-046a-40b0-944d-22528595dcfe",
-                    "title": "Hospital Change of Ownership : 2024-03-31",
+                    "format": "API",
                     "modified": "2024-04-15",
-                    "temporal": "2024-01-01/2024-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/3cba80db-046a-40b0-944d-22528595dcfe",
+                    "temporal": "2024-01-01/2024-03-31",
+                    "title": "Hospital Change of Ownership : 2024-03-31"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/df7d9aa1-19ef-4220-b962-9cf230d2e0af/Hospital_CHOW_2024.01.05.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/278595ef-6f5b-4d37-9b50-8d7acd4bfa25",
-                    "title": "Hospital Change of Ownership : 2023-12-31",
                     "modified": "2024-01-17",
-                    "temporal": "2023-10-01/2023-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/278595ef-6f5b-4d37-9b50-8d7acd4bfa25",
+                    "temporal": "2023-10-01/2023-12-31",
+                    "title": "Hospital Change of Ownership : 2023-12-31"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/278595ef-6f5b-4d37-9b50-8d7acd4bfa25/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/278595ef-6f5b-4d37-9b50-8d7acd4bfa25",
-                    "title": "Hospital Change of Ownership : 2023-12-31",
+                    "format": "API",
                     "modified": "2024-01-17",
-                    "temporal": "2023-10-01/2023-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/278595ef-6f5b-4d37-9b50-8d7acd4bfa25",
+                    "temporal": "2023-10-01/2023-12-31",
+                    "title": "Hospital Change of Ownership : 2023-12-31"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/ad61f629-1981-4320-b6ee-82326db365db/Hospital_CHOW_2023.10.02.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7c76c201-98c6-4840-ac0d-58a4b31043c5",
-                    "title": "Hospital Change of Ownership : 2023-09-30",
                     "modified": "2023-10-16",
-                    "temporal": "2023-07-01/2023-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7c76c201-98c6-4840-ac0d-58a4b31043c5",
+                    "temporal": "2023-07-01/2023-09-30",
+                    "title": "Hospital Change of Ownership : 2023-09-30"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/7c76c201-98c6-4840-ac0d-58a4b31043c5/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7c76c201-98c6-4840-ac0d-58a4b31043c5",
-                    "title": "Hospital Change of Ownership : 2023-09-30",
+                    "format": "API",
                     "modified": "2023-10-16",
-                    "temporal": "2023-07-01/2023-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/7c76c201-98c6-4840-ac0d-58a4b31043c5",
+                    "temporal": "2023-07-01/2023-09-30",
+                    "title": "Hospital Change of Ownership : 2023-09-30"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/626b4774-b9a3-4b1e-81c7-72cf3c67bf2d/Hospital_CHOW_2023.07.06.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/aa821455-086f-40e4-836e-9fd30a95cb67",
-                    "title": "Hospital Change of Ownership : 2023-06-30",
                     "modified": "2023-07-17",
-                    "temporal": "2023-04-01/2023-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/aa821455-086f-40e4-836e-9fd30a95cb67",
+                    "temporal": "2023-04-01/2023-06-30",
+                    "title": "Hospital Change of Ownership : 2023-06-30"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/aa821455-086f-40e4-836e-9fd30a95cb67/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/aa821455-086f-40e4-836e-9fd30a95cb67",
-                    "title": "Hospital Change of Ownership : 2023-06-30",
+                    "format": "API",
                     "modified": "2023-07-17",
-                    "temporal": "2023-04-01/2023-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/aa821455-086f-40e4-836e-9fd30a95cb67",
+                    "temporal": "2023-04-01/2023-06-30",
+                    "title": "Hospital Change of Ownership : 2023-06-30"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/8bc00c59-f2ed-41cb-8405-5ffc9dd20305/Hospital_CHOW_2023.03.31.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0825fbbd-c57b-4722-bb4d-655c50236be2",
-                    "title": "Hospital Change of Ownership : 2023-03-31",
                     "modified": "2023-04-25",
-                    "temporal": "2023-01-01/2023-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0825fbbd-c57b-4722-bb4d-655c50236be2",
+                    "temporal": "2023-01-01/2023-03-31",
+                    "title": "Hospital Change of Ownership : 2023-03-31"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/0825fbbd-c57b-4722-bb4d-655c50236be2/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0825fbbd-c57b-4722-bb4d-655c50236be2",
-                    "title": "Hospital Change of Ownership : 2023-03-31",
+                    "format": "API",
                     "modified": "2023-04-25",
-                    "temporal": "2023-01-01/2023-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/0825fbbd-c57b-4722-bb4d-655c50236be2",
+                    "temporal": "2023-01-01/2023-03-31",
+                    "title": "Hospital Change of Ownership : 2023-03-31"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2023-01/71b731a2-d327-49d5-9229-c3b050024414/Hospital_CHOW_2022.12.30.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6748a5be-cfe1-4b2c-8b46-ab1322c6364c",
-                    "title": "Hospital Change of Ownership : 2022-12-30",
                     "modified": "2023-03-06",
-                    "temporal": "2022-10-01/2022-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6748a5be-cfe1-4b2c-8b46-ab1322c6364c",
+                    "temporal": "2022-10-01/2022-12-31",
+                    "title": "Hospital Change of Ownership : 2022-12-30"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/6748a5be-cfe1-4b2c-8b46-ab1322c6364c/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6748a5be-cfe1-4b2c-8b46-ab1322c6364c",
-                    "title": "Hospital Change of Ownership : 2022-12-30",
+                    "format": "API",
                     "modified": "2023-03-06",
-                    "temporal": "2022-10-01/2022-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/6748a5be-cfe1-4b2c-8b46-ab1322c6364c",
+                    "temporal": "2022-10-01/2022-12-31",
+                    "title": "Hospital Change of Ownership : 2022-12-30"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-10/56134ab3-5a94-4c43-b97a-5408e3b7dc0f/Hospital_CHOW_2022.09.30.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4a71ba37-45d0-4a8b-93bb-dedb3f39c049",
-                    "title": "Hospital Change of Ownership : 2022-09-30",
                     "modified": "2022-10-25",
-                    "temporal": "2022-07-01/2022-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4a71ba37-45d0-4a8b-93bb-dedb3f39c049",
+                    "temporal": "2022-07-01/2022-09-30",
+                    "title": "Hospital Change of Ownership : 2022-09-30"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/4a71ba37-45d0-4a8b-93bb-dedb3f39c049/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4a71ba37-45d0-4a8b-93bb-dedb3f39c049",
-                    "title": "Hospital Change of Ownership : 2022-09-30",
+                    "format": "API",
                     "modified": "2022-10-25",
-                    "temporal": "2022-07-01/2022-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/4a71ba37-45d0-4a8b-93bb-dedb3f39c049",
+                    "temporal": "2022-07-01/2022-09-30",
+                    "title": "Hospital Change of Ownership : 2022-09-30"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-07/1af25c56-9f89-4495-94a9-bf719f18e967/Study_01.032.02_2022.07.01_PPEF_Hospital_CHOW_Extract.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d779fb35-1882-4dda-a0a0-e754ab4e634d",
-                    "title": "Hospital Change of Ownership : 2022-06-30",
                     "modified": "2022-07-28",
-                    "temporal": "2022-04-01/2022-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d779fb35-1882-4dda-a0a0-e754ab4e634d",
+                    "temporal": "2022-04-01/2022-06-30",
+                    "title": "Hospital Change of Ownership : 2022-06-30"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/d779fb35-1882-4dda-a0a0-e754ab4e634d/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d779fb35-1882-4dda-a0a0-e754ab4e634d",
-                    "title": "Hospital Change of Ownership : 2022-06-30",
+                    "format": "API",
                     "modified": "2022-07-28",
-                    "temporal": "2022-04-01/2022-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/d779fb35-1882-4dda-a0a0-e754ab4e634d",
+                    "temporal": "2022-04-01/2022-06-30",
+                    "title": "Hospital Change of Ownership : 2022-06-30"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2022-04/Hospital_CHOW_2022Q1.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2b26bbaa-61e8-4a94-aa3f-eaf5719b78b1",
-                    "title": "Hospital Change of Ownership : 2022-03-31",
                     "modified": "2022-05-04",
-                    "temporal": "2022-01-01/2022-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2b26bbaa-61e8-4a94-aa3f-eaf5719b78b1",
+                    "temporal": "2022-01-01/2022-03-31",
+                    "title": "Hospital Change of Ownership : 2022-03-31"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/2b26bbaa-61e8-4a94-aa3f-eaf5719b78b1/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2b26bbaa-61e8-4a94-aa3f-eaf5719b78b1",
-                    "title": "Hospital Change of Ownership : 2022-03-31",
+                    "format": "API",
                     "modified": "2022-05-04",
-                    "temporal": "2022-01-01/2022-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/2b26bbaa-61e8-4a94-aa3f-eaf5719b78b1",
+                    "temporal": "2022-01-01/2022-03-31",
+                    "title": "Hospital Change of Ownership : 2022-03-31"
                 }
             ],
             "identifier": "https://data.cms.gov/data-api/v1/dataset/c04031db-54ce-461c-85d1-d2613d71f167/data-viewer",
@@ -10585,236 +10584,236 @@
                 "fn": "Provider Enrollment Data Requests - CPI",
                 "hasEmail": "mailto:ProviderEnrollmentDataRequests@cms.hhs.gov"
             },
+            "dataQuality": true,
             "describedBy": "https://data.cms.gov/sites/default/files/2024-10/Hospital_CHOW_Owners_Data_Dictionary.pdf",
             "describedByType": "application/pdf",
-            "dataQuality": true,
             "description": "The Hospital Change of Ownership (CHOW) - Owner Information dataset provides information on individual and organizational ownership interest and managerial control associated with the buyer and seller organizations, role of the owner, association date, address of the organizational owner and other ownership details.",
             "distribution": [
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/60625dc8-b621-45f0-9423-077fd133b13e/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/60625dc8-b621-45f0-9423-077fd133b13e",
                     "description": "latest",
-                    "title": "Hospital Change of Ownership - Owner Information : 2024-12-01",
+                    "format": "API",
                     "modified": "2025-01-15",
-                    "temporal": "2024-10-01/2024-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/60625dc8-b621-45f0-9423-077fd133b13e",
+                    "temporal": "2024-10-01/2024-12-31",
+                    "title": "Hospital Change of Ownership - Owner Information : 2024-12-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/e42d8d95-39eb-43a4-86ca-de774b00c7ca/Hospital_CHOW_Owners_2025.01.02.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9573d9f5-1abd-4511-b426-b5966c56050f",
-                    "title": "Hospital Change of Ownership - Owner Information : 2024-12-01",
                     "modified": "2025-01-15",
-                    "temporal": "2024-10-01/2024-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9573d9f5-1abd-4511-b426-b5966c56050f",
+                    "temporal": "2024-10-01/2024-12-31",
+                    "title": "Hospital Change of Ownership - Owner Information : 2024-12-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/9573d9f5-1abd-4511-b426-b5966c56050f/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9573d9f5-1abd-4511-b426-b5966c56050f",
-                    "title": "Hospital Change of Ownership - Owner Information : 2024-12-01",
+                    "format": "API",
                     "modified": "2025-01-15",
-                    "temporal": "2024-10-01/2024-12-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/9573d9f5-1abd-4511-b426-b5966c56050f",
+                    "temporal": "2024-10-01/2024-12-31",
+                    "title": "Hospital Change of Ownership - Owner Information : 2024-12-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/b3ddd565-52d7-4d9c-a1c6-ca663a2a0d58/Hospital_CHOW_Owners_2024.10.07.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ab0061aa-4513-465d-8e3d-162a993190b3",
-                    "title": "Hospital Change of Ownership - Owner Information : 2024-09-01",
                     "modified": "2024-10-15",
-                    "temporal": "2024-07-01/2024-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ab0061aa-4513-465d-8e3d-162a993190b3",
+                    "temporal": "2024-07-01/2024-09-30",
+                    "title": "Hospital Change of Ownership - Owner Information : 2024-09-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/ab0061aa-4513-465d-8e3d-162a993190b3/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ab0061aa-4513-465d-8e3d-162a993190b3",
-                    "title": "Hospital Change of Ownership - Owner Information : 2024-09-01",
+                    "format": "API",
                     "modified": "2024-10-15",
-                    "temporal": "2024-07-01/2024-09-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/ab0061aa-4513-465d-8e3d-162a993190b3",
+                    "temporal": "2024-07-01/2024-09-30",
+                    "title": "Hospital Change of Ownership - Owner Information : 2024-09-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/78be0289-f7fd-4866-8534-d4ebd4e4f68b/Hospital_CHOW_Owners_2024.07.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/101960de-5d1a-4a2e-a878-9caaf39b7a9a",
-                    "title": "Hospital Change of Ownership - Owner Information : 2024-06-01",
                     "modified": "2024-07-15",
-                    "temporal": "2024-04-01/2024-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/101960de-5d1a-4a2e-a878-9caaf39b7a9a",
+                    "temporal": "2024-04-01/2024-06-30",
+                    "title": "Hospital Change of Ownership - Owner Information : 2024-06-01"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
                     "accessURL": "https://data.cms.gov/data-api/v1/dataset/101960de-5d1a-4a2e-a878-9caaf39b7a9a/data",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/101960de-5d1a-4a2e-a878-9caaf39b7a9a",
-                    "title": "Hospital Change of Ownership - Owner Information : 2024-06-01",
+                    "format": "API",
                     "modified": "2024-07-15",
-                    "temporal": "2024-04-01/2024-06-30"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/101960de-5d1a-4a2e-a878-9caaf39b7a9a",
+                    "temporal": "2024-04-01/2024-06-30",
+                    "title": "Hospital Change of Ownership - Owner Information : 2024-06-01"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/c754fd99-0df2-4ee5-94f7-cc3c3625732e/Hospital_CHOW_Owners_2024.04.01.csv",
                     "mediaType": "text/csv",
-                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1166689d-490e-41d0-842a-fde005fab35e",
-                    "title": "Hospital Change of Ownership - Owner Information : 2024-03-31",
                     "modified": "2024-04-15",
-                    "temporal": "2024-01-01/2024-03-31"
+                    "resourcesAPI": "https://data.cms.gov/data-api/v1/dataset-resources/1166689d-490e-41d0-842a-fde005fab35e",
+                    "temporal": "2024-01-01/2024-03-31",
+                    "title": "Hospital Change of Ownership - Owner Information : 2024-03-31"
                 },
                 {
                     "@type": "dcat:Distribution",
-                    "format": "API",
```

