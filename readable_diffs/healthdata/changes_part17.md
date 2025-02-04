# Change History for healthdata.json (Part 17)

### Changes from 761a84b to acf49f0 (Part 6/12)
**Author:** Automated

**Date:** 2025-01-31 15:36:25+00:00

**Message:** Updated data: Fri Jan 31 15:36:25 UTC 2025

```diff
+                    "title": "Medicare Demonstrations : 2024-04-12"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/7a4938ac-9dba-4a9e-bf4b-947f14bac68f/WDDSE_Medicare_Demonstrations-Fixes-04-12-2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Demonstrations : 2024-04-12"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/b35c77ac-26e2-4320-91e1-ba71c4d7ff2c/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Demonstrations : 2024-04-12"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/medicare-demonstrations-data-dictionary",
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
+            "landingPage": "http://www.accessdata.fda.gov/scripts/animaldrugsatfda/index.cfm",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "cvm",
+                "labeling"
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
+            "identifier": "ee7073db-55c0-46b0-b831-1c659fe7137d",
+            "description": "On November 16, 1988, the President of the United States signed into law the Generic Animal Drug and Patent Restoration Act (GADPTRA). Among its major provisions, the Act extends eligibility for submission of Abbreviated New Animal Drug Applications (ANADAs) to all animal drug products approved for safety and effectiveness under the Federal Food, Drug, and Cosmetic Act. The Act also requires that each sponsor of an approved animal drug product submit to the FDA certain information regarding patents held for the animal drug or its method of use. The Act requires that this information, as well as a list of all animal drug products approved for safety and effectiveness, be made available to the public. This list must be updated monthly under the provisions of the Act. This publication, which is known as the \ufffdGreen Book\ufffd, was first published in January of 1989. Updates have been added monthly since then. The list is published in its entirety each January.",
+            "title": "Approved Animal Drug Products (Green Book)",
+            "programCode": [
+                "009:004"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/animaldrugsatfda/index.cfm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P1Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/u7wx-dav2",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-04-26",
+            "@type": "dcat:Dataset",
+            "modified": "2019-05-30",
+            "keyword": [
+                "2019",
+                "(age <5 years)",
+                "haemophilus influenzae",
+                "invasive disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "non-b serotype",
+                "nontypeable",
+                "unknown serotype",
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
+            "identifier": "https://data.cdc.gov/api/views/u7wx-dav2",
+            "description": "NNDSS - TABLE 1N. Haemophilus influenzae, invasive disease, (age <5 years), Non-b serotype to Unknown serotype - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html\r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1N. Haemophilus influenzae, invasive disease, (age <5 years), Non-b serotype to Unknown serotype",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/u7wx-dav2/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/u7wx-dav2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/u7wx-dav2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/u7wx-dav2/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/dhdsp/index.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-08-11",
+            "@type": "dcat:Dataset",
+            "modified": "2024-04-09",
+            "references": [
+                "https://www.cdc.gov/dhdsp/index.htm",
+                "https://www.cdc.gov/dhdsp/maps/dtm/data_sources.htm",
+                "https://www.cdc.gov/dhdsp/maps/dtm/data_risks.htm"
+            ],
+            "keyword": [
+                "cardiovascular disease",
+                "claims data",
+                "heart disease",
+                "stroke"
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
+            "identifier": "https://data.cdc.gov/api/views/iw6q-r3ja",
+            "description": "2016\u20132021. CMS compiles claims data for Medicare and Medicaid patients across a variety of categories and years. This includes Inpatient and Outpatient claims, Master Beneficiary Summary Files, and many other files. Indicators from this data source have been computed by personnel in CDC's Division for Heart Disease and Stroke Prevention (DHDSP). This was one of the datasets provided by the National Cardiovascular Disease Surveillance System and presented on DHDSP\u2019s Data, Trends, and Maps online tool. This tool was retired in April of 2024 and this dataset will not be updated. Contact dhdsprequests@cdc.gov if you need assistance with data previously included in this dataset. The data are organized by location (national and state) and indicator. The data can be plotted as trends and stratified by sex and race/ethnicity.",
+            "title": "Center for Medicare & Medicaid Services (CMS) , Medicare Claims data",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/iw6q-r3ja/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/iw6q-r3ja/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/iw6q-r3ja/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/iw6q-r3ja/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Heart-Disease-Stroke-Prevention/Center-for-Medicare-Medicaid-Services-CMS-Medicare/iw6q-r3ja",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Heart Disease & Stroke Prevention"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.cdc.gov/Widgets/",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2025-01-30",
+            "@type": "dcat:Dataset",
+            "modified": "2012-05-30",
+            "keyword": [
+                "brownie",
+                "cake and pie",
+                "candy",
+                "cereal",
+                "cookie",
+                "cracker",
+                "donut",
+                "fda",
+                "federal widget",
+                "ice cream",
+                "national",
+                "peanut butter",
+                "pet food",
+                "product",
+                "product-recalls",
+                "recalls",
+                "salmonella",
+                "snack bars"
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
+            "identifier": "ece9c52a-ba02-4615-b441-fa0d2f8b9722",
+            "description": "The FDA Peanut-Containing Product Recall widget allows you to browse the Food and Drug Administration (FDA) database of peanut butter and peanut-containing products subject to recall. This database makes it easier for you to determine whether any of the products you have at home are subject to recent recalls, and will be updated as new information becomes available.",
+            "title": "FDA Peanut-Containing Product Recall",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.cdc.gov/Widgets/",
+                    "mediaType": "application/vnd.pmi.widget"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/bver-eziq",
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
+            "identifier": "58af1996-6af7-5b7c-82a8-6d69c5652420",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "CoreSEt measure v2.10.6 (coreset-etl-test)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.6/20241023/measure.csv",
+                    "description": "CoreSEt measure v2.10.6 (coreset-etl-test)",
+                    "@type": "dcat:Distribution",
+                    "title": "CoreSEt measure v2.10.6 (coreset-etl-test)"
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
+            "landingPage": "https://healthdata.gov/d/bvst-ezb8",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-12-10",
+            "@type": "dcat:Dataset",
+            "modified": "2024-12-18",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "py2025",
+                "service area"
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
+            "identifier": "46925516-0fb4-4e60-b00d-b0d7f7ddc372",
+            "description": "The Service Area PUF (SA-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The SA-PUF contains issuer-level data on geographic service areas including state, county, and zip code.",
+            "title": "Service Area PUF \u2013 PY2025",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2025/service_area_PUF.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/v76h-zdce",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2020-06-01",
+            "@type": "dcat:Dataset",
+            "modified": "2021-07-07",
+            "keyword": [
+                "air pollution",
+                "asthma",
+                "environmental health",
+                "ozone"
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
+            "identifier": "https://data.cdc.gov/api/views/v76h-zdce",
+            "description": "This dataset provides modeled predictions of ozone levels from the EPA's Downscaler model. Data are at the census tract level for 2001-2005. These data are used by the CDC's National Environmental Public Health Tracking Network to generate air quality measures. Census tract-level datasets contain estimates of the mean predicted concentration and associated standard error. Please refer to the metadata attachment for more information.\n\nLearn more about outdoor air quality on the Tracking Network's website: https://ephtracking.cdc.gov/showAirLanding.action.\n\nBy using these data, you signify your agreement to comply with the following requirements:\n1. Use the data for statistical reporting and analysis only.\n2. Do not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals.\n3. Do not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov.\n4. Do not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating.\n5. Acknowledge, in all reports or presentations based on these data, the original source of the data and CDC.\n6. Suggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking.",
+            "title": "Daily Census Tract-Level Ozone Concentrations, 2001-2005",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/v76h-zdce/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/v76h-zdce/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/v76h-zdce/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/v76h-zdce/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/ekd3-qu3w",
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
+                "rmsf",
+                "spotted fever rickettsiosis",
+                "syphilis primary and secondary",
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
+            "identifier": "https://data.cdc.gov/api/views/ekd3-qu3w",
+            "description": "NNDSS - Table II. Spotted Fever Rickettsiosis to Syphilis - 2015.In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.    NP: Nationally notifiable but not published.    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table 2 to facilitate case count verification with reporting jurisdictions. \ufffd\ufffd\ufffd Case counts for reporting year 2015 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \ufffd\ufffd Illnesses with similar clinical presentation that result from Spotted fever group rickettsia infections are reported as Spotted fever rickettsioses. Rocky Mountain spotted fever (RMSF) caused by Rickettsia rickettsii, is the most common and well-known spotted fever.",
+            "title": "NNDSS - Table II. Spotted Fever Rickettsiosis to Syphilis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ekd3-qu3w/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ekd3-qu3w/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ekd3-qu3w/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ekd3-qu3w/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/bw9e-y3qb",
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
+            "identifier": "85272998-7ec9-4bd9-87ef-8c75156436ac",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20210830 to 20210905",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rpt-drugs-sept-20210830-to-20210905.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2014",
+            "issued": "2016-05-23",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
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
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2014-nid13618",
+            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment history and perceived need for treatment, and included questions from the Diagnostic and Statistical Manual (DSM) of Mental Disorders that allow diagnostic criteria to be applied. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing. Questions introduced in previous administrations were retained in the 2014 survey, including questions asked only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes toward drug use and activities such as school work. Several measures focused on prevention-related themes in this section. Also retained were questions on mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking. Questions on the tobacco brand used most often were introduced with the 1999 survey. For the 2008 survey, adult mental health questions were added to measure symptoms of psychological distress in the worst period of distress that a person experienced in the past 30 days and suicidal ideation. In 2008, a split-sample design also was included to administer separate sets of questions (WHODAS vs. SDS) to assess impairment due to mental health problems. Beginning with the 2009 NSDUH, however, all of the adults in the sample received only the WHODAS questions. Background information includes gender, race, age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.<br />\nThis study has 1 Data Set.</p>",
+            "title": "National Survey on Drug Use and Health (NSDUH-2014)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2014-nid13618",
+                    "description": "National Survey on Drug Use and Health (NSDUH-2014) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2014-nid13618"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/rg4j-6mcc",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2015-01-08",
+            "@type": "dcat:Dataset",
+            "modified": "2015-08-27",
+            "keyword": [
+                "2014",
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
+            "identifier": "https://data.cdc.gov/api/views/rg4j-6mcc",
+            "description": "NNDSS - Table II. Hepatitis (viral, acute) - 2014.In this Table, all conditions with a 5-year average annual national total of more than or equals 1,000 cases but less than or equals 10,000 cases will be displayed (\ufffd\ufffd\ufffd 1,000 and \ufffd\ufffd_ 10,000). The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Case counts for reporting years 2013 and 2014 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly.More information on NNDSS is available at http://wwwn.cdc.gov/nndss/.",
+            "title": "NNDSS - Table II. Hepatitis (viral, acute)",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rg4j-6mcc/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rg4j-6mcc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rg4j-6mcc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rg4j-6mcc/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cms.gov/quality-of-care/quality-payment-program-experience",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2017-01-01/2022-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2024-05-08",
+            "references": [
+                "https://data.cms.gov/sites/default/files/2024-04/2022%20QPP%20Experience%20Report%20Public%20Use%20Files%20Methodology.pdf"
+            ],
+            "keyword": [
+                "health care use & payments",
+                "medicare",
+                "original medicare"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Quality Payment Program - CCSQ",
+                "hasEmail": "mailto:qpp@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/7adb8b1b-b85c-4ed3-b314-064776e50180/data-viewer",
+            "description": "The Quality Payment Program (QPP) Experience dataset provides participation and performance information in the Merit-based Incentive Payment System (MIPS) during each performance year. They cover eligibility and participation, performance categories, and final score and payment adjustments. The dataset provides additional details at the TIN/NPI level on what was published in the previous performance year. You can sort the data by variables like clinician type, practice size, scores, and payment adjustments.",
+            "title": "Quality Payment Program Experience",
+            "describedByType": "application/pdf",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7adb8b1b-b85c-4ed3-b314-064776e50180/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Quality Payment Program Experience : 2022-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/a963b1e9-d6d2-47a5-a385-80e37884aca2/2022_puf.csv",
+                    "mediaType": "text/csv",
+                    "title": "Quality Payment Program Experience : 2022-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/b3438273-b4a6-44ca-8fb2-9e6026b74642/data",
+                    "mediaType": "text/html",
+                    "title": "Quality Payment Program Experience : 2022-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/0bac88bc-a4c8-4dff-bdbf-660d24e6a689/2021_puf_QPPAR-18260.csv",
+                    "mediaType": "text/csv",
+                    "title": "Quality Payment Program Experience : 2021-05-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8c2ab3e4-597e-43c9-9d94-7223c66d7f25/data",
+                    "mediaType": "text/html",
+                    "title": "Quality Payment Program Experience : 2021-05-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/fb3758dd-6ace-4ddb-863b-1b895cef4d7e/2020_puf_qppar_QPPAR-17660.csv",
+                    "mediaType": "text/csv",
+                    "title": "Quality Payment Program Experience : 2020-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/48a484e6-ff02-4284-8666-6045b3cac17f/data",
+                    "mediaType": "text/html",
+                    "title": "Quality Payment Program Experience : 2020-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/f9ef9f64-91d8-49a2-a1be-5a48bbdcc1e9/2019_puf_qppar_QPPAR-17661.csv",
+                    "mediaType": "text/csv",
+                    "title": "Quality Payment Program Experience : 2019-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5776e77d-a844-49fd-b697-a2b01bdacdc7/data",
+                    "mediaType": "text/html",
+                    "title": "Quality Payment Program Experience : 2019-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/d2a19b56-7a5f-49c7-b78d-4d0dd49b9391/2018_puf_qppar-QPPAR-17662.csv",
+                    "mediaType": "text/csv",
+                    "title": "Quality Payment Program Experience : 2018-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4cae2e39-693d-4699-ac23-2611b29c5da7/data",
+                    "mediaType": "text/html",
+                    "title": "Quality Payment Program Experience : 2018-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/d117f544-48ac-40be-9c30-74868837f587/2017_puf_qppar_QPPAR_17663.csv",
+                    "mediaType": "text/csv",
+                    "title": "Quality Payment Program Experience : 2017-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d87865f9-70b6-41fb-be3a-db735c4a05d2/data",
+                    "mediaType": "text/html",
+                    "title": "Quality Payment Program Experience : 2017-12-31"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-04/2022%20QPP%20Experience%20Report%20Public%20Use%20Files%20Data%20Dictionary.pdf",
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
+            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-04-08",
+            "temporal": "1950/2022",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-15",
+            "keyword": [
+                "american indian or alaska native",
+                "asian",
+                "black or african american",
+                "death rates",
+                "health us",
+                "heart disease",
+                "hispanic or latino",
+                "men",
+                "mortality",
+                "native hawaiian or other pacific islander",
+                "white",
+                "women"
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
+            "identifier": "https://data.cdc.gov/api/views/4892-xxjy",
+            "description": "Data on death rates for diseases of heart in the United States, by age, sex, race, and Hispanic origin. Data are from Health, United States. SOURCE: National Center for Health Statistics, National Vital Statistics System, Mortality File.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
+            "title": "DQS Death rates for heart disease, by sex, race, Hispanic origin, and age: United States from CDC WONDER",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4892-xxjy/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4892-xxjy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4892-xxjy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4892-xxjy/rows.xml?accessType=DOWNLOAD",
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
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2006-0",
+            "issued": "2016-05-23",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
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
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2006-nid13554",
+            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series<br />\n(formerly titled National Household Survey on Drug Abuse) primarily<br />\nmeasures the prevalence and correlates of drug use in the United<br />\nStates. The surveys are designed to provide quarterly, as well as<br />\nannual, estimates. Information is provided on the use of illicit<br />\ndrugs, alcohol, and tobacco among members of United States households<br />\naged 12 and older. Questions included age at first use as well as<br />\nlifetime, annual, and past-month usage for the following drug classes:<br />\nmarijuana, cocaine (and crack), hallucinogens, heroin, inhalants,<br />\nalcohol, tobacco, and nonmedical use of prescription drugs, including<br />\npain relievers, tranquilizers, stimulants, and sedatives. The survey<br />\ncovered substance abuse treatment history and perceived need for<br />\ntreatment, and included questions from the Diagnostic and Statistical<br />\nManual (DSM) of Mental Disorders that allow diagnostic criteria to be<br />\napplied. The survey included questions concerning treatment for both<br />\nsubstance abuse and mental health related disorders. Respondents were<br />\nalso asked about personal and family income sources and amounts,<br />\nhealth care access and coverage, illegal activities and arrest record,<br />\nproblems resulting from the use of drugs, and needle-sharing.<br />\nQuestions introduced in previous administrations were retained in the<br />\n2006 survey, including questions asked only of respondents aged 12 to<br />\n17. These \"youth experiences\" items covered a variety of topics, such<br />\nas neighborhood environment, illegal activities, drug use by friends,<br />\nsocial support, extracurricular activities, exposure to substance<br />\nabuse prevention and education programs, and perceived adult attitudes<br />\ntoward drug use and activities such as school work. Several measures<br />\nfocused on prevention-related themes in this section. Also retained<br />\nwere questions on mental health and access to care, perceived risk of<br />\nusing drugs, perceived availability of drugs, driving and personal<br />\nbehavior, and cigar smoking. Questions on the tobacco brand used most<br />\noften were introduced with the 1999 survey. Background information<br />\nincludes gender, race, age, ethnicity, marital status, educational<br />\nlevel, job status, veteran status, and current household composition.This study has 1 Data Set.</p>",
+            "title": "National Survey on Drug Use and Health (NSDUH-2006)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2006-nid13554",
+                    "description": "National Survey on Drug Use and Health (NSDUH-2006) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2006-nid13554"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.healthit.gov/data/datasets/2015-edition-market-readiness-hospitals-and-clinicians-data",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-10-03",
+            "@type": "dcat:Dataset",
+            "modified": "2019-04-01",
+            "references": [
+                "https://www.healthit.gov/data/quickstats/2015-edition-market-readiness-hospitals-and-clinicians"
+            ],
+            "keyword": [
+                "certified",
+                "ehrs",
+                "electronic health records",
+                "health information technology",
+                "health it",
+                "market"
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
+            "identifier": "j7aeu9v0-eudg-eqb6-3cik-gyv36mrqd7e7",
+            "description": "This dataset provides the proportion of developers, by market share, that have certified 2015 edition health IT modules. Market share approximations are determined through an analysis of the certified health IT products reported by participants in the Medicare EHR Incentive Program from 2011 to 2016. Approximations use the most recently reported data for each unique clinician and hospital participant. It is important to understand how to interpret these approximations. Some clinicians and hospitals report certified software from more than one unique developer. The market share percentages in this dataset, therefore, include some double counting (the percentages will, if summed together, add up above 100 percent.) The approximations convey the percent of hospitals and clinicians who use a developer's technology, and are not to be interpreted in aggregate as the percent of all hospitals and clinicians who have access to 2015 edition certified technology.",
+            "title": "2015 Edition Market Readiness for Hospitals and Clinicians Data",
+            "programCode": [
+                "009:110"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/2015-edition-market-readiness-hospitals-clinicians-data.csv",
+                    "mediaType": "text/csv",
+                    "title": "2015-edition-market-readiness-hospitals-clinicians-data.csv"
+                }
+            ],
+            "describedBy": "https://www.healthit.gov/data/datasets/2015-edition-market-readiness-hospitals-and-clinicians-data"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/bzbt-2kdz",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-02-28",
+            "@type": "dcat:Dataset",
+            "modified": "2024-02-26",
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
+            "identifier": "be496f61-3e23-47aa-b442-2334a1fbe40a",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 02-19-2024-to-02-25-2024",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/mdrp-newly-rprt-drug-02-19-2024-to-02-25-2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 02-19-2024-to-02-25-2024"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P10Y"
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
+            "temporal": "1970/2015",
+            "modified": "2022-03-29",
+            "references": [
+                "http://www.cdc.gov/nchs/data/databriefs/db162.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_01.pdf"
+            ],
+            "keyword": [
+                "age",
+                "births",
+                "nchs",
+                "nonmarital",
+                "percent distribution"
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
+            "identifier": "https://data.cdc.gov/api/views/hzd8-r9mj",
+            "description": "This dataset includes percent distribution of births to unmarried women by age group in the United States since 1970.\n\nMethods for collecting information on marital status changed over the reporting period and have been documented in:\n\n\u2022 Ventura SJ, Bachrach CA. Nonmarital childbearing in the United States, 1940\u201399. National vital statistics reports; vol 48 no 16. Hyattsville, Maryland: National Center for Health Statistics. 2000. Available from: http://www.cdc.gov/nchs/data/nvsr/nvsr48/nvs48_16.pdf.\n\u2022 National Center for Health Statistics. User guide to the 2013 natality public use file. Hyattsville, Maryland: National Center for Health Statistics. 2014. Available from: http://www.cdc.gov/nchs/data_access/VitalStatsOnline.htm.",
+            "title": "NCHS - Percent Distribution of Births to Unmarried Women by Age Group: United States",
+            "isPartOf": "NCHS - Percent Distribution of Births to Unmarried Women by Age Group: United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hzd8-r9mj/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hzd8-r9mj/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hzd8-r9mj/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hzd8-r9mj/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States",
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
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-spending-by-drug/medicaid-spending-by-drug",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2022-01-01/2022-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2024-06-13",
+            "references": [
+                "https://data.cms.gov/resources/medicaid-spending-by-drug-methodology"
+            ],
+            "keyword": [
+                "all other provider care types",
+                "drugs",
+                "medicaid"
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/be64fce3-e835-4589-b46b-024198e524a6/data-viewer",
+            "description": "The Medicaid by Drug dataset presents information on spending for covered outpatient drugs prescribed to beneficiaries enrolled in Medicaid by physicians and other healthcare professionals.\u00a0\n\n\u00a0\n\nThe dataset focuses on average spending per dosage unit and change in average spending per dosage unit over time. Units refer to the drug unit in the lowest dispensable amount. It also includes spending information for manufacturer(s) of the drugs as well as consumer-friendly information of drug uses and clinical indications.\n\n\u00a0\n\nDrug spending metrics for Medicaid represent the total amount reimbursed by both Medicaid and non-Medicaid entities to pharmacies for the drug. Medicaid drug spending contains both the Federal and State reimbursement and is inclusive of any applicable dispensing fees. In addition, this total is not reduced or affected by Medicaid rebates paid to the states.",
+            "title": "Medicaid Spending by Drug",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/be64fce3-e835-4589-b46b-024198e524a6/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Medicaid Spending by Drug : 2022-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/ec5c3a56-84b9-46e6-8f28-5900349821b9/DSD_MCD_RY24_P06_V20_D22_BGM.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicaid Spending by Drug : 2022-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/512a1a54-0d43-4aa2-adb6-3f1d19e9a917/data",
+                    "mediaType": "text/html",
+                    "title": "Medicaid Spending by Drug : 2022-01-01"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/medicaid-spending-by-drug-data-dictionary",
+            "dataQuality": true,
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "Medicaid"
+            ],
+            "language": [
+                "en-US"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-03-01",
+            "temporal": "1950/2021",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-15",
+            "keyword": [
+                "american indian or alaska native",
+                "asian",
+                "black or african american",
+                "death rates",
+                "health us",
+                "hispanic or latino",
+                "men",
+                "mental health",
+                "native hawaiian or other pacific islander",
+                "suicide",
+                "white",
+                "women"
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
+            "identifier": "https://data.cdc.gov/api/views/p7se-k3ix",
+            "description": "Data on death rates for suicide in the United States, by age, sex, race, and Hispanic origin. Data are from Health, United States. SOURCE: National Center for Health Statistics, National Vital Statistics System, Mortality File.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
+            "title": "DQS Death rates for suicide, by sex, race, Hispanic origin, and age: United States from CDC WONDER",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/p7se-k3ix/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/p7se-k3ix/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/p7se-k3ix/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/p7se-k3ix/rows.xml?accessType=DOWNLOAD",
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
+            "accessLevel": "non-public",
+            "landingPage": "http://www.cdc.gov/STATESystem",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2025-01-31",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-31",
+            "keyword": [
+                "global",
+                "gtss",
+                "gyts",
+                "osh",
+                "tobacco",
+                "youth"
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
+            "identifier": "https://data.cdc.gov/api/views/57qw-ifet",
+            "description": "1999-2018. The GYTS is a school-based survey that collects data on students aged 13\u201315 years using a standardized methodology for constructing the sample frame, selecting schools and classes, and processing data. The GYTS surveillance system is intended to enhance the capacity of countries to design, implement, and evaluate tobacco control and prevention programs. Funding for the GYTS has been provided by the Canadian Public Health Association, National Cancer Institute, United Nations Children Emergency Fund, and the World Health Organization\u2014Tobacco Free Initiative.",
+            "title": "Global Tobacco Surveillance System (GTSS) - Global Youth Tobacco Survey (GYTS)",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/57qw-ifet/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/57qw-ifet/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/57qw-ifet/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/57qw-ifet/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Global-Survey-Data/Global-Tobacco-Surveillance-System-GTSS-Global-You/57qw-ifet",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Global Survey Data"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/c2aj-88y2",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2024-11-13",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-12",
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
+            "identifier": "792f9cf5-a4c9-5d41-a267-14ff9962456b",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "CoreSEt version v2.10.16 (coreset-dev0)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.16/20241029/version.csv",
+                    "description": "CoreSEt version v2.10.16 (coreset-dev0)",
+                    "@type": "dcat:Distribution",
+                    "title": "CoreSEt version v2.10.16 (coreset-dev0)"
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
+            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-02-21",
+            "temporal": "1989/2015",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-01",
+            "keyword": [
+                "american indian or alaska native",
+                "asian or pacific islander",
+                "black or african american",
+                "child and adolescent",
+                "deaths",
+                "health us",
+                "hispanic or latino",
+                "infant mortality",
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
+            "identifier": "https://data.cdc.gov/api/views/pjb2-jvdr",
+            "description": "This topic is no longer available in the NCHS Data Query System (DQS). Search, visualize, and download other estimates from over 120 health topics with DQS, available from: https://www.cdc.gov/nchs/dataquery/index.htm.\nData on on average annual infant mortality rates in the United States and U.S. dependent areas, by race and Hispanic origin of mother, state, and territory. Data are from Health, United States. SOURCE: National Center for Health Statistics, National Vital Statistics System, Linked Birth/Infant Death Data Set.",
+            "title": "DQS Infant mortality rates, by race and Hispanic origin of mother, state, and territory: United States and U.S. dependent areas (Archived)",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pjb2-jvdr/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pjb2-jvdr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pjb2-jvdr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pjb2-jvdr/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/c3dm-3fy7",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2022-08-31",
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
+            "identifier": "cf603cd1-db1f-533f-acad-d03954787bab",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "devAuto_measureSearchInfo",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measureSearchInfo.csv",
+                    "description": "{\"dataset\": \"measureSearchInfo\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "@type": "dcat:Distribution",
+                    "title": "measureSearchInfo csv file"
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
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2006",
+            "issued": "2016-05-23",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
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
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2006-nid13546",
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2006)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2006-nid13546",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2006) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2006-nid13546"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/c48b-9hs6",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2022-03-16",
+            "@type": "dcat:Dataset",
+            "modified": "2022-03-14",
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
+            "identifier": "aab40af5-2e31-478c-be9b-9475f919e9c7",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2022-03-07 to 2022-03-13",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rpt-drugs-mar-03-07-2022-03-13-2022.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.acf.hhs.gov/programs/ana/",
+            "bureauCode": [
+                "009:70"
+            ],
+            "issued": "2012-08-10",
+            "temporal": "2010-01-01T00:00:00-05:00/2010-01-01T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "administrative",
+                "social and economic  development"
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
+            "identifier": "73c33ee9-43a3-407a-8df9-186a43671599",
+            "description": "<p>The 2010 Congressional Report provides results for 70 ANA projects that ended in 2010. The report includes a brief summary of each project visited and an analysis of how ANA funding has impacted Native American communities.</p>",
+            "title": "Administration for Native Americans (ANA) Projects Report",
+            "programCode": [
+                "009:095"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.acf.hhs.gov/ana/research",
+                    "mediaType": "text/html",
+                    "title": "HTML"
+                }
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.accessdata.fda.gov/scripts/cber/CFAppsPub/",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2010-06-04",
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
+            "identifier": "a0710f78-0585-45c8-9320-7d252b291390",
+            "description": "This application provides information for active, inactive, and pre-registered firms. Query options are by FEI, Applicant Name, Establishment Name, Other Names, Establishment Type, Establishment Status, City, State, Zip Code, Country and Reporting Official First Name or Last Name.",
+            "title": "Blood Establishment Registration Database",
+            "programCode": [
+                "009:003"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.accessdata.fda.gov/scripts/cber/CFAppsPub/",
+                    "mediaType": "text/html"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/c5te-qbma",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-10-08",
+            "@type": "dcat:Dataset",
+            "modified": "2022-09-21",
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
+            "identifier": "53426d8c-82b5-5dec-b44b-0f935b4603e5",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "devAuto_files_stateSnapshot",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20220921_v2_ETL_DEV/files_stateSnapshot.csv",
+                    "description": "{\"dataset\": \"files_stateSnapshot\", \"stage\": \"devAuto\", \"update_id\": \"20220921_v2_ETL_DEV\"}",
+                    "@type": "dcat:Distribution",
+                    "title": "files_stateSnapshot csv file"
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
+            "landingPage": "https://www.cdc.gov/prams/index.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-07-18",
+            "@type": "dcat:Dataset",
+            "modified": "2023-09-05",
+            "references": [
+                "https://www.cdc.gov/prams/index.htm",
+                "https://www.cdc.gov/prams/pramstat/index.html"
+            ],
+            "keyword": [
+                "abuse",
+                "alcohol use",
+                "breastfeeding",
+                "contraception",
+                "infant health",
+                "medicaid",
+                "mental health",
+                "morbidity",
+                "obesity",
+                "preconception health",
+                "pregnancy history",
+                "prenatal care",
+                "reproductive health",
+                "sleep behavior",
+                "smoke exposure",
+                "stress",
+                "tobacco use",
+                "unintended pregnancy",
+                "wic"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DRH Public Inquiries",
+                "hasEmail": "mailto:PRAMSProposals@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/u76f-m89e",
+            "description": "2003. Centers for Disease Control and Prevention (CDC). PRAMS, the Pregnancy Risk Assessment Monitoring System, is a surveillance system collecting state-specific, population-based data on maternal attitudes and experiences before, during, and shortly after pregnancy. It is a collaborative project of the Centers for Disease Control and Prevention (CDC) and state health departments. PRAMS provides data for state health officials to use to improve the health of mothers and infants. PRAMS topics include abuse, alcohol use, contraception, breastfeeding, mental health, morbidity, obesity, preconception health, pregnancy history, prenatal-care, sleep behavior, smoke exposure, stress, tobacco use, WIC, Medicaid, infant health, and unintended pregnancy. Data will be updated annually as it becomes available.",
+            "title": "CDC PRAMStat Data for 2003",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/u76f-m89e/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/u76f-m89e/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/u76f-m89e/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/u76f-m89e/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2003/u76f-m89e",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Maternal & Child Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/y8pa-p62q",
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
+            "identifier": "https://data.cdc.gov/api/views/y8pa-p62q",
+            "description": "Source for 2012 national data: National Occupant Protection Use Survey (NOPUS), 2012. Source for 2014 national data: National Occupant Protection Use Survey (NOPUS), 2014.  Source for 2012 state data: State Observational Survey of Seat Belt Use, 2012. Source for 2014 state data: Seat Belt Use in 2014- Use Rates in the States and Territories",
+            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, Region 7 - Kansas City",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/y8pa-p62q/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/y8pa-p62q/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/y8pa-p62q/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/y8pa-p62q/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "http://www.ncbi.nlm.nih.gov/geo/",
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
+                "fn": "Barret, Tanya",
+                "hasEmail": "mailto:barrett@ncbi.nlm.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
+            "identifier": "03c4f32c-8437-4eb5-af9f-bfb70ffaec73",
+            "description": "<p>Gene Expression Omnibus is a public functional genomics data repository supporting MIAME-compliant submissions of array- and sequence-based data. Tools are provided to help users query and download experiments and curated gene expression profiles.</p>",
+            "title": "Gene Expression Omnibus (GEO)",
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
+            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225439.htm",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2010-10-01",
+            "keyword": [
+                "food",
+                "health",
+                "market",
+                "notifications",
+                "peanut",
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
+            "identifier": "486663d1-b2cd-4ccc-b221-6f9a155675e9",
+            "description": "Contains data for FDA peanut product recalls since January 2009.",
+            "title": "FDA Peanut Product Recalls Widget",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225439.htm",
+                    "mediaType": "application/vnd.ms-excel"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2017-12-04",
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
+            "identifier": "https://data.cdc.gov/api/views/dxpw-cm5u",
+            "description": "2017, 2016. Data were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. 500 cities project city-level data in GIS-friendly format can be joined with city spatial data (https://chronicdata.cdc.gov/500-Cities/500-Cities-City-Boundaries/n44h-hy2j) in a geographic information system (GIS) to produce maps of 27 measures at the city-level. There are 7 measures (all teeth lost, dental visits, mammograms, Pap tests, colorectal cancer screening, core preventive services among older adults, and sleep less than 7 hours) in this 2019 release from the 2016 BRFSS that were the same as the 2018 release.",
+            "title": "500 Cities: City-level Data (GIS Friendly Format), 2019 release",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dxpw-cm5u/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dxpw-cm5u/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dxpw-cm5u/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dxpw-cm5u/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/500-Cities/500-Cities-City-level-Data-GIS-Friendly-Format-201/dxpw-cm5u",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "500 Cities & Places"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/c7xe-en73",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2014-11-07",
+            "temporal": "2016-01-01T00:00:00+00:00/2017-01-01T00:00:00+00:00",
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
+            "identifier": "7656fc17-f1b4-566b-9a2d-c4a4f2ac7ae1",
+            "description": "National Average Drug Acquisition Cost (NADAC) weekly reference data for the calendar year.",
+            "title": "NADAC (National Average Drug Acquisition Cost) 2016",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/nadac-national-average-drug-acquisition-cost.a4y5-998d.7656fc17-f1b4-566b-9a2d-c4a4f2ac7ae1.csv",
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
+            "landingPage": "https://www.cdc.gov/nchs/covid19/rands/telemedicine.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2020-09-14",
+            "@type": "dcat:Dataset",
+            "temporal": "2020-06-09/2021-06-30",
+            "modified": "2023-04-24",
+            "keyword": [
+                "covid-19",
+                "rands"
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
+            "identifier": "https://data.cdc.gov/api/views/8xy9-ubqz",
+            "description": "The Research and Development Survey (RANDS) is a platform designed for conducting survey question evaluation and statistical research. RANDS is an ongoing series of surveys from probability-sampled commercial survey panels used for methodological research at the National Center for Health Statistics (NCHS). RANDS estimates are generated using an experimental approach that differs from the survey design approaches generally used by NCHS, including possible biases from different response patterns and sampling frames as well as increased variability from lower sample sizes. Use of the RANDS platform allows NCHS to produce more timely data than would be possible using traditional data collection methods. RANDS is not designed to replace NCHS\u2019 higher quality, core data collections. Below are experimental estimates of telemedicine access and use for three rounds of RANDS during COVID-19. Data collection for the three rounds of RANDS during COVID-19 occurred between June 9, 2020 and July 6, 2020, August 3, 2020 and August 20, 2020, and May 17, 2021 and June 30, 2021. Information needed to interpret these estimates can be found in the Technical Notes. RANDS during COVID-19 included questions about whether providers offered telemedicine (including video and telephone appointments) in the last 2 months\u2014both during and before the pandemic\u2014and about the use of telemedicine in the last 2 months during the pandemic. As a result of the coronavirus pandemic, many local and state governments discouraged people from leaving their homes for nonessential reasons. Although health care is considered an essential activity, telemedicine offers an opportunity for care without the potential or perceived risks of leaving the home. The National Health Interview Survey, conducted by NCHS, added telemedicine questions to its sample adult questionnaire in July 2020.  The Household Pulse Survey (https://www.cdc.gov/nchs/covid19/pulse/telemedicine-use.htm), an online survey conducted in response to the COVID-19 pandemic by the Census Bureau in partnership with other federal agencies including NCHS, also reports estimates of telemedicine use during the pandemic (beginning in Phase 3.1, which started on April 14, 2021). The Household Pulse Survey reports telemedicine use in the last 4 weeks among adults and among households with at least one child under age 18 years. The experimental estimates on this page are derived from RANDS during COVID-19 and show the percentage of U.S. adults who have a usual place of care and a provider that offered telemedicine in the past 2 months, who used telemedicine in the past 2 months, or who have a usual place of care and a provider that offered telemedicine prior to the coronavirus pandemic. Technical Notes: https://www.cdc.gov/nchs/covid19/rands/telemedicine.htm#limitations",
+            "title": "Access and Use of Telemedicine During COVID-19",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8xy9-ubqz/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8xy9-ubqz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8xy9-ubqz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8xy9-ubqz/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/c8di-4x22",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-03-28",
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
+            "identifier": "3f3dd079-167e-58ac-ac1b-dbbed02ae596",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "Scorecard state v2.11.16 (dev)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.16/20241107/state.csv",
+                    "description": "Scorecard state v2.11.16 (dev)",
+                    "@type": "dcat:Distribution",
+                    "title": "Scorecard state v2.11.16 (dev)"
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
+            "landingPage": "https://chpl.healthit.gov/#/resources/chpl_api",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-10-03",
+            "@type": "dcat:Dataset",
+            "modified": "2023-10-03",
+            "references": [
+                "https://chpl.healthit.gov/"
+            ],
+            "keyword": [
+                "na"
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
+            "identifier": "hl1o4xum-glh3-5j9f-ral7-kkm8hprfl53q",
+            "description": "The Certified Health IT Product List (CHPL) is a comprehensive and authoritative listing of all certified Health Information Technology which has been successfully tested and certified by the ONC Health IT Certification program. All products listed on the CHPL have been tested by an ONC-Accredited Testing Laboratory (ONC-ATL) and certified by an ONC-Authorized Certification Body (ONC-ACB) to meet criteria adopted by the Secretary of the Department of Health and Human Services (HHS). This is a fully queryable REST API with JSON and XML output.",
+            "title": "Certified Health IT Product List (CHPL) Open API",
+            "programCode": [
+                "009:110"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://chpl.healthit.gov/#/resources/chpl_api",
+                    "mediaType": "text/html",
+                    "title": "CHPL Open API"
+                }
+            ],
+            "describedBy": "https://chpl.healthit.gov/#/resources/chpl_api"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/xsu4-4sk9",
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
+            "identifier": "https://data.cdc.gov/api/views/xsu4-4sk9",
+            "description": "Rate of deaths by age/gender (per 100,000 population) for motor vehicle occupants killed in crashes, 2012 & 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Safety Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
+            "title": "Motor Vehicle Occupant Death Rate, by Age and Gender, 2012 & 2014,  Region 9 - San Francisco",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xsu4-4sk9/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xsu4-4sk9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xsu4-4sk9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xsu4-4sk9/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-04-28",
+            "temporal": "1988/2019",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-29",
+            "keyword": [
+                "adult",
+                "african americans",
+                "age",
+                "asian continental ancestry group",
+                "chronic conditions",
+                "continental population groups",
+                "european continental ancestry group",
+                "health risk factors",
+                "health us",
+                "hispanic americans",
+                "obesity",
+                "overweight",
+                "poverty",
+                "sex"
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
+            "identifier": "https://data.cdc.gov/api/views/3nzu-udr9",
+            "description": "Data on normal weight, overweight, and obesity among adults aged 20 and over by selected population characteristics. Please refer to the PDF or Excel version of this table in the HUS 2019 Data Finder (https://www.cdc.gov/nchs/hus/contents2019.htm) for critical information about measures, definitions, and changes over time. \n\nSOURCE: NCHS, National Health and Nutrition Examination Survey. For more information on the National Health and Nutrition Examination Survey, see the corresponding Appendix entry at https://www.cdc.gov/nchs/data/hus/hus19-appendix-508.pdf.",
+            "title": "Normal weight, overweight, and obesity among adults aged 20 and over, by selected characteristics: United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3nzu-udr9/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3nzu-udr9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3nzu-udr9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3nzu-udr9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-births-0",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2012-08-03",
+            "temporal": "1995-01-01T00:00:00-05:00/2009-12-31T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "natality births population health state county infant race hispanic age sex year birth weight gestat",
+                "population statistics"
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
+            "identifier": "fb7cc429-69d2-4424-b287-68855af600ff",
+            "description": "<p>The Births (Natality) online databases in CDC WONDER report birth rates, fertility rates and counts of live births occurring within the United States to U.S. residents and non-residents. Counts can be obtained by state, county, child's gender and weight, mother's race, mother's age, mother's education, gestation period, prenatal care, birth plurality, and mother's medical and tobacco use risk factors. The data are derived from birth certificates. Data are available since 1995. The data are produced by the National Center for Health Statistics.</p>",
+            "title": "CDC WONDER: Births",
+            "programCode": [
+                "009:015"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://wonder.cdc.gov/natality.html",
+                    "mediaType": "text/html",
+                    "title": "Text "
+                }
+            ],
+            "describedBy": "http://wonder.cdc.gov/wonder/help/natality.html",
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "Health",
+                "State"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/c9tb-dwqg",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-04-08",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-13",
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
+            "identifier": "e9c931e7-55b5-570c-bdee-aa0b5fe87e1f",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "Scorecard filters v2.11.18 (etl-test)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.18/20241107/filters.csv",
+                    "description": "Scorecard filters v2.11.18 (etl-test)",
+                    "@type": "dcat:Distribution",
+                    "title": "Scorecard filters v2.11.18 (etl-test)"
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
+            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-02-26",
+            "temporal": "2005/2018",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-08",
+            "keyword": [
+                "accidental falls",
+                "accidents",
+                "children and adolescents",
+                "emergency department visits",
+                "health care use",
+                "health us",
+                "injury",
+                "men",
+                "older persons",
+                "traffic",
+                "women",
+                "wounds and injuries"
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
+            "identifier": "https://data.cdc.gov/api/views/qdzf-zqgy",
+            "description": "Data on initial injury-related visits to hospital emergency departments in the United States, by sex, age, and intent and mechanism of injury. Data are from Health, United States. SOURCE: National Center for Health Statistics, National Hospital Ambulatory Medical Care Survey.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
+            "title": "DQS Initial injury-related visits to hospital emergency departments, by sex, age, and intent and mechanism of injury: United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qdzf-zqgy/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qdzf-zqgy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qdzf-zqgy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qdzf-zqgy/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/vxsn-2csw",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2018-01-04",
+            "@type": "dcat:Dataset",
+            "modified": "2018-01-04",
+            "keyword": [
+                "2017",
+                "hepatitis",
+                "hepatitis (viral acute)",
+                "hepatitis (viral acute) type a",
+                "hepatitis (viral acute) type b",
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
+            "identifier": "https://data.cdc.gov/api/views/vxsn-2csw",
+            "description": "NNDSS - Table II. Hepatitis (viral, acute) A & B - 2017.  In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n*Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u2020 Case counts for reporting year 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.",
+            "title": "NNDSS - Table II. Hepatitis (viral, acute) A & B",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vxsn-2csw/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vxsn-2csw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vxsn-2csw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vxsn-2csw/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-09-04",
+            "temporal": "1999/2022",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-15",
+            "keyword": [
+                "american indian or alaska native",
+                "asian",
+                "black or african american",
+                "cancer",
+                "death rates",
+                "health us",
+                "hispanic or latino",
+                "men",
+                "mortality",
+                "native hawaiian or other pacific islander",
+                "neoplasms",
+                "white",
+                "women"
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
+            "identifier": "https://data.cdc.gov/api/views/4giy-47wy",
+            "description": "Data on death rates for neoplasms in the United States, by age, sex, race, and Hispanic origin. Data are from Health, United States. SOURCE: National Center for Health Statistics, National Vital Statistics System, Mortality File.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
+            "title": "DQS Death rates for malignant neoplasms, by sex, race, Hispanic origin, and age: United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4giy-47wy/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4giy-47wy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4giy-47wy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4giy-47wy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Annual",
+            "theme": [
+                "National Center for Health Statistics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/9yc3-yir3",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2018-01-04",
+            "@type": "dcat:Dataset",
+            "modified": "2018-01-04",
+            "keyword": [
+                "2017",
+                "age <5",
+                "invasive pneumococcal diseases",
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
+            "identifier": "https://data.cdc.gov/api/views/9yc3-yir3",
+            "description": "NNDSS - Table II. Invasive Pneumococcal Diseases, Age <5 - 2017. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\n U: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n*Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u2020 Case counts for reporting years 2016 and 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.\r\n\r\n\u00a7 Includes drug resistant and susceptible cases of Invasive Pneumococcal Disease. This condition was previously named Streptococcus pneumoniae invasive disease and cases were reported to CDC using different event codes to specify whether the cases were drug resistant or in a defined age group, such as <5 years.",
+            "title": "NNDSS - Table II. Invasive Pneumococcal Diseases, Age <5",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9yc3-yir3/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9yc3-yir3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9yc3-yir3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9yc3-yir3/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.acf.hhs.gov/ofa/data/tanf-final-rule-pages-17769-17818",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2013-06-18",
+            "temporal": "1996-01-01T00:00:00-05:00/2010-12-31T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-29",
+            "keyword": [
+                "children's health",
+                "temporary assistance to needy families  cash assistance  welfare policy"
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
+            "identifier": "20287f1e-d621-41ee-928f-284caeb0b786",
+            "description": "<p>Single source providing information on Temporary Assistance for Needy Families (TANF) program rules among States and across years (currently 1996-2010), including longitudinal tables with state TANF polices for selected years.</p>",
+            "title": "TANF Rules Data Base",
+            "programCode": [
+                "009:102"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.acf.hhs.gov/ofa/data/tanf-final-rule-pages-17769-17818",
+                    "description": "[Federal Register: April 12, 1999 (Volume 64, Number 69)]\n[Rules and Regulations]\n[Page 17769-17818]\nFrom the Federal Register Online via GPO Access [wais.access.gpo.gov]\n[DOCID:fr12ap99-24]\n\n[[pp. 17769-17818]] Temporary Assistance for Needy Families Program (TANF)\n",
+                    "@type": "dcat:Distribution",
+                    "title": "TANF Final Rule \u2013 Pages 17769 - 17818"
+                }
+            ],
+            "dataQuality": false,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/gxj9-t96f",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-11-17",
+            "@type": "dcat:Dataset",
+            "temporal": "2020-12-13/2022-08-10",
+            "modified": "2022-10-20",
+            "references": [
+                "https://www.cdc.gov/coronavirus/2019-ncov/vaccines/distributing/about-vaccine-data.html"
+            ],
+            "keyword": [
+                "administration",
+                "cases",
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
+            "identifier": "https://data.cdc.gov/api/views/gxj9-t96f",
+            "description": "</p><p style=\"margin:0in;vertical-align:baseline;\"><strong><em><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>After October 13, 2022, this dataset will no longer be updated as the related CDC COVID Data Tracker site was retired on October 13, 2022.</span></em></strong><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>&nbsp;</span></p>This dataset contains historical trends in vaccinations and cases by age group, at the US national level. Data is stratified by at least one dose and fully vaccinated. Data also represents all vaccine partners including jurisdictional partner clinics, retail pharmacies, long-term care facilities, dialysis centers, Federal Emergency Management Agency and Health Resources and Services Administration partner sites, and federal entity facilities.",
+            "title": "Archive: COVID-19 Vaccination and Case Trends by Age Group, United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gxj9-t96f/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gxj9-t96f/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gxj9-t96f/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gxj9-t96f/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "US",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Archived",
+            "theme": [
+                "Vaccinations"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/cdnr-9f3u",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-05-02",
+            "@type": "dcat:Dataset",
+            "modified": "2023-05-01",
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
+            "identifier": "e56d9a47-fe57-42c0-b37d-4ab244fd08b1",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-04-24-to-2023-04-30",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rprt-drug-4-24-2023-to-4-30-2023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-04-24-to-2023-04-30"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/cefh-9ep2",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-02-09",
+            "@type": "dcat:Dataset",
+            "modified": "2023-02-07",
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
+            "identifier": "cfbf62b6-ab10-46d1-9284-b08475964470",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-01-23-to-2023-01-29",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rprt-drug-01232023-to-01292023_0.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-01-23-to-2023-01-29"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "restricted public",
+            "landingPage": "https://data.cdc.gov/d/66km-38zv",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "issued": "2022-06-08",
+            "@type": "dcat:Dataset",
+            "temporal": "2021",
+            "modified": "2023-04-24",
+            "keyword": [
+                "anxiety",
+                "covid-19",
+                "depression",
+                "life satisfaction",
+                "missed healthcare",
+                "research-data-center",
+                "telemedicine",
+                "vaccination"
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
+            "identifier": "https://data.cdc.gov/api/views/66km-38zv",
+            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys from probability-sampled commercial survey panels. As part of a special iteration of RANDS that focuses on COVID-19, RANDS during COVID-19 Round 3 is the third round of a three-round survey. The sampled participants of RANDS during COVID-19 Round 3 were recruited using NORC at the University of Chicago (NORC)\u2019s AmeriSpeak Panel, and the survey was administered by NORC from May 17, 2021 to June 30, 2021. RANDS during COVID-19 Round 3 has a known survey sampling design and can be used to produce nationally and sub-nationally representative estimates.",
+            "title": "NCHS Research and Development Survey (RANDS) Round 3 during COVID-19 Restricted File",
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
+            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS_COVID_3_technical_documentation.pdf",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/cgyd-rri7",
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
+            "identifier": "e7d5089e-647c-4aa7-8c7b-f98dd8ea3852",
+            "description": "This data set includes monthly enrollment counts of Medicaid and CHIP beneficiaries by benefit package (full-scope, comprehensive, limited, or unknown). \r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating these measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable or of high concern based on DQ Atlas thresholds for the topic Restricted Benefits Code. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+            "title": "Benefit Package for Medicaid and CHIP Beneficiaries by Month",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/BenefitPackage-montly.csv",
+                    "description": "This data set includes monthly enrollment counts of Medicaid and CHIP beneficiaries by benefit package (full-scope, comprehensive, limited, or unknown). \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating these measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable or of high concern based on DQ Atlas thresholds for the topic Restricted Benefits Code. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "@type": "dcat:Distribution",
+                    "title": "Benefit Package for Medicaid and CHIP Beneficiaries by Month"
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
+            "landingPage": "https://data.cdc.gov/d/hv7b-3sw8",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-06-22",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-02",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Surveillance and Epidemiology Branch, Immunization Services Division, NCIRD, CDC",
+                "hasEmail": "mailto:VaxView@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/hv7b-3sw8",
+            "description": "Estimates are for pregnant persons who are up-to-date with COVID-19 vaccines, overall and by race and ethnicity based on data from the Vaccine Safety Datalink*.",
+            "title": "Data: COVID-19 vaccination among pregnant people aged 18-49 years overall, by race and ethnicity, and date reported to CDC - Vaccine Safety Datalink,* United States",
+            "programCode": [
+                "009:026"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hv7b-3sw8/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hv7b-3sw8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hv7b-3sw8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hv7b-3sw8/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.nlm.nih.gov/hmd/indexcat/index.html",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2016-08-04",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-05",
+            "keyword": [
+                "dataset",
+                "history of medicine",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/axmu-a5jw",
+            "description": "IndexCat provides access to the digitized version of the printed Index-Catalogue of the Library of the Surgeon General's Office; eTK for medieval Latin texts; and eVK2 for medieval English texts; along with links to other selected NLM resources.",
+            "title": "IndexCat",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.nlm.nih.gov/hmd/indexcat/index.html",
+                    "mediaType": "text/html",
+                    "title": "IndexCat Homepage and Search"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.nlm.nih.gov/hmd/indexcat/indexcatxml.html",
+                    "mediaType": "text/html",
+                    "title": "Download IndexCat Data"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Images"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/95m5-agj4",
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
+                "fn": "Active Bacterial Core surveillance",
+                "hasEmail": "mailto:abcs@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/95m5-agj4",
+            "description": "ABCs is an ongoing surveillance program that began in 1997. <a href=\"https://www.cdc.gov/abcs/reports-findings/surv-reports.html\">ABCs reports</a> describe the ABCs case definition and the specific methodology used to calculate rates and estimated numbers in the United States for each bacterium by year.  The methods, <a href=\"https://www.cdc.gov/abcs/methodology/surv-pop.html\">surveillance areas</a>, and <a href=\"https://www.cdc.gov/abcs/methodology/surv-pop.html\">laboratory isolate collection areas</a> have changed over time.\n                Additionally, the way missing data are taken into account changed in 2010.  It went from distributing unknown values based on known values of cases by site to use of multiple imputation using a sequential regression imputation method.\n                Given these changes over time, trends should be interpreted with caution.\n<ul><li> <a href=\"http://www.cdc.gov/abcs/methodology/index.html\">Methodology</a>\nFind details about surveillance population, case determination, surveillance evaluation, and more. </li> <li><a href=\"http://www.cdc.gov/abcs/reports-findings/index.html\">Reports and Findings</a>\nGet official interpretations from reports and publications created from ABCs data.\n </li>                </ul>",
+            "title": "Active Bacterial Core surveillance (ABCs) Group B Streptococcus",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/95m5-agj4/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/95m5-agj4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/95m5-agj4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/95m5-agj4/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/vaccines/vaxview/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-02-09",
+            "@type": "dcat:Dataset",
+            "temporal": "2023-2024",
+            "modified": "2024-08-05",
+            "keyword": [
+                "covid-19 vaccination",
+                "iis",
+                "immunization information system"
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
+            "identifier": "https://data.cdc.gov/api/views/vugp-mqip",
+            "description": "Monthly Cumulative Percent of Persons Who Received 1+ updated 2023-24 COVID-19 Vaccination Doses by Age Group and Jurisdiction\n\n\u2022 Estimated Number of COVID-19 vaccinations among children 6 months\u201317 years and adults is assessed through U.S. jurisdictions\u2019 Immunization Information Systems (IIS) data, submitted from jurisdictions to CDC monthly in aggregate by age group.\n\n \u2022 Starting in September 2023, the CDC recommended the 2023-2024 updated COVID-19 vaccine to protect against serious illness from COVID-19. (https://www.cdc.gov/coronavirus/2019-ncov/vaccines/stay-up-to-date.html)\n\u2003",
+            "title": "Monthly Cumulative Number and Percent of Persons Who Received 1+ updated 2023-24 COVID-19 Vaccination Doses by Age Group and Jurisdiction, United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vugp-mqip/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vugp-mqip/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vugp-mqip/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vugp-mqip/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "Jurisdictions - States, District of Columbia, Islands, and US cities",
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
+            "landingPage": "http://www.fda.gov/ICECI/EnforcementActions/WarningLetters/2013/default.htm",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "ora",
+                "regulations"
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
+            "identifier": "8ab03039-617f-469d-bf37-b4f844372945",
+            "description": "An index of FDA warning letters issued to companies operating in the United States.",
+            "title": "Warning Letters",
+            "programCode": [
+                "009:008"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fda.gov/DataSets/WarningLetters/WarningLettersDataSet.xml",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P1W"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/respiratory-viruses/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-10-02",
+            "@type": "dcat:Dataset",
+            "temporal": "2023-24 & 2024-25",
+            "modified": "2025-01-29",
+            "keyword": [
+                "covid-19 vaccination",
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
+            "identifier": "https://data.cdc.gov/api/views/pvk6-8bzd",
+            "description": "\u2022 Weekly COVID-19 Vaccination Coverage, Pregnant Women 18-49 Years Old by Race and Ethnicity \n\n\u2022 Weekly COVID-19 vaccination coverage estimates for pregnant women ages 18\u201349 years are based on electronic health record (EHR) data from the Vaccine Safety Datalink (VSD) ((https://www.cdc.gov/vaccine-safety-systems/vsd/), a collaboration between CDC\u2019s Immunization Safety Office and multiple integrated health care organizations.",
+            "title": "Weekly COVID-19 Vaccination Coverage Among Pregnant Women 18-49 Years, by Race and Ethnicity",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pvk6-8bzd/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pvk6-8bzd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pvk6-8bzd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pvk6-8bzd/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/covidvaxview/weekly-dashboard/child-coverage-vaccination.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2025-01-29",
+            "@type": "dcat:Dataset",
+            "temporal": "2023-2024 & 2024-2025",
+            "modified": "2025-01-29",
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
+            "identifier": "https://data.cdc.gov/api/views/ker6-gs6z",
+            "description": "\u2022 Weekly Parental Intent for Vaccination and Cumulative Percentage of Children 6 Months-17 Years Who are Up to date with the COVID-19 Vaccines by Season. \n\n\u2022 Weekly estimates of COVID-19 vaccination coverage and parental intent for vaccination among children through December 31, 2023, were calculated using data from the National Immunization Survey\u2013Child COVID Module (NIS\u2013CCM). The NIS\u2013CCM was discontinued at the end of 2023 and questions regarding COVID-19 vaccination status and intent were added to the National Immunization Survey\u2013Flu (NIS\u2013Flu) (https://www.cdc.gov/nis/about/index.html).",
+            "title": "Weekly Parental Intent for Vaccination and Cumulative Percentage of Children 6 Months -17 Years Who are Up to date with the COVID-19 Vaccines by Season, United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ker6-gs6z/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ker6-gs6z/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ker6-gs6z/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ker6-gs6z/rows.xml?accessType=DOWNLOAD",
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
+            "accessLevel": "restricted public",
+            "landingPage": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information. Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement. If approved, data access would occur at a NCHS or Federal Statistical Research Data Center. For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
+            "issued": "2022-12-22",
+            "@type": "dcat:Dataset",
+            "temporal": "2016/2020",
+            "modified": "2023-04-14",
+            "keyword": [
+                "births",
+                "county",
+                "date of birth",
+                "date of death",
+                "infant deaths",
+                "nhcs",
+                "research-data-center",
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
+            "identifier": "https://data.cdc.gov/api/views/wis9-vyx6",
+            "description": "This dataset includes all infant deaths that were linked to their corresponding birth certificate and includes all items released in the public-use file. Additional information in this file includes state and county of residence and exact dates of birth and death (which includes day of month, month, and year).",
+            "title": "NCHS - All-County Linked Births/Infant Deaths File with Exact Dates of Birth and Death",
+            "isPartOf": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "description": "This dataset includes all infant deaths that were linked to their corresponding birth certificate and includes all items released in the public-use file. Additional information in this file includes state and county of residence and exact dates of birth and death (which includes day of month, month, and year).",
+                    "@type": "dcat:Distribution",
+                    "title": "NCHS - All-County Linked Births/Infant Deaths File with Exact Dates of Birth and Death"
+                }
+            ],
+            "spatial": "50 states and District of Columbia, all counties with a population of 100,000 or greater",
+            "describedBy": "All registered infant deaths linked with corresponding birth certificates occurring to residents of the United States",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/cmfu-57yz",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-12-10",
+            "@type": "dcat:Dataset",
+            "modified": "2024-12-18",
+            "keyword": [
+                "individual",
+                "individual market dental",
+                "py2025",
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
+            "identifier": "fade0e37-50d8-418b-92a0-46828980a384",
+            "description": "The Dental Individual Market file of the QHP Landscape Files contains information on certified dental plans offered through an Exchange to consumers in the individual market. These plans are also known as Stand-alone Dental Plans (SADPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
+            "title": "QHP Landscape PY2025 Individual Dental",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2025/individual_market_dental.zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/kw6u-z8u2",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-03-23",
+            "@type": "dcat:Dataset",
+            "modified": "2022-09-25",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Mara Howard-Williams",
+                "hasEmail": "mailto:prw0@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/kw6u-z8u2",
+            "description": "This dataset contains all state and territorial vaccine mandates that were issued from July 26, 2021 to ____, regardless of whether the law has been superseded by a subsequent law, postponed by subsequent law, or otherwise modified. State and territorial laws are collected from publicly available government websites and cataloged and coded using HHS Protect by one coder with one or more additional coders conducting quality assurance. \nData were collected to determine when certain groups were subject to vaccine mandates. Data can be used to determine when states announced and required different groups to be vaccinated. \nThese data are derived from publicly available state and territorial laws and official policy documents found by CDC\u2019s COVID-19 Mitigation Policy Analysis Unit, and CDC\u2019s Center for State, Tribal, Local, and Territorial Support, Public Health Law Program from July 26, 2021 through _____. These data will be updated as new laws are collected. Any orders not available through publicly accessible websites are not included in this dataset. Recommendations not included in a law are not included in these data. Effective and expiration dates were coded using only the date provided in the law. These data do not necessarily represent the official position of the Centers for Disease Control and Prevention.",
+            "title": "State-Level Vaccine Mandates - All",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kw6u-z8u2/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kw6u-z8u2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kw6u-z8u2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kw6u-z8u2/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "http://ephtracking.cdc.gov/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2015-08-13",
+            "@type": "dcat:Dataset",
+            "modified": "2018-06-05",
+            "keyword": [
+                "air pollution",
+                "air quality",
+                "air quality index",
+                "air quality system",
+                "caa 109: clean air act section 109",
+                "daily 24 hour average concentration",
+                "daily maximum 8 hour average concentration",
+                "environmental hazard",
+                "environmental health",
+                "hourly observations",
+                "national ambient air quality standards",
+                "national environmental health tracking network",
+                "o3",
+                "oxygen",
+                "ozone",
+                "ozone residual",
+                "ozone - residual",
+                "particle pollution",
+                "particulate matter",
+                "particulate matter < 2.5 um",
+                "particulate matter - pm2.5",
+                "pm2.5",
+                "pm2.5 - local conditions",
+                "pm fine 0-2.5 um stp",
+                "regulatory resources",
+                "site monitoring data",
+                "tracking",
+                "tracking network",
+                "tracking program"
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
+            "identifier": "https://data.cdc.gov/api/views/cjae-szjv",
+            "description": "The Environmental Protection Agency (EPA) provides air pollution data about ozone and particulate matter (PM2.5) to CDC for the Tracking Network. The EPA maintains a database called the Air Quality System (AQS) which contains data from approximately 4,000 monitoring stations around the country, mainly in urban areas. Data from the AQS is considered the \"gold standard\" for determining outdoor air pollution. However, AQS data are limited because the monitoring stations are usually in urban areas or cities and because they only take air samples for some air pollutants every three days or during times of the year when air pollution is very high. CDC and EPA have worked together to develop a statistical model (Downscaler) to make modeled predictions available for environmental public health tracking purposes in areas of the country that do not have monitors and to fill in the time gaps when monitors may not be recording data. This data does not include \"Percent of population in counties exceeding NAAQS (vs. population in counties that either meet the standard or do not monitor PM2.5)\". Please visit the Tracking homepage for this information.View additional information for indicator definitions and documentation by selecting Content Area \"Air Quality\" and the respective indicator at the following website: http://ephtracking.cdc.gov/showIndicatorsData.action",
+            "title": "Air Quality Measures on the National Environmental Health Tracking Network",
+            "programCode": [
+                "009:032"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cjae-szjv/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cjae-szjv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cjae-szjv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cjae-szjv/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "irregular",
+            "theme": [
+                "Environmental Health & Toxicology"
+            ],
+            "language": [
+                "English"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/cqip-xq88",
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
+            "identifier": "ce40c2ae-06e3-593f-b055-41d39df5edcb",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "Scorecard state v2.11.9 (prod)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.9/20241107/state.csv",
+                    "description": "Scorecard state v2.11.9 (prod)",
+                    "@type": "dcat:Distribution",
+                    "title": "Scorecard state v2.11.9 (prod)"
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
+            "landingPage": "https://www.hcup-us.ahrq.gov",
+            "bureauCode": [
+                "009:33"
+            ],
+            "issued": "2022-06-07",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "references": [
+                "https://www.hcup-us.ahrq.gov/reports/trendtables/HCUPSummaryTrendTables_Methods.xlsx"
+            ],
+            "keyword": [
+                "agency-for-healthcare-research-and-quality-department-of-health-human-services",
+                "hcup",
+                "healthcare cost and utilization"
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
+            "identifier": "https://healthdata.gov/api/views/cqqt-nv72",
+            "description": "The HCUP Summary Trend Tables include monthly information on hospital utilization derived from the HCUP State Inpatient Databases (SID) and HCUP State Emergency Department Databases (SEDD). Information on emergency department (ED) utilization is dependent on availability of HCUP data; not all HCUP Partners participate in the SEDD.\n\nThe HCUP Summary Trend Tables include downloadable Microsoft\u00ae Excel tables with information on the following topics:\n\n<li>Overview of monthly trends in inpatient and emergency department utilization\n<li>All inpatient encounter types\n<li>Inpatient stays by priority conditions\n-COVID-19\n-Influenza\n-Other acute or viral respiratory infection\n<li>Inpatient encounter type\n-Normal newborns\n-Deliveries\n-Non-elective inpatient stays, admitted through the ED\n-Non-elective inpatient stays, not admitted through the ED\n-Elective inpatient stays\n<li>Inpatient service line\n-Maternal and neonatal conditions\n-Mental health and substance use disorders\n-Injuries\n-Surgeries\n-Other medical conditions\n<li>Emergency department treat-and-release visits\n<li>Emergency department treat-and-release visits by priority conditions\n-COVID-19\n-Influenza\n-Other acute or viral respiratory infection\n<li>Description of the data source, methodology, and clinical criteria",
+            "title": "Healthcare Cost and Utilization Project (HCUP) Summary Trends Tables",
+            "programCode": [
+                "009:074"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.hcup-us.ahrq.gov/reports/trendtables/summarytrendtables.jsp",
+                    "mediaType": "text/html",
+                    "title": "Healthcare Cost and Utilization Project (HCUP) Summary Trends Tables"
+                }
+            ],
+            "describedBy": "https://www.hcup-us.ahrq.gov/reports/trendtables/summarytrendtables.jsp"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-06-15",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-25",
+            "references": [
+                "https://www.cdc.gov/places/measure-definitions/index.html"
+            ],
+            "keyword": [
+                "behaviors",
+                "county",
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
+            "identifier": "https://data.cdc.gov/api/views/xyst-f73f",
+            "description": "This dataset contains model-based county-level estimates for the PLACES 2022 release in GIS-friendly format. PLACES covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. Project was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2020 or 2019 data, Census Bureau 2020 or 2019 county population estimates, and American Community Survey (ACS) 2016\u20132020 or 2015\u20132019 estimates. The 2022 release uses 2020 BRFSS data for 25 measures and 2019 BRFSS data for 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, and cholesterol screening) that the survey collects data on every other year. These data can be joined with the census 2020 county boundary file in a GIS system to produce maps for 29 measures at the county level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software. https://cdcarcgis.maps.arcgis.com/home/item.html?id=3b7221d4e47740cab9235b839fa55cd7",
+            "title": "PLACES: County Data (GIS Friendly Format), 2022 release",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xyst-f73f/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xyst-f73f/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xyst-f73f/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xyst-f73f/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/ygrm-jkkz",
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
+                "q fever",
+                "q fever acute",
+                "q fever chronic",
+                "total",
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
+            "identifier": "https://data.cdc.gov/api/views/ygrm-jkkz",
+            "description": "NNDSS - TABLE 1BB. Q fever, Total to Q fever, Chronic - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1BB. Q fever, Total to Q fever, Chronic",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ygrm-jkkz/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ygrm-jkkz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ygrm-jkkz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ygrm-jkkz/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/hospice-all-owners",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-04-20",
+            "temporal": "2023-04-01/2025-03-31",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-15",
+            "references": [
+                "https://data.cms.gov/sites/default/files/2023-03/f193e9ef-9fd7-4de3-9a27-0d5281cf80a9/Hospice_Data_Guidance.pdf"
+            ],
+            "keyword": [
+                "hospice",
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/e983965e-1603-4cb8-82b5-c40090e380d1/data-viewer",
+            "description": "The \u00a0Hospice All Owners dataset provides ownership information on all hospices currently enrolled in Medicare. This data includes ownership information such as ownership name, ownership type, ownership address and ownership effective date.",
+            "title": "Hospice All Owners",
+            "describedByType": "application/pdf",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e983965e-1603-4cb8-82b5-c40090e380d1/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Hospice All Owners : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/662c8886-9074-4669-bbfb-3807ba85b484/Hospice_All_Owners_2025.01.02.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospice All Owners : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/31bebe15-6de5-496c-af31-65da426d03d2/data",
+                    "mediaType": "text/html",
+                    "title": "Hospice All Owners : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/135426ab-453d-424e-bba8-c89cd53d947f/Hospice_All_Owners_2024.10.07.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospice All Owners : 2024-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/0d8d3a8b-21c0-4967-8df0-ad4032ad3d3d/data",
+                    "mediaType": "text/html",
+                    "title": "Hospice All Owners : 2024-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/354ce286-5164-4722-8a43-6b8e90df3684/Hospice_All_Owners_2024.07.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospice All Owners : 2024-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f5f4be6a-49fb-43e4-bb02-b260f1011985/data",
+                    "mediaType": "text/html",
+                    "title": "Hospice All Owners : 2024-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/06f1815a-c792-4888-90e0-141539f3f59b/Hospice_All_Owners_2024.04.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospice All Owners : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5d27cc83-31fc-41ba-a97c-c0302e93081e/data",
+                    "mediaType": "text/html",
+                    "title": "Hospice All Owners : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/78185aa4-ca7b-4746-9340-88631bc75341/Hospice_All_Owners_2024.01.05.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospice All Owners : 2024-01-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a53bdaf9-7650-4ec4-ad43-1cf9676afffb/data",
+                    "mediaType": "text/html",
+                    "title": "Hospice All Owners : 2024-01-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/3902d572-c865-4ffe-a721-0c23782c0a5e/Hospice_All_Owners_2023.10.02.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospice All Owners : 2023-10-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/12e0cedf-6c91-4edc-bf85-85a249658f38/data",
+                    "mediaType": "text/html",
+                    "title": "Hospice All Owners : 2023-10-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/b37deb97-253b-4876-bd6c-22c9fe6ef0c3/Hospice_All_Owners_2023.07.06.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospice All Owners : 2023-07-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/0445304f-7d1d-47f3-a438-da084816a3ce/data",
+                    "mediaType": "text/html",
+                    "title": "Hospice All Owners : 2023-07-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/53590f19-716d-4cb9-8381-e8c755f32a2b/Hospice_All_Owners_2023.03.31.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospice All Owners : 2023-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f200545a-cd96-4806-91d6-6212b485e0f0/data",
+                    "mediaType": "text/html",
+                    "title": "Hospice All Owners : 2023-04-01"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-10/Hospice_All_Owners_Data_Dictionary.pdf",
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
+            "landingPage": "https://www.ncbi.nlm.nih.gov/projects/CCDS/CcdsBrowse.cgi",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-06-17",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-04",
+            "keyword": [
+                "dataset",
+                "genetics",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/nmdi-yqxg",
+            "description": "The Consensus CDS (CCDS) project is a collaborative effort to identify a core set of human and mouse protein coding regions that are consistently annotated and of high quality. The long term goal is to support convergence towards a standard set of gene annotations.",
+            "title": "Consensus CDS (CCDS)",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/projects/CCDS/CcdsBrowse.cgi",
+                    "mediaType": "text/html",
+                    "title": "Consensus CDS (CCDS) Homepage"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://ftp.ncbi.nih.gov/pub/CCDS",
+                    "mediaType": "text/html",
+                    "title": "Download CCDS Data"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Molecular biology/Genetics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/nq6q-szvs",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2014-04-01",
+            "@type": "dcat:Dataset",
+            "modified": "2017-10-25",
+            "keyword": [
+                "brain injury",
+                "head trauma",
+                "tbi",
+                "traumatic brain injury"
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
+            "identifier": "https://data.cdc.gov/api/views/nq6q-szvs",
+            "description": "Changes in the rates of TBI-related deaths vary depending on age.  For persons 44 years of age and younger, TBI-related deaths decreased between the periods of 2001-2002 and 2009-2010.  Rates for age groups 45-64 years of age remained stable for this same ten-year period.  For persons 65 years and older, rates of TBI-related deaths increased during this time period, from 41.2 to 45.2 deaths per 100,000.Go to http://www.cdc.gov/traumaticbraininjury/data/index.html to view more TBI data & statistics.Source: http://www.cdc.gov/traumaticbraininjury/data/rates_deaths_byage.html",
+            "title": "Rates of TBI-related Deaths by Age Group - United States, 2001 - 2010",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/nq6q-szvs/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/nq6q-szvs/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/nq6q-szvs/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/nq6q-szvs/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Traumatic Brain Injury"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/cssi-nbpn",
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
+            "identifier": "6f27ead3-bc9e-529a-a2b1-2cf5efea881e",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "Scorecard pillar v2.12.1-test (local)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.12.1-test/20241030/pillar.csv",
+                    "description": "Scorecard pillar v2.12.1-test (local)",
+                    "@type": "dcat:Distribution",
+                    "title": "Scorecard pillar v2.12.1-test (local)"
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
+            "landingPage": "https://www.findhivcare.hrsa.gov/",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2012-05-30",
+            "temporal": "2010-01-01T00:00:00-05:00/2010-01-01T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "references": [
+                "https://hab.hrsa.gov/stateprofiles/State-Overview.aspx"
+            ],
+            "keyword": [
+                "health care providers",
+                "health center",
+                "hiv aids",
+                "locator",
+                "low income",
+                "map",
+                "medical",
+                "ryan white",
+                "service",
+                "treatment"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "HRSA Data Warehouse",
+                "hasEmail": "mailto:datawarehouse@hrsa.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Health Resources and Services Administration, Department of Health & Human Services"
+            },
+            "identifier": "d5636ec5-83f1-40fc-bd15-973fdc17359b",
+            "description": "<p>The Find Ryan White HIV/AIDS Medical Care Providers tool is a locator that helps people living with HIV/AIDS access medical care and related services. Users can search for Ryan White-funded medical care providers near a specific complete address, city and state, state and county, or ZIP code.</p>\n<p>Search results are sorted by distance away and include the Ryan White HIV/AIDS facility name, address, approximate distance from the search point, telephone number, website address, and a link for driving directions.</p>\n<p>HRSA's Ryan White program funds an array of grants at the state and local levels in areas where most needed. These grants provide medical and support services to more than a half million people who otherwise would be unable to afford care.</p>",
+            "title": "Find Ryan White HIV/AIDS Medical Care Providers",
+            "programCode": [
+                "009:016"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://findhivcare.hrsa.gov/Search_HAB.aspx",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/qz67-9a9h",
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
+                "non-congenital",
+                "wonder",
+                "yellow fever",
+                "zika virus disease"
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
+            "identifier": "https://data.cdc.gov/api/views/qz67-9a9h",
+            "description": "NNDSS - TABLE 1PP. Yellow fever to Zika virus disease, non-congenital - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1PP. Yellow fever to Zika virus disease, non-congenital",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qz67-9a9h/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qz67-9a9h/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qz67-9a9h/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qz67-9a9h/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.healthit.gov/data/datasets/electronic-prescribing-adoption-and-use-county",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-10-03",
+            "@type": "dcat:Dataset",
+            "modified": "2014-06-01",
+            "references": [
+                "https://www.healthit.gov/data/quickstats/physician-e-rx-through-ehr"
+            ],
+            "keyword": [
+                "county",
+                "doctors",
+                "ehr",
+                "electronic prescribing",
+                "e-prescribing",
+                "health information",
+                "health it",
+                "physicians"
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
+            "identifier": "y6vgv2n0-vxxe-pk39-wsqz-9l5plgpjljzr",
+            "description": "Electronic prescribing (eRx) is a key component of the meaningful use of health IT to improve health care quality and lower costs. This dataset includes county-level electronic prescribing (eRx) and health information exchange activity by community pharmacies and office-based health care providers active through the Surescripts Network. Surescripts is a health information network, and ONC procured electronic prescribing activity data conducted within its network from December 2008 through April 2014. The Surescripts network is used by the majority of all U.S. community pharmacies to rout prescriptions, excluding closed systems such as Kaiser Permanente. These include chain, franchise, and independently owned pharmacies. Data for annual percentages of new and renewal prescriptions routed through the Surescripts network exclude controlled substances. You may view more information about Surescripts, contact the company, and access more network data through the company's official site.",
+            "title": "Electronic Prescribing Adoption and Use by County",
+            "programCode": [
+                "009:110"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/Surescripts_County_04-2014.csv",
+                    "mediaType": "text/csv",
+                    "title": "Surescripts_County_04-2014.csv"
+                }
+            ],
+            "describedBy": "https://www.healthit.gov/data/datasets/electronic-prescribing-adoption-and-use-county"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/cxha-65ek",
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
+            "identifier": "b5cdefdb-4031-575a-8bb4-8607fabf6cb3",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "Scorecard TAG v0.2.4-1 (dev0)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/0.2.4-1/TAG.csv",
+                    "description": "Scorecard TAG v0.2.4-1 (dev0)",
+                    "@type": "dcat:Distribution",
+                    "title": "Scorecard TAG v0.2.4-1 (dev0)"
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
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/rysd-8s3y",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-09-14",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-05",
+            "keyword": [
+                "health services research",
+                "public health"
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/rysd-8s3y",
+            "description": "Health Services Research Projects in Progress (HSRProj) was a database of health services research and public health projects in progress, related to research in quality, cost, and access to health care. It included behavioral health research and public health research, with over 38,000 projects and information back to the 1990s.\n\nThis resource was retired on September 14, 2021 and is no longer updated.",
+            "title": "Health Services Research Projects in Progress (HSRProj)",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/rysd-8s3y/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/rysd-8s3y/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/rysd-8s3y/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/rysd-8s3y/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Research"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-09-15",
+            "temporal": "2015/2021",
+            "@type": "dcat:Dataset",
+            "modified": "2022-04-01",
+            "keyword": [
+                "age",
+                "age group",
+                "all causes",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "hhs region",
+                "hispanic origin",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
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
+            "identifier": "https://data.cdc.gov/api/views/xy7w-35q7",
+            "description": "Provisional deaths involving coronavirus disease 2019 (COVID-19) and deaths from all causes reported to NCHS by week the death occurred, HHS region of occurrence, race and Hispanic origin, and age group (0-24, 25-64, 65+ years), from 2015-2021.\n\nUnited States death counts include the 50 states, plus the District of Columbia and New York City. The ten (10) United States Department of Health and Human Services (HHS) regions include the following jurisdictions. Region 1: Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, Vermont; Region 2: New Jersey, New York, New York City; Region 3: Delaware, District of Columbia, Maryland, Pennsylvania, Virginia, West Virginia; Region 4: Alabama, Florida, Georgia, Kentucky, Mississippi, North Carolina, South Carolina, Tennessee; Region 5: Illinois, Indiana, Michigan, Minnesota, Ohio, Wisconsin; Region 6: Arkansas, Louisiana, New Mexico, Oklahoma, Texas; Region 7: Iowa, Kansas, Missouri, Nebraska; Region 8: Colorado, Montana, North Dakota, South Dakota, Utah, Wyoming; Region 9: Arizona, California, Hawaii, Nevada; Region 10: Alaska, Idaho, Oregon, Washington.",
+            "title": "AH Provisional COVID-19 Deaths by HHS Region, Race, and Age, 2015-2021",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xy7w-35q7/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xy7w-35q7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xy7w-35q7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xy7w-35q7/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/udsf-9v7b",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-07-06",
+            "@type": "dcat:Dataset",
+            "modified": "2024-01-24",
+            "keyword": [
+                "covid19",
+                "covid-19 vaccination",
+                "immunization",
+                "nis-acm",
+                "vaccination",
+                "vaccination coverage",
+                "vaccine confidence",
+                "vaxviews"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "James Singleton",
+                "hasEmail": "mailto:VaxView@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/udsf-9v7b",
+            "description": "National Immunization Survey Adult COVID Module (NIS-ACM): CDC is providing information on COVID-19 vaccine confidence to supplement vaccine administration data. These data represent trends in vaccination status and intent, and other behavioral indicators, by demographics and other characteristics.",
+            "title": "National Immunization Survey Adult COVID Module (NIS-ACM): COVIDVaxViews| Data | Centers for Disease Control and Prevention (cdc.gov)-Archived",
+            "programCode": [
+                "009:026"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/udsf-9v7b/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/udsf-9v7b/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/udsf-9v7b/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/udsf-9v7b/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Vaccinations"
+            ]
+        },
+        {
+            "accessLevel": "restricted public",
+            "landingPage": "https://www.cdc.gov/nchs/data-linkage/esrd-restricted.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "issued": "2022-06-16",
+            "@type": "dcat:Dataset",
+            "temporal": "1974/2018",
+            "modified": "2024-10-11",
+            "references": [
+                "https://www.cdc.gov/nchs/data/datalinkage/Variable-List.pdf"
+            ],
+            "keyword": [
+                "linked usrds esrd files",
+                "nchs surveys",
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
+            "identifier": "https://data.cdc.gov/api/views/jmgj-74h4",
+            "description": "NCHS has linked data from various surveys with End Stage Renal Disease (ESRD) data obtained from the United States Renal Data System (USRDS). Linkage of the data from NCHS survey participants with the USRDS ESRD data provides the opportunity to study changes in health status and health care utilization among patients diagnosed with ESRD.",
+            "title": "NCHS Survey Data Linked to United States Renal Data System (USRDS) End-Stage Renal Disease Files",
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
+            "describedBy": "Match status can be found in the match rate tables here: https://www.cdc.gov/nchs/data/datalinkage/MatchRate-Tables.pdf",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/art/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-07-18",
+            "@type": "dcat:Dataset",
+            "modified": "2024-12-18",
+            "keyword": [
+                "art",
+                "assisted reproductive technology",
+                "clinic",
+                "fertility",
+                "infertility",
+                "services",
+                "success rates"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "ARTINFO",
+                "hasEmail": "mailto:ARTINFO@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/cchw-gdwa",
+            "description": "ART data are made available as part of the National ART Surveillance System (NASS) that collects success rates, services, profiles and annual summary data from fertility clinics across the U.S. There are four datasets available: ART Services and Profiles, ART Patient and Cycle Characteristics, ART Success Rates, and ART Summary. All four datasets may be linked by \u201cClinicID.\u201d ClinicID is a unique identifier for each clinic that reported cycles. The Success Rates dataset contains success rates for ART cycles started during the year indicated. Since ART success depends on whether patients are using their own eggs or donor eggs, success rates are included separately for these two groups. Success rates for patients using their own eggs are shown per intended retrieval, per actual retrieval, and per transfer. These success rates are reported as cumulative success rates, which take into account transfers that occur within 1 year after an egg retrieval. Since ART success depends on whether patients are using ART for the first time or had prior ART cycles, users can examine success rates for all \u201cPatients using their own eggs\u201d or for \u201cPatients with no prior ART using their own eggs.\u201d For new patients using ART for the first time, the success rates are also shown after 1, 2, or all intended egg retrievals during the reporting year. In addition, the average number of transfers per intended retrieval and the average number of intended retrievals per live-birth delivery are shown. Success rates for ART cycles that involve the transfer of embryos created from donor eggs or donated embryos are shown and are not cumulative. They are based on donor cycles started in the year indicated that had embryo transfers, regardless of when the donor eggs were retrieved. Success rates in this section are not presented by patient age group because previous data show that an intended parent\u2019s age does not substantially affect success when using donor eggs or donated embryos. The success rates are presented by types of embryos and eggs used in the transfer. This dataset excludes cycles that were considered research\u2014that is, cycles performed to evaluate new procedures.",
+            "title": "2022 Final Assisted Reproductive Technology (ART) Success Rates",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cchw-gdwa/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cchw-gdwa/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cchw-gdwa/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/cchw-gdwa/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://data.cdc.gov/dataset/2020-Final-Assisted-Reproductive-Technology-ART-Su/cchw-gdwa",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Assisted Reproductive Technology (ART)"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/summary-statistics-on-provider-enrollment/medicare-provider-type-reports/cms-program-statistics-medicare-providers",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2013-01-01/2021-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2023-03-06",
+            "references": [
+                "https://data.cms.gov/resources/medicare-provider-type-methodology"
+            ],
+            "keyword": [
+                "medicare",
+                "national",
+                "original medicare",
+                "provider enrollment",
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/5ad4e138-a8b4-49e1-a2f4-34f52b3a665a/data-viewer",
+            "description": "The CMS Program Statistics -\u00a0Medicare Providers summary tables provide data on institutional (i.e., hospitals, skilled nursing facilities, home health agencies, hospices, etc.) and non-institutional (i.e., physicians, nonphysicians, specialists, and suppliers) providers.\u00a0\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\u00a0\n\nBelow is the list of tables:\n\nMDCR PROVIDERS 1. \u00a0Medicare Providers: Number of Medicare Certified Institutional Providers, Yearly Trend\n\tMDCR PROVIDERS 2. \u00a0Medicare Providers: \u00a0Number of Medicare Certified Inpatient Hospital and Skilled Nursing Facility Beds and Beds Per 1,000 Enrollees, Yearly Trend\n\tMDCR PROVIDERS 3. \u00a0Medicare Providers: \u00a0Number of Medicare Certified Facilities, by Type of Control, Yearly Trend\n\tMDCR PROVIDERS 4. \u00a0Medicare Providers: \u00a0Number of Skilled Nursing Facilities and Medicare Certified Hospitals, and Number of Beds, by State, Territories, Possessions and Other Areas\n\tMDCR PROVIDERS 5. \u00a0Medicare Providers: \u00a0Number of Medicare Certified Providers, by Type of Provider, by State, Territories, Possessions, and Other Areas\n\tMDCR PROVIDERS 6. \u00a0Medicare Providers: \u00a0Number of Medicare Non-Institutional Providers by Specialty, Yearly Trend\n\tMDCR PROVIDERS 7. \u00a0Medicare Providers: \u00a0Number of Medicare Non-Institutional Providers, by State, Territories, Possessions, and Other Areas, Yearly Trend",
+            "title": "CMS Program Statistics - Medicare Providers",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-02/CPS%20MDCR%20PROVIDERS%202021.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Providers : 2021-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-02/CPS%20MDCR%20PROVIDERS%202020.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Providers : 2020-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-01/CPS_MDCR_PROVIDERS_1-7.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Providers : 2019-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-11/CPS%20MDCR%20TOTAL%20PROVIDERS%202018.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Providers : 2018-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2019-12/CPS_MDCR_PROVIDERS_2017_2.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Providers : 2017-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-01/CPS_MDCR_PROVIDERS_ALL.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Providers : 2016-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-01/CPS_MDCR_PROVIDERS_ALL_0.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Providers : 2015-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-01/CPS_MDCR_PROVIDERS_ALL_1.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Providers : 2014-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-01/CPS_MDCR_PROVIDERS_ALL_2.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Providers : 2013-12-31"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/medicare-provider-type-glossary",
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
+            "landingPage": "https://data.cms.gov/medicare-shared-savings-program/accountable-care-organization-participants",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2014-01-01/2025-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-15",
+            "references": [
+                "https://data.cms.gov/resources/acos-aco-participants-and-snf-affiliates-methodology"
+            ],
+            "keyword": [
+                "accountable care organizations",
+                "coordinated care",
+                "medicare",
+                "payment models",
+                "value-based care"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Shared Savings Program - CM",
+                "hasEmail": "mailto:SharedSavingsProgram@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/9767cb68-8ea9-4f0b-8179-9431abc89f11/data-viewer",
+            "description": "The Accountable Care Organization Participants data presents overview information on ACO participants in the Medicare Shared Savings Program (Shared Savings Program), including their name, track status, number of years in the program, and contact information of key personnel.\n\n\u00a0\n\nDISCLAIMER: This information is current as of the last update. Changes to ACO information occur periodically. Each ACO has the most up-to-date information about their organization. Consider contacting the ACO for the latest information.",
+            "title": "Accountable Care Organization Participants",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9767cb68-8ea9-4f0b-8179-9431abc89f11/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Accountable Care Organization Participants : 2025-01-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/f7fefddf-238c-49ea-afa5-07cb0e0a0d2c/PY2025_Medicare_Shared_Savings_Program_Participants.csv",
+                    "mediaType": "text/csv",
+                    "title": "Accountable Care Organization Participants : 2025-01-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/597651f4-ed85-40b1-8008-d0a9ee4f4b7e/data",
+                    "mediaType": "text/html",
+                    "title": "Accountable Care Organization Participants : 2025-01-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/afc09855-5e4b-4baf-bdc4-88a4459a52e5/PY2024_Medicare_Shared_Savings_Program_Participants.csv",
+                    "mediaType": "text/csv",
+                    "title": "Accountable Care Organization Participants : 2024-01-24"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/42b86f46-d8be-4e6d-bd03-b0b32dafe2d5/data",
+                    "mediaType": "text/html",
+                    "title": "Accountable Care Organization Participants : 2024-01-24"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-01/95509a9d-0344-4a5d-9cbb-3adcedbe191f/SSP_ACO_Participants_2023_01_01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Accountable Care Organization Participants : 2023-01-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/fd907586-71e8-4128-ad95-801ee1f4f6f0/data",
+                    "mediaType": "text/html",
+                    "title": "Accountable Care Organization Participants : 2023-01-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-01/048c24ac-89f8-4ca4-8fd0-a5ed32dcb9b2/SSP_ACO_Participants_2022_01_01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Accountable Care Organization Participants : 2022-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5b678653-aa36-455b-9144-1d073ef7991b/data",
+                    "mediaType": "text/html",
+                    "title": "Accountable Care Organization Participants : 2022-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/d3640f80-8b36-4ae2-acf3-b1eced28b314/SSP_ACO_Participants_2021_01_01.csv",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Accountable Care Organization Participants : 2021-01-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7b409bba-ca00-426e-9493-1dc10e5340cc/data",
+                    "mediaType": "text/html",
+                    "title": "Accountable Care Organization Participants : 2021-01-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/0194cc38-7cf3-4584-a077-0f1e873c635e/SSP_ACO_Participants_2020_01_01.csv",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Accountable Care Organization Participants : 2020-01-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3870b29c-4312-4fb1-a956-71c148ae5b50/data",
+                    "mediaType": "text/html",
+                    "title": "Accountable Care Organization Participants : 2020-01-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/0e4e117e-cd35-4719-9f0b-d62f1c96b84e/SSP_ACO_Participants_2019_07_01.csv",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Accountable Care Organization Participants : 2019-07-31oc1"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/2c209bdb-ed0c-42e0-b027-8a97024b8035/data",
+                    "mediaType": "text/html",
+                    "title": "Accountable Care Organization Participants : 2019-07-31oc1"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/5537ed12-0d9c-4213-9125-180d137ec5a0/SSP_ACO_Participants_2019_01_01.csv",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Accountable Care Organization Participants : 2019-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/017e6ab7-7e19-4e98-b4fa-30578b47e578/data",
+                    "mediaType": "text/html",
+                    "title": "Accountable Care Organization Participants : 2019-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/cd5b68e6-8e09-4866-8381-d34bc8db4220/SSP_ACO_Participants_2018_01_01.csv",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Accountable Care Organization Participants : 2018-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6ed410fb-5e7d-477f-90ed-a499e951c5d1/data",
+                    "mediaType": "text/html",
+                    "title": "Accountable Care Organization Participants : 2018-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/41c6c604-30f3-439e-8460-3087cbab0344/SSP_ACO_Participants_2017_01_01.csv",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Accountable Care Organization Participants : 2017-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/bbde17e0-01b1-46d2-b8bf-9949da11a448/data",
+                    "mediaType": "text/html",
+                    "title": "Accountable Care Organization Participants : 2017-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/2087df69-afb4-43ed-b50a-cd13c7a46d9a/SSP_ACO_Participants_2016_01_01.csv",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Accountable Care Organization Participants : 2016-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d2b525f5-77b6-416e-858c-36c9c381eb33/data",
+                    "mediaType": "text/html",
+                    "title": "Accountable Care Organization Participants : 2016-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/9f516f5c-6c08-4bab-947f-8d3f2c950db4/SSP_ACO_Participants_2015_01_01.csv",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Accountable Care Organization Participants : 2015-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4a743510-fbc3-4363-aab5-9d6c0fe3dea7/data",
+                    "mediaType": "text/html",
+                    "title": "Accountable Care Organization Participants : 2015-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/d6084efd-ae4b-4633-8983-25485978717c/SSP_ACO_Participants_2014_01_01.csv",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Accountable Care Organization Participants : 2014-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5ebc6246-1861-4d9f-92b4-33c69b315d64/data",
+                    "mediaType": "text/html",
+                    "title": "Accountable Care Organization Participants : 2014-12-31"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/accountable-care-organization-participants-data-dictionary",
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
+            "landingPage": "https://data.cdc.gov/d/bk9t-cq4b",
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
+                "non-congenital",
+                "wonder",
+                "yellow fever",
+                "zika virus disease"
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
+            "identifier": "https://data.cdc.gov/api/views/bk9t-cq4b",
+            "description": "NNDSS - TABLE 1PP. Yellow fever to Zika virus disease, non-congenital \u2013 2020.  In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1PP. Yellow fever to Zika virus disease, non-congenital",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bk9t-cq4b/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bk9t-cq4b/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bk9t-cq4b/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bk9t-cq4b/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/dataset/service-locator-family-planning-title-x",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2014-04-08",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "birth control",
+                "cervical cancer",
+                "community health",
+                "contraceptives",
+                "family planning",
+                "health care providers",
+                "health services",
+                "locator",
+                "pregnancy",
+                "primary care",
+                "providers",
+                "safety",
+                "sexual assault",
+                "sexually transmitted infections",
+                "stds",
+                "stis",
+                "testing",
+                "treatment",
+                "treatments",
+                "wellness"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Office of Population Affairs",
+                "hasEmail": "mailto:opa@hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Health & Human Services"
+            },
+            "identifier": "20f6d943-1707-457d-876b-ef65bcd7f476",
+            "description": "<p>This locator tool will help you find Title X family planning centers that provide high quality and cost-effective family planning and related preventive health services for low-income women and men.</p>\n<p>Family planning centers offer a broad range of FDA-approved contraceptive methods and related counseling; as well as breast and cervical cancer screening; pregnancy testing and counseling; screening and treatment for sexually transmitted infections (STIs); HIV testing; and other patient education and referrals.</p>\n<p>4,400 family planning centers serve about 5 million clients each year. Services are provided through state, county, and local health departments; community health centers; Planned Parenthood centers; and hospital-based, school-based, faith-based, other private nonprofits.</p>\n<p>Title X staff are specially trained to meet the contraceptive needs of individuals with limited English proficiency, teenagers, and those confronting complex medical and personal issues such as substance abuse, disability, homelessness or interpersonal and domestic violence.</p>",
+            "title": "Service Locator - Family Planning Title X",
+            "programCode": [
+                "009:019"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://locator.aids.gov/opa-widget.js",
+                    "mediaType": "text/html",
+                    "title": "Widget "
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.hhs.gov/opa/",
+                    "mediaType": "text/html",
+                    "title": "Text "
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.hhs.gov/opa/widgets/",
+                    "mediaType": "text/html",
+                    "title": "Widget "
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://locator.aids.gov/data-how-to.html",
+                    "mediaType": "text/html",
+                    "title": "API "
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
+            "landingPage": "https://healthdata.gov/d/d2f3-87v3",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2015-04-07",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-08",
+            "keyword": [
+                "drug manufacturer contacts"
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
+            "identifier": "9fcb14ec-d5f0-536e-9938-3f0024531e5b",
+            "description": "Drug Manufacturer Contact Information contains Optional Effective Date, Termination Date (if applicable), and Legal, Invoice and Technical Contact information for each drug company participating in the Medicaid Drug Rebate Program. For more information see: https://www.medicaid.gov/medicaid/prescription-drugs/medicaid-drug-rebate-program/index.html",
+            "title": "Drug Manufacturer Contacts",
+            "programCode": [
+                "009:076"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/3Q2024LabelerContacts.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P10Y",
+            "theme": [
+                "Uncategorized"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/d3b6-wcft",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-01-24",
+            "@type": "dcat:Dataset",
+            "modified": "2024-01-22",
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
+            "identifier": "bbdcd2d0-13ac-4c1f-8670-914acb43b81e",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2024-01-15-to-2024-01-21",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rprt-drug-01-15-2024-to-01-21-2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2024-01-15-to-2024-01-21"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/d3br-cfmg",
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
+            "identifier": "edbb579b-1056-5cb6-99b9-16f4dafbd27e",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "implAuto_fileType_measureDisplayGroups",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/fileType_measureDisplayGroups.csv",
+                    "description": "{\"dataset\": \"fileType_measureDisplayGroups\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "@type": "dcat:Distribution",
+                    "title": "fileType_measureDisplayGroups csv file"
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
+            "bureauCode": [
+                "009:20"
+            ],
+            "landingPage": "https://data.cdc.gov/d/9ikp-t8tw",
+            "issued": "2024-11-21",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-23",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Emma Baubly",
+                "hasEmail": "mailto:rno8@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/9ikp-t8tw",
+            "description": "",
+            "title": "CDT_INDIVIDUAL_BY_WEEK_LOCAL",
+            "programCode": [
+                "009:028"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9ikp-t8tw/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9ikp-t8tw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9ikp-t8tw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9ikp-t8tw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/d52h-r2s7",
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
+            "identifier": "ec0d4b04-55bc-56d1-bff5-280f68915442",
+            "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
+            "title": "State Drug Utilization Data 1993",
+            "programCode": [
+                "009:076"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/StateDrugUtilizationData1993.csv",
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
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/skilled-nursing-facility-enrollments",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2022-09-27",
+            "temporal": "2022-09-01/2025-01-31",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-15",
+            "references": [
+                "https://data.cms.gov/sites/default/files/2024-12/1ea55414-f441-4694-a13c-6400d4e28ef6/SNF_Data_Guidance.pdf"
+            ],
+            "keyword": [
+                "hospitals & facilities",
+                "medicare",
+                "medicare advantage",
+                "original medicare",
+                "provider enrollment",
+                "skilled nursing"
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/5f2c306f-3b1c-42cd-b037-187b2ce22126/data-viewer",
+            "description": "The Skilled Nursing Facility (SNF) Enrollments dataset provides enrollment information of all SNF 's currently enrolled in Medicare. This data includes information on the SNF's legal business name, doing business as name, organization type and address.\n\n\u00a0\n\nOn November 17, 2023, CMS published in the Federal Register a final rule titled, \u201cMedicare and Medicaid Programs; Disclosures of Ownership and Additional Disclosable Parties Information for Skilled Nursing Facilities and Nursing Facilities; Medicare Providers\u2019 and Suppliers\u2019 Disclosure of Private Equity Companies and Real Estate Investment Trusts\u201d (88 FR 80141). This final rule implements parts of section 1124(c) of the Act which requires SNFs to disclose detailed information about their ownership and management as well as additional data regarding: (1) other parties with which the SNF is associated; and (2) the ownership structures of these other parties.\u00a0 Refer to Medicare Enrollment for Providers & Suppliers for more information on the Skilled Nursing Facility disclosure requirements. \n\nSection 6101(b) of the Affordable Care Act states that no later than 1 year after final regulations promulgated under section 1124(c) of the Act are published in the\u00a0Federal Register, the Secretary shall make the information reported available to the public.\n\n\u00a0On November 21, 2024 CMS updated this dataset to include this reported information.",
+            "title": "Skilled Nursing Facility Enrollments",
+            "describedByType": "application/pdf",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5f2c306f-3b1c-42cd-b037-187b2ce22126/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Skilled Nursing Facility Enrollments : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/9e1eb2ca-8b81-4d3b-a77f-51b52c1a6e84/SNF_Enrollments_2025.01.02.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Enrollments : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f9368b76-cffb-452c-b718-fd091d57abf1/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Enrollments : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/8abf115a-f63f-46fe-b1f6-ebb163631dca/SNF_Enrollments_2024.12.05.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Enrollments : 2024-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5b3bf673-11ff-4912-b95b-56f2b39d3835/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Enrollments : 2024-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/6a307bc7-b6d3-4c29-9594-f1d2ca0c4caa/SNF_Enrollments_2024.10.30.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Enrollments : 2024-11-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8b543110-bbd1-4823-b3ab-dde6abb3b39d/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Enrollments : 2024-11-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/170649d4-c6f4-4357-b913-67ea3d9eb860/SNF_Enrollments_2024.10.07.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Enrollments : 2024-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/57f6a81b-c9d5-4168-9788-326a799878e7/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Enrollments : 2024-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/a0828130-4ccc-4aa7-b9ea-3522dc24441b/SNF_Enrollments_2024.09.02.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Enrollments : 2024-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/700ea9e5-e45e-49b5-a95a-c8a5ea9ddf74/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Enrollments : 2024-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/ef6c62dd-989e-4d01-9c9c-98adf8fa8035/SNF_Enrollments_2024.08.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Enrollments : 2024-08-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5751cc8d-a6f7-469b-9048-44519d0affcf/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Enrollments : 2024-08-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/d0500dde-61ef-4e3a-81e8-75b6e2319b27/SNF_Enrollments_2024.07.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Enrollments : 2024-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/1b0b0e22-cfc4-40e3-bb72-a599c002fc8d/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Enrollments : 2024-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/73e539b0-428a-4c09-8e4c-327054c15452/SNF_Enrollments_2024.06.03.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Enrollments : 2024-06-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f01200e3-3ba4-4307-88c8-8e18f3e6dfd9/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Enrollments : 2024-06-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/1c7ef9a3-04c3-4180-b8f9-b0c7b7ffd073/SNF_Enrollments_2024.05.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Enrollments : 2024-05-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/b9b08823-8fab-4560-a817-a5bfe19446ac/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Enrollments : 2024-05-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/ef4ac112-6b70-4f3b-a6d4-fb7243c13bf4/SNF_Enrollments_2024.04.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Enrollments : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f57c7020-e0f6-49ee-9da1-2136254a7d6a/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Enrollments : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/31692461-d8b7-43e3-a86f-c01e563fc29e/SNF_Enrollments_2024.03.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Enrollments : 2024-03-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/bfb5dedd-d984-4a83-ac19-f257eafe8b3a/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Enrollments : 2024-03-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/737cb9f2-c943-42a4-8069-f4d17a7c5a67/SNF_Enrollments_2024.02.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Enrollments : 2024-02-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/45ef7e1a-8983-4b1e-aa0c-dfa9b81a0ba7/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Enrollments : 2024-02-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/2055c3b2-83d2-4f3f-a3dc-bae3d86fd68f/SNF_Enrollments_2024.01.05.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Enrollments : 2024-01-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9384eb6d-c67c-427b-86db-957ce2ba464f/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Enrollments : 2024-01-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/02ff69b5-5e72-45b8-9f9f-5736d501b738/SNF_Enrollments_2023.12.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Enrollments : 2023-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/27c7c081-cc70-410d-aa17-642130190dfb/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Enrollments : 2023-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/9db0d892-9962-4d39-937e-b87d773d5b44/SNF_Enrollments_2023.11.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Enrollments : 2023-11-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/b66f1ec7-445b-4492-a1dc-0b605a6f3965/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Enrollments : 2023-11-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/800d57bd-9b12-43a5-8f89-b05b2591c8ca/SNF_Enrollments_2023.10.02.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Enrollments : 2023-10-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/cff5276c-9833-422b-a4e6-acccacaf6f96/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Enrollments : 2023-10-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/4baa54dc-206d-49e9-bf05-d3b0ae664543/SNF_Enrollments_2023.09.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Enrollments : 2023-09-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/15445287-c032-43f2-95cd-3108e8334ef1/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Enrollments : 2023-09-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/0305936f-c257-4a4f-9cae-5b2c40b3cb46/SNF_Enrollments_2023.08.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Enrollments : 2023-08-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/03b7e19c-07c3-4781-aa08-156e6cea8442/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Enrollments : 2023-08-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/3e7557f6-9eee-4e33-9cb4-1fe60adcd4bc/SNF_Enrollments_2023.07.06.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Enrollments : 2023-07-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3fc3d236-ca64-45d3-8356-12111c1cfb63/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Enrollments : 2023-07-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/486b9f0e-79b6-4d6e-93a2-d5c8b8f26f82/SNF_Enrollments_2023.06.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Enrollments : 2023-06-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/49b744ed-32f6-4559-bfb3-d3760c8af726/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Enrollments : 2023-06-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/b9c9548a-8196-4f77-aad5-990d7f40a0a8/SNF_Enrollments_2023.05.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Enrollments : 2023-05-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/124978a3-3291-4841-88c4-06abff9aee0c/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Enrollments : 2023-05-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/3dc5011e-f26e-4a56-bb94-2515f200bcd7/SNF_Enrollments_2023.03.31.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Enrollments : 2023-04-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/cc584953-f08d-4c51-af24-6aba63d08535/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Enrollments : 2023-04-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-03/cda8a791-992b-44d9-9ede-9d9b829d234a/SNF_Enrollments_2023.03.10.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Enrollments : 2023-03-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/db868f58-8864-4a13-ad29-fc341720ffda/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Enrollments : 2023-03-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-02/a964416e-ced6-48e7-b4d2-f0aa1c0e06c5/SNF_Enrollments_2023.02.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Enrollments : 2023-02-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/651f17d7-8acc-4636-b035-16441b17ed7c/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Enrollments : 2023-02-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-01/46f18401-31d7-4748-b77e-d92050939029/SNF_Enrollments_2022.12.30.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Enrollments : 2023-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/67fcc7b3-aeef-4d37-b761-df0bf2bb65d2/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Enrollments : 2023-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-12/0b126f7f-b3e0-42ff-b4f9-afc926e9ef41/SNF_Enrollments.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Enrollments : 2022-11-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/57238616-3730-4548-a157-11128528eeba/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Enrollments : 2022-11-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-11/da84446f-b80a-4396-b941-c4c76e3d2c9d/SNF_Enrollments.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Enrollments : 2022-10-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ee70fa85-7d78-47c3-83b2-e1a5b54cee7c/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Enrollments : 2022-10-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-09/793922d8-9ffe-4a6e-bfe8-cfa30a4f3fb1/SNF_Enrollments.csv",
+                    "mediaType": "text/csv",
+                    "title": "Skilled Nursing Facility Enrollments : 2022-09-20"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/b6a79e6e-1257-43c8-ada3-dcd1d115570c/data",
+                    "mediaType": "text/html",
+                    "title": "Skilled Nursing Facility Enrollments : 2022-09-20"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-10/SNF_Enrollments_Data_Dictionary.pdf",
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
+            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-09-19",
+            "temporal": "2000/2021",
+            "@type": "dcat:Dataset",
+            "modified": "2024-09-30",
+            "keyword": [
+                "bureau of labor statistics",
+                "health care employment",
+                "health care practitioners",
+                "health care practitioners and technical occupations",
+                "health care support occupations",
+                "health care wages",
+                "health us",
+                "hourly wages",
+                "industry",
+                "mean hourly wages",
+                "occupational employment and wage statistics",
+                "sdoh-occupation-type",
+                "sdoh-source-of-health-care",
+                "sdoh-wages",
+                "us department of labor"
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
+            "identifier": "https://data.cdc.gov/api/views/q9cb-be9u",
+            "description": "Data on health care employment and wages in the United States, by selected occupations. Data are from Health, United States. Source: U.S. Department of Labor, Bureau of Labor Statistics, Occupational Employment and Wage Statistics.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
+            "title": "DQS Health care employment and wages, by selected occupations: United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/q9cb-be9u/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/q9cb-be9u/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/q9cb-be9u/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/q9cb-be9u/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Annual",
+            "theme": [
+                "National Center for Health Statistics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-05-14",
+            "@type": "dcat:Dataset",
+            "modified": "2022-04-27",
+            "keyword": [
+                "african americans",
+                "alaskan natives",
+                "american natives",
+                "asian continental ancestry group",
+                "continental population groups",
+                "death",
+                "european continental ancestry group",
+                "fetal death",
+                "health us",
+                "hispanic americans",
+                "infant",
+                "infant death",
+                "live birth",
+                "mortality",
+                "mothers",
+                "oceanic ancestry group",
+                "pregnancy",
+                "pregnancy complications"
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
+            "identifier": "https://data.cdc.gov/api/views/nfuu-hu6j",
+            "description": "Data on infant, neonatal, postneonatal, fetal, and perinatal mortality rates by selected characteristics of the mother. Please refer to the PDF or Excel version of this table in the HUS 2019 Data Finder (https://www.cdc.gov/nchs/hus/contents2019.htm) for critical information about measures, definitions, and changes over time. \n\nSOURCE: NCHS, National Vital Statistics System, public-use Linked Birth/Infant Death Data Set, public-use Fetal Death File, and public-use Birth File. For more information on the National Vital Statistics System, see the corresponding Appendix entry at https://www.cdc.gov/nchs/data/hus/hus19-appendix-508.pdf.",
+            "title": "Infant, neonatal, postneonatal, fetal, and perinatal mortality rates, by detailed race and Hispanic origin of mother: United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/nfuu-hu6j/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/nfuu-hu6j/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/nfuu-hu6j/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/nfuu-hu6j/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/Medsun/searchReportText.cfm",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2013-11-13",
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
+            "identifier": "068aa9da-ef7e-419a-9de2-2a690dbec65b",
+            "description": "The Medical Product Safety Network (MedSun) is an adverse event reporting program launched in 2002. The primary goal for MedSun is to work collaboratively with the clinical community to identify, understand, and solve problems with the use of medical devices.",
+            "title": "MedSun Reports",
+            "programCode": [
+                "009:005"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/Medsun/searchReportText.cfm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/dataset/health-it-catalog",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2013-11-08",
+            "temporal": "2013-07-01T00:00:00-04:00/2013-07-01T00:00:00-04:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "health care cost",
+                "health care providers",
+                "office-of-the-national-coordinator-for-health-information-technology-department-of-health-human-services",
+                "other"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "HealthITcatalog",
+                "hasEmail": "mailto:HealthITcatalog@hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of the National Coordinator for Health Information Technology, Department of Health & Human Services"
+            },
+            "identifier": "0fb05840-02fe-4199-8f2b-efaac0e5d868",
+            "description": "<p>This is a consolidated list of Health IT initiatives and websites across HHS.</p>",
+            "title": "Health IT Catalog",
+            "programCode": [
+                "009:110"
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/fiscal-intermediary-shared-system-attending-and-rendering",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2023-05-21/2025-01-18",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-21",
+            "references": [
+                "https://data.cms.gov/sites/default/files/2020-08/Fiscal%20Intermediary%20Standard%20System%20%28FISS%29.pdf"
+            ],
+            "keyword": [
+                "medicare",
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/75e8dcb2-78eb-4a7d-a377-9108441966db/data-viewer",
+            "description": "The Fiscal Intermediary Shared System (FISS) Attending and Rendering dataset provides a list of those attending and rendering physicians for the FISS. FISS edits require that the Line Item Rendering Physician information be transmitted when providers submit a combined claim. Claims that include both facility and professional components, need to report the rendering physician or other practitioner at the line level if it differs from the rendering physician/practitioner reported at the claim level.\n\n\u00a0\n\nNote: This full dataset contains more records than most spreadsheet programs can handle, which will result in an incomplete load of data. Use of a database or statistical software is required.",
+            "title": "Fiscal Intermediary Shared System Attending and Rendering",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/75e8dcb2-78eb-4a7d-a377-9108441966db/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/09f329ea-ac43-452b-9e01-6a0410170a2c/FISS_AR_20250121.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7eb8e1a2-573c-43cf-8b2e-92a02fc2af12/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/474c5d07-9311-4ed0-a1be-cc86bb06edd3/FISS_AR_20250117.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f0acdba9-686b-4624-88ff-fd5b3da9a493/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/83364b8c-b003-4aac-890d-929c5c3970c7/FISS_AR_20250113.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/45754bc3-7ec9-41ed-98bf-0b7ba533b9ab/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/00de2339-1960-4faf-8c0e-958d1d6588dd/FISS_AR_20250109.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-10"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/15fc4c7e-7b0d-4d40-9ee7-764617b88314/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-10"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/4343a52f-bcd4-4a7b-80df-62ae1843c5bc/FISS_AR_20250106.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/72c2f88a-119d-46e6-93a6-53f51df70322/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/2dc247ec-959e-404c-9429-3c9c89b2d29a/FISS_AR_20250102.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6690cab2-a02b-4e71-9f9e-217a8b1fa1c8/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2025-01-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/426fa31d-24f7-4ec1-a27b-5616333e7bfb/FISS_AR_20241230.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/b5fc06b1-1985-46aa-8d2d-e1b978b1ebe4/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/dbad4a20-990e-4804-ac21-46e8d3ac1b33/FISS_AR_20241226.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a0ac8443-e8c3-488e-b723-bf38ca8fc5f0/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/014325b1-1bb2-4f34-b322-b9021bb1f56f/FISS_AR_20241223.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/b360845d-eae3-4075-9a22-c920d4ca5a28/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/85e3eee3-b208-4f07-8afa-340859a8ced7/FISS_AR_20241219.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-20"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f4721857-9285-49df-9c50-59828c62e8f9/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-20"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/d2c014ca-f2cf-40e2-9ee3-86403a7f5f4f/FISS_AR_20241216.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ec7ceec5-237f-43ae-a67b-d5a85e40eaec/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/099bdb31-063f-4396-8bec-513f500f55c0/FISS_AR_20241212.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f2149601-fbaa-43eb-97ac-7078e0d980ed/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/5744e19f-5baa-4da7-a583-6b868ee6730f/FISS_AR_20241209.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-10"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/61001003-0443-474e-aa30-1529f19f8e08/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-10"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/341796c3-a235-403f-97d4-2900c0194d12/FISS_AR_20241205.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f073c4b6-27d9-4c94-8bf5-d9e453e73835/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/47594677-d992-41fd-b35d-3308881ce3bd/FISS_AR_20241202.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/140ded17-df75-4182-a591-95430259374c/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-12-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/2d550efb-e0d4-446f-8cbd-fdb22ab95043/FISS_AR_20241129.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/550e9016-eef0-49a1-ab44-f4a531844ac6/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/1c26b1de-a9ba-46be-b932-de94beddcaad/FISS_AR_20241125.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/806921ea-04d0-4105-8286-ce1079a0e883/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/4c631191-30fd-46fd-82d6-f6ce500fcc7c/FISS_AR_20241121.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6463d5d5-3d98-474c-9c84-fd2c02166574/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/c6bd5230-1c49-4d93-a679-28688e809fab/FISS_AR_20241118.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d0eb0f87-f9f7-4cc6-aa81-2334974f81bf/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/14a91ecd-dab9-40a7-8d8a-2b299334151e/FISS_AR_20241114.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/fcb7637d-8cf5-4abe-8d54-e15c195ba124/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/6760109e-2e4a-4ce1-a88d-08d79c4ed142/FISS_AR_20241112.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/aa96d2f5-5be4-47f5-bae0-c9189f58d049/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/f2975682-597e-4e70-aeb0-365681d70365/FISS_AR_20241107.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e42de85e-4265-47c8-8534-ce49f20d7ea6/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/f5fda85e-b208-4e98-b50d-91387875e750/FISS_AR_20241104.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f3148bfb-8410-4fd5-85c9-fe2e5e7fa2b2/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/38c30221-e9f5-4abc-a1d5-e3954fea2397/FISS_AR_20241031.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7ae39053-2d53-4f1f-9569-63e310de7554/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-11-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/b84ebcaf-78e1-4f0c-bc68-23a83ae7b90f/FISS_AR_20241028.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5689e659-88a7-4240-baa3-48225b12eae1/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/97cbaebc-79aa-4bed-b9a3-e8545c9a16ac/FISS_AR_20241024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-25"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7fd350d0-0e68-4f59-9a7c-6fff0345f181/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-25"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/d9e537db-5649-449c-94cc-47cc13b12a74/FISS_AR_20241021.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/733dc123-cd57-47bc-a4aa-7c87a5781934/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/6b45df61-2b99-4798-8f1a-98b88236e4c8/FISS_AR_20241017.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-18"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d4b9b67b-7c15-4617-897a-9bcfb23280ce/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-18"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/0d54ef8c-cf19-4f65-8592-5cc10ba0d9b8/FISS_AR_20241015.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a438db1f-57b9-4d63-bc78-fd648ca908b3/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/153b4397-9dfc-4bb0-917f-a26b8a3ddb7c/FISS_AR_20241010.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f8d0352e-2670-4aaa-a150-f51a074bc336/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/4b6eb3b2-b9f5-4c7d-b64e-9f5997202808/FISS_AR_20241007.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d0ec72d9-f705-4c79-9efb-e603f3470d71/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/f615cbb5-38ec-44e5-b44a-2f1adea533b2/FISS_AR_20241003.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-04"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/b761e361-b2b4-4778-aa87-6c9550714b85/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-04"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/40fcff68-2524-4045-af19-65c2fcea54ab/FISS_AR_20240930.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/76600c23-89d5-4cdf-b667-7a398d9cf567/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/2949d8c0-ff22-43c0-a87e-b892e8f5b5cb/FISS_AR_20240926.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7e8d18c1-60e6-4672-9a14-900d36d1aebf/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/c7fd8a1e-7768-406a-b481-8d4cbaeafc1a/FISS_AR_20240923.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-24"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8736defb-6eaa-4bf9-8d1a-720431a76571/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-24"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/6e36cb23-3085-4b1c-8ab8-e80d9cf514bb/FISS_AR_20240919.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-20"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/134d1783-60cd-436a-a33e-98a369b844d4/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-20"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/024ea43e-70cd-4ea9-9d6f-e9c82b638dee/FISS_AR_20240916.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/01ead372-97d2-427b-bb06-52b64cd674a8/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/f4e3e21b-44a2-4c41-9c69-cdb139ab35c3/FISS_AR_20240912.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/36cbbf42-33a9-4dad-8f62-9936ee3b78d0/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/995cb12a-e855-47d0-b084-2333ff1f6881/FISS_AR_20240909.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-10"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/afb2dc1a-0828-4e9f-8678-eb180d0c34e6/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-10"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/8fc6ec5a-ea70-4bed-83f3-bb5931df815d/FISS_AR_20240905.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/726981dd-4854-4c11-bd2f-776507bd276b/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/0af84e0e-d29c-403f-bba4-da1e6f6bc238/FISS_AR_20240903.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-04"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c28f7040-1817-4455-9301-2958e9cd26d2/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-09-04"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/c4263f08-8500-4ce5-b9a4-1aa6f4e7447f/FISS_AR_20240829.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/01118d40-b93e-41af-97e9-93d644edaf9f/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/3d82538a-c4fa-4ea0-ad06-39bd3728f392/FISS_AR_20240826.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/be79731c-5eef-48c4-a55f-829e143098d6/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/9538b51c-9d08-4ed7-9f0e-88bc46df01a5/FISS_AR_20240822.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5798cc0a-ffe0-456d-8b0f-780d4fe7b8bc/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/e2748d2f-752f-4f79-9b3d-ca4ef5e3e570/FISS_AR_20240819.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-20"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/0063124a-af45-45c2-8b8e-5f91b67648d0/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-20"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/47cee078-a858-44a3-98ac-484f9e2cf9ba/FISS_AR_20240815.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/29d06a31-ddd9-4b52-b678-31355217a9fa/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/f1f8d277-b2ac-46d2-9121-794f71804f87/FISS_AR_20240812.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/839d9042-a39f-41fb-bbc4-88c3d9f4c3b9/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/6cc20ca2-534a-486c-b322-51947883ffea/FISS_AR_20240808.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/fce0228b-16b0-404a-872b-a34e8d01ada1/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/1edc801f-5e93-4071-886f-72fbd4869a98/FISS_AR_20240805.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/10a01a39-36cb-4510-96e3-0f6ff0e585d1/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/d28629a9-8bd3-4bd9-b410-e743901a93eb/FISS_AR_20240801.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c8bf9741-5a2e-460e-9d0e-c8e7254c850f/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-08-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/f3f4d6ea-eeff-4b8b-b3d4-60ec86f5573b/FISS_AR_20240729.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/56e31267-840a-4b95-aa28-c7ecc8377664/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/49069c44-008a-4174-908f-0cd0a4fa6558/FISS_AR_20240725.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5f397310-01d9-48a0-a89f-560198c03523/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/07a37ec9-1642-4212-8c51-b0200fd57303/FISS_AR_20240722.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/76b42075-bc48-4898-a0c0-b9c1a4a9516f/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/98daa63b-1982-4bbb-8452-f1b653a50134/FISS_AR_20240718.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/82a7baaf-2e2f-4a56-97df-6ea1d0c998c7/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/61a3e1b5-39d4-40a7-a31d-925510ee6c7d/FISS_AR_20240715.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/b0ec6284-cab7-47b5-9401-9d2ee550c31f/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/fe268742-36d9-4979-bd59-8c8891e50c1e/FISS_AR_20240711.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3ba38bb3-9024-4246-b101-1794132c8c3b/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/2f21ce07-5fca-445a-9a5f-56464b00b149/FISS_AR_20240708.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a5732418-2c2d-4c78-a418-c92eb19d56f0/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/2440b8de-4fed-48a2-84ad-16e46f80c600/FISS_AR_20240705.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6d302b6f-2388-455f-af86-022ed1b1dbe2/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/28f34db0-711f-4ba0-8650-cb1b14233b20/FISS_AR_20240701.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ce1a7f2d-a86b-497f-9c36-5401106b60b6/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-07-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/2095c686-3dd1-4fe6-811b-eba03efe576b/FISS_AR_20240627.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4f0ffaeb-5d29-43f1-903e-1e72ff380735/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/47120d82-d767-4da3-8914-e71d95d4d06b/FISS_AR_20240624.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-25"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/119273f5-f6cb-420e-9194-3a2ab1d8f1f3/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-25"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/53480c18-5c65-4216-8ff9-4e1f9c6847a6/FISS_AR_20240620.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/00d8a926-7a71-49e8-ad22-f37c8141e2f6/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/99842d5a-aa43-4912-b319-1631cfccfedc/FISS_AR_20240617.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-18"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/2eb0dd30-df9c-4a08-8ca8-f9b6c95c6da6/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-18"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/80016f6c-aac6-40e1-a3f9-6119bde49d97/FISS_AR_20240613.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/1ea6c61a-73c4-4ecf-a655-87f72fc49081/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/bd6f30ae-92cf-4af8-bf91-ef962af9bcef/FISS_AR_20240610.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6655da6e-bbc5-45bc-8cf5-76085f127d32/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/62a8b94b-a642-4fb3-9572-74fcbef36c43/FISS_AR_20240606.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e25efd14-237a-4f72-ba70-d383009210df/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/73666b24-e4a6-493f-9366-d5acfb462eae/FISS_AR_20240603.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-04"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6032266f-38f7-4c5a-9d24-b5b5d78a768c/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-06-04"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/8146601e-f8cc-4c18-bed9-f82191dd9071/FISS_AR_20240530.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/12ddd8ee-2610-4bdf-9a2d-3715321e8dc0/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/26aa1c3e-fec2-443e-b014-461681a42f18/FISS_AR_20240528.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/207e4bdd-2208-44b2-bccd-cd893272d524/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/6e2e4960-c2cc-44d0-9787-d3dd66276eaa/FISS_AR_20240523.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/243f8795-b01d-4b75-aa53-24447db9809b/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/e3d903e4-f090-434e-93e5-5d724769157f/FISS_AR_20240520.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/bb50957d-5f42-43e6-baa2-97732d270559/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/21971043-4460-4e4f-8c33-bfa662c3bb3d/FISS_AR_20240516.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5273263b-438e-4790-8708-76c5b77e71f7/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/84ce3651-e545-46e9-86de-3b310e927285/FISS_AR_20240513.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7358d903-e410-4ff0-8d47-2f90004e6d68/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/646706c4-6d8c-40ed-90a0-fcc03e0857b9/FISS_AR_20240509.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-10"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/01ad7b7f-5e87-4a8d-80e9-b74ddda0ee34/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-10"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/de2cb741-8742-49f7-91a6-8ab3c499751d/FISS_AR_20240506.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4049fe60-811c-48e1-a93a-92964940e2d3/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/4a67eac5-cb96-4085-b319-b78549d69bd9/FISS_AR_20240502.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/49031519-53af-4bf2-b370-73641b046296/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-05-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/efc05f60-389d-4f9c-a011-17bd27524274/FISS_AR_20240429.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/daa70c47-280b-4ea8-80ed-eee7e7d854e5/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/09dea68b-78d2-4b3f-ac56-5131c3c7d738/FISS_AR_20240425.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6e148086-b09a-4be5-afd0-c88500f889ea/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/4b7b8b7d-37c8-4e21-81ef-1efd631e8b25/FISS_AR_20240422.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a15b8f30-0e10-48ac-ae06-974df43aa567/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/1a270571-1903-4301-ae89-fded1e7ab0b0/FISS_AR_20240418.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4889910f-06d7-4c8c-9d7b-8069b9be8907/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/71e5d150-0a7b-415c-8292-2cae6e4b8632/FISS_AR_20240415.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/65d6de54-53b3-4088-94a8-d9f658b0662c/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/e88c06da-384e-4214-99a7-88138b619306/FISS_AR_20240411.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-12"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e43701de-6010-454c-a580-faac98366a82/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-12"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/36ba7388-e6b0-4249-91c6-b714eb2003b6/FISS_AR_20240408.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3997a8e1-5710-4448-8066-7e6474be0458/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/47225ab9-f424-4c67-a286-869f47a08ea5/FISS_AR_20240404.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/20dee1c9-c321-4557-bb6d-7c0892fb8fa0/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/29350c78-dbeb-41b8-8295-bd2f57f7c5d4/FISS_AR_20240401.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/0eea222d-6d27-44f2-bf71-61b1f77ee53f/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-04-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/674f8851-f28d-4211-9ecc-ce0b9c9fbc71/FISS_AR_20240328.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ec3e4892-bfcd-42fd-adb7-21cd0b693fe5/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/f4c56758-a1f1-4786-88dd-b4bd55cf62bb/FISS_AR_20240325.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/eb191fc1-81ba-46f3-bfa6-bde5bb53df8a/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/a12729f5-994a-4a6f-98a7-f18a6dae8f02/FISS_AR_20240321.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/573d1ead-92c8-418b-a2f0-17b3dd79049a/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/c5d80789-22d2-4a66-abb9-99d3fb1639d1/FISS_AR_20240318.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ff87c616-dd2e-4e4d-ab23-62d1c16ad16b/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/cbdc1069-10da-4cb0-85ef-56b89f1bd9c2/FISS_AR_20240314.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d4e7a5a7-95b6-46eb-8ee9-23f51df42cd6/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/f9caaef4-c904-4863-96a8-13be57e27b67/FISS_AR_20240311.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-12"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f84b09ad-b3a1-412d-a5ed-b9c3743027a8/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-12"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/f6de1ecd-f63d-4d45-8fca-21cc49dcde98/FISS_AR_20240307.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4d502a4d-0be6-44c7-a1f5-d3e23a74e4f1/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/442ecb71-b990-4766-8d7f-81bf42e57bed/FISS_AR_20240304.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c6a80c91-e507-43f1-8903-192e25b6ce31/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/782673b2-6877-4f1b-b3ce-7d0594dee84a/FISS_AR_20240229.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/027f07ad-9b98-4f80-8f79-c21e408b5ebc/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-03-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/75d2b77e-1b1a-47c5-b56b-a4a7bc14509e/FISS_AR_20240226.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5fb5b043-4030-487c-8fc7-f4ccdf9483eb/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/930d6e59-b7f2-45bd-b8ab-87e9ca0e4686/FISS_AR_20240222.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/525ce3e3-1e30-4311-b9ad-41b7bdb44860/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/34614b33-c9b6-4f7f-87cd-6f5038fa3c5f/FISS_AR_20240220.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/2c60e94f-862c-488a-99c4-ed7e56d5d6e0/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/c854c01a-c63a-4cce-9eae-13261295c6fc/FISS_AR_20240215.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d27b01b0-f266-4665-a33d-1b9c0a740aed/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/f705f608-f082-47e5-97f5-c8e6dc9d8715/FISS_AR_20240212.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/40535bb5-6033-4edd-91bc-8a874670028e/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/2a8cc37b-8d66-4c6c-99c2-735c44a7252f/FISS_AR_20240208.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/333a55b5-2c6a-4d4f-9ff2-27752fb618ba/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/4d295a3e-7742-4fde-ad3f-12bc46d03da1/FISS_AR_20240205.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/676c46d4-9dd1-4c3e-a2d7-7a821e3fcade/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/8a20dbe9-c9c5-4293-bc50-1c31410f73b0/FISS_AR_20240202.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/005caef9-888c-48de-bedd-fd277ed99b16/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-02-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/15a6984f-1f54-4438-82b5-26fc66cc4557/FISS_AR_20240129.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/74c4ef9a-204a-4b8e-80a0-5597652e9336/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/08ef4657-4669-468b-836e-15a407817a55/FISS_AR_20240126.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4631bbb6-3924-421d-9f2d-f16d6b2526b4/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/1bdf9b0b-386b-4f7f-b9dc-3b48ab94c887/FISS_AR_20240122.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/bd0bb369-dbe6-40ab-8729-7113f1ac64c0/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/65a06865-4edc-4e8d-a151-a5bfa953c314/FISS_AR_20240119.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/93f797c5-3a27-44ba-9a35-16fa1b9f19b1/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/5d2895e2-4c32-4a1c-a320-058b4ebdd919/FISS_AR_20240115.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a4213a34-e7db-4e7b-9f3b-ade91b81d957/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/19dbdb50-117e-4aec-918b-f21da3d8d471/FISS_AR_20240111.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-12"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e1e0c962-89ea-4452-8576-74b166309bcd/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-12"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/665557d7-32f6-438b-bb89-a2f490832ad4/FISS_AR_20240108.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/b11141bc-9352-4692-9215-6269c40c686d/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/a78aa3e4-42d0-4c74-8ea6-2bed183c931e/FISS_AR_20240104.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ed5f8ef0-66a4-4afd-9980-4bf529c541ea/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/63cb649d-d0a9-4c31-a6e1-882a2b262a08/FISS_AR_20240102.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5d1a8be3-1d4e-4d49-870d-fdcf2ca27846/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2024-01-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/3c512f2a-e2cd-41af-a988-d41b48cec9bf/FISS_AR_20231228.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/14ddd928-dbe5-470a-8a5a-55183b13494d/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/ca45f782-f275-44b1-9dcb-568aa8d21862/FISS_AR_20231226.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4041b8f9-b70b-4c82-94db-244bf7c123b3/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/416e9ade-3624-4a17-a833-6253d0602458/FISS_AR_20231221.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/65ade0ce-5255-40ea-8e22-b9dc790e406a/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/df86c744-b2c4-49c0-ba4f-ef6a245f0763/FISS_AR_20231218.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6709c6b9-5457-410d-a792-5797d7161e93/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/6d665cdb-a8bc-486f-ae1e-4872e5db13c8/FISS_AR_20231214.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/02cb5188-011c-4093-ae92-3570c287d7cc/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/2606f0c8-8c44-49d4-9b5b-12fbfeb3aa11/FISS_AR_20231211.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/1043fa1a-421c-40c1-ab63-0e087633823e/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/22ad40b0-f3b4-4762-8152-c6cf1ff3cc91/FISS_AR_20231207.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/b23c7720-893d-4e27-a961-f2738ffc8b3e/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/0d4f43c1-d87a-4d5a-bad3-f0fe4ddb3de4/FISS_AR_20231204.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4c00c6df-9ac6-4377-85b8-09d9c6b3dfe9/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/866d1d67-350b-4eb5-afcc-c064fdfbdf3e/FISS_AR_20231130.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/82e77c44-333c-4628-beaf-91d4c07ef86c/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/2ecb70a1-ba79-44cc-90ef-90b6da511bfa/FISS_AR_20231127.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/2d579af6-7f56-4dec-b704-2354643adc63/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/3e5e7c31-815b-4f1d-9b4f-75332dc8ab33/FISS_AR_20231122.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-24"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/1639daa6-6aba-47f2-bf13-74342b9ff295/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-24"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/44288098-b7f0-4c08-a859-eb414aae30cc/FISS_AR_20231120.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/46d2b756-d8db-40db-8813-e2ac9699414d/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/0b26df43-a784-46bd-9c4b-343695a4ef46/FISS_AR_20231116.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5e5934d3-450e-4879-8f25-a3c43f95f3ef/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/5369862b-10cd-4e8a-830a-f18400874712/FISS_AR_20231113.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6058c157-5c7b-4900-b88c-fc24a5680b11/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/7bea4994-86eb-4358-8d19-8f4e904baa15/FISS_AR_20231109.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/2001b9c2-40e3-48b8-b607-4442ba0a5ee5/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/60386412-33a8-4a3c-a3de-1168e4864d7b/FISS_AR_20231106.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/cbf0011d-1dcc-408c-a529-8392391ec3af/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/7e8b6d0c-ce01-4e1a-83db-2f0d42ad9fa0/FISS_AR_20231102.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e23c7d89-6145-4b28-a3a6-216168539210/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-11-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/adb4e76c-e40b-436a-a07c-7fe98b68a905/FISS_AR_20231030.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4f64860a-4368-451f-a9d9-ab4e4457f068/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/9c7f4293-3566-472e-9dc8-1700c29f6e9e/FISS_AR_20231026.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/07b5c392-bc7c-4b66-a137-cfe426bff5b1/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/11d68344-448e-441b-aae5-a94f9b125ef9/FISS_AR_20231023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-24"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c05911e3-563a-4c9d-bee0-09cea59de406/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-24"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/54f73849-e6ca-4b43-83f6-6a43a1751702/FISS_AR_20231019.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-20"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6300ac24-4179-4a28-a3f3-ed7b0a06b3c2/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-20"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/7f55df95-06da-43dd-a6b1-83675b8374f2/FISS_AR_20231016.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d77776bb-62af-4922-858a-a82ba52e4246/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/444e2e58-6e54-413b-ad82-1dc16799aa94/FISS_AR_20231012.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/fade2ff9-e520-4884-8bb2-3b3c7be9c493/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/d949a6e0-2b59-49f3-b7be-df365f5fe418/FISS_AR_20231010.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/da243d59-b3a9-476e-a5ee-dd5dbe4dc17e/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/26018faf-160e-4bd3-b4dc-3cd4a0dfdeb9/FISS_AR_20231005.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/deea52b2-15c9-4b1a-9fd6-c4341ebabffd/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/5722d2c3-4df5-4013-b6ee-ddd4b1408f35/FISS_AR_20231002.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3396dbb6-b1d7-45b1-a3c3-3630dbcceb10/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-10-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/0480c8e1-24c3-43e1-b903-99c313fcae46/FISS_AR_20230928.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d70c976f-4230-4aec-9b78-3d0ff9198beb/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/9e1f1758-68a3-403f-b2b4-7b324627a057/FISS_AR_20230925.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e935d254-2d9a-4c4c-a28d-a3b34a40e607/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/1790b083-a74b-4384-a159-0ad27a7ec9a7/FISS_AR_20230922.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3c818122-9568-4d6a-baaa-a43daf2dc241/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/77e071cc-85c0-4070-9356-290a06af2589/FISS_AR_20230918.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-18"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5b46146c-4c66-42e5-ad82-1ca04fb8c1b7/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-18"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/d1723766-78c0-4728-8aeb-88f73914be25/FISS_AR_20230914.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ba7475b5-6d9b-46e2-89f9-6af3a6ecd744/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/3a083201-d561-4ecf-99dd-65c699691057/FISS_AR_20230911.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7353bd93-8af0-42a5-afbd-c76bae3a54fc/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/87e8d43d-2963-4da5-b87c-3f291b0a5ba5/FISS_AR_20230907.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/b9e26fc2-6e71-4f80-8884-c25dabb74065/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/5557a921-897f-4d0a-a25b-0dedbdf3e0dd/FISS_AR_20230905.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/cff94111-e355-42e3-a8d2-7e62e6e2106d/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-09-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/76727c8a-fc6a-463b-aec7-17d735e93030/FISS_AR_20230831.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/b3492fcf-a0d6-4959-a0f5-6acbb2278e95/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/6b133a86-3942-4389-8d1d-30731b5ca966/FISS_AR_20230828.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d9f12e5e-cabe-4d60-9ae8-fbf6a18aff47/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/d2209779-b60d-4e3f-9ceb-bd1742e9f378/FISS_AR_20230824.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-24"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/11f057e9-b45c-4d70-8eef-5ccfe149542b/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-24"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/8032a92e-cd66-42ef-bf1d-4ffdcffd48e4/FISS_AR_20230821.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/27f9604f-1834-4a0c-8afe-75209d093134/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/b5e54be6-7197-470a-9f42-1ca548be71b6/FISS_AR_20230817.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/463f6d4a-fd18-481c-afc6-91d36324c94a/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/5eddf7e5-e5d6-4d27-99e9-b0c2d2c2345d/FISS_AR_20230814.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/cf9cc428-fc56-48bc-a9f8-2654f3e01328/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/9bb836a9-22bf-4c18-a0a9-877e6441a68f/FISS_AR_20230810.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-10"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ff182662-558a-473c-922e-a8511643e774/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-10"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/77f10360-3e72-4f39-9ff0-2fcbef0a1070/FISS_AR_20230807.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f10f0d1b-ef01-4f1c-be1a-9701e08f5b0a/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/303dae4e-0c48-4604-85f6-70e0a4a6759d/FISS_AR_20230803.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/095f84bf-4d74-461b-830b-5fcc5cae4144/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/f7034408-3ce3-445c-b192-80d4abc4462b/FISS_AR_20230731.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4e8a09af-97a2-4739-9588-cd47fd703872/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-08-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/4f291e6d-ee49-47a8-9acf-e1906d706a04/FISS_AR_20230727.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/24057976-4d92-46a7-9915-b12608a3768a/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/ba60902a-fecc-4f2a-9581-2c284c748eb5/FISS_AR_20230724.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-25"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/1fc70571-1bff-4836-b10e-54a99269b5ea/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-25"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/5cdf7dbc-548b-4652-9779-9dff44498851/FISS_AR_20230720.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/cffa589a-598f-4317-92b6-2f1f112fd7db/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/f5af0694-c617-453e-b277-60b754ece3c4/FISS_AR_20230718.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/46bc04b7-cbe9-4157-a9b8-8fb1a0af5c30/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/2d8239db-85c1-4567-86a5-a8d80f240604/FISS_AR_20230713.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/158adc21-0ef1-48da-abc0-269e5935c0fd/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/ec598333-7833-4946-a38b-5895bd976aa8/FISS_AR_20230710.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9e8afcac-8727-4615-892c-f9c2133c62dd/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/5971652b-0722-4a2b-8e83-362b3e95de09/FISS_AR_20230706.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/77ce886b-fcaf-4eef-8030-769e0ef55742/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/65af7fc2-99a0-4201-90e7-1ee069ae1a1b/FISS_AR_20230703.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/285e83bb-f153-4f8a-b386-5e6ad0a8aff2/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/4d551acd-94eb-4b94-a5c9-e28766e14f39/FISS_AR_20230629.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8934f94a-adaf-4192-b5ad-9d000e0e0a76/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-07-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/90e8edcb-3a1e-4455-a550-1fe3a405b989/FISS_AR_20230626.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4235e93e-331a-4345-95cb-b2af561a2b8c/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/746dc5f2-6fa0-4b3c-adc5-78b7cd98736b/FISS_AR_20230622.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/447ac2de-68bb-4364-a1e6-2d1449c69e42/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/130e8837-3776-4702-8bb3-0944979a9e66/FISS_AR_20230619.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-20"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8cb4c77e-c393-4841-a400-38e085a76f04/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-20"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/937d5f63-f6c8-4051-b972-3aec85ba12e3/FISS_AR_20230615.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f08341c9-ee08-497d-8799-4b8f09c3c4c7/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/d1042f3f-bf5d-410e-9e23-2bcdcb94fca6/FISS_AR_20230612.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5d281d1e-b906-4f5c-8c2f-4ab1bd97ea43/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/4d080649-e36d-490b-b4d6-15ec8e64d8b9/FISS_AR_20230608.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/01307335-54cb-4ee2-aa3e-944a61c80128/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/4b82df1a-619b-4f0c-a2f6-b4314697af6d/FISS_AR_20230601.csv",
+                    "mediaType": "text/csv",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3a59aa8b-46fb-4a5e-a255-c28494d53194/data",
+                    "mediaType": "text/html",
+                    "title": "Fiscal Intermediary Shared System Attending and Rendering : 2023-06-01"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/fiscal-intermediary-shared-system-attending-and-rendering-data-dictionary",
+            "dataQuality": true,
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P3.5D",
+            "theme": [
+                "Medicare"
+            ],
+            "language": [
+                "en-US"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/rwap-xbst",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-04-24",
+            "@type": "dcat:Dataset",
+            "modified": "2020-01-02",
+            "keyword": [
+                "2019",
+                "all ages",
+                "confirmed",
+                "invasive pneumococcal disease",
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
+            "identifier": "https://data.cdc.gov/api/views/rwap-xbst",
+            "description": "NNDSS - TABLE 1S. Invasive pneumococcal disease, all ages, Confirmed to Invasive pneumococcal disease, all ages, Probable - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 Includes drug resistant and susceptible cases of Invasive Pneumococcal Disease.",
+            "title": "NNDSS - TABLE 1S. Invasive pneumococcal disease, all ages, Confirmed to Invasive pneumococcal disease, all ages, Probable",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rwap-xbst/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rwap-xbst/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rwap-xbst/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rwap-xbst/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/dataset/2015-plan-selections-zip-code-health-insurance-marketplace",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2015-04-10",
+            "temporal": "2014-11-15T00:00:00-05:00/2015-02-22T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "administrative",
+                "marketplace enrollment  zip code  plan selections",
+                "population statistics"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Munira Gunja",
+                "hasEmail": "mailto:munira.gunja@hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Assistant Secretary for Planning & Evaluation, Department of Health & Human Services"
+            },
+            "identifier": "de6f60a0-e3d0-4b25-9601-701ff82d7e0e",
+            "description": "<p>The dataset here provides the total number of Qualified Health Plan selections by ZIP Code for 37 states for the second Health Insurance Marketplace open enrollment period (November 15, 2014 \u2013 February 15, 2015, including additional special enrollment period activity reported through February 22, 2015).</p>",
+            "title": "2015 Plan Selections by ZIP Code in the Health Insurance Marketplace",
+            "programCode": [
+                "009:072"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://aspe.hhs.gov/health/reports/2015/MarketPlaceEnrollment/EnrollmentByZip/feb2015_zipcode_enrollment.csv",
+                    "mediaType": "text/csv",
+                    "title": "CSV"
+                }
+            ],
+            "describedBy": "http://aspe.hhs.gov/health/reports/2015/MarketPlaceEnrollment/EnrollmentByZip/rpt_EnrollmentByZip_Apr2015.cfm",
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/data-visualization/mortality-trends/index.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2015-07-14",
+            "@type": "dcat:Dataset",
+            "temporal": "1950-01-01/2000-12-31",
+            "modified": "2022-03-23",
+            "keyword": [
+                "cause of death",
+                "mortality",
+                "nchs",
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
+            "identifier": "https://data.cdc.gov/api/views/mc4y-cbbv",
+            "description": "This dataset contains information on the number of deaths and age-adjusted death rates for the five leading causes of death in 1900, 1950, and 2000.\n\nAge-adjusted death rates (deaths per 100,000) after 1998 are calculated based on the 2000 U.S. standard population. Populations used for computing death rates for 2011\u20132017 are postcensal estimates based on the 2010 census, estimated as of July 1, 2010. Rates for census years are based on populations enumerated in the corresponding censuses. Rates for noncensus years between 2000 and 2010 are revised using updated intercensal population estimates and may differ from rates previously published. Data on age-adjusted death rates prior to 1999 are taken from historical data (see References below).\n\nSOURCES\n\nCDC/NCHS, National Vital Statistics System, historical data, 1900-1998 (see https://www.cdc.gov/nchs/nvss/mortality_historical_data.htm); CDC/NCHS, National Vital Statistics System, mortality data (see http://www.cdc.gov/nchs/deaths.htm); and CDC WONDER (see http://wonder.cdc.gov).\n\nREFERENCES\n\n1. National Center for Health Statistics, Data Warehouse. Comparability of cause-of-death between ICD revisions. 2008. Available from: http://www.cdc.gov/nchs/nvss/mortality/comparability_icd.htm.\n\n2. National Center for Health Statistics. Vital statistics data available. Mortality multiple cause files. Hyattsville, MD: National Center for Health Statistics. Available from: https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm.\n\n3. Kochanek KD, Murphy SL, Xu JQ, Arias E. Deaths: Final data for 2017. National Vital Statistics Reports; vol 68 no 9. Hyattsville, MD: National Center for Health Statistics. 2019. Available from: https://www.cdc.gov/nchs/data/nvsr/nvsr68/nvsr68_09-508.pdf.\n\n4. Arias E, Xu JQ. United States life tables, 2017. National Vital Statistics Reports; vol 68 no 7. Hyattsville, MD: National Center for Health Statistics. 2019. Available from: https://www.cdc.gov/nchs/data/nvsr/nvsr68/nvsr68_07-508.pdf.\n\n5. National Center for Health Statistics. Historical Data, 1900-1998. 2009. Available from: https://www.cdc.gov/nchs/nvss/mortality_historical_data.htm.",
+            "title": "NCHS - Top Five Leading Causes of Death: United States, 1990, 1950, 2000",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mc4y-cbbv/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mc4y-cbbv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mc4y-cbbv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mc4y-cbbv/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/d9iu-q3ng",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-08-06",
+            "@type": "dcat:Dataset",
+            "modified": "2024-08-14",
+            "keyword": [
+                "py2024",
+                "qhp",
+                "qhp landscape",
+                "shop",
+                "shop market medical"
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
+            "identifier": "e68d9ef0-549c-4fec-a91b-781eb865c60e",
+            "description": "The Medical SHOP Market file of the QHP Landscape Files contains information on certified medical plans offered through an Exchange to employers in the Small Business Health Options Program (SHOP) market. These plans are also known as Qualified Health Plans (QHPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
+            "title": "QHP Landscape PY2024 Medical SHOP",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2024/shop_market_medical.zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "restricted public",
+            "landingPage": "https://wwwn.cdc.gov/nchs/nhanes/search/DataPage.aspx?Component=LimitedAccess&Cycle=1959-1994",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
+            "issued": "2018-03-01",
+            "@type": "dcat:Dataset",
+            "temporal": "1971/1994",
+            "modified": "2023-04-17",
+            "references": [
+                "https://www.cdc.gov/nchs/nhanes/index.htm"
+            ],
+            "keyword": [
+                "health statistics",
+                "nchs",
+                "nhanes",
+                "nutrition",
+                "research-data-center",
+                "surveillance",
+                "survey"
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
+            "identifier": "https://data.cdc.gov/api/views/ic32-yq9m",
+            "description": "The <b> National Health and Nutrition Examination Survey</b> (NHANES) is designed to assess the health and nutritional status of adults and children in the United States. The survey is unique in that it combines interviews with standardized physical examinations and laboratory tests. <br>\nNHANES was conducted on a periodic basis from 1971 to 1994, including NHANES I (1971-1975), NHANES II (1976-1980), NHANES III (1988-1994), and a Hispanic Health and Nutrition Examination Survey (HHANES, 1982-1984). In 1999, NHANES became continuous and has been collecting data annually ever since. <br>\nAll of the NHANES programs utilized a stratified, multistage probability cluster design to provide a nationally representative sample of the U.S. civilian, noninstitutionalized population. The NHANES interview includes demographic, socioeconomic, dietary, and health-related questions. The examination component conducted in a mobile examination center consists of medical, dental, and physiological measurements, as well as the collection of biospecimens, such as blood and urine for laboratory testing.\n\nThis set of restricted data contains indirect identifying and/or sensitive information collected in <b>NHANES prior to 1999. </b>Please refer to the links below for additional data available from NHANES:\n<ul><li><a href=\"https://wwwn.cdc.gov/nchs/nhanes/Default.aspx\">NHANES Public Use Data at: https://wwwn.cdc.gov/nchs/nhanes/Default.aspx</a></li>\n<li><a href=\"https://data.cdc.gov/dataset/National-Health-and-Nutrition-Examination-Survey-N/9ixb-fwvy\">NHANES Restricted Data: 1999 - present at: https://data.cdc.gov/dataset/National-Health-and-Nutrition-Examination-Survey-N/9ixb-fwvy</a></li>\n<li><a href=\"https://data.cdc.gov/dataset/National-Health-and-Nutrition-Examination-Survey-N/hdx4-e4uu\">NHANES Genetic Restricted Data at: https://data.cdc.gov/dataset/National-Health-and-Nutrition-Examination-Survey-N/hdx4-e4uu</a></li>\n<li><a href=\"https://data.cdc.gov/dataset/3-NHANES-National-Youth-Fitness-Survey-NNYFS-Restr/5u84-m4rs\">NHANES National Youth Fitness Survey (NNYFS) Restricted Data at: https://data.cdc.gov/dataset/3-NHANES-National-Youth-Fitness-Survey-NNYFS-Restr/5u84-m4rs</a></li> </ul>\nPlease refer to the <a href=\"https://www.cdc.gov/nchs/nhanes/index.htm\">NHANES - National Health and Nutrition Examination Survey Homepage at: https://www.cdc.gov/nchs/nhanes/index.htm</a> for further details on the NHANES design, implementation, and data analysis.",
+            "title": "National Health and Nutrition Examination Survey (NHANES) Restricted Data: Prior to 1999",
+            "isPartOf": "https://wwwn.cdc.gov/nchs/nhanes/default.aspx",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html",
+                    "title": "National Health and Nutrition Examination Survey (NHANES) Restricted Data: Prior to 1999"
+                }
+            ],
+            "spatial": "United States",
+            "describedBy": "The NHANES samples were selected using complex, stratified, multistage probability cluster sampling designs.",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/ssz5-s49e",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-06-24",
+            "@type": "dcat:Dataset",
+            "modified": "2022-11-17",
+            "keyword": [
+                "haicviz",
+                "healthcare associated infections",
+                "mrsa",
+                "mssa",
+                "staphylococcus aureus"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "HAIC",
+                "hasEmail": "mailto:erib@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/ssz5-s49e",
+            "description": "<p>The healthcare-associated infection component of CDC\u2019s <a href=\"https://www.cdc.gov/ncezid/dpei/eip/index.html\" target=\"_blank\">EIP</a> engages a <a href=\"https://www.cdc.gov/ncezid/dpei/eip/eip-sites.html\" target=\"_blank\">network</a> of state health departments and their academic medical center partners to help answer critical questions about emerging HAI threats, advanced infection tracking methods, and antibiotic resistance in the United States. Information gathered through this activity will play a key role in shaping future policies and recommendations targeting HAI prevention. Click <a href=\"https://www.cdc.gov/hai/eip/saureus.html\" target=\"_blank\">here</a> to learn more about Invasive Staphylococcus aureus infections</p>\n\n<h3>Interpretation</h3>\n<ul><li>Data presented in HAICViz may differ from other HAIC publications since different datasets or methods may be used.</li><li>Small numbers for some topics or filters may make year to year changes difficult to interpret.</li><li>Since each infection may have unique characteristics, the information available to display differs by individual organism.</li></ul>\n\n<h3>More Details</h3>\n<ul><li><a href=\"https://www.cdc.gov/hai/eip/saureus.html#Methods\" target=\"_blank\">Methodology</a>: Find details about surveillance population, case determination, surveillance evaluation, and more.</li><li>Reports and Findings: Access <a href=\"https://www.cdc.gov/hai/eip/saureus.html#anchor_1611155585754\" target=\"_blank\">reports</a> or lists of <a href=\"https://www.cdc.gov/hai/eip/saureus.html#anchor_1611155777037\" target=\"_blank\">publications</a> using HAIC Invasive Staphylococcus aureus data</li></ul>",
+            "title": "HAICViz - iSA",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ssz5-s49e/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ssz5-s49e/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ssz5-s49e/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ssz5-s49e/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/damp-z9iv",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-11-12",
+            "@type": "dcat:Dataset",
+            "modified": "2021-11-10",
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
+            "identifier": "92b5948f-b32b-404c-ad28-ea83de8a324e",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20211101 to 20211107",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rpt-drugs-nov-20211101-to-20211107.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://pubchem.ncbi.nlm.nih.gov/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2012-05-30",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "api",
+                "chemistry physical",
+                "community health",
+                "dataset",
+                "organic chemicals"
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/t2ny-ab25",
+            "description": "PubChem contains the chemical structures of small organic molecules and information on their biological activities. PubChem includes substance information, compound structures, and bioactivity data in three primary databases, PCSubstance, PCCompound, and PCBioAssay, respectively. PubChem is integrated with Entrez, NCBI's primary search engine, and also provides compound neighboring, sub/superstructure, similarity structure, bioactivity data, and other searching features. Technical documentation at \thttp://pubchem.ncbi.nlm.nih.gov/help.html#faq",
+            "title": "PubChem",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://pubchemdocs.ncbi.nlm.nih.gov/power-user-gateway",
+                    "description": "The PubChem Power User Gateway (PUG) provides access to PubChem services via programmatic interfaces (REST, SOAP, . The basic design principle is straightforward. There is a single CGI (pug.cgi, referred to hereafter as simply PUG) that is the central gateway to multiple PubChem functions. PUG takes no URL arguments; all communication with PUG is through XML.",
+                    "@type": "dcat:Distribution",
+                    "title": "API - PubChem Power User Gateway (PUG)"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://pubchem.ncbi.nlm.nih.gov/standardize/standardize.cgi",
+                    "description": "Standardization in PubChem is the validation and determination of a unique chemical structure that is used to create a PubChem Compound from one or more submitted Substance records. Standardization is part of the PubChem Upload pipeline for submitted records with valid chemical structures. It allows PubChem to display one Compound page for aspirin (for example) that includes information from many submitted aspirin Substance records.",
+                    "@type": "dcat:Distribution",
+                    "title": "PubChem Standardization Service"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://pubchem.ncbi.nlm.nih.gov/search/search.cgi",
+                    "description": "PubChem Structure Search provides various chemical search types and options.",
+                    "@type": "dcat:Distribution",
+                    "title": "PubChem Structure Search - Query Interface"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://pubchem.ncbi.nlm.nih.gov/upload/#welcome",
+                    "description": "The PubChem Upload tool enables you to submit data to the PubChem Substance and PubChem BioAssay databases, or update your existing data, including chemical structures, experimental biological activity results, annotations, siRNA data and more. Once your submission is reviewed and published in PubChem, your data will be available for Open Access to the public around the world.",
+                    "@type": "dcat:Distribution",
+                    "title": "PubChem Upload"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/pcsubstance",
+                    "description": "The PubChem Substance Database contains descriptions of samples, from a variety of sources, and links to biological screening results that are available in PubChem BioAssay. If the chemical contents of a sample are known, the description includes links to PubChem Compound.",
+                    "@type": "dcat:Distribution",
+                    "title": "PubChem Substance"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/pccompound",
+                    "description": "The PubChem Compound Database contains validated chemical depiction information provided to describe substances in PubChem Substance. Structures stored within PubChem Compounds are pre-clustered and cross-referenced by identity and similarity groups.",
+                    "@type": "dcat:Distribution",
+                    "title": "PubChem Compound"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/pcassay",
+                    "description": "The PubChem BioAssay Database contains bioactivity screens of chemical substances described in PubChem Substance. It provides searchable descriptions of each bioassay, including descriptions of the conditions and readouts specific to that screening procedure.",
+                    "@type": "dcat:Distribution",
+                    "title": "PubChem BioAssay"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://pubchemdocs.ncbi.nlm.nih.gov/downloads",
+                    "mediaType": "text/html",
+                    "title": "Downloading PubChem Data"
+                }
+            ],
+            "license": "http://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "Drugs and Chemicals"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/dbdd-hhrf",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-04-08",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-13",
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
+            "identifier": "0833a46e-3155-5b38-a029-2d05abe6721c",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "Scorecard measure v2.11.18 (etl-test)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.18/20241107/measure.csv",
+                    "description": "Scorecard measure v2.11.18 (etl-test)",
+                    "@type": "dcat:Distribution",
+                    "title": "Scorecard measure v2.11.18 (etl-test)"
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
+            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/strong-start-for-mothers-and-newborns-initiative/strong-start-awardees",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2017-01-01/2017-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2023-05-12",
+            "references": [
+                "https://data.cms.gov/resources/strong-start-awardees-methodology"
+            ],
+            "keyword": [
+                "children's health insurance program",
+                "health care use & payments",
+                "medicaid",
+                "payment models",
+                "service delivery models",
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/9d4218d7-bb48-4278-964b-01755f0d8a85/data-viewer",
+            "description": "The Strong Start Awardees dataset provides information on the financial awards made to participants in the Strong Start for Mothers and Newborns Initiative. This initiative tested three evidence-based maternity care service approaches with the goal of improving health outcomes of pregnant women and newborns. The data can include the participant name, participant location, locations of practices participating under the participants\u2019 umbrella practice, descriptive text for the type(s) of enhanced prenatal care provided, and the amount of funding awarded to the participant as a result of their participation in year 1 of the initiative.",
+            "title": "Strong Start Awardees",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9d4218d7-bb48-4278-964b-01755f0d8a85/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Strong Start Awardees : 2017-09-25"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/5e378ec5-dfc9-4d07-9f73-53169b024245/Socrata-StrongStartAwardees_05-12-23-Fix-1.csv",
+                    "mediaType": "text/csv",
+                    "title": "Strong Start Awardees : 2017-09-25"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/647e8a75-2135-49a0-83a8-f3b12f687d18/data",
+                    "mediaType": "text/html",
+                    "title": "Strong Start Awardees : 2017-09-25"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/strong-start-awardees-data-dictionary",
+            "dataQuality": true,
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "Medicaid",
+                "Children's Health Insurance Program"
+            ],
+            "language": [
+                "en-US"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://api.ncbi.nlm.nih.gov/variation/v0/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-06-30",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "api",
+                "data specifications",
+                "genetics",
+                "genomics",
+                "molecular biology",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/jy6x-w83b",
+            "description": "This genetic variation services interconvert and transform short genetic variants between HGVS expressions,  VCF format, and the new SPDI (Sequence Position Deletion Insertion) format, based on alignment datasets used by ClinVar and dbSNP.  NOTE: This service is still in beta testing mode",
+            "title": "SPDI Variation Service",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://api.ncbi.nlm.nih.gov/variation/v0/",
+                    "description": "dbSNP provides bulk download in VCF and JSON at https://ftp.ncbi.nih.gov/snp/latest_release/ for users with a large number of RefSNPs (>100K) to process.  NOTE: This service is still in beta testing mode. Please limit your request rate to 1 request/second.  ",
+                    "@type": "dcat:Distribution",
+                    "title": "API"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Molecular biology/Genetics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-spending-by-drug/medicare-part-b-spending-by-drug",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2022-01-01/2022-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2024-06-13",
+            "references": [
+                "https://data.cms.gov/resources/medicare-part-b-spending-by-drug-methodology"
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/76a714ad-3a2c-43ac-b76d-9dadf8f7d890/data-viewer",
+            "description": "The Medicare Part B by Drug dataset presents information on spending for drugs administered in doctors\u2019 offices and other outpatient settings by physicians and other healthcare providers to Medicare Part B enrollees.\u00a0\n\nThe dataset focuses on average spending per dosage unit and change in average spending per dosage unit over time. It\u00a0also includes consumer-friendly descriptions of the drug uses, clinical indications, and manufacturer(s).\n\nDrug spending metrics for Part B drugs represent the full value of the product, including the Medicare payment and beneficiary liability. All Part B drug spending metrics are calculated at the HCPCS level.",
+            "title": "Medicare Part B Spending by Drug",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/76a714ad-3a2c-43ac-b76d-9dadf8f7d890/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Medicare Part B Spending by Drug : 2022-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/52fa5471-bf9a-4e84-b27c-84d8827408d6/DSD_PTB_RY24_P06_V10_DYT22_HCPCS-%20240201.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Part B Spending by Drug : 2022-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/be562dd4-34a0-4e1a-9cde-dcc58efde527/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Part B Spending by Drug : 2022-01-01"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/medicare-part-b-spending-by-drug-data-dictionary",
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
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/natality.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2016-08-03",
+            "@type": "dcat:Dataset",
+            "temporal": "2021-01-01/2024-09-30",
+            "modified": "2024-12-18",
+            "keyword": [
+                "birth rate",
+                "cesarean delivery",
+                "fertility rate",
+                "nchs",
+                "preterm birth",
+                "vital statistics rapid release",
+                "vsrr"
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
+            "identifier": "https://data.cdc.gov/api/views/76vv-a7x8",
+            "description": "Provisional estimates of selected reproductive indicators. Estimates are presented for: general fertility rates, age-specific birth rates, total and low risk cesarean delivery rates, preterm birth rates and other gestational age categories.",
+            "title": "NCHS - VSRR Quarterly provisional estimates for selected birth indicators",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/76vv-a7x8/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/76vv-a7x8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/76vv-a7x8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/76vv-a7x8/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P3M",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2020-10-21",
+            "temporal": "2020-01-01/2020-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2022-04-01",
+            "keyword": [
+                "age",
+                "age group",
+                "causes of death",
+                "chronic liver disease",
+                "chronic lower respiratory disease",
+                "cirrhosis",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "diabetes",
+                "hypertensive disease",
+                "kidney disease",
+                "major cardiovascular diseases",
+                "monthly",
+                "mortality",
+                "nchs",
+                "nvss",
+                "obesity",
+                "provisional",
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
+            "identifier": "https://data.cdc.gov/api/views/qdcb-uzft",
+            "description": "Provisional death counts of diabetes, coronavirus disease 2019 (COVID-19) and other select causes of death, by month, sex, and age.",
+            "title": "AH Provisional Diabetes Death Counts for 2020",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qdcb-uzft/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qdcb-uzft/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qdcb-uzft/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qdcb-uzft/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://meps.ahrq.gov",
+            "bureauCode": [
+                "009:33"
+            ],
+            "issued": "2021-02-13",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "agency-for-healthcare-research-and-quality-department-of-health-human-services",
+                "health care cost"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "MEPS Project Director",
+                "hasEmail": "mailto:mepsprojectdirector@ahrq.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Agency for Healthcare Research and Quality, Department of Health & Human Services"
+            },
+            "identifier": "0855a432-ecad-4c56-8734-76bac1184345",
+            "description": "The Medical Expenditure Panel Survey (MEPS) Household Component (HC) collects data from a sample of families and individuals in selected communities across the United States, drawn from a nationally representative subsample of households that participated in the prior year's National Health Interview Survey (conducted by the National Center for Health Statistics). During the household interviews, MEPS collects detailed information for each person in the household on the following: demographic characteristics, health conditions, health status, use of medical services, charges and source of payments, access to care, satisfaction with care, health insurance coverage, income, and employment. The panel design of the survey, which features several rounds of interviewing, makes it possible to determine how changes in respondents' health status, income, employment, eligibility for public and private insurance coverage, use of services, and payment for care are related. Public Use Files for Household data are available on the MEPS website.",
+            "title": "Medical Expenditure Panel Survey (MEPS) Household Component Public Use Files",
+            "programCode": [
+                "009:072"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://meps.ahrq.gov/mepsweb/data_stats/download_data_files.jsp",
+                    "mediaType": "text/html",
+                    "title": "Data, Codebook, and Documentation "
+                }
+            ],
+            "describedBy": "https://meps.ahrq.gov/mepsweb/data_stats/download_data_files.jsp"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.nlm.nih.gov/healthit/snomedct/index.html",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-06-30",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/aq5x-f2xa",
+            "description": "SNOMED CT is one of a suite of designated standards for use in U.S. Federal Government systems for the electronic exchange of clinical health information and is also a required standard in interoperability specifications of the U.S. Healthcare Information Technology Standards Panel.",
+            "title": "SNOMED CT",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.nlm.nih.gov/healthit/snomedct/index.html",
+                    "mediaType": "text/html",
+                    "title": "Download SNOMED CT Data"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Terminology"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://datatools.ahrq.gov/meps-hc",
+            "bureauCode": [
+                "009:33"
+            ],
+            "issued": "2022-06-03",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "agency for healthcare research and quality",
+                "agency-for-healthcare-research-and-quality-department-of-health-human-services",
+                "ahrq",
+                "expenditure",
+                "expenses",
+                "healthcare",
+                "household",
+                "medical expenditure",
+                "meps"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "MEPS Project Director",
+                "hasEmail": "mailto:mepsprojectdirector@ahrq.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Agency for Healthcare Research and Quality, Department of Health & Human Services"
+            },
+            "identifier": "https://healthdata.gov/api/views/de7f-8ncr",
+            "description": "The Medical Expenditure Panel Survey (MEPS) Household Component collects data on all members of sample households from selected communities across the United States. With the MEPS-HC Data Tools, users can explore trends and cross-sectional bar charts for nationally representative estimates of household medical utilization and expenditures, demographic and socioeconomic characteristics, health insurance coverage, accessibility and quality of care, treated medical conditions, and prescribed medicine purchases.",
+            "title": "Medical Expenditure Panel Survey (MEPS) Household Component Data Tools",
+            "programCode": [
+                "009:073"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datatools.ahrq.gov/meps-hc",
+                    "mediaType": "text/html",
+                    "title": "Query Tool"
+                }
+            ],
+            "describedBy": "https://datatools.ahrq.gov/meps-hc",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "National"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/jr4g-zdpg",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-01-21",
+            "@type": "dcat:Dataset",
+            "modified": "2022-01-12",
+            "keyword": [
+                "2021",
+                "meningococcal disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "other serogroups",
+                "unknown serogroup",
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
+            "identifier": "https://data.cdc.gov/api/views/jr4g-zdpg",
+            "description": "NNDSS - TABLE 1X. Meningococcal disease, Other serogroups to Meningococcal disease, Unknown serogroup - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1X. Meningococcal disease, Other serogroups to Meningococcal disease, Unknown serogroup",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/jr4g-zdpg/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/jr4g-zdpg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/jr4g-zdpg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/jr4g-zdpg/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/dfe6-ej4t",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2021-10-19",
+            "@type": "dcat:Dataset",
+            "modified": "2021-10-18",
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
+            "identifier": "e38a7952-47df-4d57-b75f-e2775fb854f1",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20211011 to 20211017",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rpt-drugs-sept-20211011-to-20211017.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/rsk8-spa7",
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
+                "non-congenital",
+                "wonder",
+                "yellow fever",
+                "zika virus disease"
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
+            "identifier": "https://data.cdc.gov/api/views/rsk8-spa7",
+            "description": "NNDSS - TABLE 1PP. Yellow fever to Zika virus disease, non-congenital \u2013 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1PP. Yellow fever to Zika virus disease, non-congenital",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rsk8-spa7/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rsk8-spa7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rsk8-spa7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rsk8-spa7/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://datatools.ahrq.gov",
+            "bureauCode": [
+                "009:33"
+            ],
+            "issued": "2022-06-03",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "agency-for-healthcare-research-and-quality-department-of-health-human-services",
+                "household",
+                "medical expenditure",
+                "meps"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "MEPS Project Director",
+                "hasEmail": "mailto:mepsprojectdirector@ahrq.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Agency for Healthcare Research and Quality, Department of Health & Human Services"
+            },
+            "identifier": "https://healthdata.gov/api/views/dfw3-qjdi",
+            "description": "The Medical Expenditure Panel Survey (MEPS) Household Component collects data on all members of sample households from selected communities across the United States. The MEPS-HC Variable Explorer Tool provides a quick and easy way to search across MEPS Public Use Files for variables and files needed for users' research projects.",
+            "title": "Medical Expenditure Panel Survey (MEPS) Household Component Variable Explorer",
+            "programCode": [
+                "009:072"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datatools.ahrq.gov/meps-hc#varexpLabel",
+                    "mediaType": "text/html",
+                    "title": "Query Tool"
+                }
+            ],
+            "describedBy": "https://datatools.ahrq.gov/meps-hc#varexpLabel"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/dg8p-t4kf",
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
+            "identifier": "7a7c087d-83f5-5056-94c9-6d479b7b7b49",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "Scorecard state v2.12.1-test (local)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.12.1-test/20241030/state.csv",
+                    "description": "Scorecard state v2.12.1-test (local)",
+                    "@type": "dcat:Distribution",
+                    "title": "Scorecard state v2.12.1-test (local)"
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
+            "landingPage": "https://data.cdc.gov/d/exs3-hbne",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-01-25",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-21",
+            "keyword": [
+                "age-adjusted",
+                "age group",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "mortality",
+                "race and ethnicity",
+                "sex"
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
+            "identifier": "https://data.cdc.gov/api/views/exs3-hbne",
+            "description": "Monthly COVID-19 death rates per 100,000 population stratified by age group, race/ethnicity, sex, and region, with race/ethnicity by age group and age group by race/ethnicity double stratification",
+            "title": "Monthly COVID-19 Death Rates per 100,000 Population by Age Group, Race and Ethnicity, Sex, and Region with Double Stratification",
+            "programCode": [
+                "009:026"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/exs3-hbne/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/exs3-hbne/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/exs3-hbne/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/exs3-hbne/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States",
+            "license": "https://www.usa.gov/government-works",
+            "theme": [
+                "Public Health Surveillance"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-1992",
+            "issued": "2016-05-23",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
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
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1992-nid13534",
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-1992)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1992-nid13534",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-1992) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1992-nid13534"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/cdi/overview.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-11-13",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-16",
+            "keyword": [
+                "alcohol",
+                "arthritis",
+                "asthma",
+                "cancer",
+                "copd",
+                "diabetes",
+                "tobacco"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CDC Info",
+                "hasEmail": "mailto:cdcinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/hksd-2xuw",
+            "description": "CDC's Division of Population Health provides a cross-cutting set of 115 indicators developed by consensus among CDC, the Council of State and Territorial Epidemiologists, and the National Association of Chronic Disease Directors.  These indicators allow states and territories to uniformly define, collect, and report chronic disease data that are important to public health practice in their area. In addition to providing access to state-specific indicator data, the CDI web site serves as a gateway to additional information and data resources.",
+            "title": "U.S. Chronic Disease Indicators",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hksd-2xuw/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hksd-2xuw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hksd-2xuw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hksd-2xuw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "Chronic Disease Indicators"
+            ]
+        },
+        {
+            "accessLevel": "restricted public",
+            "landingPage": "https://wwwn.cdc.gov/nchs/nhanes/search/nnyfsdata.aspx?Component=LimitedAccess",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
+            "issued": "2022-10-01",
+            "@type": "dcat:Dataset",
+            "temporal": "2012/2012",
+            "modified": "2023-04-17",
+            "references": [
+                "https://www.cdc.gov/nchs/nnyfs/index.htm"
+            ],
+            "keyword": [
+                "fitness",
+                "health statistics",
+                "nchs",
+                "nhanes",
+                "nnyfs",
+                "nutrition",
+                "physical activity",
+                "research-data-center",
+                "surveillance",
+                "survey"
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
+            "identifier": "https://data.cdc.gov/api/views/5u84-m4rs",
+            "description": "The <b>National Health and Nutrition Examination Survey\u2019s</b> (NHANES) <b>National Youth Fitness Survey</b> (NNYFS) was conducted in 2012 to collect nationally representative data on physical activity and fitness levels for U.S. children and adolescents aged 3-15 years, through household interviews and fitness tests conducted in mobile examination centers. <br>\nThe NNYFS interview includes demographic, socioeconomic, dietary, and health-related questions. The fitness tests included standardized measurements of core, upper, and lower body muscle strength, and gross motor skills, as well as a measurement of cardiovascular fitness by walking and running on a treadmill. A total of 1,640 children and adolescents aged 3-15 were interviewed and 1,576 were examined. <br>\nThis set of restricted data files contains indirect identifying and/or sensitive information collected in NNYFS. For NNYFS public use files, please visit <a href=\"https://wwwn.cdc.gov/nchs/nhanes/search/nnyfs12.aspx\">NNYFS 2012 at: https://wwwn.cdc.gov/nchs/nhanes/search/nnyfs12.aspx.</a>\nFor more information on the survey design, implementation, and data analysis, see the <a href=\"https://www.cdc.gov/nchs/nnyfs/analytic_guidelines.htm\"> NNYFS Analytic Guidelines at: https://www.cdc.gov/nchs/nnyfs/analytic_guidelines.htm.</a> \nFor more information on NHANES, visit the <a href=\"https://www.cdc.gov/nchs/nhanes/index.htm\"> NHANES - National Health and Nutrition Examination Survey Homepage at: https://www.cdc.gov/nchs/nhanes/index.htm.</a>",
+            "title": "NHANES National Youth Fitness Survey (NNYFS) Restricted Data",
+            "isPartOf": "https://wwwn.cdc.gov/nchs/nhanes/search/nnyfs12.aspx",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html",
+                    "title": "NHANES National Youth Fitness Survey (NNYFS) Restricted Data"
+                }
+            ],
+            "spatial": "United States",
+            "describedBy": "NNYFS was conducted concurrently with NHANES in 2012, the second year of the NHANES 2011\u20132012 cycle, with survey participants selected from an independent sample of dwelling units within the segments selected for that year of NHANES. The sample design has consisted of stratified, clustered four-stage probability sampling.",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/diu3-pej8",
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
+            "identifier": "9001e41d-13c2-589d-b62f-1712298c8c35",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "implAuto_measure_compare",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measure_compare.csv",
+                    "description": "{\"dataset\": \"measure_compare\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
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
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-06-15",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-25",
+            "references": [
+                "https://www.cdc.gov/places/measure-definitions/index.html"
+            ],
+            "keyword": [
+                "behaviors",
+                "brfss",
+                "census tract",
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
+            "identifier": "https://data.cdc.gov/api/views/nw2y-v4gm",
+            "description": "This dataset contains model-based census tract-level estimates for the PLACES 2022 release. PLACES covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. The dataset includes estimates for 29 measures: 13 for health outcomes, 9 for preventive services use, 4 for chronic disease-related health risk behaviors, and 3 for health status. These estimates can be used to identify emerging health problems and to help develop and carry out effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2020 or 2019 data, Census Bureau 2010 population data, and American Community Survey 2015\u20132019 estimates. The 2022 release uses 2020 BRFSS data for 25 measures and 2019 BRFSS data for 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, and cholesterol screening) that the survey collects data on every other year. More information about the methodology can be found at www.cdc.gov/places.",
+            "title": "PLACES: Local Data for Better Health, Census Tract Data 2022 release",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/nw2y-v4gm/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/nw2y-v4gm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/nw2y-v4gm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/nw2y-v4gm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-Census-Tract-D/cwsq-ngmh",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "500 Cities & Places"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/b5mu-3rk7",
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
+            "identifier": "https://data.cdc.gov/api/views/b5mu-3rk7",
+            "description": "Triclosan is an antimicrobial chemical incorporated into products that are applied to the skin of healthcare workers. Exposure to triclosan has previously been shown to be immunomodulatory and associated with allergic disease. Additionally, we have shown that exposure to triclosan dermally activates the NLRP3 inflammasome and disrupts the skin barrier integrity in mice. The skin is the largest organ in the body and plays an important role as a physical barrier and regulator of the immune system. Alterations in the barrier and immune regulatory functions of the skin have been demonstrated to increase the risk of sensitization and development of allergic disease. In this study, the impact of triclosan exposure on the skin barrier and keratinocyte function was investigated using a model of reconstructed human epidermis. The apical surface of reconstructed human epidermis was exposed to triclosan once for 6, 24, or 48 hours or daily for 5 consecutive days.",
+            "title": "Exposure to the antimicrobial chemical triclosan disrupts keratinocyte function and skin integrity in a model of reconstructed human epidermis",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/b5mu-3rk7/application/x-zip-compressed",
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
+            "landingPage": "https://healthdata.gov/dataset/fda-peanut-containing-product-recall-0",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2012-05-30",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "brownie",
+                "cake and pie",
+                "candy",
+                "cereal",
+                "cookie",
+                "cracker",
+                "donut",
+                "fda",
+                "federal widget",
+                "ice cream",
+                "national",
+                "peanut butter",
+                "pet food",
+                "product",
+                "product-recalls",
+                "recalls",
+                "safety",
+                "salmonella",
+                "snack bars"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration, Department of Health & Human Services"
+            },
+            "identifier": "178c1eb8-c2cc-4301-a3e1-b6ff1609b1a6",
+            "description": "<p>The FDA Peanut-Containing Product Recall widget allows you to browse the Food and Drug Administration (FDA) database of peanut butter and peanut-containing products subject to recall. This database makes it easier for you to determine whether any of the products you have at home are subject to recent recalls, and will be updated as new information becomes available.</p>",
+            "title": "FDA Peanut-Containing Product Recall",
+            "programCode": [
+                "009:001"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.cdc.gov/Widgets/#peanutrecall",
+                    "mediaType": "text/html",
+                    "title": "Widget "
+                }
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "National"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/aagc-37gx",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-04-26",
+            "@type": "dcat:Dataset",
+            "modified": "2019-05-30",
+            "keyword": [
+                "2019",
+                "meningococcal disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "other serogroups",
+                "unknown serogroup",
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
+            "identifier": "https://data.cdc.gov/api/views/aagc-37gx",
+            "description": "NNDSS - TABLE 1X. Meningococcal disease,  Other serogroups to Meningococcal disease, Unknown serogroup - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1X. Meningococcal disease,  Other serogroups to Meningococcal disease, Unknown serogroup",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/aagc-37gx/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/aagc-37gx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/aagc-37gx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/aagc-37gx/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/xm94-zmtx",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2020-05-28",
+            "@type": "dcat:Dataset",
+            "modified": "2021-07-07",
+            "keyword": [
+                "air pollution",
+                "asthma",
+                "environmental health",
+                "ozone"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Craig Kassinger",
+                "hasEmail": "mailto:trackingsupport@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/xm94-zmtx",
+            "description": "This dataset provides modeled predictions of ozone levels from the EPA's Downscaler model. Data are at the census tract level for 2006-2010. These data are used by the CDC's National Environmental Public Health Tracking Network to generate air quality measures. Census tract-level datasets contain estimates of the mean predicted concentration and associated standard error. Please refer to the metadata attachment for more information.\n\nLearn more about outdoor air quality on the Tracking Network's website: https://ephtracking.cdc.gov/showAirLanding.action.\n\nBy using these data, you signify your agreement to comply with the following requirements:\n1. Use the data for statistical reporting and analysis only.\n2. Do not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals.\n3. Do not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov.\n4. Do not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating.\n5. Acknowledge, in all reports or presentations based on these data, the original source of the data and CDC.\n6. Suggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking.",
+            "title": "Daily Census Tract-Level Ozone Concentrations, 2006-2010",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xm94-zmtx/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xm94-zmtx/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xm94-zmtx/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/xm94-zmtx/rows.xml?accessType=DOWNLOAD",
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
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1996",
+            "issued": "2016-05-23",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "alcohol abuse",
+                "alcohol consumption",
+                "amphetamines",
+                "barbiturates",
+                "cocaine",
+                "crime",
+                "demographic characteristics",
+                "drug abuse",
+                "drugs",
+                "drug use",
+                "hallucinogens",
+                "health care",
+                "health insurance",
+                "heroin",
+                "hiv",
+                "households",
+                "inhalants",
+                "marijuana",
+                "mental health",
+                "mental health services",
+                "methamphetamine",
+                "prescription drugs",
+                "smoking",
+                "stimulants",
+                "substance abuse",
+                "substance abuse treatment",
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
+            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1996-nid13564",
+            "description": "<p>This series measures the prevalence and correlates of drug<br />\nuse in the United States. The surveys are designed to provide<br />\nquarterly, as well as annual, estimates. Information is provided on<br />\nthe use of illicit drugs, alcohol, and tobacco among members of United<br />\nStates households aged 12 and older. Questions include age at first<br />\nuse as well as lifetime, annual, and past-month usage for the<br />\nfollowing drug classes: marijuana, cocaine (and crack), hallucinogens,<br />\nheroin, inhalants, alcohol, tobacco, and nonmedical use of<br />\nprescription drugs, including psychotherapeutics. Respondents were<br />\nalso asked about substance abuse treatment history, illegal<br />\nactivities, problems resulting from the use of drugs, personal and<br />\nfamily income sources and amounts, need for treatment for drug or<br />\nalcohol use, criminal record, and needle-sharing. Questions on mental<br />\nhealth and access to care, which were introduced in the 1994-B<br />\nquestionnaire (see NATIONAL HOUSEHOLD SURVEY ON DRUG ABUSE, 1994), were retained in this administration of the survey. In<br />\n1996, the section on risk/availability of drugs was reintroduced, and<br />\nsections on driving behavior and personal behavior were<br />\nadded. Demographic data include gender, race, age, ethnicity, marital<br />\nstatus, educational level, job status, income level, veteran status,<br />\nand current household composition.This study has 1 Data Set.</p>",
+            "title": "National Household Survey on Drug Abuse (NHSDA-1996)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1996-nid13564",
+                    "description": "National Household Survey on Drug Abuse (NHSDA-1996) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1996-nid13564"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.nlm.nih.gov/nichsr/hedges/search.html",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2022-02-08",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-05",
+            "keyword": [
+                "health services research",
+                "reference"
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/q6im-bymd",
+            "description": "Health Service Research (HSR) PubMed Queries contains preformulated specialized PubMed searches on healthcare quality and costs.",
+            "title": "Health Service Research (HSR) PubMed Queries",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.nlm.nih.gov/nichsr/hedges/search.html",
+                    "mediaType": "text/html",
+                    "title": "Health Service Research (HSR) PubMed Queries Homepage and Search"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Research"
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
+                "e-cigarette",
+                "legislation",
+                "licensure",
+                "osh",
+                "policy",
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
+            "identifier": "https://data.cdc.gov/api/views/ne52-uraz",
+            "description": "1995-2024. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System.  E-Cigarette Legislation\u2014Licensure. The STATE System houses current and historical state-level legislative data on tobacco use prevention and control policies.  Data are reported on a quarterly basis. Data include information related to requirements, restrictions and penalties associated with holding a retail license to sell e-cigarettes over-the-counter and through vending machines.",
+            "title": "CDC STATE System E-Cigarette Legislation - Licensure",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ne52-uraz/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ne52-uraz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ne52-uraz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ne52-uraz/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-E-Cigarette-Legislation-Licensure/ne52-uraz",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "theme": [
+                "Legislation"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/yrur-wghw",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-12-14",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-30",
+            "keyword": [
+                "age",
+                "age group",
+                "coronavirus",
+                "covid-19",
+                "death rate",
+                "deaths",
+                "hhs region",
+                "hispanic origin",
+                "monthly",
+                "mortality",
+                "nchs",
+                "nvss",
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
+            "identifier": "https://data.cdc.gov/api/views/yrur-wghw",
+            "description": "This file contains COVID-19 death counts and rates by month and year of death, jurisdiction of residence (U.S., HHS Region) and demographic characteristics (sex, age, race and Hispanic origin, and age/race and Hispanic origin). United States death counts and rates include the 50 states, plus the District of Columbia.\n\nDeaths with confirmed or presumed COVID-19, coded to ICD\u201310 code U07.1. Number of deaths reported in this file are the total number of COVID-19 deaths received and coded as of the date of analysis and may not represent all deaths that occurred in that period. Counts of deaths occurring before or after the reporting period are not included in the file.\n\nData during recent periods are incomplete because of the lag in time between when the death occurred and when the death certificate is completed, submitted to NCHS and processed for reporting purposes. This delay can range from 1 week to 8 weeks or more, depending on the jurisdiction and cause of death.\n\nDeath counts should not be compared across jurisdictions. Data timeliness varies by state. Some states report deaths on a daily basis, while other states report deaths weekly or monthly.\n\nThe ten (10) United States Department of Health and Human Services (HHS) regions include the following jurisdictions. Region 1: Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, Vermont; Region 2: New Jersey, New York; Region 3: Delaware, District of Columbia, Maryland, Pennsylvania, Virginia, West Virginia; Region 4: Alabama, Florida, Georgia, Kentucky, Mississippi, North Carolina, South Carolina, Tennessee; Region 5: Illinois, Indiana, Michigan, Minnesota, Ohio, Wisconsin; Region 6: Arkansas, Louisiana, New Mexico, Oklahoma, Texas; Region 7: Iowa, Kansas, Missouri, Nebraska; Region 8: Colorado, Montana, North Dakota, South Dakota, Utah, Wyoming; Region 9: Arizona, California, Hawaii, Nevada; Region 10: Alaska, Idaho, Oregon, Washington.\n\nRates were calculated using the population estimates for 2021, which are estimated as of July 1, 2021 based on the Blended Base produced by the US Census Bureau in lieu of the April 1, 2020 decennial population count. The Blended Base consists of the blend of Vintage 2020 postcensal population estimates, 2020 Demographic Analysis Estimates, and 2020 Census PL 94-171 Redistricting File (see https://www2.census.gov/programs-surveys/popest/technical-documentation/methodology/2020-2021/methods-statement-v2021.pdf).\n\nRate are based on deaths occurring in the specified week and are age-adjusted to the 2000 standard population using the direct method (see https://www.cdc.gov/nchs/data/nvsr/nvsr70/nvsr70-08-508.pdf). These rates differ from annual age-adjusted rates, typically presented in NCHS publications based on a full year of data and annualized weekly age-adjusted rates which have been adjusted to allow comparison with annual rates. Annualization rates presents deaths per year per 100,000 population that would be expected in a year if the observed period specific (weekly) rate prevailed for a full year.\n\nSub-national death counts between 1-9 are suppressed in accordance with NCHS data confidentiality standards. Rates based on death counts less than 20 are suppressed in accordance with NCHS standards of reliability as specified in NCHS Data Presentation Standards for Proportions (available from: https://www.cdc.gov/nchs/data/series/sr_02/sr02_175.pdf.).",
+            "title": "Provisional COVID-19 death counts and rates by month, jurisdiction of residence, and demographic characteristics",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yrur-wghw/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yrur-wghw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yrur-wghw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yrur-wghw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1W",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "restricted public",
+            "landingPage": "https://www.cdc.gov/nchs/npals/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/application-process/submission.html",
+            "issued": "2022-06-16",
+            "@type": "dcat:Dataset",
+            "temporal": "2020-01-01/2021-07-21",
+            "modified": "2025-01-13",
+            "keyword": [
+                "adult day services centers",
+                "covid-19",
+                "long-term care",
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
+            "identifier": "https://data.cdc.gov/api/views/xqjn-3jef",
+            "description": "The National Post-acute and Long-term Care Study (NPALS) is a biennial study of major post-acute and long-term care providers and their services users. Seven provider settings are in included. NPALS collects survey data on the residential care community and adult day services sectors, and uses administrative data (available from CMS) for home health, nursing home, hospice, inpatient rehabilitation, and long-term care hospital sectors.\nThe goals of the study are to: estimate the supply of paid, regulated post-acute and long-term care services providers; estimate key policy-relevant characteristics and practices of these providers; estimate the number of post-acute and long-term care services users; estimate key policy-relevant characteristics of these users; produce national and state estimates where feasible; compare across provider sectors; and monitor trends over time.",
+            "title": "National Post-acute and Long-term Care Study: Adult Day Service Provider Restricted Dataset",
+            "describedByType": "application/pdf",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "mediaType": "text/html",
+                    "title": "National Post-acute and Long-term Care Study: Adult Day Service Provider Restricted Dataset"
+                }
+            ],
+            "spatial": "United States",
+            "describedBy": "https://www.cdc.gov/nchs/data/npals/2020-NPALS-ADSC-Questionnaire-Center.pdf",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "Irregular",
+            "theme": [
+                "NCHS"
+            ],
+            "language": [
+                "en-US"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/dngx-euui",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2017-12-09",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-16",
+            "keyword": [
+                "bho",
+                "comprehensive mco",
+                "managed care enrollment",
+                "mco",
+                "medicaid",
+                "medicare",
+                "mltss",
+                "pace",
+                "pahp",
+                "pccm",
+                "pihp"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Jeff Chamblee",
+                "hasEmail": "mailto:Medicaid.gov@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "0bef7b8a-c663-5b14-9a46-0b5c2b86b0fe",
+            "description": "The Medicaid Managed Care Enrollment Report profiles enrollment statistics on Medicaid managed care programs on a plan-specific level. The managed care enrollment statistics include enrollees receiving comprehensive benefits and limited benefits and are point-in-time counts.\r\n\r\n1. The information in this table was provided by state officials. In some cases, program or plan names in this table differ from those used in publicly available sources. Questions regarding state-specific information in this table should be directed to State/territorial Medicaid officials.",
+            "title": "Managed Care Enrollment by Program and Plan",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/managed-care-enrollment-by-program-and-plan2022.csv",
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
+            "landingPage": "https://healthdata.gov/d/dnzj-fmps",
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
+            "identifier": "49948457-e2d0-55a4-be39-82f0de8d72e1",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "CoreSEt measure_value v2.10.14 (coreset-dev)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.14/20241029/measure_value.csv",
+                    "description": "CoreSEt measure_value v2.10.14 (coreset-dev)",
+                    "@type": "dcat:Distribution",
+                    "title": "CoreSEt measure_value v2.10.14 (coreset-dev)"
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
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-07-18",
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
+                "brfss",
+                "census",
+                "cities",
+                "outcomes",
+                "prevalence",
+                "prevention",
+                "tracts",
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
+            "identifier": "https://data.cdc.gov/api/views/rja3-32tc",
+            "description": "This is the complete dataset for the 500 Cities project 2018 release. This dataset includes 2016, 2015 model-based small area estimates for 27 measures of chronic disease related to unhealthy behaviors (5), health outcomes (13), and use of preventive services (9). Data were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. It represents a first-of-its kind effort to release information on a large scale for cities and for small areas within those cities. It includes estimates for the 500 largest US cities and approximately 28,000 census tracts within these cities. These estimates can be used to identify emerging health problems and to inform development and implementation of effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these measures include Behavioral Risk Factor Surveillance System (BRFSS) data (2016, 2015), Census Bureau 2010 census population data, and American Community Survey (ACS) 2012-2016, 2011-2015 estimates. Because some questions are only asked every other year in the BRFSS, there are 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, cholesterol screening) from the 2015 BRFSS that are the same in the 2018 release as the previous 2017 release. More information about the methodology can be found at www.cdc.gov/500cities.",
+            "title": "500 Cities: Local Data for Better Health, 2018 release",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rja3-32tc/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rja3-32tc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rja3-32tc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rja3-32tc/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/dpeb-iic2",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2022-10-07",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-14",
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
+            "identifier": "f45f35c5-7aa4-4500-b196-ae7833717add",
+            "description": "Clotting Factor (CF) designation allows for a minimum rebate percentage of 17.1 percent of Average Manufacturer Price (AMP) for single source and innovator multiple source drugs.",
+            "title": "Clotting Factor Drug Report",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/cf-drug-report-01132025.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/dqff-mbxx",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2025-01-08",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-06",
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
+            "identifier": "c1561c13-1ed6-430f-8d88-7d8cbea6d083",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 12-30-2024-to-01-05-2025",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/mdrp-newly-rprt-drug-12-30-2024-to-01-05-2025.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 12-30-2024-to-01-05-2025"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/ksf9-pem2",
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
+            "identifier": "https://data.cdc.gov/api/views/ksf9-pem2",
+            "description": "Rate of deaths by age/gender (per 100,000 population) for people killed in crashes involving a driver with BAC =>0.08%, 2012, 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File. Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
+            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, Region 1 - Boston",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ksf9-pem2/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ksf9-pem2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ksf9-pem2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ksf9-pem2/rows.xml?accessType=DOWNLOAD",
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
+            "issued": "2020-09-04",
+            "@type": "dcat:Dataset",
+            "modified": "2022-04-01",
+            "keyword": [
+                "age",
+                "age group",
+                "all causes",
+                "alzheimer disease",
+                "cancer",
+                "causes of death",
+                "cerebrovascular disease",
+                "chronic lower respiratory disease",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "diabetes",
+                "diseases of heart",
+                "hispanic origin",
+                "influenza",
+                "kidney disease",
+                "monthly",
+                "mortality",
+                "natural cause",
+                "nchs",
+                "nvss",
+                "pneumonia",
+                "provisional",
+                "race",
+                "respiratory disease",
+                "septicemia",
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
+            "identifier": "https://data.cdc.gov/api/views/65mz-jvh5",
+            "description": "Provisional counts of deaths by the month the deaths occurred, by age group, sex, and race/ethnicity, for select underlying causes of death for 2020-2021. Final data are provided for 2019. The dataset also includes monthly provisional counts of death for COVID-19, coded to ICD-10 code U07.1 as an underlying or multiple cause of death.",
+            "title": "AH Monthly Provisional Counts of Deaths for Select Causes of Death by Sex, Age, and Race and Hispanic Origin",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/65mz-jvh5/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/65mz-jvh5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/65mz-jvh5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/65mz-jvh5/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "http://www.fda.gov/Drugs/InformationOnDrugs/ucm135162.htm",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2013-08-29",
+            "keyword": [
+                "bmis",
+                "cder"
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
+            "identifier": "8d346d8d-33c7-47f8-890d-a4ced16e45dd",
+            "description": "This contains information that identifies clinical investigators, contract research organizations, and institutional review boards involved in the conduct of Investigational New Drug (IND) studies with human investigational drugs and therapeutic biologics.",
+            "title": "Bioresearch Monitonoring Information System (BMIS)",
+            "programCode": [
+                "009:002"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fda.gov/downloads/Drugs/InformationOnDrugs/UCM135169.zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.cdc.gov/oralhealth/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-07-14",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-25",
+            "references": [
+                "https://www.cdc.gov/oralhealthdata/"
+            ],
+            "keyword": [
+                "division of oral health",
+                "healthy people",
+                "nohss",
+                "oral health",
+                "water fluoridation",
+                "wfrs"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Oral Health Inquiries",
+                "hasEmail": "mailto:oralhealth@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/8235-5d73",
+            "description": "2000-2018. Water Fluoridation Statistics is a biennial report of the percentage and number of people receiving fluoridated water from 2000 through 2018, originally published at http://www.cdc.gov/fluoridation/statistics/index.htm. For more information, see: http://www.cdc.gov/oralhealthdata/overview/fluoridation_indicators.html",
+            "title": "Water Fluoridation Statistics - Percent of PWS population receiving fluoridated water",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8235-5d73/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8235-5d73/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8235-5d73/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8235-5d73/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Oral-Health/Water-Fluoridation-Statistics-Percent-of-PWS-popul/8235-5d73",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "theme": [
+                "Oral Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/b36e-ru3r",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2015-01-08",
+            "@type": "dcat:Dataset",
+            "modified": "2015-08-27",
+            "keyword": [
+                "2014",
+                "cryptosporidiosis",
+                "dengue fever",
+                "dengue hemorrhagic fever",
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
+            "identifier": "https://data.cdc.gov/api/views/b36e-ru3r",
+            "description": "NNDSS - Table II. Cryptosporidiosis to Dengue Hemorrhagic Fever - 2014.In this Table, all conditions with a 5-year average annual national total of more than or equals 1,000 cases but less than or equals 10,000 cases will be displayed (\ufffd\ufffd\ufffd 1,000 and \ufffd\ufffd_ 10,000). The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories. Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnotes:C.N.M.I.: Commonwealth of Northern Mariana Islands. U: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable    Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum. * Case counts for reporting years 2013 and 2014 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly. \ufffd\ufffd\ufffd Dengue Fever includes cases that meet criteria for Dengue Fever with hemorrhage, other clinical, and unknown case classifications. \ufffd\ufffd DHF includes cases that meet criteria for dengue shock syndrome (DSS), a more severe form of DHF.More information on NNDSS is available at http://wwwn.cdc.gov/nndss/.",
+            "title": "NNDSS - Table II. Cryptosporidiosis to Dengue Hemorrhagic Fever",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/b36e-ru3r/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/b36e-ru3r/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/b36e-ru3r/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/b36e-ru3r/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/dv46-8qnu",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2022-08-12",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-21",
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
+            "identifier": "200c2cba-e58d-4a95-aa60-14b99736808d",
+            "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
+            "title": "State Drug Utilization Data 2022",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/SDUD2022.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y",
+            "theme": [
+                "State Drug Utilization"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.ncbi.nlm.nih.gov/Structure/cdd/wrpsb.cgi",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-06-30",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-04",
+            "keyword": [
+                "computational biology",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/j6ef-yjai",
+            "description": "Identifies the conserved domains present in a protein sequence. CD-Search uses RPS-BLAST (Reverse Position-Specific BLAST) to compare a query sequence against position-specific score matrices that have been prepared from conserved domain alignments present in the Conserved Domain Database (CDD).",
+            "title": "CD Search (Conserved Domain Search Service)",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/Structure/cdd/wrpsb.cgi",
+                    "mediaType": "text/html",
+                    "title": "Conserved Domain Search Service (CD Search) Homepage and Search"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Molecular biology/Genetics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "rights": "N/A",
+            "bureauCode": [
+                "009:20"
+            ],
+            "landingPage": "N/A",
+            "issued": "2024-12-23",
+            "temporal": "N/A",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-29",
+            "references": [
+                "NHSN Hospital Respiratory Data (HRD) Reporting: https://www.cdc.gov/nhsn/psc/hospital-respiratory-reporting.html  NHSN Hospital Respiratory Data (HRD) Dashboard: https://wwwdev.cdc.gov/nhsn/psc/hospital-respiratory-dashboard.html#anchor_83745   Centers for Medicare and Medicaid Services (CMS) requirements: Updates to the Condition of Participation (CoP) Requirements for Hospitals and Critical Access Hospitals (CAHs) To Report Acute Respiratory Illnesses."
+            ],
+            "keyword": [
+                "admissions",
+                "coronavirus",
+                "covid19",
+                "hospital capacity",
+                "hospitalizations",
+                "hospital occupancy",
+                "icu beds",
+                "influenza",
+                "inpatient beds",
+                "respiratory",
+                "respiratory syncytial virus",
+                "rsv"
+            ],
+            "conformsTo": "N/A",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DHQP",
+                "hasEmail": "mailto:nhsn@cdc.gov"
+            },
+            "identifier": "https://data.cdc.gov/api/views/mpgq-jmmr",
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "description": "This dataset represents preliminary weekly hospital respiratory data and metrics aggregated to national and state/territory levels reported to CDC\u2019s National Health Safety Network (NHSN) beginning August 2020. This dataset updates weekly on Wednesdays with preliminary data reported to NHSN for the previous reporting week (Sunday \u2013 Saturday). \n\nData for reporting dates through April 30, 2024 represent data reported during a previous mandated reporting period as specified by the HHS Secretary. Data for reporting dates May 1, 2024 \u2013 October 31, 2024 represent voluntarily reported data in the absence of a mandate. Data for reporting dates beginning November 1, 2024 represent data reported during a current mandated reporting period. All data and metrics capturing information on respiratory syncytial virus (RSV) were voluntarily reported until November 1, 2024. All data included in this dataset represent aggregated counts, and include metrics capturing information specific to hospital capacity, occupancy, hospitalizations, and new hospital admissions with corresponding metrics indicating reporting coverage for a given reporting week. NHSN monitors national and local trends in healthcare system stress and capacity for all acute care and critical access hospitals in the United States.\n\nFor more information on the reporting mandate per the Centers for Medicare and Medicaid Services (CMS) requirements, visit: <a href=\"https://www.cms.gov/medicare/health-safety-standards/quality-safety-oversight-general-information/policy-memos-states/updates-condition-participation-cop-requirements-hospitals-and-critical-access-hospitals-cahs-report\"> Updates to the Condition of Participation (CoP) Requirements for Hospitals and Critical Access Hospitals (CAHs) To Report Acute Respiratory Illnesses</a>.\n\nFor more information regarding NHSN\u2019s collection of these data, including full reporting guidance, visit: <a href=\"https://www.cdc.gov/nhsn/psc/hospital-respiratory-reporting.html\">NHSN Hospital Respiratory Data</a>. \n\nFor data that is considered final for a given reporting week (Sunday \u2013 Saturday), and reflects that which is used in <a href=\"https://www.cdc.gov/nhsn/psc/hospital-respiratory-dashboard.html\">NHSN HRD dashboards</a> for publication each Friday, visit: <a href=\"https://data.cdc.gov/Public-Health-Surveillance/Weekly-Hospital-Respiratory-Data-HRD-Metrics-by-Ju/ua7e-t2fy/about_data\">https://data.cdc.gov/Public-Health-Surveillance/Weekly-Hospital-Respiratory-Data-HRD-Metrics-by-Ju/ua7e-t2fy/about_data</a>. \n\nCDC coordinates weekly forecasts of hospitalization admissions based on this data set. More information about flu forecasting can be found at <a href=\"https://www.cdc.gov/flu-forecasting/about/index.html\">About Flu Forecasting | FluSight | CDC</a>, and information about COVID-19 forecasting and other modeling analyses for the Respiratory Virus Season are available at <a href=\"https://www.cdc.gov/forecast-outbreak-analytics/our-work/respiratory-virus-season-insights.html\">CFA's Insights for Respiratory Virus Season | CFA | CDC</a>.\n\n<b>Source: CDC National Healthcare Safety Network (NHSN).</b> <ul><li><b>Data source description</b> (updated November 15, 2024): As of October 9, 2024, Hospital Respiratory Data (HRD; formerly Respiratory Pathogen, Hospital Capacity, and Supply data or 'COVID-19 hospital data') are reported to HHS through CDC's National Healthcare Safety Network (NHSN) based on updated requirements from the Centers for Medicare and Medicaid Services (CMS). These data were voluntarily reported to NHSN May 1, 2024 until November 1, 2024, at which time CMS began requiring acute care and critical access hospitals to electronically report information via NHSN about COVID-19, influenza, and RSV, hospital bed census and capacity. Hospital bed capacity and occupancy data for all patients and for patients with COVID-19 or influenza for collection dates prior to May 1, 2024, represent data reported during a previously mandated reporting",
+            "title": "Weekly Hospital Respiratory Data (HRD) Metrics by Jurisdiction, National Healthcare Safety Network (NHSN) (Preliminary)",
+            "isPartOf": "N/A",
+            "primaryITInvestmentUII": "N/A",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mpgq-jmmr/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mpgq-jmmr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mpgq-jmmr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mpgq-jmmr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "US",
+            "describedBy": "N/A",
+            "license": "https://www.usa.gov/government-works",
+            "systemOfRecords": "N/A",
+            "theme": [
+                "Public Health Surveillance"
+            ],
+            "accrualPeriodicity": "Weekly",
+            "language": [
+                "English"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/covid19/pulse/long-covid.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-06-22",
+            "@type": "dcat:Dataset",
+            "temporal": "2022-06-01/2024-09-16",
+            "modified": "2024-10-04",
+            "keyword": [
+                "covid-19",
+                "post-covid"
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
+            "identifier": "https://data.cdc.gov/api/views/gsea-w83j",
+            "description": "As part of an ongoing partnership with the Census Bureau, the National Center for Health Statistics (NCHS) recently added questions to assess the prevalence of post-COVID-19 conditions (long COVID), on the experimental Household Pulse Survey. This 20-minute online survey was designed to complement the ability of the federal statistical system to rapidly respond and provide relevant information about the impact of the coronavirus pandemic in the U.S. Data collection began on April 23, 2020. Beginning in Phase 3.5 (on June 1, 2022), NCHS included questions about the presence of symptoms of COVID that lasted three months or longer. Phase 3.5 will continue with a two-weeks on, two-weeks off collection and dissemination approach. \n\nEstimates on this page are derived from the Household Pulse Survey and show the percentage of adults aged 18 and over who a) as a proportion of the U.S. population, the percentage of adults who EVER experienced post-COVID conditions (long COVID). These adults had COVID and had some symptoms that lasted three months or longer; b) as a proportion of adults who said they ever had COVID, the percentage who EVER experienced post-COVID conditions; c) as a proportion of the U.S. population, the percentage of adults who are CURRENTLY experiencing post-COVID conditions. These adults had COVID, had long-term symptoms, and are still experiencing symptoms; d) as a proportion of adults who said they ever had COVID, the percentage who are CURRENTLY experiencing post-COVID conditions; and e) as a proportion of the U.S. population, the percentage of adults who said they ever had COVID.",
+            "title": "Post-COVID Conditions",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gsea-w83j/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gsea-w83j/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gsea-w83j/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gsea-w83j/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "U.S.",
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
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-spending-by-drug/medicare-part-d-spending-by-drug",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2022-01-01/2022-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2024-06-13",
+            "references": [
+                "https://data.cms.gov/resources/medicare-part-d-spending-by-drug-methodology"
+            ],
+            "keyword": [
+                "drugs",
+                "medical suppliers & equipment",
+                "medicare",
+                "medicare prescription drug"
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/7e0b4365-fd63-4a29-8f5e-e0ac9f66a81b/data-viewer",
+            "description": "The Medicare Part D by Drug dataset presents information on spending for drugs prescribed to Medicare beneficiaries enrolled in Part D by physicians and other healthcare providers. Drugs prescribed in the Medicare Part D program are drugs patients generally administer themselves.\n\n\u00a0\n\nThe dataset focuses on average spending per dosage unit and change in average spending per dosage unit over time. It\u00a0also includes spending information for manufacturer(s) of the drugs as well as consumer-friendly information of drug uses and clinical indications.\n\n\u00a0\n\nDrug spending metrics for Part D drugs are based on the gross drug cost, which represents total spending for the prescription claim, including Medicare, plan, and beneficiary payments. The Part D spending metrics do not reflect any manufacturers\u2019 rebates or other price concessions as CMS is prohibited from publicly disclosing such information.",
+            "title": "Medicare Part D Spending by Drug",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7e0b4365-fd63-4a29-8f5e-e0ac9f66a81b/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Medicare Part D Spending by Drug : 2022-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/663f0dab-d621-41c5-9130-dc9ce1beecf2/DSD_PTD_RY24_P04_V10_DY22_BGM.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Part D Spending by Drug : 2022-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/87604795-a3e2-4190-9b3a-e39142221fcd/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Part D Spending by Drug : 2022-01-01"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/medicare-part-d-spending-by-drug-data-dictionary",
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
+            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "National Center for Health Statistics",
+            "issued": "2024-07-22",
+            "@type": "dcat:Dataset",
+            "temporal": "1988/2020",
+            "modified": "2024-10-11",
+            "keyword": [
+                "chronic conditions",
+                "female",
+                "health us",
+                "high blood pressure",
+                "hispanic",
+                "hypertension",
+                "male",
+                "mexican",
+                "national health and nutrition examination survey",
+                "nhanes",
+                "non-hispanic asian",
+                "non-hispanic black",
+                "non-hispanic white",
+                "poverty level",
+                "sdoh-access-to-health-care",
+                "sdoh-poverty-income",
+                "sdoh-use-of-health-care"
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
+            "identifier": "https://data.cdc.gov/api/views/c49c-tp7w",
+            "description": "Data on hypertension in adults age 20 and older in the United States, by selected characteristics. Data are from Health, United States. SOURCE: National Center for Health Statistics, National Health and Nutrition Examination Survey.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
+            "title": "DQS Hypertension in adults age 20 and older, by selected characteristics: United States.",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/c49c-tp7w/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/c49c-tp7w/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/c49c-tp7w/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/c49c-tp7w/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "Annual (R/P1Y)",
+            "theme": [
+                "National Center for Health Statistics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/dataset/aid-families-dependent-children-quality-control-review-panel-decisions-0",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2012-05-30",
+            "temporal": "1991-08-09T00:00:00-04:00/1996-09-16T00:00:00-04:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "acf",
+                "administrative",
+                "adopt",
+                "afdc",
+                "affirm",
+                "appeal",
+                "appellate",
+                "assessment",
+                "assistance",
+                "award",
+                "balance",
+                "beneficiary",
+                "benefit",
+                "billing",
+                "board",
+                "cancellation",
+                "charge",
+                "children",
+                "code",
+                "collect",
+                "compliance",
+                "control",
+                "cost",
+                "coverage",
+                "crd",
+                "dab",
+                "debar",
+                "debt",
+                "decision",
+                "denial",
+                "determination",
+                "disallowance",
+                "disapprove",
+                "discontinution",
+                "eligibility",
+                "enforcement",
+                "enrollment",
+                "exclusion",
+                "expenditure",
+                "fiscal",
+                "food stamp",
+                "funding",
+                "grant",
+                "health care",
+                "hearing",
+                "income",
+                "invalid",
+                "judge",
+                "law",
+                "marketing",
+                "misconduct",
+                "modify",
+                "non-compliance",
+                "overpayment",
+                "participation",
+                "patient",
+                "payment",
+                "penalty",
+                "quality",
+                "recipient",
+                "reduction",
+                "repay",
+                "rescind",
+                "reverse",
+                "review",
+                "sanction",
+                "schip",
+                "ssa",
+                "ssn",
+                "tanf",
+                "termination",
+                "underpayment",
+                "violation",
+                "welfare",
+                "withold"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Debbie Nobelman",
+                "hasEmail": "mailto:Debbie.Nobleman@hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Departmental Appeals Board"
+            },
+            "identifier": "094cdb8f-68b1-4634-aa79-b3ba578488b3",
+            "description": "<p>Decisions issued by the Aid to Families with Dependent Children (AFDC) Quality Control Review Panel of the Departmental Appeals Board concerning the AFDC program (predecessor of Temporary Aid for Needy Families) established by title IV-A of the Social Security Act.</p>",
+            "title": "Aid to Families with Dependent Children Quality Control Review Panel Decisions",
+            "programCode": [
+                "009:102"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.hhs.gov/dab/decisions/index.html",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "describedBy": "http://www.hhs.gov/dab/decisions/afdcquality/index.html",
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "Health",
+                "Quality"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/jnru-aqxk",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-05-17",
+            "@type": "dcat:Dataset",
+            "temporal": "August 1, 2020 to June 30, 2022",
+            "modified": "2024-05-17",
+            "references": [
+                "Zviedrite N",
+                "Jahan F",
+                "Moreland S",
+                "Ahmed F",
+                "Uzicanin A. COVID-19\u2013Related School Closures",
+                "United States",
+                "July 27",
+                "2020\u2013June 30",
+                "2022. Emerg Infect Dis. 2024;30(1):58-69. https://doi.org/10.3201/eid3001.231215"
+            ],
+            "keyword": [
+                "community mitigation",
+                "covid-19",
+                "emergency preparedness",
+                "pandemic",
+                "pandemic preparedness",
+                "school closure"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Nicole Zviedrite",
+                "hasEmail": "mailto:nzviedrite@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/jnru-aqxk",
+            "description": "Unplanned public K-12 school district and individual school closures due to COVID-19 in the United States from August 1, 2020\u2013June 30, 2022.",
+            "title": "COVID-19-related School Closures: USA, 2020-2022",
+            "programCode": [
+                "009:028"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/jnru-aqxk/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/jnru-aqxk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/jnru-aqxk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/jnru-aqxk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States, 50 States and D.C.",
+            "license": "https://www.usa.gov/government-works",
+            "theme": [
+                "Public Health Surveillance"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-discharges-teds-d-2008",
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
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2008-nid13549",
+            "description": "<p>The Treatment Episode Data Set -- Discharges (TEDS-D) is a national census data system of annual discharges from substance abuse treatment facilities. TEDS-D provides annual data on the number and characteristics of persons discharged from public and private substance abuse treatment programs that receive public funding. Data collected both at admission and at discharge is included. The unit of analysis is a treatment discharge. TEDS-D consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Admissions (TEDS-A), collects data on admissions to substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS-D variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables unique to TEDS-D, and not part of TEDS-A, are the length of stay, reason for leaving treatment, and service setting at time of discharge. TEDS-D also provides many of the same variables that exist in TEDS-A. This includes information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008) .<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "title": "Treatment Episode Data Set: Discharges (TEDS-D-2008)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2008-nid13549",
+                    "description": "Treatment Episode Data Set: Discharges (TEDS-D-2008) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2008-nid13549"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.nlm.nih.gov/mesh/meshhome.html",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2022-12-19",
+            "@type": "dcat:Dataset",
+            "modified": "2024-09-03",
+            "keyword": [
+                "mesh"
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/m5y3-25uc",
+            "description": "Listed below are MeSH Topical Qualifiers listed by Name, Abbreviation, and Short Form. Each Qualifier is defined by a Scope Note that provides guidance on how it should be used.",
+            "title": "MeSH Qualifiers with Scope Notes",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/m5y3-25uc/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/m5y3-25uc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/m5y3-25uc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/m5y3-25uc/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/puin-6ss7",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-04-26",
+            "@type": "dcat:Dataset",
+            "modified": "2019-05-30",
+            "keyword": [
+                "2019",
+                "all serogroups",
+                "meningococcal disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "serogroup b",
+                "serogroups acwy",
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
+            "identifier": "https://data.cdc.gov/api/views/puin-6ss7",
+            "description": "NNDSS - TABLE 1W.  Meningococcal disease,  All serogroups to Meningococcal disease, Serogroup B - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1W. Meningococcal disease, All serogroups to Meningococcal disease, Serogroup B",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/puin-6ss7/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/puin-6ss7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/puin-6ss7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/puin-6ss7/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/847z-pxin",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2020-06-01",
+            "@type": "dcat:Dataset",
+            "modified": "2021-07-07",
+            "keyword": [
+                "air pollution",
+                "asthma",
+                "environmental health",
+                "ozone"
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
+            "identifier": "https://data.cdc.gov/api/views/847z-pxin",
+            "description": "This dataset provides modeled predictions of ozone levels from the EPA's Downscaler model. Data are at the census tract level for 2001-2005. These data are used by the CDC's National Environmental Public Health Tracking Network to generate air quality measures. Census tract-level datasets contain estimates of the mean predicted concentration and associated standard error. Please refer to the metadata attachment for more information.\n\nLearn more about outdoor air quality on the Tracking Network's website: https://ephtracking.cdc.gov/showAirLanding.action.\n\nBy using these data, you signify your agreement to comply with the following requirements:\n1. Use the data for statistical reporting and analysis only.\n2. Do not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals.\n3. Do not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov.\n4. Do not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating.\n5. Acknowledge, in all reports or presentations based on these data, the original source of the data and CDC.\n6. Suggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking.",
+            "title": "Daily Census Tract-Level Ozone Concentrations, 2011-2015",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/847z-pxin/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/847z-pxin/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/847z-pxin/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/847z-pxin/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "http://mimic.physionet.org/",
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
+                "fn": "PAI, VINAY MANJUNATH",
+                "hasEmail": "mailto:paiv@mail.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
+            "identifier": "f4dd62fd-e5cb-4e95-a5b9-a3003f1ab7a6",
+            "description": "<p>The objective of this Bioengineering Research Partnership is to focus the resources of a powerful interdisciplinary team from academia (MIT), industry (Philips Medical Systems) and clinical medicine (Beth Israel Deaconess Medical Center) to develop and evaluate advanced ICU patient monitoring systems that will substantially improve the efficiency, accuracy and timeliness of clinical decision making in intensive care.</p>",
+            "title": "Multiparameter Intelligent Monitoring in Intensive Care II (MIMIC-II)",
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
+            "landingPage": "https://data.cdc.gov/d/dgwc-f5xf",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-15",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Miner Health Branch (MHB), Spokane Mining Research Division (SMRD)",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/dgwc-f5xf",
+            "description": "A method for the quantification of airborne organic carbon (OC) and elemental carbon (EC) within aerosolized diesel particulate matter (DPM) is described in the article cited below. DPM is a known carcinogen encountered in many industrial workplaces (notably mining) and in the ambient atmosphere. The method described here collects DPM particles onto a quartz fiber filter, after which reflection-mode infrared spectra are measured on a mid-infrared Fourier transform (FT-IR) spectrometer. Several infrared absorption bands are investigated for their efficacy in quantifying OC and EC. The thermo-optical (T-O) method is used to calibrate a linear regression model to predict OC and EC from the infrared spectra. The calibrated model, generated from laboratory DPM samples, is then utilized to quantify OC and EC in\nmine samples obtained from two metal mine locations under a variety of operating conditions. The feasibility of further improving these results by partial least squares (PLS) regression was investigated. A single calibration that is broadly applicable would be considered an improvement over currently available portable instruments, which require aerosol-specific calibration.",
+            "title": "DPM OC, EC and FT-IR data (Quantifying elemental and organic carbon in diesel particulate matter by mid infrared spectrometry).",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/dgwc-f5xf/application/x-zip-compressed",
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
+            "landingPage": "https://www.cdc.gov/nchs/nhanes/visualization/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-02-06",
+            "@type": "dcat:Dataset",
+            "temporal": "1999-2018",
+            "modified": "2024-09-17",
+            "references": [
+                "https://www.cdc.gov/nchs/nhanes/visualization/"
+            ],
+            "keyword": [
+                "dqs",
+                "nhanes"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:CDCINFO@CDC.GOV"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/be3w-4inw",
+            "description": "These data represent prevalence estimates of select infectious diseases from the National Health and Nutrition Examination Survey (NHANES). This version of the NHANES dataset is specific to visualization within the NCHS DQS.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
+            "title": "DQS NHANES Select Infectious Diseases Prevalence Estimates",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/be3w-4inw/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/be3w-4inw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/be3w-4inw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/be3w-4inw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States",
+            "describedBy": "https://www.cdc.gov/nchs/nhanes/visualization/",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "NA",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2020-08-07",
+            "@type": "dcat:Dataset",
+            "temporal": "2020-01-01/2022-03-28",
+            "modified": "2023-07-12",
+            "keyword": [
+                "age",
+                "all causes",
+                "children",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
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
+            "identifier": "https://data.cdc.gov/api/views/3apk-4u4f",
+            "description": "Effective June 28, 2023, this dataset will no longer be updated. Similar data are accessible from CDC WONDER (https://wonder.cdc.gov/mcd-icd10-provisional.html).\n\nCumulative deaths involving COVID-19 reported to NCHS by sex and age in years, in the United States.",
+            "title": "Provisional COVID-19 Death Counts by Age in Years, 2020-2023",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3apk-4u4f/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3apk-4u4f/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3apk-4u4f/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3apk-4u4f/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.nlm.nih.gov/research/umls/rxnorm/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2012-08-22",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "api",
+                "dataset",
+                "drugs",
+                "generic",
+                "health data standards",
+                "semantic",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/t84b-g5db",
+            "description": "RxNorm provides normalized names for clinical drugs and links its names to many of the drug vocabularies commonly used in pharmacy management and drug interaction software, including those of First Databank, Micromedex, Gold Standard, and Multum. By providing links between these vocabularies, RxNorm can mediate messages between systems not using the same software and vocabulary.\n\nTechnical documentation at http://www.nlm.nih.gov/research/umls/rxnorm/docs/index.html",
+            "title": "RxNorm",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.nlm.nih.gov/research/umls/rxnorm/docs/rxnormfiles.html",
+                    "mediaType": "text/html",
+                    "title": "Download RxNorm Data"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://rxnav.nlm.nih.gov/RxNormAPIs.html#",
+                    "mediaType": "text/html",
+                    "title": "RxNorm API"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://rxnav.nlm.nih.gov/PrescribableAPIs.html",
+                    "mediaType": "text/html",
+                    "title": "Prescribable RxNorm API"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://mor.nlm.nih.gov/RxNav/",
+                    "mediaType": "text/html",
+                    "title": "Query Interface (RxNav)"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Drugs and Chemicals"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/revalidation-reassignment-list",
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
+                "provider enrollment",
+                "states & territories",
+                "zip code"
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/20f51cff-4137-4f3a-b6b7-bfc9ad57983b/data-viewer",
+            "description": "The Revalidation Reassignment List dataset provides information on reassignments of providers who are due for revalidation.\n\n\u00a0\n\nNote: This full dataset contains more records than most spreadsheet programs can handle, which will result in an incomplete load of data. Use of a database or statistical software is required.",
+            "title": "Revalidation Reassignment List",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/20f51cff-4137-4f3a-b6b7-bfc9ad57983b/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Revalidation Reassignment List : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/20b356f5-23c7-4f6e-8d71-55aa623f19fc/revalidation_group_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Reassignment List : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e1700c55-4e42-4fea-96fb-bf3198418e47/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Reassignment List : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/b137f460-7749-4853-9449-385ac88fbaaa/revalidation_group_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Reassignment List : 2024-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ab09a9d5-d986-4711-9024-692ea3866594/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Reassignment List : 2024-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/ecb380a5-b868-471b-8d5f-d02927715ea5/revalidation_group_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Reassignment List : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8d31ec1a-b237-46d6-bab1-878a05c1a04f/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Reassignment List : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/f43b317e-5648-4bba-ad8c-ef907195b402/revalidation_group_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Reassignment List : 2024-02-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7e6c96d6-96fd-4a5e-841c-495aeaa873d1/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Reassignment List : 2024-02-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/b87b68cc-ba7c-460c-9249-62a063d6c3b6/revalidation_group_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Reassignment List : 2024-01-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/60b4b211-8cb5-4646-a289-cc06f94ec097/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Reassignment List : 2024-01-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/cfb625f1-439c-417b-ad42-8b07154eb1aa/revalidation_group_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Reassignment List : 2023-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/fa6b0e04-685a-4f9e-bc4d-89a9da3ed47e/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Reassignment List : 2023-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/09950d88-3c2f-408a-8874-7c48f15af214/revalidation_group_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Reassignment List : 2023-11-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/bf072b16-acfc-4276-8513-bbf362af77a8/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Reassignment List : 2023-11-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/a86b1fc2-669e-4191-8f9f-641bb2a12f38/revalidation_group_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Reassignment List : 2023-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/353d718b-d676-4dc6-988a-2c01423d97f3/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Reassignment List : 2023-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/20abf22f-a23c-4f81-9411-2af3754bc227/revalidation_group_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Reassignment List : 2023-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7e571259-cae5-4453-808c-4fd729222863/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Reassignment List : 2023-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/e290cb26-483c-4784-a56d-babe0ab86766/revalidation_group_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Reassignment List : 2023-08-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/05b3e677-5abe-4f4f-9a91-a1bdc7c20d13/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Reassignment List : 2023-08-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/0c9b09b0-529d-4380-8063-cba1d098cdd4/revalidation_group_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Reassignment List : 2023-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f6c275b5-c11f-4a9e-a3d6-575abe083773/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Reassignment List : 2023-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/da379cf8-0e30-4fe9-a808-763a729ad757/revalidation_group_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Reassignment List : 2023-06-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/b98fc565-a0dd-4812-912e-997b23cb18d0/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Reassignment List : 2023-06-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/d791e9d9-9aca-4c66-9f83-dd76229c86e6/revalidation_group_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Reassignment List : 2023-05-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3e645a5d-cf7e-4d6c-bcd9-b0398947e4f4/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Reassignment List : 2023-05-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-02/fe180369-0276-48df-a69e-d5ada04c5808/revalidation_group_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Reassignment List : 2023-03-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/974dba8f-5345-4f4e-b1ba-dd55a8782389/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Reassignment List : 2023-03-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-12/83ca058b-e45a-4c7f-87b4-59899a016979/revalidation_group_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Reassignment List : 2022-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ff893063-7d95-4970-8024-65bdd9d000f1/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Reassignment List : 2022-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-10/5d090936-6f8d-4a19-b896-93a5186b99a8/revalidation_group_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Reassignment List : 2022-11-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ee93d955-39d5-4f8a-902d-8754373bf89a/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Reassignment List : 2022-11-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-10/b7d38028-fd59-472e-bc0d-18ac1c9bab9c/revalidation_group_reassignment_pa_xref_0.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Reassignment List : 2022-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/455b5698-bd49-4a23-b114-ce58514abf90/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Reassignment List : 2022-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-10/14354e48-78d0-4447-a2b2-774bc8749fdf/revalidation_group_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Reassignment List : 2022-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/290d532e-db33-4d92-844a-402ad8d2c466/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Reassignment List : 2022-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-07/5d385317-fd23-4f65-bb46-7b2879485aac/revalidation_group_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Reassignment List : 2022-08-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/831e09fe-634b-44c3-b934-31fee577e59b/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Reassignment List : 2022-08-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-07/cb21a887-c134-4e27-9f59-2ac59f318431/revalidation_group_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Reassignment List : 2022-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/244d678f-be10-4a87-ba8b-8e509604c597/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Reassignment List : 2022-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-05/a32b15c7-ffc0-4989-af41-cea0027ca751/revalidation_group_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Reassignment List : 2022-06-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e433f043-39b5-4c1a-bf06-e8c0a4b50b3a/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Reassignment List : 2022-06-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-05/60fd2595-3330-4591-bce6-27a25bb8b66b/revalidation_group_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Reassignment List : 2022-04-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/09e7d601-a1c4-4d19-b6aa-25dd30332e8a/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Reassignment List : 2022-04-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-03/bbef200b-ac81-4053-b823-5211a53c1454/revalidation_group_reassignment_pa_xref.csv",
+                    "mediaType": "text/csv",
+                    "title": "Revalidation Reassignment List : 2022-02-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e8916717-c807-4e09-b90d-0b1c242c1dcc/data",
+                    "mediaType": "text/html",
+                    "title": "Revalidation Reassignment List : 2022-02-28"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/revalidation-reassignments-list-data-dictionary",
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
+            "landingPage": "http://www.cdc.gov/STATESystem",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2019-02-27",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-22",
+            "keyword": [
+                "office on smoking and health",
+                "osh",
+                "qit",
+                "survey questions",
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
+            "identifier": "https://data.cdc.gov/api/views/vdgb-f9s3",
+            "description": "1965, 1966, 1970, 1974-2015, 2017. Centers for Disease Control and Prevention (CDC). Office on Smoking and Health (OSH). Survey Questions (Tobacco Use). The QIT is a compilation of more than 7,000 historical tobacco-related survey questions from various state, national and international surveys.",
+            "title": "Question Inventory on Tobacco (QIT)",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vdgb-f9s3/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vdgb-f9s3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vdgb-f9s3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vdgb-f9s3/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Survey Questions (Tobacco Use)"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/pjtk-n43k",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2020-01-17",
+            "@type": "dcat:Dataset",
+            "modified": "2021-01-07",
+            "keyword": [
+                "2020",
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
+            "identifier": "https://data.cdc.gov/api/views/pjtk-n43k",
+            "description": "NNDSS - TABLE 1B. Arboviral diseases, Jamestown Canyon virus disease to Powassan virus disease  \u2013 2020.  In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - Table 1B. Arboviral diseases, Jamestown Canyon virus disease to Powassan virus disease",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pjtk-n43k/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pjtk-n43k/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pjtk-n43k/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pjtk-n43k/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cms.gov/summary-statistics-on-beneficiary-enrollment/medicare-and-medicaid-reports/cms-program-statistics-medicare-newly-enrolled",
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
+                "health equity",
+                "medicare",
+                "medicare advantage",
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/619a72e4-07cc-414e-95d6-058e3c10557a/data-viewer",
+            "description": "The CMS Program Statistics -\u00a0Medicare Newly Enrolled tables provide data on characteristics of the newly enrolled Medicare population.\u00a0\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\u00a0\n\nBelow is the list of tables:\n\nMDCR ENROLL AB 21. \u00a0Medicare Newly Enrolled Beneficiaries: \u00a0Total, Aged, and Disabled Enrollees, Yearly Trend\n\tMDCR ENROLL AB 22. \u00a0Medicare Newly Enrolled Beneficiaries: \u00a0Total Enrollees by Month of Enrollment, Yearly Trend\n\tMDCR ENROLL AB 23. \u00a0Medicare Newly Enrolled Beneficiaries: \u00a0Total Enrollees, by Demographic Characteristics\n\tMDCR ENROLL AB 24. \u00a0Medicare Newly Enrolled Beneficiaries: \u00a0Total, Aged, and Disabled Enrollees, by Area of Residence\n\tMDCR ENROLL AB 25. \u00a0Medicare Newly Enrolled Beneficiaries: \u00a0Total, Aged, and Disabled Original Medicare Enrollees\n\tMDCR ENROLL AB 26. \u00a0Medicare Newly Enrolled Beneficiaries: \u00a0Original Medicare Enrollees by Month of Enrollment, Yearly Trend\n\tMDCR ENROLL AB 27. \u00a0Medicare Newly Enrolled Beneficiaries: \u00a0Original Medicare Enrollees, by Demographic Characteristics\n\tMDCR ENROLL AB 28. \u00a0Medicare Newly Enrolled Beneficiaries: \u00a0Total, Aged, and Disabled Original Medicare Enrollees, by Area of Residence\n\tMDCR ENROLL AB 29. \u00a0Medicare Newly Enrolled Beneficiaries: \u00a0Total, Aged, and Disabled Medicare Advantage and Other Health Plan Enrollees, Yearly Trend\n\tMDCR ENROLL AB 30. \u00a0Medicare Newly Enrolled Beneficiaries: \u00a0Medicare Advantage and Other Health Plan Enrollees, by Month of Enrollment, Yearly Trend\n\tMDCR ENROLL AB 31. \u00a0Medicare Newly Enrolled Beneficiaries: \u00a0Medicare Advantage and Other Health Plan Enrollees, by Demographic Characteristics\n\tMDCR ENROLL AB 32. \u00a0Medicare Newly Enrolled Beneficiaries: \u00a0Total, Aged, and Disabled Medicare Advantage and Other Health Plan Enrollees, by Area of Residence",
+            "title": "CMS Program Statistics - Medicare Newly Enrolled",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-02/CPS%20MDCR%20ENROLL%20AB%2021-32%202021.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Newly Enrolled : 2021-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-02/CPS%20MDCR%20ENROLL%20AB%2021-32%202020.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Newly Enrolled : 2020-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-01/CPS_MDCR_ENROLL_AB_21-32.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Newly Enrolled : 2019-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-11/CPS%20MDCR%20TOTAL%20ENROLL%20AB%2021-32%202018.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Newly Enrolled : 2018-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2019-12/2017_Newly_Enroll_0.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Newly Enrolled : 2017-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-01/2016_Newly_Enroll.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Newly Enrolled : 2016-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-01/2015_Newly_Enroll.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Newly Enrolled : 2015-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-01/2014_Newly_Enroll_0.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Newly Enrolled : 2014-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-01/2013_Newly_Enroll.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Newly Enrolled : 2013-12-31"
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
+            "landingPage": "https://data.cdc.gov/d/hwk8-wu83",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-06-26",
+            "@type": "dcat:Dataset",
+            "temporal": "2020-12-13/2023-10-14",
+            "modified": "2023-10-14",
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
+            "identifier": "https://data.cdc.gov/api/views/hwk8-wu83",
+            "description": "This site provides historical data beginning June 14, 2023, for the visualization presented on <a href=\"https://covid.cdc.gov/covid-data-tracker/#vaccinations\">COVID-19 Data Tracker\u2019s \u201cVaccinations in the United States\" </a> site titled \u201cUS COVID-19 Vaccine Doses Delivered by Vaccine Type\u201d\n\n<b>Definition for Distributed: </b>\nCumulative number of COVID-19 updated vaccine doses distributed in the United States.\nCDC is no longer reporting metrics for Johnson & Johnson, and the original Pfizer and Moderna vaccines.\n\nData represents all vaccine partners including jurisdictional partner clinics, retail pharmacies, long-term care facilities, dialysis centers, Federal Emergency Management Agency and Health Resources and Services Administration partner sites, and federal entity facilities.",
+            "title": "COVID-19 Updated Vaccines Distributed",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hwk8-wu83/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hwk8-wu83/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hwk8-wu83/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hwk8-wu83/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/e6pu-b7n6",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-16",
+            "@type": "dcat:Dataset",
+            "modified": "2021-12-15",
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
+            "identifier": "0563d88c-8fe5-42a8-9d69-f67fd21c0e91",
+            "description": "This table presents the rate of neonatal abstinence syndrome per 1,000 newborns whose deliveries were covered by Medicaid or CHIP, 2017 - 2019.\r\n\r\nSome states have serious data quality issues, making the data unusable for identifying this population. Data for a state are considered unusable based on DQ Atlas thresholds for the following topics: Total Medicaid and CHIP Enrollment, Claims Volume - IP, Claims Volume - OT, Claims Volume - IP, Diagnosis Code - IP, Diagnosis Code - OT, Procedure Codes - OT Professional. Data from Maryland, Tennessee, and Utah are omitted for the tables due to data quality concerns. Values for Maryland were excluded due to unusuable diagnosis codes in the IP file and the OT file in 2017. Tennessee was excluded due to unusable diagnosis codes in the IP file in 2017 - 2019. Utah was excluded due to unusable procedure codes on OT professional claims in 2017 - 2019.  In addition, states with a high data quality concern on one or more measures are noted in the table with an asterisk (*). \r\n\r\nPlease refer to the DQ Atlas for more information about data quality assessment methods.",
+            "title": "Rate of NAS per 1,000 births in newborns whose deliveries were covered by Medicaid or CHIP, 2017 - 2019",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/rate-of-nas-per-thous-in-newborns-2017-to-2019.csv",
+                    "description": "This table presents the rate of neonatal abstinence syndrome per 1,000 newborns whose deliveries were covered by Medicaid or CHIP, 2017 - 2019.\n\nSome states have serious data quality issues, making the data unusable for identifying this population. Data for a state are considered unusable based on DQ Atlas thresholds for the following topics: Total Medicaid and CHIP Enrollment, Claims Volume - IP, Claims Volume - OT, Claims Volume - IP, Diagnosis Code - IP, Diagnosis Code - OT, Procedure Codes - OT Professional. Data from Maryland, Tennessee, and Utah are omitted for the tables due to data quality concerns. Values for Maryland were excluded due to unusuable diagnosis codes in the IP file and the OT file in 2017. Tennessee was excluded due to unusable diagnosis codes in the IP file in 2017 - 2019. Utah was excluded due to unusable procedure codes on OT professional claims in 2017 - 2019.  In addition, states with a high data quality concern on one or more measures are noted in the table with an asterisk (*). \n\nPlease refer to the DQ Atlas for more information about data quality assessment methods.",
+                    "@type": "dcat:Distribution",
+                    "title": "Rate of NAS per 1,000 births in newborns whose deliveries were covered by Medicaid or CHIP, 2017 - 2019"
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
+            "landingPage": "https://data.cdc.gov/d/8ggw-jwph",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-15",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Allergy and Clinical Immunology Branch, Health Effects Laboratory Division",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/8ggw-jwph",
+            "description": "The fundamental goal of this study was to develop an in vivo model of the exposome that could be used to evaluate exposure-induced alterations in local and systemic immune markers as a function of various exposomal factors. Accordingly, the model was designed to mimic an occupationally-relevant scenario in which inhalation of welding fumes (WF) constituted the primary occupational/environmental exposure of interest. Immune endpoints were assessed at three different time points representative of different stages in the exposure/response timeline (before WF exposure, directly after, and following a 12 wk recovery period). Moreover, the potential impact of genetic variation and lifestyle factors on the immune response to WF exposure and subsequent recovery was addressed by incorporating two different rat strains (Sprague-Dawley [SD] and Brown Norway [BN]) and two variations in diet (regular and high fat) into the model.\n\nOne of the primary objectives of this study was to determine whether consumption of a HF diet is associated with increased immunological responsivity following exposure to a common respiratory toxicant. The study was also executed with the goal of identifying which experimental factor (genetics/strain, diet, occupational exposure) is most influential in the modulation of local and systemic markers of immune status following WF exposure, and subsequently, the efficacy of inflammation resolution. The information obtained from these analyses will help elucidate which exposomic determinants may be particularly relevant in the context of immunotoxicity, and accordingly, warrant special attention in future investigations. The results will also contribute to the development of other in vivo exposome models and direct future efforts related to the exposome and its impact on human health.",
+            "title": "Examination of the exposome in an animal model: the impact of high fat diet and rat strain on local and systemic immune markers following occupational welding fume exposure",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/8ggw-jwph/application/x-zip-compressed",
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
+            "landingPage": "https://healthdata.gov/d/e6y3-2bid",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2022-08-10",
+            "@type": "dcat:Dataset",
+            "modified": "2022-08-17",
+            "keyword": [
+                "individual",
+                "individual market medical",
+                "py2022",
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
+            "identifier": "fb97ce4a-5e5b-4e18-bab8-27299e56d5cf",
+            "description": "The Medical Individual Market file of the QHP Landscape Files contains information on certified medical plans offered through an Exchange to consumers in the individual market. These plans are also known as Qualified Health Plans (QHPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
+            "title": "QHP Landscape PY2022 Individual Medical",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2022/individual_market_medical.zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/e6z4-xemc",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2022-08-10",
+            "@type": "dcat:Dataset",
+            "modified": "2022-08-17",
+            "keyword": [
+                "exchange puf",
+                "marketplace puf",
+                "network",
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
+            "identifier": "0953b9c0-0843-4f41-88e9-cc44aed14407",
+            "description": "The Network PUF (Ntwrk-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The Ntwrk-PUF contains issuer-level data identifying provider network URLs.",
+            "title": "Network PUF - PY2022",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2022/network_puf.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/e8eg-9rei",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2022-08-31",
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
+            "identifier": "9f53c963-b4c3-581e-ae56-4067452ea599",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
+            "title": "prodAuto_measureSearchInfo",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measureSearchInfo.csv",
+                    "description": "{\"dataset\": \"measureSearchInfo\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "@type": "dcat:Distribution",
+                    "title": "measureSearchInfo csv file"
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
+            "landingPage": "https://data.cdc.gov/d/2qxe-cmv4",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-01-21",
+            "@type": "dcat:Dataset",
+            "modified": "2022-01-12",
+            "keyword": [
+                "2021",
+                "hepatitis c",
+                "influenza-associated pediatric mortality",
+                "nedss",
+                "netss",
+                "nndss",
+                "perinatal infection",
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
+            "identifier": "https://data.cdc.gov/api/views/2qxe-cmv4",
+            "description": "NNDSS - TABLE 1R. Hepatitis C, perinatal infection to Influenza-associated pediatric mortality - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Please refer to the CDC WONDER publication for weekly updates to the footnote for this condition.",
+            "title": "NNDSS - TABLE 1R. Hepatitis C, perinatal infection to Influenza-associated pediatric mortality",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2qxe-cmv4/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2qxe-cmv4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2qxe-cmv4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2qxe-cmv4/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/5i5k-6cmh",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-08-11",
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
+            "identifier": "https://data.cdc.gov/api/views/5i5k-6cmh",
+            "description": "This site provides data for select demographic characteristics (age, sex, and age by sex) of people receiving COVID-19 vaccinations in the United States at the national and jurisdictional levels. For national race/ethnicity data, please visit <a href=\"https://data.cdc.gov/Vaccinations/COVID-19-Vaccination-Demographics-in-the-United-St/km4m-vcsb\">COVID-19 Vaccination Demographics in the United States,National</a>. For jurisdictional race/ethnicity data, please visit the relevant health department website if available.\n \nData represents all vaccine partners including jurisdictional partner clinics, retail pharmacies, long-term care facilities, dialysis centers, Federal Emergency Management Agency and Health Resources and Services Administration partner sites, and federal entity facilities.\u202f",
+            "title": "COVID-19 Vaccination Age and Sex Trends in the United States, National and Jurisdictional",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5i5k-6cmh/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5i5k-6cmh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5i5k-6cmh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5i5k-6cmh/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2020-09-02",
+            "@type": "dcat:Dataset",
+            "temporal": "2020-01-01/2023-07-29",
+            "modified": "2023-09-27",
+            "keyword": [
+                "age",
+                "age group",
+                "all causes",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "influenza",
+                "monthly",
+                "mortality",
+                "nchs",
+                "nvss",
+                "place of death",
+                "pneumonia",
+                "provisional",
+                "puerto rico",
+                "state",
+                "united states",
+                "yearly"
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
+            "identifier": "https://data.cdc.gov/api/views/4va6-ph5s",
+            "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nDeaths involving COVID-19, influenza, and pneumonia reported to NCHS by jurisdiction of occurrence, place of death, and age group.",
+            "title": "Provisional COVID-19 Deaths by Place of Death and Age",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4va6-ph5s/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4va6-ph5s/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4va6-ph5s/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4va6-ph5s/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/ncezid/dfwed/beam-dashboard.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-12-15",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-16",
+            "keyword": [
+                "beam",
+                "beam dashboard",
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
+            "identifier": "https://data.cdc.gov/api/views/ch83-ush6",
+            "description": "The BEAM (Bacteria, Enterics, Amoeba, and Mycotics) Dashboard is an interactive tool to access and visualize data from the System for Enteric Disease Response, Investigation, and Coordination (SEDRIC). The BEAM Dashboard provides timely data on pathogen trends and serotype details to inform work to prevent illnesses from food and animal contact.",
+            "title": "BEAM Dashboard \u2013 Top 30 Most Common Serotypes",
+            "programCode": [
+                "009:028"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ch83-ush6/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ch83-ush6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ch83-ush6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ch83-ush6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "US",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Monthly",
+            "theme": [
+                "Foodborne",
+                "Waterborne",
+                "and Related Diseases"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/qz3x-mf9n",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-02-10",
+            "@type": "dcat:Dataset",
+            "modified": "2021-07-23",
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
+            "identifier": "https://data.cdc.gov/api/views/qz3x-mf9n",
+            "description": "State, territorial, and county executive orders, administrative orders, resolutions, and proclamations are collected from government websites and cataloged and coded using Microsoft Excel by one coder with one or more additional coders conducting quality assurance.\n\nData were collected to determine when individuals in states, territories, and counties were subject to executive orders, administrative orders, resolutions, and proclamations for COVID-19 that require or recommend people stay in their homes.\n\nThese data are derived from the publicly available state, territorial, and county executive orders, administrative orders, resolutions, and proclamations (\u201corders\u201d) for COVID-19 that expressly require or recommend individuals stay at home found by the CDC, COVID-19 Community Intervention and At-Risk Task Force, Monitoring and Evaluation Team & CDC, Center for State, Tribal, Local, and Territorial Support, Public Health Law Program from March 15 through May 5, 2020. These data will be updated as new orders are collected. Any orders not available through publicly accessible websites are not included in these data. Only official copies of the documents or, where official copies were unavailable, official press releases from government websites describing requirements were coded; news media reports on restrictions were excluded. Recommendations not included in an order are not included in these data. These data do not include mandatory business closures, curfews, or limitations on public or private gatherings. These data do not necessarily represent an official position of the Centers for Disease Control and Prevention.",
+            "title": "U.S. State, Territorial, and County Stay-At-Home Orders: March 15-May 5 by County by Day",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qz3x-mf9n/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qz3x-mf9n/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qz3x-mf9n/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qz3x-mf9n/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://wwwn.cdc.gov/NHISDataQueryTool/ER_Biannual/index_biannual.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-07-07",
+            "temporal": "2019/2021",
+            "@type": "dcat:Dataset",
+            "modified": "2024-12-09",
+            "keyword": [
+                "early release",
+                "key health indicators",
+                "nhis"
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
+            "identifier": "https://data.cdc.gov/api/views/trpk-sp8z",
+            "description": "Interactive Biannual Early Release Estimates provide health statistics based on data from the 2019-2021 National Health Interview Survey (NHIS) for selected health topics for adults aged 18 years and over. All estimates are unadjusted percentages based on preliminary data files and are released prior to final data editing and final weighting to provide access to the most recent information from the NHIS. Estimates can be grouped by demographic characteristics (such as age, race and Hispanic origin, or sex). Estimates based on 2019-2020 NHIS quarterly data are available in Interactive Quarterly Early Release Estimates. Estimates based on the 1997\u20132018 NHIS can be found in Previous Early Release Reports on Key Health Indicators.",
+            "title": "NHIS Interactive Biannual Early Release Estimates",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/trpk-sp8z/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/trpk-sp8z/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/trpk-sp8z/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/trpk-sp8z/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P6M",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:00"
+            ],
+            "landingPage": "https://data.cdc.gov/d/tug7-57z5",
+            "issued": "2024-08-29",
+            "@type": "dcat:Dataset",
+            "modified": "2024-08-29",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Phong Le",
+                "hasEmail": "mailto:pyv8@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/tug7-57z5",
+            "description": "This data is what is visualized in the HHS DRIVE dashboard.",
+            "title": "HHS DRIVE",
+            "programCode": [
+                "009:031"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tug7-57z5/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tug7-57z5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tug7-57z5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tug7-57z5/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/vp2h-kf33",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-09-14",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-05",
+            "keyword": [
+                "health services research",
+                "public health"
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/vp2h-kf33",
+            "description": "Health Services and Sciences Research Resources (HSRR) provides information about research datasets and instruments/indices employed in Health Services Research, Behavioral and Social Sciences and Public Health.\n\nThis resource was retired on September 14, 2021 and is no longer updated.",
+            "title": "Health Services and Sciences Research Resources (HSRR)",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/vp2h-kf33/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/vp2h-kf33/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/vp2h-kf33/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/vp2h-kf33/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Research"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/3m2r-fh4s",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-03-23",
+            "@type": "dcat:Dataset",
+            "modified": "2022-09-25",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Mara Howard-Williams",
+                "hasEmail": "mailto:prw0@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/3m2r-fh4s",
+            "description": ": This dataset contains all vaccine mandate prohibitions that were issued as of ____, by 50 states, 5 territories, and the District of Columbia regardless of whether the law has been superseded by a subsequent law, postponed by subsequent law, or otherwise modified. State and territorial laws are collected from publicly available government websites and cataloged and coded in HHS Protect by one coder with one or more additional coders conducting quality assurance. \nData were collected to determine when certain groups were prohibited from issuing vaccine mandates and to what groups those prohibitions applied. Data can be used to determine when states announced and began prohibiting for different groups from being required to be vaccinated. \nThese data are derived from publicly available state and territorial laws and official policy documents found by the CDC, COVID-19 Mitigation Policy Analysis Unit, and the CDC, Center for State, Tribal, Local, and Territorial Support, Public Health Law Program from March 1, 2020 through _____. These data will be updated as new laws are collected. Any orders not available through publicly accessible websites are not included in this dataset. Recommendations not included in a law are not included in these data. Effective and expiration dates were coded using only the date provided in the law. These data do not necessarily represent the official position of the Centers for Disease Control and Prevention.",
+            "title": "State-Level Restrictions on Vaccine Mandates \u2013 All",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3m2r-fh4s/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3m2r-fh4s/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3m2r-fh4s/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3m2r-fh4s/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-09-27",
+            "temporal": "1997/2022",
+            "@type": "dcat:Dataset",
+            "modified": "2024-09-27",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:healthus@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/aewi-gwni",
+            "description": "Data on asthma in children younger than age 18 in the United States, by selected characteristics. Data are from Health, United States. Source: National Center for Health Statistics, National Health Interview Survey.",
+            "title": "Asthma in children younger than age 18, by selected characteristics: United States.",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/aewi-gwni/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/aewi-gwni/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/aewi-gwni/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/aewi-gwni/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Annual",
+            "theme": [
+                "National Center for Health Statistics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/g9dy-mhts",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2016-06-15",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-27",
+            "keyword": [
+                "cessation",
+                "cigarette",
+                "cigarette use",
+                "current",
+                "fact sheet",
+                "high school",
+                "infographic",
+                "middle school",
+                "nyts",
+                "office on smoking and health",
+                "osh",
+                "prevalence",
+                "quit",
+                "smokeless",
+                "smoker",
+                "smoking",
+                "smoking status",
+                "state system",
+                "survey",
+                "tobacco",
+                "tobacco use",
+                "youth"
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
+            "identifier": "https://data.cdc.gov/api/views/g9dy-mhts",
+            "description": "Explore the Youth and Tobacco Use Infographic which outlines key facts related to tobacco use among youth.",
+            "title": "Youth And Tobacco Use Infographic",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/g9dy-mhts/application/pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Survey Data"
+            ]
+        },
+        {
+            "accessLevel": "non-public",
+            "landingPage": "http://www.cdc.gov/STATESystem",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2025-01-31",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-31",
+            "keyword": [
+                "adult",
+                "gats",
+                "gtss",
+                "osh",
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
+            "identifier": "https://data.cdc.gov/api/views/4xf6-nrwk",
+            "description": "2008-2017. Centers for Disease Control and Prevention (CDC).   Office on Smoking and Health (OSH) \u2013 Global Tobacco Surveillance System (GTSS) - Global Adult Tobacco Survey (GATS).    The Global Adult Tobacco Survey (GATS) is the global standard to systematically monitor adult tobacco use and track key tobacco control indicators. GATS is a nationally representative household survey of adults 15 years of age or older, using a standard protocol. It is intended to generate comparable data within and across countries. GATS enhances countries' capacity to design, implement and evaluate tobacco control interventions.",
+            "title": "Global Tobacco Surveillance System (GTSS) - Global Adult Tobacco Survey (GATS)",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4xf6-nrwk/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4xf6-nrwk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4xf6-nrwk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4xf6-nrwk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Global-Survey-Data/Global-Tobacco-Surveillance-System-GTSS-Global-Adu/4xf6-nrwk",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Global Survey Data"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.ncbi.nlm.nih.gov/taxonomy",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-08-26",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "biology",
+                "classification",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/nmc6-m47x",
+            "description": "The Taxonomy Database is a curated classification and nomenclature for all of the organisms in the public sequence databases. This currently represents about 10% of the described species of life on the planet.",
+            "title": "Taxonomy",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Root",
+                    "description": "Search the taxonomy tree using partial taxonomic names, common names, wild cards and phonetically similar names.",
+                    "@type": "dcat:Distribution",
+                    "title": "Taxonomy Browser - Query Interface"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/Taxonomy/CommonTree/wwwcmt.cgi",
+                    "description": "Generates a taxonomic tree for a selected group of organisms. Users can upload a file of taxonomy IDs or names, or they can enter names or IDs directly.",
+                    "@type": "dcat:Distribution",
+                    "title": "Taxonomy Common Tree"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/Taxonomy/taxonomyhome.html/index.cgi?chapter=STATISTICS&uncultured=hide&unspecified=hide",
+                    "description": "Displays the number of taxonomic nodes in the database for a given rank and date of inclusion.",
+                    "@type": "dcat:Distribution",
+                    "title": "Taxonomy Statistics - Query Interface"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/Taxonomy/TaxIdentifier/tax_identifier.cgi",
+                    "description": "Displays the current status of a set of taxonomic nodes or IDs.",
+                    "@type": "dcat:Distribution",
+                    "title": "Taxonomy Status Reports"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/Taxonomy/taxonomyhome.html/index.cgi?chapter=cgencodes",
+                    "description": "Currently, genetic codes can be set independently for nucleus, mitochondria, plastids and hydrogenosomes. The current settings for each of these on the taxonomic tree can be viewed with this following code list.",
+                    "@type": "dcat:Distribution",
+                    "title": "Genetic Codes"
+                },
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/Taxonomy/taxonomyhome.html/index.cgi?chapter=extinct",
+                    "description": "Extinct organisms that are represented with sequence data at GenBank",
+                    "@type": "dcat:Distribution",
+                    "title": "Extinct Organisms"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Molecular biology/Genetics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/statesystem/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-07-14",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-25",
+            "keyword": [
+                "administration and management",
+                "allocation",
+                "appropriation",
+                "awards",
+                "best practices",
+                "cessation",
+                "dollars",
+                "expenditure",
+                "federal",
+                "funding",
+                "funds",
+                "grants",
+                "health communication",
+                "interventions",
+                "money",
+                "office on smoking and health",
+                "osh",
+                "recommendation",
+                "recommended level",
+                "spending",
+                "state and community",
+                "state system",
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
+            "identifier": "https://data.cdc.gov/api/views/vw7y-v3uk",
+            "description": "1991-2016. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System.  Funding Data, Appropriations (1991-2016) and Expenditures (2008-2016).  Appropriations data show public funds allocated to/by a particular state for tobacco prevention and control.  They are not necessarily expended.  Appropriations are from four major funding sources, Federal, state, Robert Wood Johnson Foundation (RWJF), and the American Legacy Foundation (Legacy).  Expenditures are amounts spent by state tobacco control programs on tobacco prevention and control.  Expenditure data are available by CDC Best Practices Program Components (State and Community Interventions, Health Communication Interventions, Cessation Interventions, Surveillance and Evaluation, and Administration and Management). Expenditures from 2008 to 2014 are compared against 2007 CDC Best Practices Recommendations; expenditures from 2015 and forward are compared against 2014 CDC Best Practices Recommendations.",
+            "title": "University of Illinois at Chicago Health Policy Center - Funding",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vw7y-v3uk/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vw7y-v3uk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vw7y-v3uk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vw7y-v3uk/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/ege4-wxz9",
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
+            "identifier": "c21bff91-35f5-5333-9bf5-ffd895d96c6a",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "devAuto_states_measures",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/states_measures.csv",
+                    "description": "{\"dataset\": \"states_measures\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "@type": "dcat:Distribution",
+                    "title": "states_measures csv file"
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
+            "landingPage": "https://data.cms.gov/provider-compliance/cost-report/hospital-provider-cost-report",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2011-01-01/2022-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-23",
+            "references": [
+                "https://data.cms.gov/resources/hospital-provider-cost-report-methodology"
+            ],
+            "keyword": [
+                "financials",
+                "health care use & payments",
+                "hospitals & facilities",
+                "inpatient",
+                "medicare",
+                "original medicare",
+                "value-based care"
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/44060663-47d8-4ced-a115-b53b4c270acb/data-viewer",
+            "description": "The Hospital Provider Cost Report\u00a0dataset provides select measures from the hospital annual cost report. This data\u00a0includes provider information such as facility characteristics, utilization data, cost and charges by cost center (in total and for Medicare), Medicare settlement data, and financial statement data organized by CMS Certification Number.",
+            "title": "Hospital Provider Cost Report",
+            "describedByType": "application/pdf",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/44060663-47d8-4ced-a115-b53b4c270acb/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Hospital Provider Cost Report : 2022-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/b220a101-219f-47d5-acfe-1685596bc727/CostReport_2022_Final.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Provider Cost Report : 2022-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8015f175-35cc-4cab-a664-b7c87d91a027/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Provider Cost Report : 2022-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/33034296-65ab-4287-aa91-228497e69f4c/CostReport_2021_Final.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Provider Cost Report : 2021-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/16b3c471-e983-47fb-8593-56759131b098/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Provider Cost Report : 2021-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/8d78525c-4b52-4a64-a288-c87514951975/CostReport_2020_Final.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Provider Cost Report : 2020-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/485570bb-b706-44ab-8ded-27800b8264ea/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Provider Cost Report : 2020-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/8e73f828-2995-4916-ac33-20968b5a5186/CostReport_2019_Final.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Provider Cost Report : 2019-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/1f467342-5894-40fb-b02e-186d78196c2c/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Provider Cost Report : 2019-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/1ab25e07-2e0e-4994-a42b-25d7c7cbee26/CostReport_2018_Final.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Provider Cost Report : 2018-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8726fe1f-0857-41d8-a63c-ccc69edd3f63/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Provider Cost Report : 2018-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/5423482e-80c5-4008-afaa-8abefce424cf/CostReport_2017_Final.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Provider Cost Report : 2017-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9560fa2c-96b5-4da1-a9ec-b2752251edef/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Provider Cost Report : 2017-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/b90632a9-c2d2-4bf0-bf91-1b8897374902/CostReport_2016_Final.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Provider Cost Report : 2016-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d67ea70e-ab34-4d51-afac-429d8dfd6b03/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Provider Cost Report : 2016-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/5f82f9c5-e7f2-45a0-beb7-c0133ac612e3/CostReport_2015_Final.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Provider Cost Report : 2015-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3ea92c2a-8672-4b7d-a83f-4746591b6435/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Provider Cost Report : 2015-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/9e1d712b-82f1-439d-afc3-01fdbe9cf90d/CostReport_2014_Final.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Provider Cost Report : 2014-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/09ecb1c2-6dc6-4084-8db0-4c7924f7937d/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Provider Cost Report : 2014-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/c7af3e6a-d44f-4f3b-8a8f-af4f565404a6/CostReport_2013_Final.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Provider Cost Report : 2013-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8552797f-39e8-4fcd-b613-5a8eff6254bf/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Provider Cost Report : 2013-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/203f36b8-662d-453c-82ff-eeb3f3e6e834/CostReport_2012_Final.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Provider Cost Report : 2012-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/fce0b8f6-88f6-4628-a871-1b367ff6960b/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Provider Cost Report : 2012-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/37d1a219-c4dc-46bf-baf4-bb4f8a4dd4f1/CostReport_2011_Final.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Provider Cost Report : 2011-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/9bda9754-66ae-4e24-bac6-ad5ccffa4bec/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Provider Cost Report : 2011-12-02"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-03/9756088d-5280-4090-80b9-449d31ef25a3/Cost%20Report%20Data%20Dictionary%20Update.pdf",
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
+            "landingPage": "https://data.cdc.gov/d/y4x9-2nqn",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-04-26",
+            "@type": "dcat:Dataset",
+            "modified": "2019-05-30",
+            "keyword": [
+                "2019",
+                "acute",
+                "by type) a",
+                "by type) b",
+                "hemolytic uremic syndrome post-diarrheal",
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
+            "identifier": "https://data.cdc.gov/api/views/y4x9-2nqn",
+            "description": "NNDSS - TABLE 1P.  Hemolytic uremic syndrome post-diarrheal to Hepatitis (viral, acute, by type), B - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1P.  Hemolytic uremic syndrome post-diarrheal to Hepatitis (viral, acute, by type), B",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/y4x9-2nqn/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/y4x9-2nqn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/y4x9-2nqn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/y4x9-2nqn/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/6wqg-8ykc",
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
+            "identifier": "https://data.cdc.gov/api/views/6wqg-8ykc",
+            "description": "In August 2020 there were over 186,000 employees in the oil and gas extraction industry in the United States (United States Department of Labor. Bureau of Labor Statistics, 2020).  Many workers in the upstream oil extraction industry have potential risk of crude oil vapor (COV) inhalation.  There are many current knowledge gaps regarding the health effects from inhalation of complex mixtures found in crude oil vapors.  To aid research in filling these gaps, an automated system that could carefully deliver and control the COV concentration within an animal inhalation exposure chamber was needed.  The objective of this project was to develop an automated computer-controlled system to expose small laboratory animals to precise concentrations of crude oil vapor (COV).",
+            "title": "Automated oil vapor inhalation exposure system",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/6wqg-8ykc/application/x-zip-compressed",
+                    "mediaType": "application/x-zip-compressed"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "National Institute for Occupational Safety and Health"
+            ]
+        },
+        {
+            "accessLevel": "restricted public",
+            "landingPage": "https://data.cdc.gov/d/ri74-jp8e",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "issued": "2022-06-08",
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
+            "identifier": "https://data.cdc.gov/api/views/ri74-jp8e",
+            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional surveys from probability-sampled commercial survey panels. As part of a special iteration of RANDS that focuses on COVID-19, RANDS during COVID-19 Round 2 is the second round of a three-round survey. In addition to the probability sample of RANDS during COVID-19 Round 2, the questionnaire was administered to the Dynata non-probability online opt-in sample by NORC at the University of Chicago (NORC) from August 3, 2020 to August 20, 2020.  The RANDS during COVID-19 Round 2 Non-Probability Sample does not have a known survey sampling design and cannot be used to produce nationally or sub-nationally representative estimates.",
+            "title": "NCHS Research and Development Survey (RANDS) Round 2 during COVID-19 non-probability sampled Restricted File",
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
+            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS_COVID_2_np_technical_documentation.pdf",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/healthyyouth/data/yrbs/index.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-07-19",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-22",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DASH Public Inquiries",
+                "hasEmail": "mailto:nccddashinfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/svam-8dhg",
+            "description": "1991-2017. High School Dataset. The Youth Risk Behavior Surveillance System (YRBSS) monitors six categories of priority health behaviors \r\namong youth and young adults: 1) behaviors that contribute to unintentional injuries and violence; 2) tobacco use; 3) alcohol and \r\nother drug use; 4) sexual behaviors related to unintended pregnancy and sexually transmitted infections (STIs), including human \r\nimmunodeficiency virus (HIV) infection; 5) unhealthy dietary behaviors; and 6) physical inactivity. In addition, YRBSS monitors \r\nthe prevalence of obesity and asthma and other priority health behaviors.",
+            "title": "DASH - Youth Risk Behavior Surveillance System (YRBSS): High School - Excluding Sexual Identity",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/svam-8dhg/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/svam-8dhg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/svam-8dhg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/svam-8dhg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Youth-Risk-Behaviors/DASH-Youth-Risk-Behavior-Surveillance-System-YRBSS/svam-8dhg",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Youth Risk Behaviors"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/62yv-gyiz",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-04-26",
+            "@type": "dcat:Dataset",
+            "modified": "2019-05-30",
+            "keyword": [
+                "2019",
+                "age<5",
+                "confirmed",
+                "invasive pneumococcal disease",
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
+            "identifier": "https://data.cdc.gov/api/views/62yv-gyiz",
+            "description": "NNDSS - TABLE 1T. Invasive pneumococcal disease, age<5 , Confirmed to Invasive pneumococcal disease, age <5, Probable  - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 Includes drug resistant and susceptible cases of Invasive Pneumococcal Disease.",
+            "title": "NNDSS - TABLE 1T. Invasive pneumococcal disease, age<5 , Confirmed to Invasive pneumococcal disease, age <5, Probable",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/62yv-gyiz/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/62yv-gyiz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/62yv-gyiz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/62yv-gyiz/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.hrsa.gov/tools/medicare/physician-bonus",
+            "bureauCode": [
+                "009:15"
+            ],
+            "issued": "2012-05-30",
+            "temporal": "2011-01-01T00:00:00-05:00/2011-01-01T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "census tract number",
+                "community health",
+                "county subdivision",
+                "elderly",
+                "federally qualified health center",
+                "find shortage area",
+                "health care providers",
+                "health professional shortage area",
+                "hpsa",
+                "medicare",
+                "medicare physician bonus payment",
+                "mental health hpsa",
+                "poverty",
+                "primary care hpsa"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "HRSA Bureau of Health Workforce",
+                "hasEmail": "mailto:data@hrsa.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Health Resources and Services Administration"
+            },
+            "identifier": "5d9629e2-beac-4b50-bcc6-1d929e47fc36",
+            "description": "<p>The HPSAs Eligible for the Medicare Physician Bonus Payment advisor tools allows the user (physician) to determine if an address is eligible for bonus payments. Medicare makes bonus payments to physicians who provide medical care services in geographic areas that are HRSA-designated as primary medical care Health Professional Shortage Areas (HPSAs) and to psychiatrists who provide services in HRSA-designated mental health HPSAs.</p>\n<p>The search results indicate if the address is in a Primary Care HPSA or Mental Health HPSA, along with state, county name, Census Tract, zip code, and a map identifying the address.</p>",
+            "title": "Find Shortage Areas: HPSAs Eligible for the Medicare Physician Bonus Payment",
+            "programCode": [
+                "009:078"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://datawarehouse.hrsa.gov/geoHPSAAdvisor/GeographicHPSAAdvisor.aspx",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "Community",
+                "Health",
+                "Medicare"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/xajj-cnsu",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2020-09-18",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-04",
+            "keyword": [
+                "data distribution"
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/xajj-cnsu",
+            "description": "Hazardous Substances Data Bank (HSDB) was a toxicology database that focused on the toxicology of potentially hazardous chemicals. It provided information on human exposure, industrial hygiene, emergency handling procedures, environmental fate, regulatory requirements, nanomaterials, and related areas. The information in HSDB has been assessed by a Scientific Review Panel.\n\nThis version of HSDB data includes a subset of HSDB for downloading, but is no longer updated. HSDB data has been incorporated into PubChem.",
+            "title": "Hazardous Substances Data Bank (HSDB)",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/hsdblease/",
+                    "description": "Download over 5,000 hazardous substance records from HSDB.",
+                    "@type": "dcat:Distribution",
+                    "title": "Download HSDB Data"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/sample/hsdb/",
+                    "mediaType": "text/html",
+                    "title": "Download HSDB Sample Data"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/hsdblease/hsdbconv.txt",
+                    "mediaType": "text/html",
+                    "title": "HSDB Data Element Guide"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Drugs and Chemicals"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/provisional-maternal-deaths.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-03-10",
+            "@type": "dcat:Dataset",
+            "temporal": "2019-01-01/2024-09-30",
+            "modified": "2025-01-29",
+            "keyword": [
+                "age",
+                "age group",
+                "deaths",
+                "hispanic origin",
+                "maternal causes",
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
+            "identifier": "https://data.cdc.gov/api/views/e2d5-ggg7",
+            "description": "This data presents national-level provisional maternal mortality rates based on a current flow of mortality and natality data in the National Vital Statistics System. Provisional rates which are an early estimate of the number of maternal deaths per 100,000 live births, are shown as of the date specified and may not include all deaths and births that occurred during a given time period (see Technical Notes).\n\nA maternal death is the death of a woman while pregnant or within 42 days of termination of pregnancy irrespective of the duration and the site of the pregnancy, from any cause related to or aggravated by the pregnancy or its management, but not from accidental or incidental causes. In this data visualization, maternal deaths are those deaths with an underlying cause of death assigned to International Statistical Classification of Diseases, 10th Revision (ICD-10) code numbers A34, O00\u2013O95, and O98\u2013O99.\n\nThe provisional data  include reported 12 month-ending provisional maternal mortality rates overall, by age, and by race and Hispanic origin. Provisional maternal mortality rates presented in this data visualization are for \u201c12-month ending periods,\u201d defined as the number of maternal deaths per 100,000 live births occurring in the 12-month period ending in the month indicated. For example, the 12-month ending period in June 2020 would include deaths and births occurring from July 1, 2019, through June 30, 2020. Evaluation of trends over time should compare estimates from year to year (June 2020 and June 2021), rather than month to month, to avoid overlapping time periods. In the visualization and in the accompanying data file, rates based on death counts less than 20 are suppressed in accordance with current NCHS standards of reliability for rates. Death counts between 1-9 in the data file are suppressed in accordance with National Center for Health Statistics (NCHS) confidentiality standards.\n\nProvisional data presented on this page will be updated on a quarterly basis as additional records are received. Previously released estimates are revised to include data and record updates received since the previous release. As a result, the reliability of estimates for a 12-month period ending with a specific month will improve with each quarterly release and estimates for previous time periods may change as new data and updates are received.",
+            "title": "VSRR Provisional Maternal Death Counts and Rates",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/e2d5-ggg7/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/e2d5-ggg7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/e2d5-ggg7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/e2d5-ggg7/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P3M",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/eikg-657m",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-11-13",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-12",
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
+            "identifier": "648ac749-46d9-45bf-aa68-141c7d4dea45",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 11-04-2024-to-11-10-2024",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/mdrp-newly-rprt-drug-11-04-2024-to-11-10-2024.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2003",
+            "issued": "2016-05-23",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
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
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2003-nid13575",
+            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, update SAMHSA's Inventory of Substance Abuse Treatment Services (I-SATS), analyze general treatment services trends, and generate the National Directory of Drug and Alcohol Abuse Treatment Programs and its online equivalent, the Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>.<br />\nData are collected on topics including facility operation, services offered (assessment, substance abuse therapy and counseling, pharmacotherapies, testing, transitional, ancillary), primary focus (substance abuse, mental health, both, general health, other), hotline operation, Opioid Treatment Programs and medication dispensed, languages in which treatment is provided, type of treatment provided, number of clients (total and under age 18), number of beds, types of payment accepted, sliding fee scale, special programs offered, facility accreditation and licensure/certification, and managed care agreements.This study has 1 Data Set.</p>",
+            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2003)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2003-nid13575",
+                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2003) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2003-nid13575"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/e92c-t3mi",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2016-03-01",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-27",
+            "keyword": [
+                "bars",
+                "fact sheet",
+                "infographic",
+                "restaurants",
+                "secondhand smoke",
+                "smokefree",
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
+            "identifier": "https://data.cdc.gov/api/views/e92c-t3mi",
+            "description": "Explore the Going Smokefree Matters \u2013 Bars and Restaurants Infographic which outlines key facts related to the effects of secondhand smoke exposure in bars and restaurants.",
+            "title": "Going Smokefree Matters - Bars and Restaurants Infographic",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/e92c-t3mi/application/pdf",
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
+            "landingPage": "https://data.cdc.gov/d/mi28-ze7h",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-04-26",
+            "@type": "dcat:Dataset",
+            "modified": "2019-05-30",
+            "keyword": [
+                "2019",
+                "animal",
+                "human",
+                "nedss",
+                "netss",
+                "nndss",
+                "rabies",
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
+            "identifier": "https://data.cdc.gov/api/views/mi28-ze7h",
+            "description": "NNDSS - TABLE 1CC. Rabies, Animal to Rabies, Human - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1CC. Rabies, Animal to Rabies, Human",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mi28-ze7h/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mi28-ze7h/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mi28-ze7h/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mi28-ze7h/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/ekm7-cmu8",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-03-01",
+            "@type": "dcat:Dataset",
+            "modified": "2023-02-28",
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
+            "identifier": "0919b0f0-267b-4418-a585-6d3fb7e60658",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-02-20-to-2023-02-26",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rprt-drug-02202023-to-02262023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-02-20-to-2023-02-26"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/em69-hj4k",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-08-09",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-16",
+            "keyword": [
+                "py2023",
+                "qhp",
+                "qhp landscape",
+                "shop",
+                "shop market medical"
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
+            "identifier": "aa2cf0c7-ff39-484a-9472-764e243ffea9",
+            "description": "The Medical SHOP Market file of the QHP Landscape Files contains information on certified medical plans offered through an Exchange to employers in the Small Business Health Options Program (SHOP) market. These plans are also known as Qualified Health Plans (QHPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
+            "title": "QHP Landscape PY2023 Medical SHOP",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2023/shop_market_medical.zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-02-24",
+            "@type": "dcat:Dataset",
+            "modified": "2023-03-30",
+            "keyword": [
+                "age",
+                "age group",
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
+                "sex",
+                "united states",
+                "yearly"
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
+            "identifier": "https://data.cdc.gov/api/views/4ueh-89p9",
+            "description": "Deaths by educational attainment, race, sex, and age group for deaths occurring in the United States. Data are final for 2019 and provisional for 2020.  The dataset includes annual counts of death for total deaths and for COVID-19, coded to ICD-10 code U07.1 as an underlying or multiple cause of death.",
+            "title": "AH Deaths by Educational Attainment, 2019-2020",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4ueh-89p9/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4ueh-89p9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4ueh-89p9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4ueh-89p9/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-2002",
+            "issued": "2016-05-23",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
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
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2002-nid13566",
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-2002)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2002-nid13566",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-2002) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-2002-nid13566"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/medicare-shared-savings-program/number-of-accountable-care-organization-assigned-beneficiaries-by-county",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2016-01-01/2023-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-21",
+            "references": [
+                "https://data.cms.gov/resources/number-of-accountable-care-organization-assigned-beneficiaries-by-county-methodology"
+            ],
+            "keyword": [
+                "accountable care organizations",
+                "coordinated care",
+                "medicare",
+                "original medicare",
+                "payment models",
+                "value-based care"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Shared Savings Program - CM",
+                "hasEmail": "mailto:SharedSavingsProgram@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/ae8c9418-acc9-4442-b217-33291448f6b8/data-viewer",
+            "description": "The Shared Savings Program Number of Accountable Care Organization Assigned Beneficiaries by County dataset provides aggregate data of total assigned beneficiaries by Shared Savings Program ACO for each county where at least one of their assigned beneficiaries resides. Assigned beneficiary person-year counts are based on certified Shared Savings Program ACO Participant Lists and assignment methodology for that performance year.\n\n\u00a0\n\nDISCLAIMER: This information is current as of the last update. Changes to Shared Savings Program ACO information occur periodically. Each Shared Savings Program ACO has the most up-to-date information about their organization. Consider contacting the Shared Savings Program ACO for the latest information. Contact information is available in the ACO Public Use File (PUF) and the ACO Participants PUF.",
+            "title": "Number of Accountable Care Organization Assigned Beneficiaries by County",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ae8c9418-acc9-4442-b217-33291448f6b8/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Number of Accountable Care Organization Assigned Beneficiaries by County : 2023-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/8a74dd30-06a1-4751-beee-dc0dd3c9d609/Number_Of_ACO_Assigned_Beneficiaries_by_County_PUF_2023_01_01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Number of Accountable Care Organization Assigned Beneficiaries by County : 2023-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4f64f8d2-f62b-4690-8ce4-85a9cf9adb76/data",
+                    "mediaType": "text/html",
+                    "title": "Number of Accountable Care Organization Assigned Beneficiaries by County : 2023-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/821b7023-f0e9-4452-90ce-eea7db1609d0/Number_Of_ACO_Assigned_Beneficiaries_by_County_PUF_2022_01_01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Number of Accountable Care Organization Assigned Beneficiaries by County : 2022-02-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7071eb0c-71b6-450d-b3c2-077a3166ed46/data",
+                    "mediaType": "text/html",
+                    "title": "Number of Accountable Care Organization Assigned Beneficiaries by County : 2022-02-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-09/112e507f-41e0-4c26-8ac5-5fb64e0fc0d0/Number_Of_ACO_Assigned_Beneficiaries_by_County_PUF_2021_01_01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Number of Accountable Care Organization Assigned Beneficiaries by County : 2021-01-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/95490093-9f62-4566-b9bf-693d2a00fe08/data",
+                    "mediaType": "text/html",
+                    "title": "Number of Accountable Care Organization Assigned Beneficiaries by County : 2021-01-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/d1575906-dc3e-4b88-a661-2f202753017b/Number_Of_ACO_Assigned_Beneficiaries_by_County_PUF_2020_01_01.csv",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Number of Accountable Care Organization Assigned Beneficiaries by County : 2020-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/cff04cbb-6267-47ec-b69d-7a2315b36df3/data",
+                    "mediaType": "text/html",
+                    "title": "Number of Accountable Care Organization Assigned Beneficiaries by County : 2020-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/c78a5b90-8011-4d99-bc51-b178b9a559c3/Number_Of_ACO_Assigned_Beneficiaries_by_County_PUF_2019_07_01.csv",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Number of Accountable Care Organization Assigned Beneficiaries by County : 2019-07-01oc1"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d73a38fb-2e6e-469f-b369-f685fd45f424/data",
+                    "mediaType": "text/html",
+                    "title": "Number of Accountable Care Organization Assigned Beneficiaries by County : 2019-07-01oc1"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/24b5f85e-8f9f-468e-8b69-75d635f55cb0/Number_Of_ACO_Assigned_Beneficiaries_by_County_PUF_2019_01_01.csv",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Number of Accountable Care Organization Assigned Beneficiaries by County : 2019-01-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d076f7f0-536a-4944-aa56-8930ced2a06d/data",
+                    "mediaType": "text/html",
+                    "title": "Number of Accountable Care Organization Assigned Beneficiaries by County : 2019-01-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/d15accad-7f46-4e5e-b091-d4cff3f99c49/Number_Of_ACO_Assigned_Beneficiaries_by_County_PUF_2018_01_01.csv",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Number of Accountable Care Organization Assigned Beneficiaries by County : 2018-01-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ee439bd7-ac96-43aa-99c7-86e5c8ede0bc/data",
+                    "mediaType": "text/html",
+                    "title": "Number of Accountable Care Organization Assigned Beneficiaries by County : 2018-01-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/51755439-0b6b-4011-a64d-7a04b9bbe7a2/Number_Of_ACO_Assigned_Beneficiaries_by_County_PUF_2017_01_01.csv",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Number of Accountable Care Organization Assigned Beneficiaries by County : 2017-01-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c2b153f1-8354-4132-b6ac-9817023db82f/data",
+                    "mediaType": "text/html",
+                    "title": "Number of Accountable Care Organization Assigned Beneficiaries by County : 2017-01-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/d0115d47-f252-43eb-8647-59d0b611e3ed/Number_Of_ACO_Assigned_Beneficiaries_by_County_PUF_2016_01_01.csv",
+                    "mediaType": "application/vnd.ms-excel",
+                    "title": "Number of Accountable Care Organization Assigned Beneficiaries by County : 2016-01-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ff0d442b-8c0d-44ba-b8cd-6e392e30fab0/data",
+                    "mediaType": "text/html",
+                    "title": "Number of Accountable Care Organization Assigned Beneficiaries by County : 2016-01-15"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/number-of-accountable-care-organization-assigned-beneficiaries-by-county-data-dictionary-2023",
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
+            "landingPage": "https://healthdata.gov/d/enbs-qir9",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-08-10",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-08",
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
+            "identifier": "b087ed0a-861b-5562-aac7-239348af8c82",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "Scorecard VERSION v0.3.58-test (local)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/0.3.58-test/20230728/VERSION.csv",
+                    "description": "Scorecard VERSION v0.3.58-test (local)",
+                    "@type": "dcat:Distribution",
+                    "title": "Scorecard VERSION v0.3.58-test (local)"
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
+            "landingPage": "https://www.cdc.gov/brfss/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-07-18",
+            "@type": "dcat:Dataset",
+            "modified": "2024-09-19",
+            "references": [
+                "http://www.cdc.gov/brfss"
+            ],
+            "keyword": [
+                "...",
+                "behavioral",
+                "brfss",
+                "factor",
+                "risk",
+                "survey"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DPH Public Inquiries",
+                "hasEmail": "mailto:PublicInquiriesDPH@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/dttw-5yxu",
+            "description": "2011 to present. BRFSS combined land line and cell phone prevalence data. BRFSS is a continuous, state-based surveillance system that collects information about modifiable risk factors for chronic diseases and other leading causes of death. Data will be updated annually as it becomes available. Detailed information on sampling methodology and quality assurance can be found on the BRFSS website (http://www.cdc.gov/brfss). Methodology: http://www.cdc.gov/brfss/factsheets/pdf/DBS_BRFSS_survey.pdf Glossary: https://data.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factor-Surveillance-System-BRFSS-H/iuq5-y9ct",
+            "title": "Behavioral Risk Factor Surveillance System (BRFSS) Prevalence Data (2011 to present)",
+            "describedByType": "application/pdf",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dttw-5yxu/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dttw-5yxu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dttw-5yxu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dttw-5yxu/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "http://www.cdc.gov/brfss/factsheets/pdf/DBS_BRFSS_survey.pdf",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Behavioral Risk Factors"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/u92k-ms37",
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
+                "vibriosis confirmed",
+                "vibriosis probable",
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
+            "identifier": "https://data.cdc.gov/api/views/u92k-ms37",
+            "description": "NNDSS - TABLE 1LL. Vibriosis, Confirmed to Vibriosis, Probable - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1LL. Vibriosis, Confirmed to Vibriosis, Probable",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/u92k-ms37/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/u92k-ms37/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/u92k-ms37/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/u92k-ms37/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/epau-tsqw",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-02-14",
+            "@type": "dcat:Dataset",
+            "modified": "2024-02-07",
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
+            "identifier": "9951c048-36b7-4c93-aa4f-e34546836e2e",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2024-01-29-to-2024-02-04",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/mdrp-newly-rprt-drug-01-29-2024-to-02-04-2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2024-01-29-to-2024-02-04"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/epfe-db87",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2016-07-13",
+            "@type": "dcat:Dataset",
+            "modified": "2018-12-20",
+            "keyword": [
+                "continuous eligibility",
+                "enrollment strategies"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Medicaid.gov",
+                "hasEmail": "mailto:no-reply@data.medicaid.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "cdb769be-0d7b-524b-9d25-2062d36b60ab",
+            "description": "States have the option to provide children with 12 months of continuous coverage through Medicaid and CHIP, even if the family experiences a change in income during the year. Continuous eligibility is a valuable tool that helps States ensure that children stay enrolled in the health coverage for which they are eligible and have consistent access to needed health care services.",
+            "title": "Continuous Eligibility for Medicaid and CHIP Coverage",
+            "programCode": [
+                "009:076"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/continuous-eligibility-for-medicaid-and-chip-coverage.gz34-pjff.csv",
+                    "mediaType": "text/csv",
+                    "title": "CSV"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P10Y",
+            "theme": [
+                "Eligibility"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/eqkd-7gq3",
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
+            "identifier": "cc7f1f2d-8942-5b67-a9fe-e48033c972d2",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
+            "title": "prodAuto_measure_compare",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_compare.csv",
+                    "description": "{\"dataset\": \"measure_compare\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
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
+            "landingPage": "https://healthdata.gov/d/eqqh-qat3",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-04-06",
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
+            "identifier": "78d44223-b50f-5a31-91d3-ac9b2b609556",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "Scorecard pillar v2.11.16 (dev)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.16/20241107/pillar.csv",
+                    "description": "Scorecard pillar v2.11.16 (dev)",
+                    "@type": "dcat:Distribution",
+                    "title": "Scorecard pillar v2.11.16 (dev)"
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
+            "landingPage": "https://brads.nichd.nih.gov/Home/",
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
+                "fn": "Songco, David",
+                "hasEmail": "mailto:songcod@mail.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
+            "identifier": "77e6b5dd-989d-415f-b91b-252c6196cc22",
+            "description": "<p>BRADS is a repository for data and biospecimens from population health research initiatives and clinical or interventional trials designed and implemented by NICHD\u2019s Division of Intramural Population Health Research (DIPHR). Topics include human reproduction and development, pregnancy, child health and development, and women\u2019s health. The website is maintained by DIPHR.</p>",
+            "title": "Biospecimen Repository Access and Data Sharing (BRADS)",
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
+            "landingPage": "https://data.cdc.gov/d/2993-4v7d",
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
+            "identifier": "https://data.cdc.gov/api/views/2993-4v7d",
+            "description": "NNDSS - TABLE 1II. Tetanus to Trichinellosis - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1II. Tetanus to Trichinellosis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2993-4v7d/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2993-4v7d/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2993-4v7d/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2993-4v7d/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/dataset/dailymed-webservices",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2012-05-30",
+            "temporal": "2005-01-01T00:00:00-05:00/2005-01-01T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "drug labeling",
+                "pharmaceutical preparations",
+                "treatments",
+                "united states"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
+            "identifier": "4a86be2e-023b-47a2-bd8a-c112bbcc08e4",
+            "description": "<p>The DailyMed RESTful API is a web service for accessing current SPL information. It is implemented using HTTP and can be thought of as a collection of resources, specified as URLs.</p>",
+            "title": "DailyMed Webservices",
+            "programCode": [
+                "009:048"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://dailymed.nlm.nih.gov/dailymed/help.cfm#webservices",
+                    "mediaType": "text/html",
+                    "title": "API"
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
+            "identifier": "https://data.cdc.gov/api/views/66cx-b9a4",
+            "description": "2010-2020.  National Quitline Data Warehouse (NQDW). State Tobacco Activities Tracking and Evaluation (STATE) System.  NQDW Data.  National Quitline Data Warehouse (NQDW) assists in evaluating quitline activities and serves as a national resource for data on the use, success, and services of state quitlines.  States report data on quitline callers, quitting success, as well as the services provided by their quitlines. The NQDW consolidates this information for evaluating programs and improving quitline services.  The jurisdictions participating in this data collection effort include the 50 states, the District of Columbia, Guam and Puerto Rico.",
+            "title": "Quitline \u2013 Services Available \u2013 Counseling - 2010 To Present",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/66cx-b9a4/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/66cx-b9a4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/66cx-b9a4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/66cx-b9a4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Quitline/Quitline-Services-Available-Counseling-2010-To-Pre/66cx-b9a4",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "theme": [
+                "Quitline"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/covid19/covid-19-mortality-data-files.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-02-03",
+            "@type": "dcat:Dataset",
+            "modified": "2023-03-30",
+            "keyword": [
+                "age",
+                "age group",
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
+            "identifier": "https://data.cdc.gov/api/views/3ts8-hsrw",
+            "description": "Provisional counts of deaths in the United States by educational attainment, race, sex, and age group. The dataset includes cumulative provisional counts of death for COVID-19, coded to ICD-10 code U07.1 as an underlying or multiple cause of death.",
+            "title": "AH Provisional COVID-19 Deaths by Educational Attainment, Race, Sex, and Age",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3ts8-hsrw/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3ts8-hsrw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3ts8-hsrw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3ts8-hsrw/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-04-11",
+            "temporal": "1997/2019",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-30",
+            "keyword": [
+                "adults",
+                "american indian or alaska native",
+                "asian",
+                "black or african american",
+                "children and adolescents",
+                "education",
+                "female",
+                "functional limitation status",
+                "health insurance",
+                "hispanic or latino",
+                "male",
+                "medicaid",
+                "metropolitan and nonmetropolitan",
+                "mexican",
+                "multiple race",
+                "native hawaiian or other pacific islander",
+                "poverty",
+                "region",
+                "rural population",
+                "urban population",
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
+            "identifier": "https://data.cdc.gov/api/views/hdja-ybdg",
+            "description": "Data on Medicaid coverage among people under age 65, in the United States, by selected population characteristics. Data from Health, United States. SOURCE: National Center for Health Statistics, National Health Interview Survey.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
+            "title": "DQS Medicaid coverage among persons under age 65, by selected characteristics: United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hdja-ybdg/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hdja-ybdg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hdja-ybdg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hdja-ybdg/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.healthit.gov/data/datasets/onc-regional-extension-centers-rec-key-performance-indicators-kpis-county",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-10-03",
+            "@type": "dcat:Dataset",
+            "modified": "2015-06-01",
+            "keyword": [
+                "county",
+                "health information technology",
+                "health it",
+                "health it data",
+                "indicators",
+                "rec",
+                "regional extension centers"
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
+            "identifier": "x2u52lga-mizz-kkra-dbv4-fg6qmi4a0mfh",
+            "description": "The ONC Regional Extension Centers (REC) Program provides assistance to health care providers to adopt and meaningfully use certified EHR technology. The program, funded through the American Recovery and Reinvestment Act (ARRA) or The Recovery Act, provides grants to organizations, Regional Extension Centers, that assist providers directly in the organization's region. There are 62 unique RECs across the United States. This data set provides county-level health care professional participation in the REC Program. You can track metrics on the total primary care and non-primary care providers that signed up for REC assistance, gone live with an EHR, and demonstrated meaningful use of certified EHR technology. See ONC's REC data by state to track these metrics at the county level.",
+            "title": "ONC Regional Extension Centers (REC) Key Performance Indicators (KPIs) by County",
+            "programCode": [
+                "009:110"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/REC_KPI_County.csv",
+                    "mediaType": "text/csv",
+                    "title": "REC_KPI_County.csv"
+                }
+            ],
+            "describedBy": "https://www.healthit.gov/data/datasets/onc-regional-extension-centers-rec-key-performance-indicators-kpis-county"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-daily-air-temperatures-and-heat-index",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2012-08-03",
+            "temporal": "1979-01-01T00:00:00-05:00/2010-12-31T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "air temperature",
+                "heat index climate state county day month year remotely sensed",
+                "other"
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
+            "identifier": "96b92ba4-d63a-40ac-820b-f955d9f0f0f9",
+            "description": "<p>The Daily Air Temperature and Heat Index data available on CDC WONDER are county-level daily average air temperatures and heat index measures spanning the years 1979-2010. Temperature data are available in Fahrenheit or Celsius scales. Reported measures are the average temperature, number of observations, and range for the daily maximum and minimum air temperatures, and also percent coverage for the daily maximum heat index. Data are available by place (combined 48 contiguous states, region, division, state, county), time (year, month, day) and specified maximum and minimum air temperature, and heat index value. The data are derived from the North America Land Data Assimilation System (NLDAS) through NLDAS Phase 2, a collaboration project among several groups: the National Oceanic and Atmospheric Administration (NOAA) National Centers for Environmental Prediction (NCEP) Environmental Modeling Center (EMC), the National Aeronautics and Space Administration (NASA) Goddard Space Flight Center (GSFC), Princeton University, the National Weather Service (NWS) Office of Hydrological Development (OHD), the University of Washington, and the NCEP Climate Prediction Center (CPC). In a study funded by the NASA Applied Sciences Program/Public Health Program, scientists at NASA Marshall Space Flight Center/ Universities Space Research Association developed the analysis to produce the data available on CDC WONDER.</p>",
+            "title": "CDC WONDER: Daily Air Temperatures and Heat Index",
+            "programCode": [
+                "010:167"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://wonder.cdc.gov/nasa-nldas.html",
+                    "mediaType": "text/html",
+                    "title": "Text "
+                }
+            ],
+            "describedBy": "http://wonder.cdc.gov/wonder/help/nldas.html",
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "State"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/statesystem/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-07-14",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-25",
+            "references": [
+                "https://chronicdata.cdc.gov/d/fip8-rcng"
+            ],
+            "keyword": [
+                "average cost per pack",
+                "cigarette sales",
+                "office on smoking and health",
+                "osh",
+                "tax",
+                "tax burden on tobacco"
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
+            "identifier": "https://data.cdc.gov/api/views/7nwe-3aj9",
+            "description": "1970-2019. Orzechowski and Walker. Tax Burden on Tobacco. Tax burden data was obtained from the annual compendium on tobacco revenue and industry statistics, The Tax Burden on Tobacco. Data are reported on an annual basis; Data include federal and state-level information regarding taxes applied to the price of a pack of cigarettes.",
+            "title": "The Tax Burden on Tobacco, 1970-2019",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7nwe-3aj9/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7nwe-3aj9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7nwe-3aj9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7nwe-3aj9/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Policy/The-Tax-Burden-on-Tobacco-1970-2018/7nwe-3aj9",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "theme": [
+                "Policy"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/aco-realizing-equity-access-and-community-health/aco-realizing-equity-access-and-community-health-eligible-beneficiaries",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-05-26",
+            "temporal": "2021-01-01/2021-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2024-01-12",
+            "references": [
+                "https://data.cms.gov/resources/aco-realizing-equity-access-and-community-health-aco-reach-model-methodology"
+            ],
+            "keyword": [
+                "accountable care organizations",
+                "coordinated care",
+                "medicare",
+                "original medicare",
+                "payment models",
+                "value-based care"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "ACO REACH - CMMI",
+                "hasEmail": "mailto:ACOREACH@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/54551982-39a8-4744-90f6-c38bb4dd5108/data-viewer",
+            "description": "Accountable Care Organization Realizing Equity, Access and Community Health (ACO REACH) Model Eligible Beneficiary Public Use File (PUF) data details Medicare Beneficiaries who were used as the reference population for comparison to aligned to the ACO REACH Model, formerly Global and Professional Direct Contracting (GPDC) Model, including average risk scores and eligibility months. This data is redacted and does not include identifiable information.",
+            "title": "ACO Realizing Equity, Access and Community Health Eligible Beneficiaries",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/54551982-39a8-4744-90f6-c38bb4dd5108/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "ACO Realizing Equity, Access and Community Health Eligible Beneficiaries : 2021-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/ELIG_BENE_PUF_REDACT.csv",
+                    "mediaType": "text/csv",
+                    "title": "ACO Realizing Equity, Access and Community Health Eligible Beneficiaries : 2021-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5941f9b8-9d72-44a1-a102-f8386c155290/data",
+                    "mediaType": "text/html",
+                    "title": "ACO Realizing Equity, Access and Community Health Eligible Beneficiaries : 2021-12-01"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/aco-reach-eligible-beneficiary-data-dictionary",
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
+            "landingPage": "https://data.cdc.gov/d/2nf2-f75n",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-12-12",
+            "@type": "dcat:Dataset",
+            "modified": "2023-12-12",
+            "keyword": [
+                "united states"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Spiro Tsipianitis",
+                "hasEmail": "mailto:cgw0@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/2nf2-f75n",
+            "description": "This is a dataset manually created by Spiro Tsipianitis via data.cdc.gov",
+            "title": "dhds_dataset",
+            "programCode": [
+                "009:022"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2nf2-f75n/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2nf2-f75n/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2nf2-f75n/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/2nf2-f75n/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Web Metrics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/adultvaxview/index.html and https://www.cdc.gov/flu/fluvaxview/index.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-05-13",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-13",
+            "keyword": [
+                "immunization",
+                "influenza",
+                "pregnancy & vaccinations",
+                "td",
+                "tdap",
+                "vaccination",
+                "vaccination coverage",
+                "vaxviews"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NCIRD",
+                "hasEmail": "mailto:VaxView@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/h7pm-wmjc",
+            "description": "Vaccination Coverage among Pregnant Women\n\n\u2022 Data on influenza and tetanus toxoid, reduced diphtheria toxoid, and acellular pertussis (Tdap) vaccination coverage at the state level from the Pregnancy Risk Assessment Monitoring System (PRAMS) for women who had a recent live birth by age and race/ethnicity.\n\n\u2022 Additional information available at https://www.cdc.gov/vaccines/imz-managers/coverage/adultvaxview/index.html and https://www.cdc.gov/flu/fluvaxview/index.htm",
+            "title": "Vaccination Coverage among Pregnant Women",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/h7pm-wmjc/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/h7pm-wmjc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/h7pm-wmjc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/h7pm-wmjc/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/8n2k-mkiw",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-01-03",
+            "@type": "dcat:Dataset",
+            "modified": "2019-01-03",
+            "keyword": [
+                "2018",
+                "babesiosis",
+                "campylobacteriosis",
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
+            "identifier": "https://data.cdc.gov/api/views/8n2k-mkiw",
+            "description": "NNDSS - Table II. Babesiosis to Campylobacteriosis - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html \r\n\r\nFootnotes:\r\n\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.",
+            "title": "NNDSS - Table II. Babesiosis to Campylobacteriosis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8n2k-mkiw/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8n2k-mkiw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8n2k-mkiw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8n2k-mkiw/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/evma-y6ey",
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
+            "identifier": "8f7c327d-2add-5168-9837-6c55a6826f37",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "featAuto_states_measures",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/states_measures.csv",
+                    "description": "{\"dataset\": \"states_measures\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "@type": "dcat:Distribution",
+                    "title": "states_measures csv file"
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
+            "landingPage": "https://www.ncbi.nlm.nih.gov/projects/linkout/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2022-02-08",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "library services",
+                "literature",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/526z-s65v",
+            "description": "LinkOut is a service that allows you to link directly from PubMed and other NCBI databases to a wide range of information and services beyond the NCBI systems. LinkOut aims to facilitate access to relevant online resources in order to extend, clarify, and supplement information found in NCBI databases.\n\nThird parties can link directly from PubMed and other Entrez database records to relevant Web-accessible resources beyond the Entrez system. Includes full-text publications, biological databases, consumer health information and research tools.",
+            "title": "Library LinkOut",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/projects/linkout/",
+                    "mediaType": "text/html",
+                    "title": "Library LinkOut Query Interface"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Research"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/dhdsp/index.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-08-11",
+            "@type": "dcat:Dataset",
+            "modified": "2024-04-09",
+            "references": [
+                "https://www.cdc.gov/dhdsp/index.htm",
+                "https://www.cdc.gov/dhdsp/maps/dtm/data_sources.htm",
+                "https://www.cdc.gov/dhdsp/maps/dtm/data_risks.htm"
+            ],
+            "keyword": [
+                "brfss",
+                "cardiovascular disease",
+                "coronary heart disease",
+                "hypertension",
+                "risk factors",
+                "stroke"
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
+            "identifier": "https://data.cdc.gov/api/views/ikwk-8git",
+            "description": "2011\u20132020. BRFSS is a continuous, state-based surveillance system that collects information about modifiable risk factors for chronic diseases and other leading causes of death. Indicators from this data source have been computed by personnel in CDC's Division for Heart Disease and Stroke Prevention (DHDSP). This was one of the datasets provided by the National Cardiovascular Disease Surveillance System and presented on DHDSP\u2019s Data, Trends, and Maps online tool. This tool was retired in April of 2024 and this dataset will not be updated. Contact dhdsprequests@cdc.gov if you need assistance with data previously included in this dataset. The data are organized by location (national, regional, state, and selected sites) and indicator, and they include CVDs (e.g., heart failure) and risk factors (e.g., hypertension). The data can be plotted as trends and stratified by age group, sex, and race/ethnicity.",
+            "title": "Behavioral Risk Factor Surveillance System (BRFSS) -  National Cardiovascular Disease Surveillance Data",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ikwk-8git/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ikwk-8git/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ikwk-8git/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ikwk-8git/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/dataset/Behavioral-Risk-Factor-Surveillance-System-BRFSS-N/fwns-azgu",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Heart Disease & Stroke Prevention"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/ewng-ywsi",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-10-31",
+            "@type": "dcat:Dataset",
+            "modified": "2023-10-30",
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
+            "identifier": "f9923173-d3c6-4a3f-91e3-48fc7df6f209",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-10-23-to-2023-10-29",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rprt-drug-10-23-2023-to-10-29-2023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-10-23-to-2023-10-29"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/ewnm-busu",
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
+            "identifier": "fc93a1e1-dca9-557b-95bf-ba92017c8794",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "featAuto_measure_backgroundAndMethods",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measure_backgroundAndMethods.csv",
+                    "description": "{\"dataset\": \"measure_backgroundAndMethods\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "@type": "dcat:Distribution",
+                    "title": "measure_backgroundAndMethods csv file"
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
+            "landingPage": "https://data.cdc.gov/d/j63e-g9bn",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-15",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Physical Effects Research Branch, Health Effects Laboratory Division",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/j63e-g9bn",
+            "description": "The anterior and posterior superior iliac spine markers are commonly used to define the pelvis, and these markers are predisposed to occlusion during three-dimensional motion capture. The occlusion of these markers leads to the use of various tracking marker configurations on the pelvis, which can create differences in kinematic results. The purpose of this investigation was to examine the agreement of CODA pelvis kinematic results when two different tracking marker configurations were used during ergonomic roofing tasks. Three-dimensional motion data was collected on seven male subjects while mimicking a standing and kneeling roofing task. Hip joint angles were computed using the CODA pelvis with two different tracking marker configurations, the Trochanter Tracking Method (TTM), and the Virtual Pelvis Tracking Method (VPTM).",
+            "title": "Agreement of hip kinematics between two tracking marker configurations used with the 1 CODA pelvis during ergonomic roofing tasks",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/j63e-g9bn/application/x-zip-compressed",
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
+            "landingPage": "https://healthdata.gov/d/ex43-2u8q",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-04-20",
+            "@type": "dcat:Dataset",
+            "modified": "2023-04-19",
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
+            "identifier": "0131a022-958f-45d1-a746-f937bc916c6d",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-04-10-to-2023-04-16",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rprt-drug-4-10-2023-to-4-16-2023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-04-10-to-2023-04-16"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/exyz-4spk",
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
+            "identifier": "beaedcae-1ff6-4c66-b8e2-5ac43751436b",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 20210816 to 20210822",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rpt-drugs-aug-20210816-to-20210822.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/mkyn-icix",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-15",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Division of Safety Research Analysis and Field Evaluations Branch",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/mkyn-icix",
+            "description": "It is widely acknowledged that there are costs involved with fatal injury to workers. These costs cross numerous boundaries, and generally address the overall costs to victims and the affected groups, and to society as a whole. This represents a cause for concern to employers, worker groups, policy makers, medical personnel, economists and others interested in workplace safety and health. This broad-reaching burden can include social costs, organizational costs, familial and interpersonal group costs, as well as personal costs such as suffering and loss of companionship. The data in the accompanying tables focus on monetary costs of fatal occupational injury which largely consist of foregone wages, but also include the direct costs of medical care and the indirect costs of household production and certain ancillary measures.\n\nThese data represent a continuation of prior research by the National Institute for Occupational Safety and Health (NIOSH) that attempted to delimit the economic consequences of workplace injury for earlier years. Interested parties should be aware that these data serve as a supplemental update to prior NIOSH publications which described the magnitude and circumstances of occupational injury deaths for earlier years 1,2.\n\nThe current data build on this research, and the findings are compelling. Over the period studied, 2003-2010, the costs from these 42,380 premature deaths exceeded $44 billion, an amount greater than the reportable gross domestic product for some States. These findings inform the national will to reduce this severe toll on our nation\u2019s workers, institutions, communities, and the nation itself. Researchers and concerned parties within the occupational and public health professions, academia, organizations focusing on workplace safety, labor unions and the business community have all proven to be willing and avid users of this data, and have used this research to continue their efforts, in concert with continuing NIOSH research efforts, to reduce the great toll that injury imposes on our workers, workplaces, and Nation.",
+            "title": "Economic Burden of Occupational Fatal Injuries in the United States Based on the Census of Fatal Occupational Injuries, 2003-2010",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/mkyn-icix/application/x-zip-compressed",
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
+            "landingPage": "https://data.cdc.gov/d/4u7c-2g4q",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-15",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Pathology and Physiology Research Branch, Health Effects Laboratory Division",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/4u7c-2g4q",
+            "description": "The toxicity of boron nitride nanotubes (BNNTs) is confounded by the various manufacturing and purification strategies employed targeted to remove 30-60% of the residuals and impurities. Four BNNTs manufactured by the induction thermal plasma process allowed us to assess the influence of these residuals/impurities on the toxicity profile of BNNTs by producing a gradient of BNNT purity levels through sequential gas purification, and water and solvent washing, followed by filtration. Extensive characterization including Infrared, x-ray spectroscopy, thermogravimetric analysis, size, charge, surface area and density allowed characterization of the alteration in physicochemical properties as the material went through sequential purification. The material from each step was screened using acellular and in vitro assays that evaluated general toxicity, mechanisms of toxicity and macrophage function.",
+            "title": "Influence of Impurities from Manufacturing Process on the Toxicity Profile of Boron Nitride Nanotubes",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/4u7c-2g4q/application/x-zip-compressed",
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
+            "landingPage": "https://healthdata.gov/d/ezer-ms4j",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-03-28",
+            "@type": "dcat:Dataset",
+            "modified": "2023-03-24",
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
+            "identifier": "e8ec5dc4-7904-52d4-8ce9-73c2fb188514",
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
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1997",
+            "issued": "2016-05-23",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "alcohol abuse",
+                "alcohol consumption",
+                "amphetamines",
+                "barbiturates",
+                "cocaine",
+                "demographic characteristics",
+                "drug abuse",
+                "drugs",
+                "drug use",
+                "hallucinogens",
+                "health care",
+                "health insurance",
+                "heroin",
+                "households",
+                "inhalants",
+                "marijuana",
+                "mental health",
+                "mental health services",
+                "methamphetamine",
+                "offenses",
+                "prescriptions drugs",
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
+            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1997-nid13619",
+            "description": "<p>This series measures the prevalence and correlates of drug<br />\nuse in the United States. The surveys are designed to provide<br />\nquarterly, as well as annual, estimates. Information is provided on<br />\nthe use of illicit drugs, alcohol, and tobacco among members of United<br />\nStates households aged 12 and older. Questions include age at first<br />\nuse as well as lifetime, annual, and past-month usage for the<br />\nfollowing drug classes: marijuana, cocaine (and crack), hallucinogens,<br />\nheroin, inhalants, alcohol, tobacco, and nonmedical use of<br />\nprescription drugs, including psychotherapeutics. Respondents were<br />\nalso asked about substance abuse treatment history, illegal<br />\nactivities, problems resulting from the use of drugs, personal and<br />\nfamily income sources and amounts, need for treatment for drug or<br />\nalcohol use, criminal record, and needle-sharing. Questions on mental<br />\nhealth and access to care, which were introduced in the 1994-B<br />\nquestionnaire (see NATIONAL HOUSEHOLD SURVEY ON DRUG ABUSE, 1994), were retained in this administration of the survey. In<br />\n1996, the section on risk/availability of drugs was reintroduced, and<br />\nsections on driving behavior and personal behavior were added (see<br />\nNATIONAL HOUSEHOLD SURVEY ON DRUG ABUSE, 1996). The 1997<br />\nquestionnaire continued the risk/availability section along with new<br />\nitems about the use of cigars, people present when respondents used<br />\nmarijuana or cocaine for the first time (if applicable), reasons for<br />\nusing these two drugs the first time, reasons for using these two<br />\ndrugs in the past year, reasons for discontinuing use of these two<br />\ndrugs (for lifetime but not past-year users), and reasons respondents<br />\nnever used these two drugs. In addition, a new series of questions<br />\nasked only of respondents aged 12 to 17 was introduced. These items<br />\ncovered a variety of topics that may be associated with substance use<br />\nand related behaviors, such as exposure to substance abuse prevention<br />\nand education programs, gang involvement, relationship with parents,<br />\nand substance use by friends. Demographic data include gender, race,<br />\nage, ethnicity, marital status, educational level, job status, income<br />\nlevel, veteran status, and current household composition.This study has 1 Data Set.</p>",
+            "title": "National Household Survey on Drug Abuse (NHSDA-1997)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1997-nid13619",
+                    "description": "National Household Survey on Drug Abuse (NHSDA-1997) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1997-nid13619"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/yvsw-8ht9",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-04-26",
+            "@type": "dcat:Dataset",
+            "modified": "2019-05-30",
+            "keyword": [
+                "2019",
+                "mumps",
+                "nedss",
+                "netss",
+                "nndss",
+                "novel influenza a virus infections",
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
+            "identifier": "https://data.cdc.gov/api/views/yvsw-8ht9",
+            "description": "NNDSS - TABLE 1Y. Mumps to Novel influenza A virus infections - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \r\n\u00a7 Novel influenza A virus infections are human infections with influenza A viruses that are different from currently circulating human seasonal influenza viruses. With the exception of one avian lineage influenza A (H7N2) virus, all novel influenza A virus infections reported to CDC since 2012 have been variant influenza viruses.",
+            "title": "NNDSS - TABLE 1Y. Mumps to Novel influenza A virus infections",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yvsw-8ht9/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yvsw-8ht9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yvsw-8ht9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/yvsw-8ht9/rows.xml?accessType=DOWNLOAD",
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
+            "issued": "2024-05-01",
+            "@type": "dcat:Dataset",
+            "modified": "2024-05-01",
+            "references": [
+                "https://www.census.gov/content/dam/Census/programs-surveys/acs/about/ACS_Information_Guide.pdf",
+                "https://www.cdc.gov/visionhealth/vehss/data/national-surveys/american-community-survey.html"
+            ],
+            "keyword": [
+                "acs",
+                "contact lenses",
+                "glasses",
+                "visual function"
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
+            "identifier": "https://data.cdc.gov/api/views/thir-stei",
+            "description": "2014 - 2022 (excluding 2020). This dataset is a de-identified summary table of vision and eye health data indicators from ACS, stratified by all available combinations of age group, race/ethnicity, gender, and state. ACS is an annual nationwide survey conducted by the U.S. Census Bureau that collects information on demographic, social, economic, and housing characteristics of the U.S. population. Approximate sample size is 3 million annually. ACS data for VEHSS includes one question related to Visual Function. Data were suppressed for cell sizes less than 30 persons, or where the relative standard error more than 30% of the mean. Data will be updated as it becomes available. Detailed information on VEHSS ACS analyses can be found on the VEHSS ACS webpage (link). Additional information about ACS can be found on the U.S. Census Bureau website (https://www.census.gov/content/dam/Census/programs-surveys/acs/about/ACS_Information_Guide.pdf). The VEHSS ACS dataset was last updated April 2024",
+            "title": "American Community Survey (ACS) \u2013 Vision and Eye Health Surveillance",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/thir-stei/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/thir-stei/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/thir-stei/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/thir-stei/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/d/thir-stei",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "theme": [
+                "Vision & Eye Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://ii.nlm.nih.gov/Web_API/index.shtml",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2012-08-22",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "api",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/n87j-59eu",
+            "description": "The SKR Project was initiated at NLM in order to develop programs to provide usable semantic representation of biomedical free text by building on resources currently available at the library. The SKR project is concerned with reliable and effective management of the information encoded in natural language texts. The project develops programs that provide usable semantic representation of biomedical text by building on resources currently available at the Library, especially the UMLS knowledge sources and the natural language processing tools provided by the SPECIALIST system. This Java-based API to the Semantic Knowledge Representation (SKR) Scheduler facility was created to provide users with the ability to programmatically submit jobs to the Scheduler Batch and Interactive facilities instead of using the Web-based interface.",
+            "title": "Semantic Knowledge Representation API",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://ii.nlm.nih.gov/Web_API/index.shtml",
+                    "mediaType": "text/html",
+                    "title": "API"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Research"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-geographic-comparisons/medicare-geographic-variation-by-national-state-county",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2022-01-01/2022-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-31",
+            "references": [
+                "https://data.cms.gov/sites/default/files/2024-05/a0e72c13-805a-4546-bb18-4e75e84a282f/Geographic%20Variation%20Public%20Use%20File%20Methods%20Paper.pdf"
+            ],
+            "keyword": [
+                "counties",
+                "health care use & payments",
+                "health equity",
+                "medicare",
+                "national",
+                "original medicare",
+                "states & territories"
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/6219697b-8f6c-4164-bed4-cd9317c58ebc/data-viewer",
+            "description": "The Medicare Geographic Variation by National, State & County dataset provides information on the geographic differences in the use and quality of health care services for the Original Medicare\u00a0population. This dataset contains demographic, spending, use, and quality indicators at the state level (including the District of Columbia, Puerto Rico, and the Virgin Islands) and the county level.\n\nSpending is standardized to remove geographic differences in payment rates for individual services as a source of variation. In general, total standardized per capita costs are less than actual per capita costs because the extra payments Medicare made to hospitals were removed, such as payments for medical education (both direct and indirect) and payments to hospitals that serve a disproportionate share of low-income patients. Standardization does not adjust for differences in beneficiaries\u2019 health status.",
+            "title": "Medicare Geographic Variation - by National, State & County",
+            "describedByType": "application/pdf",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6219697b-8f6c-4164-bed4-cd9317c58ebc/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Medicare Geographic Variation - by National, State & County : 2022-01-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/b1675c91-4643-47d0-b377-9b029edb9ff4/2014-2022%20Medicare%20FFS%20Geographic%20Variation%20Public%20Use%20File.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Geographic Variation - by National, State & County : 2022-01-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/567a0e69-320d-429c-a31f-c59b7099f22d/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Geographic Variation - by National, State & County : 2022-01-15"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-05/3f6841ec-571e-4e03-8766-5ef355c76857/2014-2022%20Medicare%20Geographic%20Variation%20by%20National%20State%20%20County%20Data%20Dictionary_508.pdf",
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
+            "landingPage": "https://www.ncbi.nlm.nih.gov/tools/cobalt/cobalt.cgi",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-06-30",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-04",
+            "keyword": [
+                "protein",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/nerf-hjnp",
+            "description": "Constraint-Based Multiple Alignment Tool (COBALT) is a protein multiple sequence alignment tool that finds a collection of pairwise constraints derived from conserved domain database, protein motif database, and sequence similarity, using RPS-BLAST, BLASTP, and PHI-BLAST.",
+            "title": "Constraint-Based Multiple Alignment Tool (COBALT)",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/tools/cobalt/cobalt.cgi",
+                    "mediaType": "text/html",
+                    "title": "COBALT Homepage and Search"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Molecular biology/Genetics"
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
+                "smokefree indoor air",
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
+            "identifier": "https://data.cdc.gov/api/views/32fd-hyzc",
+            "description": "1995-2024. Centers for Disease Control and Prevention (CDC).  State Tobacco Activities Tracking and Evaluation (STATE) System. Legislation \u2013 Smokefree Indoor Air. The STATE System houses current and historical state-level legislative data on tobacco use prevention and control policies. Data are reported on a quarterly basis. Data include information related to state legislation on smokefree indoor air in areas such as: Bars, Commercial Day Care Centers, Government Multi-Unit Housing, Government Worksites, Home-Based Day Care Centers, Hotels and Motels, Personal Vehicles, Private Multi-Unit Housing, Private Worksites, Restaurants, Bingo Halls, Casinos, Enclosed Arenas, Grocery Stores, Hospitals, Hospital Campuses, Malls, Mental Health Outpatient and Residential Facilities, Prisons, Public Transportation, Racetrack Casinos, Substance Abuse Outpatient and Residential Facilities.",
+            "title": "CDC STATE System Tobacco Legislation - Smokefree Indoor Air",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/32fd-hyzc/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
```

