# Change History for healthdata.json (Part 21)

### Changes from 761a84b to acf49f0 (Part 10/12)
**Author:** Automated

**Date:** 2025-01-31 15:36:25+00:00

**Message:** Updated data: Fri Jan 31 15:36:25 UTC 2025

```diff
+            "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of behavioral health services, including emergency department services, inpatient services, intensive outpatient/partial hospitalizations, outpatient services, or services delivered through telehealth, provided to Medicaid and CHIP beneficiaries, by state. Users can filter by either mental health disorder or substance use disorder. \r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating behavioral health services measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Claims Volume - IP, Claims Volume - OT, Diagnosis Code - IP, Diagnosis Code - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+            "title": "Blood Lead Screening Services Provided to Medicaid and CHIP Beneficiaries Ages 1-2",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/Blood-Lead-Screening-Services-Provided-to-MedicaidCHIP-Beneficiaries-Ages-1-2.csv",
+                    "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of behavioral health services, including emergency department services, inpatient services, intensive outpatient/partial hospitalizations, outpatient services, or services delivered through telehealth, provided to Medicaid and CHIP beneficiaries, by state. Users can filter by either mental health disorder or substance use disorder. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating behavioral health services measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Claims Volume - IP, Claims Volume - OT, Diagnosis Code - IP, Diagnosis Code - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "@type": "dcat:Distribution",
+                    "title": "Blood Lead Screening Services Provided to Medicaid and CHIP Beneficiaries Ages 1-2"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-part-d-prescribers/medicare-part-d-prescribers-by-geography-and-drug",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2013-01-01/2022-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2024-06-04",
+            "references": [
+                "https://data.cms.gov/resources/medicare-part-d-prescribers-methodology"
+            ],
+            "keyword": [
+                "drugs",
+                "health equity",
+                "medicare",
+                "medicare prescription drug",
+                "national",
+                "physicians & practitioners",
+                "states & territories"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicare Provider Data - OEDA",
+                "hasEmail": "mailto:IPAG_Data_Products@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/c8ea3f8e-3a09-4fea-86f2-8902fb4b0920/data-viewer",
+            "description": "The Medicare Part D Prescribers by Geography and Drug dataset contains information on prescription drugs prescribed by individual physicians and other health care providers and paid for under the Medicare Part D Prescription Drug Program. For each drug, the dataset includes the total number of prescriptions that were dispensed, which include original prescriptions and any refills, and the total drug cost. The total drug cost includes the ingredient cost of the medication, dispensing fees, sales tax, and any applicable administration fees and is based on the amount paid by the Part D plan, Medicare beneficiary, government subsidies, and any other third-party payers.",
+            "title": "Medicare Part D Prescribers - by Geography and Drug",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c8ea3f8e-3a09-4fea-86f2-8902fb4b0920/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Medicare Part D Prescribers - by Geography and Drug : 2022-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/410ed206-d782-4dba-b442-6bcd45ae2016/MUP_DPR_RY24_P04_V10_DY22_Geo.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Part D Prescribers - by Geography and Drug : 2022-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/1fc57194-a51d-4864-aee6-de0889488151/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Part D Prescribers - by Geography and Drug : 2022-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/3d3ebd5b-b4bf-45b4-876d-afa7916d1b72/MUP_DPR_RY23_P04_V10_DY21_Geo.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Part D Prescribers - by Geography and Drug : 2021-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7dda2a9d-034a-446a-b4b3-e1254e0127b2/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Part D Prescribers - by Geography and Drug : 2021-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-07/ca71b7df-4d48-4c2d-aded-2ca22285739c/MUP_DPR_RY22_P04_V10_DY20_Geo.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Part D Prescribers - by Geography and Drug : 2020-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/83891e77-99cf-4865-b60a-97703b916e09/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Part D Prescribers - by Geography and Drug : 2020-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-08/MUP_DPR_RY21_P04_V10_DY19_Geo.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Part D Prescribers - by Geography and Drug : 2019-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/73a6335e-f16f-4c81-a84b-6b5a986e2bf8/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Part D Prescribers - by Geography and Drug : 2019-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-08/MUP_DPR_RY21_P04_V10_DY18_Geo.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Part D Prescribers - by Geography and Drug : 2018-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/b083c9b6-b841-4676-8d0a-fb03ee1431a1/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Part D Prescribers - by Geography and Drug : 2018-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/efe83dea-bdce-457f-b8b3-fe3b8e9e0c33/MUP_DPR_RY21_P04_V10_DY17_Geo.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Part D Prescribers - by Geography and Drug : 2017-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7863e41c-3f6f-4889-93a8-be65e9f3d073/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Part D Prescribers - by Geography and Drug : 2017-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-08/MUP_DPR_RY21_P04_V10_DY16_Geo_0.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Part D Prescribers - by Geography and Drug : 2016-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c5b3c840-5eb2-4e4c-ac35-c30995dcb051/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Part D Prescribers - by Geography and Drug : 2016-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-08/MUP_DPR_RY21_P04_V10_DY15_Geo_0.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Part D Prescribers - by Geography and Drug : 2015-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/73748d0b-2acb-420a-ac66-27d8e238fdc8/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Part D Prescribers - by Geography and Drug : 2015-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-08/MUP_DPR_RY21_P04_V10_DY14_Geo_0.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Part D Prescribers - by Geography and Drug : 2014-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/63099eb4-6c9e-4fec-8c9e-b6b132f1b7f4/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Part D Prescribers - by Geography and Drug : 2014-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-08/MUP_DPR_RY21_P04_V10_DY13_Geo_0.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Part D Prescribers - by Geography and Drug : 2013-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9aec2a70-4ef2-438a-bc35-1747fe2492c9/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Part D Prescribers - by Geography and Drug : 2013-12-31"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/medicare-part-d-prescribers-by-geography-and-drug-data-dictionary",
+            "dataQuality": true,
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "Medicare"
+            ],
+            "language": [
+                "en-US"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/federally-qualified-health-center-enrollments",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-12-08",
+            "temporal": "2023-10-01/2025-03-31",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-15",
+            "references": [
+                "https://data.cms.gov/sites/default/files/2023-09/FQHC_Data_Guidance.pdf"
+            ],
+            "keyword": [
+                "federally qualified health centers",
+                "hospitals & facilities",
+                "medicare",
+                "outpatient facilities",
+                "provider enrollment"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Provider Enrollment Data Requests - CPI",
+                "hasEmail": "mailto:ProviderEnrollmentDataRequests@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/4bcae866-3411-439a-b762-90a6187c194b/data-viewer",
+            "description": "The Federally Qualified Health Center (FQHC) Enrollments dataset provides enrollment information on all FQHCs currently enrolled in Medicare. This data includes information on the FQHC's legal business name, doing business as name, organization type, and address.",
+            "title": "Federally Qualified Health Center Enrollments",
+            "describedByType": "application/pdf",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4bcae866-3411-439a-b762-90a6187c194b/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Federally Qualified Health Center Enrollments : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/472db45d-c7ce-4b0b-8251-0470e625e521/FQHC_Enrollments_2025.01.02.csv",
+                    "mediaType": "text/csv",
+                    "title": "Federally Qualified Health Center Enrollments : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/376a6172-0b62-4c47-88bb-9c9732ea42eb/data",
+                    "mediaType": "text/html",
+                    "title": "Federally Qualified Health Center Enrollments : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/aaa3ac6d-2ce2-4fd5-9708-9e88a3fd1ebf/FQHC_Enrollments_2024.10.07.csv",
+                    "mediaType": "text/csv",
+                    "title": "Federally Qualified Health Center Enrollments : 2024-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/1c2ec7dd-56c1-4b04-ba73-dcc978049181/data",
+                    "mediaType": "text/html",
+                    "title": "Federally Qualified Health Center Enrollments : 2024-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/bbfda66b-17f2-4f9f-b925-a04ade860d03/FQHC_Enrollments_2024.07.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Federally Qualified Health Center Enrollments : 2024-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/81be797a-03bd-4498-92a0-4ebeb4939030/data",
+                    "mediaType": "text/html",
+                    "title": "Federally Qualified Health Center Enrollments : 2024-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/eeb6e419-6f57-41d6-97d3-3f57aca24efc/FQHC_Enrollments_2024.04.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Federally Qualified Health Center Enrollments : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/fee5c58a-9c36-421f-970b-80f5efca33d3/data",
+                    "mediaType": "text/html",
+                    "title": "Federally Qualified Health Center Enrollments : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/ccc48ded-e404-491a-bbbb-7983ce547417/FQHC_Enrollments_2024.01.05.csv",
+                    "mediaType": "text/csv",
+                    "title": "Federally Qualified Health Center Enrollments : 2024-01-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/dc4defb6-1b1d-4b49-8188-1718c96c7f85/data",
+                    "mediaType": "text/html",
+                    "title": "Federally Qualified Health Center Enrollments : 2024-01-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/e8963e3f-f1cd-4709-86e4-a74b9a1ca694/FQHC_Enrollments_2023.11.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Federally Qualified Health Center Enrollments : 2023-10-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ba0c506c-a269-402d-baa9-4941b36c71b1/data",
+                    "mediaType": "text/html",
+                    "title": "Federally Qualified Health Center Enrollments : 2023-10-28"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/sites/default/files/2023-09/FQHC_Enrollments_Data_Dictionary.pdf",
+            "dataQuality": true,
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P3M",
+            "theme": [
+                "Medicare"
+            ],
+            "language": [
+                "en-US"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/p7bq-srdf",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-03-28",
+            "@type": "dcat:Dataset",
+            "modified": "2023-03-23",
+            "references": [
+                "https://www.mathematica.org/"
+            ],
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DataConnect Support Team",
+                "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "6ac0cd59-34dd-5a2b-aca9-6f9322fbf7be",
+            "description": "This is a dataset created for use by the Scorecard website, and is not intended for use outside that application.",
+            "title": "Scorecard measure",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/measure.csv",
+                    "description": "Scorecard measure",
+                    "@type": "dcat:Distribution",
+                    "title": "Scorecard measure"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/PT1S",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/dataset/mental-health-treatement-facilities-locator",
+            "bureauCode": [
+                "009:30"
+            ],
+            "issued": "2012-12-14",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "health care providers",
+                "help",
+                "locator",
+                "mental health treatment facilities",
+                "provider",
+                "psychatrist",
+                "psychologist",
+                "safety",
+                "sexual assault",
+                "substance abuse. buprenorphine",
+                "suicide prevention",
+                "therapy",
+                "treatments"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Find Treatment",
+                "hasEmail": "mailto:findtreatment@samhsa.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Substance Abuse & Mental Health Services Administration, Department of Health & Human Services"
+            },
+            "identifier": "08d3f21c-6ab7-4f78-9590-54eb07ee6670",
+            "description": "<p>An online resource for locating mental health treatment facilities and programs supported by the Substance Abuse and Mental Health Services Administration (SAMHSA). The Mental Health Treatment Locator section of the Behavioral Health Treatment Services Locator lists facilities providing mental health services to persons with mental illness. It includes:<br />\nPublic mental health facilities that are funded by their State mental health agency (SMHA) or other State agency or department<br />\nMental health treatment facilities administered by the Department of Veterans Affairs, Private for-profit and non-profit mental health facilities that are licensed by the State or accredited by a national accreditation organization.</p>\n<p>NOTE: The Mental Health Treatment Locator does not include facilities whose primary or only focus is the provision of services to persons with Mental Retardation (MR), Developmental Disability (DD), and Traumatic Brain Injuries (TBI). Facilities that provide treatment exclusively to persons with mental illness who are incarcerated. Mental health professionals in private practice (individual) or in a small group practice not licensed or certified as a mental health clinic or (community) mental health center.</p>\n<p>SAMHSA endeavors to keep the Locator current. All information in the Locator is updated annually based on facility responses to SAMHSA's National Mental Health Services Survey (N-MHSS). The most recent complete update includes data collected as of April 30, 2010 in the N-MHSS. New facilities are added monthly. Updates to facility names, addresses, telephone numbers and services are made weekly, if facilities inform SAMHSA of changes.</p>\n<p>For additional advice, you may call the Referral Helpline operated by SAMHSA's Center for Substance Abuse Treatment:</p>\n<p><code>1-800-662-HELP (English &amp; Espa\u00f1ol)</p>\n<p>1-800-487-4889 (TTY)<br />\n</code></p>",
+            "title": "Mental Health Treatement Facilities Locator",
+            "programCode": [
+                "009:068"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://findtreatment.samhsa.gov/",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.mentalhealth.gov/widgets-badges/index.html",
+                    "mediaType": "text/html",
+                    "title": "Widget "
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://serviceslocator.mentalhealth.gov/providers/",
+                    "mediaType": "text/html",
+                    "title": "Map "
+                }
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.ncbi.nlm.nih.gov/snp",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2016-07-17",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Phan, Lon",
+                "hasEmail": "mailto:lonphan@ncbi.nlm.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
+            "identifier": "d6fe10ae-1cf5-4466-bf9e-f9e5ab267fa0",
+            "description": "<p>dbSNP is a database of single nucleotide polymorphisms (SNPs) and multiple small-scale variations that include insertions/deletions, microsatellites, and non-polymorphic variants.</p>",
+            "title": "dbSNP",
+            "programCode": [
+                "009:041"
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/p82x-rydy",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-08-08",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-07",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "c85171aa-68dc-42eb-85c6-4a24fc3185a7",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-07-31-to-2023-08-06",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rprt-drug-07-31-2023-to-08-06-2023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-07-31-to-2023-08-06"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/ef89-9ik2",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-15",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Health Effects Laboratory Division, Pathology and Physiology Research Branch",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/ef89-9ik2",
+            "description": "Interleukin (IL)-11, a pleiotropic, cationic cytokine, contributes to numerous biological processes, including adipogenesis, hematopoiesis, and inflammation.  Asthma, a chronic respiratory disease, is notably characterized by reversible airway obstruction, persistent lung inflammation, and airway hyperresponsiveness (AHR).  Nasal insufflation of IL-11 causes AHR in wild-type mice while lung inflammation induced by antigen sensitization and challenge, which mimics features of atopic asthma in humans, is attenuated in mice genetically deficient in IL-11 receptor subunit alpha-1 (IL-11R\u03b11-deficient mice), a transmembrane receptor that is required along with glycoprotein 130 to transduce IL-11 intracellular signaling.  Nevertheless, the contribution of IL-11R\u03b11 to the manifestation of phenotypic features of non-atopic asthma are not presently known. Thus, based on the aforementioned observations, we hypothesized that genetic deficiency of IL-11R\u03b11 would attenuate lung inflammation and increases in airway responsiveness following acute inhalation exposure to ozone, a criteria pollutant and non-atopic asthma stimulus.",
+            "title": "Interleukin-11 Receptor Subunit Alpha-1 is Required for Maximal Airway Responsiveness to Methacholine After Acute Exposure to Ozone",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/ef89-9ik2/application/x-zip-compressed",
+                    "mediaType": "application/x-zip-compressed"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "National Institute for Occupational Safety and Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/p8hn-wtmc",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-10-08",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-15",
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
+            ],
+            "keyword": [
+                "dqatlas",
+                "dqatlas_featauto",
+                "utility"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DataConnect Support Team",
+                "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "9e407144-9ed9-5cee-937a-17d65b07a9a7",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "featAuto_map",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/map.csv",
+                    "description": "{\"dataset\": \"map\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "@type": "dcat:Distribution",
+                    "title": "map csv file"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/PT1S",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/p8w9-uqca",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-08-23",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-28",
+            "keyword": [
+                "individual",
+                "individual market medical",
+                "py2023",
+                "qhp",
+                "qhp landscape"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Center for Consumer Information and Insurance Oversight",
+                "hasEmail": "mailto:CMS_FEPS@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "identifier": "cfbbddd9-b405-4c4a-b679-fd2986945b88",
+            "description": "The Medical Individual Market file of the QHP Landscape Files contains information on certified medical plans offered through an Exchange to consumers in the individual market. These plans are also known as Qualified Health Plans (QHPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
+            "title": "QHP Landscape PY2023 Individual Medical",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2023/individual_market_medical.zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/p988-gfex",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2015-06-11",
+            "@type": "dcat:Dataset",
+            "modified": "2024-06-11",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "17c4bf03-ba38-5c0a-9f08-96e9ed812bdf",
+            "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
+            "title": "State Drug Utilization Data 1995",
+            "programCode": [
+                "009:076"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/StateDrugUtilizationData1995.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P10Y",
+            "theme": [
+                "State Drug Utilization"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/5dqz-y4ea",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-12-06",
+            "temporal": "2024-10-04/present",
+            "@type": "dcat:Dataset",
+            "modified": "2024-12-06",
+            "keyword": [
+                "cfa",
+                "coronavirus",
+                "covid-19",
+                "epidemic trend",
+                "flu",
+                "influenza",
+                "modeling",
+                "respiratory virus response",
+                "rt",
+                "rvr"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Center for Forecasting and Outbreak Analytics",
+                "hasEmail": "mailto:cfa@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/5dqz-y4ea",
+            "description": "An archive of estimated trend categories, probabilities of epidemic growth, and Rt, updated weekly for COVID-19 and flu. Estimates are based on emergency department visits reported to the National Syndromic Surveillance Program (NSSP), and generated using a model that includes nowcasting to adjust for incomplete reports on the most recent dates. See the visuals supported by these data, and more information about the data, models and methods at https://www.cdc.gov/cfa-modeling-and-forecasting/rt-estimates/index.html, and https://www.cdc.gov/respiratory-viruses/data/activity-levels.html.\n\nFor a semi-technical overview of the modeling methods used to generate these estimates see https://www.cdc.gov/cfa-behind-the-model/php/data-research/rt-estimates/index.html.\n\nFor the code used to run the models, see https://github.com/CDCgov/cfa-epinow2-pipeline.",
+            "title": "CDC Epidemic Trends and Rt",
+            "programCode": [
+                "009:026"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5dqz-y4ea/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5dqz-y4ea/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5dqz-y4ea/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5dqz-y4ea/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P1W",
+            "theme": [
+                "Public Health Surveillance"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/p9hc-avk4",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-10-08",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-15",
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
+            ],
+            "keyword": [
+                "dqatlas",
+                "dqatlas_implauto",
+                "utility"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DataConnect Support Team",
+                "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "842c5980-37e0-5a3f-989d-a54b60436d34",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "implAuto_tafVersion",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/tafVersion.csv",
+                    "description": "{\"dataset\": \"tafVersion\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "@type": "dcat:Distribution",
+                    "title": "tafVersion csv file"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/PT1S",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/p9qu-rfuq",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-03-28",
+            "@type": "dcat:Dataset",
+            "modified": "2024-01-05",
+            "keyword": [
+                "chip",
+                "maternal health",
+                "medicaid",
+                "pregnancy"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "a4035a82-7433-4efb-985d-32a9ab8e5341",
+            "description": "This table presents the number of pregnant and postpartum Medicaid and CHIP beneficiaries, 2017-2021. It includes (1) the number and percentage of beneficiaries ever pregnant in the year; (2) the number and percentage of live births in the year; (3) the number and percentage of miscarriages, stillbirths, or terminations in the year; and (4) the number and percentage of births with an unknown delivery outcome in the year.\r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues, making the data unusable for identifying this population. Data for a state are considered unusable based on DQ Atlas thresholds for the following topics: Total Medicaid and CHIP Enrollment, Claims Volume - IP, Claims Volume - OT, Claims Volume - IP, Diagnosis Code - IP, Diagnosis Code - OT, Procedure Codes - OT Professional. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \r\n\r\nData from Maryland, Tennessee, and Utah are omitted from the tables due to data quality concerns. Maryland was excluded in 2017 due to unusable diagnosis codes in the IP file and the OT file. Tennessee was excluded due to unusable diagnosis codes in the IP file in 2017 - 2019. Utah was excluded due to unusable procedure codes on OT professional claims in 2017 - 2020. In addition, states with a high data quality concern on one or more measures are noted in the table in the \"Data Quality\" column. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+            "title": "Number of pregnant and postpartum Medicaid and CHIP beneficiaries, 2017-2021",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/pregnent-postpartum-beneficiaries-2017to2021.csv",
+                    "mediaType": "text/csv",
+                    "title": "Number of pregnant and postpartum Medicaid and CHIP beneficiaries, 2017-2021"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/p9sp-5gqf",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-10-08",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-15",
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
+            ],
+            "keyword": [
+                "dqatlas",
+                "dqatlas_featauto",
+                "utility"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DataConnect Support Team",
+                "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "a49b8d56-2f5a-5990-a1a3-bc154ca04570",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "featAuto_concernLevel",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/concernLevel.csv",
+                    "description": "{\"dataset\": \"concernLevel\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "@type": "dcat:Distribution",
+                    "title": "concernLevel csv file"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/PT1S",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/dataset/vital-stats-vital-statistics-tables-and-files-births-infant-deaths-fetal-deaths",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2012-11-05",
+            "temporal": "1990-01-01T00:00:00-05:00/2011-12-31T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "births perinatal mortality  population statistics",
+                "population statistics"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Health & Human Services"
+            },
+            "identifier": "f954e1b2-d513-4b70-b892-f1bebbed46bb",
+            "description": "<p>VitalStats:  A collection of vital statistics products including tables, data files, and reports that allow users to access and examine vital statistics and population data interactively.</p>\n<p>VitalStats includes pre-built tables and reports for quick access to statistics;  or the user can create tables--choosing from over 100 variables.  Tables can be customized to create charts, graphs, and maps.  Data can be exported.</p>",
+            "title": "Vital Stats (Vital Statistics Tables and files- Births, Infant Deaths, Fetal Deaths)",
+            "programCode": [
+                "009:048"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+                    "mediaType": "text/html",
+                    "title": "HTML "
+                }
+            ],
+            "describedBy": "http://www.cdc.gov/nchs/VitalStats.htm",
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/nhanes/visualization/index.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2020-12-16",
+            "temporal": "1999/2018",
+            "@type": "dcat:Dataset",
+            "modified": "2023-09-08",
+            "keyword": [
+                "high cholesterol",
+                "hypertension",
+                "nhanes",
+                "obesity"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/28df-2bwy",
+            "description": "This data represents the age-adjusted prevalence of high total cholesterol, hypertension, and obesity among US adults aged 20 and over between 1999-2000 to 2017-2018.\n\n\nNotes:\n\n* All estimates are age adjusted by the direct method to the U.S. Census 2000 population using age groups 20\u201339, 40\u201359, and 60 and over.\n\n\nDefinitions\n\nHypertension: Systolic blood pressure greater than or equal to 130 mmHg or diastolic blood pressure greater than or equal to 80 mmHg, or currently taking medication to lower high blood pressure\n\nHigh total cholesterol: Serum total cholesterol greater than or equal to 240 mg/dL.\n\nObesity: Body mass index (BMI, weight in kilograms divided by height in meters squared) greater than or equal to 30.\n\n\nData Source and Methods\n\nData from the National Health and Nutrition Examination Surveys (NHANES) for the years 1999\u20132000, 2001\u20132002, 2003\u20132004, 2005\u20132006, 2007\u20132008, 2009\u20132010, 2011\u20132012, 2013\u20132014, 2015\u20132016, and 2017\u20132018 were used for these analyses.\n\nNHANES is a cross-sectional survey designed to monitor the health and nutritional status of the civilian noninstitutionalized U.S. population. The survey consists of interviews conducted in participants\u2019 homes and standardized physical examinations, including a blood draw, conducted in mobile examination centers.",
+            "title": "Prevalence of Selected Measures Among Adults Aged 20 and Over: United States, 1999-2000 through 2017-2018",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/28df-2bwy/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/28df-2bwy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/28df-2bwy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/28df-2bwy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "irregular",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/hus/index.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2020-11-10",
+            "@type": "dcat:Dataset",
+            "modified": "2022-09-13",
+            "keyword": [
+                "adults",
+                "children",
+                "death rates",
+                "drug overdose",
+                "health care coverage",
+                "health conditions",
+                "health united states",
+                "heath care access",
+                "leading causes of death",
+                "life expectancy",
+                "obesity",
+                "resources",
+                "substance use"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/v5gm-kvkn",
+            "description": "Health, United States  is the report on the health status of the country. Every year, the report presents an overview of national health trends organized around four subject areas: health status and determinants, utilization of health resources, health care resources, and health care expenditures and payers.",
+            "title": "Health, United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.cdc.gov/nchs/hus/data-finder.htm",
+                    "description": "The Data Finder gives you Health, United States trend tables and figures on a subject and/or population subgroup of interest. ",
+                    "@type": "dcat:Distribution",
+                    "title": "Data Finder"
+                }
+            ],
+            "spatial": "US",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "NCHS"
+            ],
+            "language": [
+                "en-US"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/pbyt-qpdj",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-11-20",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-18",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "3e3820b8-e89f-42a5-9e53-7557f98d7a7f",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 11-11-2024-to-11-17-2024",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/mdrp-newly-rprt-drug-11-11-2024-to-11-17-2024.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/crzr-uvwg",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2019-06-27",
+            "@type": "dcat:Dataset",
+            "modified": "2024-09-03",
+            "keyword": [
+                "drug label",
+                "medication"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Library of Medicine",
+                "hasEmail": "mailto:custserv@nlm.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/crzr-uvwg",
+            "description": "This resource was retired on January 28, 2021 and is no longer updated.  These data remain available to support research and development efforts.  Pillbox's final image library is available at https://ftp.nlm.nih.gov/projects/pillbox/pillbox_production_images_full_202008.zip.  For more information on Pillbox's retirement visit https://www.nlm.nih.gov/pubs/techbull/ja20/ja20_pillbox_discontinue.html.\n\nPillbox contains metadata for oral solid dosage form medications, derived from FDA drug labeling, including physical characteristics, active and inactive ingredients, National Drug Codes, information about firms marketing those products, selected information from RxNorm, and links to images provided by the National Library of Medicine.",
+            "title": "Pillbox (retired January 28, 2021)",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/crzr-uvwg/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/crzr-uvwg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/crzr-uvwg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/crzr-uvwg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Drugs and Chemicals"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/p8tr-pquj",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2015-01-23",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-27",
+            "keyword": [
+                "glossary",
+                "methodology"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "OSHData Support",
+                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/p8tr-pquj",
+            "description": "Download the latest version of the Glossary and Methodology File",
+            "title": "SAMHSA Synar Reports: Youth Tobacco Sales Glossary and Methodology",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/p8tr-pquj/application/vnd.ms-excel",
+                    "mediaType": "application/vnd.ms-excel"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Policy"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/xbk2-5i4e",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2018-07-26",
+            "@type": "dcat:Dataset",
+            "modified": "2018-11-27",
+            "keyword": [
+                "drought",
+                "environmental health"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Craig Kassinger",
+                "hasEmail": "mailto:nephtrackingsupport@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/xbk2-5i4e",
+            "description": "This dataset provides data at the county level for the contiguous United States. It includes monthly Standardized Precipitation Index (SPI) data from 1895-2016 provided by the Cooperative Institute for Climate and Satellites - North Carolina. Please refer to the metadata attachment for more information.\r\n\r\nLearn more about drought on the Tracking Network's website: https://ephtracking.cdc.gov/showDroughtLanding.\r\n\r\nBy using these data, you signify your agreement to comply with the following requirements: \r\n1.\tUse the data for statistical reporting and analysis only. \r\n2.\tDo not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals. \r\n3.\tDo not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov. \r\n4.\tDo not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating. \r\n5.\tAcknowledge, in all reports or presentations based on these data, the original source of the data and CDC. \r\n6.\tSuggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking. \r\n\r\nProblems or Questions? \r\nEmail trackingsupport@cdc.gov.",
+            "title": "Standardized Precipitation Index, 1895-2016",
+            "programCode": [
+                "009:032"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xbk2-5i4e/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xbk2-5i4e/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xbk2-5i4e/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xbk2-5i4e/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Environmental Health & Toxicology"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/pep3-wh6f",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-04-21",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-08",
+            "references": [
+                "https://www.mathematica.org/"
+            ],
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "942d804c-6c1d-5912-a61f-08d42927ee9b",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "Scorecard state v2.11.16 (cmsdev)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.16/20241107/state.csv",
+                    "description": "Scorecard state v2.11.16 (cmsdev)",
+                    "@type": "dcat:Distribution",
+                    "title": "Scorecard state v2.11.16 (cmsdev)"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/covid/php/covid-net/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-09-22",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-24",
+            "keyword": [
+                "covid",
+                "covid19",
+                "covid-19",
+                "covidnet",
+                "covid-net",
+                "epi curve",
+                "hospitalizations",
+                "icu",
+                "in-hospital death",
+                "percent icu",
+                "percent in-hospital death",
+                "percent mechanically ventilated",
+                "respiratory illness",
+                "respiratory virus response",
+                "respnet",
+                "resp-net",
+                "surveillance"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "RESP-NET",
+                "hasEmail": "mailto:CovidRSV-Net@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/bigw-pgk2",
+            "description": "The Coronavirus Disease 2019 (COVID-19) Hospitalization Surveillance Network (COVID-NET) a network that conducts active, population-based surveillance for laboratory-confirmed COVID-19-associated hospitalizations among children and adults. COVID-NET, along with the Respiratory Syncytial Virus Hospitalization Surveillance Network (RSV-NET) and the Influenza Hospitalization Surveillance Network (FluSurv-NET), comprise the Respiratory Virus Hospitalization Surveillance Network (RESP-NET). The RESP-NET platforms have overlapping surveillance areas and use similar methods to collect data. COVID-NET is CDC\u2019s source for important data on rates of hospitalizations associated with COVID-19. Hospitalization rates show how many people in the surveillance area are hospitalized with COVID-19, compared to the total number of people residing in that area.\n\nData are preliminary and subject to change as more data become available. Data will be updated weekly.",
+            "title": "Patient Characteristics of Laboratory-Confirmed COVID-19 Hospitalizations from the COVID-NET Surveillance System",
+            "programCode": [
+                "009:038"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bigw-pgk2/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bigw-pgk2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bigw-pgk2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bigw-pgk2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "COVID-NET Sites",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Weekly",
+            "theme": [
+                "Public Health Surveillance"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/97tt-n3j3",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2016-01-07",
+            "@type": "dcat:Dataset",
+            "modified": "2016-01-07",
+            "keyword": [
+                "2015",
+                "chlamydia trachomatis infection",
+                "coccidioidomycosis",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/97tt-n3j3",
+            "description": "NNDSS - Table II. Chlamydia to Coccidioidomycosis - 2015.In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed.The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP: Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table 2 to facilitate case count verification with reporting jurisdictions. \ufffd\ufffd\ufffd Case counts for reporting year 2015 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly.",
+            "title": "NNDSS - Table II. Chlamydia to Coccidioidomycosis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/97tt-n3j3/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/97tt-n3j3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/97tt-n3j3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/97tt-n3j3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/pfpx-3ynm",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2022-08-10",
+            "@type": "dcat:Dataset",
+            "modified": "2022-08-17",
+            "keyword": [
+                "business rules",
+                "exchange puf",
+                "marketplace puf",
+                "py2022"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Center for Consumer Information and Insurance Oversight",
+                "hasEmail": "mailto:CMS_FEPS@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "identifier": "e614aeb8-580e-4aae-9140-cf55b4a22180",
+            "description": "The Business Rules PUF (BR-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The BR-PUF contains plan-level data on rating business rules, such as maximum age for a dependent and allowed dependent relationships.",
+            "title": "Business Rules PUF - PY2022",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2022/business_rules_puf.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.ncbi.nlm.nih.gov/sra",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-06-30",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "genetics",
+                "genomics",
+                "tools & utilities"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Library of Medicine",
+                "hasEmail": "mailto:custserv@nlm.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/jp6k-328y",
+            "description": "The Sequence Read Archive (SRA) stores sequencing data from the next generation of sequencing platforms including Roche 454 GS System\u00ae, Illumina Genome Analyzer\u00ae, Life Technologies AB SOLiD System\u00ae, Helicos Biosciences Heliscope\u00ae, Complete Genomics\u00ae, and Pacific Biosciences SMRT\u00ae.",
+            "title": "Sequence Read Archive (SRA)",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/sra",
+                    "mediaType": "text/html",
+                    "title": "Sequence Read Archive (SRA) - Toolkit"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastn&BLAST_PROGRAMS=megaBlast&PAGE_TYPE=BlastSearch&BLAST_SPEC=SRA&SHOW_DEFAULTS=on",
+                    "description": "BLASTN programs search SRA databases using a nucleotide query. ",
+                    "@type": "dcat:Distribution",
+                    "title": "Sequence Read Archive Nucleotide BLAST - Query Interface"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=run_browser",
+                    "description": "Search and browse data for a single RUN",
+                    "@type": "dcat:Distribution",
+                    "title": "SRA Run Browser - Query Interface"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/Traces/study/",
+                    "description": "The Run Selector can select runs from one or more studies to download or analyze with the SRA Toolkit. To retrieve data from SRA, you must download the SRA Toolkit.",
+                    "@type": "dcat:Distribution",
+                    "title": "SRA Run Selector - Query Interface"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://submit.ncbi.nlm.nih.gov/subs/sra/",
+                    "description": "The SRA accepts genetic data and the associated quality scores produced by next generation sequencing technologies. Before submitting, read the SRA Submission Wizard Help. https://www.ncbi.nlm.nih.gov/sra/docs/submitportal/",
+                    "@type": "dcat:Distribution",
+                    "title": "Sequence Read Archive (SRA) Submission Portal"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Molecular biology/Genetics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/ckve-znde",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2023-12-14",
+            "@type": "dcat:Dataset",
+            "modified": "2024-09-03",
+            "keyword": [
+                "api",
+                "mesh",
+                "mesh 2023 update",
+                "terminologies"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Library of Medicine",
+                "hasEmail": "mailto:custserv@nlm.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ckve-znde",
+            "description": "<b>(Includes MeSH 2023 changes)</b>  The MeSH 2024 Update - Split Report lists terms that are replaced by a set of terms, either descriptors or SCRs, instead of a single term.  <b>This report includes MeSH changes from previous years, starting from 2023.</b>",
+            "title": "MeSH 2024 Update - Split Report",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/ckve-znde/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/ckve-znde/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/ckve-znde/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/ckve-znde/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Terminology"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/statesystem/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-07-18",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-25",
+            "references": [
+                "https://chronicdata.cdc.gov/d/h6kq-aiu7"
+            ],
+            "keyword": [
+                "callers",
+                "cessation",
+                "intervention",
+                "national quitline data warehouse",
+                "nqdw",
+                "office on smoking and health",
+                "osh",
+                "quit",
+                "quitline",
+                "quit-now",
+                "services",
+                "state system"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "OSHData Support",
+                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/tbyb-bvjd",
+            "description": "2010-2020.  National Quitline Data Warehouse (NQDW). State Tobacco Activities Tracking and Evaluation (STATE) System.  NQDW Data.  National Quitline Data Warehouse (NQDW) assists in evaluating quitline activities and serves as a national resource for data on the use, success, and services of state quitlines.  States report data on quitline callers, quitting success, as well as the services provided by their quitlines. The NQDW consolidates this information for evaluating programs and improving quitline services.  The jurisdictions participating in this data collection effort include the 50 states, the District of Columbia, Guam and Puerto Rico.",
+            "title": "Quitline \u2013 Services Available \u2013 Medications - 2010 To Present",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tbyb-bvjd/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tbyb-bvjd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tbyb-bvjd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tbyb-bvjd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Quitline/Quitline-Services-Available-Medications-2010-To-Pr/tbyb-bvjd",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "theme": [
+                "Quitline"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://github.com/cmheilig/harvest-cdc-journals",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-03-19",
+            "temporal": "1982 - 2023",
+            "@type": "dcat:Dataset",
+            "modified": "2024-03-22",
+            "references": [
+                "\"https://github.com/cmheilig/harvest-cdc-journals?tab=readme-ov-file\"",
+                "\"https://www.cdc.gov/mmwr/\"",
+                "\"https://wwwnc.cdc.gov/eid\"",
+                "\"https://www.cdc.gov/pcd/\""
+            ],
+            "keyword": [
+                "ai",
+                "corpora",
+                "corpus",
+                "data science",
+                "eid",
+                "harvest-cdc-journals",
+                "informatics",
+                "language",
+                "llm",
+                "machine learning",
+                "ml",
+                "mmwr",
+                "ncstltphiw",
+                "nlp",
+                "pcd",
+                "phic",
+                "text analysis"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NCSTLTPHIW(PHIC) Associate Director of Informatics and Data Science",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/ut5n-bmc3",
+            "description": "The attached ZIP archives are part of the <a href=\"https://github.com/cmheilig/harvest-cdc-journals\">CDC Text Corpora for Learners</a> program. This version, comprised of 33,567 articles, was constructed on 2024-03-01 using source content retrieved on 2024-01-09. \n\nThe attached three ZIP archives contain the 33,567  articles in 33,576 compiled HTML mirrors of the MMWR <a href=\"https://www.cdc.gov/mmwr/\">Morbidity and Mortality Weekly Report</a> including its series: <i>Weekly Reports</i>, <i>Recommendations and Reports</i>, <i>Surveillance Summaries</i>, <i>Supplements</i>, and <i>Notifiable Diseases</i>, a subset of <i>Weekly Reports</i>, constructed ad hoc; EID <a href=\"https://www.cdc.gov/eid/\">Emerging Infectious Diseases</a>; and PCD <a href=\"https://www.cdc.gov/pcd/\">Preventing Chronic Disease</a>.There is one archive per series. The archive attachments are located in the <i>About this Dataset</i> section of this landing page. In that section when you click Show More, the attachments are located in the section <i>Attachments</i>.\n\nThe retrieval and organization of the files included making as few changes to raw sources as possible, to support as many downstream uses as possible.",
+            "title": "CDC Text Corpora for Learners: HTML Mirrors of MMWR, EID, and PCD",
+            "isPartOf": "CDC Text Corpora for Learners",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ut5n-bmc3/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ut5n-bmc3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ut5n-bmc3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ut5n-bmc3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://github.com/cmheilig/harvest-cdc-journals?tab=readme-ov-file#cdc-text-corpora-for-learners",
+            "license": "http://creativecommons.org/publicdomain/zero/1.0/legalcode",
+            "accrualPeriodicity": "Irregular",
+            "theme": [
+                "National Center for State",
+                "Tribal",
+                "Local",
+                "and Territorial Public Health Infrastructure and Workforce"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.ncbi.nlm.nih.gov/datasets/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2022-02-09",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-04",
+            "keyword": [
+                "dataset",
+                "genes",
+                "genomics",
+                "protein"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Library of Medicine",
+                "hasEmail": "mailto:custserv@nlm.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/3br9-y2tm",
+            "description": "NCBI Datasets is one-stop shop for finding, browsing, and downloading genomic data. Find and download taxonomy, genome, gene, transcript, protein data, including installation of NCBI Datasets command-line tools.",
+            "title": "NCBI Datasets",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/datasets/",
+                    "mediaType": "text/html",
+                    "title": "NCBI Datasets (BETA) Homepage, Search, and Utilities"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Molecular biology/Genetics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/d6p8-wqjm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-03-22",
+            "temporal": "September 19, 2021-September 24, 2022",
+            "@type": "dcat:Dataset",
+            "modified": "2023-06-09",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Vaccine Breakthrough Unit, Surveillance and Analytics Team",
+                "hasEmail": "mailto:vbtsurveillance@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/d6p8-wqjm",
+            "description": "Data for CDC\u2019s COVID Data Tracker site on Rates of COVID-19 Cases and Deaths by Vaccination Status.\nClick 'More' for important dataset description and footnotes\n\nDataset and data visualization details:\nThese data were posted on October 21, 2022, archived on November 18, 2022, and revised on February 22, 2023. These data reflect cases among persons with a positive specimen collection date through September 24, 2022, and deaths among persons with a positive specimen collection date through September 3, 2022. \n\nVaccination status: A person vaccinated with a primary series had SARS-CoV-2 RNA or antigen detected on a respiratory specimen collected \u226514 days after verifiably completing the primary series of an FDA-authorized or approved COVID-19 vaccine. An unvaccinated person had SARS-CoV-2 RNA or antigen detected on a respiratory specimen and has not been verified to have received COVID-19 vaccine. Excluded were partially vaccinated people who received at least one FDA-authorized vaccine dose but did not complete a primary series \u226514 days before collection of a specimen where SARS-CoV-2 RNA or antigen was detected.\nAdditional or booster dose: A person vaccinated with a primary series and an additional or booster dose had SARS-CoV-2 RNA or antigen detected on a respiratory specimen collected \u226514 days after receipt of an additional or booster dose of any COVID-19 vaccine on or after August 13, 2021. For people ages 18 years and older, data are graphed starting the week including September 24, 2021, when a COVID-19 booster dose was first recommended by CDC for adults 65+ years old and people in certain populations and high risk occupational and institutional settings. For people ages 12-17 years, data are graphed starting the week of December 26, 2021, 2 weeks after the first recommendation for a booster dose for adolescents ages 16-17 years. For people ages 5-11 years, data are included starting the week of June 5, 2022, 2 weeks after the first recommendation for a booster dose for children aged 5-11 years. For people ages 50 years and older, data on second booster doses are graphed starting the week including March 29, 2022, when the recommendation was made for second boosters. Vertical lines represent dates when changes occurred in U.S. policy for COVID-19 vaccination (details provided above). Reporting is by primary series vaccine type rather than additional or booster dose vaccine type. The booster dose vaccine type may be different than the primary series vaccine type.\n** Because data on the immune status of cases and associated deaths are unavailable, an additional dose in an immunocompromised person cannot be distinguished from a booster dose. This is a relevant consideration because vaccines can be less effective in this group.\nDeaths: A COVID-19\u2013associated death occurred in a person with a documented COVID-19 diagnosis who died; health department staff reviewed to make a determination using vital records, public health investigation, or other data sources. Rates of COVID-19 deaths by vaccination status are reported based on when the patient was tested for COVID-19, not the date they died. Deaths usually occur up to 30 days after COVID-19 diagnosis.\nParticipating jurisdictions: Currently, these 31 health departments that regularly link their case surveillance to immunization information system data are included in these incidence rate estimates: Alabama, Arizona, Arkansas, California, Colorado, Connecticut, District of Columbia, Florida, Georgia, Idaho, Indiana, Kansas, Kentucky, Louisiana, Massachusetts, Michigan, Minnesota, Nebraska, New Jersey, New Mexico, New York, New York City (New York), North Carolina, Philadelphia (Pennsylvania), Rhode Island, South Dakota, Tennessee, Texas, Utah, Washington, and West Virginia; 30 jurisdictions also report deaths among vaccinated and unvaccinated people. These jurisdictions represent 72% of the total U.S. population and all ten of the Health and Human Services Regions. Data on cases",
+            "title": "Rates of COVID-19 Cases or Deaths by Age Group and Vaccination Status and Booster Dose",
+            "programCode": [
+                "009:038"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/d6p8-wqjm/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/d6p8-wqjm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/d6p8-wqjm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/d6p8-wqjm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "Select US Jurisdictions",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "Monthly",
+            "theme": [
+                "Public Health Surveillance"
+            ],
+            "language": [
+                "English"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/vaccines/vaxview/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-12-18",
+            "@type": "dcat:Dataset",
+            "temporal": "2023-2024",
+            "modified": "2024-09-11",
+            "keyword": [
+                "adults",
+                "iqvia",
+                "rsv vaccination"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VaxView Team",
+                "hasEmail": "mailto:VaxView@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/a3gi-4phs",
+            "description": "Weekly Cumulative Estimated Number of RSV Vaccinations Administered in Pharmacies and Physician Medical Offices, Adults 60 Years and Older, United States\n\n\u2022 Estimated Number of RSV vaccinations among adults 60 years and older is assessed through IQVIA (https://www.iqvia.com/) as a source of information on vaccinations administered in retail pharmacies (include chain, mass merchandise, food stores, and independent pharmacies) and physician medical offices.\n\n\u2022 Starting in September 2023, the CDC recommended the RSV vaccine for adults 60 years and older.",
+            "title": "Weekly Cumulative Estimated Number of RSV Vaccinations Administered in Pharmacies and Physician Medical Offices, Adults 60 years and older, United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/a3gi-4phs/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/a3gi-4phs/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/a3gi-4phs/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/a3gi-4phs/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States- National",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Weekly",
+            "theme": [
+                "Vaccinations"
+            ],
+            "language": [
+                "English"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.accessdata.fda.gov/scripts/cber/CFAppsPub/tiss/index.cfm",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2008-04-10",
+            "keyword": [
+                "cber"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "openFDA",
+                "hasEmail": "mailto:open@fda.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "identifier": "dc73689d-c8cc-4c9f-b3ee-c293483dbdb7",
+            "description": "This application provides Human Cell and Tissue registration information for registered, inactive, and pre-registered firms. Query options are by Establishment Name, Establishment Function, Product, Establishment Status, State, Zip Code, and Country.",
+            "title": "Human Cell and Tissue Establishment Registration Public Query",
+            "programCode": [
+                "009:003"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.accessdata.fda.gov/scripts/cber/CFAppsPub/tiss/index.cfm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/pjzq-t23s",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2021-10-14",
+            "@type": "dcat:Dataset",
+            "modified": "2021-10-13",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "1fee67f0-ee42-4cf5-b764-4bf7e2610fe0",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20210802 to 20210808",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rpt-drugs-aug-20210802-to-20210808.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/kpbd-vsd5",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-01-14",
+            "@type": "dcat:Dataset",
+            "modified": "2022-02-11",
+            "keyword": [
+                "2022",
+                "imported",
+                "indigenous",
+                "malaria",
+                "measles",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/kpbd-vsd5",
+            "description": "NNDSS - TABLE 1V. Malaria to Measles, Indigenous - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
+            "title": "NNDSS - TABLE 1V. Malaria to Measles, Indigenous",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kpbd-vsd5/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kpbd-vsd5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kpbd-vsd5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kpbd-vsd5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/76u3-26ik",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-15",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Health Effects Laboratory Division, Physical Effects Research Branch",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/76u3-26ik",
+            "description": "To protect residential roofing construction workers from both fatal and musculoskeletal injuries, it is necessary to assess the musculoskeletal and biomechanical risks in residential roofing tasks. This undertaking requires accurate information of workers\u2019 3D body positions to analyze kinematics and kinetics of the human body. In this study, we proposed a novel 2- stage motion estimation approach based on a convolution neural network to estimate residential roofer\u2019s body positions using three-view video data. Instead of pursuing end-to- end training, our approach includes two stages: (1) use a multi-view model to estimate the 3D pose in a single frame; (2) use a multi-frame model to apply temporal convolutions to refine the multi-view outputs. The performance of the approach was evaluated by comparing our estimation with the gold-standard marker-based 3D human pose estimation (\u201cground truth\u201d). The evaluation results show that our marker-free video-based approach can accurately capture the 3D posture of workers during the common roofing task and the proposed multi-frame model can effectively improve the precision of the coordinate sequence. The values of mean per joint position error of estimated human position before and after processing by the multi-frame model are 27.93 and 24.81 mm, respectively. These results prove that the proposed marker-free motion capture estimation approach can efficiently and accurately locate 3D body joints and pave the way for future onsite musculoskeletal motion analysis during roofing activities.",
+            "title": "Video-Based 3D pose estimation for residential roofing-dataset",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/76u3-26ik/application/x-zip-compressed",
+                    "mediaType": "application/x-zip-compressed"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "National Institute for Occupational Safety and Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/pn26-36bb",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-07-22",
+            "@type": "dcat:Dataset",
+            "modified": "2024-12-11",
+            "references": [
+                "https://www.mathematica.org/"
+            ],
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "92926a98-0f8c-5a43-9e83-d9239fb485a3",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "Scorecard filters v2.11.9 (prod)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.9/20241107/filters.csv",
+                    "description": "Scorecard filters v2.11.9 (prod)",
+                    "@type": "dcat:Distribution",
+                    "title": "Scorecard filters v2.11.9 (prod)"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/wtvk-6zfr",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-15",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Health Effects Laboratory Division, Allergy and Clinical Immunology Branch",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/wtvk-6zfr",
+            "description": "SARS-CoV-2 can be spread by droplets and aerosols expelled by infected people when they cough, talk, sing, or exhale. To reduce exposure to these droplets and aerosols while indoors, CDC recommends measures including physical distancing, universal mask wearing, and room ventilation. Ventilation systems can be supplemented with portable air cleaners to remove infectious material from the air more quickly and provide greater protection. We conducted a case study using respiratory simulators to examine the efficacy of portable High Efficiency Particulate Air (HEPA) air cleaners and universal masking at reducing exposure to simulated exhaled aerosol particles from an infected meeting participant in a conference room. We found that, in a room with good air mixing, the use of two HEPA air cleaners meeting the EPA recommended Clean Air Delivery Rate (CADR) reduced the overall exposure by up to 65%, and that the combination of the HEPA air cleaners and universal masking reduced exposure by up to 90%. The air cleaners were most effective when they were close to the aerosol source. Our results demonstrate that portable HEPA cleaners can be an effective method to reduce exposure to airborne particles while meeting indoors, especially in combination with universal masking.",
+            "title": "Efficacy of Portable Air Cleaners and Masking for Reducing Indoor Exposure to Simulated Exhaled SARS-CoV-2 Aerosols \u2014 United States, 2021",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/wtvk-6zfr/application/x-zip-compressed",
+                    "mediaType": "application/x-zip-compressed"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "National Institute for Occupational Safety and Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.healthit.gov/data/datasets/onc-regional-extension-centers-rec-key-performance-indicators-kpis-state",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-10-03",
+            "@type": "dcat:Dataset",
+            "modified": "2015-06-01",
+            "references": [
+                "https://www.healthit.gov/data/quickstats/percent-rec-enrolled-critical-access-and-rural-hospitals-state-demonstrating",
+                "https://www.healthit.gov/data/quickstats/percent-rec-enrolled-priority-primary-care-providers-ppcps-state-demonstrating"
+            ],
+            "keyword": [
+                "health information technology",
+                "health it",
+                "health it data",
+                "indicators",
+                "rec",
+                "regional extension centers",
+                "state"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "ONC Request",
+                "hasEmail": "mailto:onc.request@hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the National Coordinator for Health Information Technology"
+            },
+            "identifier": "zyaifc3t-i181-2wnr-j3fu-j6qo40bbttxx",
+            "description": "The ONC Regional Extension Centers (REC) Program provides assistance to health care providers to adopt and meaningfully use certified EHR technology. The program, funded through the American Recovery and Reinvestment Act (ARRA) or The Recovery Act, provides grants to organizations, Regional Extension Centers, that assist providers directly in the organization's region. There are 62 unique RECs across the United States. This data set provides county-level health care professional participation in the REC Program. You can track metrics on the total primary care and non-primary care providers that signed up for REC assistance, gone live with an EHR, and demonstrated meaningful use of certified EHR technology. See ONC's REC data by state to track these metrics at the state level.",
+            "title": "ONC Regional Extension Centers (REC) Key Performance Indicators (KPIs) by State",
+            "programCode": [
+                "009:110"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/REC_KPI_State.csv",
+                    "mediaType": "text/csv",
+                    "title": "REC_KPI_State.csv"
+                }
+            ],
+            "describedBy": "https://www.healthit.gov/data/datasets/onc-regional-extension-centers-rec-key-performance-indicators-kpis-state"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/pnsv-sqfk",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2024-08-27",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-07",
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
+            ],
+            "keyword": [
+                "dqatlas",
+                "dqatlas_prodauto",
+                "utility"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DataConnect Support Team",
+                "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "103806a7-aed4-5f01-ad27-c3fccbe2694a",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
+            "title": "prodAuto_brief",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/brief.csv",
+                    "description": "{\"dataset\": \"brief\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "@type": "dcat:Distribution",
+                    "title": "brief csv file"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/PT1S",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/eddk-effy",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-15",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Health Effects Laboratory Division, Toxicology and Molecular Biology Branch",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/eddk-effy",
+            "description": "Growing evidence suggests that Gulf War Illness (GWI) is the result of underlying neuroimmune dysfunction.  For example, previously we found that several Gulf War-relevant organophosphate, acetylcholinesterase inhibitors produce heightened neuroinflammatory responses following a sub chronic stressor exposure.  The goal of the study was to evaluate the potential for the \u03b2-adrenergic receptor inhibitor and anti-inflammatory drug, propranolol, to treat neuroinflammation in a novel long-term mouse model of GWI. We established that our long-term GWI model produces enhanced and prolonged neuroinflammation that is dependent upon Gulf War-relevant organophosphate exposure. Propranolol treatment abrogated the neuroinflammation instigated in our model specifically, having no treatment effects in non-DFP exposed groups. Our results indicate that propranolol may be a promising therapy for GWI by treating the underlying neuroinflammation associated with Gulf War-relevant physiological stress and organophosphate exposures.",
+            "title": "The \u03b2-adrenergic receptor blocker and anti-inflammatory drug propranolol mitigates brain cytokine expression in a long-term model of Gulf War Illness",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/eddk-effy/application/x-zip-compressed",
+                    "mediaType": "application/x-zip-compressed"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "National Institute for Occupational Safety and Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-02-23",
+            "temporal": "2000/2016",
+            "@type": "dcat:Dataset",
+            "modified": "2024-09-18",
+            "keyword": [
+                "american indian or alaska native",
+                "asian or pacific islander",
+                "births",
+                "black or african american",
+                "child and adolescent",
+                "health risk factors",
+                "health us",
+                "hispanic or latino",
+                "state",
+                "white"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:healthus@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/dj4t-wmry",
+            "description": "Data on Low birthweight live births, by race and Hispanic origin of mother, state, and territory in the United States and U.S. dependent areas. Data are from Health, United States. SOURCE: National Center for Health Statistics, National Vital Statistics System, Birth File.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
+            "title": "DQS Low birthweight live births, by race and Hispanic origin of mother, state, and territory: United States and U.S. dependent areas",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dj4t-wmry/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dj4t-wmry/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dj4t-wmry/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dj4t-wmry/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Annual",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/dataset/panel-study-income-dynamics-psid",
+            "bureauCode": [
+                "001:05"
+            ],
+            "issued": "2014-04-08",
+            "temporal": "1968-01-01T00:00:00-05:00/1968-01-01T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "adulthood",
+                "aging",
+                "cohort",
+                "education",
+                "employment",
+                "epidemiology",
+                "event",
+                "expenditures",
+                "health",
+                "income",
+                "interview",
+                "longitudinal",
+                "marriage",
+                "panel",
+                "population statistics",
+                "sexual assault",
+                "transitions",
+                "wealth"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Panel Study of Income Dynamics Help",
+                "hasEmail": "mailto:psidhelp@umich.edu"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH), Department of Health & Human Services"
+            },
+            "identifier": "b2a0bdee-117e-48e5-ad0c-f9982e05281a",
+            "description": "<p>The Panel Study of Income Dynamics (PSID) began in 1968 with a nationally representative sample of over 18,000 individuals living in 5,000 families in the United States. Information on these individuals and their descendants has been collected continuously, including data covering employment, income, wealth, expenditures, health, marriage, childbearing, child development, philanthropy, education, and numerous other topics.</p>",
+            "title": "The Panel Study of Income Dynamics (PSID)",
+            "programCode": [
+                "009:048"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://psidonline.isr.umich.edu/Studies.aspx",
+                    "mediaType": "text/html",
+                    "title": "Text "
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://simba.isr.umich.edu/default.aspx",
+                    "mediaType": "text/html",
+                    "title": "Text "
+                }
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/47ru-cshp",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2020-09-21",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-04",
+            "keyword": [
+                "chemicals",
+                "chemistry",
+                "dataset"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Library of Medicine",
+                "hasEmail": "mailto:custserv@nlm.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/47ru-cshp",
+            "description": "ChemIDplus, the Chemical Identification Plus Database, is no longer updated. These are the final files from February 22, 2023. All ChemIDplus data have been incorporated into PubChem.\n\nChemIDplus was a dictionary of over 400,000 chemicals (names, synonyms, and structures). ChemIDplus includes links to NLM and other databases and resources, including links to federal, state and international agencies.  NLM makes a subset of ChemIDplus data available for download. The ChemIDplus Subset does not include the structure or the toxicity data available from the NLM web versions of the database. The ChemIDplus Subset is updated monthly.",
+            "title": "ChemIDplus",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/chemidlease/",
+                    "description": "ChemIDplus is no longer updated. These are the final files from February 22, 2023. All ChemIDplus data have been incorporated into PubChem. ",
+                    "@type": "dcat:Distribution",
+                    "title": "Download ChemIDplus Subset Data"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/sample/chemid/",
+                    "mediaType": "text/html",
+                    "title": "Download ChemIDplus Sample Data"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Drugs and Chemicals"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/e9r5-5hjr",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2015-08-10",
+            "@type": "dcat:Dataset",
+            "modified": "2015-08-27",
+            "keyword": [
+                "americas",
+                "chikungunya",
+                "paho"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/e9r5-5hjr",
+            "description": "Derived from Pan American Health Organization reports: http://www.paho.org/hq/index.php?option=com_topics&view=article&id=343&Itemid=40931",
+            "title": "New Chikungunya Cases Reported in the Americas",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/e9r5-5hjr/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/e9r5-5hjr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/e9r5-5hjr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/e9r5-5hjr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Health Statistics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/pqz3-as22",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2024-11-20",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-15",
+            "references": [
+                "https://www.mathematica.org/"
+            ],
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "be70cb98-52f4-5254-8fe9-f8dcb34f5f45",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "CoreSEt filters v2.10.23 (coreset-prod)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.23/20241029/filters.csv",
+                    "description": "CoreSEt filters v2.10.23 (coreset-prod)",
+                    "@type": "dcat:Distribution",
+                    "title": "CoreSEt filters v2.10.23 (coreset-prod)"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/psa5-qby7",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-10-08",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-15",
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
+            ],
+            "keyword": [
+                "dqatlas",
+                "dqatlas_devauto",
+                "utility"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DataConnect Support Team",
+                "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "fe72018c-0f13-5f58-b58b-20bf988645bc",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "devAuto_concernLevel",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/concernLevel.csv",
+                    "description": "{\"dataset\": \"concernLevel\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "@type": "dcat:Distribution",
+                    "title": "concernLevel csv file"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/PT1S",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/psgy-3uyv",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-03-27",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-06",
+            "keyword": [
+                "medicaid"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Chris Vaughn",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "1b03ec9b-07dd-4547-99a5-aacf206162d5",
+            "description": "Notes:\r\n1. CAA 2023 provides a temporary 5.0 percentage point FMAP increase to each qualifying state and territory's FMAP under section 1905(b) of the Act, beginning April 1, 2023 through June 30, 2023.\t\t\t\t\t\t\t\r\n2. CAA 2023 provides a temporary 2.5 percentage point FMAP increase to each qualifying state and territory's FMAP under section 1905(b) of the Act, beginning July 1, 2023 through September 30, 2023.\t\t\t\t\t\t\t\r\n3. CAA 2023 provides a temporary 1.5 percentage point FMAP increase to each qualifying state and territory's FMAP under section 1905(b) of the Act, beginning October 1, 2023 through December 31, 2023.\t\t\t\t\t\t\t\r\n4. States that have reported \u201c0\u201d either have no expenditures for that reporting category or have not yet reported expenditures for that category. \t\t\t\t\t\t\t\r\n5. This report is a cumulative summary report that includes current and prior period adjustment expenditures that apply to this quarter and does not include Collections or Overpayment Recoveries.",
+            "title": "Medicaid CMS-64 CAA 2023 Increased FMAP Expenditure Data Collected through MBES/CBES",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/Medicaid-CMS-64-CAA-2023-Increased-FMAP-Expenditure-Data-Collected-through-MBES-CBES-01062025.csv",
+                    "mediaType": "text/csv",
+                    "title": "CSV"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/psqj-8ru8",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-08-09",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-16",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "py2023",
+                "rate"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Center for Consumer Information and Insurance Oversight",
+                "hasEmail": "mailto:CMS_FEPS@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "identifier": "e6deb20e-dd27-495b-8eb1-c67db7bbd788",
+            "description": "The Rate PUF (Rate-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The Rate-PUF contains plan-level data on rates based on an eligible subscriber\u2019s age, tobacco use, and geographic location; and family-tier rates.",
+            "title": "Rate PUF \u2013 PY2023",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2023/rate_puf.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.datasetcatalog.nlm.nih.gov/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2024-11-04",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-04",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Library of Medicine",
+                "hasEmail": "mailto:custserv@nlm.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/k6qs-qncs",
+            "description": "The Dataset Catalog (beta)is a catalog of biomedical datasets from various repositories for users to search, discover, retrieve, and connect with datasets to accelerate scientific research. This beta version aims to collect user feedback to inform future product development.",
+            "title": "Dataset Catalog (beta)",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.datasetcatalog.nlm.nih.gov/",
+                    "mediaType": "text/html",
+                    "title": "Dataset Catalog (beta) Homepage and Search"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Research"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/covidvaxview/interactive/children-coverage-vaccination.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-11-07",
+            "@type": "dcat:Dataset",
+            "temporal": "2023-2024",
+            "modified": "2024-08-28",
+            "keyword": [
+                "covid-19 vaccination",
+                "nis-ccm"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VaxView Team",
+                "hasEmail": "mailto:VaxView@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/ithv-4e9m",
+            "description": "\u2022 COVID-19 vaccination coverage and parental intent among children 6 months to 17 years is assessed through the National Immunization Survey providing weekly COVID-19 vaccination coverage estimates (https://www.cdc.gov/vaccines/imz-managers/nis/about.html). \n\n\u2022 Weekly estimates of COVID-19 vaccination coverage and parental intent for vaccination among children through December 31, 2023, were calculated using data from the National Immunization Survey-Child COVID Module (NIS-CCM). Beginning January 2, 2024, the NIS-CCM was discontinued, and questions regarding receipt of COVID-19 vaccination among children were added to the NIS-Flu (https://www.cdc.gov/vaccines/imz-managers/nis/about.html#nis-cim). \n\n\u2022 Starting in September 2023, the CDC recommended the 2023-2024 updated COVID-19 vaccine to protect against serious illness from COVID-19.",
+            "title": "Weekly Parental Intent for Vaccination and Cumulative Percentage of Children 6 Months-17 Years who are up to date with the updated 2023-24 COVID-19 Vaccine",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ithv-4e9m/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ithv-4e9m/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ithv-4e9m/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ithv-4e9m/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States- National, Region, State",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Weekly",
+            "theme": [
+                "Child Vaccinations"
+            ],
+            "language": [
+                "English"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://aspe.hhs.gov/pdf-report/vaccine-hesitancy",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2021-05-17",
+            "@type": "dcat:Dataset",
+            "modified": "2021-06-17",
+            "keyword": [
+                "coronavirus",
+                "covid-19",
+                "vaccine hesitancy"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "HHS",
+                "hasEmail": "mailto:joel.ruhter@hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/q9mh-h2tw",
+            "description": "Due to the change in the survey instrument regarding intention to vaccinate, our estimates for \u201chesitant or unsure\u201d or \u201chesitant\u201d derived from April 14-26, 2021, are not directly comparable with prior Household Pulse Survey data and should not be used to examine trends in hesitancy.\n\nTo support state and local communication and outreach efforts, ASPE developed state, county, and sub-state level predictions of hesitancy rates (https://aspe.hhs.gov/pdf-report/vaccine-hesitancy) using the most recently available federal survey data.\n\nWe estimate hesitancy rates at the state level using the U.S. Census Bureau\u2019s Household Pulse Survey (HPS) (https://www.census.gov/programs-surveys/household-pulse-survey.html) data and utilize the estimated values to predict hesitancy rates at the Public Use Microdata Areas (PUMA) level using the Census Bureau\u2019s 2019 American Community Survey (ACS) 1-year Public Use Microdata Sample (PUMS)(https://www.census.gov/programs-surveys/acs/microdata.html). To create county-level estimates, we used a PUMA-to-county crosswalk from the Missouri Census Data Center(https://mcdc.missouri.edu/applications/geocorr2014.html). PUMAs spanning multiple counties had their estimates apportioned across those counties based on overall 2010 Census populations.\n\nThe HPS is nationally representative and includes information on U.S. residents\u2019 intentions to receive the COVID-19 vaccine when available, as well as other sociodemographic and geographic (state, region and metropolitan statistical areas) information. The ACS is a nationally representative survey, and it provides key sociodemographic and geographic (state, region, PUMAs, county) information. We utilized data for the survey collection period May 26, 2021 \u2013 June 7, 2021, which the HPS refers to as Week 31..\n\nPUMA COVID-19 Hesitancy Data - https://data.cdc.gov/Vaccinations/Vaccine-Hesitancy-for-COVID-19-Public-Use-Microdat/djj9-kh3p",
+            "title": "Vaccine Hesitancy for COVID-19: County and local estimates",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/q9mh-h2tw/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/q9mh-h2tw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/q9mh-h2tw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/q9mh-h2tw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "theme": [
+                "Vaccinations"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2019-12-05",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-25",
+            "references": [
+                "https://academic.oup.com/aje/article/179/8/1025/109078",
+                "https://academic.oup.com/aje/article/182/2/127/93984",
+                "https://www.cdc.gov/pcd/issues/2017/17_0281.htm",
+                "https://www.cdc.gov/pcd/issues/2018/18_0313.htm"
+            ],
+            "keyword": [
+                "500cities",
+                "behaviors",
+                "census",
+                "cities",
+                "gis",
+                "outcomes",
+                "prevalence",
+                "prevention",
+                "tract",
+                "unhealthy"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "500 Cities Public Inquiries",
+                "hasEmail": "mailto:places@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/pf7q-w24q",
+            "description": "2016, 2015. Data were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. 500 cities project city-level data in GIS-friendly format can be joined with city spatial data (https://chronicdata.cdc.gov/500-Cities/500-Cities-City-Boundaries/n44h-hy2j) in a geographic information system (GIS) to produce maps of 27 measures at the city-level. There are 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, cholesterol screening) in this 2018 release from the 2015 BRFSS that were the same as the 2017 release.",
+            "title": "500 Cities: City-level Data (GIS Friendly Format), 2018 release",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pf7q-w24q/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pf7q-w24q/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pf7q-w24q/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pf7q-w24q/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "500 Cities & Places"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/pvu5-a2vy",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-08-09",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-16",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "network",
+                "py2023"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Center for Consumer Information and Insurance Oversight",
+                "hasEmail": "mailto:CMS_FEPS@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "identifier": "e164fcba-c5fb-4d81-97a9-882e98a69325",
+            "description": "The Network PUF (Ntwrk-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The Ntwrk-PUF contains issuer-level data identifying provider network URLs.",
+            "title": "Network PUF - PY2023",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2023/network_puf.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/dataset/custodial-parents-living-poverty",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2014-02-10",
+            "temporal": "2011-01-01T00:00:00-05:00/2011-01-01T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "administrative",
+                "arrears management",
+                "case management",
+                "children's health",
+                "child support fact sheet",
+                "economic stability",
+                "iv-d program",
+                "job services",
+                "other",
+                "poverty",
+                "promising practices",
+                "state local child support agencies",
+                "story behind the numbers",
+                "us census bureau"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Dennis Putze",
+                "hasEmail": "mailto:dennis.putze@acf.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Administration for Children and Families, Department of Health & Human Services"
+            },
+            "identifier": "65f41ddb-094b-4181-a85a-ce55a945312e",
+            "description": "<p>Office of Child Support Enforecment (OCSE) Story Behind the Numbers - Child Support Fact Sheet #3.  This fact sheet focuses on data reported in a recent U.S. Census Bureau report, Custodial Mothers and Fathers and Their Child Support: 2011. The data reported are estimated based on a biennial survey of custodial parents, the Child Support Supplement to the Current Population Survey, March/April 2012, co-sponsored by the Office of Child Support Enforcement.  The proportion of custodial parents living below poverty line continues to increase in 2011. The report found that 4.2 million custodial parents lived in poverty in 2011, representing 29 percent of all custodial parents, about twice the poverty rate for the total population. These statistics reinforce the essential role that child support services can play in helping low-income families, especially during an economic downturn.</p>",
+            "title": "Custodial Parents Living in Poverty",
+            "programCode": [
+                "009:103"
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "State"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/px3f-paf3",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-06-06",
+            "@type": "dcat:Dataset",
+            "modified": "2023-06-05",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "4fca2c9b-d0d2-4016-8e60-644f6d552a81",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-05-29-to-2023-06-04",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rprt-drug-5-29-2023-to-6-04-2023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-05-29-to-2023-06-04"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.ncbi.nlm.nih.gov/projects/genotyping/formpage.cgi",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-07-01",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "dataset",
+                "genomics",
+                "tools & utilities",
+                "virus"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Library of Medicine",
+                "hasEmail": "mailto:custserv@nlm.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ftac-bfk9",
+            "description": "This tool helps identify the genotype of a viral sequence.",
+            "title": "Viral Genotyping Tool",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/projects/genotyping/formpage.cgi",
+                    "mediaType": "text/html",
+                    "title": "Viral Genotyping Tool - Query Interface"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Molecular biology/Genetics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/py3k-6dws",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2015-06-11",
+            "@type": "dcat:Dataset",
+            "modified": "2024-06-11",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "602e7c79-774d-529a-a377-75faa749e878",
+            "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
+            "title": "State Drug Utilization Data 1994",
+            "programCode": [
+                "009:076"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/StateDrugUtilizationData1994.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P10Y",
+            "theme": [
+                "State Drug Utilization"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/rihk-iawc",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-04-26",
+            "@type": "dcat:Dataset",
+            "modified": "2019-05-30",
+            "keyword": [
+                "2019",
+                "nedss",
+                "netss",
+                "nndss",
+                "smallpox",
+                "spotted fever rickettsiosis confirmed",
+                "spotted fever rickettsiosis probable",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/rihk-iawc",
+            "description": "NNDSS - TABLE 1GG.  Spotted fever rickettsiosis, Confirmed to Smallpox - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1GG. Spotted fever rickettsiosis, Confirmed to Smallpox",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rihk-iawc/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rihk-iawc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rihk-iawc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rihk-iawc/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/pwgb-7r9t",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "Public access to full dataset except age.  For age, reach out to point of contact",
+            "issued": "2019-03-14",
+            "@type": "dcat:Dataset",
+            "temporal": "N/A",
+            "modified": "2019-03-14",
+            "keyword": [
+                "antibody",
+                "chlamydia trachomatis",
+                "division of parasitic diseases and malaria",
+                "latent class"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Ryan E. Wiegand",
+                "hasEmail": "mailto: fwk2@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/pwgb-7r9t",
+            "description": "This set includes data used in a latent class model to compare testing platforms for detection of antibodies against the Chlamydia trachomatis antigen Pgp3.  The analysis was published as: Latent class modeling to compare testing platforms for detection of antibodies against the Chlamydia trachomatis antigen Pgp3. Wiegand RE, Cooley G, Goodhew B, Banniettis N, Kohlhoff S, Gwyn S, Martin DL. Sci Rep. 2018 Mar 9;8(1):4232. doi: 10.1038/s41598-018-22708-9. PMID: 29523810",
+            "title": "Tests for antibodies to trachoma PGP3 antigen",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pwgb-7r9t/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pwgb-7r9t/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pwgb-7r9t/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pwgb-7r9t/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "samples from patients from Africa and New York",
+            "describedBy": "https://www.nature.com/articles/s41598-018-22708-9",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "n/a",
+            "theme": [
+                "Global Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-09-21",
+            "@type": "dcat:Dataset",
+            "modified": "2023-09-21",
+            "references": [
+                "https://wwwdev.cdc.gov/visionhealth/vehss/data/claims/medicaid.html",
+                "https://www.medicaid.gov/medicaid/index.html"
+            ],
+            "keyword": [
+                "claims",
+                "diagnosed prevalence",
+                "eye exams",
+                "max",
+                "medicaid",
+                "medical diagnoses",
+                "screening",
+                "service utilization"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DDT Public Inquiries",
+                "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/bwx3-gx66",
+            "description": "2016-2019. This dataset is a de-identified summary table of prevalence rates for vision and eye health data indicators from the Medicaid Analytic eXtract (MAX) data. Medicaid MAX are a set of de-identified person-level data files with information on Medicaid eligibility, service utilization, diagnoses, and payments. The MAX data contain a convenience sample of claims processed by Medicaid and Children\u2019s Health Insurance Program (CHIP) fee for service and managed care plans.  Not all states are included in MAX in all years, and as of November 2019, 2014 data is the latest available.  Prevalence estimates are stratified by all available combinations of age group, gender, and state.  Detailed information on VEHSS Medicare analyses can be found on the VEHSS Medicaid MAX webpage (cdc.gov/visionhealth/vehss/data/claims/medicaid.html). Information on available Medicare claims data can be found on the ResDac website (www.resdac.org). The VEHSS Medicaid MAX dataset was last updated May 2023.",
+            "title": "Medicaid Claims (MAX) - Vision and Eye Health Surveillance",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bwx3-gx66/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bwx3-gx66/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bwx3-gx66/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bwx3-gx66/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Vision-Eye-Health/Private-Medicaid-Claims-MAX-Vision-and-Eye-Health-/bwx3-gx66",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "theme": [
+                "Vision & Eye Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/7vnz-2mjz",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2017-01-05",
+            "@type": "dcat:Dataset",
+            "modified": "2017-01-05",
+            "keyword": [
+                "2016",
+                "hepatitis",
+                "hepatitis (viral acute)",
+                "hepatitis (viral acute) type a",
+                "hepatitis (viral acute) type b",
+                "hepatitis (viral acute) type c",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/7vnz-2mjz",
+            "description": "NNDSS - Table II. Hepatitis (viral, acute) - 2016. In this Table, provisional* cases of selected\u2020 notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed.  The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.  NP:  Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum.\r\n\r\n * Case counts for reporting year 2016 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \r\n \u2020 Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions.",
+            "title": "NNDSS - Table II. Hepatitis (viral, acute)",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7vnz-2mjz/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7vnz-2mjz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7vnz-2mjz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7vnz-2mjz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/pywq-su29",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-10-08",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-24",
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
+            ],
+            "keyword": [
+                "dqatlas",
+                "dqatlas_devauto",
+                "utility"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DataConnect Support Team",
+                "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "26a6154a-3e36-58bd-aef3-6bcc465687c0",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "devAuto_files_allDownloads",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20220921_v2_ETL_DEV/files_allDownloads.csv",
+                    "description": "{\"dataset\": \"files_allDownloads\", \"stage\": \"devAuto\", \"update_id\": \"20220921_v2_ETL_DEV\"}",
+                    "@type": "dcat:Distribution",
+                    "title": "files_allDownloads csv file"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/PT1S",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/68sm-zh95",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-01-21",
+            "@type": "dcat:Dataset",
+            "modified": "2022-01-12",
+            "keyword": [
+                "2021",
+                "cholera",
+                "coccidioidomycosis",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/68sm-zh95",
+            "description": "NNDSS - Table 1H. Cholera to Coccidioidomycosis - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - Table 1H. Cholera to Coccidioidomycosis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/68sm-zh95/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/68sm-zh95/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/68sm-zh95/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/68sm-zh95/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-inpatient-hospitals/medicare-inpatient-hospitals-by-geography-and-service",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2013-01-01/2022-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2024-06-04",
+            "references": [
+                "https://data.cms.gov/resources/medicare-inpatient-hospitals-methodology"
+            ],
+            "keyword": [
+                "health care use & payments",
+                "health equity",
+                "hospitals & facilities",
+                "inpatient",
+                "medicare",
+                "national",
+                "original medicare",
+                "states & territories"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicare Provider Data - OEDA",
+                "hasEmail": "mailto:IPAG_Data_Products@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/2941ab09-8cee-49d8-9703-f3c5b854e388/data-viewer",
+            "description": "The Medicare Inpatient Hospitals by Geography and Service dataset provides information on hospital discharges for Original Medicare Part A beneficiaries by IPPS\u00a0hospitals. This dataset\u00a0contains information on the number of discharges, payments, and submitted charges organized by geography and Medicare Severity Diagnosis Related Group (DRG).",
+            "title": "Medicare Inpatient Hospitals - by Geography and Service",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/2941ab09-8cee-49d8-9703-f3c5b854e388/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Medicare Inpatient Hospitals - by Geography and Service : 2022-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/a9f5e5e4-b214-4a3f-97f6-b4f3d7e34cfa/MUP_INP_RY24_P03_V10_DY22_Geo.CSV",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Inpatient Hospitals - by Geography and Service : 2022-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5c8b315f-a2a3-4b2f-bba6-7be19f8d7edc/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Inpatient Hospitals - by Geography and Service : 2022-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/ee35f629-d386-426e-b51e-70451cf896d2/MUP_IHP_RY23_P03_V10_DY21_GEO.CSV",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Inpatient Hospitals - by Geography and Service : 2021-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/68739613-1a4f-40ae-9664-49da07abd81f/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Inpatient Hospitals - by Geography and Service : 2021-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/ef9ecf4c-ad7c-4112-881e-ccb9a83acb1c/MUP_IHP_RY23_P03_V10_DY20_GEO.CSV",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Inpatient Hospitals - by Geography and Service : 2020-12-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e583de38-33d7-4895-a115-0d8af74f0795/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Inpatient Hospitals - by Geography and Service : 2020-12-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/f07177de-e932-4b1a-a754-eac7bdfc4b28/MUP_IHP_RY23_P03_V10_DY19_GEO.CSV",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Inpatient Hospitals - by Geography and Service : 2019-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/337617e5-c18b-4cb9-8152-34851747584b/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Inpatient Hospitals - by Geography and Service : 2019-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/9c685ed4-a63c-4d22-9027-f225ce631c56/MUP_IHP_RY23_P03_V10_DY18_GEO.CSV",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Inpatient Hospitals - by Geography and Service : 2018-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/25b5b6c9-977d-4f7a-aaa7-7dde72f3d5cc/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Inpatient Hospitals - by Geography and Service : 2018-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/997006a4-cc2b-48ed-8b59-4c7ed6d2833f/MUP_IHP_RY23_P03_V10_DY17_GEO.CSV",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Inpatient Hospitals - by Geography and Service : 2017-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7c638c5f-7e8c-4346-8a25-9b37a0ed36dd/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Inpatient Hospitals - by Geography and Service : 2017-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/37a92da8-fe11-4f52-b96c-04211cfafb2a/MUP_IHP_RY23_P03_V10_DY16_GEO.CSV",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Inpatient Hospitals - by Geography and Service : 2016-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/81dca731-b739-4a0a-b2ec-555f6cf04ea6/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Inpatient Hospitals - by Geography and Service : 2016-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/b3cb61a4-7b3f-4508-ba0c-a3ffe3a1001e/MUP_IHP_RY23_P03_V10_DY15_GEO.CSV",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Inpatient Hospitals - by Geography and Service : 2015-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/98069693-d269-46a1-8e7e-f360f37a2031/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Inpatient Hospitals - by Geography and Service : 2015-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/8938c5bd-da0f-4810-b696-cdad9a6b7ed8/MUP_IHP_RY23_P03_V10_DY14_GEO.CSV",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Inpatient Hospitals - by Geography and Service : 2014-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/fe4fa35f-d27b-4bed-a14a-35528a870de0/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Inpatient Hospitals - by Geography and Service : 2014-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/dbee128c-28d2-4c64-b711-9c2528eed2f0/MUP_IHP_RY23_P03_V10_DY13_GEO.CSV",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Inpatient Hospitals - by Geography and Service : 2013-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c7019ecb-8f6f-4548-8eed-ee5bf35b51d5/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Inpatient Hospitals - by Geography and Service : 2013-12-31"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/medicare-inpatient-hospitals-by-geography-and-service-data-dictionary-0",
+            "dataQuality": true,
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "Medicare"
+            ],
+            "language": [
+                "en-US"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/q2v4-vdvf",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2024-11-06",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-06",
+            "references": [
+                "https://www.mathematica.org/"
+            ],
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "d605e8ea-553c-50b2-83ac-238f1734c257",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "CoreSEt version v2.10.14 (coreset-dev)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.14/20241029/version.csv",
+                    "description": "CoreSEt version v2.10.14 (coreset-dev)",
+                    "@type": "dcat:Distribution",
+                    "title": "CoreSEt version v2.10.14 (coreset-dev)"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.cdc.gov/tobacco/stateandcommunity/best_practices/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2015-01-28",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-30",
+            "keyword": [
+                "glossary",
+                "methodology"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "OSHData Support",
+                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/f8gx-sdye",
+            "description": "Download the latest version of the Glossary and Methodology File",
+            "title": "CDC Best Practices for Comprehensive Tobacco Control Programs - 2007 Glossary and Methodology",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/f8gx-sdye/application/vnd.ms-excel",
+                    "mediaType": "application/vnd.ms-excel"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Funding"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:20"
+            ],
+            "landingPage": "https://data.cdc.gov/d/gt5d-asw4",
+            "issued": "2023-09-01",
+            "@type": "dcat:Dataset",
+            "modified": "2023-09-01",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Test",
+                "hasEmail": "mailto:Test"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/gt5d-asw4",
+            "description": "",
+            "title": "SocrataDataRefresh_Test",
+            "programCode": [
+                "009:036"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gt5d-asw4/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gt5d-asw4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gt5d-asw4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gt5d-asw4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-sexually-transmitted-disease-std-morbidity",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2012-05-30",
+            "temporal": "1984-01-01T00:00:00-05:00/2008-12-31T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "age",
+                "case",
+                "epidemiology",
+                "ethnicity",
+                "guam",
+                "incidence",
+                "morbidity",
+                "puerto rico",
+                "race",
+                "sex",
+                "state",
+                "std",
+                "virgin islands",
+                "year"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
+            },
+            "identifier": "134d23cb-d5d0-45d0-8fa4-4313efb14183",
+            "description": "<p>The Sexually Transmitted Disease (STD) Morbidity online databases on CDC WONDER contain case reports reported from the 50 United States and D.C., Puerto Rico, Virgin Islands and Guam.   The online databases report  the number of cases and disease incidence rates by year, state, disease, age, gender of patient, type of STD, and area of report.  Data are produced by the U.S. Department of Health and Human Services, Public Health Service, Centers for Disease Control and Prevention (CDC), National Center for HIV/AIDS, viral Hepatitis, STD and TB Prevention (NCHHSTP).</p>",
+            "title": "CDC WONDER: Sexually Transmitted Disease (STD) Morbidity",
+            "programCode": [
+                "009:027"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://wonder.cdc.gov/std.html",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "describedBy": "http://wonder.cdc.gov/std.html",
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "State"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/q433-kijn",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2022-04-07",
+            "@type": "dcat:Dataset",
+            "modified": "2022-04-05",
+            "keyword": [
+                "medicaid"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "c5bd69ae-7c98-4787-beb6-cb347ebf329f",
+            "description": "test",
+            "title": "NADAC",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/national-average-drug-acquisition-cost-04-06-2022.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "restricted public",
+            "landingPage": "https://www.hcup-us.ahrq.gov/db/nation/neds/nedsdbdocumentation.jsp",
+            "bureauCode": [
+                "009:33"
+            ],
+            "rights": "N/A",
+            "issued": "2021-02-13",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "claims",
+                "diagnoses",
+                "emergency department",
+                "epidemiology",
+                "hcup",
+                "health care",
+                "health care cost",
+                "health care providers",
+                "health statistics",
+                "hospital",
+                "inpatient",
+                "procedures",
+                "sexual assault",
+                "utilization"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "HCUP Technical Support",
+                "hasEmail": "mailto:hcup@ahrq.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Agency for Healthcare Research and Quality, Department of Health & Human Services"
+            },
+            "identifier": "26887d97-e5da-4b40-893d-0cb9bebf1948",
+            "description": "The Healthcare Cost and Utilization Project (HCUP) Nationwide Emergency Department Sample (NEDS) is the largest all-payer emergency department (ED) database in the United States. yielding national estimates of hospital-owned ED visits. Unweighted, it contains data from over 30 million ED visits each year. Weighted, it estimates roughly 145 million ED visits nationally.  Developed through a Federal-State-Industry partnership sponsored by the Agency for Healthcare Research and Quality, HCUP data inform decision making at the national, State, and community levels.\n\nSampled from the HCUP State Inpatient Databases (SID) and State Emergency Department Databases (SEDD), the HCUP NEDS can be used to create national and regional estimates of ED care. The SID contain information on patients initially seen in the ED and subsequently admitted to the same hospital. The SEDD capture information on ED visits that do not result in an admission (i.e., treat-and-release visits and transfers to another hospital). Developed through a Federal-State-Industry partnership sponsored by the Agency for Healthcare Research and Quality, HCUP data inform decision making at the national, State, and community levels. \n\nThe NEDS contain information about geographic characteristics, hospital characteristics, patient characteristics, and the nature of visits (e.g., common reasons for ED visits, including injuries). The NEDS contains clinical and resource use information included in a typical discharge abstract, with safeguards to protect the privacy of individual patients, physicians, and hospitals (as required by data sources). It includes ED charge information for over 85% of patients, regardless of expected payer, including but not limited to Medicare, Medicaid, private insurance, self-pay, or those billed as \u2018no charge\u2019. The NEDS excludes data elements that could directly or indirectly identify individuals, hospitals, or states.Restricted access data files are available with a data use agreement and brief online security training.",
+            "title": "HCUP Nationwide Emergency Department Database (NEDS) Restricted Access File",
+            "programCode": [
+                "009:037"
+            ],
+            "describedBy": "https://www.hcup-us.ahrq.gov/db/nation/neds/nedsdbdocumentation.jsp",
+            "license": "https://www.distributor.hcup-us.ahrq.gov/Home.asp"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/dataset/occ-administrative-data",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2012-08-01",
+            "temporal": "2009-01-01T00:00:00-05:00/2010-01-01T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "administrative",
+                "children families child care",
+                "other"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Administration for Children and Families, Department of Health & Human Services"
+            },
+            "identifier": "803d680c-e91c-4347-b91b-c24051b8a7c5",
+            "description": "<p>Characteristics of families and children served by Child Care and Development Fund (CCDF)</p>",
+            "title": "OCC Administrative Data",
+            "programCode": [
+                "009:015"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.acf.hhs.gov/occ/data-0",
+                    "mediaType": "text/html",
+                    "title": "XLS "
+                }
+            ],
+            "describedBy": "http://www.acf.hhs.gov/programs/occ/resource/current-technical-bulletins",
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/mpdg-hf57",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2016-01-07",
+            "@type": "dcat:Dataset",
+            "modified": "2016-01-07",
+            "keyword": [
+                "2015",
+                "giardiasis",
+                "gonorrhea",
+                "haemophilus influenzae",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/mpdg-hf57",
+            "description": "NNDSS - Table II. Giardiasis to Haemophilus influenza - 2015.In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP: Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table 2 to facilitate case count verification with reporting jurisdictions. \ufffd\ufffd\ufffd Case counts for reporting year 2015 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \ufffd\ufffd Data for H. influenzae (age <5 years for serotype b, nonserotype b, and unknown serotype) are available in Table I.",
+            "title": "NNDSS - Table II. Giardiasis to Haemophilus influenza",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mpdg-hf57/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mpdg-hf57/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mpdg-hf57/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mpdg-hf57/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/rsvvaxview/adults-60-coverage-intent.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-11-07",
+            "@type": "dcat:Dataset",
+            "temporal": "2023-2024",
+            "modified": "2024-08-28",
+            "keyword": [
+                "nis-acm",
+                "older adults",
+                "rsv",
+                "vaccination"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VaxView Team",
+                "hasEmail": "mailto:VaxView@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/gzbv-dn9g",
+            "description": "Weekly Intent for Vaccination and Cumulative Percentage of Adults 60 Years and Older Vaccinated with RSV Vaccine.\n\n \u2022 RSV vaccination coverage among adults ages 60 years and older is assessed through the National Immunization Survey-Adult COVID Module providing weekly RSV vaccination coverage estimates. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html)\n\n \u2022 The CDC recommended the RSV vaccine for adults ages 60 years and older in July 2023. (https://www.cdc.gov/respiratory-viruses/whats-new/rsv-update-2023-09-22.html)",
+            "title": "Weekly Intent for Vaccination and Cumulative Percentage of Adults 60 Years and Older Vaccinated with RSV Vaccine",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gzbv-dn9g/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gzbv-dn9g/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gzbv-dn9g/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gzbv-dn9g/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States- National, Region, State",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Weekly",
+            "theme": [
+                "Vaccinations"
+            ],
+            "language": [
+                "English"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/rural-health-clinic-enrollments",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-12-08",
+            "temporal": "2023-10-01/2025-03-31",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-15",
+            "references": [
+                "https://data.cms.gov/sites/default/files/2024-10/RHC_Data_Guidance.pdf"
+            ],
+            "keyword": [
+                "hospitals & facilities",
+                "medicare",
+                "outpatient facilities",
+                "provider enrollment",
+                "rural health clinics"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Provider Enrollment Data Requests - CPI",
+                "hasEmail": "mailto:ProviderEnrollmentDataRequests@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/3b7e7659-067e-41ea-8e36-f9ee2036e1f6/data-viewer",
+            "description": "The Rural Health Clinic (RHC) Enrollments dataset provides enrollment information on all RHCs currently enrolled in Medicare. This data includes information on the RHC's legal business name, doing business as name, organization type and address.",
+            "title": "Rural Health Clinic Enrollments",
+            "describedByType": "application/pdf",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3b7e7659-067e-41ea-8e36-f9ee2036e1f6/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Rural Health Clinic Enrollments : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/31a07f52-068f-4849-8731-aa0216554368/RHC_Enrollments_2025.01.02.csv",
+                    "mediaType": "text/csv",
+                    "title": "Rural Health Clinic Enrollments : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7463bb3b-982b-4bb1-bdc6-08a1b36ebef2/data",
+                    "mediaType": "text/html",
+                    "title": "Rural Health Clinic Enrollments : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/97515b69-4566-485f-874a-5df558f55dfd/RHC_Enrollments_2024.10.07.csv",
+                    "mediaType": "text/csv",
+                    "title": "Rural Health Clinic Enrollments : 2024-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/aeb0958f-bbcb-4bce-8a20-76cb391dc28d/data",
+                    "mediaType": "text/html",
+                    "title": "Rural Health Clinic Enrollments : 2024-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/6e8e5e99-83b4-492a-b311-7ff4ea26cee6/RHC_Enrollments_2024.07.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Rural Health Clinic Enrollments : 2024-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/2d494295-420b-4f87-834e-58581e6e450a/data",
+                    "mediaType": "text/html",
+                    "title": "Rural Health Clinic Enrollments : 2024-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/86db0c45-b9c0-4d45-99ca-67e83aa5e1ce/RHC_Enrollments_2024.04.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Rural Health Clinic Enrollments : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/14466fc0-d153-4c7b-9093-ba5a24f7cced/data",
+                    "mediaType": "text/html",
+                    "title": "Rural Health Clinic Enrollments : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/f0cb1556-086f-4301-819a-595c07b0f3d4/RHC_Enrollments_2024.01.05.csv",
+                    "mediaType": "text/csv",
+                    "title": "Rural Health Clinic Enrollments : 2024-01-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e6a724bc-b95d-45e4-b50e-06ed1946d4f9/data",
+                    "mediaType": "text/html",
+                    "title": "Rural Health Clinic Enrollments : 2024-01-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/c62d5919-7f31-4a6a-8c91-db14108d9209/RHC_Enrollments_2023.11.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Rural Health Clinic Enrollments : 2023-10-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/aa3b55ce-363b-461b-adda-9023797512ed/data",
+                    "mediaType": "text/html",
+                    "title": "Rural Health Clinic Enrollments : 2023-10-29"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/sites/default/files/2023-09/RHC_Enrollments_Data_Dictionary.pdf",
+            "dataQuality": true,
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P3M",
+            "theme": [
+                "Medicare"
+            ],
+            "language": [
+                "en-US"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/9gny-cbhc",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-04-24",
+            "@type": "dcat:Dataset",
+            "modified": "2020-01-02",
+            "keyword": [
+                "2019",
+                "arboviral diseases",
+                "jamestown canyon virus disease",
+                "la crosse virus disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "powassan virus disease",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/9gny-cbhc",
+            "description": "NNDSS - Table 1B. Arboviral diseases, neuroinvasive and non-neuroinvasive, Jamestown Canyon virus disease to Powassan virus disease - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - Table 1B. Arboviral diseases, neuroinvasive and non-neuroinvasive, Jamestown Canyon virus disease to Powassan virus disease",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9gny-cbhc/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9gny-cbhc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9gny-cbhc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9gny-cbhc/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/xdg2-nh8n",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2016-01-20",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-27",
+            "keyword": [
+                "casinos",
+                "fact sheet",
+                "gaming",
+                "infographic",
+                "secondhand smoke",
+                "smokefree"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "OSHData Support",
+                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/xdg2-nh8n",
+            "description": "Explore the Going Smokefree Matters - Casinos Infographic which outlines key facts related to the effects of secondhand smoke exposure in casinos.",
+            "title": "Going Smokefree Matters - Casinos Infographic",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/xdg2-nh8n/application/pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Policy"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/healthy_people/hp2020/progress-tables.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-01-22",
+            "@type": "dcat:Dataset",
+            "temporal": "1988-01-01/2019-12-31",
+            "modified": "2023-08-23",
+            "keyword": [
+                "healthy people 2020"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/x749-vh2i",
+            "description": "[1] Status is determined using the baseline, final, and target value. The statuses used in Healthy People 2020 were: \n\n1 - Target met or exceeded\u2014One of the following applies: (i) At baseline, the target was not met or exceeded, and the most recent value was equal to or exceeded the target. (The percentage of targeted change achieved was equal to or greater than 100%.); (ii) The baseline and most recent values were equal to or exceeded the target. (The percentage of targeted change achieved was not assessed.) \n\n2 - Improved\u2014One of the following applies: (i) Movement was toward the target, standard errors were available, and the percentage of targeted change achieved was statistically significant; (ii) Movement was toward the target, standard errors were not available, and the objective had achieved 10% or more of the targeted change.\n\n3 - Little or no detectable change\u2014One of the following applies: (i) Movement was toward the target, standard errors were available, and the percentage of targeted change achieved was not statistically significant; (ii) Movement was toward the target, standard errors were not available, and the objective had achieved less than 10% of the targeted change; (iii) Movement was away from the baseline and target, standard errors were available, and the percent change relative to the baseline was not statistically significant; (iv) Movement was away from the baseline and target, standard errors were not available, and the objective had moved less than 10% relative to the baseline; (v) No change was observed between the baseline and the final data point.\n\n4 - Got worse\u2014One of the following applies: (i) Movement was away from the baseline and target, standard errors were available, and the percent change relative to the baseline was statistically significant; (ii) Movement was away from the baseline and target, standard errors were not available, and the objective had moved 10% or more relative to the baseline.\n\n5 - Baseline only\u2014The objective only had one data point, so progress toward target attainment could not be assessed. Note that if additional data points did not meet the criteria for statistical reliability, data quality, or confidentiality, the objective was categorized as baseline only. \n\n6 - Informational\u2014A target was not set for this objective, so progress toward target attainment could not be assessed.\n\n\n[2] The final value is generally based on data available on the Healthy People 2020 website as of January 2020. For objectives that are continuing into Healthy People 2030, more recent data are available on the Healthy People 2030 website: https://health.gov/healthypeople. \n\n\n[3] For objectives that moved toward their targets, movement toward the target was measured as the percentage of targeted change achieved (unless the target was already met or exceeded at baseline): \n\nPercentage of targeted change achieved = (Final value - Baseline value) / (HP2020 target - Baseline value) * 100\n\n\n[4] For objectives that were not improving, did not meet or exceed their targets, and did not move towards their targets, movement away from the baseline was measured as the magnitude of the percent change from baseline: \n\nMagnitude of percent change from baseline = |Final value - Baseline value| / Baseline value * 100\n\n\n[5] Statistical significance was tested when the objective had a target, at least two data points (of unequal value), and available standard errors of the data. A normal distribution was assumed. All available digits were used to test statistical significance. Statistical significance of the percentage of targeted change achieved or the magnitude of the percentage change from baseline was assessed at the 0.05 level using a normal one-sided test. \n\n\n[6] For more information on the Healthy People 2020 methodology for measuring progress toward target attainment and the elimination of health disparities, see: Healthy People Statistical Notes, no 27; available from: https://www.cdc.gov/nchs/data/sta",
+            "title": "Healthy People 2020 Final Progress Table",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/x749-vh2i/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/x749-vh2i/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/x749-vh2i/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/x749-vh2i/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "US",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "irregular",
+            "theme": [
+                "NCHS"
+            ],
+            "language": [
+                "en-US"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/fuzh-wm4c",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-04-24",
+            "@type": "dcat:Dataset",
+            "modified": "2020-01-02",
+            "keyword": [
+                "2019",
+                "nedss",
+                "netss",
+                "nndss",
+                "salmonella paratyphi infection",
+                "salmonella typhi infection",
+                "salmonellosis (excluding salmonella typhi infection and salmonella paratyphi infection)",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/fuzh-wm4c",
+            "description": "NNDSS - TABLE 1EE. Salmonella Paratyphi infection to Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection) - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 In previous years, cases were reported as Salmonellosis. Beginning in January 2019, cases began to be reported as Salmonella Paratyphi infection.\r\n\u00b6 In previous years, cases were reported as typhoid fever. Beginning in January 2019, cases began to be reported as Salmonella Typhi infection.\r\n** In previous years, cases were reported as Salmonellosis (excluding paratyphoid fever and typhoid fever). Beginning in January 2019, cases began to be reported as Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection).",
+            "title": "NNDSS - TABLE 1EE. Salmonella Paratyphi infection to Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection)",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fuzh-wm4c/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fuzh-wm4c/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fuzh-wm4c/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fuzh-wm4c/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/nhis/index.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "The NHIS website features downloadable annual data and documentation, information about any modifications or updates to the data or documentation, and published reports (https://www.cdc.gov/nchs/nhis/index.htm). NHIS is protected by Federal confidentiality laws that state the data collected by NCHS may be used only for statistical reporting and analysis. Some NHIS survey measures have been suppressed or edited in the downloadable public use files to protect confidentiality. Analysts interested in working with data that were suppressed or edited may apply to access selected unmodified data through the NCHS Research Data Center at https://www.cdc.gov/rdc/. For information about variables that are available in the public use files, see the annual Codebook. For information about restricted variables available through the RDC, see the Codebook for Restricted-use variables. In addition, the appendix of the annual Survey Description Document (SDD) includes a list of questionnaire variables that were recoded, suppressed, or are not available.",
+            "issued": "2023-06-28",
+            "@type": "dcat:Dataset",
+            "temporal": "2019\u20132023",
+            "modified": "2024-08-06",
+            "references": [
+                "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NHIS/2019/srvydesc-508.pdf",
+                "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NHIS/2020/srvydesc-508.pdf",
+                "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NHIS/2021/srvydesc-508.pdf",
+                "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NHIS/2022/srvydesc-508.pdf"
+            ],
+            "keyword": [
+                "access-to-health-care",
+                "civic-participation",
+                "crime-violence",
+                "discrimination",
+                "early-childhood",
+                "employment",
+                "environmental",
+                "food-insecurity",
+                "health-related behaviors",
+                "health status and conditions",
+                "higher-education",
+                "high-school",
+                "housing-stability",
+                "incarceration",
+                "language.",
+                "mental health",
+                "paradata",
+                "poverty-income",
+                "racism",
+                "research-data-center",
+                "social determinants of health (sdoh)",
+                "social-emotional",
+                "source-of-health-care",
+                "transportation",
+                "use-of-health-care",
+                "workplace"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:nhislist@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/8zhx-mf8r",
+            "description": "2019\u2013present. The National Health Interview Survey (NHIS) is a nationally representative household health survey of the U.S. civilian noninstitutionalized population. The NHIS data are used to monitor trends in illness and disability, track progress toward achieving national health objectives, for epidemiologic and policy analysis of various health problems, determining barriers to accessing and using appropriate health care, and evaluating Federal health programs. NHIS is conducted continuously throughout the year by the National Center for Health Statistics (NCHS). Public-use data files on adults and children with corresponding imputed income data files, and survey paradata are released annually. The NHIS data website (https://www.cdc.gov/nchs/nhis/data-questionnaires-documentation.htm) features the most up-to-date public-use data files and documentation for downloading including questionnaire, codebooks, CSV and ASCII data files, programs and sample code, and in-depth survey description. Most of the NHIS data are included in the public use files. NHIS is protected by Federal confidentiality laws that state the data collected by NCHS may be used only for statistical reporting and analysis. Some NHIS variables have been suppressed or edited in the public use files to protect confidentiality. Analysts interested in using data that has been suppressed or edited may apply for access through the NCHS Research Data Center at https://www.cdc.gov/rdc/. In 2019, NHIS launched a redesigned content and structure that differs from its previous questionnaire designs. NHIS has been conducted continuously since 1957.",
+            "title": "National Health Interview Survey",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/nchs/nhis/data-questionnaires-documentation.htm",
+                    "mediaType": "text/html",
+                    "title": "National Health Interview Survey"
+                }
+            ],
+            "spatial": "United States",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "NCHS"
+            ],
+            "language": [
+                "English"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/w7ew-4aqz",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-04-24",
+            "@type": "dcat:Dataset",
+            "modified": "2020-01-02",
+            "keyword": [
+                "2019",
+                "dengue",
+                "dengue-like illness",
+                "dengue virus infections",
+                "nedss",
+                "netss",
+                "nndss",
+                "severe dengue",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/w7ew-4aqz",
+            "description": "NNDSS - TABLE 1J. Dengue virus infections, Dengue to Severe dengue - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes: \r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 Includes data for dengue and dengue-like illness.",
+            "title": "NNDSS - TABLE 1J. Dengue virus infections, Dengue to Severe dengue",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/w7ew-4aqz/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/w7ew-4aqz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/w7ew-4aqz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/w7ew-4aqz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/q7jh-763c",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-08-06",
+            "@type": "dcat:Dataset",
+            "modified": "2024-08-14",
+            "keyword": [
+                "py2024",
+                "qhp landscape instructions",
+                "sadp",
+                "shop",
+                "shop market dental"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Center for Consumer Information and Insurance Oversight",
+                "hasEmail": "mailto:CMS_FEPS@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "identifier": "bcaea23a-7ece-4c8c-8e53-c1f10231eb95",
+            "description": "The Dental SHOP Market file of the QHP Landscape Files contains information on certified dental plans offered through an Exchange to employers in the Small Business Health Options Program (SHOP) market. These plans are also known as Stand-alone Dental Plans (SADPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
+            "title": "QHP Landscape Instructions PY2024 Dental SHOP",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2024/den-shop-lndscp-in.pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/6dep-qtzm",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-04-24",
+            "@type": "dcat:Dataset",
+            "modified": "2020-01-02",
+            "keyword": [
+                "2019",
+                "anaplasma phagocytophilum infection",
+                "ehrlichia chaffeensis infection",
+                "ehrlichiosis and anaplasmosis",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/6dep-qtzm",
+            "description": "NNDSS - Table 1K. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html \r\n\r\nFootnotes: \r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1K. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6dep-qtzm/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6dep-qtzm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6dep-qtzm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6dep-qtzm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/5p6r-d32s",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2016-09-14",
+            "@type": "dcat:Dataset",
+            "modified": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/5p6r-d32s",
+            "description": "Source: Behavioral Risk Factor Surveillance System (BRFSS), 2012, 2014.",
+            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days), 2012 & 2014, Region 5 - Chicago",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5p6r-d32s/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5p6r-d32s/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5p6r-d32s/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5p6r-d32s/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Motor Vehicle"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/mtc3-kq6r",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-10-01",
+            "@type": "dcat:Dataset",
+            "temporal": "2020-07-01/2021-12-14",
+            "modified": "2025-01-13",
+            "keyword": [
+                "coronavirus",
+                "covid",
+                "covid19",
+                "covid-19",
+                "laboratory",
+                "prevalence",
+                "sars-cov",
+                "seroprevalence",
+                "serosurveys"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC-INFO",
+                "hasEmail": "mailto:cdcinfo@cdcinquiry.onmicrosoft.com"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/mtc3-kq6r",
+            "description": "CDC is collaborating with the National Institutes of Health (NIH), the Food and Drug Administration (FDA), Vitalant Research Institute (VRI), Westat Inc., and numerous blood collection organizations across the United States to conduct a nationwide COVID-19 seroprevalence survey of blood donors. This is the largest nationwide COVID-19 seroprevalence survey to date. De-identified blood samples are tested for antibodies to SARS-CoV-2 to better understand the percentage of people in the United States who have antibodies against SARS-CoV-2 (the virus that causes COVID-19) and to track how this percentage changes over time. Both SARS-CoV-2 infection and COVID-19 vaccines currently used in the United States result in production of anti-spike (anti-S) antibodies but only infection results in production of anti-nucleocapsid (anti-N) antibodies. Infection-induced seroprevalence estimates the proportion of the population with evidence of previous SARS-CoV-2 infection and refers to the prevalence of the population with both anti-S and anti-N antibodies.\n\nThis link connects to a webpage that displays the data from the Nationwide Blood Donor Seroprevalence Survey. It offers an interactive visualization available at https://covid.cdc.gov/covid-data-tracker/#nationwide-blood-donor-seroprevalence\n\nAdditional information is available at: https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/blood-bank-serosurvey.html",
+            "title": "2020-2021 Nationwide Blood Donor Seroprevalence Survey Infection-Induced Seroprevalence Estimates",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mtc3-kq6r/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mtc3-kq6r/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mtc3-kq6r/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mtc3-kq6r/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "US",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Monthly",
+            "theme": [
+                "Laboratory Surveillance"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/q9ee-jubp",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-08-06",
+            "@type": "dcat:Dataset",
+            "modified": "2024-08-14",
+            "keyword": [
+                "py2024",
+                "qhp landscape",
+                "sadp",
+                "shop",
+                "shop market dental"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Center for Consumer Information and Insurance Oversight",
+                "hasEmail": "mailto:CMS_FEPS@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "identifier": "0e706798-a495-4121-b1b6-feb319e39726",
+            "description": "The Dental SHOP Market file of the QHP Landscape Files contains information on certified dental plans offered through an Exchange to employers in the Small Business Health Options Program (SHOP) market. These plans are also known as Stand-alone Dental Plans (SADPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
+            "title": "QHP Landscape PY2024 Dental SHOP",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2024/shop_market_dental.zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/vq7a-fvin",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-01-21",
+            "@type": "dcat:Dataset",
+            "modified": "2022-01-12",
+            "keyword": [
+                "2021",
+                "confirmed",
+                "nedss",
+                "netss",
+                "nndss",
+                "probable",
+                "vibriosis",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/vq7a-fvin",
+            "description": "NNDSS - TABLE 1LL. Vibriosis, Confirmed to Vibriosis, Probable \u2013 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data",
+            "title": "NNDSS - TABLE 1LL. Vibriosis, Confirmed to Vibriosis, Probable",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vq7a-fvin/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vq7a-fvin/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vq7a-fvin/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vq7a-fvin/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "restricted public",
+            "landingPage": "https://data.cdc.gov/d/gn5f-ec35",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "issued": "2022-06-15",
+            "@type": "dcat:Dataset",
+            "temporal": "2015",
+            "modified": "2023-04-20",
+            "keyword": [
+                "chronic conditions",
+                "food security",
+                "health behaviors",
+                "health insurance",
+                "o\tanxiety",
+                "physical activity",
+                "research-data-center"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/gn5f-ec35",
+            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional \nsurveys from probability-sampled commercial survey panels which began in 2015. \nRANDS 1 was administered by Gallup using the Gallup Panel in the fall of 2015 \nand contains existing questions from the National Health Interview Survey (NHIS).",
+            "title": "NCHS Research and Development Survey (RANDS) Round 1 Restricted File",
+            "describedByType": "application/pdf",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "spatial": "50 states and District of Columbia",
+            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS1_technical_documentation.pdf",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-10-11",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-25",
+            "references": [
+                "https://www.cdc.gov/places/measure-definitions/index.html"
+            ],
+            "keyword": [
+                "behaviors",
+                "city",
+                "gis",
+                "health",
+                "outcomes",
+                "place",
+                "places",
+                "prevalence",
+                "prevention",
+                "risk",
+                "status"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "PLACES Public Inquiries",
+                "hasEmail": "mailto:places@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/cj8b-94cj",
+            "description": "This dataset contains model-based place (incorporated and census designated places) level estimates for the PLACES 2021 release in GIS-friendly format. PLACES is the expansion of the original 500 Cities Project and covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code Tabulation Area (ZCTA) levels. It represents a first-of-its kind effort to release information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2019 or 2018 data, Census Bureau 2010 population estimates, and American Community Survey (ACS) 2015\u20132019 or 2014\u20132018 estimates. The 2021 release uses 2019 BRFSS data for 22 measures and 2018 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours a night). Seven measures are based on the 2018 BRFSS data because the relevant questions are only asked every other year in the BRFSS. These data can be joined with the 2019 Census TIGER/Line place boundary file in a GIS system to produce maps for 29 measures at the place level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software. https://cdcarcgis.maps.arcgis.com/home/item.html?id=024cf3f6f59e49fe8c70e0e5410fe3cf",
+            "title": "PLACES: Place Data (GIS Friendly Format), 2021 release",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cj8b-94cj/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cj8b-94cj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cj8b-94cj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cj8b-94cj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "500 Cities & Places"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-08-23",
+            "@type": "dcat:Dataset",
+            "modified": "2024-12-23",
+            "references": [
+                "https://www.cdc.gov/places/measure-definitions/index.html"
+            ],
+            "keyword": [
+                "behaviors",
+                "brfss",
+                "county",
+                "disability",
+                "health",
+                "outcomes",
+                "places",
+                "prevalence",
+                "prevention",
+                "risk",
+                "status"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "PLACES Public Inquiries",
+                "hasEmail": "mailto:places@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/swc5-untb",
+            "description": "This dataset contains model-based county estimates. PLACES covers the entire United States\u201450 states and the District of Columbia\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. This dataset includes estimates for 40 measures: 12 for health outcomes, 7 for preventive services use, 4 for chronic disease-related health risk behaviors, 7 for disabilities, 3 for health status, and 7 for health-related social needs. These estimates can be used to identify emerging health problems and to help develop and carry out effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2022 or 2021 data, Census Bureau 2022 county population estimate data, and American Community Survey 2018\u20132022 estimates. The 2024 release uses 2022 BRFSS data for 36 measures and 2021 BRFSS data for 4 measures (high blood pressure, high cholesterol, cholesterol screening, and taking medicine for high blood pressure control among those with high blood pressure) that the survey collects data on every other year. More information about the methodology can be found at www.cdc.gov/places.",
+            "title": "PLACES: Local Data for Better Health, County Data 2024 release",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/swc5-untb/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/swc5-untb/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/swc5-untb/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/swc5-untb/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "500 Cities & Places"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/wzwe-859x",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-01-14",
+            "@type": "dcat:Dataset",
+            "modified": "2022-02-11",
+            "keyword": [
+                "2022",
+                "ehrlichia ewingii infection",
+                "ehrlichiosis and anaplasmosis",
+                "giardiasis",
+                "nedss",
+                "netss",
+                "nndss",
+                "undetermined ehrlichiosis/anaplasmosis",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/wzwe-859x",
+            "description": "NNDSS - TABLE 1L. Ehrlichiosis and Anaplasmosis, Ehrlichia ewingii infection to Giardiasis - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
+            "title": "NNDSS - TABLE 1L. Ehrlichiosis and Anaplasmosis, Ehrlichia ewingii infection to Giardiasis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/wzwe-859x/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/wzwe-859x/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/wzwe-859x/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/wzwe-859x/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "restricted public",
+            "landingPage": "https://data.cdc.gov/d/g76d-z8vy",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "issued": "2022-06-15",
+            "@type": "dcat:Dataset",
+            "temporal": "2020",
+            "modified": "2023-04-24",
+            "keyword": [
+                "anxiety",
+                "covid-19",
+                "depression",
+                "missed healthcare",
+                "research-data-center",
+                "telemedicine"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/g76d-z8vy",
+            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys from probability-sampled commercial survey panels. As part of a special iteration of RANDS that focuses on COVID-19, RANDS during COVID-19 Round 2 is the second round of a three-round survey. The probability sample of RANDS during COVID-19 Round 2 was recruited using NORC at the University of Chicago (NORC)'s AmeriSpeak Panel, and the survey was administered by NORC from August 3, 2020 to August 20, 2020.  The RANDS during COVID-19 Round 2 Probability Sample has a known survey sampling design and can be used to produce nationally and sub-nationally representative estimates",
+            "title": "NCHS Research and Development Survey (RANDS) Round 2 during COVID-19 probability sampled Restricted File",
+            "describedByType": "application/pdf",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "spatial": "50 states and District of Columbia",
+            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS_COVID_2_technical_documentation.pdf",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/qbqi-u7ub",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-08-23",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-22",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "52b6029b-6833-45d0-b3bf-aa5b8bf7fd92",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-08-14-to-2023-08-20",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/mdrp-newly-rprt-drug-08-14-2023-to-08-20-2023_0.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-08-14-to-2023-08-20"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/summary-statistics-on-beneficiary-enrollment/medicare-and-medicaid-reports/cms-program-statistics-medicare-advantage-other-health-plan-enrollment",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2013-01-01/2021-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2023-03-06",
+            "references": [
+                "https://data.cms.gov/resources/medicare-and-medicaid-reports-methodology"
+            ],
+            "keyword": [
+                "beneficiary enrollment",
+                "health equity",
+                "medicare",
+                "medicare advantage",
+                "national",
+                "states & territories"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CMS Program Statistics - OEDA",
+                "hasEmail": "mailto:IPAG_Data_Products@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/24fe2a9a-4144-46b2-bf1a-07aa86fb65ae/data-viewer",
+            "description": "The CMS Program Statistics -\u00a0Medicare Advantage & Other Health Plan Enrollment tables provide data on characteristics of the population covered by Medicare Advantage & other health plans.\u00a0\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\u00a0\n\nBelow is the list of tables:\n\nMDCR ENROLL AB 15. \u00a0Medicare Advantage and Other Health Plan Enrollment: \u00a0Part A and/or Part B Total, Aged, and Disabled Enrollees, Yearly Trend\n\tMDCR ENROLL AB 16. \u00a0Medicare Advantage and Other Health Plan Enrollment: Part A and/or Part B Enrollees, by Age Group, Yearly Trend\n\tMDCR ENROLL AB 17. \u00a0Medicare Advantage and Other Health Plan Enrollment: \u00a0Part A and/or Part B Enrollees, by Demographic Characteristics\n\tMDCR ENROLL AB 18. \u00a0Medicare Advantage and Other Health Plan Enrollment: \u00a0Part A and/or Part B Enrollees, by Type of Entitlement and Demographic Characteristics\n\tMDCR ENROLL AB 19. \u00a0Medicare Advantage and Other Health Plan Enrollment: \u00a0Part A and/or Part B Total, Aged, and Disabled Enrollees, by Area of Residence\n\tMDCR ENROLL AB 20. \u00a0Medicare Advantage and Other Health Plan Enrollment: \u00a0Part A and/or Part B Enrollees, by Type of Entitlement and Area of Residence",
+            "title": "CMS Program Statistics - Medicare Advantage & Other Health Plan Enrollment",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-02/a5dd97e6-0511-4434-a612-404c5de5abac/CPS%20MDCR%20ENROLL%20AB%2015-20%202021.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Advantage & Other Health Plan Enrollment : 2021-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-02/CPS%20MDCR%20ENROLL%20AB%2015-20%202020.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Advantage & Other Health Plan Enrollment : 2020-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-01/CPS_MDCR_ENROLL_AB_15-20.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Advantage & Other Health Plan Enrollment : 2019-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-11/CPS%20MDCR%20TOTAL%20ENROLL%20AB%2015-20%202018.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Advantage & Other Health Plan Enrollment : 2018-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2019-12/2017_MA_Other_Enroll.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Advantage & Other Health Plan Enrollment : 2017-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-01/2016_MA_Other_Enroll.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Advantage & Other Health Plan Enrollment : 2016-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-01/2015_MA_Other_Enroll.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Advantage & Other Health Plan Enrollment : 2015-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-01/2014_MA_Other_Enroll.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Advantage & Other Health Plan Enrollment : 2014-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-01/2013_MA_Other_Enroll_0.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Advantage & Other Health Plan Enrollment : 2013-12-31"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/medicare-summary-reports-glossary",
+            "dataQuality": true,
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "Medicare"
+            ],
+            "language": [
+                "en-US"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/hospital-enrollments",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2022-12-21",
+            "temporal": "2022-11-01/2025-01-31",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-15",
+            "references": [
+                "https://data.cms.gov/sites/default/files/2024-10/Hospital_Data_Guidance.pdf"
+            ],
+            "keyword": [
+                "hospitals & facilities",
+                "medicare",
+                "medicare advantage",
+                "original medicare",
+                "provider enrollment"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Provider Enrollment Data Requests - CPI",
+                "hasEmail": "mailto:ProviderEnrollmentDataRequests@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/f6f6505c-e8b0-4d57-b258-e2b94133aaf2/data-viewer",
+            "description": "The Hospital Enrollments dataset provides enrollment information of all Hospitals currently enrolled in Medicare. This data includes information on the Hospital's sub-group type, legal business name, doing business as name, organization type and address.\u00a0",
+            "title": "Hospital Enrollments",
+            "describedByType": "application/pdf",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f6f6505c-e8b0-4d57-b258-e2b94133aaf2/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Hospital Enrollments : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/0ef8ef0d-bf93-4b00-a542-a4e2853947cc/Hospital_Enrollments_2025.01.02.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Enrollments : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4a4388c8-4a14-4a4d-b03a-f67d85d041f0/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Enrollments : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/0b60b159-56e3-4c48-94e6-15d11eb3f1d0/Hospital_Enrollments_2024.12.05.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Enrollments : 2024-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/be4d4816-be24-4635-9f4b-af9af75b708e/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Enrollments : 2024-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/2bf5c555-46a1-4165-8ea7-4c38c2844cbc/Hospital_Enrollments_2024.11.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Enrollments : 2024-11-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/0b4b0c5d-0ea7-41a6-9b1f-af5cf98289ce/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Enrollments : 2024-11-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/51d63517-8592-459f-a1e6-1359b78c1f5d/Hospital_Enrollments_2024.10.07.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Enrollments : 2024-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/bc0698f5-672f-473e-9ea4-72a8ecf73e52/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Enrollments : 2024-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/a366b87a-5c4e-4647-b705-b5449ffa5417/Hospital_Enrollments_2024.09.02.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Enrollments : 2024-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6730716f-6a3f-47d3-9887-efd364764e71/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Enrollments : 2024-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/2cab501d-c837-4c14-8b83-8c1bde463d29/Hospital_Enrollments_2024.08.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Enrollments : 2024-08-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8f04d11f-7a25-4fb4-ae7d-e63975f544db/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Enrollments : 2024-08-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/0a685e7e-3464-41d0-8c6e-9bb08015c2e8/Hospital_Enrollments_2024.07.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Enrollments : 2024-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/adf543ec-03a4-4eab-851c-d2646f03167d/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Enrollments : 2024-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/aaa4a326-ab47-4938-805e-c6d140169a2b/Hospital_Enrollments_2024.06.03.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Enrollments : 2024-06-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/da6d46bd-b701-432e-b5d9-c0f5a9c078b8/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Enrollments : 2024-06-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/3f882174-f1da-4d99-b752-97d17ebba7ff/Hospital_Enrollments_2024.05.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Enrollments : 2024-05-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e6672740-a004-462c-9fc2-4333f26b070a/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Enrollments : 2024-05-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/70a1031c-bf8d-4123-9ae5-ec7bccdd3ca3/Hospital_Enrollments_2024.04.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Enrollments : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f975f35a-a4a0-48ad-9360-9db84c6725ad/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Enrollments : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/5b46a510-8e0c-46d3-a8d5-9bb67707095a/Hospital_Enrollments_2024.03.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Enrollments : 2024-03-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/76dddaa4-4136-4642-a5fc-d05c19f60c9c/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Enrollments : 2024-03-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/5ff2f212-3c2a-47d8-bfcf-c6b42e348860/Hospital_Enrollments_2024.02.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Enrollments : 2024-02-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/eb06749d-f988-4799-aeba-9d0881860690/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Enrollments : 2024-02-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/73657dcd-e512-4cd6-81f4-5619e22778bb/Hospital_Enrollments_2024.01.05.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Enrollments : 2024-01-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/bc22c157-7779-473b-b624-085ad7265f91/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Enrollments : 2024-01-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/4cb89b12-8150-48d4-a7e4-d169e4366074/Hospital_Enrollments_2023.12.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Enrollments : 2023-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/dde19e76-3228-44c7-8185-779cdb654ebf/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Enrollments : 2023-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/a28700e0-2a12-46ce-a92c-6460c31968e5/Hospital_Enrollments_2023.11.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Enrollments : 2023-11-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a85fa452-dee9-4c8f-8156-665238b8492f/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Enrollments : 2023-11-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/9589bd7e-6e2b-496e-9e63-48bfc45a6e8e/Hospital_Enrollments_2023.10.02.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Enrollments : 2023-10-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7cfeded7-0d46-40c0-a23a-453b51271ae4/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Enrollments : 2023-10-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/002066db-b33b-42ca-ad0d-beb4a6702bda/Hospital_Enrollments_2023.09.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Enrollments : 2023-09-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/daf5c2d5-15fd-4431-9469-93faec8aa567/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Enrollments : 2023-09-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/8c594d5e-fbe8-4a16-a249-1768d9579089/Hospital_Enrollments_2023.08.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Enrollments : 2023-08-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/1e406482-cafe-4787-84b0-4241fd76cee9/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Enrollments : 2023-08-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/b2371ce0-2458-4662-97f0-3a1fe23e539f/Hospital_Enrollments_2023.07.06.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Enrollments : 2023-07-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/621b6745-dbd9-4924-8004-7e334ce1885e/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Enrollments : 2023-07-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/6d3c35e7-5c70-4ce4-886e-321ccdc8cae9/Hospital_Enrollments_2023.06.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Enrollments : 2023-06-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/0480e7af-4410-4b93-bd13-d8c8fd3d1153/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Enrollments : 2023-06-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/a2512929-95f7-4948-925b-247fe972fdb2/Hospital_Enrollments_2023.05.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Enrollments : 2023-05-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ce85ae8a-4b06-41fd-a926-e3d19292bff2/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Enrollments : 2023-05-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/fc235f18-95a6-4b0a-af44-b142c8422350/Hospital_Enrollments_2023.03.31.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Enrollments : 2023-04-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9786bd59-b775-4556-9a1f-c5431fcbe6d1/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Enrollments : 2023-04-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-03/ecf5e8bd-05ad-4920-b636-484d2cea4a7f/Hospital_Enrollments_2023.03.10.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Enrollments : 2023-03-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f162edc0-c6b6-4a9e-9f31-7c5a5e2a0128/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Enrollments : 2023-03-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-02/26b98405-95dc-46eb-89aa-eb2e3516bc8d/Hospital_Enrollments_2023.02.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Enrollments : 2023-02-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/cceab54a-f9b2-4ae0-8bc5-275bcaed6c3b/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Enrollments : 2023-02-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-01/438b668c-0361-4482-9ac1-98fca829b310/Hospital_Enrollments_2022.12.30.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Enrollments : 2023-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4c7919b0-545e-4188-94fa-0819c5b3b063/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Enrollments : 2023-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-12/462f3d6d-3e45-4d14-9116-858a3f6be4aa/Hospital_Enrollments.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Enrollments : 2022-11-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ea39ffd9-3a46-4844-857a-10c1503fbfa7/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Enrollments : 2022-11-21"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/sites/default/files/2023-07/Hospital_Enrollments_Data_Dictionary.pdf",
+            "dataQuality": true,
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1M",
+            "theme": [
+                "Medicare"
+            ],
+            "language": [
+                "en-US"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2020-10-02",
+            "@type": "dcat:Dataset",
+            "modified": "2022-04-01",
+            "keyword": [
+                "age",
+                "age group",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "mortality",
+                "nchs",
+                "nvss",
+                "place of death",
+                "provisional",
+                "united states",
+                "weekly"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/g7hk-rc8d",
+            "description": "Provisional death counts of COVID-19 deaths by place of death, week, and age.\n\nData source: National Center for Health Statistics National Vital Statistics System. Provisional data for 2020-2021.",
+            "title": "AH Provisional COVID-19 Deaths by Week, Place of Death, and Age",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/g7hk-rc8d/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/g7hk-rc8d/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/g7hk-rc8d/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/g7hk-rc8d/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "irregular",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/respiratory-viruses/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-12-11",
+            "@type": "dcat:Dataset",
+            "temporal": "2023-2024",
+            "modified": "2024-04-17",
+            "keyword": [
+                "pregnancy",
+                "rsv",
+                "vsd"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VaxView Team",
+                "hasEmail": "mailto:VaxView@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/g4jn-64pd",
+            "description": "Weekly RSV Vaccination Coverage, Pregnant Persons 18-49 Years Old\n\n\u2022 RSV vaccination coverage among pregnant persons is assessed through the Vaccine Safety Datalink*\n\n\u2022 Data on RSV vaccinations among pregnant persons was available starting September 22, 2023, and includes doses received starting September 24, 2023.",
+            "title": "Weekly Respiratory Syncytial Virus (RSV) Vaccination Coverage among Pregnant Persons by Race and Ethnicity",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/g4jn-64pd/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/g4jn-64pd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/g4jn-64pd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/g4jn-64pd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Weekly",
+            "theme": [
+                "Pregnancy & Vaccination"
+            ],
+            "language": [
+                "English"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/qeuw-ymq9",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-03-28",
+            "@type": "dcat:Dataset",
+            "modified": "2024-01-05",
+            "keyword": [
+                "chip",
+                "medicaid",
+                "neonatal abstinence syndrome"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "9c9ad0d1-c59b-4a25-9314-8e7e44e7f281",
+            "description": "This table presents the number of beneficiaries with NAS and the rate of neonatal abstinence syndrome per 1,000 newborns whose deliveries were covered by Medicaid or CHIP, 2017 - 2021.\r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues, making the data unusable for identifying this population. Data for a state are considered unusable based on DQ Atlas thresholds for the following topics: Total Medicaid and CHIP Enrollment, Claims Volume - IP, Claims Volume - OT, Claims Volume - IP, Diagnosis Code - IP, Diagnosis Code - OT, Procedure Codes - OT Professional. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \r\n\r\nData from Maryland, Tennessee, and Utah are omitted due to data quality concerns. Maryland was excluded in 2017 due to unusable diagnosis codes in the IP file and the OT file. Tennessee was excluded due to unusable diagnosis codes in the IP file in 2017 - 2019. Utah was excluded due to unusable procedure codes on OT professional claims in 2017 - 2020. In addition, states with a high data quality concern on one or more measures are noted in the table in the \"Data Quality\" column. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+            "title": "Number and rate of NAS per 1,000 births in newborns whose deliveries were covered by Medicaid or CHIP, 2017 - 2021",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/rate-of-nas-per-thous-in-newborns-2017-to-2021.csv",
+                    "mediaType": "text/csv",
+                    "title": "Number and rate of NAS per 1,000 births in newborns whose deliveries were covered by Medicaid or CHIP, 2017 - 2021"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/wngq-sdai",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2017-09-07",
+            "@type": "dcat:Dataset",
+            "modified": "2017-09-07",
+            "keyword": [
+                "electronic health information",
+                "law",
+                "public health law program"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Rachel Hulkower",
+                "hasEmail": "mailto:hzo2@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/wngq-sdai",
+            "description": "Authors: Cason Schmit, JD, Gregory Sunshine, JD, Dawn Pepin, JD, MPH, Tara Ramanathan, JD, MPH, Akshara Menon, JD, MPH, Matthew Penn, JD, MLIS\r\nThis legal data set consists of state statutes and regulations in effect as of January 1, 2014, related to electronic health information (EHI). Jurisdictions were limited to US states, territories, and the District of Columbia that had statutes and regulations in the Westlaw legal database that expressly referenced EHI. This data set includes 2,364 EHI-related laws representing 49 EHI uses in 54 jurisdictions. For information about research methods, please reference the Electronic Health Information Legal Epidemiology Protocol 2014.",
+            "title": "Electronic Health Information Legal Epidemiology Data Set 2014",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/wngq-sdai/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/wngq-sdai/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/wngq-sdai/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/wngq-sdai/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/qpq4-k3td",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-04-24",
+            "@type": "dcat:Dataset",
+            "modified": "2020-01-02",
+            "keyword": [
+                "2019",
+                "ehrlichia ewingii infection",
+                "ehrlichiosis and anaplasmosis",
+                "giardiasis",
+                "nedss",
+                "netss",
+                "nndss",
+                "undetermined",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/qpq4-k3td",
+            "description": "NNDSS - Table 1L. Ehrlichiosis and Anaplasmosis, Ehrlichia ewingii infection to Giardiasis - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html \r\n\r\nFootnotes: \r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1L. Ehrlichiosis and Anaplasmosis, Ehrlichia ewingii infection to Giardiasis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qpq4-k3td/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qpq4-k3td/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qpq4-k3td/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qpq4-k3td/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.healthit.gov/data/datasets/hospital-public-health-reporting",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-10-03",
+            "@type": "dcat:Dataset",
+            "modified": "2017-01-01",
+            "references": [
+                "https://www.healthit.gov/data/quickstats/hospital-selection-public-health-measures-state"
+            ],
+            "keyword": [
+                "cms ehr incentive program",
+                "emergency department visits",
+                "health information technology",
+                "health it",
+                "interoperability",
+                "public health measures",
+                "public health measures reporting"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "ONC Request",
+                "hasEmail": "mailto:onc.request@hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the National Coordinator for Health Information Technology"
+            },
+            "identifier": "vzcc5ta0-36kx-g2f7-uzay-ps4jb0jt6xdw",
+            "description": "The Centers for Medicare &amp; Medicaid Services (CMS) EHR Incentive Program provides incentive payments for eligible hospitals to adopt and meaningfully use certified health IT. Among the requirements to receive an incentive payment, participating hospitals must report on public health measures. These measures include the electronic reporting of data regarding: immunizations, emergency department visits (syndromic surveillance), reportable infectious disease laboratory results, and electronic patient data to specialized registries, like cancert. As of 2015, stage 2 of the EHR Incentive Program requires hospitals to report on three public health measures, when applicable, and modified stage 2 of the program requires hospitals to report on two of the three measures. This dataset includes the percentage of hospitals who reported on these measures in program years, 2013, 2014 and 2015.",
+            "title": "Hospital Public Health Reporting",
+            "programCode": [
+                "009:110"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/hospital-mu-public-health-measures.csv",
+                    "mediaType": "text/csv",
+                    "title": "hospital-mu-public-health-measures.csv"
+                }
+            ],
+            "describedBy": "https://www.healthit.gov/data/datasets/hospital-public-health-reporting"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-07-15",
+            "@type": "dcat:Dataset",
+            "modified": "2024-08-26",
+            "references": [
+                "https://www.cdc.gov/places/measure-definitions/index.html"
+            ],
+            "keyword": [
+                "behaviors",
+                "census tract",
+                "disability",
+                "gis",
+                "health",
+                "outcomes",
+                "places",
+                "prevalence",
+                "prevention",
+                "risk",
+                "status"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "PLACES Public Inquiries",
+                "hasEmail": "mailto:places@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/hky2-3tpn",
+            "description": "This dataset contains model-based census tract level estimates in GIS-friendly format. PLACES covers the entire United States\u201450 states and the District of Columbia\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2021 or 2020 data, Census Bureau 2010 population estimates, and American Community Survey (ACS) 2015\u20132019 estimates. The 2023 release uses 2021 BRFSS data for 29 measures and 2020 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours) that the survey collects data on every other year. These data can be joined with the census tract 2015 boundary file in a GIS system to produce maps for 36 measures at the census tract level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software.\nhttps://cdcarcgis.maps.arcgis.com/home/item.html?id=2c3deb0c05a748b391ea8c9cf9903588",
+            "title": "PLACES: Census Tract Data (GIS Friendly Format), 2023 release",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hky2-3tpn/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hky2-3tpn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hky2-3tpn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hky2-3tpn/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Census-Tract-Data-GIS-Friendly-Format-2020-/yjkw-uj5s",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "500 Cities & Places"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/qgsr-s7bf",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2016-08-01",
+            "@type": "dcat:Dataset",
+            "modified": "2024-06-11",
+            "keyword": [
+                "drug utilization",
+                "medicaid reimbursements",
+                "pharmacy"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "53cf9f05-97e3-5bd6-a237-bc971e3642d9",
+            "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
+            "title": "State Drug Utilization Data 2016",
+            "programCode": [
+                "009:076"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/StateDrugUtilizationData2016.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P10Y",
+            "theme": [
+                "State Drug Utilization"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/re9g-kq7w",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-15",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Health Effects Laboratory Division, Pathology and Physiology Research Branch",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/re9g-kq7w",
+            "description": "Thermal spray coating is an industrial process where molten metal is sprayed onto a surface as a protective coat at high velocity. Using acellular, in vitro, and in vivo models, the toxicity of these aerosols was evaluated. An automated electric arc wire thermal spray coating aerosol generator and inhalation exposure system were developed to simulate an occupational exposure in an experimental model. Using the inhalation system, male Sprague-Dawley rats were exposed to stainless steel PMET720 aerosols at 25 mg/m3 x 4 hr/d x 9 d. Lung injury, inflammation, and cytokine alteration were determined. Resolution of the response was assessed by evaluating these parameters at 1, 7, 14 and 28 days after exposure. The aerosols generated were also collected and characterized. Macrophages were exposed to 0 \u2013 200 \u00b5g/ml of the collected particles to determine cytotoxicity and screened for known mechanisms of toxicity. Other metal particles similar in composition and morphology, gas metal arc (GMA-SS) and manual metal arc (MMA-SS) stainless steel, were used as particle controls. The influence of pressure used during the process on the toxicity profile of the generated aerosols also was assessed and found to be minimal. The PMET720 thermal spray coating particles exhibited in vitro cytotoxicity and membrane damage only at the highest dose tested. Electron paramagnetic resonance spectroscopy (EPR) showed the PMET720 particles to have oxidative stress potential and caused a dose-dependent increase in intracellular oxidative stress. There also was a dose-dependent increase in NF-kB/AP-1 activity. Treatment with uptake inhibitors showed that the PMET720 particles were internalized via clathrin- and caveolar-mediated endocytosis as wells as actin-dependent pinocytosis/phagocytosis. In most of the cell assays, the two welding fume control particles generated a greater response compared to the PMET720 particles. In vivo, lung damage, inflammation and alteration in cytokines were observed 1 day after inhalation exposure, and this response returned to air control exposure levels by day 7. Alveolar macrophages retained the particulate even after 28 days after exposure. The results suggest that compared to stainless steel welding fumes, the PMET 720 aerosols were less potent, and the animals recovered from the acute pulmonary toxicity induced after 7 days.",
+            "title": "In vivo and in vitro toxicity of a stainless-steel aerosol generated during thermal spray coating",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/re9g-kq7w/application/x-zip-compressed",
+                    "mediaType": "application/x-zip-compressed"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "National Institute for Occupational Safety and Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/dataset/intergovernmental-reference-guide-irg-policy-profies-and-contacts",
+            "bureauCode": [
+                "009:70"
+            ],
+            "issued": "2014-02-07",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "administrative",
+                "age of majority",
+                "children's health",
+                "child support",
+                "child support enforcement",
+                "income withholding",
+                "insurance match",
+                "interest on arrears",
+                "iv-d offices",
+                "lump sum payment",
+                "melson formula",
+                "other",
+                "paternity",
+                "paternity established",
+                "percentage of income model",
+                "policy",
+                "reciprocity",
+                "shared income model",
+                "state child support agency",
+                "statute of limitations",
+                "support enforcement",
+                "support order establishment",
+                "uifsa",
+                "uniform interstate family support act",
+                "usa states"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Dennis Putze",
+                "hasEmail": "mailto:dennis.putze@acf.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Administration for Children and Families, Department of Health & Human Services"
+            },
+            "identifier": "d7cd8d21-678c-4565-8ffa-886189db7f86",
+            "description": "<p>Child support program, policy, and local conatct information.</p>",
+            "title": "Intergovernmental Reference Guide (IRG); Policy Profies and Contacts",
+            "programCode": [
+                "009:084"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.acf.hhs.gov/programs/css/irg-state-map",
+                    "mediaType": "text/html",
+                    "title": "Map"
+                }
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "State"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://pdbp.ninds.nih.gov/",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2016-07-17",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "parkinsons"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "SUTHERLAND, MARGARET L",
+                "hasEmail": "mailto:sutherlandm@ninds.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
+            "identifier": "9047712c-cc5b-4a53-8cb0-a09d769af693",
+            "description": "<p>The NINDS Parkinson\u2019s Disease (PD) Biomarkers Program Data Management Resource enables web-based data entry for clinical studies supporting PD biomarker development, as well as broad data sharing (imaging, clinical, genetic, and biospecimen analysis) across the entire PD research community. The PDBP DMR coordinates information and access to PD biospecimens distributed through the NINDS Human Genetics, DNA, iPSC , Cell Line and Biospecimen Repository and the Harvard Neurodiscovery Initiative.</p>",
+            "title": "Parkinson\u2019s Disease Biomarkers Program Data Management Resource (PDBP DMR)",
+            "programCode": [
+                "009:041"
+            ],
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "dataQuality": true
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/qhz2-qcgn",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2024-11-20",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-15",
+            "references": [
+                "https://www.mathematica.org/"
+            ],
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "7ef3fd19-f2a2-5fbe-93c3-c9efd7247872",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "CoreSEt measure_value v2.10.22 (coreset-impl)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.22/20241029/measure_value.csv",
+                    "description": "CoreSEt measure_value v2.10.22 (coreset-impl)",
+                    "@type": "dcat:Distribution",
+                    "title": "CoreSEt measure_value v2.10.22 (coreset-impl)"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-durable-medical-equipment-devices-supplies/medicare-durable-medical-equipment-devices-supplies-by-geography-and-service",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2014-01-01/2022-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2024-06-04",
+            "references": [
+                "https://data.cms.gov/resources/medicare-durable-medical-equipment-devices-supplies-methodology"
+            ],
+            "keyword": [
+                "health care use & payments",
+                "health equity",
+                "medicare",
+                "national",
+                "original medicare",
+                "physicians & practitioners",
+                "states & territories"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicare Provider Data - OEDA",
+                "hasEmail": "mailto:IPAG_Data_Products@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/27c150fd-8578-43b1-bba5-6388987e32af/data-viewer",
+            "description": "The Medicare Durable Medical Equipment, Devices & Supplies by Geography and Service dataset contains information on usage, payments, and submitted charges organized by geography, Healthcare Common Procedure Coding System (HCPCS) code, and supplier rental indicator.",
+            "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Geography and Service",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/27c150fd-8578-43b1-bba5-6388987e32af/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Geography and Service : 2022-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/75aedbf5-34dd-4b6e-8692-81e2ab64d025/mup_dme_ry24_p05_v10_dy22_geor.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Geography and Service : 2022-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a9d1461a-9c63-49e1-8d91-696082e20e47/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Geography and Service : 2022-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/0de02a58-f287-4757-83e1-b6eeac59bafe/mup_dme_ry24_p05_v10_dy21_geor.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Geography and Service : 2021-12-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/daedccd6-5881-4997-93cb-ad6f3d1dd2fd/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Geography and Service : 2021-12-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/3de69379-e812-45be-8291-12ee3ae2fc1b/mup_dme_ry24_p05_v10_dy20_geor.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Geography and Service : 2020-12-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c5da241c-71d2-4b04-9f44-b324ff4b4c01/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Geography and Service : 2020-12-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/eaec290e-2e73-48e7-8969-781716a9d154/mup_dme_ry24_p05_v10_dy19_geor.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Geography and Service : 2019-12-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3931609c-3f1d-4ab4-95f9-0e31d43613f0/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Geography and Service : 2019-12-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/18ebb7be-a6d2-487b-a024-7f1132d1c774/mup_dme_ry24_p05_v10_dy18_geor.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Geography and Service : 2018-12-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/bc473128-1fae-409f-8665-adf71444f5ca/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Geography and Service : 2018-12-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/089fce32-c793-4095-ad25-1e31f6c718f8/mup_dme_ry24_p05_v10_dy17_geor.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Geography and Service : 2017-12-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/55a97c7d-082f-4605-a21c-37499e7351fc/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Geography and Service : 2017-12-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/cc6da030-8887-42fb-88ca-1b0236c1a759/mup_dme_ry24_p05_v10_dy16_geor.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Geography and Service : 2016-12-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/cb61a768-3ded-47f6-b92d-3fd403d567c8/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Geography and Service : 2016-12-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/e9944cca-386f-462d-bc5e-856736d505e6/mup_dme_ry24_p05_v10_dy15_geor.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Geography and Service : 2015-12-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e679ad08-6e14-4857-9e22-78f1cb2e0851/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Geography and Service : 2015-12-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/358947e6-6f10-4fb8-88ad-7b97c686d37d/mup_dme_ry24_p05_v10_dy14_geor.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Geography and Service : 2014-12-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/52e4df6d-ea54-4fe3-b863-2f7ffc9dddbe/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Geography and Service : 2014-12-16"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/medicare-durable-medical-equipment-devices-supplies-by-geography-and-service-data-dictionary-2022",
+            "dataQuality": true,
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "Medicare"
+            ],
+            "language": [
+                "en-US"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/ttjk-6u2v",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-04-24",
+            "@type": "dcat:Dataset",
+            "modified": "2020-01-02",
+            "keyword": [
+                "2019",
+                "anthrax",
+                "arboviral diseases",
+                "chikungunya virus disease",
+                "eastern equine encephalitis virus disease",
+                "nedss",
+                "netss",
+                "neuroinvasive and non-neuroinvasive",
+                "nndss",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/ttjk-6u2v",
+            "description": "NNDSS - Table 1A. Anthrax to Arboviral diseases, Eastern equine encephalitis virus disease - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1A. Anthrax to Arboviral diseases, Eastern equine encephalitis virus disease",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ttjk-6u2v/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ttjk-6u2v/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ttjk-6u2v/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ttjk-6u2v/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-12-20",
+            "@type": "dcat:Dataset",
+            "modified": "2024-12-20",
+            "references": [
+                "https://wwwdev.cdc.gov/visionhealth/vehss/data/claims/marketscan.html",
+                "https://marketscan.truvenhealth.com/marketscanportal/"
+            ],
+            "keyword": [
+                "claims",
+                "diagnosed prevalence",
+                "eye exams",
+                "marketscan",
+                "medical diagnoses",
+                "service utilization",
+                "truven"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DDT Public Inquiries",
+                "hasEmail": "mailto:ddtpubsmailbox@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/a35h-9yn4",
+            "description": "2016. This dataset is a de-identified summary table of prevalence rates for vision and eye health data indicators from the 2016 MarketScan\u00ae Commercial Claims and Encounters Data (CCAE) is produced by Truven Health Analytics, a division of IBM Watson Health.  The CCEA data contain a convenience sample of insurance claims information from person with employer-sponsored insurance and their dependents, including 43.6 million person years of data. Prevalence estimates are stratified by all available combinations of age group, gender, and state.  Detailed information on VEHSS MarketScan analyses can be found on the VEHSS MarketScan webpage (cdc.gov/visionhealth/vehss/data/claims/marketscan.html). Information on available Medicare claims data can be found on the IBM MarketScan website (https://marketscan.truvenhealth.com). The VEHSS MarketScan summary dataset was last updated November 2019.",
+            "title": "Commercial Medical Insurance (MSCANCC) - Vision and Eye Health Surveillance",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/a35h-9yn4/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/a35h-9yn4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/a35h-9yn4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/a35h-9yn4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Vision-Eye-Health/Shell-Commercial-Medical-Insurance-MSCANCC-Vision-/a35h-9yn4",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "theme": [
+                "Vision & Eye Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-discharges-teds-d-2006-2011",
+            "issued": "2016-05-23",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "alcohol abuse",
+                "drug abuse",
+                "drug treatment",
+                "health care services",
+                "health insurance",
+                "intervention",
+                "mental health",
+                "substance abuse",
+                "substance abuse treatment",
+                "treatment programs"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Substance Abuse & Mental Health Services Administration"
+            },
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2006-2011-nid13578",
+            "description": "<p>The Treatment Episode Data Set -- Discharges (TEDS-D) is a national census data system of annual discharges from substance abuse treatment facilities. TEDS-D provides annual data on the number and characteristics of persons discharged from public and private substance abuse treatment programs that receive public funding. Data collected both at admission and at discharge is included. The unit of analysis is a treatment discharge. TEDS-D consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Admissions (TEDS-A), collects data on admissions to substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS-D variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables unique to TEDS-D, and not part of TEDS-A, are the length of stay, reason for leaving treatment, and service setting at time of discharge. TEDS-D also provides many of the same variables that exist in TEDS-A. This includes information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and<br />\nhashish, heroin, nonprescription methadone, other opiates and<br />\nsynthetics, PCP, other hallucinogens, methamphetamine, other amphetamines,<br />\nother stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates,<br />\nother non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications,<br />\nand other substances.<br />\nCreated variables include total number<br />\nof substances reported, intravenous drug use (IDU), and flags for any<br />\nmention of specific substances.This study has 1 Data Set.</p>",
+            "title": "Treatment Episode Data Set: Discharges (TEDS-D-2006-2011)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2006-2011-nid13578",
+                    "description": "Treatment Episode Data Set: Discharges (TEDS-D-2006-2011) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2006-2011-nid13578"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/qjb4-un5j",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-03-28",
+            "@type": "dcat:Dataset",
+            "modified": "2024-01-05",
+            "keyword": [
+                "chip",
+                "contraceptives",
+                "dq atlas",
+                "medicaid"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "eb88943c-309d-440f-a2d5-ef93e066d83c",
+            "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of contraceptives, including any contraceptives and long-acting reversible contraceptives, provided to female Medicaid and CHIP beneficiaries ages 15 to 44 (as of the first day of the month), by state. \r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating contraceptive care services measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Procedure Codes - OT Professional, Claims Volume - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+            "title": "Contraceptive Care Services Provided to Medicaid and CHIP Beneficiaries ages 15 to 44",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/Contraceptive-Care-Services-Provided-to-MedicaidCHIP-Beneficiaries-ages-15-to-44.csv",
+                    "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of contraceptives, including any contraceptives and long-acting reversible contraceptives, provided to female Medicaid and CHIP beneficiaries ages 15 to 44 (as of the first day of the month), by state. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating contraceptive care services measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Procedure Codes - OT Professional, Claims Volume - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "@type": "dcat:Distribution",
+                    "title": "Contraceptive Care Services Provided to Medicaid and CHIP Beneficiaries ages 15 to 44"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/qjcp-amex",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-03-28",
+            "@type": "dcat:Dataset",
+            "modified": "2023-05-16",
+            "references": [
+                "https://www.mathematica.org/"
+            ],
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "047d3943-6ed3-532e-8eb4-eb67e9b6afc3",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "Scorecard TAG v0.2.4-1 (dev)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/0.2.4-1/TAG.csv",
+                    "description": "Scorecard TAG v0.2.4-1 (dev)",
+                    "@type": "dcat:Distribution",
+                    "title": "Scorecard TAG v0.2.4-1 (dev)"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/dp9i-idru",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-01-21",
+            "@type": "dcat:Dataset",
+            "modified": "2022-01-12",
+            "keyword": [
+                "2021",
+                "age <5 years serotype b",
+                "all ages all serotypes",
+                "gonorrhea",
+                "haemophilus influenzae",
+                "invasive disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/dp9i-idru",
+            "description": "NNDSS - TABLE 1M. Gonorrhea to Haemophilus influenzae, invasive disease, Age <5 years, Serotype b - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1M. Gonorrhea to Haemophilus influenzae, invasive disease, Age <5 years, Serotype b",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dp9i-idru/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dp9i-idru/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dp9i-idru/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dp9i-idru/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/crtu-weni",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2013-08-05",
+            "@type": "dcat:Dataset",
+            "modified": "2015-08-27",
+            "keyword": [
+                "adults",
+                "diabetes",
+                "hus"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/crtu-weni",
+            "description": "Health, United States is an annual report on trends in health statistics, find more information at http://www.cdc.gov/nchs/hus.htm.",
+            "title": "Selected Trend Table from Health, United States, 2011. Diabetes prevalence and glycemic control among adults 20 years of age and over, by sex, age, and race and Hispanic origin: United States, selected years 1988 - 1994 through 2003 - 2006",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/crtu-weni/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/crtu-weni/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/crtu-weni/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/crtu-weni/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Health Statistics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/qkzp-9x7x",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-10-08",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-15",
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
+            ],
+            "keyword": [
+                "dqatlas",
+                "dqatlas_featauto",
+                "utility"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DataConnect Support Team",
+                "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "78430aaa-df0a-5343-92a5-395dcf7c5e33",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "featAuto_measure_concernLevel",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measure_concernLevel.csv",
+                    "description": "{\"dataset\": \"measure_concernLevel\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "@type": "dcat:Distribution",
+                    "title": "measure_concernLevel csv file"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/PT1S",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/qm9a-s4n5",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-07-20",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-18",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "55978f20-d0db-49a0-a304-1c4471367a95",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-07-10-to-2023-07-16",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rprt-drug-07-10-2023-to-07-16-2023_0.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-07-10-to-2023-07-16"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/hospital-change-of-ownership",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2022-04-21",
+            "temporal": "2022-01-01/2024-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-15",
+            "references": [
+                "https://data.cms.gov/sites/default/files/2024-10/Hospital_CHOW_Data_Guidance.pdf"
+            ],
+            "keyword": [
+                "hospitals & facilities",
+                "medicare",
+                "medicare advantage",
+                "original medicare",
+                "provider enrollment"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Provider Enrollment Data Requests - CPI",
+                "hasEmail": "mailto:ProviderEnrollmentDataRequests@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/c04031db-54ce-461c-85d1-d2613d71f167/data-viewer",
+            "description": "The Hospital Change of Ownership (CHOW) dataset provides information on the hospital ownership changes that occurred on or after January 1, 2016. This data includes information on the buyer and seller organization\u2019s legal business name, provider type, change of ownership type (CHOW, Acquisition/Merger, or Consolidation) and the effective date of the change.",
+            "title": "Hospital Change of Ownership",
+            "describedByType": "application/pdf",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c04031db-54ce-461c-85d1-d2613d71f167/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Hospital Change of Ownership : 2024-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/2e9ddac3-eb7e-4805-a3e0-9c52152af37a/Hospital_CHOW_2025.01.02.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Change of Ownership : 2024-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/852a0391-86e0-4470-a56a-6b259984171c/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Change of Ownership : 2024-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/e071c47e-8026-4f4d-a8fe-f254132d056c/Hospital_CHOW_2024.10.07.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Change of Ownership : 2024-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c409dfea-0f37-41ff-b846-1e1435fcc0ff/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Change of Ownership : 2024-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/e5c6a41d-8304-4043-ad0a-f5e5f2605649/Hospital_CHOW_2024.07.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Change of Ownership : 2024-06-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/919e2896-182d-4e6c-9bb5-2e6f85de5fdf/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Change of Ownership : 2024-06-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/942b0c0e-5560-4831-98cd-89433db6584c/Hospital_CHOW_2024.04.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Change of Ownership : 2024-03-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3cba80db-046a-40b0-944d-22528595dcfe/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Change of Ownership : 2024-03-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/df7d9aa1-19ef-4220-b962-9cf230d2e0af/Hospital_CHOW_2024.01.05.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Change of Ownership : 2023-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/278595ef-6f5b-4d37-9b50-8d7acd4bfa25/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Change of Ownership : 2023-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/ad61f629-1981-4320-b6ee-82326db365db/Hospital_CHOW_2023.10.02.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Change of Ownership : 2023-09-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7c76c201-98c6-4840-ac0d-58a4b31043c5/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Change of Ownership : 2023-09-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/626b4774-b9a3-4b1e-81c7-72cf3c67bf2d/Hospital_CHOW_2023.07.06.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Change of Ownership : 2023-06-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/aa821455-086f-40e4-836e-9fd30a95cb67/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Change of Ownership : 2023-06-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/8bc00c59-f2ed-41cb-8405-5ffc9dd20305/Hospital_CHOW_2023.03.31.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Change of Ownership : 2023-03-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/0825fbbd-c57b-4722-bb4d-655c50236be2/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Change of Ownership : 2023-03-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-01/71b731a2-d327-49d5-9229-c3b050024414/Hospital_CHOW_2022.12.30.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Change of Ownership : 2022-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6748a5be-cfe1-4b2c-8b46-ab1322c6364c/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Change of Ownership : 2022-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-10/56134ab3-5a94-4c43-b97a-5408e3b7dc0f/Hospital_CHOW_2022.09.30.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Change of Ownership : 2022-09-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4a71ba37-45d0-4a8b-93bb-dedb3f39c049/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Change of Ownership : 2022-09-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-07/1af25c56-9f89-4495-94a9-bf719f18e967/Study_01.032.02_2022.07.01_PPEF_Hospital_CHOW_Extract.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Change of Ownership : 2022-06-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d779fb35-1882-4dda-a0a0-e754ab4e634d/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Change of Ownership : 2022-06-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-04/Hospital_CHOW_2022Q1.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Change of Ownership : 2022-03-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/2b26bbaa-61e8-4a94-aa3f-eaf5719b78b1/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Change of Ownership : 2022-03-31"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/sites/default/files/2023-01/Hospital_CHOW_Data_Dictionary_2022.12.30.pdf",
+            "dataQuality": true,
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P3M",
+            "theme": [
+                "Medicare"
+            ],
+            "language": [
+                "en-US"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/covidvaxview/weekly-dashboard/adult-vaccination-coverage.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-09-26",
+            "@type": "dcat:Dataset",
+            "temporal": "2024-2025",
+            "modified": "2025-01-29",
+            "keyword": [
+                "covid-19 vaccination",
+                "iis",
+                "iqvia",
+                "nis-acm",
+                "nis-flu",
+                "vsd"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VaxView Team",
+                "hasEmail": "mailto:VaxView@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/ksfb-ug5d",
+            "description": "Weekly COVID-19 Vaccination Coverage and intent among adults 18 Years and Older by Demographic Characteristics and Jurisdiction \u2022 Weekly estimates of COVID-19 vaccination coverage and intent among adults 18 years and older are calculated using data from the National Immunization Survey\u2013Adult COVID Module (NIS\u2013ACM) (https://www.cdc.gov/nis/about/). \n\nWeekly comparisons to previous season should take into account differences between seasons in vaccine availability dates. 2023\u201324 COVID-19 vaccines were first available mid-September 2023, and 2024\u201325 COVID-19 vaccines were first available at the end of August 2024.",
+            "title": "Weekly Cumulative COVID-19 Vaccination Coverage and Intent, Overall, by Selected Demographics and Jurisdiction, Among Adults 18 Years and Older",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ksfb-ug5d/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ksfb-ug5d/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ksfb-ug5d/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ksfb-ug5d/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States- National, Region, State",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Weekly",
+            "theme": [
+                "Vaccinations"
+            ],
+            "language": [
+                "English"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/7pb7-w9us",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2016-01-07",
+            "@type": "dcat:Dataset",
+            "modified": "2016-01-07",
+            "keyword": [
+                "2015",
+                "all serogroups",
+                "invasive",
+                "lyme disease",
+                "malaria",
+                "meningococcal disease",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/7pb7-w9us",
+            "description": "NNDSS - Table II. Lyme disease to Meningococcal - 2015.In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed.The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP: Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table 2 to facilitate case count verification with reporting jurisdictions. \ufffd\ufffd\ufffd Case counts for reporting year 2015 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \ufffd\ufffd Data for meningococcal disease, invasive caused by serogroups ACWY; serogroup B; other serogroup; and unknown serogroup are available in Table I.",
+            "title": "NNDSS - Table II. Lyme disease to Meningococcal",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7pb7-w9us/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7pb7-w9us/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7pb7-w9us/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7pb7-w9us/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/qngr-rkng",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-10-08",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-15",
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
+            ],
+            "keyword": [
+                "dqatlas",
+                "dqatlas_devauto",
+                "utility"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DataConnect Support Team",
+                "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "cb8d7614-bf80-5ffd-a166-4f3903f1ddd4",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "devAuto_measure_compare",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_compare.csv",
+                    "description": "{\"dataset\": \"measure_compare\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "@type": "dcat:Distribution",
+                    "title": "measure_compare csv file"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/PT1S",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/qp4n-462d",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-10-08",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-15",
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
+            ],
+            "keyword": [
+                "dqatlas",
+                "dqatlas_devauto",
+                "utility"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DataConnect Support Team",
+                "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "cf8cfb80-9c92-5582-adbc-11c22f5ed9bc",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "devAuto_topicArea_measureDisplayGroups",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/topicArea_measureDisplayGroups.csv",
+                    "description": "{\"dataset\": \"topicArea_measureDisplayGroups\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "@type": "dcat:Distribution",
+                    "title": "topicArea_measureDisplayGroups csv file"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/PT1S",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "NHDS - National Hospital Discharge Survey Homepage (cdc.gov)",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "Restricted data files can be requested through the Research Data Center. Restricted files contain sensitive protected health information.",
+            "issued": "2010-05-19",
+            "@type": "dcat:Dataset",
+            "temporal": "1970\u20142010",
+            "modified": "2024-02-20",
+            "keyword": [
+                "discharge",
+                "hospital",
+                "hospitals",
+                "inpatient",
+                "sdoh-use-of-health-care",
+                "short-stay-hospitals"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:nhcs@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/9f67-8jse",
+            "description": "The National Hospital Discharge Survey (NHDS), conducted from 1965 to 2010, was a national probability survey designed to meet the need for information on characteristics of inpatients discharged from non-Federal short-stay hospitals in the United States. From 1988-2007 the NHDS collected data from a sample of approximately 270,000 inpatient records acquired from a national sample of about 500 hospitals. From 2008 to 2010 the sample size was reduced to 239. Only hospitals with an average length of stay of fewer than 30 days for all patients, general hospitals, or children\u2019s general hospitals are included in the survey. Federal, military, and Department of Veterans Affairs hospitals, as well as hospital units of institutions (such as prison hospitals), and hospitals with fewer than six beds staffed for patient use, are excluded.\nBeginning in 1988, two data collection procedures have been used in the survey. The medical abstract form and the automated data tapes contain items that relate to the personal characteristics of the patient. These items include age, sex, race, ethnicity, marital status, and expected sources of payment. Administrative items such as admission and discharge dates (which allow calculation of length of stay), as well as discharge status are also included. Medical information about patients includes diagnoses and procedures coded to the International Classification of Diseases, 9th Revision, Clinical Modification (ICD-9-CM).",
+            "title": "National Hospital Discharge Survey (NHDS) 1970-2010",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NHDS/",
+                    "description": "Links to downloadable data files and data documentation included.",
+                    "@type": "dcat:Distribution",
+                    "title": "NHDS 1970-2010"
+                }
+            ],
+            "spatial": "United States",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Database will not be updated again.",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.nursa.org/index.cfm",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2016-07-17",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "HYDE, JAMES F\u00a0",
+                "hasEmail": "mailto:hydej@niddk.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
+            "identifier": "ff71e3cf-f17b-463c-97ef-c0b61c2bb9c0",
+            "description": "<p>The Nuclear Receptor Signaling Atlas (NURSA) is designed to foster the development of a comprehensive understanding of the structure, function, and role in disease of nuclear receptors (NRs) and coregulators. NURSA seeks to elucidate the roles played by NRs and coregulators in metabolism and the development of metabolic disorders (including type 2 diabetes, obesity, osteoporosis, and lipid dysregulation), as well as in cardiovascular disease, oncology, regenerative medicine and the effects of environmental agents on their actions.</p>",
+            "title": "Nuclear Receptor Signaling Atlas (NURSA)",
+            "programCode": [
+                "009:048"
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://classification.nlm.nih.gov/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-08-26",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "classification",
+                "dataset",
+                "library services"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Library of Medicine",
+                "hasEmail": "mailto:custserv@nlm.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/a7sv-mxd2",
+            "description": "A product of the National Library of Medicine for the arrangement of library materials in the field of medicine and related sciences used internationally.  The NLM Classification is updated twice a year with the winter edition published in January and the summer edition published in August. Publication of printed editions ceased with the 5th revised edition, 1999. Beginning with the 2006 edition, the NLM Classification is also available in PDF (Portable Document Format) at https://www.nlm.nih.gov/class/terms_cond.html",
+            "title": "NLM Classification",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://classification.nlm.nih.gov/static/classification/pdf/nlm_policy_on_classification.pdf",
+                    "mediaType": "application/pdf",
+                    "title": "NLM Policy on Classification"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://classification.nlm.nih.gov/current_edition_class_numbers",
+                    "mediaType": "text/html",
+                    "title": "Class Numbers Added and Canceled (Current Edition)"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://classification.nlm.nih.gov/cumulative_class_numbers_added",
+                    "mediaType": "text/html",
+                    "title": "Class Numbers Added (Cumulative List)"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://classification.nlm.nih.gov/cumulative_class_numbers_canceled",
+                    "description": "The National Library of Medicine cancels classification numbers from its schedules for a variety of reasons - most often classification numbers are realigned to better reflect their domain and improve collocation of materials on related concepts.",
+                    "@type": "dcat:Distribution",
+                    "title": "Canceled Class Numbers (Cumulative List)"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://classification.nlm.nih.gov/outline",
+                    "mediaType": "text/html",
+                    "title": "Outline of the NLM Classification"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://classification.nlm.nih.gov/tableg",
+                    "description": "Table G is a cutter system of notations that provides geographical or jurisdictional arrangement of materials under specific class numbers in the NLM Classification. The use of Table G permits a shelving order which is controlled geographically and alphabetically.",
+                    "@type": "dcat:Distribution",
+                    "title": "Table G (Geographic Notation)"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://classification.nlm.nih.gov/19century_schedule",
+                    "description": "Classify here works and reprints of works published between 1801-1913. Classify here translations of works originally published from 1801-1913 only if the translation itself is published from 1801-1913.",
+                    "@type": "dcat:Distribution",
+                    "title": "19th Century Schedule"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Other"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/qrfh-d6pe",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-11-27",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-25",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "ea9cd328-bfc4-4444-b02a-0411d93e419a",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 11-18-2024-to-11-24-2024",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/mdrp-newly-rprt-drug-11-18-2024-to-11-24-2024.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/759d-qk63",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-01-14",
+            "@type": "dcat:Dataset",
+            "modified": "2022-02-11",
+            "keyword": [
+                "2022",
+                "nedss",
+                "netss",
+                "nndss",
+                "vancomycin-intermediate staphylococcus aureus",
+                "vancomycin-resistant staphylococcus aureus",
+                "varicella morbidity",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/759d-qk63",
+            "description": "NNDSS - TABLE 1KK. Vancomycin-intermediate Staphylococcus aureus to Varicella morbidity \u2013 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
+            "title": "NNDSS - TABLE 1KK. Vancomycin-intermediate Staphylococcus aureus to Varicella morbidity",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/759d-qk63/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/759d-qk63/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/759d-qk63/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/759d-qk63/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/qshf-g2pe",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2022-03-30",
+            "@type": "dcat:Dataset",
+            "modified": "2022-03-29",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "f7e2cee0-4e65-4c44-8a28-4dab252a8e5b",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2022-03-21 to 2022-03-27",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rpt-drugs-mar-03-21-2022-03-27-2022.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "restricted public",
+            "landingPage": "https://data.cdc.gov/d/airz-k28h",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "issued": "2023-02-22",
+            "@type": "dcat:Dataset",
+            "temporal": "2022",
+            "modified": "2023-04-20",
+            "keyword": [
+                "gender identity",
+                "intimate partner violence",
+                "physical violence",
+                "research-data-center",
+                "sexual identity",
+                "sexual violence",
+                "stalking"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/airz-k28h",
+            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys using probability-sampled commercial survey panels. The fifth round of RANDS (RANDS 5) was administered by NORC at the University of Chicago using the AmeriSpeak Panel from January 1, 2022 to March 9, 2022. RANDS 5 contained the embedded probe questions and experiments as in previous rounds of RANDS. It also examined responses to gender identity questions as well as different survey administrations of questions appearing in CDC\u2019s National Intimate Partner and Sexual Violence Survey (NISVS). RANDS 5 has a known survey sampling design and can be used to produce nationally and sub-nationally representative estimates.",
+            "title": "NCHS Research and Development Survey (RANDS) Round 5 Restricted File",
+            "describedByType": "application/pdf",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "spatial": "50 states and District of Columbia",
+            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS5-technical-documentation.pdf",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/medicare-durable-medical-equipment-devices-supplies/medicare-durable-medical-equipment-devices-supplies-by-referring-provider-and-service",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2014-01-01/2022-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2024-06-04",
+            "references": [
+                "https://data.cms.gov/resources/medicare-durable-medical-equipment-devices-supplies-methodology"
+            ],
+            "keyword": [
+                "health care use & payments",
+                "health equity",
+                "medical suppliers & equipment",
+                "medicare",
+                "original medicare",
+                "physicians & practitioners"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicare Provider Data - OEDA",
+                "hasEmail": "mailto:IPAG_Data_Products@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/86b4807a-d63a-44be-bfdf-ffd398d5e623/data-viewer",
+            "description": "The Medicare Durable Medical Equipment, Devices & Supplies by Referring Provider and Service dataset contains information on usage, payments and submitted charges organized by National Provider Identifier (NPI), Healthcare Common Procedure Coding System (HCPCS) code, and supplier rental indicator.\n\n\u00a0\n\nNote: This full dataset contains more records than most spreadsheet programs can handle, which will result in an incomplete load of data. Use of a database or statistical software is required.",
+            "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Referring Provider and Service",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/86b4807a-d63a-44be-bfdf-ffd398d5e623/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Referring Provider and Service : 2022-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/dde624cd-2444-4b12-839b-94f56d9110a4/mup_dme_ry24_p05_v10_dy22_rfrhpr.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Referring Provider and Service : 2022-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7f98d91f-f2a6-44cd-a57f-1ac02eaaf795/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Referring Provider and Service : 2022-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/1afb2650-2a26-43f4-b8bc-c8f6d06b814f/mup_dme_ry24_p05_v10_dy21_rfrhpr.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Referring Provider and Service : 2021-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/442050e6-3d96-47b9-bf0e-d894f74a137f/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Referring Provider and Service : 2021-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/08798f22-e778-4b77-91dc-2f0a34f2d131/mup_dme_ry24_p05_v10_dy20_rfrhpr.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Referring Provider and Service : 2020-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/72ce1cd5-efa9-484e-bd74-90ab3a10d244/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Referring Provider and Service : 2020-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/d471019d-7f45-4c91-b9ba-48b27de8062c/mup_dme_ry24_p05_v10_dy19_rfrhpr.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Referring Provider and Service : 2019-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5d2c51d1-50cb-4b10-8930-3e40b7561060/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Referring Provider and Service : 2019-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/c7d48f92-c86c-445b-bab1-01b9f93a64d3/mup_dme_ry24_p05_v10_dy18_rfrhpr.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Referring Provider and Service : 2018-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f848042c-b0b8-4e7d-b2c0-ac6133672076/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Referring Provider and Service : 2018-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/870d54a4-754d-43fa-b282-77472e5c3e8b/mup_dme_ry24_p05_v10_dy17_rfrhpr.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Referring Provider and Service : 2017-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/49a59bf3-78a7-4346-a402-dc7bd239dce6/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Referring Provider and Service : 2017-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/488730ca-9309-48b0-acea-ef491a86b2cd/mup_dme_ry24_p05_v10_dy16_rfrhpr.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Referring Provider and Service : 2016-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3749c9ac-a576-4c7e-bfc5-2fb2b1e1681c/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Referring Provider and Service : 2016-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/5fda2678-9df8-4bce-a0c8-a76e4131ed45/mup_dme_ry24_p05_v10_dy15_rfrhpr.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Referring Provider and Service : 2015-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/da444e4c-a713-4739-b1d5-a71ce9e2f596/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Referring Provider and Service : 2015-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/abeafdf4-1a8c-4609-a68d-631389ed589e/mup_dme_ry24_p05_v10_dy14_rfrhpr.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Referring Provider and Service : 2014-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/04695917-1285-4063-9e98-f51d3db84392/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Durable Medical Equipment, Devices & Supplies - by Referring Provider and Service : 2014-12-30"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/medicare-durable-medical-equipment-devices-supplies-by-referring-provider-and-service-data-dictionary",
+            "dataQuality": true,
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "Medicare"
+            ],
+            "language": [
+                "en-US"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/dataset/adoption-and-foster-care-analysis-and-reporting-system-trends-chart-and-table",
+            "bureauCode": [
+                "009:70"
+            ],
+            "issued": "2013-01-18",
+            "temporal": "2010-01-01T00:00:00-05:00/2011-01-01T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "adoption and foster care",
+                "children's health"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Administration for Children and Families"
+            },
+            "identifier": "186960c3-830b-4181-9c12-b965b051047f",
+            "description": "<p>The AFCARS Trends Chart tracks children in Foster Care from FY 2002 through the most recent year.  A table of data and a graphic depiction of trends are shown for children in care on the first day of the year, entries to foster care, exits, children waiting to be adopted,  children adopted, children with terminations of parental rights, and total children served in foster care.</p>",
+            "title": "Adoption and Foster Care Analysis and Reporting System Trends Chart and Table",
+            "programCode": [
+                "009:101"
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-02-01",
+            "temporal": "2020-03-01/2020-07-31",
+            "@type": "dcat:Dataset",
+            "modified": "2022-04-01",
+            "keyword": [
+                "age",
+                "age group",
+                "all causes",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "hispanic origin",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "race",
+                "sex",
+                "united states"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/s9qn-46pq",
+            "description": "Provisional counts of deaths in the United States by age group, sex, and race/ethnicity, from March-July 2020. The dataset includes cumulative provisional counts of death for COVID-19, coded to ICD-10 code U07.1 as an underlying or multiple cause of death.",
+            "title": "AH Provisional COVID-19 Deaths By Race, Age, and Sex from 3/1/2020 to 7/31/2020",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/s9qn-46pq/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/s9qn-46pq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/s9qn-46pq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/s9qn-46pq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "irregular",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/revalidation-due-date-list",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2022-02-01/2025-01-31",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-02",
+            "references": [
+                "https://data.cms.gov/resources/additional-information-on-revalidation"
+            ],
+            "keyword": [
+                "medicare",
+                "medicare advantage",
+                "original medicare",
+                "provider enrollment"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Provider Enrollment Data Requests - CPI",
+                "hasEmail": "mailto:ProviderEnrollmentDataRequests@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/3746498e-874d-45d8-9c69-68603cafea60/data-viewer",
+            "description": "The Revalidation Due Date List dataset contains revalidation due dates for Medicare providers who are due to revalidate in the following six months. If a provider's due date does not fall within the ensuing six months, the due date is marked 'TBD'. In addition the dataset also includes subfiles with reassignment information for a given provider as well as due date listings for clinics and group practices and their providers.\n\n\u00a0\n\nNote: This full dataset contains more records than most spreadsheet programs can handle, which will result in an incomplete load of data. Use of a database or statistical software is required.",
+            "title": "Revalidation Due Date List",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3746498e-874d-45d8-9c69-68603cafea60/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Revalidation Due Date List : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/d773a8f0-f70a-4185-b2a1-37e39e899e5c/revalidation_base.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Due Date List : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/822c0c0f-865f-4a9d-a9bf-788ce1f574db/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Due Date List : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/3e3c9323-440d-48a5-a38c-5ba6a6999bfb/revalidation_base.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Due Date List : 2024-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ca7b3e71-9fad-4564-a9c2-e8071e7a3044/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Due Date List : 2024-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/336920fa-e652-484f-ab3d-38d1e0c42ce0/revalidation_base.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Due Date List : 2024-04-01a2"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6ee81f4f-162f-4aa0-a2d0-e40bcc61e75e/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Due Date List : 2024-04-01a2"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/85bf3dd0-d8cb-446e-9cd8-835e8a979695/revalidation_base.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Due Date List : 2024-04-01a1"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/2e524d39-6446-461c-b326-c52a406ca658/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Due Date List : 2024-04-01a1"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/b68a2f52-5bde-43aa-b13d-792eff7722e0/revalidation_base.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Due Date List : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/633ef615-7fa2-42b4-a0c2-c196ebc8335b/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Due Date List : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/e8d0361a-4cea-4f45-abe7-4313327ff70f/revalidation_base.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Due Date List : 2024-02-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8b304a52-408a-41ae-878e-26ffe0e8e647/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Due Date List : 2024-02-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/9496b5dc-0dd0-4c04-8246-ea12b835a861/revalidation_base.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Due Date List : 2024-01-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e520dc2b-9b97-4bd0-8862-98ad56e26314/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Due Date List : 2024-01-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/8bfcdc84-14aa-488e-ab6d-2698e61c6bd7/revalidation_base.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Due Date List : 2023-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/61f9e78e-4f5e-4154-b00a-6c0c320482bc/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Due Date List : 2023-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/3082c4b1-d870-4f4a-ad8e-f75368146320/revalidation_base.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Due Date List : 2023-11-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4ab269e9-f990-42e6-89a9-322959133f1e/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Due Date List : 2023-11-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/80bc1738-6878-42bf-9f4a-09af4380cddf/revalidation_base.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Due Date List : 2023-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/912a759e-8d93-419d-8dfe-24538a647083/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Due Date List : 2023-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/7b1345d5-3ff7-4f48-abed-f14c48df12e5/revalidation_base.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Due Date List : 2023-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/0ee81ae9-9012-476a-a42c-a7350b2927a3/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Due Date List : 2023-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/65bc3c08-55da-4952-b315-4c7a0745145c/revalidation_base.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Due Date List : 2023-08-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/41cc90d5-e8c8-4826-9a9e-f2d54cce53fd/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Due Date List : 2023-08-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/82f0ebf8-b9b1-4304-a996-529f6d6de56c/revalidation_base.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Due Date List : 2023-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/dea96ce6-4e63-4ec7-a589-cbbb0d082378/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Due Date List : 2023-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/660c9dbb-b10c-44b0-9ac2-02a5a7ec1043/revalidation_base.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Due Date List : 2023-06-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/92607c1d-6dc1-4bd8-b67c-c4bb50f78e90/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Due Date List : 2023-06-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/21491a12-1e5c-401b-bbb3-2966eed69c6f/Revalidation_base.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Due Date List : 2023-05-04"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/2b3c73e6-54a5-49c1-8228-4a4fd7d6eb55/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Due Date List : 2023-05-04"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-02/cb1525b2-0019-4801-bae9-10d6f8447e80/revalidation_base.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Due Date List : 2023-03-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/853054ee-2f17-4c8f-83a7-f6670b0df875/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Due Date List : 2023-03-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-11/1b3e57ee-1cad-4355-9a61-6784d4951fed/revalidation_base.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Due Date List : 2022-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d022e5bf-4179-4b24-a349-cc675fdb3faa/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Due Date List : 2022-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-11/08c14d82-d397-4bea-b03f-9ceab135c5e2/revalidation_base.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Due Date List : 2022-11-18"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ab4a4ed4-81ed-4285-bb95-20fffaa39045/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Due Date List : 2022-11-18"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-09/84927be5-f111-4331-9c1a-a4f04348322c/revalidation_base.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Due Date List : 2022-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5feb2d49-b5f3-474d-ae18-743f819556e6/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Due Date List : 2022-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-08/9e8b2d15-0d2e-47a4-a45c-19649c61bb22/revalidation_base.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Due Date List : 2022-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/68fa7b65-f27a-4218-8380-86127791d335/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Due Date List : 2022-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-07/e6bc2757-32e0-41a0-bbe2-428f9f0a0739/revalidation_base.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Due Date List : 2022-08-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d0a18c13-83ae-44a0-bfa2-e95505af25bf/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Due Date List : 2022-08-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-07/16486767-d811-4d14-811f-e4b1220bafa3/revalidation_base.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Due Date List : 2022-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/484a0a8b-1069-4322-bd57-47e5a7d88258/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Due Date List : 2022-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-06/177f28ba-d5b8-4f19-9cfd-fef11b4d8439/revalidation_base.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Due Date List : 2022-06-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8b26cdaa-8860-467a-b065-f7ecb11375c2/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Due Date List : 2022-06-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-05/85c47358-6feb-4540-b022-aab84e7d07e9/revalidation_base.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Due Date List : 2022-04-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d378fb6b-12ad-4bf3-95f6-b6dcb7cbb48d/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Due Date List : 2022-04-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-03/8dac2ad1-7df0-4718-ab55-f49542de3736/revalidation_base.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Due Date List : 2022-02-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6993d4bc-2484-4d16-abd4-b15abe12241e/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Due Date List : 2022-02-28"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/revalidation-due-date-list-data-dictionary",
+            "dataQuality": true,
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1M",
+            "theme": [
+                "Medicare"
+            ],
+            "language": [
+                "en-US"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2020-06-24",
+            "@type": "dcat:Dataset",
+            "modified": "2023-09-27",
+            "keyword": [
+                "all causes",
+                "coronavirus",
+                "county",
+                "covid-19",
+                "deaths",
+                "hispanic origin",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "race",
+                "united states"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/k8wy-p9cg",
+            "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nCounty data on race and Hispanic origin is available for counties with more than 100 COVID-19 deaths.\u00a0Deaths are cumulative from the week ending January 4, 2020 to the most recent reporting week, and based on county of occurrence. Data is provisional. \n\nUrban-rural classification is based on the 2013 National Center for Health Statistics Urban-Rural Classification Scheme for Counties (https://www.cdc.gov/nchs/data_access/urban_rural.htm).",
+            "title": "Provisional COVID-19 Deaths by County, and Race and Hispanic Origin",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/k8wy-p9cg/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/k8wy-p9cg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/k8wy-p9cg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/k8wy-p9cg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "irregular",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "public",
+            "issued": "2015-12-02",
+            "@type": "dcat:Dataset",
+            "temporal": "1960/2018",
+            "modified": "2022-03-28",
+            "references": [
+                "https://www.cdc.gov/nchs/data/vsus/vsus_1950_1.pdf",
+                "https://www.cdc.gov/nchs/data/misc/usvss.pdf",
+                "https://www.cdc.gov/nchs/data/vsus/nat67_1.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_01.pdf",
+                "https://www.cdc.gov/nvsr/nvsr67/nvsr67_01.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr68/nvsr68_13.pdf"
+            ],
+            "keyword": [
+                "birth rates",
+                "births",
+                "ethnicity",
+                "fertility rates",
+                "hispanic origin",
+                "nchs",
+                "race",
+                "united states"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:births@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/89yk-m38d",
+            "description": "This dataset includes live births, birth rates, and fertility rates by race of mother in the United States since 1960. \n\nData availability varies by race and ethnicity groups. All birth data by race before 1980 are based on race of the child. Since 1980, birth data by race are based on race of the mother. For race, data are available for Black and White births since 1960, and for American Indians/Alaska Native and Asian/Pacific Islander births since 1980. Data on Hispanic origin are available since 1989. Teen birth rates for specific racial and ethnic categories are also available since 1989. From 2003 through 2015, the birth data by race were based on the \u201cbridged\u201d race categories (5). Starting in 2016, the race categories for reporting birth data changed; the new race and Hispanic origin categories are: Non-Hispanic, Single Race White; Non-Hispanic, Single Race Black; Non-Hispanic, Single Race American Indian/Alaska Native; Non-Hispanic, Single Race Asian; and, Non-Hispanic, Single Race Native Hawaiian/Pacific Islander (5,6). Birth data by the prior, \u201cbridged\u201d race (and Hispanic origin) categories are included through 2018 for comparison.\n\nSOURCES\n\nNCHS, National Vital Statistics System, birth data (see https://www.cdc.gov/nchs/births.htm); public-use data files (see https://www.cdc.gov/nchs/data_access/VitalStatsOnline.htm); and CDC WONDER (see http://wonder.cdc.gov/).\n\nREFERENCES\n\n1. National Office of Vital Statistics. Vital Statistics of the United States, 1950, Volume I. 1954. Available from: https://www.cdc.gov/nchs/data/vsus/vsus_1950_1.pdf.\n\n2. Hetzel AM. U.S. vital statistics system: major activities and developments, 1950-95. National Center for Health Statistics. 1997. Available from: https://www.cdc.gov/nchs/data/misc/usvss.pdf.\n\n3. National Center for Health Statistics. Vital Statistics of the United States, 1967, Volume I\u2013Natality. 1969. Available from: https://www.cdc.gov/nchs/data/vsus/nat67_1.pdf.\n\n4. Martin JA, Hamilton BE, Osterman MJK, et al. Births: Final data for 2015. National vital statistics reports; vol 66 no 1. Hyattsville, MD: National Center for Health Statistics. 2017. Available from: https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_01.pdf.\n\n5. Martin JA, Hamilton BE, Osterman MJK, Driscoll AK, Drake P. Births: Final data for 2016. National Vital Statistics Reports; vol 67 no 1. Hyattsville, MD: National Center for Health Statistics. 2018. Available from: https://www.cdc.gov/nvsr/nvsr67/nvsr67_01.pdf.\n\n6. Martin JA, Hamilton BE, Osterman MJK, Driscoll AK, Births: Final data for 2018. National vital statistics reports; vol 68 no 13. Hyattsville, MD: National Center for Health Statistics. 2019. Available from: https://www.cdc.gov/nchs/data/nvsr/nvsr68/nvsr68_13.pdf.",
+            "title": "NCHS - Natality Measures for Females by Race and Hispanic Origin: United States",
+            "isPartOf": "NCHS - Natality Measures for Females by Race and Hispanic Origin: United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/89yk-m38d/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/89yk-m38d/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/89yk-m38d/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/89yk-m38d/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "50 states and District of Columbia",
+            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "license": "https://www.usa.gov/government-works",
+            "theme": [
+                "NCHS"
+            ],
+            "language": [
+                "English"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "public",
+            "issued": "2015-12-02",
+            "@type": "dcat:Dataset",
+            "temporal": "1989/2018",
+            "modified": "2022-03-29",
+            "references": [
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_01.pdf",
+                "https://www.cdc.gov/nvsr/nvsr67/nvsr67_01.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr68/nvsr68_13.pdf"
+            ],
+            "keyword": [
+                "birth",
+                "birth rate",
+                "ethnicity",
+                "fertility rate",
+                "hispanic origin",
+                "nchs",
+                "united states"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:births@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/s54h-bixi",
+            "description": "This dataset includes live births, birth rates, and fertility rates by Hispanic origin of mother in the United States since 1989. \n\nNational data on births by Hispanic origin exclude data for Louisiana, New Hampshire, and Oklahoma in 1989; New Hampshire and Oklahoma in 1990; and New Hampshire in 1991 and 1992. Birth and fertility rates for the Central and South American population includes other and unknown Hispanic. Information on reporting Hispanic origin is detailed in the Technical Appendix for the 1999 public-use natality data file (see ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/Nat1999doc.pdf).",
+            "title": "NCHS - Natality Measures for Females by Hispanic Origin Subgroup: United States",
+            "isPartOf": "NCHS - Natality Measures for Females by Hispanic Origin Subgroup: United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/s54h-bixi/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/s54h-bixi/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/s54h-bixi/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/s54h-bixi/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "50 states and District of Columbia",
+            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "license": "https://www.usa.gov/government-works",
+            "theme": [
+                "NCHS"
+            ],
+            "language": [
+                "English"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/5c6r-xi2t",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-11-09",
+            "@type": "dcat:Dataset",
+            "temporal": "2023-2024 respiratory virus season",
+            "modified": "2025-01-24",
+            "keyword": [
+                "coronavirus",
+                "covid19",
+                "immunization",
+                "ncird",
+                "nis-acm",
+                "nis-ccm",
+                "respiratory-virus-response",
+                "rsv",
+                "vaccination",
+                "vaccination-coverage"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "James Singleton",
+                "hasEmail": "mailto:vaxview@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/5c6r-xi2t",
+            "description": "The weekly respiratory virus vaccination data come from the National Immunization Survey-Adult COVID Module (NIS-ACM), National Immunization Survey-Child COVID Module (NIS-CCM), and the National Immunization Survey-Flu (NIS-Flu). The NIS-ACM provides data on Influenza (flu), COVID-19, and RSV vaccination for adults aged \u226518 years in the United States. The NIS-CCM provides data on COVID-19 vaccination for children aged 6 months-17 years in the United States. The NIS-Flu provides data on Influenza vaccination for children aged 6 months-17 years in the United States National Immunization Survey data are collected by telephone interview using a random-digit-dialed sample of cellular telephone numbers stratified by state, the District of Columbia, five local jurisdictions (Bexar County TX, Chicago IL, Houston TX, New York City NY, and Philadelphia County PA), and Guam, Puerto Rico, and the United States Virgin Islands. Data are weighted to represent the non-institutionalized United States population and mitigate possible bias that can result from incomplete sample frame (exclusion of households with no phone service or only landline telephones) or non-response. All responses are self-reported, or reported by a parent for children 6 months-17 years. For more information about the surveys, see\u202fhttps://www.cdc.gov/vaccines/imz-managers/nis/about.html#current-surveys. Estimates should be interpreted with caution when there is a small sample size or wide confidence interval.\u202f",
+            "title": "Weekly Respiratory Virus Vaccination Data, Children 6 Months-17 Years and Adults 18 Years and Older, National Immunization Survey",
+            "programCode": [
+                "009:037"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5c6r-xi2t/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5c6r-xi2t/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5c6r-xi2t/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5c6r-xi2t/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "U.S.",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1W",
+            "theme": [
+                "Vaccinations"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/t984-9cdv",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2013-08-13",
+            "@type": "dcat:Dataset",
+            "modified": "2015-08-27",
+            "keyword": [
+                "adults",
+                "brfss",
+                "health care coverage",
+                "heath care access"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/t984-9cdv",
+            "description": "Percentages are weighted to population characteristics. Data are not available if it did not meet BRFSS stability requirements. For more information on these requirements, as well as risk factors and calculated variables, see the Technical Documents and Survey Data for a specific year - http://www.cdc.gov/brfss/annual_data/annual_data.htm. Recommended citation: Centers for Disease Control and Prevention (CDC). Behavioral Risk Factor Surveillance System. Atlanta, Georgia: U.S. Department of Health and Human Services, Centers for Disease Control and Prevention, [appropriate year].",
+            "title": "BRFSS Prevalence And Trends Data: Health Care Access/Coverage for 1995-2010",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/t984-9cdv/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/t984-9cdv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/t984-9cdv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/t984-9cdv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Health Statistics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/qvpz-fkkp",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-10-08",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-15",
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
+            ],
+            "keyword": [
+                "dqatlas",
+                "dqatlas_implauto",
+                "utility"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DataConnect Support Team",
+                "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "d2469e00-b3f0-568b-8f66-658ee6e67c86",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "implAuto_states_measures_download",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/states_measures_download.csv",
+                    "description": "{\"dataset\": \"states_measures_download\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "@type": "dcat:Distribution",
+                    "title": "states_measures_download csv file"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/PT1S",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.healthit.gov/techlab/ipg/",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-10-03",
+            "@type": "dcat:Dataset",
+            "modified": "2023-10-03",
+            "keyword": [
+                "data standards",
+                "health care",
+                "health it",
+                "interoperability"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "ONC Request",
+                "hasEmail": "mailto:onc.request@hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the National Coordinator for Health Information Technology"
+            },
+            "identifier": "obq8zsu3-97j2-kg6f-m27a-jblq9u0jqg4s",
+            "description": "The Interoperability Proving Ground (IPG) is an open, community platform where you can share, learn, and be inspired by interoperability projects occurring in the United States (and around the world).",
+            "title": "Interoperability Proving Ground",
+            "programCode": [
+                "009:110"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/techlab/ipg/",
+                    "mediaType": "text/csv",
+                    "title": "Interoperability_Proving_Ground.csv"
+                }
+            ],
+            "describedBy": "https://www.healthit.gov/techlab/ipg/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/qw6v-hk93",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2024-11-20",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-15",
+            "references": [
+                "https://www.mathematica.org/"
+            ],
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "7973548e-1362-5969-8ee7-8e9ea0cda0fe",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "CoreSEt filters v2.10.22 (coreset-impl)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.22/20241029/filters.csv",
+                    "description": "CoreSEt filters v2.10.22 (coreset-impl)",
+                    "@type": "dcat:Distribution",
+                    "title": "CoreSEt filters v2.10.22 (coreset-impl)"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/r7hc-32zu",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2016-01-07",
+            "@type": "dcat:Dataset",
+            "modified": "2016-01-07",
+            "keyword": [
+                "2015",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "west nile virus",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/r7hc-32zu",
+            "description": "NNDSS - Table II. West Nile virus disease - 2015.In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed.The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP: Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table 2 to facilitate case count verification with reporting jurisdictions. \ufffd\ufffd\ufffd Case counts for reporting year 2015 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \ufffd\ufffd Updated weekly from reports to the Division of Vector-Borne Diseases, National Center for Emerging and Zoonotic Infectious Diseases (ArboNET Surveillance). Data for California serogroup, Chikungunya virus, eastern equine, Powassan, St. Louis, and western equine diseases are available in Table I. \ufffd\ufffd Not reportable in all states. Data from states where the condition is not reportable are excluded from this table, except starting in 2007 for the domestic arboviral diseases, influenza-associated pediatric mortality, and in 2003 for SARS-CoV. Reporting exceptions are available at http://wwwn.cdc.gov/nndss/downloads.html.",
+            "title": "NNDSS - Table II. West Nile virus disease",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/r7hc-32zu/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/r7hc-32zu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/r7hc-32zu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/r7hc-32zu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/qw9z-s3b4",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2024-08-27",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-07",
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
+            ],
+            "keyword": [
+                "dqatlas",
+                "dqatlas_prodauto",
+                "utility"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DataConnect Support Team",
+                "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "c9de5ddc-5651-5e76-83e1-e132e0826839",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
+            "title": "prodAuto_briefType",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/briefType.csv",
+                    "description": "{\"dataset\": \"briefType\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "@type": "dcat:Distribution",
+                    "title": "briefType csv file"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/PT1S",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/qwzd-jxqv",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-03-28",
+            "@type": "dcat:Dataset",
+            "modified": "2024-01-05",
+            "keyword": [
+                "chip",
+                "covid-19",
+                "dq atlas",
+                "medicaid",
+                "t-msis analytic files"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "ed35fa7f-279b-4d68-b624-b6ff32e956df",
+            "description": "This data set includes monthly counts and percentages of Medicaid and CHIP beneficiaries, by state, who received at least one service for each of the following conditions: acute bronchitis, acute respiratory distress, bronchitis not other specified (NOS), COVID-19 (based on the presence of diagnosis code U07.1), influenza, lower or acute respiratory infection, pneumonia, respiratory infection NOS, and suspected COVID-19 (based on the presence of diagnosis code B97.29).\r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating COVID-related conditions measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Claims Volume - IP, Claims Volume - OT, Claims Volume - IP, Diagnosis Code - IP, Diagnosis Code - OT, Procedure Codes - OT Professional. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+            "title": "Respiratory Conditions in the Medicaid and CHIP Population",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/Respiratory-Conditions-in-the-MedicaidCHIP-Population.csv",
+                    "description": "This data set includes monthly counts and percentages of Medicaid and CHIP beneficiaries, by state, who received at least one service for each of the following conditions: acute bronchitis, acute respiratory distress, bronchitis not other specified (NOS), COVID-19 (based on the presence of diagnosis code U07.1), influenza, lower or acute respiratory infection, pneumonia, respiratory infection NOS, and suspected COVID-19 (based on the presence of diagnosis code B97.29).\n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating COVID-related conditions measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Claims Volume - IP, Claims Volume - OT, Claims Volume - IP, Diagnosis Code - IP, Diagnosis Code - OT, Procedure Codes - OT Professional. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "@type": "dcat:Distribution",
+                    "title": "Respiratory Conditions in the Medicaid and CHIP Population"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nors/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-07-29",
+            "@type": "dcat:Dataset",
+            "modified": "2024-12-30",
+            "keyword": [
+                "foodborne",
+                "gastroenteritis",
+                "outbreak",
+                "waterborne"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NORS Team",
+                "hasEmail": "mailto:NORSDashboard@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/5xkq-dg7x",
+            "description": "The National Outbreak Reporting System (NORS) is a web-based platform designed to support reporting to CDC by local, state, and territorial health departments in the United States of all waterborne disease outbreaks and enteric disease outbreaks transmitted by food, contact with environmental sources, infected persons or animals, or unknown modes of transmission.",
+            "title": "NORS",
+            "programCode": [
+                "009:026"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5xkq-dg7x/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5xkq-dg7x/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5xkq-dg7x/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5xkq-dg7x/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Annual",
+            "theme": [
+                "Foodborne",
+                "Waterborne",
+                "and Related Diseases"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.accessdata.fda.gov/scripts/infantformula/InfantFormulaRecallList2010.xml",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "1900-01-01",
+            "keyword": [
+                "recalls"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "openFDA",
+                "hasEmail": "mailto:open@fda.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "identifier": "cbb45912-ca03-4398-8d6d-607e335a8ed9",
+            "description": "This list includes products subject to recall since September 2010 related to infant formula distributed by Abbott. This list will be updated with publicly available information as received. The information is current as of the date indicated. If we learn that any information is not accurate, we will revise the list as soon as possible. When available, this database also includes photos of recalled products that have been voluntarily submitted by recalling firms to the FDA to assist the public in identifying those products that are subject to recall.",
+            "title": "Abbott Infant Formula Recall",
+            "programCode": [
+                "009:001"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/infantformula/InfantFormulaRecallList2010.xml",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "irregular"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/covid19/nhcs.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2020-12-15",
+            "@type": "dcat:Dataset",
+            "temporal": "2020-03-18/2023-12-26",
+            "modified": "2024-07-29",
+            "keyword": [
+                "covid-19",
+                "emergency department",
+                "hospital encounters",
+                "inpatient",
+                "intubation",
+                "mortality",
+                "respiratory illness",
+                "screenings",
+                "ventilator use"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/q3t8-zr7t",
+            "description": "The National Hospital Care Survey (NHCS) collects data on patient care in hospital-based settings to describe patterns of health care delivery and utilization in the United States. Settings currently include inpatient and emergency departments (ED). Additionally, the NHCS contributes data that may inform public health emergencies as the survey is designed to capture emerging diseases and viruses that require hospitalizations, including COVID-19 encounters. The 2020 - 2023 NHCS are not yet fully operational so it is important to note that these data are not nationally representative.\n\nThe data are from 26 hospitals submitting inpatient and 26 hospitals submitting ED Uniform Bill (UB)-04 administrative claims from March 18, 2020-December 26, 2023.  Even though the data are not nationally representative, they can provide insight on the impact of COVID-19 on various types of hospitals throughout the country. This information is not available in other hospital reporting systems. The NHCS data from these hospitals can show results by a combination of indicators related to COVID-19, such as length of inpatient stay, in-hospital mortality, comorbidities, and intubation or ventilator use. NHCS data allow for reporting on patient conditions and treatments within the hospital over time.",
+            "title": "COVID-19 Hospital Data from the National Hospital Care Survey",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/q3t8-zr7t/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/q3t8-zr7t/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/q3t8-zr7t/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/q3t8-zr7t/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P2M",
+            "theme": [
+                "NCHS"
+            ],
+            "language": [
+                "en-US"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://mor.nlm.nih.gov/RxMix/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-06-30",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "api",
+                "drugs",
+                "supplements",
+                "tools & utilities"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Library of Medicine",
+                "hasEmail": "mailto:custserv@nlm.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/jqkg-525p",
+            "description": "An interface for building applications that allows users to combine functions of various NLM drug APIs, including the RxNorm, RxClass, RxTerms, and NDF-RT APIs. Sequences of functions can be executed interactively or in batch mode.",
+            "title": "RxMix",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://mor.nlm.nih.gov/RxMix/",
+                    "mediaType": "text/html",
+                    "title": "Query Interface"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Drugs and Chemicals"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/hyak-nxqs",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-01-14",
+            "@type": "dcat:Dataset",
+            "modified": "2022-02-11",
+            "keyword": [
+                "2022",
+                "nedss",
+                "netss",
+                "nndss",
+                "tetanus",
+                "toxic shock syndrome (other than streptococcal)",
+                "trichinellosis",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/hyak-nxqs",
+            "description": "NNDSS - TABLE 1II. Tetanus to Trichinellosis \u2013 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
+            "title": "NNDSS - TABLE 1II. Tetanus to Trichinellosis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hyak-nxqs/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hyak-nxqs/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hyak-nxqs/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hyak-nxqs/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/7jik-jwvu",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2020-01-21",
+            "@type": "dcat:Dataset",
+            "modified": "2021-01-07",
+            "keyword": [
+                "2020",
+                "dengue",
+                "dengue-like illness",
+                "dengue virus infections",
+                "nedss",
+                "netss",
+                "nndss",
+                "severe dengue",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/7jik-jwvu",
+            "description": "NNDSS - TABLE 1J. Dengue virus infections, Dengue to Severe dengue - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1J. Dengue virus infections, Dengue to Severe dengue",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7jik-jwvu/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7jik-jwvu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7jik-jwvu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7jik-jwvu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/qzza-zykr",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-04-27",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-15",
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
+            ],
+            "keyword": [
+                "dqatlas",
+                "dqatlas_devauto",
+                "utility"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DataConnect Support Team",
+                "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "095672d6-0a1f-520c-a59a-a87227801cf4",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "devAuto_footnotes",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/footnotes.csv",
+                    "description": "{\"dataset\": \"footnotes\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "@type": "dcat:Distribution",
+                    "title": "footnotes csv file"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/PT1S",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/4bft-6yws",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2020-01-17",
+            "@type": "dcat:Dataset",
+            "modified": "2021-01-07",
+            "keyword": [
+                "2020",
+                "botulism",
+                "foodborne",
+                "infant",
+                "nedss",
+                "netss",
+                "nndss",
+                "other (wound & unspecified)",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/4bft-6yws",
+            "description": "NNDSS - Table 1E. Botulism, Foodborne to Botulism, Other (wound & unspecified) - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - Table 1E. Botulism, Foodborne to Botulism, Other (wound & unspecified)",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4bft-6yws/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4bft-6yws/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4bft-6yws/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4bft-6yws/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "restricted public",
+            "landingPage": "https://www.cdc.gov/nchs/nnhs/index.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
+            "issued": "2007-04-13",
+            "@type": "dcat:Dataset",
+            "temporal": "2004-08-01/2004-12-31",
+            "modified": "2024-03-25",
+            "keyword": [
+                "icd-9-cm",
+                "long-term care",
+                "medications",
+                "national nursing home survey",
+                "research-data-center"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/tks5-umwc",
+            "description": "The 2004 National Nursing Home Survey (NNHS), conducted between August and December of 2004, was reintroduced into the field after a five-year break, during which time the survey was redesigned and expanded to collect many new data items. All nursing homes that participated in the NNHS had at least three beds and were either certified (by Medicare or Medicaid) or had a state license to operate as a nursing home. The redesigned survey was administered using a computer-assisted personal interviewing (CAPI) system. The National Nursing Home Survey provides information on nursing homes from two perspectives-that of the provider of services and that of the recipient of care. Data about the facilities include characteristics such as size, ownership, Medicare/Medicaid certification, services provided and specialty programs offered, and charges. For recipients, data were obtained on demographic characteristics, health status and medications taken, services received, and sources of payment.\n\nData for the survey were obtained through personal interviews with facility administrators and designated staff who used administrative records to answer questions about the facilities, staff, services and programs, and medical records to answer questions about the residents.\n\nThe total number of nursing home facilities that participated in NNHS is 1,174.",
+            "title": "2004 National Nursing Home Survey - Restricted Resident Medications Dataset",
+            "isPartOf": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NNHS/nnhs04/SAS_Data/",
+            "describedByType": "application/pdf",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html",
+                    "title": "2004 National Nursing Home Survey - Restricted Resident Medications Dataset"
+                }
+            ],
+            "spatial": "United States",
+            "describedBy": "https://www.cdc.gov/nchs/data/nnhsd/2004NNHS_DesignCollectionEstimates_072706tags.pdf",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NCHS"
+            ],
+            "language": [
+                "en-US"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/statesystem/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-07-18",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-10",
+            "references": [
+                "https://chronicdata.cdc.gov/d/5qag-uzp2"
+            ],
+            "keyword": [
+                "legislation",
+                "osh",
+                "policy",
+                "smokefree campus",
+                "state system",
+                "tobacco"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "OSHData Support",
+                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/yhkp-cczf",
+            "description": "1995-2024. Centers for Disease Control and Prevention (CDC).  State Tobacco Activities Tracking and Evaluation (STATE) System. Legislation \u2013 Smokefree Campuses. The STATE System houses current and historical state-level legislative data on tobacco use prevention and control policies. Data are reported on a quarterly basis. Data include state smokefree indoor air policies in areas such as: Smokefree campuses for private and public colleges and schools (K-12).",
+            "title": "CDC STATE System Tobacco Legislation - Smokefree Campus",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yhkp-cczf/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yhkp-cczf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yhkp-cczf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yhkp-cczf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-Tobacco-Legislation-Smokefree-Cam/yhkp-cczf",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "theme": [
+                "Legislation"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/x7zy-2xmx",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2016-11-08",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-17",
+            "keyword": [
+                "500 cities",
+                "boundaries",
+                "census tract",
+                "shapefile"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "500 Cities Public Inquiries",
+                "hasEmail": "mailto:places@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/x7zy-2xmx",
+            "description": "This census tract shapefile for the 500 Cities project was extracted from the Census 2010 Tiger/Line database and modified to remove portions of census tracts that were outside of city boundaries. This shapefile can be joined with 500 Cities census tract-level Data (GIS Friendly Format) in a geographic information system (GIS) to make maps at the census tract level.",
+            "title": "500 Cities: Census Tract Boundaries",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/x7zy-2xmx/application/zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "500 Cities & Places"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/g3k9-gyw7",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2020-04-10",
+            "@type": "dcat:Dataset",
+            "modified": "2020-04-10",
+            "keyword": [
+                "artesunate",
+                "division of parasitic diseases and malaria",
+                "malaria"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Francisca Abanyie, MD, MPH",
+                "hasEmail": "mailto:why6@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/g3k9-gyw7",
+            "description": "This dataset includes deidentified data on patients receiving artesunate through the National Artesunate for Severe Malaria Program from April- December 2019. \n\nThis dataset contains the data from the case report form only.\nPlease see the links below for the other datasets and the attached document 'Guide to NASMP Datasets':\nData from Case Report Form- https://data.cdc.gov/Global-Health/National-Artesunate-for-Severe-Malaria-Program-Cas/igaz-icki\nData on Artesunate Dosing- https://data.cdc.gov/dataset/National-Artesunate-for-Severe-Malaria-Program-Art/qan4-gt4k\nData on Microscopy (Parasitemia values)- https://data.cdc.gov/Global-Health/National-Artesunate-for-Severe-Malaria-Program-Mic/v2k9-ctv4\n\nAll data can be easily linked using the ParticipantID field, a unique ID number assigned to each participant.",
+            "title": "National Artesunate for Severe Malaria Program Follow-On Antimalarial Dosing Data- April to December 2019",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/g3k9-gyw7/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/g3k9-gyw7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/g3k9-gyw7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/g3k9-gyw7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Global Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/3pbe-qh9z",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-07-25",
+            "@type": "dcat:Dataset",
+            "temporal": "2020-12-13/2023-05-12",
+            "modified": "2023-05-12",
+            "references": [
+                "https://www.cdc.gov/coronavirus/2019-ncov/vaccines/distributing/about-vaccine-data.html"
+            ],
+            "keyword": [
+                "administration",
+                "age",
+                "coronavirus",
+                "covid-19",
+                "demographics",
+                "ethnicity",
+                "immunization",
+                "izdl",
+                "race",
+                "sex",
+                "vaccination"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NCIRD",
+                "hasEmail": "mailto:iisinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/3pbe-qh9z",
+            "description": "This site provides historical data beginning June 22, 2022, for the visualization presented on <a href=\"https://covid.cdc.gov/covid-data-tracker/#vaccinations\" target=\"_blank\">COVID-19 Data Tracker\u2019s \u201cVaccinations in the United States\u201d</a> site titled \u201cPrimary Series Completion, Booster Dose Eligibility, and Booster Dose Receipt by Age, United States\u201d.\n\n<b >Fully Vaccinated / Completed Primary Series:</b> <ul><li> For surveillance purposes, COVID Data Tracker counts people as being \"fully vaccinated\" or as having \"completed a primary series\" if they received two doses on different days (regardless of time interval) of the two-dose mRNA series or received one dose of a single-dose vaccine. When the vaccine manufacturer is not reported, the recipient is considered fully vaccinated with two doses.</li></ul><b>First Booster Dose:\u202f </b><ul><li>For surveillance purposes, the count and percentage of people who received a first booster dose includes anyone who is fully vaccinated and has received another dose of COVID-19 vaccine since August 13, 2021. This includes people who received a first booster dose and people who received an additional primary series dose as this metric does not distinguish if the recipient is <b><a href='https://www.cdc.gov/coronavirus/2019-ncov/vaccines/recommendations/immuno.html' target=\"_blank\">\u202fimmunocompromised and received an additional dose</a></b>.</li><li><b>   First booster dose eligibility: </b><ul><li>CDC counts people as being <b>\"\u202f<a href=\"https://www.cdc.gov/coronavirus/2019-ncov/vaccines/booster-shot.html\" target=\"_blank\">eligible for a first booster dose</a>\"</b> if it has been at least 5 months since completion of a Pfizer-BioNTech or Moderna primary series or at least 2 months since receipt of a Janssen (Johnson & Johnson) singe-dose vaccine. </li></ul></li></ul>\n<b>Second Booster Dose:</b><ul><li>For surveillance purposes, the count and percentage of people who received a second booster dose includes anyone who is fully vaccinated and has received two subsequent doses of COVID-19 vaccine since August 13, 2021. This includes people who received two booster doses and people who received one additional dose and one booster dose.\u202f </li><li>The count of people who received a second booster dose and the percentage of people with a first booster who received a second booster dose does not account for whether a person is <b><a href='https://www.cdc.gov/coronavirus/2019-ncov/vaccines/recommendations/immuno.html'  target=\"_blank\">immunocompromised or time interval since first booster dose</a></b>. </li><li><b>Second booster dose eligibility: </b><ul><li>CDC counts people as being\u202f <b>\"<a href=\"https://www.cdc.gov/coronavirus/2019-ncov/vaccines/booster-shot.html\" target=\"_blank\"><b>eligible for a second booster dose</b></a>\"\u202f</b> if it has been at least 4 months since receiving a first booster dose. </ul></li></li><li><b>Limitations to counting people with a second booster dose: </b>\n<ul><li>Due to the aggregate vaccination record reporting method used by Idaho for its residents under the age of 18 years and by Texas for all its residents, CDC counts all 4th doses received by these populations as a second booster dose. This includes immunocompromised individuals who received a three-dose primary series and only one booster dose. This limitation may lead to an undercount of people who received the single-dose J&J/Janssen vaccine as their primary series and two booster doses.</li></ul>\n</li></ul>Data represents all vaccine partners including jurisdictional partner clinics, retail pharmacies, long-term care facilities, dialysis centers, Federal Emergency Management Agency and Health Resources and Services Administration partner sites, and federal entity facilities.",
+            "title": "COVID-19 Primary Series Completion, Booster Dose Eligibility, and Booster Dose Receipt by Age, United States\u00a0",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3pbe-qh9z/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3pbe-qh9z/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3pbe-qh9z/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3pbe-qh9z/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "US",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1D",
+            "theme": [
+                "Vaccinations"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:10"
+            ],
+            "landingPage": "https://healthdata.gov/d/r4a9-ub25",
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2014-12-01",
+            "keyword": [
+                "information center; foods help desk"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FDA Enterprise Data Inventory",
+                "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "identifier": "A6EEDE4E-01A2-4167-A196-87066F135C34",
+            "description": "This system supports the Information Center's Help Desk capabilities, and reports can be exported.",
+            "title": "CFSAN Knowledge Management System",
+            "programCode": [
+                "009:001"
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/9kpc-xntn",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-14",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Chemical and Biochemical Monitoring Branch (CBMB), Health Effects Laboratory Division (HELD)",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/9kpc-xntn",
+            "description": "The goal of the experimental design and research presented herein was to produce peracetic acid (PAA) atmospheres suitable for evaluating PAA sampling methods in a controlled environment. To achieve this, generated test atmospheres must: enable simultaneous exposure of multiple samplers to equivalent atmospheres; maintain a continuous stable atmosphere for a duration to exceed experimental time frames; and produce a range of analyte concentrations, air velocities, temperatures and humidities. The American Conference of Governmental Industrial Hygienists (AGCIH) Threshold Limit Value (TLV) for PAA is 0.4 ppm. The goal was to generate PAA atmospheres with concentrations from one tenth of the TLV up to 100 times the TLV.\n\nPAA is a reactive chemical, which presents some inherent challenges to generation of standard reference materials and atmospheres. PAA is a strong oxidant. PAA solutions are labile, thus it is difficult to keep reference standards or atmospheres. In solution, PAA and water are in equilibrium with acetic acid (AA) and hydrogen peroxide (HP). The equilibrium shifts as solutions of PAA evolve oxygen gas through the degradation of HP. Dynamic PAA atmospheres which are flowing and continuously refreshed are the preferred method for exposing samplers to equivalent atmospheres. Generation of static atmospheres by evaporating PAA solution into a closed container cannot be maintained for very long before needing to be refreshed. Dynamically generated atmospheres are created by a continuously renewed flow of air as a carrier and a source of PAA vapors, which are necessary for evaluating sensor performance over time frames relevant to occupational safety.\n\nGeneration of PAA vapors can be accomplished from assisted vaporization, including applying heat and/or aerosolization with a nebulizer to accelerate evaporation. Glass reacts with PAA to hydroxylate the silica. used a glass syringe to deliver PAA solution to a nebulizer; however, gas bubbles formed in the syringe leading to uncontrollable ejection of the PAA solution from the syringe. To mitigate this, used acid washed syringes. They generated atmospheres of up to 2 ppm with a reported 95% recovery of theoretical delivered PAA. Dilute solutions of PAA can help to mitigate gas evolution but require more energy to evaporate and introduce additional humidity.\n\nFor these experiments, PAA vapors were swept directly from the headspace above a PAA solution into our generation system. The flow rate of the air sweeping the headspace was varied to achieve the desired concentration after dilution into the carrier gas stream. When evaporating diluted PAA solutions using a nebulizer, the minimum humidity range is limited due to the water content in the dilute PAA solution. Thus, a wider humidity range on the low end is available when sweeping the headspace. The ability to maintain the concentration of PAA in the headspace above the solution is limited by the kinetics at the PAA solution-air interface. A practical solution was achieved using a PAA delivery system where air was passed through the headspace above a PAA solution in a vial. An impinger with a N,N-diethyl-p-phenylenediamine (DPD) analysis was used as the reference measurement for the PAA concentrations in the generated atmospheres.",
+            "title": "Controlled Generation of Peracetic Acid Atmospheres for the Evaluation of Chemical Samplers",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/9kpc-xntn/application/x-zip-compressed",
+                    "mediaType": "application/x-zip-compressed"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "National Institute for Occupational Safety and Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/p8ia-4jqj",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-04-24",
+            "@type": "dcat:Dataset",
+            "modified": "2020-01-02",
+            "keyword": [
+                "2019",
+                "cryptosporidiosis",
+                "cyclosporiasis",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/p8ia-4jqj",
+            "description": "NNDSS - Table 1I. Cryptosporidiosis to Cyclosporiasis - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1I. Cryptosporidiosis to Cyclosporiasis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/p8ia-4jqj/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/p8ia-4jqj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/p8ia-4jqj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/p8ia-4jqj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "restricted public",
+            "landingPage": "https://www.cdc.gov/nchs/data-linkage/nhcs-hud.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "issued": "2022-06-23",
+            "@type": "dcat:Dataset",
+            "temporal": "2013/2017",
+            "modified": "2024-10-11",
+            "references": [
+                "https://www.cdc.gov/nchs/data/datalinkage/NHCS-Linked-HUD-Program-Participation-Any.pdf"
+            ],
+            "keyword": [
+                "linked hud data",
+                "nhcs",
+                "research-data-center"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NCHS Data Linkage Program",
+                "hasEmail": "mailto:DataLinkage@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/qfu5-aeqe",
+            "description": "Through its data linkage program, NCHS has been able to expand the analytic utility of the data collected from the 2014 and 2016\u00a0National Hospital Care Surveys (NHCS)\u00a0by linking patient records with up to three years of administrative housing data from the U.S. Department of Housing and Urban Development\u2019s (HUD) largest housing assistance programs: the Housing Choice Voucher (HCV) program, Public Housing (PH) , and privately owned, subsidized Multifamily housing (MF). These innovative linked data will support a wide array of patient outcomes studies, including the opportunity to study complex relationships between housing and health.",
+            "title": "National Hospital Care Survey (NHCS) linked to Department of Housing and Urban Development (HUD) Administrative Housing Data",
+            "isPartOf": "https://www.cdc.gov/nchs/data-linkage/index.htm",
+            "describedByType": "application/pdf",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "spatial": "United States",
+            "describedBy": "Match status can be found in the match rate table (see Table 1 on page 11) here: https://www.cdc.gov/nchs/data/datalinkage/NHCS-HUD-Linkage-Methods-and-Analytic-Considerations.pdf",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.fda.gov/DataSets/Recalls/Food/Food.xml",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "recalls"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "openFDA",
+                "hasEmail": "mailto:open@fda.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "identifier": "cdaa413b-325f-4f81-a78e-f8e55ac77098",
+            "description": "Press Releases of food recalls from industry",
+            "title": "Food Recalls",
+            "programCode": [
+                "009:001"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fda.gov/DataSets/Recalls/Food/Food.xml",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.neuromorpho.org/",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2016-07-17",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "GNADT, JAMES W\u00a0",
+                "hasEmail": "mailto:gnadtjw@ninds.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
+            "identifier": "95a4d2ef-29d6-4c6d-9a32-339fe4d9771f",
+            "description": "<p>NeuroMorpho.Org is a centrally curated inventory of digitally reconstructed neurons associated with peer-reviewed publications. It contains contributions from over 80 laboratories worldwide and is continuously updated as new morphological reconstructions are collected, published, and shared.</p>",
+            "title": "NeuroMorpho",
+            "programCode": [
+                "009:054"
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/r6pz-e6cq",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2025-01-18",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-17",
+            "keyword": [
+                "chip",
+                "demographics",
+                "geography",
+                "medicaid",
+                "rural",
+                "t-msis analytic files",
+                "urban"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "73fdbf7c-569e-427b-9bff-eeed34a51dcb",
+            "description": "This data set includes annual counts and percentages of Medicaid and Children\u2019s Health Insurance Program (CHIP) enrollees by urban or rural residence. Results are shown overall; by state; and by four subpopulation topics: scope of Medicaid and CHIP benefits, race and ethnicity, disability-related eligibility category, and managed care participation.\r\nThese results were generated using Transformed Medicaid Statistical Information System (T-MSIS) Analytic Files (TAF) Release 1 data and the Race/Ethnicity Imputation Companion File. This data set includes Medicaid and CHIP enrollees in all 50 states, the District of Columbia, Puerto Rico, and the U.S. Virgin Islands who were enrolled for at least one day in the calendar year, except where otherwise noted. Enrollees in Guam, American Samoa, and the Northern Mariana Islands are not included. Results shown overall (where subpopulation topic is \"Total enrollees\") and for the race and ethnicity subpopulation topic exclude enrollees in the U.S. Virgin Islands. Results shown for the race and ethnicity, disability category, and managed care participation subpopulation topics only include Medicaid and CHIP enrollees with comprehensive benefits. Results shown for the disability category subpopulation topic only include working-age adults (ages 19 to 64). Results for states with TAF data quality issues in the year have a value of \"Unusable data.\" Some rows in the data set have a value of \"DS,\" which indicates that data were suppressed according to the Centers for Medicare & Medicaid Services\u2019 Cell Suppression Policy for values between 1 and 10.\r\nThis data set is based on the brief: \"Rural Medicaid and CHIP enrollees in 2020.\" Enrollees are assigned to an urban or rural category based on the 2010 Rural-Urban Commuting Area (RUCA) code associated with their home or mailing address ZIP code in TAF. Enrollees are assigned to the comprehensive benefits or limited benefits subpopulation according to the criteria in the \"Identifying Beneficiaries with Full-Scope, Comprehensive, and Limited Benefits in the TAF\" DQ Atlas brief. Enrollees are assigned to a race and ethnicity subpopulation using the state-reported race and ethnicity information in TAF when it is available and of good quality; if it is missing or unreliable, race and ethnicity is indirectly estimated using an enhanced version of Bayesian Improved Surname Geocoding (BISG) (Race and ethnicity of the national Medicaid and CHIP population in 2020). Enrollees are assigned to a disability category subpopulation using their latest reported eligibility group code and age in the year (Medicaid enrollees who qualify for benefits based on disability in 2020). Enrollees are assigned to a managed care participation subpopulation based on the managed care plan type code that applies to the majority of their enrolled-months during the year (Enrollment in CMC Plans). Please refer to the full brief for additional context about the methodology and detailed findings. Future updates to this data set will include more recent data years as the TAF data become available.",
+            "title": "Rural Medicaid and CHIP enrollees",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/rural-residence-2020-2022-01162025.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/r6ud-pman",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-12-10",
+            "@type": "dcat:Dataset",
+            "modified": "2024-12-18",
+            "keyword": [
+                "benefits and cost sharing",
+                "exchange puf",
+                "marketplace puf",
+                "py2025"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Center for Consumer Information and Insurance Oversight",
+                "hasEmail": "mailto:CMS_FEPS@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "identifier": "8060e816-b052-42b3-ad60-9eac699d7c8b",
+            "description": "The Benefits and Cost Sharing PUF (BenCS-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The BenCS-PUF contains plan variant-level data on essential health benefits, coverage limits, and cost sharing for each QHP and SADP.",
+            "title": "Benefits and Cost Sharing PUF - PY2025",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2025/Benefits_Cost_Sharing_PUF.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/r74b-4d67",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-10-30",
+            "@type": "dcat:Dataset",
+            "modified": "2022-06-13",
+            "keyword": [
+                "medicaid"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "72135da5-f8b4-475b-b602-91621f4205d9",
+            "description": "Dataset.",
+            "title": "2019 Managed Care Programs By State",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/2019_Table9_10_0.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/y2iy-8irm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-09-10",
+            "@type": "dcat:Dataset",
+            "modified": "2021-09-10",
+            "keyword": [
+                "covid-19",
+                "executive order",
+                "government order",
+                "legal epidemiology",
+                "mitigation",
+                "proclamation",
+                "public health order",
+                "shelter-in-place",
+                "social distancing",
+                "stay-at-home"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Craig Kassinger",
+                "hasEmail": "mailto:cak8@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/y2iy-8irm",
+            "description": "State and territorial executive orders, administrative orders, resolutions, and proclamations are collected from government websites and cataloged and coded using Microsoft Excel by one coder with one or more additional coders conducting quality assurance.\n\nData were collected to determine when individuals in states and territories were subject to executive orders, administrative orders, resolutions, and proclamations for COVID-19 that require or recommend people stay in their homes. Data consists exclusively of state and territorial orders, many of which apply to specific counties within their respective state or territory; therefore, data is broken down to the county level.\n\nThese data are derived from the publicly available state and territorial executive orders, administrative orders, resolutions, and proclamations (\u201corders\u201d) for COVID-19 that expressly require or recommend individuals stay at home found by the CDC, COVID-19 Community Intervention and At-Risk Task Force, Monitoring and Evaluation Team & CDC, Center for State, Tribal, Local, and Territorial Support, Public Health Law Program from March 15, 2020 through August 15, 2021. These data will be updated as new orders are collected. Any orders not available through publicly accessible websites are not included in these data. Only official copies of the documents or, where official copies were unavailable, official press releases from government websites describing requirements were coded; news media reports on restrictions were excluded. Recommendations not included in an order are not included in these data. These data do not include mandatory business closures, curfews, or limitations on public or private gatherings. These data do not necessarily represent an official position of the Centers for Disease Control and Prevention.",
+            "title": "U.S. State and Territorial Stay-At-Home Orders: March 15, 2020 \u2013 August 15, 2021 by County by Day",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/y2iy-8irm/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/y2iy-8irm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/y2iy-8irm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/y2iy-8irm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Policy Surveillance"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.ncbi.nlm.nih.gov/genbank/TPA.html",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2022-03-02",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "computational biology",
+                "dataset",
+                "genomics"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Library of Medicine",
+                "hasEmail": "mailto:custserv@nlm.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/eg2g-944h",
+            "description": "A database that contains sequences built from the existing primary sequence data in GenBank. The sequences and corresponding annotations are experimentally supported and have been published in a peer-reviewed scientific journal.",
+            "title": "Third Party Annotation (TPA) Database",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/genbank/tpa/",
+                    "mediaType": "text/html",
+                    "title": "About Third Party Annotation (TPA) Database"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/genbank/TPA-Exp",
+                    "description": "Annotation of sequence data is supported by peer-reviewed wet-lab experimental evidence.",
+                    "@type": "dcat:Distribution",
+                    "title": "Third Party Annotation (TPA) Database: Experimental"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/genbank/TPA-Inf",
+                    "description": "Annotation of sequence data by inference (where the source molecule or its product(s) have not been the subject of direct experimentation)",
+                    "@type": "dcat:Distribution",
+                    "title": "Third Party Annotation (TPA) Database: Inferential"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Molecular biology/Genetics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/n5qs-vw3x",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-10-03",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-13",
+            "keyword": [
+                "coronavirus",
+                "covid",
+                "covid cases",
+                "covid deaths",
+                "covid-19",
+                "dialysis",
+                "hemodialysis",
+                "sars-cov-2"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC-INFO",
+                "hasEmail": "mailto:cdcinfo@cdcinquiry.onmicrosoft.com"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/n5qs-vw3x",
+            "description": "Mandated reporting of Weekly Aggregate Case and Death Count data among dialysis patients and dialysis facility staff (healthcare personnel or HCP) in the United States was discontinued May 11, 2023, with the expiration of the COVID-19 public health emergency declaration. This dataset will contain weekly aggregate data from January 1, 2021, through May 10, 2023, and will remain publicly available.\n\nThis archived public use dataset contains reported COVID-19 case and death data per week for all states and territories, along with weekly totals for the entire United States, throughout the given timeframe.",
+            "title": "Weekly United States COVID-19 Cases and Deaths among Dialysis Patients - ARCHIVED",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/n5qs-vw3x/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/n5qs-vw3x/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/n5qs-vw3x/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/n5qs-vw3x/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States",
+            "license": "https://www.usa.gov/government-works",
+            "theme": [
+                "Case Surveillance"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.nlm.nih.gov/research/umls/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2016-08-04",
+            "@type": "dcat:Dataset",
+            "modified": "2022-09-30",
+            "keyword": [
+                "api",
+                "dataset",
+                "health data standards",
+                "terminologies"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Library of Medicine",
+                "hasEmail": "mailto:custserv@nlm.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/9t6e-u9qh",
+            "description": "The UMLS integrates and distributes key terminology, classification and coding standards, and associated resources to promote creation of more effective and interoperable biomedical information systems and services, including electronic health records.",
+            "title": "Unified Medical Language System (UMLS)",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.nlm.nih.gov/research/umls/licensedcontent/umlsknowledgesources.html",
+                    "mediaType": "text/html",
+                    "title": "Download UMLS Data - Knowledge Sources"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://documentation.uts.nlm.nih.gov/",
+                    "description": "The UTS API is intended for application developers to perform Web service calls and retrieve UMLS data within their own applications. The UTS API provides the ability to search, retrieve, and filter terms, concepts, attributes, relations, metadata and more from over 160 vocabularies of the UMLS Metathesaurus, as well as the Semantic Network. Paging, sorting and filtering (PSF) capabilities allows users to customize results of Web service calls in many ways: choose to include or exclude specific criteria, sort results by fields, or specify results displayed per page. The documentation provides a suite of Web Services Description Language (WSDL) files, API installation instructions, and sample code.",
+                    "@type": "dcat:Distribution",
+                    "title": "API"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://uts.nlm.nih.gov/metathesaurus.html",
+                    "mediaType": "text/html",
+                    "title": "Search UMLS Metathesaurus"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.nlm.nih.gov/research/umls/licensedcontent/downloads.html",
+                    "mediaType": "text/html",
+                    "title": "Download UMLS Data - Vocabulary Standards and Mappings"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Terminology"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/rcdh-n3ej",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-01-14",
+            "@type": "dcat:Dataset",
+            "modified": "2022-02-11",
+            "keyword": [
+                "2022",
+                "nedss",
+                "netss",
+                "nndss",
+                "salmonella paratyphi infection",
+                "salmonella typhi infection",
+                "salmonellosis (excluding salmonella typhi infection and salmonella paratyphi infection)",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/rcdh-n3ej",
+            "description": "NNDSS - TABLE 1EE. Salmonella Paratyphi infection to Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection) \u2013 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
+            "title": "NNDSS - TABLE 1EE. Salmonella Paratyphi infection to Salmonellosis (excluding Salmonella Typhi infection and Salmonella Paratyphi infection)",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rcdh-n3ej/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rcdh-n3ej/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rcdh-n3ej/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rcdh-n3ej/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/vagq-bwyc",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-15",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Health Effects Laboratory Division, Toxicology and Molecular Biology Branch",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/vagq-bwyc",
+            "description": "Loading-induced hypertrophy with transcriptional upregulation has been observed concomitant with nuclei accretion in various studies regarding both humans and rodents.   Bruusgaard et al. in 2010 pioneered work utilizing a model of synergist ablation to cause hypertrophy followed by denervation-induced atrophy to demonstrate that load-induced gains in myonuclei could be long-lasting after the termination of such exposure.  This finding was consistent with the idea of enduring myonuclear accretion as a form of \u201cmuscle memory\u201d allowing enhanced muscle adaptation following a period of detraining.  Subsequent research groups further investigated this possibility in the context of exercise utilizing rodents and various loaded exercise paradigms such as weighted wheel running and ladder climbing.  This research yielded a spectrum of results.  While these studies were instrumental in highlighting the variation in outcomes possible following load-induced hypertrophy in general, they were limited in their direct relatedness to resistance training \u2013 the predominate form of exposure utilized to induce hypertrophy.  Our research group has established and repeatedly validated a rat research model to investigate resistance-type training.   The model is based on using a dynamometer to precisely expose dorsiflexor muscles of rats to 8 sets of 10 repetitions (per set) of stretch-shortening contractions (SSCs) \u2013 a consecutive sequence of isometric, lengthening, and shortening contractions.  Training with this exposure 3 sessions per week for one month results in increases in muscle mass and performance.  This is accompanied by an increase in muscle fiber area accompanied by a proportional increase in myonuclei number and a rise in overall transcriptional output as measured by total RNA levels.  The purpose of the present study was to determine to what extent alterations in performance, muscle mass, nuclei number, and transcriptional output persist several months following the termination of this relevant and valid model of resistance-type training.",
+            "title": "Elevated muscle mass accompanied by transcriptional and nuclear alterations several months following cessation of resistance-type training in rats",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/vagq-bwyc/application/x-zip-compressed",
+                    "mediaType": "application/x-zip-compressed"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "National Institute for Occupational Safety and Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-05-12",
+            "@type": "dcat:Dataset",
+            "temporal": "2015-01-04/2021-07-03",
+            "modified": "2023-11-16",
+            "keyword": [
+                "all causes",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "hospital referral region",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "united states",
+                "weekly"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/mqmc-4b9n",
+            "description": "Provisional count of deaths involving coronavirus disease 2019 (COVID-19) in the United States by week of death and by hospital referral region (HRR). HRR is determined by county of occurrence. Weekly weighted counts of deaths from all causes and due to COVID-19 are provided by HRR overall and for decedents 65 years and older. The weighted counts by HRRs are based on published methods for aggregating county-level data to HRRs. More detail about aggregating to HRRs from counties can be found in the following: https://github.com/Dartmouth-DAC/covid-19-hrr-mapping\nhttps://dartmouthatlas.org/covid-19/hrr-mapping/",
+            "title": "AH Provisional COVID-19 Deaths by Hospital Referral Region",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mqmc-4b9n/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mqmc-4b9n/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mqmc-4b9n/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mqmc-4b9n/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "irregular",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/covid19/excess_deaths.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2020-05-28",
+            "@type": "dcat:Dataset",
+            "modified": "2023-09-27",
+            "keyword": [
+                "alzheimer disease",
+                "cancer",
+                "causes of death",
+                "cerebrovascular disease",
+                "chronic lower respiratory disease",
+                "circulatory disease",
+                "deaths",
+                "dementia",
+                "diabetes",
+                "heart failure",
+                "hypertensive disease",
+                "influenza",
+                "ischemic heart disease",
+                "mortality",
+                "nchs",
+                "nvss",
+                "pneumonia",
+                "provisional",
+                "puerto rico",
+                "renal failure",
+                "respiratory disease",
+                "septicemia",
+                "state",
+                "united states",
+                "weekly"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/u6jv-9ijr",
+            "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nThis visualization provides weekly data on the number of deaths by jurisdiction of occurrence and cause of death. Counts of deaths in more recent weeks can be compared with counts from earlier years to determine if the number is higher than expected. Selected causes of death are shown, based on analyses of the most prevalent comorbid conditions reported on death certificates where COVID-19 was listed as a cause of death (see https://www.cdc.gov/nchs/nvss/vsrr/covid_weekly/index.htm#Comorbidities). Cause of death counts are based on the underlying cause of death, and presented for Respiratory diseases, Circulatory diseases, Malignant neoplasms, and Alzheimer disease and dementia. Estimated numbers of deaths due to these other causes of death could represent misclassified COVID-19 deaths, or potentially could be indirectly related to COVID-19 (e.g., deaths from other causes occurring in the context of health care shortages or overburdened health care systems). Deaths with an underlying cause of death of COVID-19 are not included in these estimates of deaths due to other causes. Deaths due to external causes (i.e. injuries) or unknown causes are excluded. For more detail, see the Technical Notes.",
+            "title": "Weekly Counts of Death by Jurisdiction and Select Causes of Death",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/u6jv-9ijr/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/u6jv-9ijr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/u6jv-9ijr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/u6jv-9ijr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States, Puerto Rico",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "irregular",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-07-15",
+            "@type": "dcat:Dataset",
+            "modified": "2024-08-26",
+            "references": [
+                "https://www.cdc.gov/places/measure-definitions/index.html"
+            ],
+            "keyword": [
+                "behaviors",
+                "county",
+                "disability",
+                "gis",
+                "health",
+                "outcomes",
+                "places",
+                "prevalence",
+                "prevention",
+                "risk",
+                "status"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "PLACES Public Inquiries",
+                "hasEmail": "mailto:places@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/7cmc-7y5g",
+            "description": "This dataset contains model-based county-level estimates in GIS-friendly format. PLACES covers the entire United States\u201450 states and the District of Columbia\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. Project was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2021 or 2020 data, Census Bureau 2021 or 2020 county population estimates, and American Community Survey (ACS) 2017\u20132021 or 2016\u20132020 estimates. The 2023 release uses 2021 BRFSS data for 29 measures and 2020 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours) that the survey collects data on every other year. These data can be joined with the census 2020 county boundary file in a GIS system to produce maps for 36 measures at the county level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software.\nhttps://cdcarcgis.maps.arcgis.com/home/item.html?id=2c3deb0c05a748b391ea8c9cf9903588",
+            "title": "PLACES: County Data (GIS Friendly Format), 2023 release",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7cmc-7y5g/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7cmc-7y5g/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7cmc-7y5g/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7cmc-7y5g/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "500 Cities & Places"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225437.htm",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2010-10-01",
+            "keyword": [
+                "health",
+                "hvp",
+                "hydrolyzed vegetable protein",
+                "market",
+                "notifications",
+                "recalls",
+                "safety"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "FDA Enterprise Data Inventory",
+                "hasEmail": "mailto:FDA_Enterprise_Data_Inventory@fda.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "identifier": "1281388f-93e7-4c1c-9369-5143ec0fdb8e",
+            "description": "Contains data for FDA Hydrolyzed Vegetable Protein (HVP) Containing Products recalls since February, 2010.",
+            "title": "FDA Hydrolyzed Vegetable Protein (HVP) Containing Products Recalls Widget",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225437.htm",
+                    "mediaType": "application/vnd.ms-excel"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "restricted public",
+            "landingPage": "https://data.cdc.gov/d/vxpx-d2pt",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "issued": "2022-06-15",
+            "@type": "dcat:Dataset",
+            "temporal": "2020",
+            "modified": "2023-04-24",
+            "keyword": [
+                "anxiety",
+                "covid-19",
+                "depression",
+                "missed healthcare",
+                "research-data-center",
+                "telemedicine"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/vxpx-d2pt",
+            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys from probability-sampled commercial survey panels. As part of a special iteration of RANDS that focuses on COVID-19, RANDS during COVID-19 Round 1 is the first round of a three-round survey. In addition to the probability sample in RANDS during COVID-19 Round 1, the questionnaire was administered to the Dynata non-probability online opt-in sample by NORC at the University of Chicago (NORC) from June 9, 2020 to June 30, 2020. The RANDS during COVID-19 Round 1 Non-Probability Sample does not have a known survey sampling design and cannot be used to produce nationally or sub-nationally representative estimates.",
+            "title": "NCHS Research and Development Survey (RANDS) Round 1 during COVID-19 non-probability sampled Restricted File",
+            "describedByType": "application/pdf",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "spatial": "50 states and District of Columbia",
+            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS_COVID_1_np_technical_documentation.pdf",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/raru-q8p9",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-04-12",
+            "@type": "dcat:Dataset",
+            "modified": "2023-04-10",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "fa6bdb2e-a9ac-4f7c-8d10-5549f8146754",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-04-03-to-2023-04-09",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rprt-drug-4-03-2023-to-4-09-2023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-04-03-to-2023-04-09"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/statesystem/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-07-18",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-10",
+            "references": [
+                "https://chronicdata.cdc.gov/d/5qag-uzp2"
+            ],
+            "keyword": [
+                "legislation",
+                "osh",
+                "policy",
+                "preemption",
+                "state system",
+                "tobacco"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "OSHData Support",
+                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/xsta-sbh5",
+            "description": "1995-2024. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System. Legislation\u2014Preemption. The STATE System houses current and historical state-level legislative data on tobacco use prevention and control policies.  Data are reported on a quarterly basis. Data include information related to statutory state preemption of more stringent local laws on advertising, smokefree indoor air, youth access and licensure.",
+            "title": "CDC STATE System Tobacco Legislation - Preemption",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xsta-sbh5/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xsta-sbh5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xsta-sbh5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xsta-sbh5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-Tobacco-Legislation-Preemption/xsta-sbh5",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "theme": [
+                "Legislation"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/rbee-8ezs",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2017-12-13",
+            "@type": "dcat:Dataset",
+            "modified": "2018-08-22",
+            "keyword": [
+                "medicaid"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Jeff Chamblee",
+                "hasEmail": "mailto:no-reply@data.medicaid.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "0e112ea8-8e8e-5dee-a7e2-7ed551c3baa4",
+            "description": "Provides program names, program features, population enrolled, benefits covered, quality assurance and improvement, performance incentives, provider value-based purchasing, participating plans, regions served and program notes.",
+            "title": "Managed Care Programs by State",
+            "programCode": [
+                "009:076"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/managed-care-programs-by-state.p9c7-tuup.csv",
+                    "mediaType": "text/csv",
+                    "title": "CSV"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P10Y",
+            "theme": [
+                "Enrollment"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "issued": "2022-08-30",
+            "@type": "dcat:Dataset",
+            "modified": "2022-08-30",
+            "keyword": [
+                "all causes",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "united states",
+                "weekly"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/6mjs-pnrx",
+            "description": "Provisional counts of deaths involving coronavirus disease 2019 (COVID-19) by week and age group, in the United States.",
+            "title": "AH Provisional COVID-19 Deaths by Week and Age",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6mjs-pnrx/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6mjs-pnrx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6mjs-pnrx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6mjs-pnrx/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "irregular",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/8ihh-n7ic",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2016-10-18",
+            "@type": "dcat:Dataset",
+            "modified": "2016-10-18",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/8ihh-n7ic",
+            "description": "Rate of deaths by age/gender (per 100,000 population) for motor vehicle occupants killed in crashes, 2012 & 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Safety Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
+            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014, Region 6 - Dallas",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8ihh-n7ic/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8ihh-n7ic/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8ihh-n7ic/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8ihh-n7ic/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Motor Vehicle"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.nlm.nih.gov/mesh/meshhome.html",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2020-08-06",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "api",
+                "dataset",
+                "health data standards",
+                "terminologies"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Library of Medicine",
+                "hasEmail": "mailto:custserv@nlm.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/arcv-nkd5",
+            "description": "Medical Subject Headings (MeSH) is a hierarchically-organized terminology for indexing and cataloging of biomedical information. It is used for the indexing of PubMed and other NLM databases. Please see the Terms and Conditions for more information regarding the use and re-use of MeSH. NLM produces Medical Subject Headings XML, ASCII, MARC 21 and RDF formats. \n\nUpdates to the data files are made according to the following schedule:\n\nMeSH XML\nMeSH Descriptor files updated annually\nMeSH Qualifier files updated annually\nMeSH Supplemental Concept Records (SCR) updated daily (Monday - Friday)\n\nMeSH ASCII\nMeSH Descriptor files updated annually\nMeSH Qualifier files updated annually\nMeSH Supplemental Concept Records (SCR) updated daily (Monday - Friday)\n\nMeSH MARC21\nAll files posted monthly\n\nMeSH RDF\nAll files posted daily (Monday - Friday)",
+            "title": "Medical Subject Headings (MeSH)",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://nlmpubs.nlm.nih.gov/projects/mesh/rdf/2022/",
+                    "mediaType": "application/rdf+xml",
+                    "title": "Download - MeSH - Current Production Year"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://nlmpubs.nlm.nih.gov/projects/mesh/MESH_FILES/xmlmesh/",
+                    "mediaType": "application/xml",
+                    "title": "Download - MeSH - Current Production Year"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://nlmpubs.nlm.nih.gov/projects/mesh/MESH_FILES/meshmarc/",
+                    "mediaType": "text/html",
+                    "title": "Download - MeSH - Current Production Year"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://nlmpubs.nlm.nih.gov/projects/mesh/MESH_FILES/asciimesh/",
+                    "mediaType": "text/html",
+                    "title": "Download - MeSH - Current Production Year"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://nlmpubs.nlm.nih.gov/projects/mesh/",
+                    "description": "Directories 1999-2010\n-All the yearly release files produced by MeSH from 1999 to 2010\n\nDirectories 2011-2016\n-These directories contain the yearly release file of MeSH. These files are distributed in November of the prior MeSH year and do not get updated.\n\nRDF MESH N-TRIPLE DATA folders - for info see https://id.nlm.nih.gov/mesh/",
+                    "@type": "dcat:Distribution",
+                    "title": "Download - MeSH - Archive of Prior Production Years"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://id.nlm.nih.gov/mesh/swagger/ui#/",
+                    "description": "The SPARQL 1.1 endpoint returns RDF results and graphs.  The lookup API returns simple JSON.",
+                    "@type": "dcat:Distribution",
+                    "title": "API - MeSH RDF SPARKL endpoint"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://meshb.nlm.nih.gov/search",
+                    "description": "The browser offers two search methods: FullWord Search and SubString Search.  Each method can be further modified to search by Exact Match, All Fragments, or Any Fragment.  ",
+                    "@type": "dcat:Distribution",
+                    "title": "Query Interface - MeSH Browser - Current Production Year"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://id.nlm.nih.gov/mesh/",
+                    "description": "Resources supporting the RDF serialization of the Medical Subject Headings (MeSH).",
+                    "@type": "dcat:Distribution",
+                    "title": "MeSH RDF Resources"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Terminology"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/dataset/substance-abuse-treatment-facilities-locator",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2012-12-14",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "drug and alcohol abuse treatment facilities",
+                "health care providers"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Substance Abuse & Mental Health Services Administration, Department of Health & Human Services"
+            },
+            "identifier": "c6c074c3-e676-48f1-be33-a412b846e7bb",
+            "description": "<p>The Substance Abuse and Mental Health Services Administration (SAMHSA) provides on-line resource for locating drug and alcohol abuse treatment programs. The Substance Abuse Treatment Facility Locator lists:</p>\n<p>Private and public facilities that are licensed, certified, or otherwise approved for inclusion by their State substance abuse agency</p>\n<p>Treatment facilities administered by the Department of Veterans Affairs, the Indian Health Service and the Department of Defense.</p>\n<p>SAMHSA endeavors to keep the Locator current. All information in the Locator is completely updated each year, based on facility responses to SAMHSA's National Survey of Substance Abuse Treatment Services. The most recent complete update occurred on April 16, 2012 based on data collected as of March 31, 2011 in the National Survey of Substance Abuse Treatment Services. New facilities are added monthly. Updates to facility names, addresses, telephone numbers and services are made weekly, if facilities inform SAMHSA of changes.</p>",
+            "title": "Substance Abuse Treatment Facilities Locator",
+            "programCode": [
+                "009:068"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://findtreatment.samhsa.gov/locator.html",
+                    "mediaType": "text/html",
+                    "title": "HTML"
+                }
+            ],
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "dataQuality": true
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/rcra-yvyi",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2016-09-22",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-08",
+            "keyword": [
+                "drug products",
+                "drug rebate program"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "0ad65fe5-3ad3-5d79-a3f9-7893ded7963a",
+            "description": "Active drugs that have been reported by participating drug manufacturers under the Medicaid Drug Rebate Program. All drugs are identified by National Drug Code (NDC), unit type, units per package size, product name, Food and Drug Administration (FDA) approval date, the date the drug entered the market, plus indicators to show whether the drug is an innovator or non-innovator drug; whether it is available by prescription or over-the-counter (OTC); the FDA therapeutic equivalency code; and the Drug Efficacy Study Implementation (DESI) rating and termination date. Each quarter posted represents a snapshot of data in the system at that time and is not updated by subsequent changes.",
+            "title": "Drug Products in the Medicaid Drug Rebate Program",
+            "programCode": [
+                "009:076"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/drugproducts3q_2024_Updated11082024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Drug Products in the Medicaid Drug Rebate Program"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P10Y",
+            "theme": [
+                "Drug Pricing and Payment"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/re3e-j6wf",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2024-11-20",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-10",
+            "references": [
+                "https://www.mathematica.org/"
+            ],
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "78950031-dea0-53d7-9247-d5affba75d96",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "CoreSet measure_value v2.10.64 (coreset-impl)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/measure_value.csv",
+                    "description": "CoreSet measure_value v2.10.64 (coreset-impl)",
+                    "@type": "dcat:Distribution",
+                    "title": "CoreSet measure_value v2.10.64 (coreset-impl)"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/cygf-tgyd",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-15",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Allergy and Clinical Immunology Branch (ACIB), Health Effects Laboratory Division (HELD)",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/cygf-tgyd",
+            "description": "Allergic airway diseases are a growing concern in industrialized nations and can be influenced by fungal exposures. Pathogenic yeast species such as Cryptococcus neoformans are known to exacerbate allergic airway disease. Recent indoor assessments have identified Basidiomycota yeasts, including non-pathogenic species such as Vishniacozyma victoriae (syn. Cryptococcus victoriae), to be prevalent and potentially associated with asthma. However, the pulmonary immune response to repeated V. victoriae exposure was previously unexplored. This study aimed to compare the immunological impact of repeated pulmonary exposure to pathogenic and non-pathogenic Cryptococcus yeasts. Mice were repeatedly exposed to either C. neoformans, V. victoriae, or PBS control, and the immune responses were analyzed by measuring histopathological scores, and quantifications of immune cells in the bronchoalveolar lavage fluid or lung via flow cytometry, and cytokine concentrations in the lung. These findings highlight the importance of in vivo characterizations of exposures to frequently detected fungal organisms.",
+            "title": "Persisting Cryptococcus Yeast Species Vishniacozyma victoriae and Cryptococcus neoformans Elicit Unique Airway Inflammation in Mice Following Repeated Exposure",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/cygf-tgyd/application/x-zip-compressed",
+                    "mediaType": "application/x-zip-compressed"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "National Institute for Occupational Safety and Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/provider-summary-by-type-of-service/provider-service-classifications/restructured-betos-classification-system",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2024-01-01/2024-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-22",
+            "references": [
+                "https://data.cms.gov/sites/default/files/2024-10/2024%20RBCS%20Final%20Report.pdf"
+            ],
+            "keyword": [
+                "hospitals & facilities",
+                "medical suppliers & equipment",
+                "medicare",
+                "medicare advantage",
+                "original medicare",
+                "outpatient facilities",
+                "physicians & practitioners"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "PDAG Data Products - OEDA",
+                "hasEmail": "mailto:PDAG_Data_Products@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/e3db6e56-149f-49ce-b374-40aecda2357b/data-viewer",
+            "description": "The Restructured BETOS Classification System (RBCS) dataset\u00a0is a taxonomy that allows researchers to group healthcare service codes for Medicare Part B services (i.e., HCPCS codes) into clinically meaningful categories and subcategories. It is based on the original Berenson-Eggers Type of Service (BETOS) classification created in the 1980s, and includes notable updates such as Part B non-physician services.\u00a0The RBCS will undergo annual updates by a technical expert panel of researchers and clinicians.",
+            "title": "Restructured BETOS Classification System",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e3db6e56-149f-49ce-b374-40aecda2357b/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Restructured BETOS Classification System : 2024-10-04"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/30b74146-c5ce-47e0-8ae2-ad1204c81906/2024%20RBCS%20Taxonomy_CSV.csv",
+                    "mediaType": "text/csv",
+                    "title": "Restructured BETOS Classification System : 2024-10-04"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/aaeeb33a-1b8f-4f09-bffc-f9d194d9662f/data",
+                    "mediaType": "text/html",
+                    "title": "Restructured BETOS Classification System : 2024-10-04"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/rbcs-data-dictionary-2024",
+            "dataQuality": true,
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "Medicare"
+            ],
+            "language": [
+                "en-US"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/dhdsp/index.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-07-18",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-25",
+            "references": [
+                "https://www.cdc.gov/dhdsp/index.htm",
+                "https://www.cdc.gov/dhdsp/maps/dtm/data_sources.htm",
+                "https://www.cdc.gov/dhdsp/maps/dtm/data_risks.htm"
+            ],
+            "keyword": [
+                "cardiovascular disease",
+                "county",
+                "heart disease"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DHDSP Requests",
+                "hasEmail": "mailto:dhdsprequests@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/r35g-znws",
+            "description": "2012 to 2014, 3-year average. Rates are age-standardized. County rates are spatially smoothed. The data can be viewed by gender and race/ethnicity. Data source: National Vital Statistics System. Additional data, maps, and methodology can be viewed on the Interactive Atlas of Heart Disease and Stroke http://www.cdc.gov/dhdsp/maps/atlas",
+            "title": "Heart Disease Mortality Data Among US Adults (35+) by State/Territory and County",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/r35g-znws/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/r35g-znws/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/r35g-znws/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/r35g-znws/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Heart-Disease-Stroke-Prevention/Heart-Disease-Mortality-Data-Among-US-Adults-35-by/r35g-znws",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Heart Disease & Stroke Prevention"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-dashboard.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-09-30",
+            "@type": "dcat:Dataset",
+            "temporal": "2018-2023",
+            "modified": "2024-03-29",
+            "references": [
+                "CDC"
+            ],
+            "keyword": [
+                "flu",
+                "flu vaccination",
+                "influenza"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Vax Views",
+                "hasEmail": "mailto:VaxView@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/k87d-gv3u",
+            "description": "Weekly Cumulative Doses (in Millions) of Influenza Vaccine Distributed by Flu Season in the United States\n\n\u2022  Archived data are available here:  https://data.cdc.gov/resource/e5zk-7tx5 \n\u2022  Flu vaccine is produced by private manufacturers, so supply depends on manufacturers. Vaccine manufacturers have projected that they will supply the United States with as many as 173.5 million to 183.5 million doses of influenza vaccines for the 2022-2023 season. \n\u2022  Additional information is available:\u202fhttps://www.cdc.gov/flu/prevent/vaccine-supply-distribution.htm.",
+            "title": "Weekly Cumulative Doses (in Millions) of Influenza Vaccine Distributed by Flu Season in the United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/k87d-gv3u/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/k87d-gv3u/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/k87d-gv3u/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/k87d-gv3u/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Weekly",
+            "theme": [
+                "Vaccinations"
+            ],
+            "language": [
+                "English"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/rh4q-adeb",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-10-08",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-15",
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
+            ],
+            "keyword": [
+                "dqatlas",
+                "dqatlas_devauto",
+                "utility"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DataConnect Support Team",
+                "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "97ad1e5c-235e-5fcb-b7f0-be14d8d5c804",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "devAuto_measure_concernLevel",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_concernLevel.csv",
+                    "description": "{\"dataset\": \"measure_concernLevel\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "@type": "dcat:Distribution",
+                    "title": "measure_concernLevel csv file"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/PT1S",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/dataset/national-child-abuse-and-neglect-data-system-ncands-child-file",
+            "bureauCode": [
+                "009:70"
+            ],
+            "issued": "2013-01-18",
+            "temporal": "2010-01-01T00:00:00-05:00/2010-01-01T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "child abuse",
+                "child maltreatment",
+                "children",
+                "children's health",
+                "child safety",
+                "safety"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Hale, Malcolm",
+                "hasEmail": "mailto:malcolm.hale@acf.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Administration for Children and Families"
+            },
+            "identifier": "6820d1cb-0e93-4870-b6e0-4a33d84122c1_6_0",
+            "description": "<p>The National Child Abuse and Neglect Data System (NCANDS) Child File data set consists of child-specific data of all reports of maltreatment to State child protective service agencies that received an investigation or assessment response. NCANDS is a Federally-sponsored national data collection effort created for the purpose of tracking the volume and nature of child maltreatment reporting each year within the United States. The Child File is the case-level component of the NCANDS. Child File data are collected annually through the voluntary participation of States. Participating States submit their data after going through a process in which the State's administrative system is mapped to the NCANDS data structure.  Data elements include the demographics of children and their perpetrators, types of maltreatment, investigation or assessment dispositions, risk factors, and services provided as a result of the investigation or assessment.</p>",
+            "title": "National Child Abuse and Neglect Data System (NCANDS) Child File: Link to child file dataset for eligible members of the research community",
+            "programCode": [
+                "009:094"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.ndacan.acf.hhs.gov/datasets/datasets-list-ncands-child-file-dcdc.cfm",
+                    "mediaType": "text/html",
+                    "title": "Link to child file dataset for eligible members of the research community"
+                }
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1988",
+            "issued": "2016-05-23",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "alcohol abuse",
+                "alcohol consumption",
+                "amphetamines",
+                "barbiturates",
+                "cocaine",
+                "drug abuse",
+                "drugs",
+                "drug use",
+                "hallucinogens",
+                "heroin",
+                "households",
+                "inhalants",
+                "marijuana",
+                "methamphetamine",
+                "prescription drugs",
+                "sedatives",
+                "smoking",
+                "stimulants",
+                "substance abuse",
+                "substance abuse treatment",
+                "tobacco use",
+                "tranquilizers",
+                "youths"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Substance Abuse & Mental Health Services Administration"
+            },
+            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1988-nid13604",
+            "description": "<p>This series measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, anabolic steroids, and tobacco among members of United States households aged 12 and older. Questions include age at first use, as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, inhalants, cocaine, hallucinogens, heroin, alcohol, tobacco, and nonmedical use of psychotherapeutics. Respondents were also asked about problems resulting from their use of drugs, alcohol, and tobacco, their perceptions of the risks involved, insurance coverage, and personal and family income sources and amounts. Demographic data include gender, race, ethnicity, educational level, job status, income level, household composition, and population density.This study has 1 Data Set.</p>",
+            "title": "National Household Survey on Drug Abuse (NHSDA-1988)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1988-nid13604",
+                    "description": "National Household Survey on Drug Abuse (NHSDA-1988) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1988-nid13604"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/rnd6-9eip",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2024-11-20",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-15",
+            "references": [
+                "https://www.mathematica.org/"
+            ],
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "933971be-11d4-50e3-bcb0-38388796ac24",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "CoreSEt filters v2.10.22 (coreset-impl)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.22/20241029/filters.csv",
+                    "description": "CoreSEt filters v2.10.22 (coreset-impl)",
+                    "@type": "dcat:Distribution",
+                    "title": "CoreSEt filters v2.10.22 (coreset-impl)"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/rpi2-kmqe",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-10-08",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-07",
+            "references": [
+                "https://www.medicaid.gov/dq-atlas/welcome",
+                "https://www.mathematica.org/"
+            ],
+            "keyword": [
+                "dqatlas",
+                "dqatlas_prodauto",
+                "utility"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DataConnect Support Team",
+                "hasEmail": "mailto:dataconnectsupport@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "a4d6c830-21c6-5194-81b3-e69a3606ac78",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
+            "title": "prodAuto_topicArea_measureDisplayGroups",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/topicArea_measureDisplayGroups.csv",
+                    "description": "{\"dataset\": \"topicArea_measureDisplayGroups\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "@type": "dcat:Distribution",
+                    "title": "topicArea_measureDisplayGroups csv file"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/PT1S",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "non-public",
+            "landingPage": "https://data.cdc.gov/Laboratory-Surveillance/Percent-Positivity-of-Respiratory-Syncytial-Virus-/3cxc-4k8q",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-09-24",
+            "@type": "dcat:Dataset",
+            "temporal": "Data from 2020-04-11 to present",
+            "modified": "2025-01-30",
+            "keyword": [
+                "chronic lower respiratory disease",
+                "respiratory disease",
+                "respiratory syncytial virus",
+                "rsv"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Surveillance and Analytics Team",
+                "hasEmail": "mailto:nrevss@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/3cxc-4k8q",
+            "description": "More than 450 public health, clinical, and commercial laboratories located throughout the United States voluntarily participate in surveillance for respiratory syncytial virus (RSV) through CDC's National Respiratory and Enteric Virus Surveillance System (NREVSS) (https://www.cdc.gov/surveillance/nrevss/labs/index.html). The data contain weekly, aggregate counts of RSV tests performed and RSV detections as reported to NREVSS since April 11, 2020. \n\nNREVSS data are reported weekly at the national and 10 HHS regional levels (https://www.hhs.gov/about/agencies/iea/regional-offices/index.html). The presented data are RSV Nucleic Acid Amplification Test (NAAT) results, which include reverse transcription-polymerase chain reaction (RT-PCR) tests. These data exclude antigen, antibody, and at-home test results. Less than 5% of RSV tests reported to NREVSS are from antigen tests. All data are provisional and subject to change. Reporting is less complete for the most recent weeks, but relatively complete (>90%) for the period up to 2 weeks earlier. \n\nPercent positivity is a surveillance metric used to monitor RSV activity over time and by geographic area. Participating laboratories send weekly reports of the total number of RSV tests performed that week, and the number of those tests that were positive. In the table and upon hovering on the map, the total test counts reflect the latest data reported to NREVSS and may differ from data presented by public health jurisdictions. Public health jurisdictions may have additional data not reported to NREVSS and may use a different reporting cadence. The RSV trend graphs display the weekly average percent of tests positive for RSV among all the tests performed. Each point on the regional table displays the average number of RSV tests that were performed, and the average percent of those that were positive during a 3-week period (i.e., the specified week, and the weeks immediately preceding and following it). This is also known as a centered, 3-week moving average. The RSV detections displayed are the 5-week moving average (average of the 4 previous and current weeks) in accordance with the recommendations for assessing RSV trends by detections (https://academic.oup.com/jid/article/216/3/345/3860464). \n\nNREVSS strives to present precise estimates of respiratory viral trends and minimize reporting burden for participating laboratories. However, there are several limitations to this surveillance system. NREVSS is a laboratory-based surveillance system that does not have patient-specific data; multiple tests from a single patient may be included. In addition, NREVSS does not collect demographic or clinical data (i.e., hospitalizations or deaths). Testing practices may vary regionally, and the number of participating laboratories may change from year to year. Laboratories from all 50 states report data weekly, but reporting is voluntary and may not be representative of local RSV activity. The data do not include all test results within a jurisdiction and therefore do not reflect all RSV NAATs administered regionally or nationally. Participating laboratories vary in size, testing capabilities, and areas and populations served. Geographic results from clinical laboratories are based on testing location and laboratories may test samples from across one or more states.  For more information on NREVSS and RSV surveillance please visit: https://www.cdc.gov/surveillance/nrevss.",
+            "title": "Percent Positivity of Respiratory Syncytial Virus Nucleic Acid Amplification Tests by HHS Region, National Respiratory and Enteric Virus Surveillance System",
+            "programCode": [
+                "009:026"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3cxc-4k8q/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3cxc-4k8q/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3cxc-4k8q/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3cxc-4k8q/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "US",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "Weekly",
+            "theme": [
+                "Laboratory Surveillance"
+            ],
+            "language": [
+                "English"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/vaccines/data-reporting/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2025-01-29",
+            "@type": "dcat:Dataset",
+            "temporal": "2019-20, 2020-21, 2021-22, 2022-23, 2023-24 & 2024-25",
+            "modified": "2025-01-29",
+            "keyword": [
+                "flu vaccination",
+                "iis",
+                "iqvia",
+                "nis",
+                "vsd"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VaxView Team",
+                "hasEmail": "mailto:VaxView@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/agz7-4mvg",
+            "description": "\u2022 Weekly Cumulative Influenza Vaccination Coverage, by Flu Season and Race and Ethnicity, Medicare Fee-For-Service Beneficiaries, Adults aged 65 years and Older\n\n\u2022 Influenza vaccination coverage among Medicare fee-for-service beneficiaries 65 years and older is assessed using data files from the Medicare Fee-For-Service (FFS) administrative claims data managed by the Centers for Medicare & Medicaid Services (CMS).",
+            "title": "Weekly Cumulative Influenza Vaccination Coverage, by Flu Season and Race and Ethnicity, Medicare Fee-For-Service Beneficiaries aged \u226565 years, United States, Data Source: Centers for Medicare & Medicaid Services Chronic Conditions Warehouse",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/agz7-4mvg/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/agz7-4mvg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/agz7-4mvg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/agz7-4mvg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States- National",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Weekly",
+            "theme": [
+                "Flu Vaccinations"
+            ],
+            "language": [
+                "English"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-02-10",
+            "@type": "dcat:Dataset",
+            "temporal": "2019-12-29/2023-07-29",
+            "modified": "2023-09-27",
+            "keyword": [
+                "age",
+                "age group",
+                "all causes",
+                "children",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "hhs region",
+                "hispanic origin",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "puerto rico",
+                "race",
+                "united states",
+                "weekly"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/tpcp-uiv5",
+            "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nDeaths involving COVID-19 reported to NCHS by time-period, HHS region, race and Hispanic origin, and age group.\n\nUnited States death counts include the 50 states, plus the District of Columbia and New York City. The ten (10) United States Department of Health and Human Services (HHS) regions include the following jurisdictions. Region 1: Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, Vermont; Region 2: New Jersey, New York, New York City, Puerto Rico; Region 3: Delaware, District of Columbia, Maryland, Pennsylvania, Virginia, West Virginia; Region 4: Alabama, Florida, Georgia, Kentucky, Mississippi, North Carolina, South Carolina, Tennessee; Region 5: Illinois, Indiana, Michigan, Minnesota, Ohio, Wisconsin; Region 6: Arkansas, Louisiana, New Mexico, Oklahoma, Texas; Region 7: Iowa, Kansas, Missouri, Nebraska; Region 8: Colorado, Montana, North Dakota, South Dakota, Utah, Wyoming; Region 9: Arizona, California, Hawaii, Nevada; Region 10: Alaska, Idaho, Oregon, Washington.",
+            "title": "Provisional COVID-19 Deaths by HHS Region, Race, and Age",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tpcp-uiv5/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tpcp-uiv5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tpcp-uiv5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tpcp-uiv5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "irregular",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/drug-abuse-warning-network-dawn-2005",
+            "issued": "2016-05-23",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "alcohol",
+                "demographic characteristics",
+                "detoxification",
+                "drug overdose",
+                "drug use",
+                "emergency departments",
+                "energy drinks",
+                "nonprescription drugs",
+                "substance abuse",
+                "suicide"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Substance Abuse & Mental Health Services Administration"
+            },
+            "identifier": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2005-nid13596",
+            "description": "<p>The Drug Abuse Warning Network (DAWN) is a nationally representative public health surveillance system that has monitored drug related emergency department (ED) visits to hospitals since the early 1970s. First administered by the Drug Enforcement Administration (DEA) and the National Institute on Drug Abuse (NIDA), the responsibility for DAWN now rests with the Substance Abuse and Mental Health Services Administration's (SAMHSA) Center for Behavioral Health Statistics and Quality (CBHSQ). Over the years, the exact survey methodology has been adjusted to improve the quality, reliability, and generalizability of the information produced by DAWN. The current approach was first fully implemented in the 2004 data collection year.<br />\nDAWN relies on a longitudinal probability sample of hospitals located throughout the United States. To be eligible for selection into the DAWN sample, a hospital must be a non-Federal, short-stay, general surgical and medical hospital located in the United States, with at least one 24-hour ED. DAWN cases are identified by the systematic review of ED medical records in participating hospitals. The unit of analysis is any ED visit involving recent drug use. DAWN captures both ED visits that are directly caused by drugs and those in which drugs are a contributing factor but not the direct cause of the ED visit. The reason a patient used a drug is not part of the criteria for considering a visit to be drug related. Therefore, all types of drug-related events are included: drug misuse or abuse, accidental drug ingestion, drug-related suicide attempts, malicious drug poisonings, and adverse reactions. DAWN does not report medications that are unrelated to the visit.<br />\nThe DAWN public-use dataset provides information for all types of drugs, including illegal drugs, prescription drugs, over-the-counter medications, dietary supplements, anesthetic gases, substances that have psychoactive effects when inhaled, alcohol when used in combination with other drugs (all ages), and alcohol alone (only for patients aged 20 or younger). Public-use dataset variables describe and categorize up to 16 drugs contributing to the ED visit, including toxicology confirmation and route of administration. Administrative variables specify the type of case, case disposition, categorized episode time of day, and quarter of year.  Metropolitan area is included for represented metropolitan areas. Created variables include the number of unique drugs reported and case-level indicators for alcohol, non-alcohol illicit substances, any pharmaceutical, non-medical use of pharmaceuticals, and all misuse and abuse of drugs. Demographic items include age category, sex, and race/ethnicity. Complex sample design and weighting variables are included to calculate various estimates of drug-related ED visits for the Nation as a whole, as well as for specific metropolitan areas, from the ED visits classified as DAWN cases in the selected hospitals.This study has 1 Data Set.</p>",
+            "title": "Drug Abuse Warning Network (DAWN-2005)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2005-nid13596",
+                    "description": "Drug Abuse Warning Network (DAWN-2005) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2005-nid13596"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/6tk5-h85s",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-01-03",
+            "@type": "dcat:Dataset",
+            "modified": "2019-01-03",
+            "keyword": [
+                "2018",
+                "carbapenemase-producing carbapenem-resistant enterobacteriaceae",
+                "enterobacter spp.",
+                "escherichia coli",
+                "klebsiella spp.",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/6tk5-h85s",
+            "description": "NNDSS - Table II. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html \r\n\r\nFootnotes:\r\n\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.  \r\n\r\n\u2020 Data for carbapenemase-producing carbapenem-resistant Enterobacteriaceae (CP-CRE) will be displayed in this table after the CDC obtains Office of Management and Budget Paperwork Reduction Act approval to receive data for this condition.",
+            "title": "NNDSS - Table II. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6tk5-h85s/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6tk5-h85s/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6tk5-h85s/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6tk5-h85s/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/24ct-nyt8",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-15",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Research Branch (RB) National Personal Protective Technology Laboratory (NPPTL)",
+                "hasEmail": "mailto:ODAdmin@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/24ct-nyt8",
+            "description": "Filtering facepiece respirators (FFRs) are used extensively by healthcare personnel (HCP) during a pandemic. FFRs are primarily reserved for those personnel who have a greater risk and longer duration of exposure compared with other workers and the general public. Some FFR models contain an exhalation valve, which is a device that closes to allow inhaled breath to be pulled through the filter media and opens to allow exhaled breath to be expelled from the respirator through the exhalation valve as well as the filter media. These FFR models provide the wearer with a level of protection like that of an FFR without an exhalation valve, and they are thought to increase the wearer\u2019s comfort at high work rates and be suitable for longer periods of use. However, respiratory secretions expelled by wearers may exit along with air through the exhalation valve. A concern with FFRs with an exhalation valve is that individuals may spread disease if unfiltered, virus-laden aerosols pass through the valve.\n\nDuring the COVID-19 pandemic, guidance from the Centers for Disease Control and Prevention (CDC) did not recommend using an FFR with an exhalation valve for source control (i.e., to filter respiratory secretions to prevent disease transmission to others) and advised that if only this option isavailable and source control was needed, then the valve should be covered with a surgical mask, procedure mask, or a cloth face covering that does not interfere with the respirator fit. The CDC requested research to provide improved science-based recommendations on the use of exhalation valves.\n\nThis study had three aims: (1) to measure the filtration efficiency provided by FFRs with an exhalation valve under conditions of inward airflow (i.e., in the direction of inhalation) and outward airflow (i.e., in the direction of exhalation); (2) to evaluate how particle penetration in FFRs with an exhalation valve compares to particle penetration in surgical masks, procedure masks, cloth face coverings, and fabric from cotton t-shirts; and (3) to determine the filtration efficiency of three modifications to the exhalation valve in FFRs with the goal of mitigating the emission of unfiltered particles. To accomplish these three aims, thirteen FFR models were each tested in two positions: inward position, which is used by the NIOSH Respirator Approval Program when testing N-type respirators, and outward position, which was used experimentally to channel airflow in the direction of exhalation. For the inward position, three mitigation strategies were used:\n(1)covering the valve on the interior of the FFR with commonly available surgical tape,\n(2)covering the valve on the interior of the FFR with an electrocardiogram (ECG) pad; and\n(3)stretching a surgical mask over the exterior of the FFR.\n\nThe purpose of these three strategies was to measure the varying filtration efficiencies to determine their contribution toward source control. Both positions and all mitigation strategies were tested at three airflow rates: 25, 55, and 85 lpm (liters per minute). In addition to the FFR evaluations, researchers evaluated a selection of surgical masks, procedure masks, cloth face coverings, and fabric from cotton t-shirts using the outward position and flowrates described previously.",
+            "title": "NPPTL Filtering Facepiece Respirators with an Exhalation Valve: Measurements of Filtration Efficiency to Evaluate Their Potential for Source Control",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/24ct-nyt8/application/x-zip-compressed",
+                    "mediaType": "application/x-zip-compressed"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "National Institute for Occupational Safety and Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/rs7d-uj9p",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-04-21",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-08",
+            "references": [
+                "https://www.mathematica.org/"
+            ],
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "197a420c-9b82-5108-b9ba-c2bf27da20c6",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "Scorecard pillar v2.11.16 (cmsdev)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.16/20241107/pillar.csv",
+                    "description": "Scorecard pillar v2.11.16 (cmsdev)",
+                    "@type": "dcat:Distribution",
+                    "title": "Scorecard pillar v2.11.16 (cmsdev)"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.ncbi.nlm.nih.gov/popset",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-08-26",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "api",
+                "genetics",
+                "genomics"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Library of Medicine",
+                "hasEmail": "mailto:custserv@nlm.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/c8eu-unh6",
+            "description": "The PopSet database is a collection of related DNA sequences derived from population, phylogenetic, mutation and ecosystem studies that have been submitted to GenBank.",
+            "title": "PopSet",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/popset",
+                    "mediaType": "text/html",
+                    "title": "Search PopSet - Query Interface"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Molecular biology/Genetics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/ap9g-4wiq",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-04-26",
+            "@type": "dcat:Dataset",
+            "modified": "2019-05-30",
+            "keyword": [
+                "2019",
+                "congenital",
+                "nedss",
+                "netss",
+                "nndss",
+                "primary and secondary",
+                "streptococcal toxic shock syndrome",
+                "syphilis",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/ap9g-4wiq",
+            "description": "NNDSS - TABLE 1HH. Streptococcal toxic shock syndrome to Syphilis, Primary and Secondary - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1HH. Streptococcal toxic shock syndrome to Syphilis, Primary and Secondary",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ap9g-4wiq/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ap9g-4wiq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ap9g-4wiq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ap9g-4wiq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-pregnancy-and-health-survey-drug-use-among-women-delivering-live-births-nphs-1992",
+            "issued": "2016-05-23",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "alcohol",
+                "amphetamines",
+                "cocaine",
+                "demographic characteristics",
+                "drug testing",
+                "drug treatment",
+                "drug use",
+                "economic indicators",
+                "heroin",
+                "hospitals",
+                "live births",
+                "marijuana",
+                "methadone",
+                "pregnancy",
+                "prenatal care",
+                "reproductive history",
+                "sedatives",
+                "tobacco use",
+                "tranquilizers",
+                "urinalysis",
+                "women"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Substance Abuse & Mental Health Services Administration"
+            },
+            "identifier": "https://datafiles.samhsa.gov/study/national-pregnancy-and-health-survey-drug-use-among-women-delivering-live-births-nphs-1992",
+            "description": "<p>The primary objective of the National Pregnancy and Health<br />\nSurvey (NPHS) was to produce national annual estimates of the<br />\npercentages and numbers of mothers of live newborns in the United<br />\nStates who used selected licit and illicit drugs in the 12 months<br />\nprior to delivery. A further objective was to describe patterns of<br />\nprenatal substance use among demographic subgroups of<br />\nwomen. Information on demographic and socioeconomic characteristics,<br />\nobstetric history, and drug treatment of women who delivered infants<br />\nat sampled hospitals was obtained through an interviewer-administered<br />\nquestionnaire, while data on substance use before and during pregnancy<br />\nwere collected through a questionnaire completed by the respondent and<br />\nconcealed from the interviewer. Respondents were asked about use of<br />\nthe following substances: alcohol, amphetamines, analgesics, cocaine,<br />\ncrack cocaine, barbiturates, hallucinogens, hashish, heroin,<br />\nmarijuana, methadone, methamphetamine, sedatives, stimulants, tobacco,<br />\nand tranquilizers. Additionally, information was collected on the<br />\nrespondent's pregnancy, prenatal care, delivery, previous pregnancies,<br />\nand background. Additional data were obtained from the mothers' and<br />\ninfants' medical records. Urine specimens collected routinely by the<br />\nhospital on obstetric admissions were tested for selected<br />\ndrugs. Finally, in a subsample of six hospitals, hair specimens were<br />\nrequested from respondents to evaluate the potential of hair as a<br />\nsource of toxicological data in future studies.This study has 1 Data Set.</p>",
+            "title": "National Pregnancy and Health Survey: Drug Use Among Women Delivering Live Births (NPHS-1992)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-pregnancy-and-health-survey-drug-use-among-women-delivering-live-births-nphs-1992",
+                    "description": "National Pregnancy and Health Survey: Drug Use Among Women Delivering Live Births (NPHS-1992) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/national-pregnancy-and-health-survey-drug-use-among-women-delivering-live-births-nphs-1992"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/dataset/licensing-opportunities-nih-cdc-fda-technologies",
+            "bureauCode": [
+                "001:05"
+            ],
+            "issued": "2012-05-30",
+            "temporal": "2014-04-01T00:00:00-04:00/2014-04-01T00:00:00-04:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "biomedical research",
+                "cdc",
+                "fda",
+                "innovation",
+                "invention",
+                "licensing",
+                "materials",
+                "nih",
+                "occupational safety",
+                "other",
+                "patents",
+                "reasearch",
+                "technology"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Ajoy Prabhu",
+                "hasEmail": "mailto:aprabhu@od.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
+            "identifier": "caf1a232-013f-4bcf-9258-d7fc10adc73e",
+            "description": "<p>This dataset represents all technologies available for licensing from the National Institutes of Health (NIH), the Food and Drug Administration (FDA), and the Center for Disease Control and Prevention (CDC).</p>",
+            "title": "Licensing Opportunities for NIH, CDC & FDA Technologies",
+            "programCode": [
+                "009:046"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.ott.nih.gov/opportunities",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                },
+                {
+                    "format": "API",
+                    "description": "NIH OTT API - National Institutes of Health Office of Technology Transfer API \n",
+                    "accessURL": "http://www.ott.nih.gov/nih-ott-api",
+                    "@type": "dcat:Distribution",
+                    "title": "NIH OTT API"
+                }
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/ruxz-gvwu",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-03-28",
+            "@type": "dcat:Dataset",
+            "modified": "2024-01-05",
+            "keyword": [
+                "chip",
+                "dq atlas",
+                "medicaid",
+                "program enrollment",
+                "t-msis analytic files"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "50f83c5a-6fa9-4e91-b36c-3d3e225c905f",
+            "description": "This data set presents annual enrollment counts of Medicaid and CHIP beneficiaries by benefit package (full-scope, comprehensive, limited, or unknown). There are three metrics presented: (1) the number of beneficiaries ever enrolled with each benefit package over the year (duplicated count); (2) the number of beneficiaries enrolled with each benefit package as of an individual\u2019s last month of enrollment (unduplicated count); and (3) average monthly enrollment with each benefit package. \r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating these measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable or of high concern based on DQ Atlas thresholds for the topic Restricted Benefits Code. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Some cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.\r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+            "title": "Benefit Package for Medicaid and CHIP Beneficiaries by Year",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/BenefitPackage-anul.csv",
+                    "description": "This data set presents annual enrollment counts of Medicaid and CHIP beneficiaries by benefit package (full-scope, comprehensive, limited, or unknown). There are three metrics presented: (1) the number of beneficiaries ever enrolled with each benefit package over the year (duplicated count); (2) the number of beneficiaries enrolled with each benefit package as of an individual\u2019s last month of enrollment (unduplicated count); and (3) average monthly enrollment with each benefit package. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating these measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable or of high concern based on DQ Atlas thresholds for the topic Restricted Benefits Code. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Some cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "@type": "dcat:Distribution",
+                    "title": "Benefit Package for Medicaid and CHIP Beneficiaries by Year"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y",
+            "theme": [
+                "Enrollment"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/4ynm-6jgm",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2020-01-17",
+            "@type": "dcat:Dataset",
+            "modified": "2021-01-07",
+            "keyword": [
+                "2020",
+                "arboviral diseases",
+                "nedss",
+                "netss",
+                "nndss",
+                "st. louis virus disease",
+                "west nile virus disease",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/4ynm-6jgm",
+            "description": "NNDSS - Table 1C. Arboviral diseases, St. Louis encephalitis virus disease to West Nile   virus disease - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - Table 1C. Arboviral diseases, St. Louis encephalitis virus disease to West Nile virus disease",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4ynm-6jgm/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4ynm-6jgm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4ynm-6jgm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4ynm-6jgm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/healthywater/surveillance/wastewater-surveillance/wastewater-surveillance.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-04-07",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-22",
+            "keyword": [
+                "covid19",
+                "sars-cov-2",
+                "wastewater"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Wastewater Surveillance System",
+                "hasEmail": "mailto:nwss@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/2ew6-ywp6",
+            "description": "This dataset provides a complete time history of metrics calculated using SARS-CoV-2 concentrations in wastewater.",
+            "title": "NWSS Public SARS-CoV-2 Wastewater Metric Data",
+            "programCode": [
+                "009:028"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2ew6-ywp6/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2ew6-ywp6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2ew6-ywp6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2ew6-ywp6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "Daily",
+            "theme": [
+                "Public Health Surveillance"
+            ],
+            "language": [
+                "English"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/dwmy-m9r6",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2020-01-21",
+            "@type": "dcat:Dataset",
+            "modified": "2021-01-07",
+            "keyword": [
+                "2020",
+                "confirmed",
+                "leptospirosis",
+                "listeriosis",
+                "nedss",
+                "netss",
+                "nndss",
+                "probable",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/dwmy-m9r6",
+            "description": "NNDSS - TABLE 1U. Leptospirosis to Listeriosis, Probable - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Data from California published in week 29 for years 2019 and 2020 were incomplete when originally published on July 24, 2020. On August 4, 2020, incomplete case counts were replaced with a \"U\" indicating case counts are not available for specified time period. \n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Before 2019, listeriosis cases in neonates less than or equal to 60 days of age were counted as one case in a mother-infant pair. Beginning in 2019, maternal and neonatal listeriosis cases are being counted separately. Beginning in 2020, confirmed and probable cases are published separately. Prior years included confirmed cases only.",
+            "title": "NNDSS - TABLE 1U. Leptospirosis to Listeriosis, Probable",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dwmy-m9r6/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dwmy-m9r6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dwmy-m9r6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dwmy-m9r6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/dataset/bridged-race-population-estimates",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2012-11-05",
+            "temporal": "2002-01-01T00:00:00-05:00/2011-12-31T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "population statistics",
+                "race and ethnicity statistics"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "065b5b37-ad82-4921-87db-b676f20aab99",
+            "description": "<p>Population estimates from \"bridging\" the 31 race categories used in Census 2000, as specified in the 1997 Office of Management and Budget (OMB) race and ethnicity data collection standards, to the four race categories specified under the 1977 standards (Asian or Pacific Islander, Black or African American, American Indian or Alaska Native, White).</p>",
+            "title": "Bridged Race Population Estimates",
+            "programCode": [
+                "009:031"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://wonder.cdc.gov/wonder/help/bridged-race.html",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "describedBy": "http://wonder.cdc.gov/wonder/help/bridged-race.html",
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/rwqu-teks",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-10-11",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-24",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "py2025",
+                "transparency in coverage"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Center for Consumer Information and Insurance Oversight",
+                "hasEmail": "mailto:CMS_FEPS@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "identifier": "230fcdc8-3a0b-48d5-98d9-36744a87906e",
+            "description": "The Transparency in Coverage PUF (TC-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The PUF contains data on issuer and plan-level claims, appeals, and active URL data. The PY2025 PUF contains data from PY2023 for issuers participating in the Exchanges in PY2023.",
+            "title": "Transparency in Coverage PUF - PY2025",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2025/transparency_in_coverage_PUF.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2003-0",
+            "issued": "2016-05-23",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "addiction",
+                "alcohol",
+                "alcohol abuse",
+                "alcohol consumption",
+                "amphetamines",
+                "barbiturates",
+                "cocaine",
+                "controlled drugs",
+                "depression (psychology)",
+                "drinking behavior",
+                "drug abuse",
+                "drug dependence",
+                "drugs",
+                "drug treatment",
+                "drug use",
+                "hallucinogens",
+                "heroin",
+                "households",
+                "inhalants",
+                "marijuana",
+                "mental health",
+                "mental health services",
+                "methamphetamine",
+                "prescription drugs",
+                "sedatives",
+                "smoking",
+                "stimulants",
+                "substance abuse",
+                "substance abuse treatment",
+                "tranquilizers"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Substance Abuse & Mental Health Services Administration"
+            },
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2003-nid13569",
+            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series<br />\n(formerly titled National Household Survey on Drug Abuse) measures the<br />\nprevalence and correlates of drug use in the United States. The<br />\nsurveys are designed to provide quarterly, as well as annual,<br />\nestimates. Information is provided on the use of illicit drugs,<br />\nalcohol, and tobacco among members of United States households aged 12<br />\nand older. Questions included age at first use as well as lifetime,<br />\nannual, and past-month usage for the following drug classes:<br />\nmarijuana, cocaine (and crack), hallucinogens, heroin, inhalants,<br />\nalcohol, tobacco, and nonmedical use of prescription drugs, including<br />\npain relievers, tranquilizers, stimulants, and sedatives. The survey<br />\ncovered substance abuse treatment history and perceived need for<br />\ntreatment, and included questions from the Diagnostic and Statistical<br />\nManual (DSM) of Mental Disorders that allow diagnostic criteria to be<br />\napplied. The survey included questions concerning treatment for both<br />\nsubstance abuse and mental health related disorders. Respondents were<br />\nalso asked about personal and family income sources and amounts,<br />\nhealth care access and coverage, illegal activities and arrest record,<br />\nproblems resulting from the use of drugs, and needle-sharing.<br />\nQuestions introduced in previous administrations were retained in the<br />\n2003 survey, including questions asked only of respondents aged 12 to<br />\n17. These \"youth experiences\" items covered a variety of topics, such<br />\nas neighborhood environment, illegal activities, gang involvement,<br />\ndrug use by friends, social support, extracurricular activities,<br />\nexposure to substance abuse prevention and education programs, and<br />\nperceived adult attitudes toward drug use and activities such as<br />\nschool work. Several measures focused on prevention related themes in<br />\nthis section. Also retained were questions on mental health and access<br />\nto care, perceived risk of using drugs, perceived availability of<br />\ndrugs, driving and personal behavior, and cigar smoking. Questions on<br />\nthe tobacco brand used most often were introduced with the 1999 survey<br />\nand retained through the 2003 survey. Background information includes<br />\ngender, race, age, ethnicity, marital status, educational level, job<br />\nstatus, veteran status, and current household composition. A number of additional questions were added in 2003, including questions on prior marijuana and cigarette use, additional questions on drug treatment, adult mental health services, and social environment.This study has 1 Data Set.</p>",
+            "title": "National Survey on Drug Use and Health (NSDUH-2003)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2003-nid13569",
+                    "description": "National Survey on Drug Use and Health (NSDUH-2003) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2003-nid13569"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/mmi4-8ajr",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2013-06-19",
+            "@type": "dcat:Dataset",
+            "modified": "2015-08-27",
+            "keyword": [
+                "flu shot",
+                "immunization",
+                "prams",
+                "pregnant women"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/mmi4-8ajr",
+            "description": "For more information about the Pregnancy Risk Assessment Monitoring System please visit http://www.cdc.gov/prams/. See http://www.cdc.gov/mmwr/preview/mmwrhtml/mm6107a1.htm?s_cid=mm6107a1_e for the MMWR article.",
+            "title": "State Specific Influenza Vaccination Coverage Among Women With Live Birth- PRAMS, 2009-10 Influenza Season",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mmi4-8ajr/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mmi4-8ajr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mmi4-8ajr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mmi4-8ajr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Pregnancy & Vaccination"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/ryqa-f6tz",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2020-11-06",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-07",
+            "keyword": [
+                "drug acquisition cost",
+                "nadac"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Chris Vaughn",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "e3af839d-8175-5be0-b94e-4a302ed7a035",
+            "description": "The tables below display new National Average Drug Acquisition Cost (NADAC) rates, sorted by Drug Product and Date. The drug products listed have not had a NADAC rate in the past.",
+            "title": "First Time NADAC Rates",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/first-time-nadac-rates-01072025.csv",
+                    "mediaType": "text/csv",
+                    "title": "CSV"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P10Y",
+            "theme": [
+                "Drug Pricing and Payment"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/nfn2-3v66",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2023-12-14",
+            "@type": "dcat:Dataset",
+            "modified": "2024-12-16",
+            "keyword": [
+                "api",
+                "mesh",
+                "mesh 2023 update",
+                "terminologies"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Library of Medicine",
+                "hasEmail": "mailto:custserv@nlm.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/nfn2-3v66",
+            "description": "<b>(Includes MeSH 2023 and 2024 changes)</b>  The MeSH 2025 Update - Combine Report lists new Entry Combinations.  These are cases where a new, precoordinated Descriptor has been created to replace an existing Descriptor / Qualifier combination.  <b>This report includes MeSH changes from previous years, starting from 2023.</b>",
+            "title": "MeSH 2025 Update - Combine Report",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/nfn2-3v66/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/nfn2-3v66/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/nfn2-3v66/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/nfn2-3v66/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Terminology"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/hp6w-4ap6",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2015-06-08",
+            "@type": "dcat:Dataset",
+            "modified": "2015-08-27",
+            "keyword": [
+                "youth risk behavior risk surveillance school-based surveillance"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/hp6w-4ap6",
+            "description": "The Youth Risk Behavior Surveillance System (YRBSS) monitors six types of health-risk behaviors that contribute to the leading causes of death and disability among youth and adults. This file contains state-level results for 13 tobacco-use variables by sex and grade for 2013.",
+            "title": "YRBS State Tobacco Variables  2013 - v2",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hp6w-4ap6/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hp6w-4ap6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hp6w-4ap6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hp6w-4ap6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/rzmt-rapu",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2025-01-18",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-17",
+            "keyword": [
+                "medicaid"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "13a06cdb-6bbb-4f86-bba7-9d6f3db41090",
+            "description": "Medicaid Enterprise System Datatable",
+            "title": "Medicaid Enterprise System Datatable",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/data-analysis-table-for-medcaid-01172025.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/btcp-84tv",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-01-03",
+            "@type": "dcat:Dataset",
+            "modified": "2019-01-03",
+            "keyword": [
+                "2018",
+                "acute",
+                "by type) a & b",
+                "hepatitis (viral",
+                "nedss",
+                "netss",
+                "nndss",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/btcp-84tv",
+            "description": "NNDSS - Table II. Hepatitis (viral, acute, by type) A & B - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html.\r\n \r\nFootnotes:\r\n\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.  \r\n\r\n\u2020 Perinatal hepatitis C cases are not included in this table. These data will be included in the annual NNDSS tables on the NNDSS Data and Statistics page (https://wwwn.cdc.gov/nndss/data-and-statistics.html) beginning with data year 2018 and in the annual Summary of Viral Hepatitis, published online by CDC's Division of Viral Hepatitis, available at https://www.cdc.gov/hepatitis/statistics/2015surveillance/index.htm.",
+            "title": "NNDSS - Table II. Hepatitis (viral, acute, by type) A & B",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/btcp-84tv/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/btcp-84tv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/btcp-84tv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/btcp-84tv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/vaccines/data-reporting/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-20",
+            "@type": "dcat:Dataset",
+            "temporal": "2024-2025",
+            "modified": "2025-01-29",
+            "keyword": [
+                "iis",
+                "iqvia",
+                "nis-acm",
+                "rsv vaccination",
+                "vsd"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VaxView Team",
+                "hasEmail": "mailto:VaxView@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/n2zz-25mk",
+            "description": "\u2022 Monthly Cumulative Percent of Adults 75 Years and Older Who Received 1+ RSV Vaccination Doses by Jurisdiction, United States. \n\u2022 Respiratory Syncytial Virus (RSV) vaccination coverage for adults is assessed through U.S. jurisdictions\u2019 Immunization Information Systems Resources (IIS) data, submitted from jurisdictions to CDC monthly in aggregate by age group (https://www.cdc.gov/iis/about/).",
+            "title": "Monthly Cumulative Number and Percent of Adults 75 Years and Older Who Received 1+ RSV Vaccination Doses by Jurisdiction, United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/n2zz-25mk/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/n2zz-25mk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/n2zz-25mk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/n2zz-25mk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States- National",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Monthly",
+            "theme": [
+                "Vaccinations"
+            ],
+            "language": [
+                "English"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-dashboard.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-12-10",
+            "@type": "dcat:Dataset",
+            "temporal": "2019-2020, 2020-2021, 2021-2022, 2022-2023",
+            "modified": "2024-05-24",
+            "references": [
+                "Centers for Medicare & Medicaid Services Chronic Conditions Warehouse"
+            ],
+            "keyword": [
+                "flu",
+                "flu vaccination",
+                "influenza"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Vax Views",
+                "hasEmail": "mailto:VaxView@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/g57i-yx3r",
+            "description": "Weekly Cumulative Influenza Vaccination Coverage, by Flu Season and Race/Ethnicity, Medicare Fee-For-Service Beneficiaries aged \u226565 years, United States \n\n\u2022\tInfluenza vaccination coverage among Medicare fee-for-service beneficiaries aged \u226565 years is assessed using data files from the Medicare Fee-For-Service (FFS) administrative claims data managed by the Centers for Medicare & Medicaid Services (CMS). \n\n\u2022\tWeekly influenza vaccination coverage estimates were calculated using Kaplan-Meier survival analysis, based on beneficiaries enrolled as of August 1, 2019 and followed through May 31, 2020 for 2019-20 flu season; and enrolled as of August 1, 2020 and followed through May 31, 2021 for 2020-21 flu season; and enrolled as of Aug 1, 2021 and followed through May 28, 2022 for the 2021-22 flu season. \n\n\u2022\tAdditional information about data source is available https://www2.ccwdata.org/web/guest/home/.",
+            "title": "Weekly Cumulative Influenza Vaccination Coverage, by Flu Season and Race/Ethnicity, Medicare Fee-For-Service Beneficiaries aged \u226565 years, United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/g57i-yx3r/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/g57i-yx3r/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/g57i-yx3r/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/g57i-yx3r/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Weekly",
+            "theme": [
+                "Vaccinations"
+            ],
+            "language": [
+                "English"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-premium-reports/cms-program-statistics-medicare-premiums",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2013-01-01/2021-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2023-03-06",
+            "references": [
+                "https://data.cms.gov/resources/medicare-service-type-reports-methodology"
+            ],
+            "keyword": [
+                "beneficiary costs",
+                "health care use & payments",
+                "health equity",
+                "medicare",
+                "national",
+                "original medicare",
+                "states & territories"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CMS Program Statistics - OEDA",
+                "hasEmail": "mailto:IPAG_Data_Products@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/22c117c2-c04f-4078-9b7d-782167c8f0bb/data-viewer",
+            "description": "The CMS Program Statistics -\u00a0Medicare Premium tables provide information on counts of Medicare Part A (Hospital Insurance)\u00a0and Part B (Medical Insurance) total premium, standard base premium, reduced base premium, and penalty beneficiaries. In addition, these tables include premium amounts and penalty amounts. For the Part B premium tables, information on Income Related Monthly Adjustment Amount (IRMAA) beneficiaries, IRMAA amounts, Managed Care Reduction beneficiaries and Managed Care Reduction amounts are also included.\u00a0\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\u00a0\n\nBelow is the list of tables:\n\nMDCR PREMIUMS 1. Medicare Premiums: \u00a0Medicare Part A Premium Beneficiaries and Amounts, Yearly Trend\n\tMDCR PREMIUMS 2. Medicare Premiums: \u00a0Medicare Part A Premium Beneficiaries and Amounts by Demographic Characteristics and Medicare-Medicaid Enrollment Status\n\tMDCR PREMIUMS 3. Medicare Premiums: \u00a0Medicare Part A Premium Beneficiaries and Amounts, by Area of Residence\n\tMDCR PREMIUMS 4. Medicare Premiums: \u00a0Medicare Part B Premium Beneficiaries and Amounts, Yearly Trend\n\tMDCR PREMIUMS 5. Medicare Premiums: \u00a0Medicare Part B Premium Beneficiaries and Amounts by Demographic Characteristics and Medicare-Medicaid Enrollment Status\n\tMDCR PREMIUMS 6. Medicare Premiums: \u00a0Medicare Part B Premium Beneficiaries and Amounts, by Area of Residence",
+            "title": "CMS Program Statistics - Medicare Premiums",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-02/CPS%20MDCR%20PREMIUMS%202021.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Premiums : 2021-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-02/CPS%20MDCR%20PREMIUMS%202020.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Premiums : 2020-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-01/CPS_MDCR_PREMIUMS_1-6.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Premiums : 2019-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-11/CPS%20MDCR%20TOTAL%20PREMIUMS%202018.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Premiums : 2018-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2019-12/CPS_MDCR_PREMIUMS_2017.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Premiums : 2017-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-01/CPS%20MDCR%20PREMIUMS%20ALL.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Premiums : 2016-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-01/CPS%20MDCR%20PREMIUMS%20ALL_0.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Premiums : 2015-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-01/CPS%20MDCR%20PREMIUMS%20ALL_1.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Premiums : 2014-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-01/CPS%20MDCR%20PREMIUMS%20ALL_2.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Premiums : 2013-12-31"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/medicare-and-medicaid-summary-statistics-glossary",
+            "dataQuality": true,
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "Medicare"
+            ],
+            "language": [
+                "en-US"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/dataset/national-violent-death-reporting-system-nvdrs",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2014-04-08",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "community health",
+                "health care providers",
+                "injury deaths",
+                "nonfatal injuries",
+                "population statistics",
+                "safety",
+                "sexual assault",
+                "violent deaths",
+                "ypll"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "nvrds@cdc.gov",
+                "hasEmail": "mailto:nvrds@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention, Department of Health & Human Services"
+            },
+            "identifier": "a4b95d02-096c-47a6-9334-9e0088322ece",
+            "description": "<p>The National Violent Death Reporting System (NVDRS) provides states and communities with a clearer understanding of violent deaths to guide local decisions about efforts to prevent violence and helps them track progress over time.</p>\n<p>To stop violent deaths, we must first understand all the facts. Created in 2002, the NVDRS is a surveillance system that pulls together data on violent deaths in 18 states (see map below), including information about homicides, such as homicides perpetrated by a intimate partner (e.g., boyfriend, girlfriend, wife, husband), child maltreatment (or child abuse) fatalities, suicides, deaths where individuals are killed by law enforcement in the line of duty, unintentional firearm injury deaths, and deaths of undetermined intent.</p>\n<p>These data are supported by WISQARS, an interactive query system that provides data on injury deaths, violent deaths, and nonfatal injuries.</p>",
+            "title": "National Violent Death Reporting System (NVDRS)",
+            "programCode": [
+                "009:100"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.cdc.gov/injury/wisqars/",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "Community",
+                "Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/program-integrity-market-saturation-by-type-of-service/market-saturation-utilization-core-based-statistical-areas",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2023-01-01/2023-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-31",
+            "references": [
+                "https://data.cms.gov/resources/market-saturation-utilization-core-based-statistical-areas-methodology"
+            ],
+            "keyword": [
+                "fraud waste & abuse prevention",
+                "health care use & payments",
+                "medicare",
+                "original medicare",
+                "rural-urban",
+                "states & territories"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Market Saturation - CPI",
+                "hasEmail": "mailto:MarketSaturation@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/9b0e7798-d945-48fc-9861-d38bb5083a74/data-viewer",
+            "description": "The Market Saturation and Utilization Core-Based Statistical Areas (CBSA) dataset provides monitoring of market saturation as a means to help prevent potential fraud, waste, and abuse (FWA). CBSAs are geographical delineations that are Census Bureau-defined urban clusters of at least 10,000 people. Market saturation, in the present context, refers to the density of providers of a particular service within a defined geographic area relative to the number of beneficiaries receiving that service in the area. The data can be used to reveal the degree to which use of a service is related to the number of providers servicing a geographic region. There are also a number of secondary research uses for these data, but one objective of making these data public is to assist health care providers in making informed decisions about their service locations and the beneficiary population they serve.\n\nThe interactive dataset can be filtered and analyzed on the site or downloaded in Excel format.",
+            "title": "Market Saturation & Utilization Core-Based Statistical Areas",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9b0e7798-d945-48fc-9861-d38bb5083a74/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Market Saturation & Utilization Core-Based Statistical Areas : 2023-12-04"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/c7a402bc-2391-41cf-89f6-1e04f739ce86/Market_Saturation_and_Utilization_CBSA_Dataset_Release_19_20241025.csv",
+                    "mediaType": "text/csv",
+                    "title": "Market Saturation & Utilization Core-Based Statistical Areas : 2023-12-04"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ec13a93f-3d70-409f-8bc1-9e5df5bb95bc/data",
+                    "mediaType": "text/html",
+                    "title": "Market Saturation & Utilization Core-Based Statistical Areas : 2023-12-04"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/market-saturation-utilization-core-based-statistical-area-data-dictionary",
+            "dataQuality": true,
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "Medicare"
+            ],
+            "language": [
+                "en-US"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2014",
+            "issued": "2016-05-23",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "alcohol abuse",
+                "drug abuse",
+                "drug treatment",
+                "health care services",
+                "hiv",
+                "intervention",
+                "substance abuse",
+                "substance abuse treatment",
+                "treatment facilities",
+                "treatment programs"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Substance Abuse & Mental Health Services Administration"
+            },
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2014-nid13605",
+            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, to update SAMHSA's Inventory of Behavioral Health Services (I-BHS), to analyze general treatment services trends, and to generate the online Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>, as well as the National Directory of Drug and Alcohol Abuse Treatment Programs.Data are collected on topics including facility operation, services offered (assessment, testing, transitional, ancillary, and pharmacotherapies), detoxification, primary focus (substance abuse, mental health, both, general health, and other), Opioid Treatment Programs and medications dispensed/prescribed, counseling and therapeutic approaches, standard operating procedures, special programs/groups offered, languages in which treatment is provided, type of treatment provided (hospital inpatient, residential, outpatient), number of clients (by service, total, and under age 18), number of beds, types of payment accepted, sliding fee scale, and facility accreditation and licensure/certification.This study has 1 Data Set.</p>",
+            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2014)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2014-nid13605",
+                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2014) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2014-nid13605"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/s3ks-nh9r",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2024-11-02",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-24",
+            "references": [
+                "https://www.mathematica.org/"
+            ],
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "67ed2b07-ecd9-5506-84a7-b5613ae185c9",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "CoreSEt measure_value v2.10.6 (coreset-etl-test)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.6/20241023/measure_value.csv",
+                    "description": "CoreSEt measure_value v2.10.6 (coreset-etl-test)",
+                    "@type": "dcat:Distribution",
+                    "title": "CoreSEt measure_value v2.10.6 (coreset-etl-test)"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/s3n2-fbxq",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-03-28",
+            "@type": "dcat:Dataset",
+            "modified": "2024-01-05",
+            "keyword": [
+                "behavioral health care",
+                "chip",
+                "integrated care",
+                "medicaid",
+                "mental health condition",
+                "physical health condition"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "7db0e932-5275-4c3c-b4b6-8dc5f1520c3b",
+            "description": "This table presents beneficiaries who received a service for a physical health condition among beneficiaries who received a service for a mental health condition, by physical health condition, 2017-2021.\r\n\r\nSome states have serious data quality issues, making the data unusable for identifying this population. To assess data quality, analysts used measures featured in the DQ Atlas. Data for a state are considered unusable based on DQ Atlas thresholds for the following topics: Total Medicaid and CHIP Enrollment, Claims Volume - IP, Claims Volume - OT, Claims Volume - IP, Diagnosis Code - IP, Diagnosis Code - OT, Procedure Codes - OT Professional, Gender, Age, Zip code, Race and ethnicity, Eligibility group code, Enrollment in CMC Plans. \r\n\r\nData from Maryland, Tennessee, and Utah are omitted for the tables due to data quality concerns. Maryland was excluded in 2017 due to unusable diagnosis codes in the IP file and the OT file. Tennessee was excluded due to unusable diagnosis codes in the IP file in 2017 - 2019. Utah was excluded due to unusable procedure codes on OT professional claims in 2017 - 2020. In addition, states with a high data quality concern on one or more measures are noted in the table in the \"Data Quality\" column. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+            "title": "Beneficiaries receiving a physical hlth serv among beneficiaries receiving a mental hlth serv, by physical hlth cond, 2017-2021",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/benf-rcving-phy-hlth-amg-ben-rcvin-mntl-hlth-serv-2017-2021.csv",
+                    "mediaType": "text/csv",
+                    "title": "Beneficiaries receiving a physical hlth serv among beneficiaries receiving a mental hlth serv, by physical hlth cond, 2017-2021"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P10Y",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/rh2h-3yt2",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-12-01",
+            "@type": "dcat:Dataset",
+            "temporal": "2020-12-13/2023-05-12",
+            "modified": "2023-05-12",
+            "references": [
+                "https://www.cdc.gov/coronavirus/2019-ncov/vaccines/distributing/about-vaccine-data.html"
+            ],
+            "keyword": [
+                "administration",
+                "coronavirus",
+                "covid-19",
+                "immunization",
+                "izdl",
+                "report date",
+                "vaccination"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NCIRD",
+                "hasEmail": "mailto:iisinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/rh2h-3yt2",
+            "description": "Overall\u00a0Trends in Number of COVID-19 Vaccinations in the US at\u00a0national\u00a0and jurisdictional levels. Data represents all vaccine partners including jurisdictional partner clinics, retail pharmacies, long-term care facilities, dialysis centers, Federal Emergency Management Agency and Health Resources and Services Administration partner sites, and federal entity facilities.\u00a0",
+            "title": "COVID-19 Vaccination Trends in the United States,National and Jurisdictional",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rh2h-3yt2/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rh2h-3yt2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rh2h-3yt2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rh2h-3yt2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "US",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1D",
+            "theme": [
+                "Vaccinations"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/adultvaxview/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-07-28",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-22",
+            "keyword": [
+                "immunization",
+                "pneumococcal",
+                "shingles",
+                "td",
+                "tdap",
+                "vaccination",
+                "vaccination coverage",
+                "vaxviews",
+                "zoster"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VaxView Team",
+                "hasEmail": "mailto:VaxView@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/aetd-68ew",
+            "description": "Vaccination Coverage among Adults (18+ Years)\n\n\u2022 Data on adult vaccination coverage from the Behavioral Risk Factor Surveillance System (BRFSS) for the general population at the national, regional, and state levels by age groups.\n\n\u2022 Additional information available at https://www.cdc.gov/vaccines/imz-managers/coverage/adultvaxview/index.html",
+            "title": "Vaccination Coverage among Adults (18+ Years)",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/aetd-68ew/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/aetd-68ew/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/aetd-68ew/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/aetd-68ew/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Vaccinations"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-spending-by-drug/medicare-part-b-discarded-drug-units",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2022-01-21",
+            "temporal": "2022-01-01/2022-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2024-03-14",
+            "references": [
+                "https://data.cms.gov/resources/medicare-part-b-discarded-drug-units-methodology"
+            ],
+            "keyword": [
+                "drugs",
+                "medicare",
+                "original medicare"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CMS Drug Spending - OEDA",
+                "hasEmail": "mailto:IPAG_Data_Products@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/09fd71b8-eb3e-45af-a01e-f8ab5a190e84/data-viewer",
+            "description": "The Medicare Part B Discarded Drug Units dataset provides spending information on claims for Medicare Part B drugs that were identified as having discarded amounts of a drug. As of January 1, 2017, the Centers for Medicare & Medicaid Services (CMS) requires all physicians, hospitals, and other providers submitting claims for Medicare Part B drugs to report any discarded amount of a single use vial or other single use package drug on its claim for payment. With the passage of the Infrastructure Investment and Jobs Act in November 2021, manufacturers must pay a refund to Medicare for discarded amounts above a specified threshold effective for drugs furnished beginning with January 1, 2023.",
+            "title": "Medicare Part B Discarded Drug Units",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/09fd71b8-eb3e-45af-a01e-f8ab5a190e84/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Medicare Part B Discarded Drug Units : 2022-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/0feea016-6773-45b5-9e8a-b25b61cf5b74/DW_RY24_P04_V10_DY22_HCPCS-%20240205.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Part B Discarded Drug Units : 2022-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d9278560-5136-4359-b869-a07dd0c34b87/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Part B Discarded Drug Units : 2022-01-01"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/medicare-part-b-discarded-drug-units-data-dictionary",
+            "dataQuality": true,
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "Medicare"
+            ],
+            "language": [
+                "en-US"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/247v-f7n9",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2020-01-21",
+            "@type": "dcat:Dataset",
+            "modified": "2021-01-07",
+            "keyword": [
+                "2020",
+                "nedss",
+                "netss",
+                "nndss",
+                "paralytic",
+                "pertussis",
+                "plague",
+                "poliomyelitis",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/247v-f7n9",
+            "description": "NNDSS - TABLE 1Z. Pertussis to Poliomyelitis, paralytic - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Data from California published in week 29 for years 2019 and 2020 were incomplete when originally published on July 24, 2020. On August 4, 2020, incomplete case counts were replaced with a \"U\" indicating case counts are not available for specified time period. \n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 The pertussis case definition was modified by CSTE effective January 1, 2020. Criteria were modified increasing sensitivity for case ascertainment such that case counts may increase.",
+            "title": "NNDSS - TABLE 1Z. Pertussis to Poliomyelitis, paralytic",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/247v-f7n9/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/247v-f7n9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/247v-f7n9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/247v-f7n9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/s4kg-z8sq",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-06-01",
+            "@type": "dcat:Dataset",
+            "modified": "2023-05-31",
+            "references": [
+                "https://www.mathematica.org/"
+            ],
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "4000fb2c-f5ac-5599-81ed-9443b7135416",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "Scorecard TAG v0.3.0-1 (etl_test)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/0.3.0-1/TAG.csv",
+                    "description": "Scorecard TAG v0.3.0-1 (etl_test)",
+                    "@type": "dcat:Distribution",
+                    "title": "Scorecard TAG v0.3.0-1 (etl_test)"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/s4w6-ihsn",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2022-03-25",
+            "@type": "dcat:Dataset",
+            "modified": "2022-03-21",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "c6f03fab-fe07-4ba3-bc33-212ae0e7cdc8",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2022-03-14 to 2022-03-20",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://edit.data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rpt-drugs-mar-03-14-2022-03-20-2022.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm135778.htm",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "cder",
+                "establishments",
+                "registration"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "openFDA",
+                "hasEmail": "mailto:open@fda.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "identifier": "fa27e8ba-4b3c-4a2d-bb29-19eecffa0847",
+            "description": "The Drug Establishments Current Registration Site (DECRS) is a database of current information submitted by drug firms to register establishments (facilities) which manufacture, prepare, propagate, compound or process drugs that are commercially distributed in the U.S. or offered for import to the U.S.",
+            "title": "Drug Establishments Current Registration Site",
+            "programCode": [
+                "009:002"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fda.gov/downloads/Drugs/InformationOnDrugs/UCM197817.zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P3M"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://rdocdb.nimh.nih.gov/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2016-07-17",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Farber, Greg",
+                "hasEmail": "mailto:farberg@mail.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
+            "identifier": "951435a3-1699-43cc-a00b-f138c892058b",
+            "description": "<p>RDoCdb supports the Research Domain Criteria Initiative (RDoC), which calls for the development, for research purposes, of new ways of classifying psychopathology based on dimensions of observable behavior and neurobiological measures by providing the research community a data repository for the sharing of research data related to this initiative.</p>",
+            "title": "RDoCdb",
+            "programCode": [
+                "009:060"
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/4qb4-rsd8",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2017-01-05",
+            "@type": "dcat:Dataset",
+            "modified": "2017-01-05",
+            "keyword": [
+                "2016",
+                "congenital syndrome",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "rubella",
+                "salmonellosis",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/4qb4-rsd8",
+            "description": "NNDSS - Table II. Rubella to Salmonellosis - 2016.  In this Table, provisional* cases of selected\u2020 notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.   NP:  Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. \r\n\r\n * Case counts for reporting year 2016 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly.\r\n\u2020 Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions.",
+            "title": "NNDSS - Table II. Rubella to Salmonellosis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4qb4-rsd8/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4qb4-rsd8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4qb4-rsd8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4qb4-rsd8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.healthit.gov/data/datasets/ehr-products-used-meaningful-use-attestation",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-10-03",
+            "@type": "dcat:Dataset",
+            "modified": "2019-01-01",
+            "references": [
+                "https://www.healthit.gov/data/quickstats/health-care-professional-health-it-developers",
+                "https://www.healthit.gov/data/quickstats/hospital-health-it-developers",
+                "https://www.healthit.gov/data/apps/ehr-vendors-reported-hospitals-demonstrating-meaningful-use",
+                "https://www.healthit.gov/data/apps/ehr-vendors-reported-office-based-providers-demonstrating-meaningful-use"
+            ],
+            "keyword": [
+                "certified",
+                "ehrs",
+                "electronic health records",
+                "health information technology",
+                "health it",
+                "interoperability"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "ONC Request",
+                "hasEmail": "mailto:onc.request@hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the National Coordinator for Health Information Technology"
+            },
+            "identifier": "11c83d84-83c1-4310-963f-2134f953943b",
+            "description": "The Medicare Electronic Health Record (EHR) Incentive Program provides incentives to eligible clinicians and hospitals to adopt electronic health records. This dataset combines meaningful use attestations from the Medicare EHR Incentive Program and certified health IT product data from the ONC Certified Health IT Product List (CHPL) to identify the unique vendors, products, and product types of each certified health IT product used to attest to meaningful use. The dataset also includes important provider-specific data, related to the provider&apos;s participation and status in the program, unique provider identifiers, and other characteristics unique to each provider, like geography and provider type.",
+            "title": "EHR Products Used for Meaningful Use Attestation",
+            "programCode": [
+                "009:110"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/MU_REPORT.csv",
+                    "mediaType": "text/csv",
+                    "title": "MU_REPORT.csv"
+                }
+            ],
+            "describedBy": "https://www.healthit.gov/data/datasets/ehr-products-used-meaningful-use-attestation"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/8bda-nhxv",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-06-23",
+            "@type": "dcat:Dataset",
+            "modified": "2024-09-03",
+            "keyword": [
+                "abcs",
+                "bactfacts"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Active Bacterial Core Surveillance",
+                "hasEmail": "mailto:abcs@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/8bda-nhxv",
+            "description": "<p>ABCs is an ongoing surveillance program that began in 1997. <a href=\"https://www.cdc.gov/abcs/reports-findings/surv-reports.html\">ABCs reports</a> describe the ABCs case definition and the specific methodology used to calculate rates and estimated numbers in the United States for each bacterium by year.  The methods, <a href=\"https://www.cdc.gov/abcs/methodology/surv-pop.html\">surveillance areas</a>, and <a href=\"https://www.cdc.gov/abcs/methodology/surv-pop.html\">laboratory isolate collection areas</a> have changed over time.\n                Additionally, the way missing data are taken into account changed in 2010.  It went from distributing unknown values based on known values of cases by site to use of multiple imputation using a sequential regression imputation method.\n                Given these changes over time, trends should be interpreted with caution.\n<ul> <li> <a href=\"http://www.cdc.gov/abcs/methodology/index.html\">Methodology</a>\nFind details about surveillance population, case determination, surveillance evaluation, and more. </li>                    <li> <a href=\"http://www.cdc.gov/abcs/reports-findings/index.html\">Reports and Findings</a>\nGet official interpretations from reports and publications created from ABCs data. </li>\n  </ul>",
+            "title": "Active Bacterial Core surveillance (ABCs) Neisseria meningitidis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8bda-nhxv/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8bda-nhxv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8bda-nhxv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8bda-nhxv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Public Health Surveillance"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2008",
+            "issued": "2016-05-23",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "alcohol abuse",
+                "drug abuse",
+                "drug treatment",
+                "health care services",
+                "health insurance",
+                "intervention",
+                "mental health",
+                "substance abuse",
+                "substance abuse treatment",
+                "treatment programs"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Substance Abuse & Mental Health Services Administration"
+            },
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2008-nid13576",
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2008)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2008-nid13576",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2008) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2008-nid13576"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/s99n-4m79",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-05-31",
+            "@type": "dcat:Dataset",
+            "modified": "2023-05-30",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "46732f54-2971-48e2-b2ae-02d902ca6d33",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-05-22-to-2023-05-28",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rprt-drug-5-22-2023-to-5-28-2023_0.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-05-22-to-2023-05-28"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/9w38-t35p",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2016-09-14",
+            "@type": "dcat:Dataset",
+            "modified": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/9w38-t35p",
+            "description": "Source: Behavioral Risk Factor Surveillance System (BRFSS), 2012, 2014.",
+            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days), 2012 & 2014, Region 6 - Dallas",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9w38-t35p/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9w38-t35p/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9w38-t35p/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9w38-t35p/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Motor Vehicle"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/h98p-htn6",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-14",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Health Effects Laboratory, Research Pathology and Physiology Research Branch",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/h98p-htn6",
+            "description": "As more women join the skilled-trade workforce, the effects of workplace exposures on pregnancy need to be explored. This study aimed to identify the effects of mild-steel (MS) and stainless-steel (SS) welding fume exposures on first-trimester placental trophoblast cells, using the HTR-8/SVneo cell line. MS is primarily composed of Iron (Fe) and Manganese (Mn), while SS also contains chromium (Cr) and nickel (Ni). We found that all three welding fumes had significant effects on cellular viability, and also caused increases in free radical production, while negatively affecting their invasive capabilities. MS was the only sample to cause an increase in production of the pro-inflammatory cytokines IL-6 and IL-8. Our results show that welding fume exposure is in fact cytotoxic to trophoblasts, and understanding how these occupational exposures could impact maternal and fetal health is necessary. Identifying how the varying combinations of heavy metals and other materials present in MS and SS welding fumes, along",
+            "title": "Effects of Welding Fume Exposure on Human Placental Cells",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/h98p-htn6/application/x-zip-compressed",
+                    "mediaType": "application/x-zip-compressed"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "National Institute for Occupational Safety and Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/s9cg-pwbt",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2024-11-02",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-24",
+            "references": [
+                "https://www.mathematica.org/"
+            ],
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "3470acd5-0658-5971-bed7-80019b8a8ee2",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "CoreSEt state v2.10.6 (coreset-etl-test)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.6/20241023/state.csv",
+                    "description": "CoreSEt state v2.10.6 (coreset-etl-test)",
+                    "@type": "dcat:Distribution",
+                    "title": "CoreSEt state v2.10.6 (coreset-etl-test)"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.cdc.gov/tobacco/stateandcommunity/best_practices/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-07-14",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-25",
+            "keyword": [
+                "administration and management",
+                "best practices",
+                "best practices for comprehensive tobacco control programs",
+                "centers for disease control and prevention",
+                "cessation intervention",
+                "health communication interventions",
+                "office on smoking and health",
+                "osh",
+                "state and community interventions",
+                "surveillance and evaluation",
+                "tobacco"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "OSHData Support",
+                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/vm4m-idi8",
+            "description": "2014. Centers for Disease Control and Prevention (CDC). Best Practices for Comprehensive Tobacco Control Programs. Funding. CDC's Best Practices for Comprehensive Tobacco Control Programs is an evidence-based guide to help states plan and establish effective tobacco control programs to prevent and reduce tobacco use.  These data update Best Practices for Comprehensive Tobacco Control Programs\u20142007.  Data are reported at total and per capita funding levels. Data include recommended and minimum total funding levels for state programs, in addition to funding breakdowns by intervention areas such as: State and Community Interventions, Mass-Reach Health Communication Interventions, Cessation Interventions, Surveillance and Evaluation, and Infrastructure, Administration, and Management.",
+            "title": "CDC Best Practices for Comprehensive Tobacco Control Programs - 2014",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vm4m-idi8/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vm4m-idi8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vm4m-idi8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vm4m-idi8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "theme": [
+                "Funding"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfmdr/search.CFM",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "temporal": "1992-01-01/1996-07-31",
+            "@type": "dcat:Dataset",
+            "modified": "1996-07-31",
+            "references": [
+                "http://www.fda.gov/MedicalDevices/Safety/ReportaProblem/ucm124073.htm"
+            ],
+            "keyword": [
+                "cdrh"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "openFDA",
+                "hasEmail": "mailto:open@fda.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "identifier": "290bc7d6-538c-4889-823f-2ec60b6d3b6a",
+            "description": "This database allows you to search the CDRH's database information on medical devices which may have malfunctioned or caused a death or serious injury during the years 1992 through 1996.",
+            "title": "MDR (Medical Device Reporting)",
+            "programCode": [
+                "009:005"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfmdr/search.CFM",
+                    "mediaType": "text/html"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/saz5-9hgg",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2021-02-24",
+            "@type": "dcat:Dataset",
+            "modified": "2021-06-17",
+            "keyword": [
+                "coronavirus",
+                "covid-19",
+                "vaccination"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "ASPA Media",
+                "hasEmail": "mailto:media@hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/saz5-9hgg",
+            "description": "New weekly allocations of doses are posted every Tuesday.  Beginning the following Thursday, states can begin ordering doses from that week\u2019s new allocation of 1st doses.  Beginning two weeks (Pfizer) or three weeks (Moderna) from the following Sunday, states can begin ordering doses from that week\u2019s new allocation of 2nd doses. After doses are ordered by states, shipments begin the following Monday. The entire order may not arrive in one shipment or on one day, but over the course of the week.\n\nSecond doses are opened up for orders on Sundays, at the appropriate interval two or three weeks later according to the manufacturer\u2019s label, with shipments occurring after jurisdictions place orders. \n\nShipments of an FDA-authorized safe and effective COVID-19 vaccine continue to arrive at sites across America. Vaccinations began on December 14, 2020. \n\nhttps://www.hhs.gov/coronavirus/covid-19-vaccines/index.html\n\nModerna Vaccine Data - https://data.cdc.gov/Vaccinations/COVID-19-Vaccine-Distribution-Allocations-by-Juris/b7pe-5nws\n\nJanssen Vaccine Data - https://data.cdc.gov/Vaccinations/COVID-19-Vaccine-Distribution-Allocations-by-Juris/w9zu-fywh",
+            "title": "COVID-19 Vaccine Distribution Allocations by Jurisdiction - Pfizer",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/saz5-9hgg/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/saz5-9hgg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/saz5-9hgg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/saz5-9hgg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "theme": [
+                "Vaccinations"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/8i5t-42wz",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2016-10-18",
+            "@type": "dcat:Dataset",
+            "modified": "2016-10-18",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/8i5t-42wz",
+            "description": "Rate of deaths by age/gender (per 100,000 population) for motor vehicle occupants killed in crashes, 2012 & 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Safety Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
+            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014, Region 8 - Denver",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8i5t-42wz/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8i5t-42wz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8i5t-42wz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8i5t-42wz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Motor Vehicle"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-02-01",
+            "@type": "dcat:Dataset",
+            "temporal": "2020-01-01/2021-01-30",
+            "modified": "2023-04-03",
+            "keyword": [
+                "all causes",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "education",
+                "hispanic origin",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "race",
+                "united states"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/i6ej-9eac",
+            "description": "Provisional counts of deaths in the United States by race and educational attainment. The dataset includes cumulative provisional counts of death for COVID-19, coded to ICD-10 code U07.1 as an underlying or multiple cause of death.",
+            "title": "AH Provisional COVID-19 Deaths by Race and Educational Attainment",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/i6ej-9eac/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/i6ej-9eac/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/i6ej-9eac/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/i6ej-9eac/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "irregular",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/bwwd-cuna",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-15",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Allergy and Clinical Immunology Branch (ACIB), Health Effects Laboratory Division (HELD)",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/bwwd-cuna",
+            "description": "Aspergillus versicolor is ubiquitous in the environment and is particularly abundant in damp indoor spaces. Exposure to Aspergillus species, as well as other environmental fungi, has been linked to adverse health outcomes including asthma, allergy, and even local or disseminated infection. However, the pulmonary immunological mechanisms associated with repeated exposure to A. versicolor have remained relatively uncharacterized. Here, A. versicolor was cultured and desiccated on rice, then placed in an acoustical generator system to achieve aerosolization. Mice were challenged with titrated doses of aerosolized conidia to examine deposition, lymphoproliferative properties, and then the immunotoxicological response to repeated inhalation exposures. The necessary dose to induce lymphoproliferation, but not infection-like pathology, was identified. Further, it was determined that the dose was able to initiate localized immune responses. The data presented in this study demonstrate an optimized and reproducible method for delivering A. versicolor conidia to rodents via nose-only inhalation. Additionally, the feasibility of a long-term repeated exposure study was established.  This experimental protocol can be used in future studies to investigate physiological effects of repeated pulmonary exposure to fungal conidia utilizing a practical and relevant mode of delivery. In total, these data constitute an important foundation for subsequent research in the field.",
+            "title": "Optimization of Aspergillus versicolor culture and aerosolization in a murine model of inhalational fungal exposure",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/bwwd-cuna/application/x-zip-compressed",
+                    "mediaType": "application/x-zip-compressed"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "National Institute for Occupational Safety and Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/ncezid/dfwed/beam-dashboard.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2025-01-21",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-21",
+            "keyword": [
+                "beam",
+                "beam dashboard",
+                "campylobacteriosis",
+                "escherichia",
+                "salmonella"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "SIMSO",
+                "hasEmail": "mailto:simso@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/8na9-qgz7",
+            "description": "The BEAM (Bacteria, Enterics, Amoeba, and Mycotics) Dashboard is an interactive tool to access and visualize data from the System for Enteric Disease Response, Investigation, and Coordination (SEDRIC). The BEAM Dashboard provides timely data on pathogen trends and serotype details to inform work to prevent illnesses from food and animal contact.",
+            "title": "BEAM Dashboard - Serotypes of concern: Burden and Trajectory",
+            "programCode": [
+                "009:028"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8na9-qgz7/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8na9-qgz7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8na9-qgz7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8na9-qgz7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "US",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Annually",
+            "theme": [
+                "Foodborne",
+                "Waterborne",
+                "and Related Diseases"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/a37y-w96i",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2016-09-14",
+            "@type": "dcat:Dataset",
+            "modified": "2016-09-14",
+            "keyword": [
+                "cdc",
+                "centers for disease control and prevention"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/a37y-w96i",
+            "description": "Source: Behavioral Risk Factor Surveillance System (BRFSS), 2012, 2014",
+            "title": "Percentage of Adults Who Report Driving After Drinking Too Much (in the past 30 days), 2012 & 2014, Region 8 - Denver",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/a37y-w96i/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/a37y-w96i/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/a37y-w96i/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/a37y-w96i/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Motor Vehicle"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/scme-3d32",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2014-11-07",
+            "temporal": "2018-01-01T00:00:00+00:00/2019-01-01T00:00:00+00:00",
+            "@type": "dcat:Dataset",
+            "modified": "2021-08-23",
+            "keyword": [
+                "drug acquisition cost",
+                "nadac"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "8de1b213-73c5-552b-b84e-ac795f34d056",
+            "description": "National Average Drug Acquisition Cost (NADAC) weekly reference data for the calendar year.",
+            "title": "NADAC (National Average Drug Acquisition Cost) 2018",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/nadac-national-average-drug-acquisition-cost.a4y5-998d.8de1b213-73c5-552b-b84e-ac795f34d056.csv",
+                    "mediaType": "text/csv",
+                    "title": "CSV"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P10Y",
+            "theme": [
+                "National Average Drug Acquisition Cost",
+                "Drug Pricing and Payment"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.cdc.gov/nccdphp/DNPAO/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-06-28",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-25",
+            "keyword": [
+                "breastfeeding",
+                "nutrition physical activity and weight status",
+                "policy"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Division of Nutrition, Physical Activity, and Obesity",
+                "hasEmail": "mailto:dnpaoinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/8hus-y5nc",
+            "description": "Community-Based Survey of Supports for Healthy Eating and Active Living (CBS HEAL) is a CDC survey of a nationally representative sample of U.S. municipalities to better understand existing community-level policies and practices that support healthy eating and active living. The survey collects information about policies such as nutrition standards, incentives for healthy food retail, bike/pedestrian-friendly design, and Complete Streets. About 2,000 municipalities respond to the survey. Participating municipalities receive a report that allows them to compare their policies and practices with other municipalities of similar geography, population size, and urban status.\n\nThe CBS HEAL survey was first administered in 2014 and was administered again in 2021. Data is provided in multiple formats for download including as a SAS file. A methods report and a SAS program for formatting the data are also provided.",
+            "title": "National Community Based Survey of Supports for Healthy Eating and Active Living  (CBS HEAL)",
+            "programCode": [
+                "009:029"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8hus-y5nc/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8hus-y5nc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8hus-y5nc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8hus-y5nc/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "theme": [
+                "Nutrition",
+                "Physical Activity",
+                "and Obesity"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/vaccines/data-reporting/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-10-16",
+            "@type": "dcat:Dataset",
+            "temporal": "2022-23, 2023-2024, & 2024-25",
+            "modified": "2025-01-29",
+            "keyword": [
+                "flu vaccination",
+                "iis",
+                "iqvia",
+                "nis-acm",
+                "vsd"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "VaxView Team",
+                "hasEmail": "mailto:VaxView@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/b6ny-6cd5",
+            "description": "\u2022 Monthly Cumulative Percent of Persons Who Received \u22651 Influenza Vaccination Doses and Comparison Between 2024-25 and Two Previous Seasons, by Jurisdiction, United States.\n\n\u2022 Influenza (flu) vaccination coverage for children and adults is assessed through U.S. jurisdictions\u2019 Immunization Information Systems Resources (IIS) data, submitted from jurisdictions to CDC monthly, in aggregate, by age group (https://www.cdc.gov/iis/about/).",
+            "title": "Monthly Cumulative Number and Percent of Who Received \u22651 Influenza Vaccination Doses and Comparison Between 2024-25 and Two Previous Seasons, by Jurisdiction, United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/b6ny-6cd5/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/b6ny-6cd5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/b6ny-6cd5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/b6ny-6cd5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States- National",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Monthly",
+            "theme": [
+                "Flu Vaccinations"
+            ],
+            "language": [
+                "English"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2010-0",
+            "issued": "2016-05-23",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "addiction",
+                "alcohol",
+                "alcohol abuse",
+                "alcohol consumption",
+                "amphetamines",
+                "barbiturates",
+                "cocaine",
+                "controlled drugs",
+                "crack cocaine",
+                "demographic characteristics",
+                "depression (psychology)",
+                "drinking behavior",
+                "drug abuse",
+                "drug dependence",
+                "drugs",
+                "drug treatment",
+                "drug use",
+                "employment",
+                "hallucinogens",
+                "health care",
+                "heroin",
+                "households",
+                "income",
+                "inhalants",
+                "marijuana",
+                "mental health",
+                "mental health services",
+                "methamphetamine",
+                "pregnancy",
+                "prescription drugs",
+                "sedatives",
+                "smoking",
+                "stimulants",
+                "substance abuse",
+                "substance abuse treatment",
+                "tobacco use",
+                "tranquilizers",
+                "youths"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Substance Abuse & Mental Health Services Administration"
+            },
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2010-nid13572",
+            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment history and perceived need for treatment, and included questions from the Diagnostic and Statistical Manual (DSM) of Mental Disorders that allow diagnostic criteria to be applied. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing. Questions introduced in previous administrations were retained in the 2010 survey, including questions asked only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes toward drug use and activities such as school work. Several measures focused on prevention-related themes in this section. Also retained were questions on mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking. Questions on the tobacco brand used most often were introduced with the 1999 survey. For the 2008 survey, adult mental health questions were added to measure symptoms of psychological distress in the worst period of distress that a person experienced in the past 30 days and suicidal ideation. In 2008, a split-sample design also was included to administer separate sets of questions (WHODAS vs. SDS) to assess impairment due to mental health problems. Beginning with the 2009 NSDUH, however, all of the adults in the sample received only the WHODAS questions. Background information includes gender, race, age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.This study has 1 Data Set.</p>",
+            "title": "National Survey on Drug Use and Health (NSDUH-2010)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2010-nid13572",
+                    "description": "National Survey on Drug Use and Health (NSDUH-2010) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2010-nid13572"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-10-11",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-25",
+            "references": [
+                "https://www.cdc.gov/places/measure-definitions/index.html"
+            ],
+            "keyword": [
+                "behaviors",
+                "brfss",
+                "county",
+                "health",
+                "outcomes",
+                "places",
+                "prevalence",
+                "prevention",
+                "risk",
+                "status"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "PLACES Public Inquiries",
+                "hasEmail": "mailto:places@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/pqpp-u99h",
+            "description": "This dataset contains model-based county-level estimates for the PLACES 2021 release. PLACES is the expansion of the original 500 Cities Project and covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code Tabulation Area (ZCTA) levels. It represents a first-of-its kind effort to release information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. The dataset includes estimates for 29 measures: 4 chronic disease-related health risk behaviors, 13 health outcomes, 3 health status, and 9 on using preventive services. These estimates can be used to identify emerging health problems and to help develop and carry out effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2019 or 2018 data, Census Bureau 2019 or 2018 county population estimate data, and American Community Survey (ACS) 2015\u20132019 or 2014\u20132018 estimates. The 2021 release uses 2019 BRFSS data for 22 measures and 2018 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours a night). Seven measures are based on the 2018 BRFSS because the relevant questions are only asked every other year in the BRFSS. More information about the methodology can be found at www.cdc.gov/places.",
+            "title": "PLACES: Local Data for Better Health, County Data 2021 release",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pqpp-u99h/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pqpp-u99h/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pqpp-u99h/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pqpp-u99h/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-County-Data-20/swc5-untb",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "500 Cities & Places"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2020-09-11",
+            "@type": "dcat:Dataset",
+            "modified": "2022-04-01",
+            "keyword": [
+                "age",
+                "age group",
+                "census region",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "hispanic origin",
+                "monthly",
+                "mortality",
+                "nchs",
+                "nvss",
+                "place of death",
+                "provisional",
+                "race",
+                "sex",
+                "united states"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/aie4-agrk",
+            "description": "Deaths involving coronavirus disease 2019 (COVID-19) by month of death, region, age, place of death, and race and Hispanic origin.",
+            "title": "AH Monthly Provisional COVID-19 Deaths, by Census Region, Age, and Race and Hispanic Origin",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/aie4-agrk/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/aie4-agrk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/aie4-agrk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/aie4-agrk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "irregular",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/sdsu-w7mh",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-03-28",
+            "@type": "dcat:Dataset",
+            "modified": "2024-01-05",
+            "keyword": [
+                "chip",
+                "dq atlas",
+                "major eligibility group",
+                "medicaid",
+                "t-msis analytic files"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "ea9b7db3-db71-4663-b4e1-67e11d1d4fcc",
+            "description": "This data set includes monthly enrollment counts of Medicaid and CHIP beneficiaries by major eligibility group (children, adult expansion group, adult, aged, persons with disabilities, or COVID newly-eligible).\r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating these measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable or of high concern  based on DQ Atlas thresholds for the topic Eligibility Group Code. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+            "title": "Major Eligibility Group Information for Medicaid and CHIP Beneficiaries by Month",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/MajorEligibilityGroup-montly.csv",
+                    "description": "This data set includes monthly enrollment counts of Medicaid and CHIP beneficiaries by major eligibility group (children, adult expansion group, adult, aged, persons with disabilities, or COVID newly-eligible).\n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating these measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable or of high concern  based on DQ Atlas thresholds for the topic Eligibility Group Code. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "@type": "dcat:Distribution",
+                    "title": "Major Eligibility Group Information for Medicaid and CHIP Beneficiaries by Month"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y",
+            "theme": [
+                "Enrollment"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://ii.nlm.nih.gov/MTI/index.shtml",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-06-30",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "api",
+                "history of medicine",
+                "medical informatics",
+                "terminologies",
+                "tools & utilities"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Library of Medicine",
+                "hasEmail": "mailto:custserv@nlm.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Library of Medicine"
+            },
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ivwm-qssp",
+            "description": "A system for producing indexing recommendations to assist in the indexing process at NLM.  Currently provides indexing recommendations to more than 100 journals based on the NLM Medical Subject Headings (MeSH) vocabulary.\n\nMTI is the main product of the Indexing Initiative project and has been providing indexing recommendations based on the Medical Subject Headings (MeSH\u00ae) vocabulary since 2002. In 2011, NLM expanded MTI's role by designating it as the first-line indexer (MTIFL) for a few journals; today the MTIFL workflow includes over 350 journals and continues to increase. The close collaboration of the NLM Index Section, Lister Hill National Center for Biomedical Communications, and Office of Computer & Communications Systems continues to expand and refine the ability of MTI to provide assistance to the indexers.",
+            "title": "Medical Text Indexer (MTI)",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://ii.nlm.nih.gov/MTI/index.shtml",
+                    "mediaType": "text/html",
+                    "title": "Access NLM Medical Text Indexer (MTI)"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Terminology"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/se7n-wqxt",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2024-11-02",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-24",
+            "references": [
+                "https://www.mathematica.org/"
+            ],
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "4256aa88-c7ba-582e-aec6-f6f905c70cb3",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "CoreSEt filters v2.10.6 (coreset-etl-test)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.6/20241023/filters.csv",
+                    "description": "CoreSEt filters v2.10.6 (coreset-etl-test)",
+                    "@type": "dcat:Distribution",
+                    "title": "CoreSEt filters v2.10.6 (coreset-etl-test)"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/8zak-ewtm",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2013-08-02",
+            "@type": "dcat:Dataset",
+            "modified": "2015-08-27",
+            "keyword": [
+                "brfss",
+                "current smokers",
+                "former smoker",
+                "non-smoker"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/8zak-ewtm",
+            "description": "Percentages are weighted to population characteristics. Data are not available if it did not meet BRFSS stability requirements.For more information on these requirements, as well as risk factors and calculated variables, see the Technical Documents and Survey Data for a specific year - http://www.cdc.gov/brfss/annual_data/annual_data.htm.Recommended citation: Centers for Disease Control and Prevention (CDC). Behavioral Risk Factor Surveillance System. Atlanta, Georgia: U.S. Department of Health and Human Services, Centers for Disease Control and Prevention, [appropriate year].",
+            "title": "BRFSS Prevalence and Trends Data: Tobacco Use - Four Level Smoking Data for 1995-2010",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8zak-ewtm/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8zak-ewtm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8zak-ewtm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8zak-ewtm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Smoking & Tobacco Use"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/kebt-3t25",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-01-21",
+            "@type": "dcat:Dataset",
+            "modified": "2022-01-12",
+            "keyword": [
+                "2021",
+                "nedss",
+                "netss",
+                "nndss",
+                "paralytic",
+                "pertussis",
+                "plague",
+                "poliomyelitis",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/kebt-3t25",
+            "description": "NNDSS - TABLE 1Z. Pertussis to Poliomyelitis, paralytic - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1Z. Pertussis to Poliomyelitis, paralytic",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kebt-3t25/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kebt-3t25/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kebt-3t25/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kebt-3t25/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/seqp-2d8w",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2017-12-01",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-16",
+            "keyword": [
+                "medicaid"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "52ed908b-0cb8-5dd2-846d-99d4af12b369",
+            "description": "The Medicaid Managed Care Enrollment Report profiles enrollment statistics on Medicaid managed care programs on a plan-specific level. The managed care enrollment statistics include enrollees receiving comprehensive benefits and limited benefits and are point-in-time counts.\r\n\r\n1. Total Medicaid Enrollees represents an unduplicated count of all beneficiaries in FFS and any type of managed care, including Medicaid-only and Medicare-Medicaid (\"dual\") enrollees.\t\t\t\t\r\n2. Total Medicaid enrollment in Any Type of Managed Care represents an unduplicated count of beneficiaries enrolled in any Medicaid managed care program, including comprehensive MCOs, limited benefit MCOs, and PCCMs.\r\n3. The \u201cMedicaid Enrollment in Comprehensive Managed Care\u201d column represents an unduplicated count of Medicaid beneficiaries enrolled in a managed care plan that provides comprehensive benefits (acute, primary care, specialty, and any other), or PACE program. It excludes beneficiaries who are enrolled in a Financial Alignment Demonstration Medicare-Medicaid Plan as their only form of managed care.\t\t\t\r\n4. The \u201cMedicaid Enrollment in Comprehensive MCOs Under ACA Section VIII Expansion\u201d column is a subset of the total reported in column C and includes individuals who are enrolled in comprehensive MCOs and are low-income adults, with or without dependent children, eligible for Medicaid under ACA Section VIII.\r\n5. n/a\" indicates that a state or territory was either not able to report data or does not operate a managed care program.",
+            "title": "Managed Care Enrollment Summary",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/managed-care-enrollment-summary-2022-table1.csv",
+                    "mediaType": "text/csv",
+                    "title": "CSV"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P10Y",
+            "theme": [
+                "Enrollment"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2013",
+            "issued": "2016-05-23",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "addiction",
+                "alcohol",
+                "alcohol abuse",
+                "alcohol consumption",
+                "amphetamines",
+                "barbiturates",
+                "cocaine",
+                "controlled drugs",
+                "crack cocaine",
+                "demographic characteristics",
+                "depression (psychology)",
+                "drinking behavior",
+                "drug abuse",
+                "drug dependence",
+                "drugs",
+                "drug treatment",
+                "drug use",
+                "employment",
+                "hallucinogens",
+                "health care",
+                "heroin",
+                "households",
+                "income",
+                "inhalants",
+                "marijuana",
+                "mental health",
+                "mental health services",
+                "methamphetamine",
+                "pregnancy",
+                "prescription drugs",
+                "sedatives",
+                "smoking",
+                "stimulants",
+                "substance abuse",
+                "substance abuse treatment",
+                "tobacco use",
+                "tranquilizers",
+                "youths"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Brooklyn Lupari, SAMHSA/CBHSQ c/o SAMHDA Support",
+                "hasEmail": "mailto:samhda-support@samhsa.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Substance Abuse & Mental Health Services Administration"
+            },
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2013-nid13555",
+            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment history and perceived need for treatment, and included questions from the Diagnostic and Statistical Manual (DSM) of Mental Disorders that allow diagnostic criteria to be applied. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing. Questions introduced in previous administrations were retained in the 2013 survey, including questions asked only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes toward drug use and activities such as school work. Several measures focused on prevention-related themes in this section. Also retained were questions on mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking. Questions on the tobacco brand used most often were introduced with the 1999 survey. For the 2008 survey, adult mental health questions were added to measure symptoms of psychological distress in the worst period of distress that a person experienced in the past 30 days and suicidal ideation. In 2008, a split-sample design also was included to administer separate sets of questions (WHODAS vs. SDS) to assess impairment due to mental health problems. Beginning with the 2009 NSDUH, however, all of the adults in the sample received only the WHODAS questions. Background information includes gender, race, age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.This study has 1 Data Set.</p>",
+            "title": "National Survey on Drug Use and Health (NSDUH-2013)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2013-nid13555",
+                    "description": "National Survey on Drug Use and Health (NSDUH-2013) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2013-nid13555"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/sfha-xqk6",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2022-08-10",
+            "@type": "dcat:Dataset",
+            "modified": "2022-08-17",
+            "keyword": [
+                "individual",
+                "individual market dental",
+                "py2022",
+                "qhp landscape",
+                "sadp"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Center for Consumer Information and Insurance Oversight",
+                "hasEmail": "mailto:CMS_FEPS@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Center for Consumer Information and Insurance Oversight"
+            },
+            "identifier": "0ad77e97-5a72-46a0-ba74-37a159d100f7",
+            "description": "The Dental Individual Market file of the QHP Landscape Files contains information on certified dental plans offered through an Exchange to consumers in the individual market. These plans are also known as Stand-alone Dental Plans (SADPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
+            "title": "QHP Landscape PY2022 Individual Dental",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2022/individual_market_dental.zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/sfsy-6enj",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-11-02",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-28",
+            "keyword": [
+                "drug rebate program"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "5f23f199-d3cf-44a1-b39c-cd6e34af7a29",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 10-21-2024-to-10-27-2024",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/mdrp-newly-rprt-drug-10-21-2024-to-10-27-2024.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/dy4n-fbwg",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-04-23",
+            "@type": "dcat:Dataset",
+            "modified": "2020-01-02",
+            "keyword": [
+                "2019",
+                "nedss",
+                "netss",
+                "nndss",
+                "vancomycin-resistant staphylococcus aureus",
+                "varicella morbidity",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/dy4n-fbwg",
+            "description": "NNDSS - TABLE 1KK. Vancomycin-resistant Staphylococcus aureus to Varicella morbidity - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1KK. Vancomycin-resistant Staphylococcus aureus to Varicella morbidity",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dy4n-fbwg/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dy4n-fbwg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dy4n-fbwg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dy4n-fbwg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NNDSS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/cms-innovation-models-overview/innovation-center-milestones-and-updates",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2025-01-05/2025-01-11",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-15",
+            "references": [
+                "https://data.cms.gov/resources/milestones-and-updates-methodology"
+            ],
+            "keyword": [
+                "children's health insurance program",
+                "medicare",
+                "medicare advantage",
+                "medicare prescription drug",
+                "original medicare",
+                "payment models",
+                "value-based care"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CMS Innovation Center - CMMI",
+                "hasEmail": "mailto:cmmi-dataset-support@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/4ce4157f-4e02-4188-b43a-2b21b7769b4e/data-viewer",
+            "description": "The Innovation Center Milestones and Updates dataset contains a variety of contributions from CMS Innovation Center models, demonstrations, initiatives and programs. These resources include relevant milestones, dates, and changes to the status or parameters of a model, demonstration, or initiative.",
+            "title": "Innovation Center Milestones and Updates",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4ce4157f-4e02-4188-b43a-2b21b7769b4e/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Innovation Center Milestones and Updates : 2025-01-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/7feff2bb-9f5c-46dc-822c-387843a9a584/Milestones%20and%20Updates-Upload-File-REACH-Flex-KCC-01-15-25.csv",
+                    "mediaType": "text/csv",
+                    "title": "Innovation Center Milestones and Updates : 2025-01-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3817f5a4-bb28-416e-93b5-9cd794a76024/data",
+                    "mediaType": "text/html",
+                    "title": "Innovation Center Milestones and Updates : 2025-01-15"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/milestones-and-updates-data-dictionary",
+            "dataQuality": true,
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1W",
+            "theme": [
+                "Medicare",
+                "Children's Health Insurance Program"
+            ],
+            "language": [
+                "en-US"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/statesystem/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-07-18",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-10",
+            "keyword": [
+                "legislation",
+                "osh",
+                "policy",
+                "preemption",
+                "state system",
+                "tobacco"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "OSHData Support",
+                "hasEmail": "mailto:nccdoshinquiries@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/hj2x-85ya",
+            "description": "1995-2024. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System. Legislation - Preemption. The STATE System houses current and historical state-level legislative data on tobacco use prevention and control policies. Data are reported on a quarterly basis. Data include information related to summary state preemption of more stringent or differing local laws on smokefree indoor air, youth access and licensure.",
+            "title": "CDC STATE System Tobacco Legislation - Preemption Summary",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hj2x-85ya/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hj2x-85ya/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hj2x-85ya/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hj2x-85ya/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-Tobacco-Legislation-Preemption-Su/hj2x-85ya",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "theme": [
+                "Legislation"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/shq4-bbik",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-08-08",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-30",
+            "references": [
+                "https://www.mathematica.org/"
+            ],
+            "keyword": [
+                "scorecard",
+                "utility"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "d1e8f0b9-7dbb-5840-974a-959a45bd100e",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "Scorecard filters v2.12.1-test (local)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.12.1-test/20241030/filters.csv",
+                    "description": "Scorecard filters v2.12.1-test (local)",
+                    "@type": "dcat:Distribution",
+                    "title": "Scorecard filters v2.12.1-test (local)"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/hcxx-dqtx",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-14",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Health Effects Laboratory Research, Toxicology and Molecular Biology Branch",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/hcxx-dqtx",
+            "description": "Exposure to certain engineered nanomaterials (ENMs) causes chronic lesions like lung fibrosis and cancer as a result of unresolved inflammation. Elucidating how ENM-induced inflammation is resolved is necessary for better evaluation of the fibrogenic and tumorigenic potentials of ENMs. This study aimed to identify pro-resolving mechanisms by analyzing the inflammatory and fibrogenic responses to multi-walled carbon nanotubes (MWCNTs, Mitsui-7) and fullerenes (fullerene C60, C60F) in B6C3F1 mice. The findings reveal that MWCNTs at a low dose (40 \u00b5g/mouse) and C60F at a high dose (>480 mg/mouse) stimulated acute neutrophilic inflammation, which exhibited rapid initiation and extended resolution. The lesion in MWCNT-exposed mice progressed to fibrotic granulomas by day 28 post-exposure, whereas it remained as alveolar histiocytosis in C60F-exposed mice. The ENMs induced high levels of proinflammatory lipid mediators leukotriene B4 (LTB4) and prostaglandin E2 (PGE2) with peaks at day 1, and high levels of special",
+            "title": "Resolution of Pulmonary Inflammation Induced by Carbon Nanotubes and Fullerenes in Mice: Role of Macrophage Polarization",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/hcxx-dqtx/application/x-zip-compressed",
+                    "mediaType": "application/x-zip-compressed"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "National Institute for Occupational Safety and Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/wff4-m3q3",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-01-21",
+            "@type": "dcat:Dataset",
+            "modified": "2022-01-12",
+            "keyword": [
+                "2021",
+                "age<5 years",
+                "confirmed",
+                "invasive pneumococcal disease",
+                "legionellosis",
+                "nedss",
+                "netss",
+                "nndss",
+                "probable",
+                "wonder"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC INFO",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/wff4-m3q3",
```

