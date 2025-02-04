# Change History for healthdata.json (Part 23)

### Changes from 761a84b to acf49f0 (Part 12/12)
**Author:** Automated

**Date:** 2025-01-31 15:36:25+00:00

**Message:** Updated data: Fri Jan 31 15:36:25 UTC 2025

```diff
+            "issued": "2024-09-26",
+            "@type": "dcat:Dataset",
+            "temporal": "2023-2024, 2024-2025",
+            "modified": "2025-01-29",
+            "keyword": [
+                "flu vaccination",
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
+            "identifier": "https://data.cdc.gov/api/views/4g6p-3ed6",
+            "description": "\u2022 Weekly Influenza Vaccination Coverage and Comparison among adults 18 Years and Older by Jurisdiction\n\n \u2022 Weekly estimates of influenza vaccination coverage and intent for vaccination among adults are calculated using data from the National Immunization Survey\u2013Adult COVID Module (NIS\u2013ACM) (https://www.cdc.gov/nis/about/).",
+            "title": "Weekly Differences in Cumulative Influenza Vaccination Coverage and Comparison Between 2024-25 and 2023-24 Among Adults 18 Years, Overall, by Selected Demographics",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4g6p-3ed6/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4g6p-3ed6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4g6p-3ed6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4g6p-3ed6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States- National, Region, State",
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
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-geographic-comparisons/medicare-advantage-geographic-variation-national-state",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2022-11-01",
+            "temporal": "2021-01-01/2021-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2024-05-30",
+            "references": [
+                "https://data.cms.gov/sites/default/files/2024-05/1633f75a-93d4-4600-80f4-ba033c9d8e38/Medicare%20Advantage%20Geographic%20Variation%20National%20%20State_Methods_RY24_508.pdf"
+            ],
+            "keyword": [
+                "hospitals & facilities",
+                "inpatient",
+                "medicare",
+                "medicare advantage",
+                "national",
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/8e989bc0-2260-49a7-9c6d-8e9e10af7cea/data-viewer",
+            "description": "The Medicare Advantage Geographic Variation National & State dataset provides information on demographic characteristics and service utilization for hospital inpatient, skilled nursing facility services, outpatient, DME, and professional services between 2016-2021 for Medicare Advantage beneficiaries at the national and state levels.",
+            "title": "Medicare Advantage Geographic Variation - National & State",
+            "describedByType": "application/pdf",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8e989bc0-2260-49a7-9c6d-8e9e10af7cea/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Medicare Advantage Geographic Variation - National & State : 2021-01-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/b85e7550-4914-4817-a947-e7dbd476e6c3/MA%20GV%20PUF_2016-2021_RY24.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Advantage Geographic Variation - National & State : 2021-01-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/ddde8085-d976-4694-914a-5d52a7818170/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Advantage Geographic Variation - National & State : 2021-01-15"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-06/7ae600cf-5662-4462-8d86-7aab3f58e7b8/Medicare%20Advantage%20Geographic%20Variation%20National%20%20State%20Data%20Dictionary_RY24.pdf",
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
+            "landingPage": "https://www.ncbi.nlm.nih.gov/protein",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-08-26",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "api",
+                "dataset",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/2xvy-u8hi",
+            "description": "The Protein database is a collection of sequences from several sources, including translations from annotated coding regions in GenBank, RefSeq and TPA, as well as records from SwissProt, PIR, PRF, and PDB. Protein sequences are the fundamental determinants of biological structure and function.",
+            "title": "Protein",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/protein",
+                    "mediaType": "text/html",
+                    "title": "Protein - Query Interface"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Molecular biology/Genetics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/vtdc-bx7p",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-07-27",
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
+            "identifier": "eec7fbe6-c4c4-5915-b3d0-be5828ef4e9d",
+            "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
+            "title": "State Drug Utilization Data 2021",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/SDUD2021.csv",
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
+            "landingPage": "https://data.cdc.gov/d/qvvb-s7gu",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-01-03",
+            "@type": "dcat:Dataset",
+            "modified": "2019-01-03",
+            "keyword": [
+                "2018",
+                "animal",
+                "congenital syndrome",
+                "nedss",
+                "netss",
+                "nndss",
+                "rabies",
+                "rubella",
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
+            "identifier": "https://data.cdc.gov/api/views/qvvb-s7gu",
+            "description": "NNDSS - Table II. Rabies, animal to Rubella, congenital syndrome - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\n\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum.\r\n \r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.",
+            "title": "NNDSS - Table II. Rabies, animal to Rubella, congenital syndrome",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qvvb-s7gu/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qvvb-s7gu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qvvb-s7gu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qvvb-s7gu/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/txmx-urgu",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2020-09-21",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/txmx-urgu",
+            "description": "TOXLINE was the National Library of Medicine (NLM) bibliographic database for toxicology, a varied science encompassing many disciplines. TOXLINE records provide bibliographic information covering the biochemical, pharmacological, physiological, and toxicological effects of drugs and other chemicals. TOXLINE references were drawn from various sources organized into component subfiles.\n\nThis version of TOXLINE is no longer updated. Updated TOXLINE content is available in PubMed or by searching PubMed using the search string: tox [sb] .",
+            "title": "Toxicology Information Online (TOXLINE) (RETIRED)",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/toxspeclease/",
+                    "description": "NOTE - This version of TOXLINE is no longer updated. Updated TOXLINE content is available in PubMed by searching using the search string: tox [su]. These data are provided for archival and research purposes only.",
+                    "@type": "dcat:Distribution",
+                    "title": "Download - TOXLINE Archival Data"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://ftp.nlm.nih.gov/projects/sample/toxspec/",
+                    "mediaType": "text/html",
+                    "title": "Sample Data "
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Drugs and Chemicals"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/dataset/study-womens-health-across-nation-swan-biospecimen-repository",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2015-03-04",
+            "temporal": "2000-09-01T00:00:00-04:00/2000-09-01T00:00:00-04:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "biobank",
+                "bone loss",
+                "cardiovascular disease",
+                "chronic diseases",
+                "cognitive function",
+                "depression",
+                "diabetes",
+                "menopause",
+                "midlife",
+                "osteoporosis",
+                "physcial function",
+                "sexual function",
+                "specimen",
+                "speciment",
+                "swan",
+                "urogenital symptoms",
+                "vasomotor symptoms",
+                "women s health"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Steffenie Merillat",
+                "hasEmail": "mailto:swan.repository@umich.edu"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Department of Health & Human Services"
+            },
+            "identifier": "f6f8f6a1-280b-48a2-a3bc-517cdfab8b76",
+            "description": "<p>The SWAN Repository is the biospecimen bank of the SWAN study. All stored specimens are from the 3,302 SWAN participants, collected across the 14 clinic visits (Baseline and 13 follow-up visits). Available biospecimen types include serum, plasma, urine and DNA which total nearly 1.8 million. Both Repository specimens and data generated through Repository studies and subsequently returned are available through the SWAN Repository. Through the Repository website, registered users can submit inquiries and applications for access to these resources.</p>",
+            "title": "Study of Womens Health Across the Nation (SWAN) Biospecimen Repository",
+            "programCode": [
+                "009:048"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.swanstudy.org/swan-research/data-access/",
+                    "mediaType": "text/html",
+                    "title": "HTML "
+                }
+            ],
+            "describedBy": "http://datawarehouse.swanrepository.com/userLogIn",
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/coverage/covidvaxview/interactive/adult-coverage-vaccination.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-12-11",
+            "@type": "dcat:Dataset",
+            "temporal": "2023-2024",
+            "modified": "2024-08-28",
+            "keyword": [
+                "adults",
+                "covid-19 vaccination",
+                "nis-acm"
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
+            "identifier": "https://data.cdc.gov/api/views/kevv-m5vs",
+            "description": "Weekly COVID-19 Vaccination Coverage of Adults 18 Years and Older by Jurisdiction \n\n\u2022 COVID-19 vaccination coverage among adults 18 years and older is assessed through the National Immunization Survey-Adult COVID Module, providing weekly COVID-19 vaccination coverage estimates. (https://www.cdc.gov/vaccines/imz-managers/nis/about.html) \n\n\u2022 Starting in September 2023, the CDC recommended the 2023-2024 updated COVID-19 vaccine for adults ages 18 years and older.",
+            "title": "Weekly Differences in Cumulative Percentage of Adults 18 Years and Older Vaccinated with the Updated 2023-24 COVID-19 Vaccine by Selected Demographics",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kevv-m5vs/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kevv-m5vs/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kevv-m5vs/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kevv-m5vs/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.healthit.gov/data/datasets/ehr-developers-reported-health-care-providers-participating-federal-programs",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-10-03",
+            "@type": "dcat:Dataset",
+            "modified": "2017-07-01",
+            "references": [
+                "https://www.healthit.gov/data/quickstats/health-care-professional-health-it-developers",
+                "https://www.healthit.gov/data/quickstats/hospital-health-it-developers"
+            ],
+            "keyword": [
+                "adoption",
+                "cehrt",
+                "certified electronic health record technology",
+                "cms ehr incentrive program",
+                "ehr developers",
+                "ehr vendors",
+                "federal programs",
+                "health it"
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
+            "identifier": "5d6zvokd-upg9-fobb-lzgn-ep6jo1du8lkd",
+            "description": "The Medicare &amp; Medicaid Electronic Health Record (EHR) Incentive Programs provide incentives to eligible ambulatory and inpatient providers to adopt electronic health records. This dataset provides the counts of health care providers that have reported a developer's product through participation in the Medicare EHR Incentive Program. The data are provided beginning in 2011. This dataset enables the tracking of trends in the adoption of healthIT by developer and by both office-based health care providers and non-federal acute-care hospitals. Filter the data by Program Year to get the most recent counts by health care provider type. The most recent data is available through the 2016 Program Year.",
+            "title": "EHR Developers Reported by Health Care Providers Participating in Federal Programs",
+            "programCode": [
+                "009:110"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.healthit.gov/sites/default/files/data/datasets/EHR-vendors-count-dataset.csv",
+                    "mediaType": "text/csv",
+                    "title": "EHR-vendors-count-dataset.csv"
+                }
+            ],
+            "describedBy": "https://www.healthit.gov/data/datasets/ehr-developers-reported-health-care-providers-participating-federal-programs"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/cuyd-c53m",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-15",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Chemical and Biological Monitoring Branch (CBMB), Health Effects Laboratory Division (HELD)",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/cuyd-c53m",
+            "description": "We investigated the suitability of graphitic carbon (GC) content of diesel particulate matter (DPM), measured using Raman spectroscopy, as a surrogate measure of elemental carbon (EC), determined by thermal optical analysis.  Raman spectra in the range of 800-1800 cm-1 (including the D mode at ~1322 cm-1 and the G mode at ~1595 cm-1) were used for GC identification and quantification. Raman spectra for two certified DPM standards (SRM 1650 and SRM 2975), two types of diesel engine exhaust soot, and three types of DPM-enriched workplace aerosols were obtained.",
+            "title": "Correlation between graphitic carbon and elemental carbon in diesel particulate matter in workplace atmospheres-Dataset",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/cuyd-c53m/application/x-zip-compressed",
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
+            "landingPage": "https://www.ncbi.nlm.nih.gov/Traces/trace.cgi",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-06-30",
+            "@type": "dcat:Dataset",
+            "modified": "2022-09-30",
+            "keyword": [
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ixrk-4tte",
+            "description": "A repository of DNA sequence chromatograms (traces), base calls, and quality estimates for single-pass reads from various large-scale sequencing projects.",
+            "title": "Trace Archive",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/Traces/trace.cgi",
+                    "mediaType": "text/html",
+                    "title": "Query Interface"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Molecular biology/Genetics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/rmzv-dc5f",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2016-09-26",
+            "@type": "dcat:Dataset",
+            "modified": "2016-09-26",
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
+            "identifier": "https://data.cdc.gov/api/views/rmzv-dc5f",
+            "description": "Source for 2012 national data: National Occupant Protection Use Survey (NOPUS), 2012. Source for 2012 state data: State Observational Survey of Seat Belt Use, 2012. Source for 2014 national data: National Highway Traffic Safety Administration's (NHTSA) National Occupant Protection Use Survey (NOPUS), 2014. Source for 2014 state data: National Highway Traffic Safety Administration's (NHTSA) State Observation of Seat Belt Use, 2014",
+            "title": "Percentage of Drivers and Front Seat Passengers Wearing Seat Belts, 2012 & 2014, All States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rmzv-dc5f/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rmzv-dc5f/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rmzv-dc5f/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rmzv-dc5f/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/3svv-v5nh",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-01-14",
+            "@type": "dcat:Dataset",
+            "modified": "2022-02-11",
+            "keyword": [
+                "2022",
+                "arboviral diseases",
+                "babesiosis",
+                "nedss",
+                "netss",
+                "nndss",
+                "western equine encephalitis virus disease",
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
+            "identifier": "https://data.cdc.gov/api/views/3svv-v5nh",
+            "description": "NNDSS - Table 1D. Arboviral diseases, Western equine encephalitis virus disease to Babesiosis - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\nFootnotes:\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
+            "title": "NNDSS - Table 1D. Arboviral diseases, Western equine encephalitis virus disease to Babesiosis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3svv-v5nh/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3svv-v5nh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3svv-v5nh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3svv-v5nh/rows.xml?accessType=DOWNLOAD",
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
+            "issued": "2024-07-05",
+            "temporal": "2001/2021",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-24",
+            "keyword": [
+                "dentists",
+                "health us",
+                "state"
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
+            "identifier": "https://data.cdc.gov/api/views/9epi-jrff",
+            "description": "Data on active dentists in the United States by state. Data are from Health, United States. SOURCE: American Dental Association, Health Policy Institute.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
+            "title": "DQS Dentists, by state: United States.",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9epi-jrff/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9epi-jrff/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9epi-jrff/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9epi-jrff/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Annual  (R/P1Y)",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/45um-c62r",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2014-04-02",
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
+            "identifier": "https://data.cdc.gov/api/views/45um-c62r",
+            "description": "In general, total combined rates for traumatic brain injury (TBI)-related emergency department (ED) visits, hospitalizations and deaths have increased over the past decade.  Total combined rates of TBI-related hospitalizations, ED visits, and deaths climbed slowly from a rate of 521.0 per 100,000 in 2001 to 615.7 per 100,000 in 2005.  The rates then dipped to 595.1 per 100,000 in 2006 and 566.7 per 100,000 in 2007.  The rates then spiked sharply in 2008 and continued to climb through 2010 to a rate of 823.7 per 100,000.  Total combined rates of TBI-related hospitalizations, ED visits, and deaths are driven in large part by the relatively high number of TBI-related ED visits.  In comparison to ED visits, the overall rates of TBI-related hospitalizations remained relatively stable changing from 82.7 per 100,000 in 2001 to 91.7 per 100,000 in 2010.  TBI-related deaths also decreased slightly over time from 18.5 per 100,000 in 2001 to 17.1 per 100,000 in 2010.  Note that the axis scale for TBI-related deaths appears to the right of the chart and differs from TBI-related hospitalizations and ED visits.Go to http://www.cdc.gov/traumaticbraininjury/data/index.html to view more TBI data & statistics.",
+            "title": "Rates of TBI-related Emergency Department Visits, Hospitalizations, and Deaths - United States, 2001 \u2013 2010",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/45um-c62r/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/45um-c62r/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/45um-c62r/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/45um-c62r/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.ncbi.nlm.nih.gov/omim",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2022-03-01",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/hra4-qimf",
+            "description": "Comprehensive, authoritative, and timely compendium of human genes and genetic phenotypes.",
+            "title": "OMIM (Online Mendelian Inheritance in Man)",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/omim",
+                    "mediaType": "text/html",
+                    "title": "OMIM (Online Mendelian Inheritance in Man)"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Molecular biology/Genetics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/visionhealth/vehss/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-06-15",
+            "@type": "dcat:Dataset",
+            "modified": "2023-09-21",
+            "references": [
+                "https://www.resdac.org",
+                "https://www.cdc.gov/visionhealth/vehss/data/claims/medicare.html"
+            ],
+            "keyword": [
+                "claims",
+                "eye exams",
+                "medical diagnoses",
+                "medicare",
+                "service utilization",
+                "treated prevalence"
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
+            "identifier": "https://data.cdc.gov/api/views/e28h-tx85",
+            "description": "2014-2019. This dataset is a de-identified summary table of vision and eye health data indicators from Medicare claims, stratified by all available combinations of age group, race/ethnicity, gender, and state. Medicare claims for VEHSS includes beneficiaries who were fully enrolled in Medicare Part B Fee-for-Service (FFS) for the duration of the year. Medicare claims provide a convenience sample that includes approximately 30 million individuals annually, which represents nearly 89% of the US population aged 65 and older and 3.3% of the US population younger than 65, including persons disabled due to blindness. Medicare data for VEHSS include Service Utilization and Medical Diagnoses indicators. Data were suppressed for de-identification to ensure protection of patient privacy. Data will be updated as it becomes available. Detailed information on VEHSS Medicare analyses can be found on the VEHSS Medicare webpage (cdc.gov/visionhealth/vehss/data/claims/medicare.html). Information on available Medicare claims data can be found on the ResDac website (www.resdac.org). The VEHSS Medicare dataset was last updated May 2023.",
+            "title": "Medicare Claims \u2013 Vision and Eye Health Surveillance",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/e28h-tx85/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/e28h-tx85/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/e28h-tx85/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/e28h-tx85/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/d/e28h-tx85",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "theme": [
+                "Vision & Eye Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-04-28",
+            "@type": "dcat:Dataset",
+            "temporal": "1988/2019",
+            "modified": "2023-08-29",
+            "keyword": [
+                "adolescent",
+                "adult",
+                "african americans",
+                "age",
+                "asian continental ancestry group",
+                "child",
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
+            "identifier": "https://data.cdc.gov/api/views/9gay-j69q",
+            "description": "Data on obesity among children and adolescents aged 2-19 years by selected population characteristics. Please refer to the PDF or Excel version of this table in the HUS 2019 Data Finder (https://www.cdc.gov/nchs/hus/contents2019.htm) for critical information about measures, definitions, and changes over time. \n\nSOURCE: NCHS, National Health and Nutrition Examination Survey. For more information on the National Health and Nutrition Examination Survey, see the corresponding Appendix entry at https://www.cdc.gov/nchs/data/hus/hus19-appendix-508.pdf.",
+            "title": "Obesity among children and adolescents aged 2\u201319 years, by selected characteristics: United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9gay-j69q/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9gay-j69q/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9gay-j69q/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9gay-j69q/rows.xml?accessType=DOWNLOAD",
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
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/986w-8kut",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-01-21",
+            "@type": "dcat:Dataset",
+            "modified": "2022-01-12",
+            "keyword": [
+                "2021",
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
+            "identifier": "https://data.cdc.gov/api/views/986w-8kut",
+            "description": "NNDSS - Table 1I. Cryptosporidiosis to Cyclosporiasis - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - Table 1I. Cryptosporidiosis to Cyclosporiasis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/986w-8kut/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/986w-8kut/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/986w-8kut/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/986w-8kut/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "http://www.tcdb.org/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2016-07-17",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "RAVICHANDRAN, VEERASAMY\u00a0",
+                "hasEmail": "mailto:veerasamy.ravichandra@nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
+            "identifier": "25c28438-56d2-49ac-8acc-c19c9dbbc6c7",
+            "description": "<p>The Transporter Classification Database details a comprehensive classification system for membrane transport proteins known as the Transporter Classification (TC) system. The TC system is analogous to the Enzyme Commission (EC) system for classification of enzymes, except that it incorporates both functional and phylogenetic information. Descriptions, TC numbers, and examples of over 600 families of transport proteins are provided.</p>",
+            "title": "Transporter Classification Database (TCDB)",
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
+            "landingPage": "https://data.cdc.gov/d/phkb-u384",
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
+            "identifier": "https://data.cdc.gov/api/views/phkb-u384",
+            "description": "Gulf War Illness (GWI) is a persistent chronic neuroinflammatory illness exacerbated by external stressors and characterized by fatigue, musculoskeletal pain, cognitive and neurological problems linked to underlying immunological dysfunction for which there is no known treatment.  Here, we constructed a logic model of immune regulatory behavior between human clinical samples and mouse models of GWI subtyped by exposure to traumatic stress.  We identify several ideal multi-intervention strategies and potential drug candidates that may be used to treat chronic neuroinflammation in GWI.",
+            "title": "Modeling Neuroimmune Interactions in Human Subjects and Animal Models to Predict Subtype Specific Multidrug Treatments for Gulf War Illness",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/phkb-u384/application/x-zip-compressed",
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
+            "landingPage": "https://www.ncbi.nlm.nih.gov/genbank/wgs/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-08-26",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/8hqv-4ds7",
+            "description": "Whole Genome Shotgun (WGS) projects are genome assemblies of incomplete genomes or incomplete chromosomes of prokaryotes or eukaryotes that are generally being sequenced by a whole genome shotgun strategy. WGS projects may be annotated, but annotation is not required. NCBI has a Prokaryotic Genomes Annotation Pipeline that may be requested at the time the genome files are submitted to GenBank. This pipeline generates a submission-ready annotated file that is posted back to the submitter for review and which the submitter could edit prior to data release.\n\nThe public WGS projects are at the list of WGS projects. https://www.ncbi.nlm.nih.gov/Traces/wgs/",
+            "title": "Whole Genome Shotgun Submissions",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/genbank/genomesubmit/",
+                    "description": "Both WGS and non-WGS genomes, including gapless complete bacterial chromosomes, can be submitted via the Submission Portal. You will be asked to choose whether the genome being submitted is considered WGS or not",
+                    "@type": "dcat:Distribution",
+                    "title": "Prokaryotic and Eukaryotic Genomes Submission Guide"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://ftp.ncbi.nih.gov/genbank/wgs/",
+                    "mediaType": "text/html",
+                    "title": "Download Whole Genome Shotgun Sequences Data"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Molecular biology/Genetics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/w2ns-vn28",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-10-08",
+            "@type": "dcat:Dataset",
+            "modified": "2022-05-09",
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
+            "identifier": "a1a4d739-514c-5952-a6e0-8bc9a2bb2709",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "devAuto_measure_allStates_download",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20220509_ETL_DEV/measure_allStates_download.csv",
+                    "description": "{\"dataset\": \"measure_allStates_download\", \"stage\": \"devAuto\", \"update_id\": \"20220509_ETL_DEV\"}",
+                    "@type": "dcat:Distribution",
+                    "title": "measure_allStates_download csv file"
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
+            "landingPage": "https://data.cdc.gov/d/gjsp-ircr",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-09-27",
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
+            "identifier": "https://data.cdc.gov/api/views/gjsp-ircr",
+            "description": "Footnotes for Health, US - Asthma in children younger than age 18, by selected characteristics: United States. \n\nData on asthma in children younger than age 18 in the United States, by selected characteristics. Data are from Health, United States. Source: National Center for Health Statistics, National Health Interview Survey.",
+            "title": "HUS_Footnote_Look_Up_ASTHCH",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gjsp-ircr/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gjsp-ircr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gjsp-ircr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gjsp-ircr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "theme": [
+                "National Center for Health Statistics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/tdge-ieq8",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-01-21",
+            "@type": "dcat:Dataset",
+            "modified": "2022-01-12",
+            "keyword": [
+                "2021",
+                "acute",
+                "chronic",
+                "nedss",
+                "netss",
+                "nndss",
+                "q fever",
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
+            "identifier": "https://data.cdc.gov/api/views/tdge-ieq8",
+            "description": "NNDSS - TABLE 1BB. Q fever, Total to Q fever, Chronic - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S, a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1BB. Q fever, Total to Q fever, Chronic",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tdge-ieq8/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tdge-ieq8/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tdge-ieq8/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/tdge-ieq8/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/w2xy-hgqk",
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
+            "identifier": "1afe96ca-dd06-5002-b4c4-5f4f45e5a171",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
+            "title": "prodAuto_measure_concernLevel",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_concernLevel.csv",
+                    "description": "{\"dataset\": \"measure_concernLevel\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
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
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2011-0",
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
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2011-nid13563",
+            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment history and perceived need for treatment, and included questions from the Diagnostic and Statistical Manual (DSM) of Mental Disorders that allow diagnostic criteria to be applied. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing. Questions introduced in previous administrations were retained in the 2011 survey, including questions asked only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes toward drug use and activities such as school work. Several measures focused on prevention-related themes in this section. Also retained were questions on mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking. Questions on the tobacco brand used most often were introduced with the 1999 survey. For the 2008 survey, adult mental health questions were added to measure symptoms of psychological distress in the worst period of distress that a person experienced in the past 30 days and suicidal ideation. In 2008, a split-sample design also was included to administer separate sets of questions (WHODAS vs. SDS) to assess impairment due to mental health problems. Beginning with the 2009 NSDUH, however, all of the adults in the sample received only the WHODAS questions. Background information includes gender, race, age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.This study has 1 Data Set.</p>",
+            "title": "National Survey on Drug Use and Health (NSDUH-2011)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2011-nid13563",
+                    "description": "National Survey on Drug Use and Health (NSDUH-2011) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2011-nid13563"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/w36q-qgu2",
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
+            "identifier": "4bc725b5-e88e-525c-880b-8547f0edd081",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "devAuto_measure_allStates_downloadLink",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/measure_allStates_downloadLink.csv",
+                    "description": "{\"dataset\": \"measure_allStates_downloadLink\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
+                    "@type": "dcat:Distribution",
+                    "title": "measure_allStates_downloadLink csv file"
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
+            "landingPage": "https://www.cdc.gov/statesystem/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-07-14",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-25",
+            "references": [
+                "https://chronicdata.cdc.gov/d/p8tr-pquj"
+            ],
+            "keyword": [
+                "cdc",
+                "office on smoking and health",
+                "osh",
+                "tobacco",
+                "youth tobacco sales"
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
+            "identifier": "https://data.cdc.gov/api/views/escb-scz6",
+            "description": "1997-2018. Substance Abuse and Mental Health Services Administration (SAMHSA). Synar Reports: Youth Tobacco Sales. Policy \u2013 Youth Tobacco Sales. SAMHSA\u2019s Synar Report on Youth Tobacco Sales presents findings on compliance of the Synar Amendment aimed at decreasing youth access to tobacco, and reviews progress in enforcing State youth tobacco access laws and in reducing the percentage of retailers selling tobacco products to minors.",
+            "title": "SAMHSA Synar Reports: Youth Tobacco Sales",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/escb-scz6/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/escb-scz6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/escb-scz6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/escb-scz6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Policy/SAMHSA-Synar-Reports-Youth-Tobacco-Sales/escb-scz6",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "theme": [
+                "Policy"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/nkri-ptxd",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2013-08-14",
+            "@type": "dcat:Dataset",
+            "modified": "2015-08-27",
+            "keyword": [
+                "children",
+                "hus",
+                "vaccination"
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
+            "identifier": "https://data.cdc.gov/api/views/nkri-ptxd",
+            "description": "Health, United States is an annual report on trends in health statistics, find more information at http://www.cdc.gov/nchs/hus.htm.",
+            "title": "Selected Trend Table from Health, United States, 2011. Vaccination coverage among children 19 - 35 months of age for selected diseases, by race, Hispanic origin, poverty level, and location of residence in metropolitan statistical area: United States, sel",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/nkri-ptxd/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/nkri-ptxd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/nkri-ptxd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/nkri-ptxd/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/rdfw-s4u4",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-15",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Health Effects Laboratory Division (HELD)",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/rdfw-s4u4",
+            "description": "Concentrated collection of aerosol particles on a substrate is essential for their chemical analysis using various microscopy and laser spectroscopic techniques. An impaction-based aerosol concentration system was developed for focused collection of particles using a multi-stage nozzle that consists of a succession of multiple smooth converging stages. Converging sections of the nozzle were designed to focus and concentrate a particle diameter range of 900 to 2500 nm into a relatively narrower particle beam to obtain particulate deposits with spot diameters of 0.5-1.56 mm. A slightly diverging section before the last contractions was included to allow for better focusing of particles at the lower end of the collectable diameter range. The characterization of this multi-stage nozzle and the impaction-based aerosol concentration system encompassing the nozzle was accomplished both numerically and experimentally. The numerical and experimental trends in collection efficiency and spot diameters agreed well qualitatively; however, the quantitative agreement between numerical and experimental results for wall losses was poor, particularly for larger particle diameters. The resulting concentrated particulate deposit, a spot sample, was analysed using Raman spectroscopy to probe effect of spot size on analytical sensitivity of measurement. The method\u2019s sensitivity was compared against other conventional techniques, such as filtration and aerosol focused impaction, implementing condensational growth.  Impaction encompassing the multi-stage focusing nozzle is the only method that can ensure high sensitivity at Reynolds numbers greater than 2000, that can be supported by small pumps which renders such method suitable for portable instrumentation.",
+            "title": "Characterization of a multi-stage focusing nozzle for collection of spot samples for aerosol chemical analysis",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/rdfw-s4u4/application/x-zip-compressed",
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
+            "issued": "2024-10-15",
+            "temporal": "2010/2022",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-05",
+            "keyword": [
+                "american indian and alaska native only",
+                "asian only",
+                "black non-hispanic",
+                "black only",
+                "domains of functioning",
+                "female",
+                "functional limitation",
+                "health us",
+                "hispanic",
+                "male",
+                "metropolitan statistical area",
+                "national health interview survey",
+                "native hawaiian or pacific islander only",
+                "nhis",
+                "poverty level",
+                "rural",
+                "sdoh-poverty-income",
+                "sdoh-social-emotional",
+                "urban",
+                "white non-hispanic",
+                "white only"
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
+            "identifier": "https://data.cdc.gov/api/views/bjpq-vm2t",
+            "description": "Data on functional limitation (or functional difficulties) in adults age 18 and older in the United States, by selected characteristics. Data are from Health, United States. Source: National Center for Health Statistics, National Health Interview Survey. \nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
+            "title": "DQS Functional difficulties in adults age 18 and older, by selected characteristics: United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bjpq-vm2t/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bjpq-vm2t/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bjpq-vm2t/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bjpq-vm2t/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/mvsw-zuaf",
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
+                "severe acute respiratory syndrome-associated coronavirus disease",
+                "shiga toxin-producing escherichia coli",
+                "shigellosis",
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
+            "identifier": "https://data.cdc.gov/api/views/mvsw-zuaf",
+            "description": "NNDSS - TABLE 1FF. Severe acute respiratory syndrome-associated coronavirus disease to Shigellosis - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1FF. Severe acute respiratory syndrome-associated coronavirus disease to Shigellosis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mvsw-zuaf/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mvsw-zuaf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mvsw-zuaf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/mvsw-zuaf/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.atsdr.cdc.gov/placeandhealth/svi/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2020-03-11",
+            "@type": "dcat:Dataset",
+            "temporal": "2018",
+            "modified": "2022-02-14",
+            "keyword": [
+                "2018",
+                "social vulnerability",
+                "social vulnerability index",
+                "tract",
+                "united states",
+                "vulnerable populations"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "SVI Coordinator",
+                "hasEmail": "mailto:svi_coordinator@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/4d8n-kk8a",
+            "description": "ATSDR\u2019s Geospatial Research, Analysis & Services Program (GRASP) created Centers for Disease Control and Prevention Social Vulnerability Index (CDC SVI or simply SVI, hereafter) to help public health officials and emergency response planners identify and map the communities that will most likely need support before, during, and after a hazardous event.\n\nSVI indicates the relative vulnerability of every U.S. Census tract. Census tracts are subdivisions of counties for which the Census collects statistical data. SVI ranks the tracts on 15 social factors, including unemployment, minority status, and disability, and further groups them into four related themes. Thus, each tract receives a\nranking for each Census variable and for each of the four themes, as well as an overall ranking.\n\nIn addition to tract-level rankings, SVI 2018 also has corresponding rankings at the\ncounty level. Notes below that describe \u201ctract\u201d methods also refer to county methods.",
+            "title": "Social Vulnerability Index 2018 - United States, tract",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4d8n-kk8a/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4d8n-kk8a/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4d8n-kk8a/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/4d8n-kk8a/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "USA",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "biennial",
+            "theme": [
+                "Health Statistics"
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
+                "community health",
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
+            "identifier": "97f8facf-a2b8-47f0-847b-d7e7bc165c09",
+            "description": "Contains data for FDA Hydrolyzed Vegetable Protein (HVP) Containing Products recalls since February, 2010.",
+            "title": "FDA Hydrolyzed Vegetable Protein (HVP) Containing Products Recalls",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/HVPCP/HydrolyzedVegetableProteinProductsList2010.xls",
+                    "mediaType": "application/vnd.ms-excel"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "restricted public",
+            "landingPage": "https://www.cdc.gov/nchs/nsrcf/index.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information. Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement. If approved, data access would occur at a NCHS or Federal Statistical Research Data Center. For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
+            "issued": "2023-07-03",
+            "@type": "dcat:Dataset",
+            "temporal": "2010-03/2010-10",
+            "modified": "2023-07-03",
+            "references": [
+                "https://www.cdc.gov/nchs/data/nsrcf/2010NSRCF_SurveyMethodologyandDocumentation.pdf"
+            ],
+            "keyword": [
+                "assisted living facilities",
+                "long-term care",
+                "research-data-center",
+                "residential care facilities",
+                "residential care facility residents",
+                "residential care facility staff",
+                "sdoh-access-to-health-care",
+                "sdoh-use-of-health-care"
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
+            "identifier": "https://data.cdc.gov/api/views/5586-cehn",
+            "description": "The 2010 National Survey of Residential Care Facilities (NSRCF) is a first-ever national probability sample survey that collects data on U.S. residential care providers, their staffs and services, and the people they serve. It is designed to provide national estimates of the number of residential care facilities operating in the United States, the number of residents receiving care, and the characteristics of both the facilities and their residents. NSRCF was conducted between March and November 2010. All residential care facilities that participated in the survey were places that were licensed, registered, listed, certified, or otherwise regulated by the state and that had 4 or more licensed, certified, or registered beds, provided room and board with at least two meals a day, around-the-clock on-site supervision, and help with personal care such as bathing and dressing or health related services such as medication management. These facilities served a predominantly adult population and had at least one current resident. Facilities licensed to serve the mentally ill or the developmentally disabled populations exclusively were excluded from the survey.",
+            "title": "National Survey of Residential Care Facilities - Restricted Resident-Level Dataset",
+            "isPartOf": "https://www.cdc.gov/nchs/nsrcf/nsrcf_questionnaires.htm",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "description": "The 2010 NSRCF data were collected through in-person interviews with facility directors and their \ndesignated staffs; no interviews were conducted directly with residents. Facility data included\nquestions on facility characteristics such as ownership, size, types of living arrangements and \namenities, policies, staffing, services, and general resident characteristics. Data collected on \nresidents included questions on the sampled residents\u2019 demographics, living arrangements, \nactivities, health conditions, cognitive and physical functioning, and services received. The total \nnumber of facilities that participated in the 2010 NSRCF is 2,302, and data are available on 8,094\nresidents from these facilities.",
+                    "@type": "dcat:Distribution",
+                    "title": "National Survey of Residential Care Facilities - Restricted Resident-Level Dataset"
+                }
+            ],
+            "spatial": "United States",
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
+            "landingPage": "https://data.cdc.gov/d/smic-9bf9",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2020-01-21",
+            "@type": "dcat:Dataset",
+            "modified": "2021-01-07",
+            "keyword": [
+                "2020",
+                "congenital syndrome",
+                "nedss",
+                "netss",
+                "nndss",
+                "rubella",
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
+            "identifier": "https://data.cdc.gov/api/views/smic-9bf9",
+            "description": "NNDSS - TABLE 1DD. Rubella to Rubella, congenital syndrome - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1DD. Rubella to Rubella, congenital syndrome",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/smic-9bf9/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/smic-9bf9/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/smic-9bf9/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/smic-9bf9/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/fztq-uwup",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-01-14",
+            "@type": "dcat:Dataset",
+            "modified": "2022-02-11",
+            "keyword": [
+                "2022",
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
+            "identifier": "https://data.cdc.gov/api/views/fztq-uwup",
+            "description": "NNDSS - Table 1H. Cholera to Coccidioidomycosis - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
+            "title": "NNDSS - Table 1H. Cholera to Coccidioidomycosis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fztq-uwup/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fztq-uwup/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fztq-uwup/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fztq-uwup/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/gepg-djaz",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2020-01-21",
+            "@type": "dcat:Dataset",
+            "modified": "2021-01-07",
+            "keyword": [
+                "2020",
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
+            "identifier": "https://data.cdc.gov/api/views/gepg-djaz",
+            "description": "NNDSS - TABLE 1K. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1K. Ehrlichiosis and Anaplasmosis, Anaplasma phagocytophilum infection to Ehrlichia chaffeensis infection",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gepg-djaz/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gepg-djaz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gepg-djaz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gepg-djaz/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/j6gu-p9yd",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2020-01-21",
+            "@type": "dcat:Dataset",
+            "modified": "2021-01-07",
+            "keyword": [
+                "2020",
+                "acute",
+                "chronic",
+                "nedss",
+                "netss",
+                "nndss",
+                "q fever",
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
+            "identifier": "https://data.cdc.gov/api/views/j6gu-p9yd",
+            "description": "NNDSS - TABLE 1BB. Q fever, Total to Q fever, Chronic - 2020. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1BB. Q fever, Total to Q fever, Chronic",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/j6gu-p9yd/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/j6gu-p9yd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/j6gu-p9yd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/j6gu-p9yd/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/w63d-rrbu",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2022-03-02",
+            "@type": "dcat:Dataset",
+            "modified": "2022-04-27",
+            "keyword": [
+                "applications",
+                "child enrollment",
+                "chip",
+                "eligibility determinations",
+                "enrollment",
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
+            "identifier": "eba2c172-07ba-4a6a-877e-5373ca442243",
+            "description": "All states (including the District of Columbia) are required to provide data to The Centers for Medicare &amp; Medicaid Services (CMS) on a range of indicators related to key application, eligibility, and enrollment processes within the state Medicaid and Children\u2019s Health Insurance Programs (CHIP). These data reflect enrollment activity for all populations receiving comprehensive Medicaid and CHIP benefits in all states, as well as state program performance.",
+            "title": "CHIP Applications, Eligibility Determinations, and Enrollment Data",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/StateMedicaidandCHIPApplicationsEligibilityDeterminationsandEnrollmentData04282022.csv",
+                    "description": "All states (including the District of Columbia) are required to provide data to The Centers for Medicare &amp; Medicaid Services (CMS) on a range of indicators related to key application, eligibility, and enrollment processes within the state Medicaid and Children\u2019s Health Insurance Programs (CHIP). These data reflect enrollment activity for all populations receiving comprehensive Medicaid and CHIP benefits in all states, as well as state program performance.",
+                    "@type": "dcat:Distribution",
+                    "title": "State Medicaid and CHIP Applications, Eligibility Determinations, and Enrollment Data-09012021"
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
+            "landingPage": "https://healthdata.gov/dataset/cdc-behavioral-risk-factor-surveillance-system-brfss",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2012-05-30",
+            "temporal": "1984-01-01T00:00:00-05:00/2009-12-31T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "chronic disease",
+                "health",
+                "health care access",
+                "health-related behaviors",
+                "infectious disease",
+                "injury",
+                "population statistics",
+                "prevalence",
+                "preventive practices",
+                "survey",
+                "trends"
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
+            "identifier": "15ece528-43c1-45c3-ba01-0b9a4f5a31f0",
+            "description": "<p>The Behavioral Risk Factor Surveillance System (BRFSS) is a state-based system of health surveys that collects information on health risk behaviors, preventive health practices, and health care access primarily related to chronic disease and injury. For many states, the BRFSS is the only available source of timely, accurate data on health-related behaviors.</p>",
+            "title": "CDC Behavioral Risk Factor Surveillance System (BRFSS)",
+            "programCode": [
+                "009:072"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.cdc.gov/brfss/",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
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
+            "landingPage": "https://data.cdc.gov/d/9y49-tura",
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
+            "identifier": "https://data.cdc.gov/api/views/9y49-tura",
+            "description": "ABCs is an ongoing surveillance program that began in 1997. <a href=\"https://www.cdc.gov/abcs/reports-findings/surv-reports.html\">ABCs reports</a> describe the ABCs case definition and the specific methodology used to calculate rates and estimated numbers in the United States for each bacterium by year.  The methods, <a href=\"https://www.cdc.gov/abcs/methodology/surv-pop.html\">surveillance areas</a>, and <a href=\"https://www.cdc.gov/abcs/methodology/surv-pop.html\" >laboratory isolate collection areas</a> have changed over time.\n                Additionally, the way missing data are taken into account changed in 2010.  It went from distributing unknown values based on known values of cases by site to use of multiple imputation using a sequential regression imputation method.\n                Given these changes over time, trends should be interpreted with caution.\n<ul><li><a href=\"http://www.cdc.gov/abcs/methodology/index.html\">Methodology</a>\nFind details about surveillance population, case determination, surveillance evaluation, and more. </li> <li> <a href=\"http://www.cdc.gov/abcs/reports-findings/index.html\">Reports and Findings</a>\nGet official interpretations from reports and publications created from ABCs data.\n</li>                </ul>",
+            "title": "Active Bacterial Core surveillance (ABCs) Group A Streptococcus",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9y49-tura/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9y49-tura/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9y49-tura/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9y49-tura/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/w6wc-sdh5",
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
+            "identifier": "05abc6c7-8d36-521a-82a8-3182ea85a1ea",
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
+            "landingPage": "https://healthdata.gov/d/w73y-7zz6",
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
+            "identifier": "1632da10-d16e-57f6-8e2d-29bdd77949de",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "Scorecard measure v2.11.16 (cmsdev)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.16/20241107/measure.csv",
+                    "description": "Scorecard measure v2.11.16 (cmsdev)",
+                    "@type": "dcat:Distribution",
+                    "title": "Scorecard measure v2.11.16 (cmsdev)"
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
+            "landingPage": "https://data.cdc.gov/d/64br-p84f",
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
+            "identifier": "https://data.cdc.gov/api/views/64br-p84f",
+            "description": "Triclosan is an antimicrobial chemical used in healthcare settings that can be absorbed through the skin. Exposure to triclosan has been positively associated with food and aeroallergy and asthma exacerbation in humans and, although not directly sensitizing, has been demonstrated to augment the allergic response in a mouse model of asthma. The skin barrier and microbiome are thought to play important roles in mediating inflammation and allergy and disruptions may contribute to development of allergic disease. To investigate potential connections of the skin barrier and microbiome with immune responses to triclosan, SKH1 mice were dermally exposed to triclosan (0.5-2%) or vehicle for up to 7 consecutive days.",
+            "title": "Dermal exposure to the immunomodulatory antimicrobial chemical triclosan alters the skin barrier integrity and microbiome in mice",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/64br-p84f/application/x-zip-compressed",
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
+            "landingPage": "https://www.cdc.gov/vaccines/vaxview/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-02-13",
+            "@type": "dcat:Dataset",
+            "temporal": "2023-2024",
+            "modified": "2024-08-05",
+            "keyword": [
+                "iis",
+                "immunization information system",
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
+            "identifier": "https://data.cdc.gov/api/views/ku7p-zn4c",
+            "description": "Monthly Cumulative Number and Percent of Children <20 Months Who Received Nirsevimab by Age Group and Jurisdiction\n\n\u2022 Estimated nirsevimab coverage for children 0-19 months is assessed through U.S. jurisdictions\u2019 Immunization Information Systems (IIS) data, submitted from jurisdictions to CDC monthly in aggregate by age group. \n\n\u2022 Starting in July 2023, the CDC recommended the RSV vaccine to protect against serious illness from RSV. (https://www.cdc.gov/respiratory-viruses/whats-new/rsv-update-2023-09-22.html)\n\u2003",
+            "title": "Monthly Cumulative Number and Percent of Children <20 Months Who Received Nirsevimab by Age Group and Jurisdiction, United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ku7p-zn4c/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ku7p-zn4c/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ku7p-zn4c/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ku7p-zn4c/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.ncbi.nlm.nih.gov/books/NBK143764/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2022-03-01",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "computational biology",
+                "education",
+                "reference",
+                "training and instruction"
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/64f9-ag6i",
+            "description": "An extensive collection of articles about NCBI databases, data models, and software.",
+            "title": "NCBI Handbook",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/books/NBK143764/",
+                    "mediaType": "text/html",
+                    "title": "NCBI Handbook"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Other"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/v2mh-3yzr",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2020-01-17",
+            "@type": "dcat:Dataset",
+            "modified": "2021-01-07",
+            "keyword": [
+                "2020",
+                "anthrax",
+                "arboviral diseases",
+                "chikungunya virus disease",
+                "eastern equine encephalitis virus disease",
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
+            "identifier": "https://data.cdc.gov/api/views/v2mh-3yzr",
+            "description": "NNDSS - TABLE 1A. Anthrax to Arboviral diseases, Eastern equine encephalitis virus disease \u2013 2020.  In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non U.S. residents.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\n* Case counts for reporting years 2019 and 2020 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1A. Anthrax to Arboviral diseases, Eastern equine encephalitis virus disease",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/v2mh-3yzr/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/v2mh-3yzr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/v2mh-3yzr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/v2mh-3yzr/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.ncbi.nlm.nih.gov/tools/vecscreen/univec/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2022-03-02",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "computational biology",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/gw7j-gxtx",
+            "description": "UniVec and UniVec_Core databases in FASTA format.",
+            "title": "UniVec",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://ftp.ncbi.nlm.nih.gov/pub/UniVec/",
+                    "mediaType": "text/html",
+                    "title": "Download UniVec Data"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/tools/vecscreen/univec/",
+                    "mediaType": "text/html",
+                    "title": "About UniVec Data"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Molecular biology/Genetics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/w8hn-p5hf",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2017-07-20",
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
+            "identifier": "776a3880-a62d-5990-8b40-4406e6861dbb",
+            "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
+            "title": "State Drug Utilization Data 2017",
+            "programCode": [
+                "009:076"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/StateDrugUtilizationData2017.csv",
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
+            "landingPage": "https://data.cdc.gov/d/gp24-kfxi",
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
+            "identifier": "https://data.cdc.gov/api/views/gp24-kfxi",
+            "description": "NNDSS - TABLE 1PP. Yellow fever to Zika virus disease, non-congenital - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1PP. Yellow fever to Zika virus disease, non-congenital",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gp24-kfxi/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gp24-kfxi/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gp24-kfxi/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gp24-kfxi/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-09-29",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-25",
+            "references": [
+                "https://www.cdc.gov/places/measure-definitions/index.html"
+            ],
+            "keyword": [
+                "behaviors",
+                "city",
+                "gis",
+                "outcomes",
+                "place",
+                "places",
+                "prevalence",
+                "prevention",
+                "unhealthy"
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
+            "identifier": "https://data.cdc.gov/api/views/ndzg-9nmv",
+            "description": "This dataset contains model-based place (incorporated and census designated places) level estimates for the PLACES project 2020 release in GIS-friendly format. The PLACES project is the expansion of the original 500 Cities project and covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code tabulation Areas (ZCTA) levels. It represents a first-of-its kind effort to release information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2018 or 2017 data, Census Bureau 2010 population estimates, and American Community Survey (ACS) 2014-2018 or 2013-2017 estimates. The 2020 release uses 2018 BRFSS data for 23 measures and 2017 BRFSS data for 4 measures (high blood pressure, taking high blood pressure medication, high cholesterol, and cholesterol screening). Four measures are based on the 2017 BRFSS data because the relevant questions are only asked every other year in the BRFSS. These data can be joined with the 2019 Census TIGER/Line place boundary file in a GIS system to produce maps for 27 measures at the place level. An ArcGIS Online feature service is also available at https://www.arcgis.com/home/item.html?id=8eca985039464f4d83467b8f6aeb1320 for users to make maps online or to add data to desktop GIS software.",
+            "title": "PLACES: Place Data (GIS Friendly Format), 2020 release",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ndzg-9nmv/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ndzg-9nmv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ndzg-9nmv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ndzg-9nmv/rows.xml?accessType=DOWNLOAD",
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
+            "bureauCode": [
+                "009:20"
+            ],
+            "landingPage": "https://data.cdc.gov/d/bst4-hnte",
+            "issued": "2023-11-20",
+            "@type": "dcat:Dataset",
+            "modified": "2023-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Jeff Kararo",
+                "hasEmail": "mailto:mnr0@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/bst4-hnte",
+            "description": "",
+            "title": "JMK_DHDS_POC",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bst4-hnte/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bst4-hnte/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bst4-hnte/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bst4-hnte/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/w9p6-ixjq",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2024-11-06",
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
+            "identifier": "77bfc8f8-bd07-5ac2-895b-546636b7c458",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "CoreSet pillar v2.10.64 (coreset-dev)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/pillar.csv",
+                    "description": "CoreSet pillar v2.10.64 (coreset-dev)",
+                    "@type": "dcat:Distribution",
+                    "title": "CoreSet pillar v2.10.64 (coreset-dev)"
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
+            "landingPage": "https://data.cdc.gov/d/dmnu-8erf",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-05-10",
+            "@type": "dcat:Dataset",
+            "temporal": "2019-12-29/2023-07-29",
+            "modified": "2023-11-02",
+            "keyword": [
+                "coronavirus",
+                "covid-19",
+                "death rate",
+                "deaths",
+                "hhs region",
+                "mortality",
+                "nchs",
+                "nvss",
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
+            "identifier": "https://data.cdc.gov/api/views/dmnu-8erf",
+            "description": "This file contains COVID-19 death counts and rates by jurisdiction of residence (U.S., HHS Region) and demographic characteristics (sex, age, race and Hispanic origin, and age/race and Hispanic origin). United States death counts and rates include the 50 states, plus the District of Columbia. \n\nDeaths with confirmed or presumed COVID-19, coded to ICD\u201310 code U07.1. Number of deaths reported in this file are the total number of COVID-19 deaths received and coded as of the date of analysis and may not represent all deaths that occurred in that period. Counts of deaths occurring before or after the reporting period are not included in the file.\n\nData during recent periods are incomplete because of the lag in time between when the death occurred and when the death certificate is completed, submitted to NCHS and processed for reporting purposes. This delay can range from 1 week to 8 weeks or more, depending on the jurisdiction and cause of death.\n\nDeath counts should not be compared across jurisdictions. Data timeliness varies by state. Some states report deaths on a daily basis, while other states report deaths weekly or monthly. \n\nThe ten (10) United States Department of Health and Human Services (HHS) regions include the following jurisdictions. Region 1: Connecticut, Maine, Massachusetts, New Hampshire, Rhode Island, Vermont; Region 2: New Jersey, New York; Region 3: Delaware, District of Columbia, Maryland, Pennsylvania, Virginia, West Virginia; Region 4: Alabama, Florida, Georgia, Kentucky, Mississippi, North Carolina, South Carolina, Tennessee; Region 5: Illinois, Indiana, Michigan, Minnesota, Ohio, Wisconsin; Region 6: Arkansas, Louisiana, New Mexico, Oklahoma, Texas; Region 7: Iowa, Kansas, Missouri, Nebraska; Region 8: Colorado, Montana, North Dakota, South Dakota, Utah, Wyoming; Region 9: Arizona, California, Hawaii, Nevada; Region 10: Alaska, Idaho, Oregon, Washington.\n\nRates were calculated using the population estimates for 2021, which are estimated as of July 1, 2021 based on the Blended Base produced by the US Census Bureau in lieu of the April 1, 2020 decennial population count. The Blended Base consists of the blend of Vintage 2020 postcensal population estimates, 2020 Demographic Analysis Estimates, and 2020 Census PL 94-171 Redistricting File (see https://www2.census.gov/programs-surveys/popest/technical-documentation/methodology/2020-2021/methods-statement-v2021.pdf).\n\nRate are based on deaths occurring in the specified week and are age-adjusted to the 2000 standard population using the direct method (see https://www.cdc.gov/nchs/data/nvsr/nvsr70/nvsr70-08-508.pdf). These rates differ from annual age-adjusted rates, typically presented in NCHS publications based on a full year of data and annualized weekly age-adjusted rates which have been adjusted to allow comparison with annual rates. Annualization rates presents deaths per year per 100,000 population that would be expected in a year if the observed period specific (weekly) rate prevailed for a full year.\n\nSub-national death counts between 1-9 are suppressed in accordance with NCHS data confidentiality standards. Rates based on death counts less than 20 are suppressed in accordance with NCHS standards of reliability as specified in NCHS Data Presentation Standards for Proportions (available from: https://www.cdc.gov/nchs/data/series/sr_02/sr02_175.pdf.).",
+            "title": "Provisional COVID-19 death counts and rates, by jurisdiction of residence and demographic characteristics",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dmnu-8erf/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dmnu-8erf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dmnu-8erf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dmnu-8erf/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/wa3r-khqx",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-12-01",
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
+            "identifier": "d890d3a9-6b00-43fd-8b31-fcba4c8e2909",
+            "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
+            "title": "State Drug Utilization Data 2023",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/SDUD2023.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P10Y",
+            "theme": [
+                "State Drug Utilization"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/dhdsp/maps/index.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-02-18",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-24",
+            "keyword": [
+                "cardiovascular",
+                "cardiovascular disease",
+                "counties",
+                "county",
+                "heart",
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
+            "identifier": "https://data.cdc.gov/api/views/7b9s-s8ck",
+            "description": "This dataset documents rates and trends in heart disease and stroke mortality. Specifically, this report presents county (or county equivalent) estimates of heart disease and stroke death rates in 2000-2019 and trends during two intervals (2000-2010, 2010-2019) by age group (ages 35\u201364 years, ages 65 years and older), race/ethnicity (non-Hispanic American Indian/Alaska Native, non-Hispanic Asian/Pacific Islander, non-Hispanic Black, Hispanic, non-Hispanic White), and sex (women, men). The rates and trends were estimated using a Bayesian spatiotemporal model and a smoothed over space, time, and demographic group. Rates are age-standardized in 10-year age groups using the 2010 US population. Data source: National Vital Statistics System.",
+            "title": "Rates and Trends in Heart Disease and Stroke Mortality Among US Adults (35+) by County, Age Group, Race/Ethnicity, and Sex \u2013 2000-2019",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7b9s-s8ck/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7b9s-s8ck/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7b9s-s8ck/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/7b9s-s8ck/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "theme": [
+                "Heart Disease & Stroke Prevention"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/art/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-01-01",
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
+            "identifier": "https://data.cdc.gov/api/views/24w5-nppr",
+            "description": "Data were updated on September 11, 2024.\n\nART data are made available as part of the National ART Surveillance System (NASS) that collects success rates, services, profiles and annual summary data from fertility clinics across the U.S. There are four datasets available: ART Services and Profiles, ART Patient and Cycle Characteristics, ART Success Rates, and ART Summary. All four datasets may be linked by \u201cClinicID.\u201d ClinicID is a unique identifier for each clinic that reported cycles. The Summary dataset provides a full snapshot of clinic services and profile, patient characteristics, and ART success rates. It is worth noting that patient medical characteristics, such as age, diagnosis, and ovarian reserve, affect ART treatment\u2019s success. Comparison of success rates across clinics may not be meaningful because of differences in patient populations and ART treatment methods. The success rates displayed in this dataset do not reflect any one patient\u2019s chance of success. Patients should consult with a doctor to understand their chance of success based on their own characteristics.",
+            "title": "2021 Final Assisted Reproductive Technology (ART) Summary",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/24w5-nppr/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/24w5-nppr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/24w5-nppr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/24w5-nppr/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://data.cdc.gov/dataset/2021-Final-Assisted-Reproductive-Technology-ART-Su/24w5-nppr/revisions/0",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Assisted Reproductive Technology (ART)"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/dataset/head-start-impact-study",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2013-06-18",
+            "temporal": "2002-01-01T00:00:00-05:00/2006-01-01T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "children's health",
+                "child well-being",
+                "head start"
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
+            "identifier": "989e4cbb-2319-4c3c-a61c-ce2fa009549b",
+            "description": "<p>Nationally representative, longitudinal information from an evaluation where children were randomly assigned to Head Start or community services as usual;direct assessments and observations of children as well as parent and staff interviews were conducted</p>",
+            "title": "Head Start Impact Study",
+            "programCode": [
+                "009:092"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://researchconnections.Org",
+                    "mediaType": "text/html",
+                    "title": "API "
+                }
+            ],
+            "describedBy": "http://www.researchconnections.org/childcare/studies/29462/documentation",
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/rsvvaxview/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-09-26",
+            "@type": "dcat:Dataset",
+            "temporal": "2024-2025",
+            "modified": "2025-01-29",
+            "keyword": [
+                "iis",
+                "iqvia",
+                "nis-acm",
+                "nis-flu",
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
+            "identifier": "https://data.cdc.gov/api/views/vdz4-qrri",
+            "description": "Infant Protection Against RSV by Maternal RSV Vaccination or Receipt of Nirsevimab and Intent for Nirsevimab Receipt, Reported by Females Aged 18-49 Years Who Have an Infant <8 Months During the RSV Season (born since April 1, 2024)\n\nMonthly estimates of infant protection against RSV by maternal RSV vaccination or receipt of nirsevimab, as well as intent for nirsevimab receipt, were calculated using data from the from the National Immunization Survey\u2013Adult COVID Module (NIS\u2013ACM). (https://www.cdc.gov/nis/about/index.html). Data were reported by adult females aged 18-49 years with infants under the age of 8 months during the RSV season (born since April 1, 2024). The NIS\u2013ACM is an ongoing random-digit-dial cellular telephone survey of households with adults 18 years and older. All estimates are based upon parent-reported receipt of nirsevimab.",
+            "title": "Infant Protection Against Respiratory Syncytial Virus (RSV) by Maternal RSV Vaccination or Receipt of Nirsevimab, and Intent for Nirsevimab Receipt, United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vdz4-qrri/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vdz4-qrri/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vdz4-qrri/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vdz4-qrri/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States- National, Region, State",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Monthly",
+            "theme": [
+                "Pregnancy & Vaccination"
+            ],
+            "language": [
+                "English"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-02-21",
+            "temporal": "1988/2018",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-11",
+            "keyword": [
+                "black or african american",
+                "body mass index",
+                "body weight",
+                "children and adolescents",
+                "chronic conditions",
+                "health risk factors",
+                "health us",
+                "hispanic or latino",
+                "mexican",
+                "obesity",
+                "overweight",
+                "poverty",
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
+            "identifier": "https://data.cdc.gov/api/views/w9cp-q6sg",
+            "description": "Data on obesity among children and adolescents aged 2-19 years in the United States, by selected characteristics, including sex, age, race, Hispanic origin, and poverty level. Data are from Health, United States. SOURCE: National Center for Health Statistics, National Health and Nutrition Examination Survey.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
+            "title": "DQS Obesity among children and adolescents aged 2\u201319 years, by selected characteristics: United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/w9cp-q6sg/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/w9cp-q6sg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/w9cp-q6sg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/w9cp-q6sg/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/idgn-d2g2",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2015-02-05",
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
+            "identifier": "https://data.cdc.gov/api/views/idgn-d2g2",
+            "description": "Download the latest version of the Glossary and Methodology File",
+            "title": "Tobacco Use Supplement to the Current Population Survey (TUS-CPS) Glossary and Methodology",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/idgn-d2g2/application/zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Survey Data"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/wdvd-qg2g",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-08-06",
+            "@type": "dcat:Dataset",
+            "modified": "2024-08-14",
+            "keyword": [
+                "benefits and cost sharing",
+                "exchange puf",
+                "marketplace puf",
+                "py2024"
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
+            "identifier": "958672e5-d4f3-464f-b75f-411000f1dafd",
+            "description": "The Benefits and Cost Sharing PUF (BenCS-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The BenCS-PUF contains plan variant-level data on essential health benefits, coverage limits, and cost sharing for each QHP and SADP.",
+            "title": "Benefits and Cost Sharing PUF - PY2024",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2024/Benefits_Cost_Sharing_PUF.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/vaccines/data-reporting/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2025-01-29",
+            "@type": "dcat:Dataset",
+            "temporal": "2024-2025",
+            "modified": "2025-01-29",
+            "keyword": [
+                "iis",
+                "iqvia",
+                "nis",
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
+            "identifier": "https://data.cdc.gov/api/views/nqu5-vn7d",
+            "description": "\u2022 Weekly Cumulative RSV Vaccination Coverage, by Race and Ethnicity, Medicare Fee-For-Service Beneficiaries aged 75 years\n\n\u2022 RSV vaccination coverage among Medicare-Fee-for-service beneficiaries aged 75 years and older and enrolled in a Part D plan in assessed using data files from the Medicare Fee-for-Service (FFS) administrative claims data managed by the Centers for Medicare & Medicaid Services (CMS).",
+            "title": "Weekly Cumulative RSV Vaccination Coverage, by Race and Ethnicity, Medicare Fee-For-Service Beneficiaries aged \u226575 years and enrolled in a Part D plan, United States, Data Source: Centers for Medicare & Medicaid Services Chronic Conditions Warehouse",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/nqu5-vn7d/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/nqu5-vn7d/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/nqu5-vn7d/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/nqu5-vn7d/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-02-26",
+            "@type": "dcat:Dataset",
+            "modified": "2022-03-30",
+            "keyword": [
+                "deaths",
+                "drug overdose",
+                "mortality",
+                "nchs",
+                "nowcasting",
+                "nvss",
+                "provisional",
+                "state",
+                "suicide",
+                "transport accidents",
+                "united states",
+                "vsrr",
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
+            "identifier": "https://data.cdc.gov/api/views/v2g4-wqg2",
+            "description": "This dataset provides model-based provisional estimates of the weekly numbers of drug overdose, suicide, and transportation-related deaths using \u201cnowcasting\u201d methods to account for the normal lag between the occurrence and reporting of these deaths. Estimates less than 10 are suppressed. These early model-based provisional estimates were generated using a multi-stage hierarchical Bayesian modeling process to generate smoothed estimates of the weekly numbers of death, accounting for reporting lags. These estimates are based on several assumptions about how the reporting lags have changed in recent months across different jurisdictions, and the resulting estimates differ from other sources of provisional mortality data.  For now, these estimates should be considered highly uncertain until further evaluations can be done to determine the validity of these assumptions about timeliness. The true patterns in reporting lags will not be known until data are finalized, typically 11\u201312 months after the end of the calendar year. Importantly, these estimates are not a replacement for monthly provisional drug overdose death counts, or quarterly provisional mortality estimates. For more detail about the nowcasting methods and models, see:\n\nRossen LM, Hedegaard H, Warner M, Ahmad FB, Sutton PD. Early provisional estimates of drug overdose, suicide, and transportation-related deaths: Nowcasting methods to account for reporting lags. Vital Statistics Rapid Release; no 11. Hyattsville, MD: National Center for Health Statistics. February 2021. DOI: https://doi.org/10.15620/ cdc:101132",
+            "title": "Early Model-based Provisional Estimates of Drug Overdose, Suicide, and Transportation-related Deaths",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/v2g4-wqg2/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/v2g4-wqg2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/v2g4-wqg2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/v2g4-wqg2/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "http://ccdb.ucsd.edu/home",
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
+                "fn": "DEATHERAGE, JAMES F.\u00a0",
+                "hasEmail": "mailto:deatherj@nigms.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
+            "identifier": "4368a9ec-2999-4c06-80c6-6e50d160a1b2",
+            "description": "<p>The Cell Centered Database (CCDB) is a web accessible database for high resolution 2D, 3D and 4D data from light and electron microscopy, including correlated imaging.</p>",
+            "title": "Cell Centred Database (CCDB)",
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
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-admissions-teds-1998",
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
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1998-nid13615",
+            "description": "<p>The Treatment Episode Data Set -- Admissions (TEDS-A) is a national census data system of annual admissions to substance abuse treatment facilities. TEDS-A provides annual data on the number and characteristics of persons admitted to public and private substance abuse treatment programs that receive public funding. The unit of analysis is a treatment admission. TEDS consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Discharges (TEDS-D), collects data on discharges from substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables in the MDS include: information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008).<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "title": "Treatment Episode Data Set: Admissions (TEDS-A-1998)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1998-nid13615",
+                    "description": "Treatment Episode Data Set: Admissions (TEDS-A-1998) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-admissions-teds-1998-nid13615"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/home-health-agency-all-owners",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-04-20",
+            "temporal": "2023-04-01/2025-03-31",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-15",
+            "references": [
+                "https://data.cms.gov/sites/default/files/2024-10/HHA_Data_Guidance.pdf"
+            ],
+            "keyword": [
+                "home health",
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/fc009b2d-7846-44b1-b4a1-692f0c143879/data-viewer",
+            "description": "The Home Health Agency (HHA) All Owners dataset provides ownership information on all HHAs currently enrolled in Medicare. This data includes ownership information such as ownership name, ownership type, ownership address and ownership effective date.",
+            "title": "Home Health Agency All Owners",
+            "describedByType": "application/pdf",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/fc009b2d-7846-44b1-b4a1-692f0c143879/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Home Health Agency All Owners : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/a0443d0f-247e-481e-8d62-cdd0621238d4/HHA_All_Owners_2025.01.02.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Health Agency All Owners : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a338d79f-d7fc-4503-91f9-ae2696742830/data",
+                    "mediaType": "text/html",
+                    "title": "Home Health Agency All Owners : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/64509ec7-b479-4b46-bd26-0dcbd7d73e81/HHA_All_Owners_2024.10.07.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Health Agency All Owners : 2024-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/dfa40c06-c5cf-43aa-a70c-15b95ae240b9/data",
+                    "mediaType": "text/html",
+                    "title": "Home Health Agency All Owners : 2024-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/bc041dea-adee-47a0-8c8c-bf0140182588/HHA_All_Owners_2024.07.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Health Agency All Owners : 2024-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/539fa7db-5720-438d-ae94-555c156e17fd/data",
+                    "mediaType": "text/html",
+                    "title": "Home Health Agency All Owners : 2024-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/7755410d-7688-4d0f-9647-dc5c530375ef/HHA_All_Owners_2024.04.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Health Agency All Owners : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c745e6c8-795f-4b3e-89df-12e85264a892/data",
+                    "mediaType": "text/html",
+                    "title": "Home Health Agency All Owners : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/7fc04d2a-a6c3-437d-878d-77692dc8c12e/HHA_All_Owners_2024.01.05.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Health Agency All Owners : 2024-01-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/c1b3a866-2efa-416c-8f7b-6f17e553dbf1/data",
+                    "mediaType": "text/html",
+                    "title": "Home Health Agency All Owners : 2024-01-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/2e7c7a07-c96a-42d1-ba9b-e898ec55dce3/HHA_All_Owners_2023.10.02.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Health Agency All Owners : 2023-10-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8f1a6139-8df2-4bfd-9e95-8ce4adec6488/data",
+                    "mediaType": "text/html",
+                    "title": "Home Health Agency All Owners : 2023-10-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/988040ed-3766-4b8f-862c-e15d07dbe430/HHA_All_Owners_2023.07.06.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Health Agency All Owners : 2023-07-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/94c1d434-bdad-47e5-b301-6bcf8634af6b/data",
+                    "mediaType": "text/html",
+                    "title": "Home Health Agency All Owners : 2023-07-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/cfb66ea6-604a-4eaf-b50e-f991a3922731/HHA_All_Owners_2023.03.31.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Health Agency All Owners : 2023-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/84a40ec7-d315-48e4-b2ed-ec00878cfec5/data",
+                    "mediaType": "text/html",
+                    "title": "Home Health Agency All Owners : 2023-04-01"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-10/HHA_All_Owners_Data_Dictionary.pdf",
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
+            "landingPage": "https://healthdata.gov/d/wh9n-d2tx",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2022-01-05",
+            "@type": "dcat:Dataset",
+            "modified": "2023-01-18",
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
+            "identifier": "dfa2ab14-06c2-457a-9e36-5cb6d80f8d93",
+            "description": "National Average Drug Acquisition Cost (NADAC) weekly reference data for the calendar year.",
+            "title": "NADAC (National Average Drug Acquisition Cost) 2022",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/nadac-national-average-drug-acquisition-cost-2022.csv",
+                    "mediaType": "text/csv",
+                    "title": "NADAC (National Average Drug Acquisition Cost) 2022"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y",
+            "theme": [
+                "National Average Drug Acquisition Cost",
+                "Drug Pricing and Payment"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/ipap-cksm",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ipap-cksm",
+            "description": "<b>(Includes MeSH 2023 and 2024 changes)</b>  The MeSH 2025 Update - Preferred Term Update Report lists changes to the Preferred Term of a Descriptor or a Supplementary Concept Record (SCR).  <b>This report includes MeSH changes from previous years, starting from 2023.</b>",
+            "title": "MeSH 2025 Update - Preferred Term Update Report",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/ipap-cksm/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/ipap-cksm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/ipap-cksm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/ipap-cksm/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Terminology"
+            ]
+        },
+        {
+            "accessLevel": "restricted public",
+            "landingPage": "https://www.hcup-us.ahrq.gov/db/state/sasddbdocumentation.jsp",
+            "bureauCode": [
+                "009:33"
+            ],
+            "rights": "N/A",
+            "issued": "2021-02-13",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "ambulatory surgery",
+                "claims",
+                "diagnoses",
+                "epidemiology",
+                "hcup",
+                "health care",
+                "health care cost",
+                "health care providers",
+                "health statistics",
+                "hospital",
+                "procedures",
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
+            "identifier": "eabeb3a6-d2d7-43be-b43d-f83414eb7ee1",
+            "description": "The Healthcare Cost and Utilization Project (HCUP) State Ambulatory Surgery Databases (SASD) contain the universe of hospital-based ambulatory surgery encounters in participating States.  The SASD include encounter-level data for ambulatory surgeries and may also include various types of outpatient services such as observation stays, lithotripsy, radiation therapy, imaging, chemotherapy, and labor and delivery. The specific types of ambulatory surgery and outpatient services included in each SASD vary by State and data year. All SASD include data from hospital-owned ambulatory surgery facilities. In addition, some States include data from nonhospital-owned facilities. The data are translated into a uniform format to facilitate multi-State comparisons and analyses. The SASD include all patients in participating settings, regardless of the expected payer including but not limited to Medicare, Medicaid, private insurance, self-pay, or those billed as \u2018no charge\u2019. Developed through a Federal-State-Industry partnership sponsored by the Agency for Healthcare Research and Quality (AHRQ), HCUP data inform decision making at the national, State, and community levels.\n\nThe SASD contain clinical and resource use information included in a typical discharge abstract, with safeguards to protect the privacy of individual patients, physicians, and facilities (as required by data sources). Data elements include but are not limited to: diagnoses, procedures, admission and discharge status, patient demographics (e.g., gender, age), total charges, and expected payment source. In addition to the core set of uniform data elements common to all SASD, some include State-specific data elements. The SASD exclude data elements that could directly or indirectly identify individuals. For some States, hospital and county identifiers are included that permit linkage to the American Hospital Association Annual Survey File and the Bureau of Health Professions' Area Resource File except in States that do not allow the release of hospital identifiers.\n\nRestricted access data files are available with a data use agreement and brief online security training.",
+            "title": "HCUP State Ambulatory Surgery Databases (SASD) - Restricted Access Files",
+            "programCode": [
+                "009:072"
+            ],
+            "describedBy": "https://www.hcup-us.ahrq.gov/db/state/sasddbdocumentation.jsp",
+            "license": "https://www.distributor.hcup-us.ahrq.gov/Home.aspx",
+            "theme": [
+                "State"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/wjrc-wdfw",
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
+            "identifier": "ce69c011-1dc5-5ffa-94fb-d3e9b05afc4b",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "Scorecard measure_value v2.11.9 (prod)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.9/20241107/measure_value.csv",
+                    "description": "Scorecard measure_value v2.11.9 (prod)",
+                    "@type": "dcat:Distribution",
+                    "title": "Scorecard measure_value v2.11.9 (prod)"
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
+            "landingPage": "https://data.cms.gov/provider-characteristics/medicare-provider-supplier-enrollment/medicare-fee-for-service-public-provider-enrollment",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2023-01-01/2024-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-15",
+            "references": [
+                "https://data.cms.gov/resources/fee-for-service-public-provider-enrollment-methodology"
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/2457ea29-fc82-48b0-86ec-3b0755de7515/data-viewer",
+            "description": "The Medicare Fee-For-Service Public Provider Enrollment dataset includes information on providers who are actively approved to bill Medicare or have completed the 855O at the time the data was pulled from the Provider Enrollment, Chain, and Ownership System (PECOS). The release of this provider enrollment data is not related to other provider information releases such as Physician Compare or Data Transparency.\n\n\u00a0\n\nNote: This full dataset contains more records than most spreadsheet programs can handle, which will result in an incomplete load of data. Use of a database or statistical software is required.",
+            "title": "Medicare Fee-For-Service  Public Provider Enrollment",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/2457ea29-fc82-48b0-86ec-3b0755de7515/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Medicare Fee-For-Service Public Provider Enrollment : 2024-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/8ced283e-4017-4b90-b511-142aabb8531b/PPEF_Enrollment_Extract_2025.01.02.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Fee-For-Service Public Provider Enrollment : 2024-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/7dcf9ea6-ee2f-4bf1-8b5d-39c18b0e8541/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Fee-For-Service Public Provider Enrollment : 2024-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/8e1bbada-e9a4-4a4c-9017-539c5cb1fff8/PPEF_Enrollment_Extract_2024.10.07.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Fee-For-Service Public Provider Enrollment : 2024-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/57312fe7-f2cc-4cda-b4a0-78d9edb42f67/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Fee-For-Service Public Provider Enrollment : 2024-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/0c28f2f8-4153-421c-a9b7-72a5be89d9e6/PPEF_Enrollment_Extract_2024.07.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Fee-For-Service Public Provider Enrollment : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8d9854d3-6b9f-49df-b315-5e4e50df7aa7/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Fee-For-Service Public Provider Enrollment : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/07dedcbc-ff73-4097-a83d-7be34d526aa9/PPEF_Enrollment_Extract_2024.04.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Fee-For-Service Public Provider Enrollment : 2024-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a5cac43c-010d-4190-9395-d8841b1c5cc6/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Fee-For-Service Public Provider Enrollment : 2024-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/22961024-cac8-43fc-86d1-163e19dca5cf/PPEF_Enrollment_Extract_2024.01.05.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Fee-For-Service Public Provider Enrollment : 2023-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3d7326b6-f5cc-49ba-967b-20c484af40ce/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Fee-For-Service Public Provider Enrollment : 2023-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/d2c13c22-d68b-4d46-8436-0e2a6abac4c9/PPEF_Enrollment_Extract_2023.10.02.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Fee-For-Service Public Provider Enrollment : 2023-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/cf2b32cc-c0e8-4d3c-bfdf-7752be357f6b/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Fee-For-Service Public Provider Enrollment : 2023-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/dc5e6313-b126-4f77-9846-2a63d32787d7/PPEF_Enrollment_Extract_2023.07.06.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Fee-For-Service Public Provider Enrollment : 2023-06-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/20fd773a-7f15-48ed-8164-f543706269a4/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Fee-For-Service Public Provider Enrollment : 2023-06-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/0239bace-c79e-461c-9fed-04e165280f25/PPEF_Enrollment_Extract_2023.03.31.csv",
+                    "mediaType": "text/csv",
+                    "title": "Medicare Fee-For-Service Public Provider Enrollment : 2023-03-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f783ac85-fd89-4db9-a7e9-288cda155258/data",
+                    "mediaType": "text/html",
+                    "title": "Medicare Fee-For-Service Public Provider Enrollment : 2023-03-31"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/medicare-fee-for-service-public-provider-enrollment-data-dictionary",
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
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2007",
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
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2007-nid13532",
+            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series<br />\n(formerly titled National Household Survey on Drug Abuse) primarily<br />\nmeasures the prevalence and correlates of drug use in the United<br />\nStates. The surveys are designed to provide quarterly, as well as<br />\nannual, estimates. Information is provided on the use of illicit<br />\ndrugs, alcohol, and tobacco among members of United States households<br />\naged 12 and older. Questions included age at first use as well as<br />\nlifetime, annual, and past-month usage for the following drug classes:<br />\nmarijuana, cocaine (and crack), hallucinogens, heroin, inhalants,<br />\nalcohol, tobacco, and nonmedical use of prescription drugs, including<br />\npain relievers, tranquilizers, stimulants, and sedatives. The survey<br />\ncovered substance abuse treatment history and perceived need for<br />\ntreatment, and included questions from the Diagnostic and Statistical<br />\nManual (DSM) of Mental Disorders that allow diagnostic criteria to be<br />\napplied. The survey included questions concerning treatment for both<br />\nsubstance abuse and mental health related disorders. Respondents were<br />\nalso asked about personal and family income sources and amounts,<br />\nhealth care access and coverage, illegal activities and arrest record,<br />\nproblems resulting from the use of drugs, and needle-sharing.<br />\nQuestions introduced in previous administrations were retained in the<br />\n2007 survey, including questions asked only of respondents aged 12 to<br />\n17. These \"youth experiences\" items covered a variety of topics, such<br />\nas neighborhood environment, illegal activities, drug use by friends,<br />\nsocial support, extracurricular activities, exposure to substance<br />\nabuse prevention and education programs, and perceived adult attitudes<br />\ntoward drug use and activities such as school work. Several measures<br />\nfocused on prevention-related themes in this section. Also retained<br />\nwere questions on mental health and access to care, perceived risk of<br />\nusing drugs, perceived availability of drugs, driving and personal<br />\nbehavior, and cigar smoking. Questions on the tobacco brand used most<br />\noften were introduced with the 1999 survey. Background information<br />\nincludes gender, race, age, ethnicity, marital status, educational<br />\nlevel, job status, veteran status, and current household composition.This study has 1 Data Set.</p>",
+            "title": "National Survey on Drug Use and Health (NSDUH-2007)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2007-nid13532",
+                    "description": "National Survey on Drug Use and Health (NSDUH-2007) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2007-nid13532"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NAMCS/doc2016_clas.pdf",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NAMCS/",
+            "issued": "2018-11-20",
+            "@type": "dcat:Dataset",
+            "temporal": "2016",
+            "modified": "2023-09-27",
+            "references": [
+                "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NAMCS/readme2016_clas.txt"
+            ],
+            "keyword": [
+                "cultural-health-beliefs",
+                "health-practices",
+                "namcs",
+                "office-based physicians",
+                "physicians",
+                "preferred-languages"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo@cdc.gov "
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/jy4b-8v6u",
+            "description": "The purpose of the National CLAS Physician Survey was to understand the provision of culturally and linguistically appropriate services among office-based physicians. The National CLAS Physician Survey was a supplement to the National Ambulatory Medical Care Survey (NAMCS), which is a national probability sample survey of visits to office-based physicians. NAMCS is a component of the National Health Care Surveys that measured health care utilization across a variety of health care providers\u2019 settings. NAMCS and the National CLAS Physician Survey were conducted by the National Center for Health Statistics (NCHS). The National CLAS Physician Survey public use file includes data from office-based physicians. No patient level data were collected. This documentation describes the public use micro-data file produced from data collected in the National CLAS Physician Survey.",
+            "title": "National Ambulatory Medical Care Survey: Culturally and Linguistically Appropriate Services Supplement, 2016",
+            "describedByType": "application/pdf",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/jy4b-8v6u/text/plain",
+                    "mediaType": "text/plain"
+                }
+            ],
+            "spatial": "United States",
+            "describedBy": "https://www.cdc.gov/nchs/data/ahcd/2016_NAMCS_CLAS_Sample_Card.pdf",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Survey will not be updated.",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/k62p-6esq",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-05-04",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "dhds",
+                "disability"
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
+            "identifier": "https://data.cdc.gov/api/views/k62p-6esq",
+            "description": "Disability and Health Data System (DHDS) is an online source of state-level data on adults with disabilities. Users can access information on six functional disability types: cognitive (serious difficulty concentrating, remembering or making decisions), hearing (serious difficulty hearing or deaf), mobility (serious difficulty walking or climbing stairs), vision (serious difficulty seeing), self-care (difficulty dressing or bathing) and independent living (difficulty doing errands alone).",
+            "title": "Disability and Health Data System (DHDS)",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/k62p-6esq/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/k62p-6esq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/k62p-6esq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/k62p-6esq/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "Annually",
+            "theme": [
+                "Disability & Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/nhanes/visualization/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-03-02",
+            "@type": "dcat:Dataset",
+            "temporal": "1999/2018",
+            "modified": "2023-04-18",
+            "keyword": [
+                "infectious disease"
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
+            "identifier": "https://data.cdc.gov/api/views/pqn7-e45s",
+            "description": "These data represent prevalence estimates of select infectious diseases from the National Health and Nutrition Examination Survey (NHANES).",
+            "title": "NHANES Select Infectious Diseases Prevalence Estimates",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pqn7-e45s/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pqn7-e45s/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pqn7-e45s/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pqn7-e45s/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "U.S.",
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
+            "landingPage": "https://www.cdc.gov/brfss/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-07-19",
+            "@type": "dcat:Dataset",
+            "modified": "2023-09-06",
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
+            "identifier": "https://data.cdc.gov/api/views/y4ft-s73h",
+            "description": "1995-2010. BRFSS land line only prevalence data. BRFSS is a continuous, state-based surveillance system that collects information about modifiable risk factors for chronic diseases and other leading causes of death. Data will be updated annually as it becomes available. Detailed information on sampling methodology and quality assurance can be found on the BRFSS website (http://www.cdc.gov/brfss). Methodology: http://www.cdc.gov/brfss/factsheets/pdf/DBS_BRFSS_survey.pdf Glossary: https://chronicdata.cdc.gov/Behavioral-Risk-Factors/Behavioral-Risk-Factor-Surveillance-System-BRFSS-H/iuq5-y9ct/data",
+            "title": "Behavioral Risk Factor Surveillance System (BRFSS) Prevalence Data (2010 and prior)",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/y4ft-s73h/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/y4ft-s73h/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/y4ft-s73h/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/y4ft-s73h/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "theme": [
+                "Behavioral Risk Factors"
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
+            "modified": "2024-10-17",
+            "references": [
+                "https://academic.oup.com/aje/article/179/8/1025/109078",
+                "https://academic.oup.com/aje/article/182/2/127/93984",
+                "https://www.cdc.gov/pcd/issues/2017/pdf/17_0281.pdf",
+                "https://www.cdc.gov/pcd/issues/2018/18_0313.htm"
+            ],
+            "keyword": [
+                "500 cities",
+                "census",
+                "estimates",
+                "prevalence",
+                "tracts"
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
+            "identifier": "https://data.cdc.gov/api/views/9z78-nsfp",
+            "description": "This is the complete dataset for the 500 Cities project 2016 release. This dataset includes 2013, 2014 model-based small area estimates for 27 measures of chronic disease related to unhealthy behaviors (5), health outcomes (13), and use of preventive services (9). Data were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. It represents a first-of-its kind effort to release information on a large scale for cities and for small areas within those cities. It includes estimates for the 500 largest US cities and approximately 28,000 census tracts within these cities. These estimates can be used to identify emerging health problems and to inform development and implementation of effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these measures include Behavioral Risk Factor Surveillance System (BRFSS) data (2013, 2014), Census Bureau 2010 census population data, and American Community Survey (ACS) 2009-2013, 2010-2014 estimates. More information about the methodology can be found at www.cdc.gov/500cities.\nNote: During the process of uploading the 2015 estimates, CDC found a data discrepancy in the published 500 Cities data for the 2014 city-level obesity crude prevalence estimates caused when reformatting the SAS data file to the open data format. . The small area estimation model and code were correct. This data discrepancy only affected the 2014 city-level obesity crude prevalence estimates on the Socrata open data file, the GIS-friendly data file, and the 500 Cities online application. The other obesity estimates (city-level age-adjusted and tract-level) and the Mapbooks were not affected. No other measures were affected. The correct estimates are update in this dataset on October 25, 2017.",
+            "title": "500 Cities: Local Data for Better Health, 2016 release",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9z78-nsfp/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9z78-nsfp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9z78-nsfp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9z78-nsfp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/500-Cities/500-Cities-Local-Data-for-Better-Health-2016-relea/9z78-nsfp",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "500 Cities & Places"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/provider-compliance/public-reporting-of-missing-digital-contact-information",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2023-01-01/2024-09-30",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-25",
+            "references": [
+                "https://data.cms.gov/sites/default/files/2021-12/8eb2b4bf-6e5f-4e05-bcdb-39c07ad8f77a/Missing_Digital_Contact_Info_Methods%20.pdf"
+            ],
+            "keyword": [
+                "medicare",
+                "provider enrollment"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "CMS Health Informatics and Interoperability Group - CPI",
+                "hasEmail": "mailto:CMSInteroperability@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/63a83bb1-4c02-43b3-8ef4-e3d3c6cf62fa/data-viewer",
+            "description": "In the May 2020 CMS Interoperability and Patient Access final rule, CMS finalized the policy to publicly report the names and NPIs of those providers who do not have digital contact information included in the NPPES system (85 FR 25584). This data includes the NPI and provider name of providers and clinicians without digital contact information in NPPES.",
+            "title": "Public Reporting of Missing Digital Contact Information",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/63a83bb1-4c02-43b3-8ef4-e3d3c6cf62fa/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Public Reporting of Missing Digital Contact Information : 2024-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/fb284594-a4ff-442f-8b66-f6838c4355ce/Providers%20without%20Endpoints%20-30Sep2024%20.csv",
+                    "mediaType": "text/csv",
+                    "title": "Public Reporting of Missing Digital Contact Information : 2024-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/2bad6a8a-6cee-4d5f-b67b-da236cd75693/data",
+                    "mediaType": "text/html",
+                    "title": "Public Reporting of Missing Digital Contact Information : 2024-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/b2303048-8c29-42f8-a9e8-4d95adf6dd55/Providers%20without%20Endpoints%20-30Jun2024%2003-01-14.csv",
+                    "mediaType": "text/csv",
+                    "title": "Public Reporting of Missing Digital Contact Information : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/86be612a-a3d8-448a-a1fc-9652cb80b1c7/data",
+                    "mediaType": "text/html",
+                    "title": "Public Reporting of Missing Digital Contact Information : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/d48158c7-5052-44ea-8227-0e340d914dad/Providers%20without%20Endpoints%20-31Dec2023%2002-01-13.csv",
+                    "mediaType": "text/csv",
+                    "title": "Public Reporting of Missing Digital Contact Information : 2023-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3722bebc-60f1-4602-8353-9742edd93303/data",
+                    "mediaType": "text/html",
+                    "title": "Public Reporting of Missing Digital Contact Information : 2023-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/2ccf627b-05c7-4b70-b100-ce9b0da6a868/Providers%20without%20Endpoints%20-30Sep2023%2003-01-09.csv",
+                    "mediaType": "text/csv",
+                    "title": "Public Reporting of Missing Digital Contact Information : 2023-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/17ac874c-7f4e-4a58-9b31-3a8db471edb6/data",
+                    "mediaType": "text/html",
+                    "title": "Public Reporting of Missing Digital Contact Information : 2023-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/54beba1e-1824-417e-a8e2-0ca88fa4119a/Providers%20without%20Endpoints%20-30Jun2023%2003-01-11.csv",
+                    "mediaType": "text/csv",
+                    "title": "Public Reporting of Missing Digital Contact Information : 2023-06-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/0b5d3db6-2f12-4259-84e7-789caf0243ed/data",
+                    "mediaType": "text/html",
+                    "title": "Public Reporting of Missing Digital Contact Information : 2023-06-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/dbea07fd-460d-4d13-85d6-80f4bffa4309/Providers%20without%20Endpoints%20-31Mar2023%2003-00-41.csv",
+                    "mediaType": "text/csv",
+                    "title": "Public Reporting of Missing Digital Contact Information : 2023-03-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/017ceedb-fda2-4c69-b7ec-ced232268135/data",
+                    "mediaType": "text/html",
+                    "title": "Public Reporting of Missing Digital Contact Information : 2023-03-31"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/public-reporting-of-missing-digital-contact-information-data-dictionary",
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
+            "landingPage": "https://healthdata.gov/d/wrj4-twjv",
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
+            "identifier": "acbd1537-69b8-548d-a90f-eedb416acd71",
+            "description": "Drug utilization data are reported by states for covered outpatient drugs that are paid for by state Medicaid agencies since the start of the Medicaid Drug Rebate Program. The data includes state, drug name, National Drug Code, number of prescriptions and dollars reimbursed. Data descriptions are available on Medicaid.gov: https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/state-drug-utilization-data-faq/index.html",
+            "title": "State Drug Utilization Data 1992",
+            "programCode": [
+                "009:076"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/StateDrugUtilizationData1992.csv",
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
+            "landingPage": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "public",
+            "issued": "2015-12-02",
+            "@type": "dcat:Dataset",
+            "temporal": "1940/2015",
+            "modified": "2022-03-29",
+            "references": [
+                "http://www.cdc.gov/nchs/data/databriefs/db162.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_01.pdf",
+                "http://www.cdc.gov/nchs/data/nvsr/nvsr48/nvs48_16.pdf",
+                "http://www.cdc.gov/nchs/data_access/VitalStatsOnline.htm"
+            ],
+            "keyword": [
+                "births",
+                "nchs",
+                "nonmarital",
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
+            "identifier": "https://data.cdc.gov/api/views/g6qk-ngsf",
+            "description": "This dataset includes number of births to unmarried women by age group in the United States since 1940. \n\nMethods for collecting information on marital status changed over the reporting period and have been documented in:\n\n\u2022 Ventura SJ, Bachrach CA. Nonmarital childbearing in the United States, 1940\u201399. National vital statistics reports; vol 48 no 16. Hyattsville, Maryland: National Center for Health Statistics. 2000. Available from: http://www.cdc.gov/nchs/data/nvsr/nvsr48/nvs48_16.pdf.\n\u2022 National Center for Health Statistics. User guide to the 2013 natality public use file. Hyattsville, Maryland: National Center for Health Statistics. 2014. Available from: http://www.cdc.gov/nchs/data_access/VitalStatsOnline.htm.",
+            "title": "NCHS - Births to Unmarried Women by Age Group: United States",
+            "isPartOf": "NCHS - Births to Unmarried Women by Age Group: United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/g6qk-ngsf/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/g6qk-ngsf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/g6qk-ngsf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/g6qk-ngsf/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/provider-of-services-file-internet-quality-improvement-and-evaluation-system-home-health-agency-ambulatory-surgical-center-and-hospice-providers",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2024-02-28",
+            "temporal": "2023-10-01/2024-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-16",
+            "references": [
+                "https://data.cms.gov/resources/pos-file-iqies-for-hha-asc-and-hospice-providers-methodology"
+            ],
+            "keyword": [
+                "home health",
+                "hospice",
+                "hospitals & facilities",
+                "medicare",
+                "medicare advantage",
+                "original medicare",
+                "provider enrollment"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "QIESData - CCSQ",
+                "hasEmail": "mailto:QIESData@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/086e48c4-87a6-4be1-8823-29e8da8f225b/data-viewer",
+            "description": "The Provider of Services File (POS) - Internet Quality Improvement and Evaluation System (iQIES) - Home Health Agency (HHA), Ambulatory Surgical Center (ASC), and Hospice Providers data\u00a0provides information on provider demographic and associated certification information. In this file you will find provider number (CMS Certification Number), name, address, and other characteristics of the participating institution providers.",
+            "title": "Provider of Services File - Internet Quality Improvement and Evaluation System - Home Health Agency, Ambulatory Surgical Center, and Hospice Providers",
+            "describedByType": "application/zip",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/086e48c4-87a6-4be1-8823-29e8da8f225b/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Provider of Services File - Internet Quality Improvement and Evaluation System - Home Health Agency, Ambulatory Surgical Center, and Hospice Providers : 2024-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/bb6fa48f-a739-4655-b956-62c20d24cc34/iQIES%20HHA_HOSPICE_ASC_data%20Q4%202024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Provider of Services File - Internet Quality Improvement and Evaluation System - Home Health Agency, Ambulatory Surgical Center, and Hospice Providers : 2024-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8ee504fc-7e19-486e-937d-495ded2f7e62/data",
+                    "mediaType": "text/html",
+                    "title": "Provider of Services File - Internet Quality Improvement and Evaluation System - Home Health Agency, Ambulatory Surgical Center, and Hospice Providers : 2024-12-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/3dc6c654-92d0-43e9-af6c-71cc0ea871a4/iQIES%20HHA_HOSPICE_ASC_data%20Q3%202024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Provider of Services File - Internet Quality Improvement and Evaluation System - Home Health Agency, Ambulatory Surgical Center, and Hospice Providers : 2024-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6c56bf74-fc55-475b-89c1-4c9e11d7fac3/data",
+                    "mediaType": "text/html",
+                    "title": "Provider of Services File - Internet Quality Improvement and Evaluation System - Home Health Agency, Ambulatory Surgical Center, and Hospice Providers : 2024-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/b90d4c1c-f829-4a99-ae4d-9455ac737d73/iQIES%20HHA_HOSPICE_ASC_data%20Q2%202024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Provider of Services File - Internet Quality Improvement and Evaluation System - Home Health Agency, Ambulatory Surgical Center, and Hospice Providers : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3ba417c4-276c-4eda-aab0-f61d7f1d5062/data",
+                    "mediaType": "text/html",
+                    "title": "Provider of Services File - Internet Quality Improvement and Evaluation System - Home Health Agency, Ambulatory Surgical Center, and Hospice Providers : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/07df1751-1412-48a9-b912-d43d35a8b958/ProviderOfService_iQIES_Mar24.csv",
+                    "mediaType": "text/csv",
+                    "title": "Provider of Services File - Internet Quality Improvement and Evaluation System - Home Health Agency, Ambulatory Surgical Center, and Hospice Providers : 2024-03-24"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/5ebbce5b-fbc2-44c2-ab7d-e286ad4ae7d2/data",
+                    "mediaType": "text/html",
+                    "title": "Provider of Services File - Internet Quality Improvement and Evaluation System - Home Health Agency, Ambulatory Surgical Center, and Hospice Providers : 2024-03-24"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/dd671b87-e70b-47f2-86e1-efd5c372848f/Provider_of_Services_File_HHA_ASC_Hospices_iQiES_2023_Q4.csv",
+                    "mediaType": "text/csv",
+                    "title": "Provider of Services File - Internet Quality Improvement and Evaluation System - Home Health Agency, Ambulatory Surgical Center, and Hospice Providers : 2023-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/1540f41e-249d-4130-8da7-a2b488e8d165/data",
+                    "mediaType": "text/html",
+                    "title": "Provider of Services File - Internet Quality Improvement and Evaluation System - Home Health Agency, Ambulatory Surgical Center, and Hospice Providers : 2023-12-31"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/sites/default/files/2025-01/47cff7a0-5575-4a62-be85-ae72dcedf677/iQIES%20POS%20Data%20Dictionary.zip",
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
+            "landingPage": "https://healthdata.gov/d/wsfv-b883",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-12-10",
+            "@type": "dcat:Dataset",
+            "modified": "2024-12-18",
+            "keyword": [
+                "business rules",
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
+            "identifier": "d849f3cc-64da-408a-92d8-790ba4973737",
+            "description": "The Business Rules PUF (BR-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The BR-PUF contains plan-level data on rating business rules, such as maximum age for a dependent and allowed dependent relationships.",
+            "title": "Business Rules PUF - PY2025",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2025/business_rules_PUF.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
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
+                "https://www.cdc.gov/nchs/data/databriefs/db162.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_01.pdf"
+            ],
+            "keyword": [
+                "birth rates",
+                "ethnicity",
+                "hispanic origin",
+                "nchs",
+                "nonmarital",
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
+            "identifier": "https://data.cdc.gov/api/views/6tkz-y37d",
+            "description": "This dataset includes birth rates for unmarried women by age group, race, and Hispanic origin in the United States since 1970. \n\nMethods for collecting information on marital status changed over the reporting period and have been documented in:\n\n\u2022 Ventura SJ, Bachrach CA. Nonmarital childbearing in the United States, 1940\u201399. National vital statistics reports; vol 48 no 16. Hyattsville, Maryland: National Center for Health Statistics. 2000. Available from: http://www.cdc.gov/nchs/data/nvsr/nvsr48/nvs48_16.pdf.\n\u2022 National Center for Health Statistics. User guide to the 2013 natality public use file. Hyattsville, Maryland: National Center for Health Statistics. 2014. Available from: http://www.cdc.gov/nchs/data_access/VitalStatsOnline.htm.\n\nNational data on births by Hispanics origin exclude data for Louisiana, New Hampshire, and Oklahoma in 1989; for New Hampshire and Oklahoma in 1990; for New Hampshire in 1991 and 1992. Information on reporting Hispanic origin is detailed in the Technical Appendix for the 1999 public-use natality data file (see (ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/Nat1999doc.pdf.)\n\nAll birth data by race before 1980 are based on race of the child. Starting in 1980, birth data by race are based on race of the mother.",
+            "title": "NCHS - Birth Rates for Unmarried Women by Age, Race, and Hispanic Origin: United States",
+            "isPartOf": "NCHS - Birth Rates for Unmarried Women by Age, Race, and Hispanic Origin: United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6tkz-y37d/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6tkz-y37d/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6tkz-y37d/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6tkz-y37d/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/dataset/cdc-child-growth-charts",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2012-05-30",
+            "temporal": "1965-01-01T00:00:00-05:00/2000-12-31T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "age",
+                "babies",
+                "bmi",
+                "child",
+                "community health",
+                "growth charts",
+                "head circumference",
+                "infant",
+                "length",
+                "lms parameters",
+                "pediatric",
+                "percentiles",
+                "population statistics",
+                "stature",
+                "weight",
+                "z-scores"
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
+            "identifier": "d161b0bc-177d-4dd8-85aa-8fcf912a49f4",
+            "description": "<p>CDC child growth charts consist of a series of percentile curves that illustrate the distribution of selected body measurements in U.S. children. Pediatric growth charts have been used by pediatricians, nurses, and parents to track the growth of infants, children, and adolescents in the United States since 1977.   Growth charts are not intended to be used as a sole diagnostic instrument. Instead, growth charts are tools that contribute to forming an overall clinical impression for the child being measured.</p>",
+            "title": "CDC Child Growth Charts",
+            "programCode": [
+                "009:029"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.cdc.gov/growthcharts/",
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
+            "landingPage": "https://healthdata.gov/d/wtr7-pvy6",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-03-28",
+            "@type": "dcat:Dataset",
+            "modified": "2024-01-05",
+            "keyword": [
+                "chip",
+                "dental",
+                "dq atlas",
+                "medicaid",
+                "service use",
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
+            "identifier": "2aa0ed3d-6ef8-47a8-90b0-06b6d2fa3953",
+            "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of dental services provided to Medicaid and CHIP beneficiaries under the age of 19 (as of the first day of the month), by state. \r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating dental services measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Procedure Codes - OT Professional, Claims Volume - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+            "title": "Dental Services Provided to Medicaid and CHIP Beneficiaries Under Age 19",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/Dental-Services-Provided-to-MedicaidCHIP-Beneficiaries-Under-Age-19.csv",
+                    "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of dental services provided to Medicaid and CHIP beneficiaries under the age of 19 (as of the first day of the month), by state. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating dental services measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Procedure Codes - OT Professional, Claims Volume - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "@type": "dcat:Distribution",
+                    "title": "Dental Services Provided to Medicaid and CHIP Beneficiaries Under Age 19"
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
+            "landingPage": "https://data.cdc.gov/d/kkvj-587h",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-12-27",
+            "@type": "dcat:Dataset",
+            "modified": "2024-12-27",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Allergy and Clinical Immunology Branch (ACIB), Health Effects Laboratory Division (HELD)",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/kkvj-587h",
+            "description": "Diesel exhaust (DE) is an air pollutant containing gaseous compounds and particulate matter.  Diesel engines are common on gas extraction and oil sites, leading to complex DE exposure to a broad range of compounds through occupational settings.  The US EPA concluded that short-term exposure to DE leads to allergic inflammatory disorders of the airways.  To further evaluate the immunotoxicity of DE, the effects of whole-body inhalation of 0.2 and 1 mg/m3 DE (total carbon; 6 h/d for 4 days) were investigated 1-, 7-, and 27-days post exposure in Sprague-Dawley rats using an occupationally relevant exposure system.  DE exposure of 1 mg/m3 increased total cellularity, number of CD4+ and CD8+ T-cells, and B-cells at 1 d post-exposure in the lung lymph nodes.  At 7 d post-exposure to 1 mg/m3, cellularity and the number of CD4+ and CD8+ T-cells decreased in the LLNs.  In the bronchoalveolar lavage, B-cell number and frequency increased at 1 d post-exposure, Natural Killer cell number and frequency decreased at 7 d post-exposure, and at 27 d post-exposure CD8+ T-cell and CD11b+ cell number and frequency decreased with 0.2 mg/m3 exposure.  In the spleen, 0.2 mg/m3 increased CD4+ T-cell frequency at 1 and 7 d post-exposure and at 27 d post-exposure increased CD4+ and CD8+ T-cell number and CD8+ T-cell frequency.  B-cells were the only immune cell subset altered in the three tissues (spleen, LLNs, and BALF), suggesting the induction of the adaptive immune response.  The increase in lymphocytes in several different organ types also suggests an induction of a systemic inflammatory response occurring following DE exposure.  These results show that DE exposure induced modifications of cellularity of phenotypic subsets that may impair immune function and contribute to airway inflammation induced by DE exposure in rats.",
+            "title": "Effects of inhaled tier-2 diesel engine exhaust on immunotoxicity in a rat model:  A hazard identification study. Part III. Immunotoxicology",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/kkvj-587h/application/x-zip-compressed",
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
+            "landingPage": "https://data.cdc.gov/d/53mp-bpbv",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "issued": "2022-06-15",
+            "@type": "dcat:Dataset",
+            "temporal": "2019",
+            "modified": "2023-04-20",
+            "keyword": [
+                "chronic conditions",
+                "disability",
+                "e-cigarette use",
+                "opioid use",
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
+            "identifier": "https://data.cdc.gov/api/views/53mp-bpbv",
+            "description": "The Research and Development Survey (RANDS) is a series of cross-sectional \nsurveys from probability-sampled commercial survey panels which began in 2015. \nRANDS 3 was administered by the National Opinion Research Center (NORC) using the \nAmerispeak Panel in the spring of 2019 and contains existing questions from \nthe National Health Interview Survey (NHIS) as well as embedded probe questions \nand split-panel experiments for cognitive evaluations.",
+            "title": "NCHS Research and Development Survey (RANDS) Round 3 Restricted File",
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
+            "describedBy": "https://www.cdc.gov/nchs/rands/files/RANDS3_technical_documentation.pdf",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/wunw-h7a2",
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
+            "identifier": "08b59dc2-a89b-512a-bab9-e8f83e4b7848",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "Scorecard filters v2.11.16 (cmsdev)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.16/20241107/filters.csv",
+                    "description": "Scorecard filters v2.11.16 (cmsdev)",
+                    "@type": "dcat:Distribution",
+                    "title": "Scorecard filters v2.11.16 (cmsdev)"
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
+            "landingPage": "https://data.cdc.gov/d/qjxm-7fny",
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
+                "particulate matter",
+                "pm2.5"
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
+            "identifier": "https://data.cdc.gov/api/views/qjxm-7fny",
+            "description": "This dataset provides modeled predictions of PM2.5 levels from the EPA's Downscaler model. Data are at the census tract level for 2011-2015. These data are used by the CDC's National Environmental Public Health Tracking Network to generate air quality measures. Census tract-level datasets contain estimates of the mean predicted concentration and associated standard error. Please refer to the metadata attachment for more information.\n\nLearn more about outdoor air quality on the Tracking Network's website: https://ephtracking.cdc.gov/showAirLanding.action.\n\nBy using these data, you signify your agreement to comply with the following requirements:\n1. Use the data for statistical reporting and analysis only.\n2. Do not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals.\n3. Do not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov.\n4. Do not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating.\n5. Acknowledge, in all reports or presentations based on these data, the original source of the data and CDC.\n6. Suggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking.",
+            "title": "Daily Census Tract-Level PM2.5 Concentrations, 2011-2015",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qjxm-7fny/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qjxm-7fny/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qjxm-7fny/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qjxm-7fny/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/aco-realizing-equity-access-and-community-health/aco-realizing-equity-access-and-community-health-providers",
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/e0eba16f-ce0d-4037-96ce-2af70c718c98/data-viewer",
+            "description": "The Accountable Care Organization Realizing Equity, Access and Community Health (ACO REACH) Model Providers Public Use File (PUF) data details Participant Providers and Preferred Providers in the ACO REACH Model, formerly Global and Professional Direct Contracting (GPDC) Model. This dataset includes information on each providers capitation arrangement, Advanced Payment Option and elected waivers.",
+            "title": "ACO Realizing Equity, Access and Community Health Providers",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e0eba16f-ce0d-4037-96ce-2af70c718c98/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "ACO Realizing Equity, Access and Community Health Providers : 2021-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/PROVIDER_PUF.csv",
+                    "mediaType": "text/csv",
+                    "title": "ACO Realizing Equity, Access and Community Health Providers : 2021-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e235bb4b-84ea-456a-a64e-b7c1b8a98ea7/data",
+                    "mediaType": "text/html",
+                    "title": "ACO Realizing Equity, Access and Community Health Providers : 2021-12-31"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/aco-reach-provider-data-dictionary",
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
+            "landingPage": "https://data.cms.gov/quality-of-care/facility-level-minimum-data-set-frequency",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2024-08-01",
+            "temporal": "2023-10-01/2024-09-30",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-04",
+            "references": [
+                "https://data.cms.gov/resources/facility-level-minimum-data-set-frequency-methodology"
+            ],
+            "keyword": [
+                "hospitals & facilities",
+                "medicare",
+                "skilled nursing"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "NH Facility - CCSQ",
+                "hasEmail": "mailto:NursingHomeData@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/d086edc0-4953-4fb9-a663-b35526371add/data-viewer",
+            "description": "The Facility-Level Minimum Data Set (MDS) Frequency\u00a0dataset provides information for active nursing home residents on topics, such as race/ethnicity, age, or marital status; discharge dispositions; hearing, speech, and vision; cognitive patterns; mood; functional abilities and goals; bladder and bowel; active diagnoses; health conditions; swallowing/nutritional status; oral/dental status; skin conditions; medications; special treatments, procedures, and programs; restraints and alarms; and participation in assessment and goal setting.\n\n\u00a0\n\nNote: The MDS dataset contains more records than most spreadsheet programs can handle. The use of a database or statistical software is generally required. The dataset can be filtered to a more manageable size for use in a spreadsheet program by clicking on the \u201cView Data\u201d button. Additional filter information can be found in the methodology, if needed.",
+            "title": "Facility-Level Minimum Data Set Frequency",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d086edc0-4953-4fb9-a663-b35526371add/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Facility-Level Minimum Data Set Frequency : 2024-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/05c9444c-b7ac-4bcd-8efa-e266222c5670/MDS_Facility_Level_2024_Q3.csv",
+                    "mediaType": "text/csv",
+                    "title": "Facility-Level Minimum Data Set Frequency : 2024-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/184a3e9c-6757-4cb1-ba98-4fd43803c557/data",
+                    "mediaType": "text/html",
+                    "title": "Facility-Level Minimum Data Set Frequency : 2024-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/16d52e37-246c-4c49-aaf3-ed5aae90c364/MDS_Facility_Level_2024_Q2.csv",
+                    "mediaType": "text/csv",
+                    "title": "Facility-Level Minimum Data Set Frequency : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/450425c3-5b81-454e-88b7-9902739ecb12/data",
+                    "mediaType": "text/html",
+                    "title": "Facility-Level Minimum Data Set Frequency : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/3a7ea82a-8869-4760-9123-7d536cdce951/MDS_Facility_Level_2024_Q1_Final.csv",
+                    "mediaType": "text/csv",
+                    "title": "Facility-Level Minimum Data Set Frequency : 2024-01-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f6a42f70-af9a-497f-91eb-ddc9dd89c6a9/data",
+                    "mediaType": "text/html",
+                    "title": "Facility-Level Minimum Data Set Frequency : 2024-01-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/97a6f62e-eb7c-4921-90f3-09321c683379/MDS_Facility_Level_2023_Q4_Final.csv",
+                    "mediaType": "text/csv",
+                    "title": "Facility-Level Minimum Data Set Frequency : 2023-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/460c94f3-7f7f-4a3e-bd25-33ad8343a66e/data",
+                    "mediaType": "text/html",
+                    "title": "Facility-Level Minimum Data Set Frequency : 2023-12-01"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/facility-level-minimum-data-set-frequency-data-dictionary",
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
+            "landingPage": "https://healthdata.gov/d/wxsh-768y",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2014-11-07",
+            "temporal": "2019-01-01T00:00:00+00:00/2020-01-01T00:00:00+00:00",
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
+            "identifier": "76a1984a-6d69-5e4d-86c8-65eb31f0506d",
+            "description": "National Average Drug Acquisition Cost (NADAC) weekly reference data for the calendar year.",
+            "title": "NADAC (National Average Drug Acquisition Cost) 2019",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/nadac-national-average-drug-acquisition-cost.a4y5-998d.76a1984a-6d69-5e4d-86c8-65eb31f0506d.csv",
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
+            "landingPage": "https://data.cdc.gov/d/ex65-qa8z",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-01-14",
+            "@type": "dcat:Dataset",
+            "modified": "2022-02-11",
+            "keyword": [
+                "2022",
+                "hemolytic uremic syndrome post-diarrheal",
+                "hepatitis (viral acute) type a",
+                "hepatitis (viral acute) type b",
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
+            "identifier": "https://data.cdc.gov/api/views/ex65-qa8z",
+            "description": "NNDSS - TABLE 1P. Hemolytic uremic syndrome post-diarrheal to Hepatitis B, acute - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
+            "title": "NNDSS - TABLE 1P. Hemolytic uremic syndrome post-diarrheal to Hepatitis B, acute",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ex65-qa8z/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ex65-qa8z/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ex65-qa8z/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ex65-qa8z/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/statesystem/index.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-07-19",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-14",
+            "keyword": [
+                "ecigarette",
+                "legislation",
+                "osh",
+                "policy",
+                "smokefree indoor air",
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
+            "identifier": "https://data.cdc.gov/api/views/i8t6-whzd",
+            "description": "1995-2024. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System. E-Cigarette Legislation \u2013 Smokefree Indoor Air. The STATE System houses current and historical state-level legislative data on tobacco use prevention and control policies. Data are reported on a quarterly basis. Data include information related to state legislation on smokefree indoor air that apply to use of e-cigarettes in private worksites, restaurants, and bars.",
+            "title": "CDC STATE System E-Cigarette Legislation - Smokefree Indoor Air Summary",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/i8t6-whzd/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/i8t6-whzd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/i8t6-whzd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/i8t6-whzd/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-Tobacco-Legislation-Smokefree-Ind/2snk-eav4",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "theme": [
+                "Legislation"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/xy5u-nzbq",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-12-03",
+            "@type": "dcat:Dataset",
+            "modified": "2024-12-03",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Health Effects Laboratory Division (HELD)",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/xy5u-nzbq",
+            "description": "Workers that regularly use vibrating hand tools as part of their job are at risk of developing hand-arm vibration syndrome (HAVS).  HAVS is characterized by cold-induced vasospasms that result in blanching of the fingers and hands, loss of sensation, pain, and reductions in manual dexterity, all of which can affect a worker\u2019s ability to perform their job and their quality of life.  Vibration exposure significantly contributes to the development of these symptoms by increasing the stress and strain within exposed tissues, which in turn can affect functioning of blood vessels, nerves and sensory receptors in those tissues.",
+            "title": "Applied pressure alters circulating hormone levels and biomarkers of peripheral vascular, sensorineural dysfunction",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/xy5u-nzbq/application/x-zip-compressed",
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
+            "landingPage": "https://healthdata.gov/d/wyqi-qmra",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-06-29",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-11",
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
+            "identifier": "076d0bf4-50f5-52f4-b142-f49d558e1bcd",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "Scorecard filters v2.11.9 (impl)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.9/20241107/filters.csv",
+                    "description": "Scorecard filters v2.11.9 (impl)",
+                    "@type": "dcat:Distribution",
+                    "title": "Scorecard filters v2.11.9 (impl)"
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
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-household-survey-drug-abuse-nhsda-1999",
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
+                "mental health",
+                "mental health services",
+                "methamphetamine",
+                "prescriptions drugs",
+                "smoking",
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
+            "identifier": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1999-nid13544",
+            "description": "<p>The National Household Survey on Drug Abuse (NHSDA) series<br />\nmeasures the prevalence and correlates of drug use in the United<br />\nStates. The surveys are designed to provide quarterly, as well as<br />\nannual, estimates. Information is provided on the use of illicit<br />\ndrugs, alcohol, and tobacco among members of United States households<br />\naged 12 and older. Questions include age at first use as well as<br />\nlifetime, annual, and past-month usage for the following drug classes:<br />\nmarijuana, cocaine (and crack), hallucinogens, heroin, inhalants,<br />\nalcohol, tobacco, and nonmedical use of prescription drugs, including<br />\npain relievers, tranquilizers, stimulants, and sedatives. The survey<br />\ncovers substance abuse treatment history and perceived need for<br />\ntreatment, and includes questions from the Diagnostic and Statistical<br />\nManual (DSM) of Mental Disorders that allow diagnostic criteria to be<br />\napplied. Respondents are also asked about personal and family income<br />\nsources and amounts, health care access and coverage, illegal<br />\nactivities and arrest record, problems resulting from the use of<br />\ndrugs, and needle-sharing. Questions introduced in previous NHSDA<br />\nadministrations were retained in the 1999 survey, including questions<br />\nasked only of respondents aged 12 to 17. These \"youth experiences\"<br />\nitems covered a variety of topics, such as neighborhood environment,<br />\nillegal activities, gang involvement, drug use by friends, social<br />\nsupport, extracurricular activities, exposure to substance abuse<br />\nprevention and education programs, and perceived adult attitudes<br />\ntoward drug use and activities such as school work. Also retained were<br />\nquestions on mental health and access to care, perceived risk of using<br />\ndrugs, perceived availability of drugs, driving behavior and personal<br />\nbehavior, and cigar smoking. Questions on the tobacco brand used most<br />\noften were introduced with the 1999 survey. Demographic data include<br />\ngender, race, age, ethnicity, marital status, educational level, job<br />\nstatus, veteran status, and current household composition.This study has 1 Data Set.</p>",
+            "title": "National Household Survey on Drug Abuse (NHSDA-1999)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1999-nid13544",
+                    "description": "National Household Survey on Drug Abuse (NHSDA-1999) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/national-household-survey-drug-abuse-nhsda-1999-nid13544"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/epap-ayij",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-10-16",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-16",
+            "keyword": [
+                "care cascade",
+                "cascade of care",
+                "latent tuberculosis infection (ltbi)",
+                "tuberculosis (tb)"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Tuberculosis Epidemiologic Studies Consortium",
+                "hasEmail": "mailto:tbesc3@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/epap-ayij",
+            "description": "This study focused on describing and quantifying the steps in the tuberculosis (TB) prevention cascade of care within health department clinics. This included better understanding the proportions of patients with latent TB infection who are identified, offered treatment, accept treatment, and complete treatment.",
+            "title": "Tuberculosis Epidemiologic Studies Consortium (TBESC)-II Part B: Strengthening Public Health Surveillance for Latent Tuberculosis Infection",
+            "programCode": [
+                "009:027"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/epap-ayij/application/x-zip-compressed",
+                    "mediaType": "application/x-zip-compressed"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "theme": [
+                "National Center for HIV",
+                "Viral Hepatitis",
+                "STD",
+                "and TB Prevention"
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
+            "modified": "2022-03-29",
+            "references": [
+                "https://www.cdc.gov/nchs/data/vsus/vsus_1950_1.pdf",
+                "https://www.cdc.gov/nchs/data/misc/usvss.pdf",
+                "https://www.cdc.gov/nchs/data/vsus/nat67_1.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr66/nvsr66_01.pdf",
+                "https://www.cdc.gov/nvsr/nvsr67/nvsr67_01.pdf",
+                "https://www.cdc.gov/nchs/data/nvsr/nvsr68/nvsr68_13.pdf"
+            ],
+            "keyword": [
+                "age",
+                "birth rate",
+                "ethnicity",
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
+            "identifier": "https://data.cdc.gov/api/views/e8kx-wbww",
+            "description": "This dataset includes teen birth rates for females by age group, race, and Hispanic origin in the United States since 1960. \n\nData availability varies by race and ethnicity groups. All birth data by race before 1980 are based on race of the child. Since 1980, birth data by race are based on race of the mother. For race, data are available for Black and White births since 1960, and for American Indians/Alaska Native and Asian/Pacific Islander births since 1980. Data on Hispanic origin are available since 1989. Teen birth rates for specific racial and ethnic categories are also available since 1989. From 2003 through 2015, the birth data by race were based on the \u201cbridged\u201d race categories (5). Starting in 2016, the race categories for reporting birth data changed; the new race and Hispanic origin categories are: Non-Hispanic, Single Race White; Non-Hispanic, Single Race Black; Non-Hispanic, Single Race American Indian/Alaska Native; Non-Hispanic, Single Race Asian; and, Non-Hispanic, Single Race Native Hawaiian/Pacific Islander (5,6). Birth data by the prior, \u201cbridged\u201d race (and Hispanic origin) categories are included through 2018 for comparison.\n\nNational data on births by Hispanic origin exclude data for Louisiana, New Hampshire, and Oklahoma in 1989; New Hampshire and Oklahoma in 1990; and New Hampshire in 1991 and 1992. Birth and fertility rates for the Central and South American population includes other and unknown Hispanic. Information on reporting Hispanic origin is detailed in the Technical Appendix for the 1999 public-use natality data file (see ftp://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/DVS/natality/Nat1999doc.pdf).",
+            "title": "NCHS - Teen Birth Rates for Females by Age Group, Race, and Hispanic Origin: United States",
+            "isPartOf": "NCHS - Teen Birth Rates for Females by Age Group, Race, and Hispanic Origin: United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/e8kx-wbww/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/e8kx-wbww/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/e8kx-wbww/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/e8kx-wbww/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States",
+            "describedBy": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "license": "https://www.usa.gov/government-works",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/bve7-bjy2",
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
+            "identifier": "https://data.cdc.gov/api/views/bve7-bjy2",
+            "description": "NNDSS - TABLE 1Z. Pertussis to Poliomyelitis, paralytic - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1Z. Pertussis to Poliomyelitis, paralytic",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bve7-bjy2/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bve7-bjy2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bve7-bjy2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bve7-bjy2/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/n8mc-b4w4",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-03-22",
+            "@type": "dcat:Dataset",
+            "temporal": "2020-01-01/2024-07-05",
+            "modified": "2025-01-13",
+            "references": [
+                "https://github.com/CDCgov/covid_case_privacy_review/blob/master/analysis/public%2019%20utility%20summary.pdf"
+            ],
+            "keyword": [
+                "cases",
+                "coronavirus",
+                "county",
+                "covid19",
+                "covid-19",
+                "microdata",
+                "state",
+                "surveillance"
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
+            "identifier": "https://data.cdc.gov/api/views/n8mc-b4w4",
+            "description": "<b>Note:</b>\nReporting of new COVID-19 Case Surveillance data will be discontinued July 1, 2024, to align with the process of removing SARS-CoV-2 infections (COVID-19 cases) from the list of nationally notifiable diseases. Although these data will continue to be publicly available, the dataset will no longer be updated.\n\nAuthorizations to collect certain public health data expired at the end of the U.S. public health emergency declaration on May 11, 2023. The following jurisdictions discontinued COVID-19 case notifications to CDC: Iowa (11/8/21), Kansas (5/12/23), Kentucky (1/1/24), Louisiana (10/31/23), New Hampshire (5/23/23), and Oklahoma (5/2/23). Please note that these jurisdictions will not routinely send new case data after the dates indicated. As of 7/13/23, case notifications from Oregon will only include pediatric cases resulting in death.\n\n\nThis case surveillance public use dataset has 19 elements for all COVID-19 cases shared with CDC and includes demographics, geography (county and state of residence), any exposure history, disease severity indicators and outcomes, and presence of any underlying medical conditions and risk behaviors.\n\nCurrently, CDC provides the public with three versions of COVID-19 case surveillance line-listed data: this <a href=\"https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data-with-Ge/n8mc-b4w4\">19 data element dataset with geography</a>, a <a href=\"https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Public-Use-Data/vbim-akqf\">12 data element public use dataset</a>, and a <a href=\"https://data.cdc.gov/Case-Surveillance/COVID-19-Case-Surveillance-Restricted-Access-Detai/mbd7-r32t\">33 data element restricted access dataset</a>.\n\nThe following apply to the public use datasets and the restricted access dataset:\n<ul><li>Data elements can be found on the COVID-19 case report form located at www.cdc.gov/coronavirus/2019-ncov/downloads/pui-form.pdf.</li><li>Data are considered provisional by CDC and are subject to change until the data are reconciled and verified with the state and territorial data providers.</li><li>Some data are suppressed to protect individual privacy.</li><li>Datasets will include all cases with the earliest date available in each record (date received by CDC or date related to illness/specimen collection) at least 14 days prior to the creation of the current datasets. This 14-day lag allows case reporting to be stabilized and ensure that time-dependent outcome data are accurately captured.</li><li>Datasets are updated monthly.</li><li>Datasets are created using CDC\u2019s <a href=\"https://www.cdc.gov/grants/additional-requirements/ar-25.html\">Policy on Public Health Research and Nonresearch Data Management and Access</a> and include protections designed to protect individual privacy.</li><li>For more information about data collection and reporting, please see\u202f<a href=\"https://www.cdc.gov/coronavirus/2019-ncov/covid-data/about-us-cases-deaths.html\">https://www.cdc.gov/coronavirus/2019-ncov/covid-data/about-us-cases-deaths.html.</a></li><li>For more information about the COVID-19 case surveillance data, please see <a href=\"https://www.cdc.gov/coronavirus/2019-ncov/covid-data/faq-surveillance.html\"> https://www.cdc.gov/coronavirus/2019-ncov/covid-data/faq-surveillance.html</a><br></li></ul>\n\n<b>Overview</b>\n\nThe COVID-19 case surveillance database includes individual-level data reported to U.S. states and autonomous reporting entities, including New York City and the District of Columbia (D.C.), as well as U.S. territories and affiliates. On April 5, 2020, COVID-19 was added to the <a href=\"https://ndc.services.cdc.gov/search-results-year/\">Nationally Notifiable Condition List</a> and classified as \u201cimmediately notifiable, urgent (within 24 hours)\u201d by a Council of State and Territorial Epidemiologists (CSTE) Interim Position Statement (<a href=\"https://cdn.ymaws.com/www.cste.org/resource/resmgr/ps/positionstatement2020/Interim-20-ID-01_COVID",
+            "title": "COVID-19 Case Surveillance Public Use Data with Geography",
+            "describedByType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/n8mc-b4w4/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/n8mc-b4w4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/n8mc-b4w4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/n8mc-b4w4/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "US",
+            "describedBy": "https://data.cdc.gov/api/views/n8mc-b4w4/files/f24e6a39-6419-4958-81d2-a22da947f8fc?download=true&filename=data_dictionary_covid_cases_public_geo.xlsx",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Monthly",
+            "theme": [
+                "Case Surveillance"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/3nrv-cydv",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2023-03-03",
+            "@type": "dcat:Dataset",
+            "modified": "2024-09-03",
+            "keyword": [
+                "mesh",
+                "population groups"
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/3nrv-cydv",
+            "description": "Working with partners across NIH, led by NIMHD and the NLM OBSSR-Behavioral Ontology Working Group, MeSH on November 29, 2022 added Federally recognized American Indian and Alaskan Native (AI/AN) tribal names and ethnic/ethnolinguistic minority terms as newly created type 5 SCR designated as \u201cPopulation Groups\u201d. These minority names (1,700+ terms) were mapped and reviewed by subject matter experts and scientists within NIH and from outside including Network of the National Library of Medicine members.\n\nStructure: All type 5 SCRs have common fields\n1.\tCC=5 Population Group \n2.\tST=T098 Population Groups\n3.\tHM= At least one HM is to an MH under Population Groups [M01.686]\n4.\tTH= NIMHD(2023)",
+            "title": "MeSH Population Groups (Type 5 SCR)",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/3nrv-cydv/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/3nrv-cydv/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/3nrv-cydv/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/3nrv-cydv/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/x4ie-279c",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-08-09",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-16",
+            "keyword": [
+                "individual",
+                "individual market dental",
+                "py2023",
+                "qhp landscape instructions",
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
+            "identifier": "492db9fe-b288-4c5b-a75b-72c642fbc4bf",
+            "description": "The Dental Individual Market file of the QHP Landscape Files contains information on certified dental plans offered through an Exchange to consumers in the individual market. These plans are also known as Stand-alone Dental Plans (SADPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
+            "title": "QHP Landscape Instructions PY2023 Individual Dental",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2023/den-ind-lndscp-in.pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/washington-dc-metropolitan-area-drug-study-homeless-and-transient-population-dc-madst-1991",
+            "issued": "2016-05-23",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "arrests",
+                "cocaine",
+                "crack cocaine",
+                "demographic characteristics",
+                "drug abuse",
+                "drug related crimes",
+                "drugs",
+                "drug use",
+                "employment",
+                "hallucinogens",
+                "health insurance",
+                "heroin",
+                "homeless persons",
+                "inhalants",
+                "living arrangements",
+                "marijuana",
+                "mental health",
+                "mental health treatment",
+                "methamphetamines",
+                "physical health",
+                "population characteristics",
+                "pregnancy",
+                "prescription drugs",
+                "sedatives",
+                "smoking",
+                "stimulants",
+                "substance abuse treatment",
+                "urban population"
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
+            "identifier": "https://datafiles.samhsa.gov/study/washington-dc-metropolitan-area-drug-study-homeless-and-transient-population-dc-madst-1991",
+            "description": "<p>The DC Metropolitan Area Drug Study (DC<em>MADS) was<br />\nconducted in 1991, and included special analyses of homeless and<br />\ntransient populations and of women delivering live births in the DC<br />\nhospitals. DC</em>MADS was undertaken to assess the full extent of the<br />\ndrug problem in one metropolitan area. The study was comprised of 16<br />\nseparate studies that focused on different sub-groups, many of which<br />\nare typically not included or are underrepresented in household<br />\nsurveys. The Homeless and Transient Population<br />\nstudy examines the prevalence of illicit drug, alcohol, and tobacco<br />\nuse among members of the homeless and transient population aged 12 and<br />\nolder in the Washington, DC, Metropolitan Statistical Area (DC<br />\nMSA). The sample frame included respondents from shelters, soup<br />\nkitchens and food banks, major cluster encampments, and literally<br />\nhomeless people. Data from the questionnaires include history of<br />\nhomelessness, living arrangements and population movement, tobacco,<br />\ndrug, and alcohol use, consequences of use, treatment history, illegal<br />\nbehavior and arrest, emergency room treatment and hospital stays,<br />\nphysical and mental health, pregnancy, insurance, employment and<br />\nfinances, and demographics. Drug specific data include age at first<br />\nuse, route of administration, needle use, withdrawal symptoms,<br />\npolysubstance use, and perceived risk.This study has 1 Data Set.</p>",
+            "title": "Washington  DC  Metropolitan Area Drug Study Homeless and Transient Population (DC-MADST-1991)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/washington-dc-metropolitan-area-drug-study-homeless-and-transient-population-dc-madst-1991",
+                    "description": "Washington  DC  Metropolitan Area Drug Study Homeless and Transient Population (DC-MADST-1991) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/washington-dc-metropolitan-area-drug-study-homeless-and-transient-population-dc-madst-1991"
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
+                "mesh",
+                "mesh 2023 update"
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/aqtu-bnvm",
+            "description": "This dataset includes all newly added MeSH Main Headings for 2023. Headings play a central role in MeSH vocabulary as a unit of Indexing and retrieval. With the exception of Class 3 Descriptors, all descriptors are organized into a numbered tree structure or hierarchy that allows users to browse in a orderly fashion from broader to narrower topics.  Scope Notes provide a concise summary describing the meaning and scope of the MeSH Descriptor.",
+            "title": "MeSH 2023 - New Headings with Scope Notes",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/aqtu-bnvm/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/aqtu-bnvm/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/aqtu-bnvm/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/aqtu-bnvm/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/nchs/ahcd/datasets_documentation_related.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "https://www.cdc.gov/nchs/ahcd/datasets_documentation_related.htm",
+            "issued": "2023-06-14",
+            "@type": "dcat:Dataset",
+            "temporal": "1992-2022",
+            "modified": "2024-07-24",
+            "references": [
+                "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Dataset_Documentation/NHAMCS/",
+                "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NHAMCS/"
+            ],
+            "keyword": [
+                "cause of injury",
+                "diagnosis",
+                "ed",
+                "emergency department",
+                "emergency-department",
+                "emergency department visits",
+                "injury",
+                "medication therapy",
+                "patient care",
+                "patient characteristics",
+                "prescription drugs",
+                "reason for visit"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Center for Health Statistics",
+                "hasEmail": "mailto:cdcinfo.cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/tqpr-vcrm",
+            "description": "The National Hospital Ambulatory Medical Care Survey (NHAMCS) has been fielded annually since 1992 to collect data on the utilization and provision of ambulatory care services in hospital emergency and outpatient departments. Data collection from hospital-based ambulatory surgery centers began in 2009. And between 2010 and 2012 NHAMCS gathered data on visits to freestanding ambulatory surgery centers. In 2018, the survey began focusing on just the ambulatory visits made to emergency departments.\nEach emergency department is randomly assigned to a 4-week reporting period. During this period, data for a systematic random sample of visits are recorded by Census interviewers using a computerized Patient Record Form. Data are obtained on patient characteristics such as age, sex, race, and ethnicity, and visit characteristics such as patient\u2019s reason for visit, provider\u2019s diagnosis, services ordered or provided, and treatments, including medication therapy. In addition, data about the facility are collected as part of a survey induction interview.",
+            "title": "National Hospital Ambulatory Medical Care Survey, Public-use data 1992-2022",
+            "isPartOf": "https://www.cdc.gov/nchs/ahcd/datasets_documentation_related.htm",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://ftp.cdc.gov/pub/Health_Statistics/NCHS/Datasets/NHAMCS/",
+                    "description": "Links to 1992-2022 .ZIP and .EXE data files. Data documentation links also inlcuded.",
+                    "@type": "dcat:Distribution",
+                    "title": "NHAMCS 1992-2022"
+                }
+            ],
+            "spatial": "United States",
+            "describedBy": "For the survey, findings are based on a national sample of visits to emergency departments (EDs) in noninstitutional general and short-stay hospitals, exclusive of Federal, military, and Veterans Administration hospitals, located in the 50 States and the District of Columbia. The sampling frame for the 2021 NHAMCS was constructed from IQVIA\u2019s database. A three-stage probability sampling design is used. The first stage consists of a sample of geographically defined areas also known as Primary Sampling Units (PSU). In the second stage, is of hospitals within those PSU and all emergency service areas within the emergency department are selected. Emergency service areas (ESAs) are not sampled at this stage. In the third stage ESAs are sampled.",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Dataset will no longer be updated.",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/x5cu-d9pq",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2022-03-12",
+            "@type": "dcat:Dataset",
+            "modified": "2022-03-10",
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
+            "identifier": "207d084f-0d9d-4cab-b210-ba813d63b572",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2022-02-28 to 2022-03-06",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rpt-drugs-mar-02-28-2022-03-06-2022.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "restricted public",
+            "landingPage": "https://www.hcup-us.ahrq.gov",
+            "bureauCode": [
+                "009:33"
+            ],
+            "issued": "2022-06-07",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "agency-for-healthcare-research-and-quality-department-of-health-human-services",
+                "ambulatory surgery",
+                "hcup"
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
+            "identifier": "https://healthdata.gov/api/views/x5sw-xtqj",
+            "description": "The largest all-payer ambulatory surgery database in the United States, the Healthcare Cost and Utilization Project (HCUP) Nationwide Ambulatory Surgery Sample (NASS) produces national estimates of major ambulatory surgery encounters in hospital-owned facilities. Major ambulatory surgeries are defined as selected major therapeutic procedures that require the use of an operating room, penetrate or break the skin, and involve regional anesthesia, general anesthesia, or sedation to control pain (i.e., surgeries flagged as \"narrow\" in the HCUP Surgery Flag Software).  Unweighted, the NASS contains approximately 9.0 million ambulatory surgery encounters each year and approximately 11.8 million ambulatory surgery procedures. Weighted, it estimates approximately 11.9 million ambulatory surgery encounters and 15.7 million ambulatory surgery procedures.\n\nSampled from the HCUP State Ambulatory Surgery and Services Databases (SASD) and State Emergency Department Databases (SEDD) in order to capture both planned and emergent major ambulatory surgeries, the NASS can be used to examine selected ambulatory surgery utilization patterns.  Developed through a Federal-State-Industry partnership sponsored by the Agency for Healthcare Research and Quality, HCUP data inform decision making at the national, State, and community levels.\n\nThe NASS contains clinical and resource-use information that is included in a typical hospital-owned facility record, including patient characteristics, clinical diagnostic and surgical procedure codes, disposition of patients, total charges, facility characteristics, and expected source of payment, regardless of payer, including patients covered by Medicaid, private insurance, and the uninsured. The NASS excludes data elements that could directly or indirectly identify individuals, hospitals, or states.  The NASS is limited to encounters with at least one in-scope major ambulatory surgery on the record, performed at hospital-owned facilities. Procedures intended primarily for diagnostic purposes are not considered in-scope.\n\nRestricted access data files are available with a data use agreement and brief online security training.",
+            "title": "HCUP Nationwide Ambulatory Surgery Sample (NASS) Database \u2013 Restricted Access",
+            "programCode": [
+                "009:074"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.hcup-us.ahrq.gov/db/nation/nass/nassdbdocumentation.jsp",
+                    "mediaType": "text/html",
+                    "title": "HCUP Nationwide Ambulatory Surgery Sample (NASS) Database \u2013 Restricted Access"
+                }
+            ],
+            "describedBy": "https://www.hcup-us.ahrq.gov/db/nation/nass/nassdbdocumentation.jsp",
+            "license": "https://www.distributor.hcup-us.ahrq.gov/Home.aspx"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/x6kx-6hpr",
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
+            "identifier": "c1c4b0cf-c957-4b00-bcf4-c0905045a5b3",
+            "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of COVID-19 testing services provided to Medicaid and CHIP beneficiaries, by state. \r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating COVID-19 testing services measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Procedure Codes - OT Professional, Claims Volume - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+            "title": "COVID Testing  and Testing-Related  Services Provided to Medicaid and CHIP Beneficiaries",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/COVID-Testing-and-Testing-Related-Services-Provided-to-MedicaidCHIP-Beneficiaries.csv",
+                    "description": "This data set includes monthly counts and rates (per 1,000 beneficiaries) of COVID-19 testing services provided to Medicaid and CHIP beneficiaries, by state. \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some states have serious data quality issues for one or more months, making the data unusable for calculating COVID-19 testing services measures. To assess data quality, analysts adapted measures featured in the DQ Atlas. Data for a state and month are considered unusable if at least one of the following topics meets the DQ Atlas threshold for unusable: Total Medicaid and CHIP Enrollment, Procedure Codes - OT Professional, Claims Volume - OT. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods. Cells with a value of \u201cDQ\u201d indicate that data were suppressed due to unusable data. \n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "@type": "dcat:Distribution",
+                    "title": "COVID Testing  and Testing-Related  Services Provided to Medicaid and CHIP Beneficiaries"
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
+            "landingPage": "https://healthdata.gov/d/x6me-tvjr",
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
+            "identifier": "4acd783c-272d-5db4-b86d-361a297722de",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "CoreSEt pillar v2.10.22 (coreset-impl)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.22/20241029/pillar.csv",
+                    "description": "CoreSEt pillar v2.10.22 (coreset-impl)",
+                    "@type": "dcat:Distribution",
+                    "title": "CoreSEt pillar v2.10.22 (coreset-impl)"
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
+            "landingPage": "https://www.cdc.gov/flu/fluvaxview/dashboard/vaccination-dashboard.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-09-30",
+            "@type": "dcat:Dataset",
+            "temporal": "2019-2020, 2020-2021, 2021-2022, 2022-2023",
+            "modified": "2024-05-03",
+            "references": [
+                "Vaccine Safety Datalink"
+            ],
+            "keyword": [
+                "children",
+                "flu",
+                "influenza",
+                "nis",
+                "nis-flu",
+                "vaccine coverage"
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
+            "identifier": "https://data.cdc.gov/api/views/fz77-au2z",
+            "description": "Cumulative Influenza Vaccination Coverage, by Flu Season and Race/Ethnicity, Pregnant Persons 18-49 years\n\t\n\u2022  These monthly flu vaccination coverage estimates for pregnant persons are based on electronic health record (EHR) data from the Vaccine Safety Datalink (VSD), a collaboration between CDC\u2019s Immunization Safety Office and nine integrated health care organizations.\u00a7 This system has been used annually to estimate vaccination coverage among pregnant persons. COVID-19 vaccination coverage for pregnant persons is available here. \n\n\u2022\tFigure 3A. Monthly Cumulative Influenza Vaccination Coverage*, by Flu Season and Race/Ethnicity, Pregnant Persons 18-49 years, United States, Data Source: Vaccine Safety Datalink \n\n\u2022\tFigure 3B. Cumulative Influenza Vaccination Coverage*, by Month, Flu Season, and Race/Ethnicity, Pregnant Persons 18-49 years, United States, Data Source: Vaccine Safety Datalink \n\n\u2022\tFor any month\u2019s coverage estimate, the denominator is the number of persons with a pregnancy during the current flu season (defined as August through March) beginning before or during the specified month. The numerator is the subset of the denominator who have received flu vaccination prior to, during, or after pregnancy. The denominator increases as more persons are identified as pregnant or having been pregnant during the flu season. Cumulative vaccination coverage for one month may be lower than cumulative coverage for a previous month due to addition to the denominator of persons who are less likely to have received vaccination.",
+            "title": "Cumulative Influenza Vaccination Coverage, by Flu Season and Race/Ethnicity, Pregnant Persons 18-49 years",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fz77-au2z/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fz77-au2z/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fz77-au2z/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fz77-au2z/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/x7c4-svex",
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
+            "identifier": "b0ba435a-a21a-5283-a470-7051321da5b1",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "implAuto_states",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/states.csv",
+                    "description": "{\"dataset\": \"states\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "@type": "dcat:Distribution",
+                    "title": "states csv file"
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
+            "landingPage": "https://healthdata.gov/dataset/drug-abuse-warning-network-dawn-2004",
+            "issued": "2016-05-23",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
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
+            "identifier": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2004-nid13613",
+            "description": "<p>The Drug Abuse Warning Network (DAWN) is a nationally representative public health surveillance system that has monitored drug related emergency department (ED) visits to hospitals since the early 1970s. First administered by the Drug Enforcement Administration (DEA) and the National Institute on Drug Abuse (NIDA), the responsibility for DAWN now rests with the Substance Abuse and Mental Health Services Administration's (SAMHSA) Center for Behavioral Health Statistics and Quality (CBHSQ). Over the years, the exact survey methodology has been adjusted to improve the quality, reliability, and generalizability of the information produced by DAWN. The current approach was first fully implemented in the 2004 data collection year.<br />\nDAWN relies on a longitudinal probability sample of hospitals located throughout the United States. To be eligible for selection into the DAWN sample, a hospital must be a non-Federal, short-stay, general surgical and medical hospital located in the United States, with at least one 24-hour ED. DAWN cases are identified by the systematic review of ED medical records in participating hospitals. The unit of analysis is any ED visit involving recent drug use. DAWN captures both ED visits that are directly caused by drugs and those in which drugs are a contributing factor but not the direct cause of the ED visit. The reason a patient used a drug is not part of the criteria for considering a visit to be drug related. Therefore, all types of drug-related events are included: drug misuse or abuse, accidental drug ingestion, drug-related suicide attempts, malicious drug poisonings, and adverse reactions. DAWN does not report medications that are unrelated to the visit.<br />\nThe DAWN public-use dataset provides information for all types of drugs, including illegal drugs, prescription drugs, over-the-counter medications, dietary supplements, anesthetic gases, substances that have psychoactive effects when inhaled, alcohol when used in combination with other drugs (all ages), and alcohol alone (only for patients aged 20 or younger). Public-use dataset variables describe and categorize up to 16 drugs contributing to the ED visit, including toxicology confirmation and route of administration. Administrative variables specify the type of case, case disposition, categorized episode time of day, and quarter of year.  Metropolitan area is included for represented metropolitan areas. Created variables include the number of unique drugs reported and case-level indicators for alcohol, non-alcohol illicit substances, any pharmaceutical, non-medical use of pharmaceuticals, and all misuse and abuse of drugs. Demographic items include age category, sex, and race/ethnicity. Complex sample design and weighting variables are included to calculate various estimates of drug-related ED visits for the Nation as a whole, as well as for specific metropolitan areas, from the ED visits classified as DAWN cases in the selected hospitals.This study has 1 Data Set.</p>",
+            "title": "Drug Abuse Warning Network (DAWN-2004)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2004-nid13613",
+                    "description": "Drug Abuse Warning Network (DAWN-2004) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/drug-abuse-warning-network-dawn-2004-nid13613"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/dataset/corporate-integrity-agreement-cia-documents-0",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2012-05-30",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "department-of-health-human-services",
+                "health care providers"
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
+            "identifier": "41153824-e789-49e9-8543-5fa710bb94e3",
+            "description": "<p>OIG negotiates corporate integrity agreements (CIA) with health care providers and other entities as part of the settlement of Federal health care program investigations arising under a variety of civil false claims statutes. Providers or entities agree to the obligations, and in exchange, OIG agrees not to seek their exclusion from participation in Medicare, Medicaid, or other Federal health care programs.</p>",
+            "title": "Corporate Integrity Agreement (CIA) documents",
+            "programCode": [
+                "422:013"
+            ],
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "dataQuality": true
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/mscq-ew9n",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-15",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Division of Safety Research Protective Technology Branch; Health Effects Laboratory Division Physical Effects Research Branch",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/mscq-ew9n",
+            "description": "Type I industrial helmets have been widely used at construction sites and by manufacturers as \u201cgeneral purpose\u201d safety helmets. The performance of Type I industrial helmets for fall protection is not required to be tested in standardized tests. Chin straps and suspension system adjustment mechanisms are two important components of a typical industrial helmet, but the effects of proper use of them on the protective performance of Type I helmets have not been evaluated. The current study was designed to analyze the fall protection performance of Type I industrial helmets and to evaluate if the use of a chin strap and the suspension system tightness have any effect on protection performance. Head impact tests were performed by letting an instrumented manikin free fall backwards, from a standing posture, so that the manikin would make head-first contact with a solid surface of two different materials (concrete and plywood-covered). The results showed that all four tested helmet models demonstrated excellent performances for fall protection compared to the control group without wearing helmets. The fall protection performance of the advanced helmet models was substantially better than the basic helmet models. However, the effects of the use of chin straps and suspension system tightness on the helmets\u2019 fall protection performance were statistically not significant. The findings of our study provide information to help construction companies and manufacturers better manage the use of Type I helmets for fall protection, thereby reducing work-related traumatic brain injury risks.",
+            "title": "Evaluation of the fall protection of Type I industrial helmets",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/mscq-ew9n/application/x-zip-compressed",
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
+            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2002",
+            "bureauCode": [
+                "009:30"
+            ],
+            "issued": "2012-05-30",
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
+                "demographics",
+                "depression",
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
+                "pain relievers",
+                "population statistics",
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
+                "fn": "HealthData.gov",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Substance Abuse & Mental Health Services Administration"
+            },
+            "identifier": "c4e3821e-0f45-4202-8893-665f48c998ed",
+            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covers substance abuse treatment history and perceived need for treatment, and includes questions from the Diagnostic and Statistical Manual (DSM) of Mental Disorders that allow diagnostic criteria to be applied. The survey included questions concerning treatment for both substance abuse and mental health-related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing.</p>\n <ul><li>National Survey on Drug Use and Health, 2002 (ICPSR 3903): http://www.icpsr.umich.edu/icpsrweb/ICPSR/series/64/studies/3903?archive=ICPSR&sortBy=7</li><li>National Survey on Drug Use and Health, 2003 (ICPSR 4138): http://www.icpsr.umich.edu/icpsrweb/ICPSR/series/64/studies/4138?archive=ICPSR&sortBy=7</li></ul>",
+            "title": "National Survey on Drug Use and Health (NSDUH), 2002",
+            "programCode": [
+                "009:061"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://nsduhweb.rti.org/respweb/homepage.cfm",
+                    "mediaType": "text/html",
+                    "title": "HTML"
+                }
+            ],
+            "describedBy": "http://www.icpsr.umich.edu/icpsrweb/SAMHDA/ssvd/studies/03903/variables",
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/x7rp-ggcs",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-03-28",
+            "@type": "dcat:Dataset",
+            "modified": "2023-03-20",
+            "keyword": [
+                "chip",
+                "dq atlas",
+                "managed care",
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
+            "identifier": "c0bef49e-46ea-4b9d-9153-76b4078d58b7",
+            "description": "This data set presents annual enrollment counts of Medicaid and CHIP beneficiaries by managed care participation (comprehensive managed care, primary care case management, MLTSS, including PACE, behavioral health organizations, nonmedical prepaid health plans, medical-only prepaid health plans, and other). There are three metrics presented: (1) the number of beneficiaries ever enrolled in each managed care plan type over the year (duplicated count); (2) the number of beneficiaries enrolled in each managed care plan type as of an individual\u2019s last month of enrollment (duplicated count); and (3) average monthly enrollment in each managed care plan type.  \r\n\r\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some cells have a value of \u201cDS\u201d. Some states have serious data quality issues, making the data unusable for calculating these measures. To assess data quality, analysts used measures featured in the DQ Atlas. Data for a state and year are considered unusable or of high concern based on DQ Atlas thresholds for the topics Enrollment in CMC, Enrollment in PCCM Programs, and Enrollment in BHO Plans. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods.\r\n\r\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+            "title": "Managed Care Information for Medicaid and CHIP Beneficiaries by Year",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/ManagedCare-anul.csv",
+                    "description": "This data set presents annual enrollment counts of Medicaid and CHIP beneficiaries by managed care participation (comprehensive managed care, primary care case management, MLTSS, including PACE, behavioral health organizations, nonmedical prepaid health plans, medical-only prepaid health plans, and other). There are three metrics presented: (1) the number of beneficiaries ever enrolled in each managed care plan type over the year (duplicated count); (2) the number of beneficiaries enrolled in each managed care plan type as of an individual\u2019s last month of enrollment (duplicated count); and (3) average monthly enrollment in each managed care plan type.  \n\nThese metrics are based on data in the T-MSIS Analytic Files (TAF). Some cells have a value of \u201cDS\u201d. Some states have serious data quality issues, making the data unusable for calculating these measures. To assess data quality, analysts used measures featured in the DQ Atlas. Data for a state and year are considered unusable or of high concern based on DQ Atlas thresholds for the topics Enrollment in CMC, Enrollment in PCCM Programs, and Enrollment in BHO Plans. Please refer to the DQ Atlas at http://medicaid.gov/dq-atlas for more information about data quality assessment methods.\n\nSome cells have a value of \u201cDS\u201d. This indicates that data were suppressed for confidentiality reasons because the group included fewer than 11 beneficiaries.",
+                    "@type": "dcat:Distribution",
+                    "title": "Managed Care Information for Medicaid and CHIP Beneficiaries by Year"
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
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2012",
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
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2012-nid13600",
+            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, to update SAMHSA's Inventory of Behavioral Health Services (I-BHS), to analyze general treatment services trends, and to generate the online Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>, as well as the National Directory of Drug and Alcohol Abuse Treatment Programs.Data are collected on topics including facility operation, services offered (assessment, testing, transitional, ancillary, and pharmacotherapies), detoxification, primary focus (substance abuse, mental health, both, general health, and other), Opioid Treatment Programs and medications dispensed/prescribed, counseling and therapeutic approaches, standard operating procedures, special programs/groups offered, languages in which treatment is provided, type of treatment provided (hospital inpatient, residential, outpatient), number of clients (by service, total, and under age 18), number of beds, types of payment accepted, sliding fee scale, and facility accreditation and licensure/certification.This study has 1 Data Set.</p>",
+            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2012)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2012-nid13600",
+                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2012) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2012-nid13600"
+                }
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
+            "identifier": "https://data.cdc.gov/api/views/pj7z-f3xf",
+            "description": "2005. Centers for Disease Control and Prevention (CDC). PRAMS, the Pregnancy Risk Assessment Monitoring System, is a surveillance system collecting state-specific, population-based data on maternal attitudes and experiences before, during, and shortly after pregnancy. It is a collaborative project of the Centers for Disease Control and Prevention (CDC) and state health departments. PRAMS provides data for state health officials to use to improve the health of mothers and infants. PRAMS topics include abuse, alcohol use, contraception, breastfeeding, mental health, morbidity, obesity, preconception health, pregnancy history, prenatal-care, sleep behavior, smoke exposure, stress, tobacco use, WIC, Medicaid, infant health, and unintended pregnancy. Data will be updated annually as it becomes available.",
+            "title": "CDC PRAMStat Data for 2005",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pj7z-f3xf/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pj7z-f3xf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pj7z-f3xf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pj7z-f3xf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Maternal-Child-Health/CDC-PRAMStat-Data-for-2005/pj7z-f3xf",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Maternal & Child Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/efpc-rr7b",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-01-03",
+            "@type": "dcat:Dataset",
+            "modified": "2019-01-03",
+            "keyword": [
+                "2018",
+                "nedss",
+                "netss",
+                "nndss",
+                "primary and secondary",
+                "spotted fever rickettsiosis",
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
+            "identifier": "https://data.cdc.gov/api/views/efpc-rr7b",
+            "description": "NNDSS - Table II. Spotted fever rickettsiosis to Syphilis, primary and secondary - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html.\r\n \r\nFootnotes:\r\n\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum.\r\n \r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.",
+            "title": "NNDSS - Table II. Spotted fever rickettsiosis to Syphilis, primary and secondary",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/efpc-rr7b/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/efpc-rr7b/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/efpc-rr7b/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/efpc-rr7b/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "http://eupathdb.org/eupathdb/",
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
+                "fn": "Yao, Alison",
+                "hasEmail": "mailto:yaoal@niaid.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
+            "identifier": "ac3f7bb4-7d95-4da1-8b12-ccfb5f6b2da7",
+            "description": "<p>EuPathDB Bioinformatics Resource Center for Biodefense and Emerging/Re-emerging Infectious Diseases is a portal for accessing genomic-scale datasets associated with the eukaryotic pathogens.</p>",
+            "title": "Eukaryotic Pathogen Database Resources (EuPathDB)",
+            "programCode": [
+                "009:028"
+            ],
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "dataQuality": true
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/i54f-wv8z",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2015-02-05",
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
+            "identifier": "https://data.cdc.gov/api/views/i54f-wv8z",
+            "description": "Download the latest version of the Glossary and Methodology File",
+            "title": "Youth Risk Behavior Surveillance System (YRBSS) Glossary and Methodology",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/i54f-wv8z/application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Survey Data"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/chnh-3rdi",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-22",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-22",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Allergy and Clinical Immunology Branch (ACIB), Health Effects Laboratory Division (HELD)",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/chnh-3rdi",
+            "description": "Powered air purifying respirators (PAPRs) are a popular alternative to the use of filtering facepiece respirators by healthcare workers. Although PAPRs protect the wearer from aerosol particles, their ability to block infectious aerosol particles exhaled by the wearer from being released into the environment (called source control) is unclear.",
+            "title": "Efficacy of powered air-purifying respirators (PAPRs) for source control of simulated respiratory aerosols-dataset",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/chnh-3rdi/application/x-zip-compressed",
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
+            "landingPage": "https://data.cdc.gov/d/4ems-va7k",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-14",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Personal Protective Technology Laboratory, Research Branch",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/4ems-va7k",
+            "description": "Total inward leakage (TIL) is an estimate of the performance of a respirator, which is measured as the leakage of contaminants through the filter media and through the faceseal interface and exhalation valve of respiratory protective devices under laboratory conditions. Several test agents have been used to measure TIL in different countries. There is a lack of consensus on the most appropriate test method to measure TIL. The International Organization for Standardization (ISO) developed a standard (ISO, 2014) on the comparison of TIL measurement using sodium chloride (NaCl) and corn oil aerosols, and sulfur hexafluoride gas. A comparison of the TIL values between different methods will enable the selection of a relatively suitable method for measuring TIL. NIOSH\u2019s National Personal Protective Technology Laboratory (NPPTL) investigated the TIL values for respirators worn by test subjects exposed to NaCl and corn oil aerosols in two aerosol chambers side-by-side. Four air-purifying respirator categories, made",
+            "title": "Total Inward Leakage (TIL) for Respiratory Protective Devices",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/4ems-va7k/application/x-zip-compressed",
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
+            "landingPage": "http://www.fda.gov/Food/RecallsOutbreaksEmergencies/Recalls/default.htm",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2013-06-06",
+            "keyword": [
+                "cfsan"
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
+            "identifier": "7268c3d7-607f-452c-a54c-2ac89d7b6b65",
+            "description": "Food producers recall their products from the marketplace when the products are mislabeled or when the food may present a health hazard to consumers because the food is contaminated or has caused a foodborne illness outbreak.",
+            "title": "Recalls of Food and Dietary Supplements",
+            "programCode": [
+                "009:001"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fda.gov/Food/RecallsOutbreaksEmergencies/Recalls/default.htm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/cms-program-statistics-medicare-part-a-part-b-all-types-of-service",
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/9400ca2c-b36a-4380-873d-380ea67a249d/data-viewer",
+            "description": "The CMS Program Statistics -\u00a0Medicare Part A & Part B - All Types of Service tables provide use and payment data by type of coverage and type of service.\u00a0\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\u00a0\n\nBelow is the list of tables:\n\nMDCR SUMMARY AB 1. \u00a0Medicare Part A and Part B Summary: Utilization, Program Payments, and Cost Sharing for All Original Medicare Beneficiaries, by Type of Coverage and Type of Service, Yearly Trend\n\tMDCR SUMMARY AB 2. \u00a0Medicare Part A and Part B Summary: \u00a0Utilization, Program Payments, and Cost Sharing for Aged Original Medicare Beneficiaries, by Type of Coverage and Type of Service, Yearly Trend\n\tMDCR SUMMARY AB 3. \u00a0Medicare Part A and Part B Summary: \u00a0Utilization, Program Payments, and Cost Sharing for Disabled Original Medicare Beneficiaries by Type of Coverage and Type of Service, Yearly Trend\n\tMDCR SUMMARY AB 4. \u00a0Medicare Part A and Part B Summary: \u00a0Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Type of Coverage, Demographic Characteristics, and Medicare-Medicaid Enrollment Status\n\tMDCR SUMMARY AB 5. \u00a0Medicare Part A and Part B Summary: \u00a0Utilization, Program Payments, and Cost Sharing for Original Medicare Beneficiaries, by Type of Coverage and by Area of Residence\n\tMDCR SUMMARY AB 6. \u00a0Medicare Part A and Part B Summary: \u00a0Utilization and Program Payments for Original Medicare Beneficiaries, by Type of Entitlement, Amount of Program Payments, Type of Coverage, and Type of Service",
+            "title": "CMS Program Statistics - Medicare Part A & Part B - All Types of Service",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-02/CPS%20MDCR%20SUMMARY%20AB%202021.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Part A & Part B - All Types of Service : 2021-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-02/CPS%20MDCR%20SUMMARY%20AB%202020.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Part A & Part B - All Types of Service : 2020-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-01/CPS_MDCR_SUMMARY_AB_1-6.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Part A & Part B - All Types of Service : 2019-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-11/CPS%20MDCR%20TOTAL%20SUMMARY%20AB%202018.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Part A & Part B - All Types of Service : 2018-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2019-12/CPS_MDCR_SUMMARY_AB_2017.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Part A & Part B - All Types of Service : 2017-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-01/CPS_MDCR_SUMMARY_AB_ALL.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Part A & Part B - All Types of Service : 2016-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-01/CPS_MDCR_SUMMARY_AB_ALL_0.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Part A & Part B - All Types of Service : 2015-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-01/CPS_MDCR_SUMMARY_AB_ALL_1.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Part A & Part B - All Types of Service : 2014-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2020-01/CPS_MDCR_SUMMARY_AB_ALL_2.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Part A & Part B - All Types of Service : 2013-12-31"
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
+            "landingPage": "https://datatools.ahrq.gov/hcup-fast-stats",
+            "bureauCode": [
+                "009:33"
+            ],
+            "issued": "2021-02-13",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "agency-for-healthcare-research-and-quality-department-of-health-human-services",
+                "fast stats"
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
+            "identifier": "2cb5e7e7-361b-45ef-b662-8938e421f3ef",
+            "description": "Healthcare Cost and Utilization Project (HCUP) Fast Stats provides easy access to the latest HCUP-based statistics for health care information topics. HCUP Fast Stats uses visual statistical displays in stand-alone graphs, trend figures, or simple tables\nto convey complex information at a glance. Fast Stats is updated regularly for timely, topic-specific national and State-level statistics.\n\nFast Stats topics and graphics on hospital stays and emergency department visits, including information at the national, and state levels, trends over time, and selected priority topics such as:\n<li>State Trends in Hospital User by Payer\n<li>National Hospital Utilization and Costs\n<li>Hurricane Impact on Hospital Use\n<li>Opioids & Neonatal Abstinence Syndrome\n<li>Severe Maternal Morbidity",
+            "title": "HCUP Fast Stats",
+            "programCode": [
+                "009:074"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "http://www.hcup-us.ahrq.gov/faststats/landing.jsp",
+                    "description": "HCUP Fast Stats provides easy access to the latest HCUP-based statistics for health information topics. HCUP Fast Stats uses visual statistical displays in stand-alone graphs, trend figures, or simple tables to convey complex information at a glance. Information on the effect of Medicaid expansion on hospital use will be updated regularly (quarterly or annually, as newer data become available). \n",
+                    "@type": "dcat:Distribution",
+                    "title": "HCUP Fast Stats"
+                }
+            ],
+            "describedBy": "https://datatools.ahrq.gov/hcup-fast-stats"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.samhsa.gov/ebp-resource-center",
+            "bureauCode": [
+                "009:30"
+            ],
+            "issued": "2018-09-28",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "children",
+                "evidence",
+                "mental health",
+                "opioids",
+                "prevention",
+                "serious mental illness",
+                "substance abuse",
+                "women"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "SAMHSA Policy Lab",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Substance Abuse & Mental Health Services Administration"
+            },
+            "identifier": "74d54c36-1323-4969-b98a-a6a2974047e8",
+            "description": "<p>The Evidence-Based Practices Resource Center aims to provide communities, clinicians, policy-makers and others in the field with the information and tools they need to incorporate evidence-based practices into their communities or clinical settings. The Resource Center contains a collection of scientifically-based resources for a broad range of audiences, including Treatment Improvement Protocols, toolkits, resource guides, clinical practice guidelines, and other science-based resources.</p>",
+            "title": "Evidence-Based Practices Resource Center",
+            "programCode": [
+                "009:069"
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "Community",
+                "Health"
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
+                "cerebrovascular disease",
+                "county",
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
+            "identifier": "https://data.cdc.gov/api/views/dhsy-4sea",
+            "description": "2012 to 2014, 3-year average. Rates are age-standardized. County rates are spatially smoothed. The data can be viewed by gender and race/ethnicity. Data source: National Vital Statistics System. Additional data, maps, and methodology can be viewed on the Interactive Atlas of Heart Disease and Stroke http://www.cdc.gov/dhdsp/maps/atlas",
+            "title": "Stroke Mortality Data Among US Adults (35+) by State/Territory and County",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dhsy-4sea/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dhsy-4sea/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dhsy-4sea/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dhsy-4sea/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Heart-Disease-Stroke-Prevention/Stroke-Mortality-Data-Among-US-Adults-35-by-State-/dhsy-4sea",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Heart Disease & Stroke Prevention"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/m5zs-rf6r",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2018-01-04",
+            "@type": "dcat:Dataset",
+            "modified": "2018-01-04",
+            "keyword": [
+                "2017",
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
+            "identifier": "https://data.cdc.gov/api/views/m5zs-rf6r",
+            "description": "NNDSS - Table II. West Nile virus disease - 2017.  In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed.  The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\n\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\n C.N.M.I.: Commonwealth of Northern Mariana Islands. \r\n\r\n U: Unavailable. \u2014: No reported cases. N: Not reportable. NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n*Three low incidence conditions, rubella, rubella congenital, and tetanus, are in Table II to facilitate case count verification with reporting jurisdictions. \r\n\r\n\u2020 Case counts for reporting year 2017 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for tuberculosis are displayed in Table IV, which appears quarterly.\r\n\r\n\u00a7 Updated weekly from the Division of Vector-Borne Diseases, National Center for Emerging and Zoonotic Infectious Diseases (ArboNET Surveillance). Data for Jamestown Canyon virus, La Crosse virus, Chikungunya virus, Eastern equine encephalitis virus, Powassan virus, St. Louis virus, and Western equine encephalitis virus diseases are available in Table I. \r\n\r\n\u00b6 Not reportable in all states. Reporting exceptions are available at http://wwwn.cdc.gov/nndss/downloads.html.",
+            "title": "NNDSS - Table II. West Nile virus disease",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/m5zs-rf6r/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/m5zs-rf6r/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/m5zs-rf6r/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/m5zs-rf6r/rows.xml?accessType=DOWNLOAD",
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
+                "health",
+                "outcomes",
+                "places",
+                "prevalence",
+                "prevention",
+                "risk",
+                "status",
+                "zcta",
+                "zip code"
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
+            "identifier": "https://data.cdc.gov/api/views/s85h-9xpy",
+            "description": "This dataset contains model-based ZIP Code Tabulation Area (ZCTA) level estimates for the PLACES 2021 release. PLACES is the expansion of the original 500 Cities Project and covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code Tabulation Area (ZCTA) levels. It represents a first-of-its kind effort to release information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. The dataset includes estimates for 29 measures: 4 chronic disease-related health risk behaviors, 13 health outcomes, 3 health status, and 9 on using preventive services. These estimates can be used to identify emerging health problems and to help develop and carry out effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2019 or 2018 data, Census Bureau 2010 population data, and American Community Survey (ACS) 2015\u20132019 or 2014\u20132018 estimates. The 2021 release uses 2019 BRFSS data for 22 measures and 2018 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours a night). Seven measures are based on the 2018 BRFSS because the relevant questions are only asked every other year in the BRFSS. More information about the methodology can be found at www.cdc.gov/places.",
+            "title": "PLACES: Local Data for Better Health, ZCTA Data 2021 release",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/s85h-9xpy/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/s85h-9xpy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/s85h-9xpy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/s85h-9xpy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/dataset/PLACES-Local-Data-for-Better-Health-ZCTA-Data-2020/qnzd-25i4",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "500 Cities & Places"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/dataset/child-maltreatment-annual-reports",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2013-01-18",
+            "temporal": "2010-01-01T00:00:00-05:00/2010-01-01T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "child abuse",
+                "child maltreatment",
+                "children's health",
+                "child safety",
+                "population statistics",
+                "safety"
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
+            "identifier": "eb78172c-71ad-465f-a941-5ec61cdd0e3d",
+            "description": "<p>Child Maltreatment Reports contain data from the National Child Abuse and Neglect Data System that have been aggregated to the State level</p>",
+            "title": "Child Maltreatment Annual Reports",
+            "programCode": [
+                "184:016"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.acf.hhs.gov/cb/data-research/child-maltreatment",
+                    "mediaType": "text/html",
+                    "title": "HTML "
+                }
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/r4kb-pc87",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2025-01-10",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-10",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Research Branch (RB), National Personal Protective Technology Laboratory (NPPTL)",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/r4kb-pc87",
+            "description": "Supplies of N95\u00ae filtering facepiece respirators (FFRs) can become depleted during widespread outbreaks of infectious respiratory illnesses. To supplement the national inventory of NIOSH Approved\u00ae N95 FFRs during times of extreme shortages, FFR reuse following decontamination is a possible strategy. Decontamination is a process to reduce the number of pathogens on used FFRs before reuse. An effective FFR decontamination technique should significantly reduce the pathogen burden, but not reduce a respirator\u2019s filtration performance or its ability to fit properly. Another consideration is that no hazardous chemical residue should be left on the FFR following the decontamination process.",
+            "title": "Assessment of Filtration Efficiency, Manikin Fit Performance, and Strap Performance for Decontaminated N95 Filtering Facepiece Respirators",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/r4kb-pc87/application/x-zip-compressed",
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
+            "landingPage": "https://data.cdc.gov/d/3bjr-fr6m",
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
+            "identifier": "https://data.cdc.gov/api/views/3bjr-fr6m",
+            "description": "Rate of deaths by age/gender (per 100,000 population) for people killed in crashes involving a driver with BAC =>0.08%, 2012, 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File. Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
+            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, Region 8 - Denver",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3bjr-fr6m/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3bjr-fr6m/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3bjr-fr6m/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3bjr-fr6m/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/6jgb-zrsp",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2017-01-05",
+            "@type": "dcat:Dataset",
+            "modified": "2017-01-05",
+            "keyword": [
+                "2016",
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
+            "identifier": "https://data.cdc.gov/api/views/6jgb-zrsp",
+            "description": "NNDSS - Table II. Spotted Fever Rickettsiosis to Syphilis - 2016.  In this Table, provisional* cases of selected\u2020 notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states, in accordance with the current method of displaying MMWR data.  Data on United States exclude counts from US territories.\r\nNote:\r\nThese are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. \r\n\r\nCase counts in this table are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. \r\n\r\nFootnotes:\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable.    -: No reported cases.    N: Not reportable.    NN: Not Nationally Notifiable.   NP:  Nationally notifiable but not published.  Cum: Cumulative year-to-date counts.    Med: Median.    Max: Maximum.\r\n\r\n* Case counts for reporting year 2016 are provisional and subject to change.   For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. Data for TB are displayed in Table IV, which appears quarterly.\r\n\u2020 Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table II to facilitate case count verification with reporting jurisdictions.\r\n\u00a7 Illnesses with similar clinical presentation that result from Spotted fever group rickettsia infections are reported as Spotted fever rickettsioses.   Rocky Mountain spotted fever (RMSF) caused by Rickettsia rickettsii, is the most common and well-known spotted fever.",
+            "title": "NNDSS - Table II. Spotted Fever Rickettsiosis to Syphilis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6jgb-zrsp/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6jgb-zrsp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6jgb-zrsp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/6jgb-zrsp/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/unsk-b7fc",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-02-24",
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
+                "immunization",
+                "izdl",
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
+            "identifier": "https://data.cdc.gov/api/views/unsk-b7fc",
+            "description": "Overall US COVID-19 Vaccine\u00a0deliveries and\u00a0administration\u00a0data at national and jurisdiction level. Data represents all vaccine partners including jurisdictional partner clinics, retail pharmacies, long-term care facilities, dialysis centers, Federal Emergency Management Agency and Health Resources and Services Administration partner sites, and federal entity facilities.\u00a0",
+            "title": "COVID-19 Vaccinations in the United States,Jurisdiction",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/unsk-b7fc/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/unsk-b7fc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/unsk-b7fc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/unsk-b7fc/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cms.gov/covid-19/covid-19-nursing-home-data",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2021-12-22",
+            "temporal": "2020-05-24/2025-01-04",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-16",
+            "references": [
+                "https://data.cms.gov/resources/covid-19-nursing-home-methodology"
+            ],
+            "keyword": [
+                "chronic conditions",
+                "co-morbidity",
+                "hospitals & facilities",
+                "medicaid",
+                "medicare",
+                "original medicare",
+                "skilled nursing"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "COVID-19 Nursing Home Data - CCSQ",
+                "hasEmail": "mailto:NH_COVID_Data@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/137f90cb-ac53-4b3d-8358-e65cf64e03d3/data-viewer",
+            "description": "Submitted data as of the week ending 01/05/2025.\n\nThe Nursing Home COVID-19 Public File includes data reported by nursing homes to the CDC\u2019s National Healthcare Safety Network (NHSN) Long Term Care Facility (LTCF) COVID-19 Module.\u00a0For resources and ways to explore and visualize the data, please see the links to the left, as well as the buttons at the top of the page.\n\nUp to Date with COVID-19 Vaccines\n\nOn January 1, 2024, the Centers for Disease Control (CDC) changed the way it collects data to calculate the percent of staff who are up to date with their COVID-19 vaccination. It may take facilities some time to adapt to the new methodology. As a result, the reported percent of staff who are up to date with their COVID-19 vaccination should be viewed with caution over the next few weeks. Contact facilities directly for more information on their vaccination levels.",
+            "title": "COVID-19 Nursing Home Data",
+            "describedByType": "application/pdf",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/137f90cb-ac53-4b3d-8358-e65cf64e03d3/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "COVID-19 Nursing Home Data : 2025-01-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/32199fe1-8845-4007-b9dc-1f5562bf3e80/COVID-19%20Nursing%20Home%20Data%2001.05.2025.csv",
+                    "mediaType": "text/csv",
+                    "title": "COVID-19 Nursing Home Data : 2025-01-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/64db7975-4f2e-4c8d-9c83-c50753c89cd2/data",
+                    "mediaType": "text/html",
+                    "title": "COVID-19 Nursing Home Data : 2025-01-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/772ffd8b-6e41-4a0e-a465-a2e6445c9a4e/COVID-19%20Nursing%20Home%20Data%20Dec%2029%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-12-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/a8307994-ca6f-44dc-85d6-72cc36cd2029/COVID-19%20Nursing%20Home%20Data%20Dec%2008%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-12-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/e8adf204-a740-45d3-8f6e-d9511bc43d59/COVID-19%20Nursing%20Home%20Data%20Dec%2001%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/84d1d03a-4e1f-4045-9128-e048bcb241d5/COVID-19%20Nursing%20Home%20Data%20Nov%2024%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-11-24"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-12/367f7065-f8d4-4f52-bcf0-8569df5a8d3d/COVID-19%20Nursing%20Home%20Data%20Nov%2010%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-11-10"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/3a756717-8e5f-4eec-913f-44b58913269f/COVID-19%20Nursing%20Home%20Data%20Nov%2003%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-11-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/ae78830e-f13f-4965-a589-9227a8244248/COVID-19%20Nursing%20Home%20Data%20Oct%2027%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-10-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-11/60d48d89-517a-4185-aef4-b941d37f43cf/COVID-19%20Nursing%20Home%20Data%20Oct%2020%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-10-20"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/a957243d-a3ad-45f2-9101-018a87583a53/COVID-19%20Nursing%20Home%20Data%20Oct%2013%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-10-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/d9b4571c-d074-43bd-96c2-b99aa7193a7e/COVID-19%20Nursing%20Home%20Data%20Oct%2006%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-10-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/e0929720-08ce-43be-922b-f7e980b1b962/COVID-19%20Nursing%20Home%20Data%20Sep%2029%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-09-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/fb03cce5-3053-4536-a990-4599dd1cb0b1/COVID-19%20Nursing%20Home%20Data%20Sep%2022%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-09-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/8bd6f9cb-e186-485e-87ee-ed463e613b94/COVID-19%20Nursing%20Home%20Data%20Sep%2015%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-09-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/4694c3ab-ef18-4eac-9cc8-4c46dec70bf0/COVID-19%20Nursing%20Home%20Data%20Sep%2008%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-09-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/054b24c0-0aab-4ed3-80ae-1876ffc7bf90/COVID-19%20Nursing%20Home%20Data%20Sep%2001%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/ca4beb1e-be4d-45c1-a40e-ec19d8a4fba6/COVID-19%20Nursing%20Home%20Data%20Aug%2025%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-08-25"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-09/75ad1acd-d79f-4052-9cfd-682de2aa527e/COVID-19%20Nursing%20Home%20Data%20Aug%2018%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-08-18"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/d676bfd6-089d-4d52-b3d6-f05db220f198/COVID-19%20Nursing%20Home%20Data%20Aug%2011%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-08-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/5402a992-16b4-4b8c-8b0e-b2e43a6a442e/COVID-19%20Nursing%20Home%20Data%20Aug%2004%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-08-04"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/95b18965-eec0-4360-b63b-a0a60ed5d591/COVID-19%20Nursing%20Home%20Data%20Jul%2028%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-07-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/5feafb25-aed9-4acd-8f51-666b38d4c07a/COVID-19%20Nursing%20Home%20Data%20Jul%2021%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-07-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/776f201f-39e4-4622-a1f8-c45066d3288c/COVID-19%20Nursing%20Home%20Data%20Jul%2014%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-07-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/527c376b-61f1-4c2f-86ee-e0f984f31ecf/COVID-19%20Nursing%20Home%20Data%20Jul%2007%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-07-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/1eec351f-4f5d-48c8-853a-88f520975cdc/COVID-19%20Nursing%20Home%20Data%20Jun%2030%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-06-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/00b2d193-5b33-4117-9782-5fa1c4040ebc/COVID-19%20Nursing%20Home%20Data%20Jun%2023%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-06-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/61766e3a-a86c-4d74-acd5-5bf9b32dbf41/COVID-19%20Nursing%20Home%20Data%20Jun%2016%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-06-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/2843f6b3-f9ec-4f14-aef8-094486251f21/COVID-19%20Nursing%20Home%20Data%20Jun%2009%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-06-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/ee302769-b2f2-458d-ab8a-ac437ef8aed9/COVID-19%20Nursing%20Home%20Data%20Jun%2002%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-06-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/a5729f7c-0534-4f78-8557-03f1373a0ffd/COVID-19%20Nursing%20Home%20Data%20May%2026%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-05-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-06/a72aa146-d89c-45a4-82c4-efc1f3f779e0/COVID-19%20Nursing%20Home%20Data%20May%2019%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-05-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/32f57561-dec5-489f-9102-611c0f3d17d6/COVID-19%20Nursing%20Home%20Data%20May%2012%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-05-12"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/3eace1c8-a474-4477-a7cc-bf194efef7ae/COVID-19%20Nursing%20Home%20Data%20May%2005%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-05-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/44d974ad-a28a-4902-94d1-0c79d8ab98a3/COVID-19%20Nursing%20Home%20Data%20Apr%2028%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-04-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/c4bd805d-d2bb-4a4a-aad8-75c7e83b9d23/COVID-19%20Nursing%20Home%20Data%20Apr%2021%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-04-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-05/af393da7-0b3c-4736-9c1a-48f28a4cda67/COVID-19%20Nursing%20Home%20Data%20Apr%2014%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-04-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/7ab8a4f7-9450-4ac0-95f0-172cdeba3edb/COVID-19%20Nursing%20Home%20Data%20Apr%2007%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-04-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/3d0588bb-fd85-4b2e-aa84-3348a9f7cfa3/COVID-19%20Nursing%20Home%20Data%20Mar%2031%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-03-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/f49f73e1-b2b2-4dda-b654-667b891d1e62/COVID-19%20Nursing%20Home%20Data%20Mar%2024%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-03-24"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/52c852da-9c38-4d0b-85e0-729145b3fd4c/COVID-19%20Nursing%20Home%20Data%20Mar%2017%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-03-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/d648b602-fb69-4b86-b28c-af11acafcafc/COVID-19%20Nursing%20Home%20Data%20Mar%2010%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-03-10"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/67c45c00-9f62-43c9-b94f-5ec4e5e23262/COVID-19%20Nursing%20Home%20Data%20Mar%2003%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-03-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/f375bcb6-0882-4528-9362-5d83e3a51009/COVID-19%20Nursing%20Home%20Data%20Feb%2025%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-02-25"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/86223cac-8213-4f7e-a489-d26a3a4ae323/COVID-19%20Nursing%20Home%20Data%20Feb%2018%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-02-18"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/63f7d4c7-c331-47fa-901d-df94e81d37f8/COVID-19%20Nursing%20Home%20Data%20Feb%2011%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-02-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/b9b705b5-0ec3-4fb2-ba6c-f5027123d34a/COVID-19%20Nursing%20Home%20Data%20Feb%2004%202024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-02-04"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/110b0448-749e-46c6-83fe-6ba393ed94f6/COVID-19%20Nursing%20Home%20Data%2001.28.2024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-01-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/820a7347-3c67-438a-9047-2546f154f29e/COVID-19%20Nursing%20Home%20Data%2001.21.2024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-01-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-02/a375be1d-f2d0-456b-98b8-e5ec22577126/COVID-19%20Nursing%20Home%20Data%2001.14.2024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-01-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/3e57bc94-4843-401f-bc09-0a78ae398428/COVID-19%20Nursing%20Home%20Data%2001.07.2024.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2024-01-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/1dbd460e-2970-48bb-8c0c-fa52eeec0449/COVID-19%20Nursing%20Home%20Data%2012.31.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/92dffa14-cc43-4226-949b-a880e4e251d4/COVID-19%20Nursing%20Home%20Data%2012.24.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-12-24"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/bb22ca87-4928-4faa-bfa1-012d4b1347de/COVID-19%20Nursing%20Home%20Data%2012.10.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-12-10"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/fef02581-13a1-4a86-905d-23079c268e09/COVID-19%20Nursing%20Home%20Data%2012.03.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-12-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/794194cf-f6fb-4497-ae75-24cc3734a9b1/COVID-19%20Nursing%20Home%20Data%2011.26.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-11-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-12/7cdc36ca-9996-45d4-addd-f3d510493aee/COVID-19%20Nursing%20Home%20Data%2011.19.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-11-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/0d067c55-51f0-40b6-9c89-34396aa331e7/COVID-19%20Nursing%20Home%20Data%2011.05.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-11-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/98ed3da9-925d-4116-9a1e-93898fa58509/COVID-19%20Nursing%20Home%20Data%2010.29.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-10-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/f5a73e32-7f9c-4936-aa68-a7498b30d452/COVID-19%20Nursing%20Home%20Data%2010.22.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-10-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-11/e15b5b6d-3d6a-4ba4-bd88-870b9e89f512/COVID-19%20Nursing%20Home%20Data%2010.15.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-10-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/7f2aa034-bb83-418b-8a30-c26100fd5ada/COVID-19%20Nursing%20Home%20Data%2010.08.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-10-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/ac1993ee-3e46-4b76-afcd-dff972d97258/COVID-19%20Nursing%20Home%20Data%2010.01.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/1573c3b1-4f0f-4996-b8bd-06744f000d0f/COVID-19%20Nursing%20Home%20Data%2009.24.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-09-24"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/56b153a6-e5d8-4cf3-807d-afd0f4b0254b/COVID-19%20Nursing%20Home%20Data%2009.17.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-09-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/988e5ac5-d7de-4cd2-bf50-f2ad20538f19/COVID-19%20Nursing%20Home%20Data%2009.10.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-09-10"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/e9a520b8-d7b0-43dc-9123-0830801db8aa/COVID-19%20Nursing%20Home%20Data%2009.03.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-09-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/d0fcffb7-62f1-49c7-850b-2b6ba46b12f3/COVID-19%20Nursing%20Home%20Data%2008.27.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-08-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/2a8bcae3-85c1-4e79-a419-47f1ffcc3b03/COVID-19%20Nursing%20Home%20Data%2008.20.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-08-20"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/95d91d5d-49bb-4ac5-9ab9-94aac2a71a1a/COVID-19%20Nursing%20Home%20Data%2008.13.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-08-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-09/695cd404-5cee-4d4e-a2ee-66e3682b62d5/COVID-19%20Nursing%20Home%20Data%2008.06.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-08-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/8dbe45a5-8bd5-47b9-b093-14c9ff702cd9/COVID-19%20Nursing%20Home%20Data%2007.30.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-07-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/b4df5430-8b70-4ec3-ac8e-498eae6dd14b/COVID-19%20Nursing%20Home%20Data%2007.23.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-07-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-08/75d592c9-27b2-45bb-8350-0d4b3e131b77/COVID-19%20Nursing%20Home%20Data%2007.16.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-07-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/079854a1-30b2-442f-a48f-692088128a41/COVID-19%20Nursing%20Home%20Data%2007.09.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-07-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/29fadea6-2ef1-4c27-90e1-54946b990ecb/COVID-19%20Nursing%20Home%20Data%2007.02.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-07-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/ad9ac043-c5d5-4368-a55f-dbd8bae7a9cb/COVID-19%20Nursing%20Home%20Data%2006.25.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-06-25"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/207e597d-642b-42c6-860e-6802efcd84a8/COVID-19%20Nursing%20Home%20Data%2006.18.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-06-18"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/9c688363-f4a1-417f-bf39-b313b987e9b6/COVID-19%20Nursing%20Home%20Data%2006.11.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-06-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/2292aa7d-4144-4973-adef-f4fa1ede1489/COVID-19%20Nursing%20Home%20Data%2006.04.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-06-04"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/2e3fa382-0a20-4813-a003-072fbbabcb96/COVID-19%20Nursing%20Home%20Data%2005.28.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-05-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/46bf1e06-fe62-4b10-8a23-b17caae079a7/COVID-19%20Nursing%20Home%20Data%2005.21.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-05-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-06/26228c7e-d1cd-4b25-9100-e6ac97e530ed/COVID-19%20Nursing%20Home%20Data%2005.14.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-05-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/8e75cb19-15ea-42c7-9add-50506f4c6a5f/COVID-19%20Nursing%20Home%20Data%2005.07.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-05-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/daf87409-03f5-4bef-b072-5ef2f46da895/COVID-19%20Nursing%20Home%20Data%2004.30.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-04-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/17fdc765-6e27-4d5e-a882-af4768611435/COVID-19%20Nursing%20Home%20Data%2004.23.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-04-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/e3cd9d79-e425-4dca-bb43-11df69741a9d/COVID-19%20Nursing%20Home%20Data%2004.16.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-04-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/452dc811-5f3c-41dd-b1d2-bfd08b464118/COVID-19%20Nursing%20Home%20Data%2004.09.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-04-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/e9c5d641-5c6e-42ac-b9bc-a8d4f83c46d7/COVID-19%20Nursing%20Home%20Data%2004.02.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-04-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/2291de78-377a-45d2-b44e-d01f0c65bc52/COVID-19%20Nursing%20Home%20Data%2003.26.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-03-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/16ec8e45-cb69-4976-aafd-300c81deac01/COVID-19%20Nursing%20Home%20Data%2003.19.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-03-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-03/54ad1acb-21aa-46c5-bcfc-2272d3fc04a0/COVID-19%20Nursing%20Home%20Data%2003.12.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-03-12"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-03/04017444-1483-4d1d-b368-2eedaf8e2ec9/COVID-19%20Nursing%20Home%20Data%2003.05.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-03-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-03/9981a877-f52a-48e6-a09a-5368f9b9a12b/COVID-19%20Nursing%20Home%20Data%2002.26.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-02-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-03/599d5470-f000-4102-9dc6-240a352c9b36/COVID-19%20Nursing%20Home%20Data%2002.19.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-02-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-03/7b347b3f-064d-4525-90d1-e487f9eace13/COVID-19%20Nursing%20Home%20Data%2002.12.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-02-12"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-02/1d1f839d-1b56-468a-8994-312761e76038/COVID-19%20Nursing%20Home%20Data%2002.05.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-02-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-02/412f5937-c036-436b-9623-9d7183cb7ba5/COVID-19%20Nursing%20Home%20Data%2001.29.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-01-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-02/4afc3c44-b8e1-48a4-ad7b-4190a9f01763/COVID-19%20Nursing%20Home%20Data%2001.22.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-01-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-02/e2590f61-e62d-4111-a9a5-d51c08227598/COVID-19%20Nursing%20Home%20Data%2001.15.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-01-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-01/24541725-693b-4f19-8b59-df273ff8e7df/COVID-19%20Nursing%20Home%20Data%2001.08.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-01-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-01/872b4cf3-46db-4b77-9c87-4283210ec8c2/COVID-19%20Nursing%20Home%20Data%2001.01.2023.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2023-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-01/6eeb4d5d-df8d-4a8d-93ea-fdb3dcfa73c6/COVID-19%20Nursing%20Home%20Data%2012.18.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-12-18"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-12/dd1c56d7-a45c-4419-8bc2-bc5656b5cd8e/COVID-19%20Nursing%20Home%20Data%2012.11.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-12-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-12/77f66cb5-2fd6-449c-af94-10aaf835eeb5/COVID-19%20Nursing%20Home%20Data%2012.04.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-12-04"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-12/46a6d41a-efec-41f1-a79e-4497a249c530/COVID-19%20Nursing%20Home%20Data%2011.27.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-11-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-12/9c2bafc0-b5a8-4087-9d2d-1e7c2833c1a3/COVID-19%20Nursing%20Home%20Data%2011.20.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-11-20"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-12/73bacb6e-dd3d-4291-91e0-011131803dc3/COVID-19%20Nursing%20Home%20Data%2011.13.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-11-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-11/d35843b9-766d-4a0a-ac27-e408efa20909/COVID-19%20Nursing%20Home%20Data%2011.06.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-11-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-11/f44e3057-6a31-4740-98d7-d68eb815963f/COVID-19%20Nursing%20Home%20Data%2010.30.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-10-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-11/1ab3a60f-60b2-4ebc-8e4f-0efc2ea8679e/COVID-19%20Nursing%20Home%20Data%2010.23.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-10-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-11/eb951670-6cba-4738-afea-a534cbdfd022/COVID-19%20Nursing%20Home%20Data%2010.16.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-10-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-10/9c487b05-42df-460e-8093-a7d15913abfa/COVID-19%20Nursing%20Home%20Data%2010.09.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-10-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-10/5f8cffb5-369b-48a6-b1dc-8a62eb333b39/COVID-19%20Nursing%20Home%20Data%2010.02.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-10-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-10/952673d0-d13c-466b-8a50-37bd7e93054f/COVID-19%20Nursing%20Home%20Data%2009.25.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-09-25"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-10/b555e632-2c6b-4808-b5ef-3e2b803e5164/COVID-19%20Nursing%20Home%20Data%2009.18.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-09-18"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-09/df439fa4-8fe2-4724-b906-bcf77c11d8b9/COVID-19%20Nursing%20Home%20Data%2009.11.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-09-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-09/5bf58869-686c-40f7-b3fe-c15b3141b424/COVID-19%20Nursing%20Home%20Data%2009.04.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-09-04"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-09/1349b7f0-dc65-4172-822c-e2c6c4b9c681/COVID-19%20Nursing%20Home%20Data%2008.28.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-08-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-09/d7de4027-3c7d-41ae-b7a7-8e56ac929fb4/COVID-19%20Nursing%20Home%20Data%2008.21.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-08-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-09/d070bc94-6fb9-4c5c-812f-069b318ee1f4/COVID-19%20Nursing%20Home%20Data%2008.14.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-08-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-08/COVID-19%20Nursing%20Home%20Data%2008.07.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-08-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-08/COVID-19%20Nursing%20Home%20Data%2007.31.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-07-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-08/e6f2b907-df0a-47fc-8790-d281abf6fe70/COVID-19%20Nursing%20Home%20Data%2007.24.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-07-24"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-08/COVID-19%20Nursing%20Home%20Data%2007.17.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-07-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-07/COVID-19%20Nursing%20Home%20Data%2007.10.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-07-10"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-07/384d6e58-ae9b-4381-be3a-6d116f919cfb/COVID-19%20Nursing%20Home%20Data%2007.03.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-07-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-07/COVID-19%20Nursing%20Home%20Data%2006.26.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-06-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-07/COVID-19%20Nursing%20Home%20Data%2006.19.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-06-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-06/COVID-19%20Nursing%20Home%20Data%2006.12.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-06-12"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-06/COVID-19%20Nursing%20Home%20Data%2006.05.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-06-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-06/fdfb646a-d3c6-4995-8869-e791c7817d39/COVID-19%20Nursing%20Home%20Data%2005.29.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-05-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-06/25c9a6e6-ca46-4576-810a-a27bfa0d90a0/COVID-19%20Nursing%20Home%20Data%2005.22.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-05-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-06/COVID-19%20Nursing%20Home%20Data%2005.15.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-05-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-05/COVID-19%20Nursing%20Home%20Data%2005.08.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-05-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-05/COVID-19%20Nursing%20Home%20Data%2005.01.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-05-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-05/COVID-19%20Nursing%20Home%20Data%2004.24.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-04-24"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-05/COVID-19%20Nursing%20Home%20Data%2004.17.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-04-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-04/COVID-19%20Nursing%20Home%20Data%2004.10.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-04-10"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-04/COVID-19%20Nursing%20Home%20Data%2004.03.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-04-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-04/COVID-19%20Nursing%20Home%20Data%2003.27.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-03-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-04/COVID-19%20Nursing%20Home%20Data%2003.20.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-03-20"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-03/COVID-19%20Nursing%20Home%20Data%2003.13.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-03-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-03/adff9b9a-ee45-40b0-a37b-f2df4dbc7b5f/COVID-19%20Nursing%20Home%20Data%2003.06.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-03-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-03/COVID-19%20Nursing%20Home%20Data%2002.27.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-02-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-03/COVID-19%20Nursing%20Home%20Data%2002.20.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-02-20"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-03/COVID-19%20Nursing%20Home%20Data%2002.13.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-02-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-02/COVID-19%20Nursing%20Home%20Data%2002.06.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-02-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-02/COVID-19%20Nursing%20Home%20Data%2001.30.2022%20FINAL.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-01-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-02/COVID-19%20Nursing%20Home%20Data%2001.23.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-01-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-02/COVID-19%20Nursing%20Home%20Data%2001.16.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-01-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-01/COVID-19%20Nursing%20Home%20Data%2001.09.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-01-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-01/COVID-19%20Nursing%20Home%20Data%2001.02.2022.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2022-01-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-01/COVID-19%20Nursing%20Home%20Data%2012.26.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-12-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-01/COVID-19%20Nursing%20Home%20Data%2012.19.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-12-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-12/COVID-19%20Nursing%20Home%20Data%2012.12.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-12-12"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-12/COVID-19%20Nursing%20Home%20Data%2012.05.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-12-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-12/COVID-19%20Nursing%20Home%20Data%2011.28.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-11-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-12/COVID-19%20Nursing%20Home%20Data%2011.21.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-11-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-12/COVID-19%20Nursing%20Home%20Data%2011.14.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-11-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/COVID-19%20Nursing%20Home%20Data%2011.07.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-11-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/COVID-19%20Nursing%20Home%20Data%2010.31.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-10-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/62cda09e-cbf0-4a35-bd92-a69e44753fe0/COVID-19%20Nursing%20Home%20Data%2010.24.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-10-24"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-11/a4c16a95-eff2-43e5-b33f-95addfc69ac2/COVID-19%20Nursing%20Home%20Data%2010.17.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-10-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-10/81407303-0c44-4c9c-ae7d-98753649eebd/COVID-19%20Nursing%20Home%20Data%2010.10.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-10-10"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-10/e0c87c9b-4cfe-4db8-b77b-0bb62153ce20/COVID-19%20Nursing%20Home%20Data%2010.03.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-10-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-03/c398cc42-55c4-409d-af8d-64681b17ae82/COVID-19%20Nursing%20Home%20Data%2009.26.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-09-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-10/2ead78d8-fda8-4aec-8ed7-3f6ce83bfd1b/COVID-19%20Nursing%20Home%20Data%2009.19.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-09-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-09/b3e1fdd5-0753-4453-88ca-5d0dc9627a5a/COVID-19%20Nursing%20Home%20Data%2009.12.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-09-12"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-09/15d3a917-aada-4acb-b7fe-ba505cca9ca7/COVID-19%20Nursing%20Home%20Data%2009.05.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-09-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-09/b7fe694d-1800-4806-b715-b9cf0195b273/COVID-19%20Nursing%20Home%20Data%2008.29.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-08-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-09/a2a7b7d0-451f-4d79-981d-9c5043ade622/COVID-19%20Nursing%20Home%20Data%2008.22.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-08-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-09/b941feb4-12a8-44d1-9d45-9a1add72001c/COVID-19%20Nursing%20Home%20Data%2008.15.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-08-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-12/COVID-19%20Nursing%20Home%20Data%2008.08.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-08-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-08/covid-19-nursing-home-data-08.01.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-08-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-08/covid-19-nursing-home-data-07.25.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-07-25"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-08/covid-19-nursing-home-data-07.18.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-07-18"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-07.11.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-07-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/COVID-19%20Nursing%20Home%20Data%2007.04.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-07-04"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/COVID-19%20Nursing%20Home%20Data%2006%2027%2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-06-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-06-20-21.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-06-20"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-06-13-21.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-06-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-06-06-21.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-06-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-05-30-21.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-05-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-05.23.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-05-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-05.16.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-05-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-05.09.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-05-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-05.02.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-05-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-04.25.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-04-25"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-04.18.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-04-18"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-04.11.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-04-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-04.04.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-04-04"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-03.28.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-03-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-03.21.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-03-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-03.14.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-03-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-03.07.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-03-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-02.28.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-02-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-02.14.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-02-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-02.14.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-02-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-02.07.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-02-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-01.31.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-01-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-01.24.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-01-24"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-01.17.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-01-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-01.10.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-01-10"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-01.03.2021.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2021-01-03"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-12.27.2020.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2020-12-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-12.20.2020.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2020-12-20"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-12.13.2020.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2020-12-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-12.06.2020.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2020-12-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-11.29.2020.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2020-11-29"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-11.22.2020.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2020-11-22"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-11.15.2020.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2020-11-15"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-11.08.2020.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2020-11-08"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-11.01.2020.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2020-11-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-10.25.2020.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2020-10-25"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-10.18.2020.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2020-10-18"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-10.11.2020.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2020-10-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-10.04.2020.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2020-10-04"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-09.27.2020.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2020-09-27"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-09.20.2020.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2020-09-20"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-09.13.2020.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2020-09-13"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-09.06.2020.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2020-09-06"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-08.30.2020.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2020-08-30"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-08.23.2020.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2020-08-23"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-08.16.2020.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2020-08-16"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-08.09.2020.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2020-08-09"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-08.02.2020.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2020-08-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-07.26.2020.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2020-07-26"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-07.19.2020.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2020-07-19"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-07.12.2020.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2020-07-12"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-07.05.2020.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2020-07-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-06.28.2020.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2020-06-28"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-06.21.2020.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2020-06-21"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-06.14.2020.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2020-06-14"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-06.07.2020.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2020-06-07"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-07/covid-19-nursing-home-data-05.31.2020.zip",
+                    "mediaType": "application/zip",
+                    "title": "COVID-19 Nursing Home Data : 2020-05-31"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-10/COVID-19%20Nursing%20Home%20Data%20Dictionary_0.pdf",
+            "dataQuality": true,
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1W",
+            "theme": [
+                "Medicare",
+                "Medicaid"
+            ],
+            "language": [
+                "en-US"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfStandards/search.cfm",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "references": [
+                "http://www.fda.gov/MedicalDevices/DeviceRegulationandGuidance/Standards/default.htm"
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
+            "identifier": "4b318035-9f0e-4f7e-b4ff-c70fd57b4994",
+            "description": "This database consists of those national and international standards recognized by FDA which manufacturers can declare conformity to and is part of the information the Center can use to make an appropriate decision regarding the clearance or approval of a submission. Information submitted on conformance with such standards will have a direct bearing on safety and effectiveness determinations made during the review of IDEs, HDEs, PMAs, and PDPs. Conformance with recognized consensus standards in and of itself, however, may not always be a sufficient basis for regulatory decisions.",
+            "title": "FDA Recognized Consensus Standards",
+            "programCode": [
+                "009:005"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfStandards/search.cfm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P3M"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/xf2e-rch5",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2025-01-18",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-17",
+            "keyword": [
+                "chip",
+                "maternal health",
+                "medicaid",
+                "preterm birth",
+                "severe maternal morbidity",
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
+            "identifier": "ee3b9534-0d19-4c1b-bf74-43f898d5de7c",
+            "description": "This data set includes annual counts and rates of Medicaid- and Children\u2019s Health Insurance Program (CHIP)-covered live-birth deliveries that were preterm or with a severe maternal morbidity (SMM) condition within six weeks before or after delivery. Results are shown overall; by state; and by four subpopulation topics: age group, race and ethnicity, disability-related eligibility category, and type of SMM condition (SMM category only). \r\nThese results were generated using Transformed Medicaid Statistical Information System (T-MSIS) Analytic Files (TAF) Release 1 data and the Race/Ethnicity Imputation Companion File. This data set includes Medicaid and CHIP enrollees in all 50 states, the District of Columbia, Puerto Rico, and the U.S. Virgin Islands, who were ages 15 to 49 as of their delivery date, who were enrolled in Medicaid or CHIP at any point in the calendar year, and who had a live birth. Enrollees in Guam, American Samoa, the Northern Mariana Islands, and select states with TAF data quality issues are not included. Results shown for the race and ethnicity subpopulation topic exclude enrollees in the U.S. Virgin Islands. Results for SMM are calculated per 10,000 Medicaid- and CHIP-covered live births. Results for states with TAF data quality issues in the year have a value of \"Unusable data.\" Some rows in the data set have a value of \"DS,\" which indicates that data were suppressed according to the Centers for Medicare & Medicaid Services\u2019 Cell Suppression Policy for values between 1 and 10.\r\n\r\nThis data set is based on the brief: \"Prematurity and severe maternal morbidity among Medicaid- and CHIP-covered live births in 2021.\" Preterm birth is defined as a live birth that occurs before the 37th week of gestation. SMM deliveries are defined as live births with an SMM condition within six weeks before or after delivery (Identifying Severe Maternal Morbidity (SMM)). Enrollees are assigned to an age group subpopulation using age as of their delivery date. Enrollees are assigned to a race and ethnicity subpopulation using the state-reported race and ethnicity information in TAF when it is available and of good quality; if it is missing or unreliable, race and ethnicity is indirectly estimated using an enhanced version of Bayesian Improved Surname Geocoding (BISG) (Race and ethnicity of the national Medicaid and CHIP population in 2020). Enrollees are assigned to a disability category subpopulation using their latest reported eligibility group code and age in the year (Medicaid enrollees who qualify for benefits based on disability in 2020). Please refer to the full brief for additional context about the methodology and detailed findings. Future updates to this data set will include more recent data years as the TAF data become available.",
+            "title": "Prematurity and severe maternal morbidity among Medicaid- and CHIP-covered live births",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/preterm-birth-and-smm-2020-2022-01172025.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/fdyw-m38t",
+            "bureauCode": [
+                "009:032"
+            ],
+            "issued": "2018-08-01",
+            "@type": "dcat:Dataset",
+            "modified": "2018-11-27",
+            "keyword": [
+                "environmental health",
+                "skin cancer",
+                "sunlight",
+                "total solar irradiance"
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
+            "identifier": "https://data.cdc.gov/api/views/fdyw-m38t",
+            "description": "This dataset provides data at the county level for the contiguous United States. It includes daily Global Horizontal Irradiance (GHI) data from 1991-2012 provided by the Environmental Remote Sensing group at the Rollins School of Public Health at Emory University. Please refer to the metadata attachment for more information.\r\n\r\nThese data are used by the CDC's National Environmental Public Health Tracking Network to generate sunlight and ultraviolet (UV) measures. Learn more about sunlight and UV on the Tracking Network's website: https://ephtracking.cdc.gov/showUVLanding.\r\n\r\nBy using these data, you signify your agreement to comply with the following requirements: \r\n1.\tUse the data for statistical reporting and analysis only. \r\n2.\tDo not attempt to learn the identity of any person included in the data and do not combine these data with other data for the purpose of matching records to identify individuals. \r\n3.\tDo not disclose of or make use of the identity of any person or establishment discovered inadvertently and report the discovery to: trackingsupport@cdc.gov. \r\n4.\tDo not imply or state, either in written or oral form, that interpretations based on the data are those of the original data sources and CDC unless the data user and data source are formally collaborating. \r\n5.\tAcknowledge, in all reports or presentations based on these data, the original source of the data and CDC. \r\n6.\tSuggested citation: Centers for Disease Control and Prevention. National Environmental Public Health Tracking Network. Web. Accessed: insert date. www.cdc.gov/ephtracking. \r\n\r\nProblems or Questions? \r\nEmail trackingsupport@cdc.gov.",
+            "title": "Population-Weighted Global Horizontal Irradiance, 1991-2012",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fdyw-m38t/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fdyw-m38t/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fdyw-m38t/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/fdyw-m38t/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/xfrb-e2j6",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-04-26",
+            "@type": "dcat:Dataset",
+            "modified": "2023-04-25",
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
+            "identifier": "3a0999f8-2850-4fee-aefe-8ae6a22e56c0",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-04-17-to-2023-04-23",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rprt-drug-4-17-2023-to-4-23-2023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-04-17-to-2023-04-23"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-07-09",
+            "temporal": "1975/2020",
+            "@type": "dcat:Dataset",
+            "modified": "2024-09-16",
+            "keyword": [
+                "american hospital association",
+                "community hospitals",
+                "federal hospitals",
+                "health care use",
+                "health us",
+                "hospital",
+                "hospital admissions",
+                "hospital ownership",
+                "hospital size",
+                "length of hospital stay",
+                "outpatient surgery",
+                "outpatient visits",
+                "sdoh-access-to-health-care",
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
+            "identifier": "https://data.cdc.gov/api/views/rear-2epk",
+            "description": "Data on hospital admission, average length of stay, outpatient visits, and outpatient surgery in the United States, by type of ownership and size of hospital. Data are from Health, United States. SOURCE: American Hospital Association (AHA) Annual Survey of Hospitals, Hospital Statistics.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
+            "title": "DQS Hospital admission, average length of stay, outpatient visits, and outpatient surgery by type of ownership and size of hospital: United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rear-2epk/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rear-2epk/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rear-2epk/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/rear-2epk/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Annual (R/P1Y)",
+            "theme": [
+                "National Center for Health Statistics"
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
+            "identifier": "https://data.cdc.gov/api/views/ix4g-rt8v",
+            "description": "ART data are made available as part of the National ART Surveillance System (NASS) that collects success rates, services, profiles and annual summary data from fertility clinics across the U.S. There are four datasets available: ART Services and Profiles, ART Patient and Cycle Characteristics, ART Success Rates, and ART Summary. All four datasets may be linked by \u201cClinicID.\u201d ClinicID is a unique identifier for each clinic that reported cycles. The Services and Profiles dataset provides an overview of clinic services, the clinic\u2019s contact information, location, the medical director\u2019s name, and summary statistics.",
+            "title": "2022 Final Assisted Reproductive Technology (ART) Services and Profiles",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ix4g-rt8v/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ix4g-rt8v/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ix4g-rt8v/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ix4g-rt8v/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://data.cdc.gov/dataset/2020-Final-Assisted-Reproductive-Technology-ART-Se/ix4g-rt8v",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Assisted Reproductive Technology (ART)"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/dataset/office-medicare-hearings-and-appeals-omha-receipts-fiscal-year",
+            "bureauCode": [
+                "001:05"
+            ],
+            "issued": "2014-02-04",
+            "temporal": "2005-01-01T00:00:00-05:00/2012-01-01T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "appeals",
+                "claims",
+                "medicare",
+                "omha",
+                "receipts"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Kimberly Rubi",
+                "hasEmail": "mailto:kimberly.rubi@hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Office of Medicare Hearings and Appeals"
+            },
+            "identifier": "037bce72-0ee5-4ddc-9299-1cc37a6a847e",
+            "description": "<p>This data set provides information about the appeals received by the Office of Medicare and Hearings for Fiscal Year 2005 - 2012.</p>",
+            "title": "Office of Medicare Hearings and Appeals (OMHA) - Receipts by Fiscal Year",
+            "programCode": [
+                "009:111"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "http://www.hhs.gov/omha/Data/Health%20Data%20Sets/receipts_2005_to_2006_csv.csv",
+                    "description": "This dataset is a compilation of appeals received in Fiscal Year 2005 and Fiscal Year 2006. \n",
+                    "@type": "dcat:Distribution",
+                    "title": "Office of Medicare Hearings and Appeals (OMHA) Receipts by Fiscal Year - 2005-2006"
+                },
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "http://www.hhs.gov/omha/Data/Health%20Data%20Sets/receipts_2007_to_2008_csv.csv",
+                    "description": "This dataset is a compilation of appeals received in Fiscal Year 2007 and Fiscal Year 2008. \n",
+                    "@type": "dcat:Distribution",
+                    "title": "Office of Medicare Hearings and Appeals (OMHA) Receipts by Fiscal Year 2007-2008"
+                },
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "http://www.hhs.gov/omha/Data/Health%20Data%20Sets/receipts_2009_to_2010_csv.csv",
+                    "description": "This dataset is a compilation of appeals received in Fiscal Year 2009 and Fiscal Year 2010. \n",
+                    "@type": "dcat:Distribution",
+                    "title": "Office of Medicare Hearings and Appeals (OMHA) Receipts by Fiscal Year 2009-2010"
+                },
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "http://www.hhs.gov/omha/Data/Health%20Data%20Sets/receipts_2011_to_2012_csv.csv",
+                    "description": "This dataset is a compilation of appeals received in Fiscal Year 2011 and Fiscal Year 2012. \n",
+                    "@type": "dcat:Distribution",
+                    "title": "Office of Medicare Hearings and Appeals (OMHA) Receipts by Fiscal Year 2011-2012"
+                }
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/adnf-fpem",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-14",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Health Effects Laboratory Research, Allergy and Clinical Immunology Branch",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/adnf-fpem",
+            "description": "MicroRNAs are essential regulators of gene expression in humans and can control pathogenesis and host-virus interactions. Notably, the role of specific miRNAs during influenza virus infections are still ill-defined. The central goal of this study was to identify novel miRNAs and their target genes in response to influenza virus infections in airway epithelium. Human airway epithelial cells exposed to influenza virus induced several novel miRNAs that were identified using next generation sequencing (NGS) and their target genes by biochemical methods. NGS analysis predicted forty-two RNA sequences as possible miRNAs based on computational algorithms. Expression patterns of these putative miRNAs were further confirmed using RT-PCR in human bronchial epithelial cells (HBEpC) exposed to H1N1, H9N1(1P10) and H9N1 (1WF10) strains of influenza virus. A time course study showed significant downregulation of put-miR-34 in H1N1 and put-miR-35 in H9N1(1P10) infected cells, consistent with the NGS data. Additionally put-miR-34, and put-miR-35 showed a high fold enrichment in argonaute-immunoprecipitation compared to the controls, indicating their ability to form a complex with argonaute protein and RNA induced silencing complex (RISC), a typical mode of action found with miRNAs. Our earlier studies have shown that replication and survival of influenza virus is modulated by certain transcription factors, such as, NF-\u0138B. To identify the target(s) of these putative miRNAs, we screened 84 transcription factors that have a role in viral pathogenesis. Cells transfected with mimic of the put-miR-34 showed significant decrease in expression of Signal Transducers and Activators of Transcription 3 (STAT3), and the inhibitor of put-miR-34 showed significant increase in STAT3 expression and its phosphorylation. In addition, put-miR-34 had 76% homology to the untranslated region (UTR) of STAT3. NGS and PCR array data submitted to the Gene Ontology also predicted the role of transcription factors modulated by put-miR-34. Our data suggests that put-miR-34 could be a good target for the antiviral therapy as the hyperactivation or inactivation of STAT3 results in viral disease, as tightly regulated STAT3 function is central to health.",
+            "title": "Influenza virus induced novel miRNAs regulate the STAT pathway",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/adnf-fpem/application/x-zip-compressed",
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
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/provisional-drug-overdose.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-04-15",
+            "@type": "dcat:Dataset",
+            "temporal": "2019-01-01/2024-06-30",
+            "modified": "2025-01-22",
+            "keyword": [
+                "deaths",
+                "drug overdose",
+                "hhs region",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "united states",
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
+            "identifier": "https://data.cdc.gov/api/views/8hzs-zshh",
+            "description": "This data presents counts of provisional drug overdose deaths by selected drugs and U.S. Department of Health and Human Services (HHS) public health regions, based on provisional mortality data from the National Vital Statistics System. This data is limited to drug overdose deaths with an underlying cause of death assigned to International Statistical Classification of Diseases, 10th Revision (ICD-10) code numbers X40-X44 (unintentional), X60-X64 (suicide), X85 (homicide), or Y10-Y14 (undetermined intent). Specific drugs were identified using methods for searching literal text from death certificates. \n\nThe provisional data are based on a current flow of mortality data and include reported 12 month-ending provisional counts of drug overdose deaths by jurisdiction of occurrence and specified drug. Provisional drug overdose death counts presented on this page are for \u201c12-month ending periods,\u201d defined as the number of deaths occurring in the 12-month period ending in the month indicated. For example, the 12-month ending period in June 2022 would include deaths occurring from July 1, 2021, through June 30, 2022. Evaluation of trends over time should compare estimates from year to year (June 2021 and June 2022), rather than month to month, to avoid overlapping time periods. It is important to note that the data represent counts of deaths, and not mortality ratios or rates, which are the standard measure used to compare groups, and therefore should not be used to determine populations at disproportionate risk of drug overdose death.",
+            "title": "Provisional drug overdose death counts for specific drugs",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8hzs-zshh/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8hzs-zshh/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8hzs-zshh/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8hzs-zshh/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P6M",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/nhanes/visualization/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-03-02",
+            "@type": "dcat:Dataset",
+            "temporal": "1999/2018",
+            "modified": "2023-09-08",
+            "keyword": [
+                "oral health"
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
+            "identifier": "https://data.cdc.gov/api/views/ggsw-596z",
+            "description": "These data represent prevalence estimates of select oral health topics from the National Health and Nutrition Examination Survey (NHANES).",
+            "title": "NHANES Select Oral Health Prevalence Estimates",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ggsw-596z/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ggsw-596z/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ggsw-596z/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ggsw-596z/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "U.S.",
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
+            "landingPage": "https://healthdata.gov/d/xinu-a2t7",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-08-09",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-16",
+            "keyword": [
+                "py2023",
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
+            "identifier": "253ecd82-4a43-4150-bd1e-3de6de1e2953",
+            "description": "The Dental SHOP Market file of the QHP Landscape Files contains information on certified dental plans offered through an Exchange to employers in the Small Business Health Options Program (SHOP) market. These plans are also known as Stand-alone Dental Plans (SADPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
+            "title": "QHP Landscape Instructions PY2023 Dental SHOP",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2023/den-shop-lndscp-in.pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/xir8-6rfn",
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
+            "identifier": "142041ba-885c-517e-be08-53cc86a13f9a",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "CoreSEt version v2.10.6 (coreset-etl-test)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/core-set/2.10.6/20241023/version.csv",
+                    "description": "CoreSEt version v2.10.6 (coreset-etl-test)",
+                    "@type": "dcat:Distribution",
+                    "title": "CoreSEt version v2.10.6 (coreset-etl-test)"
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
+            "issued": "2022-10-11",
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
+            "identifier": "https://data.cdc.gov/api/views/373s-ayzu",
+            "description": "This dataset contains model-based census tract-level estimates for the PLACES 2021 release. PLACES is the expansion of the original 500 Cities project and covers the entire United States\u201450 states and the District of Columbia (DC)\u2014at county, place, census tract, and ZIP Code Tabulation Area (ZCTA) levels. It represents a first-of-its kind effort to release information uniformly on this large scale for local areas at 4 geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. The dataset includes estimates for 29 measures: 4 chronic disease-related health risk behaviors, 13 health outcomes, 3 health status, and 9 on use of preventive services. These estimates can be used to identify emerging health problems and to help develop and carry out effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these model-based estimates include Behavioral Risk Factor Surveillance System (BRFSS) 2019 or 2018 data, Census Bureau 2010 population data, and American Community Survey (ACS) 2015\u2013019 or 2014\u20132018 estimates. The 2021 release uses 2019 BRFSS data for 22 measures and 2018 BRFSS data for 7 measures (all teeth lost, dental visits, mammograms, cervical cancer screening, colorectal cancer screening, core preventive services among older adults, and sleeping less than 7 hours a night). Seven measures are based on the 2018 BRFSS because the relevant questions are only asked every other year in the BRFSS. More information about the methodology can be found at www.cdc.gov/places.",
+            "title": "PLACES: Local Data for Better Health, Census Tract Data 2021 release",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/373s-ayzu/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/373s-ayzu/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/373s-ayzu/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/373s-ayzu/rows.xml?accessType=DOWNLOAD",
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
+            "accessLevel": "restricted public",
+            "landingPage": "https://www.cdc.gov/nchs/nvss/deaths.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.\u00a0 Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.\u00a0 If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.\u00a0 For more information about submitting a proposal for data access, please see:\u00a0https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+            "issued": "2022-05-31",
+            "@type": "dcat:Dataset",
+            "temporal": "1950-2020",
+            "modified": "2023-03-27",
+            "references": [
+                "https://www.cdc.gov/nchs/nvss/deaths.htm"
+            ],
+            "keyword": [
+                "deaths",
+                "injury",
+                "mortality",
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
+            "identifier": "https://data.cdc.gov/api/views/kn6j-fsdu",
+            "description": "Data are based on information from all death certificates filed in the 50 states and the District of Columbia and processed by the National Center for Health Statistics (NCHS). Restricted data available through the Research Data Center include geographical indicators, exact date of birth and death of decedent, among others.",
+            "title": "Restricted mortality data from the National Vital Statistics System",
+            "isPartOf": "https://www.cdc.gov/nchs/nvss/deaths.htm",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "description": "Data are based on information from all death certificates filed in the 50 states and the District of Columbia and processed by the National Center for Health Statistics (NCHS). Restricted data available through the Research Data Center include geographical indicators, exact date of birth and death of decedent, among others.",
+                    "@type": "dcat:Distribution",
+                    "title": "Restricted mortality data from the National Vital Statistics System"
+                }
+            ],
+            "spatial": "United States",
+            "describedBy": "All death certificate records issued by each state and independent jurisdiction each year",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1Y",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/xj9d-qbai",
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
+            "identifier": "fb0920cb-7ed2-57ee-b138-1f7947ba6ac5",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "Scorecard measure v2.11.9 (prod)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.9/20241107/measure.csv",
+                    "description": "Scorecard measure v2.11.9 (prod)",
+                    "@type": "dcat:Distribution",
+                    "title": "Scorecard measure v2.11.9 (prod)"
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
+            "landingPage": "http://www.informatics.jax.org/expression.shtml",
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
+                "fn": "DI FRANCESCO, VALENTINA\u00a0",
+                "hasEmail": "mailto:valentina.difrancesco@nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
+            "identifier": "7d09c1b3-9752-44a4-bec2-42c273e927f9",
+            "description": "<p>MGI is the international database resource for the laboratory mouse, providing integrated genetic, genomic, and biological data to facilitate the study of human health and disease.</p>",
+            "title": "Mouse Genome Informatics (MGI)",
+            "programCode": [
+                "009:045"
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/xkj2-kr3z",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-09-29",
+            "@type": "dcat:Dataset",
+            "modified": "2024-12-27",
+            "keyword": [
+                "marketplace",
+                "transitions in coverage"
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
+            "identifier": "5636a78c-fe18-4229-aee1-e40fa910a8a0",
+            "description": "Metrics from individual Marketplaces during the current reporting period. The report includes data for the states using HealthCare.gov.<br />\r\n<b>Sources:</b> HealthCare.gov application and policy data through October 6, 2024, HealthCare.gov inbound account transfer data through November 7, 2024, and T-MSIS Analytic Files (TAF) through July 2024 (TAF version 7.1). The table includes states that use HealthCare.gov.<br />\r\n<b>Notes: </b>\r\n<ol>\r\n<li>This table includes Marketplace consumers who submitted a HealthCare.gov application from March 6, 2023 - October 6, 2024 or who had an inbound account transfer from April 3, 2023 - November 7, 2024, who can be linked to an enrollment record in TAF that shows a last day of Medicaid or CHIP enrollment from March 31, 2023 - July 31, 2024. Beneficiaries with a leaving event may have continuous coverage through another coverage source, including Medicaid or CHIP coverage in another state. However, a beneficiary that lost Medicaid or CHIP coverage and regained coverage in the same state must have a gap of at least 31 days or a full calendar month.</li>\r\n<li>This table includes Medicaid or CHIP beneficiaries with full benefits in the month they left Medicaid or CHIP coverage.</li>\r\n<li>\u2018Account Transfer Consumers Whose Medicaid or CHIP Coverage was Terminated\u2019 are consumers 1) whose full benefit Medicaid or CHIP coverage was terminated and 2) were sent by a state Medicaid or CHIP agency via secure electronic file to the HealthCare.gov Marketplace in a process referred to as an inbound account transfer either 2 months before or 4 months after they left Medicaid or CHIP.  'Marketplace Consumers Not on Account Transfer Whose Medicaid or CHIP Coverage was Terminated' are consumers 1) who applied at the HealthCare.gov Marketplace and 2) were not sent by a state Medicaid or CHIP agency via an inbound account transfer either 2 months before or 4 months after they left Medicaid or CHIP.</li> \r\n<li>Marketplace consumers counts are based on the month Medicaid or CHIP coverage was terminated for a beneficiary. Counts include all recent Marketplace activity.</li>\r\n<li>HealthCare.gov data are organized by week. Reporting months start on the first Monday of the month and end on the first Sunday of the next month when the last day of the reporting month is not a Sunday. HealthCare.gov data are through Sunday, October 6.</li>\r\n<li>Data are preliminary and will be restated over time to reflect consumers most recent HealthCare.gov status. Data may change as states resubmit T-MSIS data or data quality issues are identified.</li>\r\n<li>See the data and methodology documentation for a full description of the data sources, measure definitions, and general data limitations.</li>\r\n</ol>\t\t\t\r\n<b>Data notes:</b> <ol>\r\n<li> The percentages for the 'Marketplace Consumers Not on Account Transfer whose Medicaid or CHIP Coverage was Terminated' data record group are marked as not available (NA) because the full population of consumers without an account transfer was not available for this report.</li>\r\n<li>Virginia operated a Federally Facilitated Exchange (FFE) on the HealthCare.gov platform during 2023.  In 2024, the state started operating a State Based Marketplace (SBM) platform. This table only includes data about 2023 applications and policies obtained through the HealthCare.gov Marketplace. Due to limited Marketplace activity on the HealthCare.gov platform in November 2023, data from November 2023 onward are excluded. The cumulative count and percentage for Virginia and the HealthCare.gov total reflect Virginia data from April 2023 through October 2023.</li>\t\r\n</ol>\t\t\t\t\r\nAPTC: Advance Premium Tax Credit; CHIP: Children's Health Insurance Program; QHP: Qualified Health Plan; NA: Not Available",
+            "title": "HealthCare.gov Transitions Marketplace Medicaid Unwinding Report",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/healthcare.gov-transitions-data-december-2024-release.csv",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/healthcare.gov-transitions-data-december-2024-release.xlsx",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P10Y",
+            "theme": [
+                "Unwinding"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/xksj-pjwd",
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
+            "identifier": "3606023c-6e7f-53b5-b1ff-1757ca9da64e",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "featAuto_files_stateSnapshot",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20220921_v2_ETL_DEV/files_stateSnapshot.csv",
+                    "description": "{\"dataset\": \"files_stateSnapshot\", \"stage\": \"featAuto\", \"update_id\": \"20220921_v2_ETL_DEV\"}",
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
+            "landingPage": "https://www.ncbi.nlm.nih.gov/books",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2022-02-08",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-08",
+            "keyword": [
+                "books",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ken6-3jnj",
+            "description": "A collection of online books and documents in life science and healthcare whose full text can be searched through the Entrez system. Bookshelf provides free online access to books and documents in life science and healthcare.",
+            "title": "Bookshelf",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/books",
+                    "mediaType": "text/html",
+                    "title": "Bookshelf Homepage and Search"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Literature"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/dt66-w6m6",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-02-24",
+            "@type": "dcat:Dataset",
+            "temporal": "2020-01-22/2023-05-10",
+            "modified": "2025-01-13",
+            "references": [
+                "https://data.cdc.gov/Public-Health-Surveillance/Weekly-COVID-19-County-Level-of-Community-Transmis/jgk8-6dpn"
+            ],
+            "keyword": [
+                "case",
+                "community transmission",
+                "coronavirus",
+                "county",
+                "covid-19",
+                "laboratory"
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
+            "identifier": "https://data.cdc.gov/api/views/dt66-w6m6",
+            "description": "Reporting of Aggregate Case and Death Count data was discontinued May 11, 2023, with the expiration of the COVID-19 public health emergency declaration. Although these data will continue to be publicly available, this dataset will no longer be updated.\n\nWeekly COVID-19 Community Levels (CCLs) have been replaced with levels of COVID-19 hospital admission rates (low, medium, or high) which demonstrate <a href=\"https://www.cdc.gov/mmwr/volumes/72/wr/mm7219e1.htm\">>99% concordance</a> by county during February 2022\u2013March 2023. For more information on the latest COVID-19 status levels in your area and hospital admission rates, visit <a href=\"https://covid.cdc.gov/covid-data-tracker/#cases_new-admissions-rate-county\">United States COVID-19 Hospitalizations, Deaths, and Emergency Visits by Geographic Area.</a>\n\nThis archived public use dataset contains historical case and percent positivity data updated weekly for all available counties and jurisdictions. Each week, the dataset was refreshed to capture any historical updates. Please note, percent positivity data may be incomplete for the most recent time period.\n\nThis archived public use dataset contains weekly community transmission levels data for all available counties and jurisdictions since October 20, 2022. The dataset was appended to contain the most recent week's data as originally posted on COVID Data Tracker. Historical corrections are not made to these data if new case or testing information become available. A separate archived file is made available here (<a href=\"https://data.cdc.gov/Public-Health-Surveillance/Weekly-COVID-19-County-Level-of-Community-Transmis/jgk8-6dpn\">: Weekly COVID-19 County Level of Community Transmission Historical Changes</a>) if historically updated data are desired.\n\n<b>Related data</b> \nCDC provides the public with two active versions of COVID-19 county-level community transmission level data: this dataset with the levels as originally posted (<a href=\"https://data.cdc.gov/Public-Health-Surveillance/Weekly-COVID-19-County-Level-of-Community-Transmis/dt66-w6m6\">Weekly Originally Posted dataset</a>), updated weekly with the most recent week\u2019s data since October 20, 2022, and a historical dataset with the county-level transmission data from January 22, 2020 (<a href=\"https://data.cdc.gov/Public-Health-Surveillance/Weekly-COVID-19-County-Level-of-Community-Transmis/jgk8-6dpn\">Weekly Historical Changes dataset</a>).  \n \n<b>Methods for calculating county level of community transmission indicator</b> \nThe County Level of Community Transmission indicator uses two metrics: (1) total new COVID-19 cases per 100,000 persons in the last 7 days and (2) percentage of positive SARS-CoV-2 diagnostic nucleic acid amplification tests (NAAT) in the last 7 days. For each of these metrics, CDC classifies transmission values as low, moderate, substantial, or high (below and\u202f<a href=\"https://www.cdc.gov/mmwr/volumes/70/wr/mm7030e2.htm?s_cid=mm7030e2_w#T1_down\">here</a>). If the values for each of these two metrics differ (e.g., one indicates moderate and the other low), then the higher of the two should be used for decision-making. \n \n<b>CDC core metrics of and thresholds for community transmission levels of SARS-CoV-2</b>\n<b>Total New Case Rate Metric:</b> \"New cases per 100,000 persons in the past 7 days\" is calculated by adding the number of new cases in the county (or other administrative level) in the last 7 days divided by the population in the county (or other administrative level) and multiplying by 100,000. \"New cases per 100,000 persons in the past 7 days\" is considered to have a transmission level of Low (0-9.99); Moderate (10.00-49.99); Substantial (50.00-99.99); and High (greater than or equal to 100.00). \n \n<b>Test Percent Positivity Metric:</b> \"Percentage of positive NAAT in the past 7 days\" is calculated by dividing the number of positive tests in the county (or other administrative level) during the last 7 days by the total number of tests conducted",
+            "title": "Weekly COVID-19 County Level of Community Transmission as Originally Posted - ARCHIVED",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dt66-w6m6/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dt66-w6m6/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dt66-w6m6/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/dt66-w6m6/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "US",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "No longer updated (dataset archived)",
+            "theme": [
+                "Public Health Surveillance"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/hus",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-08-05",
+            "temporal": "1983/2021",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-08",
+            "keyword": [
+                "american indian and alaska native",
+                "asian",
+                "asian or pacific islander",
+                "black",
+                "bridged race",
+                "central and south american",
+                "cuban",
+                "health us",
+                "hispanic",
+                "infant deaths",
+                "infant mortality",
+                "linked birth infant death data set",
+                "mexican",
+                "mortality rates",
+                "national vital statistics system",
+                "native hawaiian or pacific islander",
+                "neonatal deaths",
+                "neonatal mortality",
+                "non-hispanic",
+                "nvss",
+                "postneonatal deaths",
+                "postneonatal mortality",
+                "puerto rican",
+                "race and hispanic origin of mother",
+                "single race",
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
+            "identifier": "https://data.cdc.gov/api/views/m7w3-utaq",
+            "description": "Data on infant, neonatal, and postneonatal mortality rates in the United States, by detailed race and Hispanic origin of mother. Data are from Health, United States. Source: National Center for Health Statistics, National Vital Statistics System, Linked Birth/Infant Death Data Set.\nSearch, visualize, and download these and other estimates from over 120 health topics with the NCHS Data Query System (DQS), available from: https://www.cdc.gov/nchs/dataquery/index.htm.",
+            "title": "DQS Infant, neonatal, and postneonatal mortality rates, by detailed race and Hispanic origin of mother: United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/m7w3-utaq/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/m7w3-utaq/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/m7w3-utaq/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/m7w3-utaq/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/qsk4-8yy5",
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
+                "tularemia",
+                "vancomycin-intermediate staphylococcus aureus",
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
+            "identifier": "https://data.cdc.gov/api/views/qsk4-8yy5",
+            "description": "NNDSS - TABLE 1JJ. Tularemia to  Vancomycin-intermediate Staphylococcus aureus - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1JJ. Tularemia to  Vancomycin-intermediate Staphylococcus aureus",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qsk4-8yy5/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qsk4-8yy5/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qsk4-8yy5/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/qsk4-8yy5/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/g653-rqe2",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-06-25",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-22",
+            "keyword": [
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
+            "identifier": "https://data.cdc.gov/api/views/g653-rqe2",
+            "description": "This dataset provides a complete time history of SARS-CoV-2 concentrations in wastewater for each sampling location.",
+            "title": "NWSS Public SARS-CoV-2 Concentration in Wastewater Data",
+            "programCode": [
+                "009:028"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/g653-rqe2/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/g653-rqe2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/g653-rqe2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/g653-rqe2/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.niagads.org/",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2016-07-15",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "national-institutes-of-health-nih"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Miller, Marilyn",
+                "hasEmail": "mailto:millerm@nia.nih.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH)"
+            },
+            "identifier": "a08ab7e7-d870-4d8a-aaa1-7ebe7ca7a0ce",
+            "description": "<p>The National Institute on Aging Genetics of Alzheimer's Disease Data Storage Site (NIAGADS) is a national genetics data repository facilitating access to genotypic and phenotypic data for Alzheimer's disease (AD). Data include GWAS, whole genome (WGS) and whole exome (WES), expression, RNA Seq, and CHIP Seq analyses. Data for the Alzheimer\u2019s Disease Sequencing Project (ADSP) are available through a partnership with dbGaP (ADSP at dbGaP). Results are integrated and annotated in the searchable genomics database that also provides access to a variety of software packages, analytic pipelines, online resources, and web-based tools to facilitate analysis and interpretation of large-scale genomic data. Data are available as defined by the NIA Genomics of Alzheimer\u2019s Disease Sharing Policy and the NIH Genomics Data Sharing Policy. Investigators return secondary analysis data to the database in keeping with the NIAGADS Data Distribution Agreement.</p>",
+            "title": "The National Institute on Aging Genetics of Alzheimer\u2019s Disease Data Storage Site (NIAGADS)\u00a0",
+            "programCode": [
+                "009:044"
+            ],
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "theme": [
+                "Health"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfcfr/cfrsearch.cfm",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2013-04-01",
+            "keyword": [
+                "cdrh",
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
+            "identifier": "f1b5d989-b06e-46b6-a992-4b753912656b",
+            "description": "This database contains the most recent revision from the Government Printing Office (GPO) of the Code of Federal Regulations (CFR) Title 21 - Food and Drugs.",
+            "title": "Code of Federal Regulations Title 21",
+            "programCode": [
+                "009:005"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfcfr/cfrsearch.cfm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/nhanes/visualization/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-03-02",
+            "@type": "dcat:Dataset",
+            "temporal": "1999/2018",
+            "modified": "2023-09-08",
+            "keyword": [
+                "chronic conditions"
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
+            "identifier": "https://data.cdc.gov/api/views/i667-sjhg",
+            "description": "These data represent prevalence estimates of select chronic conditions from the National Health and Nutrition Examination Survey (NHANES).",
+            "title": "NHANES Select Chronic Conditions Prevalence Estimates",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/i667-sjhg/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/i667-sjhg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/i667-sjhg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/i667-sjhg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "U.S.",
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
+            "landingPage": "https://data.cdc.gov/d/5y75-rs75",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-14",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "National Personal Protective Technology Laboratory, Research Branch",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/5y75-rs75",
+            "description": "Filtering facepiece respirators (FFRs) and elastomeric half-mask respirators (EHRs) are commonly used by workers for protection against potentially hazardous particles, including engineered nanoparticles (i.e., particles measuring less than 100 nanometers (nm). The purpose of this study was to evaluate the performance of these types of respirators against 10-400 nm particles using human subjects exposed to NaCl aerosols under simulated workplace activities. Simulated workplace protection factors (SWPFs) were measured for eight combinations of respirator models (2 N95 FFRs, 2 P100 FFRs, 2 N95 EHRs, and 2 P100 EHRs) worn by 25 healthy test subjects (13 females and 12 males) with varying face sizes. Before beginning a SWPF test for a given respirator model, each subject had to pass a quantitative fit test. Each SWPF test was performed using a protocol of six exercises for three minutes each: (i) normal breathing, (ii) deep breathing, (iii) moving head side to side, (iv) moving head up and down, (v) bending at th",
+            "title": "Respirator Performance against Nanoparticles under Simulated Workplace Activities Data",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/5y75-rs75/application/x-zip-compressed",
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
+            "landingPage": "https://www.cdc.gov/nchs/covid19/pulse/mental-health.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2020-05-20",
+            "@type": "dcat:Dataset",
+            "temporal": "2020-08-19/2024-09-16",
+            "modified": "2024-10-04",
+            "keyword": [
+                "anxiety",
+                "covid-19",
+                "depression"
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
+            "identifier": "https://data.cdc.gov/api/views/8pt5-q6wp",
+            "description": "The U.S. Census Bureau, in collaboration with five federal agencies, launched the Household Pulse Survey to produce data on the social and economic impacts of Covid-19 on American households.  The Household Pulse Survey was designed to gauge the impact of the pandemic on employment status, consumer spending, food security, housing, education disruptions, and dimensions of physical and mental wellness.\n\nThe survey was designed to meet the goal of accurate and timely weekly estimates. It was conducted by an internet questionnaire, with invitations to participate sent by email and text message. The sample frame is the Census Bureau Master Address File Data. Housing units linked to one or more email addresses or cell phone numbers were randomly selected to participate, and one respondent from each housing unit was selected to respond for him or herself. Estimates are weighted to adjust for nonresponse and to match Census Bureau estimates of the population by age, gender, race and ethnicity, and educational attainment. All estimates shown meet the NCHS Data Presentation Standards for Proportions,",
+            "title": "Indicators of Anxiety or Depression Based on Reported Frequency of Symptoms During Last 7 Days",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8pt5-q6wp/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8pt5-q6wp/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8pt5-q6wp/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8pt5-q6wp/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "US",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P2W",
+            "theme": [
+                "NCHS"
+            ],
+            "language": [
+                "en-US"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/dataset/national-foster-care-and-adoption-directory",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2012-05-30",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "children's health",
+                "department-of-health-human-services"
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
+            "identifier": "a2f65cfc-17bf-4314-85c4-883a53034b0d",
+            "description": "<p>The National Foster Care &amp; Adoption Directory (formerly the National Adoption Directory) offers adoption and foster care resources by State.</p>",
+            "title": "National Foster Care and Adoption Directory",
+            "programCode": [
+                "009:103"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.childwelfare.gov",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/",
+            "dataQuality": true
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.fda.gov/Drugs/DrugSafety/DrugShortages/ucm050794.htm",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2025-01-29",
+            "@type": "dcat:Dataset",
+            "modified": "2013-09-26",
+            "keyword": [
+                "cder",
+                "discontinued drugs"
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
+            "identifier": "6e72c239-0510-49f4-8404-d3d7d50351ec",
+            "description": "Companies are required under Section 506C of the Federal Food, Drug, and Cosmetic Act (FD&C Act) (as amended by the Food and Drug Administration Safety and Innovation Act) to notify FDA of a permanent discontinuance of certain drug products, six months in advance, or if that is not possible, as soon as practicable. These drugs include those that are life-supporting, life-sustaining or for use in the prevention or treatment of a debilitating disease or condition, including any such drug used in emergency medical care or during surgery). The discontinuations provided below reflect information received from manufacturers, and are for informational purposes only.",
+            "title": "Drugs to be Discontinued",
+            "programCode": [
+                "009:002"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fda.gov/Drugs/DrugSafety/DrugShortages/ucm050794.htm",
+                    "mediaType": "application/unknown"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/xr2u-sbqf",
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
+            "identifier": "9701e19c-7e6f-51f4-95cd-4ce1d568e93f",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "implAuto_measure_compare_download",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/measure_compare_download.csv",
+                    "description": "{\"dataset\": \"measure_compare_download\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
+                    "@type": "dcat:Distribution",
+                    "title": "measure_compare_download csv file"
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
+            "landingPage": "https://healthdata.gov/d/xr6g-9z88",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2015-02-03",
+            "keyword": [
+                "constituents",
+                "harmful",
+                "hphc"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Danny Hsu",
+                "hasEmail": "mailto:danny.hsu@fda.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "U.S. Food and Drug Administration"
+            },
+            "identifier": "96E5B59F-286A-4127-A6E1-82EBA4981EFF",
+            "description": "The FDA shall publish in a format that is understandable and not misleading to a lay person, and place on public display, a list of 93 harmful and potentially harmful constituents in each tobacco product and smoke established under section 904(e) of the TCA.  CTP has determined the best means to display the data is web-based on FDA.GOV.  The HPHC back-end database and template for industry will be created in a future release of eSubmissions.  The scope of this project is to: Phase 1 (Current POP): 1) build a website to support the display of the HPHC constituents, 2) allow the user to access educational information about the health effects of the chemicals; Phase 2 (next POP):  1) allow users of the website to perform a search by brand and sub-brand, 2) display a report on the HPHCs contained in that tobacco product, and 3) create an admin module to allow for an import of HPHC data via an Excel spreadsheet and to update the list of constituents.",
+            "title": "Harmful and Potentially Harmful Constituents",
+            "programCode": [
+                "009:007"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fda.gov/TobaccoProducts/GuidanceComplianceRegulatoryInformation/ucm297786.htm",
+                    "mediaType": "text/html",
+                    "description": "Website is still under development, not yet published to the public. Pre-Production L is: http://accessdata-preprod.fda.gov/scripts/hphc/"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://ncbi.github.io/cxx-toolkit/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-08-26",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "computational biology",
+                "software"
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/x3vz-qq3q",
+            "description": "Provides an overview of the C++ language with a focus on its use in accessing resources of the National Center for Biotechnology Information at the National Library of Medicine, National Institutes of Health.",
+            "title": "NCBI C++ Toolkit Book",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://ncbi.github.io/cxx-toolkit/",
+                    "mediaType": "text/html",
+                    "title": "The NCBI C++ Toolkit Book"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Other"
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
+            "modified": "2024-04-09",
+            "references": [
+                "https://www.cdc.gov/dhdsp/index.htm",
+                "https://www.cdc.gov/dhdsp/maps/dtm/data_sources.htm",
+                "https://www.cdc.gov/dhdsp/maps/dtm/data_risks.htm"
+            ],
+            "keyword": [
+                "cardiovascular disease",
+                "coronary heart disease",
+                "diseases of the heart",
+                "mortality",
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
+            "identifier": "https://data.cdc.gov/api/views/kztq-p2jf",
+            "description": "2000\u20132020. NVSS is a secure, web-based data management system that collects and disseminates the Nation's official vital statistics. Indicators from this data source have been computed by personnel in CDC's Division for Heart Disease and Stroke Prevention (DHDSP). This was one of the datasets provided by the National Cardiovascular Disease Surveillance System and presented on DHDSP\u2019s Data, Trends, and Maps online tool. This tool was retired in April of 2024 and this dataset will not be updated. Contact dhdsprequests@cdc.gov if you need assistance with data previously included in this dataset. The data are organized by location (national and state) and indicator; NVSS mortality data include CVDs (e.g., heart failure). The data can be viewed by temporal trends and stratified by age group, sex, and race/ethnicity.",
+            "title": "National Vital Statistics System (NVSS) - National Cardiovascular Disease Surveillance Data",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kztq-p2jf/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kztq-p2jf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kztq-p2jf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kztq-p2jf/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Heart-Disease-Stroke-Prevention/National-Vital-Statistics-System-NVSS-National-Car/kztq-p2jf",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Heart Disease & Stroke Prevention"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.nlm.nih.gov/research/umls/Snomed/nursing_terminology_resources.html",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2022-03-01",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "health data standards",
+                "nursing",
+                "population groups",
+                "reference",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/3ymh-phhi",
+            "description": "A nursing terminologies resource for systems development. Describes the role of SNOMED CT and Laboratory Observation Identifiers Names and Codes (LOINC) in implementing Meaningful Use in the U.S., specifically for the nursing and care domain.",
+            "title": "Nursing Resources for Standards and Interoperability",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.nlm.nih.gov/research/umls/Snomed/nursing_terminology_resources.html",
+                    "mediaType": "text/html",
+                    "title": "Nursing Resources for Standards and Interoperability"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Terminology"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/kxvg-q6s7",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-01-14",
+            "@type": "dcat:Dataset",
+            "modified": "2022-02-11",
+            "keyword": [
+                "2022",
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
+            "identifier": "https://data.cdc.gov/api/views/kxvg-q6s7",
+            "description": "NNDSS - TABLE 1Y. Mumps to Novel influenza A virus infections - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
+            "title": "NNDSS - TABLE 1Y. Mumps to Novel influenza A virus infections",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kxvg-q6s7/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kxvg-q6s7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kxvg-q6s7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kxvg-q6s7/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/nchs/nvss/vsrr/covid19/excess_deaths.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2020-05-28",
+            "@type": "dcat:Dataset",
+            "modified": "2023-09-27",
+            "keyword": [
+                "age",
+                "age group",
+                "all causes",
+                "deaths",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "puerto rico",
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
+            "identifier": "https://data.cdc.gov/api/views/y5bj-9g5w",
+            "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nThis visualization provides weekly data on the number of deaths from all causes by jurisdiction of occurrence and age group. Counts of deaths in more recent weeks can be compared with counts from earlier years to determine if the number is higher than expected.",
+            "title": "Weekly Counts of Deaths by Jurisdiction and Age",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/y5bj-9g5w/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/y5bj-9g5w/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/y5bj-9g5w/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/y5bj-9g5w/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpma/pmamemos.cfm",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
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
+            "identifier": "8dabbf7e-0e4a-4e1c-a0d2-982d97398a10",
+            "description": "A 180-day supplement is a request for a significant change in components, materials, design, specification, software, color additive, and labeling to an approved premarket application or premarket report. As a pilot program under the CDRH Transparency Initiative, FDA has begun releasing some summary review memos for 180-day PMA supplements relating to design changes.",
+            "title": "Premarket Approval (PMA) Summary Review Memos for 180-Day Design Changes",
+            "programCode": [
+                "009:005"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfpma/pmamemos.cfm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P1W"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/xu6x-dfcx",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2024-08-06",
+            "@type": "dcat:Dataset",
+            "modified": "2024-08-14",
+            "keyword": [
+                "business rules",
+                "exchange puf",
+                "marketplace puf",
+                "py2024"
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
+            "identifier": "0063b2e0-f674-4c04-91a4-380d71f613ee",
+            "description": "The Business Rules PUF (BR-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The BR-PUF contains plan-level data on rating business rules, such as maximum age for a dependent and allowed dependent relationships.",
+            "title": "Business Rules PUF - PY2024",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2024/business_rules_PUF.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/summary-statistics-on-use-and-payments/medicare-medicaid-service-type-reports/cms-program-statistics-medicare-part-d",
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
+                "health care use & payments",
+                "health equity",
+                "medicare",
+                "medicare prescription drug",
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/f28a5c57-b4b2-4a3b-8c0e-18ab67c4d59b/data-viewer",
+            "description": "The CMS Program Statistics -\u00a0Medicare Part D tables provide use and Part D drug costs by type of Part D plan (stand-alone prescription drug plan and Medicare Advantage prescription drug plan).\u00a0\n\nFor additional information on enrollment, providers, and Medicare use and payment, visit the\u00a0CMS Program Statistics\u00a0page.\n\nThese data do not exist in a machine-readable format, so the view data and API options are not available. Please use the download function to access the data.\n\n\u00a0\n\nBelow is the list of tables:\n\nMDCR UTLZN D 1. \u00a0Medicare Part D Utilization: \u00a0Average Annual Prescription Drug Fills\u00a0by Type of Plan, Low Income Subsidy (LIS) Eligibility, and Generic Dispensing Rate,\u00a0Yearly Trend\n\tMDCR UTLZN D 2. \u00a0Medicare Part D Utilization: \u00a0Average Annual Gross Drug Costs Per Part D Enrollee, by Type of Plan, Low Income Subsidy (LIS) Eligibility, and Brand/Generic Drug Classification, Yearly Trend\n\tMDCR UTLZN D 3. \u00a0Medicare Part D Utilization: \u00a0Average Annual Gross Drug Costs Per Part D Enrollee, by Type of Plan, Low Income Subsidy (LIS) Eligibility, and Brand/Generic Drug Classification, Yearly Trend\n\tMDCR UTLZN D 4. \u00a0Medicare Part D Utilization: \u00a0Average Annual Prescription Drug Fills\u00a0and Average Annual Gross Drug Cost Per Part D Enrollee, by Type of Plan and Demographic Characteristics\n\tMDCR UTLZN D 5. \u00a0Medicare Part D Utilization: \u00a0Average Annual Prescription Drug Fills\u00a0and Average Annual Gross Drug Cost Per Part D Utilizer, by Type of Plan and Demographic Characteristics\n\tMDCR UTLZN D 6. \u00a0Medicare Part D Utilization: \u00a0Average Annual Prescription Drug Fills\u00a0and Average Annual Gross Drug Cost Per Part D Enrollee, by Type of Plan, by Area of Residence\n\tMDCR UTLZN D 7. \u00a0Medicare Part D Utilization: \u00a0Average Annual Prescription Drug Fills\u00a0and Average Annual Gross Drug Cost Per Part D Utilizer, by Type of Plan, by Area of Residence\n\tMDCR UTLZN D 8. \u00a0Medicare Part D Utilization: \u00a0Number of Part D Utilizers and Average Annual Prescription Drug Fills\u00a0by Type of Part D Plan, Low Income Subsidy (LIS) Eligibility, and Part D Coverage Phase, Yearly Trend\n\tMDCR UTLZN D 9. \u00a0Medicare Part D Utilization:\u00a0\u00a0Number of Part D Utilizers and Drug Costs by Type of Part D Plan, Low Income Subsidy (LIS) Eligibility, and Part D Coverage Phase, Yearly Trend\n\tMDCR UTLZN D 10. \u00a0Medicare Part D Utilization: \u00a0Number of Part D Utilizers, Average Annual Prescription Drug Events (Fills)\u00a0and Average Annual Gross Drug Cost Per Part D Utilizer, by Part D Coverage Phase and Demographic Characteristics\n\tMDCR UTLZN D 11. \u00a0Medicare Part D Utilization: \u00a0Number of Part D Utilizers, Average Annual Prescription Drug Fills\u00a0and Average Annual Gross Drug Cost Per Part D Utilizer, by Part D Coverage Phase and Area of Residence",
+            "title": "CMS Program Statistics - Medicare Part D",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-02/CPS%20MDCR%20UTLZN%20D%202021.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Part D : 2021-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2022-02/CPS%20MDCR%20UTLZN%20D%202020.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Part D : 2020-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-05/CPS_MDCR_UTLZN_D_ALL.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Part D : 2019-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-05/CPS_MDCR_UTLZN_D_ALL_0.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Part D : 2018-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-05/CPS_MDCR_UTLZN_D_ALL_1.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Part D : 2017-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-05/CPS_MDCR_UTLZN_D_ALL_2.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Part D : 2016-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-05/CPS_MDCR_UTLZN_D_ALL_3.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Part D : 2015-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-05/CPS_MDCR_UTLZN_D_ALL_4.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Part D : 2014-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2021-05/CPS_MDCR_UTLZN_D_ALL_5.zip",
+                    "mediaType": "application/zip",
+                    "title": "CMS Program Statistics - Medicare Part D : 2013-12-31"
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
+            "landingPage": "https://data.cdc.gov/d/89qs-mr7i",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-11-21",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-13",
+            "keyword": [
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "demographics",
+                "mortality"
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
+            "identifier": "https://data.cdc.gov/api/views/89qs-mr7i",
+            "description": "Monthly COVID-19 death rates per 100,000 population stratified by age group, race/ethnicity, sex, and region",
+            "title": "Monthly COVID-19 Death Rates per 100,000 Population by Age Group, Race and Ethnicity, Sex, and Region",
+            "programCode": [
+                "009:026"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/89qs-mr7i/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/89qs-mr7i/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/89qs-mr7i/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/89qs-mr7i/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/jk8p-fqhn",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-02-17",
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
+            "identifier": "https://data.cdc.gov/api/views/jk8p-fqhn",
+            "description": "<p style=\"margin:0in;vertical-align:baseline;\"><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>This site provides historical data related to COVID-19 booster dose eligibility presented on two CDC COVID Data Tracker sites:&nbsp;</span><a href=\"https://covid.cdc.gov/covid-data-tracker/#vaccinations\"><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>Vaccinations in the US</span></a><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>&nbsp;and&nbsp;</span><a href=\"https://covid.cdc.gov/covid-data-tracker/#vaccination-equity\"><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>Vaccination Equity</span></a><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>.&nbsp;</span><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>&nbsp;</span><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>Data are updated weekly on Thursdays.</span></p><p style=\"margin:0in;vertical-align:baseline;\"><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>Some COVID-19 vaccine recipients are&nbsp;</span><a href=\"https://www.cdc.gov/coronavirus/2019-ncov/vaccines/booster-shot.html\" target=\"_blank\"><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>eligible to receive booster doses</span></a><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>,&nbsp;</span><span style=\"font-size:11px;\">&nbsp;</span><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>and criteria for booster eligibility may change over time. Data and footnotes will be updated to align with the current recommendations.&nbsp;</span><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>&nbsp;</span></p><p style=\"margin:0in;vertical-align:baseline;\"><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>CDC counts people as having &ldquo;received a booster dose&rdquo; if they are fully vaccinated and received another dose of any COVID-19 vaccine on or after August 13, 2021. This does not distinguish whether the recipient is&nbsp;</span><a href=\"https://www.cdc.gov/coronavirus/2019-ncov/vaccines/recommendations/immuno.html\" target=\"_blank\"><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>immunocompromised and received an additional dose</span></a></p><p style=\"margin:0in;vertical-align:baseline;\"><strong><em><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>Data Limitations:</span></em></strong><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:black;'>&nbsp;</span></p><ul style=\"list-style-type: undefined;margin-left:0in;\"><li><span style='font-family:\"Calibri\",sans-serif;color:black;font-size:11.0pt;color:black;'>The booster eligibility metric excludes fully vaccinated recipients who have an &ldquo;Other&rdquo; primary series vaccine type.\u202f</span><span style='font-family:\"Calibri\",sans-serif;font-size:11.0pt;color:black;'>&nbsp;</span></li><li><span style='font-family:\"Calibri\",sans-serif;color:black;font-size:11.0pt;color:black;'>Booster eligibility counts and percentages exclude vaccine administrations reported by Texas as the primary series cannot be linked to booster dose in the aggregate data submitted by Texas.</span><span style='font-family:\"Calibri\",sans-serif;font-size:11.0pt;color:black;'>&nbsp;</span></li></ul><p style=\"margin:0in;vertical-align:baseline;\"><strong><em><span style='font-size:15px;font-family:\"Calibri\",sans-serif;'>Footnotes:</span></em></strong></p><p style=\"margin:0in;vertical-align:baseline;\"><span style='font-size:15px;font-family:\"Calibri\",sans-serif;'>CDC counts people as being &ldquo;</span><a href=\"https://www.cdc.gov/coronavirus/2019-ncov/vaccines/booster-shot.html\" target=\"_blank\"><span style='font-size:15px;font-family:\"Calibri\",sans-serif;color:windowtext;'>eligible to get a booster dose</span></a><",
+            "title": "COVID-19 Booster Dose Eligibility in the United States",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/jk8p-fqhn/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/jk8p-fqhn/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/jk8p-fqhn/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/jk8p-fqhn/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/pp7x-dyj2",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2016-10-13",
+            "@type": "dcat:Dataset",
+            "modified": "2019-04-05",
+            "keyword": [
+                "mortality",
+                "nchs"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Krista Kniss",
+                "hasEmail": "mailto:krk9@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/pp7x-dyj2",
+            "description": "",
+            "title": "Deaths from Pneumonia and Influenza (P&I) and all deaths, by state and region, National Center For Health Statistics Mortality Surveillance System",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pp7x-dyj2/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pp7x-dyj2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pp7x-dyj2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pp7x-dyj2/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/3crz-97tw",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-09-26",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-09",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DCPC Communications (CDC)",
+                "hasEmail": "mailto:dcpccommunications@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/3crz-97tw",
+            "description": "This database of cancer-related citations for publications authored by CDC\u2019s Division of Cancer Prevention and Control (DCPC) staff, fosters collaboration among scientists throughout the world. Allows for searching for links to scientific articles authored or co-authored by researchers from DCPC since 2000.",
+            "title": "Cancer Research Citation Search",
+            "programCode": [
+                "009:029"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3crz-97tw/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3crz-97tw/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3crz-97tw/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/3crz-97tw/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Cancer Research Citation Search"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/xvzi-6ads",
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
+            "identifier": "1109e8a3-8da6-581a-9241-52938b196807",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "CoreSet measure v2.10.64 (coreset-impl)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/measure.csv",
+                    "description": "CoreSet measure v2.10.64 (coreset-impl)",
+                    "@type": "dcat:Distribution",
+                    "title": "CoreSet measure v2.10.64 (coreset-impl)"
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
+            "landingPage": "https://data.cdc.gov/d/fip8-rcng",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2015-02-02",
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
+            "identifier": "https://data.cdc.gov/api/views/fip8-rcng",
+            "description": "Download the latest version of the Glossary and Methodology File",
+            "title": "The Tax Burden on Tobacco Glossary and Methodology",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/fip8-rcng/application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
+                    "mediaType": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Policy"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/hbbg-vj7f",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-01-21",
+            "@type": "dcat:Dataset",
+            "modified": "2022-01-12",
+            "keyword": [
+                "2021",
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
+            "identifier": "https://data.cdc.gov/api/views/hbbg-vj7f",
+            "description": "NNDSS - TABLE 1W. Meningococcal disease, All serogroups to Meningococcal disease, Serogroup B - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1W. Meningococcal disease, All serogroups to Meningococcal disease, Serogroup B",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hbbg-vj7f/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hbbg-vj7f/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hbbg-vj7f/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hbbg-vj7f/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/c75w-3h6e",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-12-02",
+            "@type": "dcat:Dataset",
+            "modified": "2024-12-02",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Health Effects Laboratory Division (HELD)",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/c75w-3h6e",
+            "description": "Trace measurement of aerosol chemical composition in workplace atmospheres requires the development of high-throughput aerosol collectors that are compact, hand-portable, and can be operated using personal pumps. We describe the design and characterization of a compact, high flow, Turbulent-mixing Condensation Aerosol-in-Liquid Concentrator (TCALC) that allows direct collection of aerosols as liquid suspensions, for off-line chemical, biological, or microscopy analysis. The TCALC unit, measuring approximately 12 \u00d7 16 \u00d7 18 cm, operates at an aerosol sample flowrate of up to 10 L min-1, using rapid mixing of a hot flow saturated with water vapor and a cold aerosol sample flow, thereby promoting condensational growth of aerosol particles. We investigated the effect of operating parameters such as vapor temperature, growth tube wall temperature, and aerosol sample flowrate, along with the effect of particle diameter, inlet humidity, aerosol concentration, and operation time on TCALC performance. Nanoparticles with an initial aerodynamic diameter \u2265 25 nm could grow to droplet diameters > 1400 nm with an efficiency \u2265 80%. Good droplet growth efficiency was achieved for sampled aerosol relative humidity \u2265 9%. We measured complete aerosol collection for concentrations of \u2264 3\u00d7105 cm-3. The results showed good agreement between the particulate mass collected through the liquid collector and direct filter collection. The TCALC eliminates the need for sample preparation and filter digestion during chemical analysis, thereby increasing sample recovery and substantially improving the limit of detection and sensitivity of off-line trace analysis of collected liquid samples.",
+            "title": "A High-throughput, Turbulent-mixing, Condensation Aerosol Concentrator for Direct Aerosol Collection as a Liquid Suspension",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/c75w-3h6e/application/x-zip-compressed",
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
+            "landingPage": "https://healthdata.gov/d/xz2b-xd8b",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2025-01-01",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-28",
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
+            "identifier": "f38d0706-1239-442c-a3cc-40ef1b686ac0",
+            "description": "National Average Drug Acquisition Cost (NADAC) weekly reference data for the calendar year.",
+            "title": "NADAC (National Average Drug Acquisition Cost) 2025",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/nadac-national-average-drug-acquisition-cost-01-29-2025.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Drug Pricing and Payment",
+                "National Average Drug Acquisition Cost"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/hospital-price-transparency-enforcement-activities-and-outcomes",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2024-03-05",
+            "temporal": "2023-10-01/2024-09-30",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-17",
+            "references": [
+                "https://data.cms.gov/resources/hospital-price-transparency-enforcement-activities-and-outcomes-methodology"
+            ],
+            "keyword": [
+                "health care use & payments",
+                "hospitals & facilities",
+                "medicare"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Price Transparency - CM",
+                "hasEmail": "mailto:Pricetransparencyhospitalcharges@cms.hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Medicare & Medicaid Services"
+            },
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/6a3aa708-3c9d-411a-a1a4-e046d3ade7ef/data-viewer",
+            "description": "The Hospital Price Transparency Enforcement Activities and Outcomes dataset contains information related to enforcement actions taken by CMS following a compliance review of a hospital's obligation to establish, update and make public a list of the hospital\u2019s standard charges for items and services provided by the hospital, in accordance with regulation (45 CFR 180). This data set includes the name of each hospital or hospital location, the hospital or hospital location address, the outcome or action following a CMS compliance review and the date of the outcome or action taken.",
+            "title": "Hospital Price Transparency Enforcement Activities and Outcomes",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6a3aa708-3c9d-411a-a1a4-e046d3ade7ef/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Hospital Price Transparency Enforcement Activities and Outcomes : 2024-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/27ffe107-0534-4c22-8a99-3c7e7e8faf56/Hospital_Price_Transparency_Enforcement_Activities_and_Outcomes_Q3_2024.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Price Transparency Enforcement Activities and Outcomes : 2024-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6a5a1ca0-14ba-4b12-86be-0fa535209e74/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Price Transparency Enforcement Activities and Outcomes : 2024-09-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-08/e58a6aec-e0f7-4570-afd2-8352f4f73049/Q2%20CY2024%20HPT%20Enforcement%20Actions.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Price Transparency Enforcement Activities and Outcomes : 2024-06-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/a077c403-59c0-4cf0-87ed-37f5527e3075/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Price Transparency Enforcement Activities and Outcomes : 2024-06-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-03/94aa0667-7a1d-4136-9943-26d0caadd691/Issued%20Compliance%20Actions%20Jan%2021%20to%20Dec%2023%20Closed%20Cases.csv",
+                    "mediaType": "text/csv",
+                    "title": "Hospital Price Transparency Enforcement Activities and Outcomes : 2023-12-31"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/8f815d76-c741-4a99-92ad-280ab2d2dceb/data",
+                    "mediaType": "text/html",
+                    "title": "Hospital Price Transparency Enforcement Activities and Outcomes : 2023-12-31"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/hospital-price-transparency-enforcement-activities-and-outcomes-data-dictionary",
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
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/national-survey-substance-abuse-treatment-services-n-ssats-2002",
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
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2002-nid13585",
+            "description": "<p>The National Survey of Substance Abuse Treatment Services (N-SSATS) is designed to collect information from all facilities in the United States, both public and private, that provide substance abuse treatment. N-SSATS provides the mechanism for quantifying the dynamic character and composition of the United States substance abuse treatment delivery system. The objectives of N-SSATS are to collect multipurpose data that can be used to assist the Substance Abuse and Mental Health Services Administration (SAMHSA) and state and local governments in assessing the nature and extent of services provided and in forecasting treatment resource requirements, update SAMHSA's Inventory of Substance Abuse Treatment Services (I-SATS), analyze general treatment services trends, and generate the National Directory of Drug and Alcohol Abuse Treatment Programs and its online equivalent, the Substance Abuse Treatment Facility Locator <a href=\"http://findtreatment.samhsa.gov\">http://findtreatment.samhsa.gov</a>.<br />\nData are collected on topics including facility operation, services offered (assessment, substance abuse therapy and counseling, pharmacotherapies, testing, transitional, ancillary), primary focus (substance abuse, mental health, both, general health, other), hotline operation, Opioid Treatment Programs and medication dispensed, languages in which treatment is provided, type of treatment provided, number of clients (total and under age 18), number of beds, types of payment accepted, sliding fee scale, special programs offered, facility accreditation and licensure/certification, and managed care agreements.This study has 1 Data Set.</p>",
+            "title": "National Survey of Substance Abuse Treatment Services (N-SSATS-2002)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2002-nid13585",
+                    "description": "National Survey of Substance Abuse Treatment Services (N-SSATS-2002) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-substance-abuse-treatment-services-n-ssats-2002-nid13585"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/ype6-idgy",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-10-18",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-15",
+            "references": [
+                "COVID Data Tracker hospital data displays: https://covid.cdc.gov/covid-data-tracker/#hospitalizations-nhsn   NHSN Hospital Data Reporting: COVID-19 Hospital Data Reporting | NHSN | CDC  Full reporting guidance: https://www.hhs.gov/sites/default/files/covid-19-faqs-hospitals-hospital-laboratory-acute-care-facility-data-reporting.pdf"
+            ],
+            "keyword": [
+                "admissions",
+                "coronavirus",
+                "covid-19",
+                "hospital capacity",
+                "hospitalizations",
+                "hospital occupancy",
+                "icu beds",
+                "influenza",
+                "inpatient beds"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DHQP",
+                "hasEmail": "mailto:nhsn@cdc.gov (subject line: weekly NHSN hospital data)"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/ype6-idgy",
+            "description": "<b>Note:</b> \nAfter November 1, 2024, this dataset will no longer be updated due to a transition in NHSN Hospital Respiratory Data reporting that occurred on Friday, November 1, 2024. For more information on NHSN Hospital Respiratory Data reporting, please visit https://www.cdc.gov/nhsn/psc/hospital-respiratory-reporting.html.\n\nDue to a recent update in voluntary NHSN Hospital Respiratory Data reporting that occurred on Wednesday, October 9, 2024, reporting levels and other data displayed on this page may fluctuate week-over-week beginning Friday, October 18, 2024. For more information on NHSN Hospital Respiratory Data reporting, please visit https://www.cdc.gov/nhsn/psc/hospital-respiratory-reporting.html.  Find more information about the updated CMS requirements: https://www.federalregister.gov/documents/2024/08/28/2024-17021/medicare-and-medicaid-programs-and-the-childrens-health-insurance-program-hospital-inpatient.\u202f  \n.\nThis dataset represents weekly respiratory virus-related hospitalization data and metrics aggregated to national and state/territory levels reported during two periods: 1) data for collection dates from August 1, 2020 to April 30, 2024, represent data reported by hospitals during a mandated reporting period as specified by the HHS Secretary; and 2) data for collection dates beginning May 1, 2024, represent data reported voluntarily by hospitals to CDC\u2019s National Healthcare Safety Network (NHSN). NHSN monitors national and local trends in healthcare system stress and capacity for up to approximately 6,000 hospitals in the United States. Data reported represent aggregated counts and include metrics capturing information specific to COVID-19- and influenza-related hospitalizations, hospital occupancy, and hospital capacity. Find more information about reporting to NHSN at: https://www.cdc.gov/nhsn/covid19/hospital-reporting.html\n\n<b>Source: COVID-19 hospitalization data reported to CDC\u2019s National Healthcare Safety Network (NHSN).</b>\n<ul><li><b>Data source description(updated October 18, 2024):</b> As of October 9, 2024, Hospital Respiratory Data (HRD; formerly Respiratory Pathogen, Hospital Capacity, and Supply data or \u2018COVID-19 hospital data\u2019) are reported to HHS through CDC\u2019s National Healthcare Safety Network based on updated requirements from the Centers for Medicare and Medicaid Services (CMS). These data are voluntarily reported to NHSN as of May 1, 2024 until November 1, 2024, at which time CMS will require acute care and critical access hospitals to electronically report information via NHSN about COVID-19, Influenza, and RSV, hospital bed census and capacity, and limited patient demographic information, including age. Data for collection dates prior to May 1, 2024, represent data reported during a previously mandated reporting period as specified by the HHS Secretary. Data for collection dates May 1, 2024, and onwards represent data reported voluntarily to NHSN; as such, data included represents reporting hospitals only for a given week and might not be complete or representative of all hospitals. NHSN monitors national and local trends in healthcare system stress and capacity for approximately 6,000 hospitals in the United States. Data reported by hospitals to NHSN represent aggregated counts and include metrics capturing information specific to hospital capacity, occupancy, hospitalizations, and admissions. Find more information about reporting to NHSN: https://www.cdc.gov/nhsn/psc/hospital-respiratory-reporting.html. Find more information about the updated CMS requirements: https://www.federalregister.gov/documents/2024/08/28/2024-17021/medicare-and-medicaid-programs-and-the-childrens-health-insurance-program-hospital-inpatient.</li><li><b>Data quality:</b> While CDC reviews reported data for completeness and errors and corrects those found, some reporting errors might still exist within the data. CDC and partners work with reporters to correct these errors and update the data in subsequent weeks",
+            "title": "Weekly United States Hospitalization Metrics by Jurisdiction, During Mandatory Reporting Period from August 1, 2020 to April 30, 2024, and for Data Reported Voluntarily Beginning May 1, 2024, National Healthcare Safety Network (NHSN) (Historical)-ARCHIVED",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ype6-idgy/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ype6-idgy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ype6-idgy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ype6-idgy/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "US",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "Weekly",
+            "theme": [
+                "Public Health Surveillance"
+            ],
+            "language": [
+                "English"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/dataset/cdc-wonder-aids-public-use-data",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2012-05-30",
+            "temporal": "1981-01-01T00:00:00-05:00/2002-12-31T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-25",
+            "keyword": [
+                "age",
+                "aids",
+                "case definition",
+                "case report",
+                "date diagnosed",
+                "date reported",
+                "diagnosis",
+                "epidemiology",
+                "ethnicity",
+                "exposure category",
+                "hemophilia",
+                "hiv",
+                "incidence",
+                "iv drug use",
+                "metropolitan area",
+                "msa",
+                "pediatric",
+                "race",
+                "region",
+                "sex",
+                "sexual orientation",
+                "vital status"
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
+            "identifier": "8208b2a4-58bb-460e-b6fc-56ae6e6cd5e2",
+            "description": "<p>The AIDS Public Information Data Set (APIDS) for years 1981-2002 on CDC WONDER online database contains counts of AIDS (Acquired Immune Deficiency Syndrome) cases reported by state and local health departments, by demographics; location (region and selected metropolitan areas); case-definition; month/year and quarter-year of diagnosis, report, and death (if applicable); and HIV exposure group (risk factors for AIDS).  Data are produced by the US Department of Health and Human Services (US DHHS), Public Health Service (PHS), Centers for Disease Control and Prevention (CDC), National Center for HIV, STD and TB Prevention (NCHSTP), Division of HIV/AIDS Prevention (DHP).</p>",
+            "title": "CDC WONDER: AIDS Public Use Data",
+            "programCode": [
+                "009:027"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://wonder.cdc.gov/AIDSPublic.html",
+                    "mediaType": "text/html",
+                    "title": "Query Tool "
+                }
+            ],
+            "describedBy": "http://wonder.cdc.gov/wonder/help/aids.html",
+            "dataQuality": true,
+            "license": "https://opendatacommons.org/licenses/odbl/1.0/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/y3kz-zbmh",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-02-15",
+            "@type": "dcat:Dataset",
+            "modified": "2023-02-13",
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
+            "identifier": "dfaabae9-21bd-4f77-84f6-3bda5806c6f7",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-02-06-to-2023-02-12",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rprt-drug-02062023-to-02122023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-02-06-to-2023-02-12"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "restricted public",
+            "landingPage": "https://www.cdc.gov/nchs/nehrs/about.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information.  Researchers must apply for data access through a proposal process, take confidentiality and sign a data use agreement.  If approved, data access would occur at a NCHS or Federal Statistical Research Data Center.  For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm\u201d",
+            "issued": "2023-09-27",
+            "@type": "dcat:Dataset",
+            "temporal": "2008-2011",
+            "modified": "2023-09-27",
+            "keyword": [
+                "electronic health records",
+                "health us",
+                "nchs",
+                "nehrs",
+                "research-data-center"
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
+            "identifier": "https://data.cdc.gov/api/views/53z7-6asy",
+            "description": "The National Electronic Health Records Survey (NEHRS) is an annual survey of non-federally employed, office-based physicians practicing in the United States (excluding those in the specialties of anesthesiology, radiology, and pathology). NEHRS began in 2008 and was originally designed as an annual mail supplement to the National Ambulatory Medical Care Survey (NAMCS). Prior to 2012, NEHRS was a supplement to the NAMCS, referred to as the NAMCS Electronic Medical Records Supplement. The annual data collected was similar to NEHRS and may be analyzed as a distinct dataset.\nData from the supplement can be used to produce state and national estimates of EHR adoption and capabilities, burden associated with EHRs, and progress physicians have made towards meeting the policy goals of the HITECH Act. \nPlease refer to the following link for the 2008\u20142011 NAMCS Electronic Medical Records Supplemental questionnaire and data dictionary: https://www.cdc.gov/nchs/nehrs/questionnaires.htm.",
+            "title": "National Ambulatory Medical Care Survey: Electronic Medical Records Supplement, 2008-2011, Restricted",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/userestricdt.htm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "spatial": "United States",
+            "describedBy": "The sampling frame was composed of Master files for all American physicians who met the following criteria: Office-based; Principally engaged in patient care activities; Non-federally employed; Not in specialties of anesthesiology, pathology, or radiology; and Younger than 85 years of age at the time of the survey.",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/8ve6-tiah",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-15",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Research Branch (RB), National Personal Protective Technology Laboratory (NPPTL)",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/8ve6-tiah",
+            "description": "In response to the shortage of N95\u00ae filtering facepiece respirators (FFRs) for healthcare workers during the COVID-19 pandemic, the Centers for Disease Control and Prevention (CDC) issued strategies for extended use and limited reuse of N95 FFRs to conserve supply. Previously worn N95 FFRs can serve as a source of pathogens, which can be transferred to the wearer while doffing and donning a respirator when practicing reuse. To reduce the risk of self-contamination when donning and doffing reused FFRs, the CDC suggested storing FFRs for five days between uses to allow for the decay of viable pathogens including SARS-CoV-2. This study assessed the persistence of the SARS-CoV-2 strain USA-WA1/2020 on N95 FFRs under controlled storage conditions for up to five days to inform the CDC guidance.",
+            "title": "Persistence of SARS-CoV-2 on N95 filtering facepiece respirators: implications for reuse",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/8ve6-tiah/application/x-zip-compressed",
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
+            "landingPage": "https://www.cdc.gov/vaccines/imz-managers/nis/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-09-28",
+            "@type": "dcat:Dataset",
+            "modified": "2023-03-28",
+            "keyword": [
+                "adults",
+                "coverage",
+                "flu vaccination",
+                "influenza",
+                "vaccination",
+                "vaccine coverage"
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
+            "identifier": "https://data.cdc.gov/api/views/8dyx-9z99",
+            "description": "Cumulative Influenza Vaccination Coverage Age Group, Race/Ethnicity, and Jurisdiction, Adults 18 Years and Older, United States, National Immunization Survey Adult COVID Module.\n\nThe National Immunization Survey-Adult COVID Module (NIS-ACM) was launched in April 2021 among adults 18 years and older. The survey was used to monitor COVID-19 vaccination uptake and confidence in vaccination among adults and included questions about influenza vaccination.",
+            "title": "Cumulative Influenza Vaccination Coverage by Race/Ethnicity and Age Group, NIS-ACM (Archived)",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8dyx-9z99/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8dyx-9z99/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8dyx-9z99/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8dyx-9z99/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "United States, District of Columbia, US Virgin Islands, and Puerto Rico",
+            "license": "https://www.usa.gov/government-works",
+            "theme": [
+                "Vaccinations"
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
+            "landingPage": "https://healthdata.gov/dataset/national-survey-drug-use-and-health-nsduh-2008-0",
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
+            "identifier": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2008-nid13602",
+            "description": "<p>The National Survey on Drug Use and Health (NSDUH) series (formerly titled National Household Survey on Drug Abuse) primarily measures the prevalence and correlates of drug use in the United States. Detailed NSDUH 2008 documentation <a href=\"http://www.samhsa.gov/data/2k12/NSDUH2008MRB/Index.aspx\">http://www.samhsa.gov/data/2k12/NSDUH2008MRB/Index.aspx</a> is available from SAMHSA. The surveys are designed to provide quarterly, as well as annual, estimates. Information is provided on the use of illicit drugs, alcohol, and tobacco among members of United States households aged 12 and older. Questions included age at first use as well as lifetime, annual, and past-month usage for the following drug classes: marijuana, cocaine (and crack), hallucinogens, heroin, inhalants, alcohol, tobacco, and nonmedical use of prescription drugs, including pain relievers, tranquilizers, stimulants, and sedatives. The survey covered substance abuse treatment history and perceived need for treatment, and included questions from the Diagnostic and Statistical Manual (DSM) of Mental Disorders that allow diagnostic criteria to be applied. The survey included questions concerning treatment for both substance abuse and mental health related disorders. Respondents were also asked about personal and family income sources and amounts, health care access and coverage, illegal activities and arrest record, problems resulting from the use of drugs, and needle-sharing. Questions introduced in previous administrations were retained in the 2008 survey, including questions asked only of respondents aged 12 to 17. These \"youth experiences\" items covered a variety of topics, such as neighborhood environment, illegal activities, drug use by friends, social support, extracurricular activities, exposure to substance abuse prevention and education programs, and perceived adult attitudes toward drug use and activities such as school work. Several measures focused on prevention-related themes in this section. Also retained were questions on mental health and access to care, perceived risk of using drugs, perceived availability of drugs, driving and personal behavior, and cigar smoking. Questions on the tobacco brand used most often were introduced with the 1999 survey. For this 2008 survey, Adult mental health questions were added to measure symptoms of psychological distress in the worst period of distress that a person experienced in the past 30 days and suicidal ideation. A split-sample design also was included to administer separate sets of questions to assess impairment due to mental health problems. Background information includes gender, race, age, ethnicity, marital status, educational level, job status, veteran status, and current household composition.This study has 1 Data Set.</p>",
+            "title": "National Survey on Drug Use and Health (NSDUH-2008)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2008-nid13602",
+                    "description": "National Survey on Drug Use and Health (NSDUH-2008) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/national-survey-drug-use-and-health-nsduh-2008-nid13602"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/y53x-tedw",
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
+            "identifier": "9a44a67b-4623-5bf5-941e-2d28a9874023",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
+            "title": "prodAuto_fileType_measureDisplayGroups",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/fileType_measureDisplayGroups.csv",
+                    "description": "{\"dataset\": \"fileType_measureDisplayGroups\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
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
+            "landingPage": "https://covid.cdc.gov/covid-data-tracker/#vaccine-confidence",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-06-22",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-03",
+            "keyword": [
+                "covid-19 vaccination",
+                "covid tracker",
+                "nis-acm"
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
+            "identifier": "https://data.cdc.gov/api/views/iwxc-qftf",
+            "description": "National Immunization Survey Adult COVID Module (NIS-ACM): CDC is providing information on COVID-19 vaccine confidence to supplement vaccine administration data. These data represent trends in vaccination status and intent by demographics. \n\nFollowing collection of August 2021 survey data, an error in data processing led to incorrect categorization of some survey respondents; some respondents who should have been categorized as MSA: Principal City instead were categorized as MSA: Non-Principal City. Data downloaded during the period September 12, 2021 through September 30, 2021 may have incorrect estimates by MSA status, SVI of county of residence, and political leaning of county of residence.",
+            "title": "National Immunization Survey Adult COVID Module (NIS-ACM): Vaccination Status and Intent by Demographics",
+            "programCode": [
+                "009:026"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/iwxc-qftf/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/iwxc-qftf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/iwxc-qftf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/iwxc-qftf/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/68ej-h5ze",
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
+            "identifier": "https://data.cdc.gov/api/views/68ej-h5ze",
+            "description": "Rate of deaths by age/gender (per 100,000 population) for people killed in crashes involving a driver with BAC =>0.08%, 2012, 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File. Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
+            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, Region 5 - Chicago",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/68ej-h5ze/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/68ej-h5ze/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/68ej-h5ze/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/68ej-h5ze/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/y5r7-kn8s",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2022-02-23",
+            "@type": "dcat:Dataset",
+            "modified": "2022-02-22",
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
+            "identifier": "1e1fd4d7-e872-4613-b40a-268815c7dabe",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2022-02-14 to 2022-02-20",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://edit.data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rpt-drugs-feb-02-14-2022-02-20-2022_1_0.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/gr26-95h2",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-06-21",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-03",
+            "keyword": [
+                "covid-19 vaccination",
+                "covid tracker",
+                "nis-ccm"
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
+            "identifier": "https://data.cdc.gov/api/views/gr26-95h2",
+            "description": "National Immunization Survey Child COVID Module (NIS-CCM): CDC is providing information on COVID-19 vaccine confidence to supplement vaccine administration data. These data represent trends in vaccination status and intent, and other behavioral indicators, by demographics and other characteristics.",
+            "title": "National Immunization Survey Child COVID Module (NIS-CCM): Vaccination Status and Intent by Demographics | Data | Centers for Disease Control and Prevention (cdc.gov)",
+            "programCode": [
+                "009:026"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gr26-95h2/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gr26-95h2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gr26-95h2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/gr26-95h2/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/y759-qbzb",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2024-07-17",
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
+            "identifier": "5937b2be-32a4-5dc9-b9dc-b1f97e38e935",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "devAuto_brief",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/brief.csv",
+                    "description": "{\"dataset\": \"brief\", \"stage\": \"devAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
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
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-08-23",
+            "@type": "dcat:Dataset",
+            "modified": "2024-08-23",
+            "references": [
+                "https://www.cdc.gov/places/measure-definitions/index.html"
+            ],
+            "keyword": [
+                "behaviors",
+                "city",
+                "disability",
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
+            "identifier": "https://data.cdc.gov/api/views/vgc8-iyc4",
+            "description": "This dataset contains model-based place (incorporated and census designated places) estimates in GIS-friendly format. PLACES covers the entire United States\u201450 states and the District of Columbia \u2014at county, place, census tract, and ZIP Code Tabulation Area levels. It provides information uniformly on this large scale for local areas at four geographic levels. Estimates were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. PLACES was funded by the Robert Wood Johnson Foundation in conjunction with the CDC Foundation. Data sources used to generate these model-based estimates are Behavioral Risk Factor Surveillance System (BRFSS) 2022 or 2021 data, Census Bureau 2020 population estimates, and American Community Survey (ACS) 2018\u20132022 estimates. The 2024 release uses 2022 BRFSS data for 36 measures and 2021 BRFSS data for 4 measures (high blood pressure, high cholesterol, cholesterol screening, and taking medicine for high blood pressure control among those with high blood pressure) that the survey collects data on every other year. These data can be joined with the 2020 Census place boundary file in a GIS system to produce maps for 40 measures at the place level. An ArcGIS Online feature service is also available for users to make maps online or to add data to desktop GIS software. https://cdcarcgis.maps.arcgis.com/home/item.html?id=3b7221d4e47740cab9235b839fa55cd7",
+            "title": "PLACES: Place Data (GIS Friendly Format), 2024 release",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vgc8-iyc4/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vgc8-iyc4/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vgc8-iyc4/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vgc8-iyc4/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/3kjq-j5dm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2015-06-17",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-27",
+            "keyword": [
+                "glossary",
+                "methodology",
+                "sae",
+                "sammec"
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
+            "identifier": "https://data.cdc.gov/api/views/3kjq-j5dm",
+            "description": "Download the latest version of the Glossary and Methodology File",
+            "title": "Smoking-Attributable Mortality, Morbidity, and Economic Costs (SAMMEC) - Smoking-Attributable Expenditures (SAE) Glossary and Methodology",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/3kjq-j5dm/application/vnd.ms-excel",
+                    "mediaType": "application/vnd.ms-excel"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Health Consequences and Costs"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cms.gov/provider-characteristics/hospitals-and-other-facilities/home-health-agency-enrollments",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-04-20",
+            "temporal": "2023-04-01/2025-03-31",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-15",
+            "references": [
+                "https://data.cms.gov/sites/default/files/2024-10/HHA_Data_Guidance.pdf"
+            ],
+            "keyword": [
+                "home health",
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/15f64ab4-3172-4a27-b589-ebd67a6d28aa/data-viewer",
+            "description": "The Home Health Agency (HHA) Enrollments dataset provides enrollment information on all HHAs currently enrolled in Medicare. This data includes information on the HHA's legal business name, doing business as name, organization type and address.\u00a0",
+            "title": "Home Health Agency Enrollments",
+            "describedByType": "application/pdf",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/15f64ab4-3172-4a27-b589-ebd67a6d28aa/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Home Health Agency Enrollments : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2025-01/c133f82f-5635-47d3-b85f-364b379a322a/HHA_Enrollments_2025.01.02.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Health Agency Enrollments : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/e9278ca0-fd12-4e20-9a21-9d5cd733cc1d/data",
+                    "mediaType": "text/html",
+                    "title": "Home Health Agency Enrollments : 2025-01-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-10/6f0ae716-79df-45e0-8fcf-5ef1d12727b3/HHA_Enrollments_2024.10.07.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Health Agency Enrollments : 2024-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/115ccf0e-4312-4229-84e9-2b35267b106c/data",
+                    "mediaType": "text/html",
+                    "title": "Home Health Agency Enrollments : 2024-10-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-07/b8e87685-b941-4e88-aa45-b2cfe3db42a4/HHA_Enrollments_2024.07.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Health Agency Enrollments : 2024-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/3a842f3f-2d77-43dc-b92c-078977a8c102/data",
+                    "mediaType": "text/html",
+                    "title": "Home Health Agency Enrollments : 2024-07-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-04/85f0a6c7-c068-40fa-962d-dbf05aa93944/HHA_Enrollments_2024.04.01.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Health Agency Enrollments : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/4410b442-fff1-4b05-bd49-3a90c9cac114/data",
+                    "mediaType": "text/html",
+                    "title": "Home Health Agency Enrollments : 2024-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2024-01/00ea617a-7f11-45ef-a49c-89ed8dff5945/HHA_Enrollments_2024.01.05.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Health Agency Enrollments : 2024-01-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/089ee308-8d5c-4ab5-afbf-a82c14b3f3b6/data",
+                    "mediaType": "text/html",
+                    "title": "Home Health Agency Enrollments : 2024-01-05"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-10/82964b76-66b6-463a-aef1-dff4ae766f9a/HHA_Enrollments_2023.10.02.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Health Agency Enrollments : 2023-10-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/6e53ed2f-c967-4661-b566-a2cbcd7996f1/data",
+                    "mediaType": "text/html",
+                    "title": "Home Health Agency Enrollments : 2023-10-02"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-07/45afd42e-9416-41e3-b2d0-0e70ce793a52/HHA_Enrollments_2023.07.06.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Health Agency Enrollments : 2023-07-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/d998c103-6d16-48a1-b58a-51e5848c6939/data",
+                    "mediaType": "text/html",
+                    "title": "Home Health Agency Enrollments : 2023-07-17"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-04/f719af15-7eab-42c6-a28e-6fd960193edb/HHA_Enrollments_2023.03.31.csv",
+                    "mediaType": "text/csv",
+                    "title": "Home Health Agency Enrollments : 2023-04-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f48bb755-bd9f-42e3-87b9-b88c562cb981/data",
+                    "mediaType": "text/html",
+                    "title": "Home Health Agency Enrollments : 2023-04-01"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/sites/default/files/2024-10/HHA_Enrollments_Data_Dictionary.pdf",
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
+            "bureauCode": [
+                "009:30"
+            ],
+            "landingPage": "https://healthdata.gov/dataset/treatment-episode-data-set-discharges-teds-d-2007",
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
+            "identifier": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2007-nid13535",
+            "description": "<p>The Treatment Episode Data Set -- Discharges (TEDS-D) is a national census data system of annual discharges from substance abuse treatment facilities. TEDS-D provides annual data on the number and characteristics of persons discharged from public and private substance abuse treatment programs that receive public funding. Data collected both at admission and at discharge is included. The unit of analysis is a treatment discharge. TEDS-D consists of data reported to state substance abuse agencies by the treatment programs, which in turn report it to SAMHSA.<br />\nA sister data system, called the Treatment Episode Data Set -- Admissions (TEDS-A), collects data on admissions to substance abuse treatment facilities. The first year of TEDS-A data is 1992, while the first year of TEDS-D is 2006.<br />\nTEDS-D variables that are required to be reported are called the \"Minimum Data Set (MDS)\", while those that are optional are called the \"Supplemental Data Set (SuDS)\".<br />\nVariables unique to TEDS-D, and not part of TEDS-A, are the length of stay, reason for leaving treatment, and service setting at time of discharge. TEDS-D also provides many of the same variables that exist in TEDS-A. This includes information on service setting, number of prior treatments, primary source of referral, gender, race, ethnicity, education, employment status, substance(s) abused, route of administration, frequency of use, age at first use, and whether methadone was prescribed in treatment. Supplemental variables include: diagnosis codes, presence of psychiatric problems, living arrangements, source of income, health insurance, expected source of payment, pregnancy and veteran status, marital status, detailed not in labor force codes, detailed criminal justice referral codes, days waiting to enter treatment, and the number of arrests in the 30 days prior to admissions (starting in 2008) .<br />\nSubstances abused include alcohol, cocaine and crack, marijuana and hashish, heroin, nonprescription methadone, other opiates and synthetics, PCP, other hallucinogens, methamphetamine, other amphetamines, other stimulants, benzodiazepines, other non-benzodiazepine tranquilizers, barbiturates, other non-barbiturate sedatives or hypnotics, inhalants, over-the-counter medications, and other substances.<br />\nCreated variables include total number of substances reported, intravenous drug use (IDU), and flags for any mention of specific substances.This study has 1 Data Set.</p>",
+            "title": "Treatment Episode Data Set: Discharges (TEDS-D-2007)",
+            "programCode": [
+                "009:030"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2007-nid13535",
+                    "description": "Treatment Episode Data Set: Discharges (TEDS-D-2007) \n",
+                    "@type": "dcat:Distribution",
+                    "title": "https://datafiles.samhsa.gov/study/treatment-episode-data-set-discharges-teds-d-2007-nid13535"
+                }
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/egm8-9wq7",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-10-06",
+            "@type": "dcat:Dataset",
+            "temporal": "2020-12-13 to 2021-09-30",
+            "modified": "2022-09-28",
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
+            "identifier": "https://data.cdc.gov/api/views/egm8-9wq7",
+            "description": "The Federal Pharmacy Partnership for Long-Term Care (LTC) Program was a partnership between CDC and CVS, Walgreens, and Managed Health Care Associates, Inc. The program offered on-site COVID-19 vaccination services for residents of nursing homes and assisted living facilities. The Federal Pharmacy Partnership for LTC Program was in effect after vaccines became available to April 23, 2021. This is the historical archived data related to the LTC Program and represents data that was shown on COVID Data Tracker through September 30, 2021. Twelve variables that provided data on residents and staff vaccinated through the program were removed from\u00a0the\u00a0COVID-19 Vaccinations in the United States,Jurisdiction dataset. LTC was removed as an option from the location variable in the following datasets: COVID-19 Vaccinations in the United States,Jurisdiction and COVID-19 Vaccination Trends in the United States,National and Jurisdictional.",
+            "title": "Archive: COVID-19 LTC Program Vaccinations and Trends in the United States, Jurisdiction",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/egm8-9wq7/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/egm8-9wq7/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/egm8-9wq7/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/egm8-9wq7/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/hwyy-s2tt",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-01-21",
+            "@type": "dcat:Dataset",
+            "modified": "2022-01-12",
+            "keyword": [
+                "2021",
+                "carbapenemase-producing carbapenem-resistant enterobacteriaceae",
+                "chancroid",
+                "chlamydia trachomatis infection",
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
+            "identifier": "https://data.cdc.gov/api/views/hwyy-s2tt",
+            "description": "NNDSS - Table 1G. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae to Chlamydia trachomatis infection - 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Reporting jurisdictions were informed CDC could receive data for this condition in August 2019. Please note there will be a delay in reporting of case notifications for this condition to CDC.",
+            "title": "NNDSS - Table 1G. Carbapenemase-producing carbapenem-resistant Enterobacteriaceae to Chlamydia trachomatis infection",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hwyy-s2tt/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hwyy-s2tt/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hwyy-s2tt/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hwyy-s2tt/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/m6gf-vfkz",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-01-03",
+            "@type": "dcat:Dataset",
+            "modified": "2019-01-03",
+            "keyword": [
+                "2018",
+                "all serotypes)",
+                "giardiasis",
+                "gonorrhea",
+                "haemophilus influenza",
+                "invasive disease (all ages",
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
+            "identifier": "https://data.cdc.gov/api/views/m6gf-vfkz",
+            "description": "NNDSS - Table II. Giardiasis to Haemophilus influenza - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html.\r\n \r\nFootnotes:\r\n\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.",
+            "title": "NNDSS - Table II. Giardiasis to Haemophilus influenza",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/m6gf-vfkz/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/m6gf-vfkz/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/m6gf-vfkz/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/m6gf-vfkz/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "http://www.ncbi.nlm.nih.gov/biosample",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2016-08-08",
+            "@type": "dcat:Dataset",
+            "modified": "2024-10-08",
+            "keyword": [
+                "biological assay",
+                "computational biology"
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/w5ku-k2ma",
+            "description": "The BioSample database contains descriptions of biological source materials used in experimental assays.",
+            "title": "BioSample",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.ncbi.nlm.nih.gov/biosample/",
+                    "mediaType": "text/html",
+                    "title": "BioSample Homepage and Search"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/books/NBK25501/",
+                    "mediaType": "text/html",
+                    "title": "BioSample API via Entrez Programming Utilities"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Molecular biology/Genetics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/5egk-p6rd",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-01-03",
+            "@type": "dcat:Dataset",
+            "modified": "2019-01-03",
+            "keyword": [
+                "2018",
+                "chlamydia trachomatis infection",
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
+            "identifier": "https://data.cdc.gov/api/views/5egk-p6rd",
+            "description": "NNDSS - Table II. Chlamydia trachomatis infection to Coccidioidomycosis - 2018. In this Table, provisional cases of selected notifiable diseases (\u22651,000 cases reported during the preceding year), and selected low frequency diseases are displayed. The Table includes total number of cases reported in the United States, by region and by states or territory.\r\n\r\nNote:\r\n\r\nThis table contains provisional cases of selected national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up.  Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html \r\n\r\nFootnotes:\r\n\r\nC.N.M.I.: Commonwealth of Northern Mariana Islands. \r\nU: Unavailable. \u2014: No reported cases. N: Not reportable. NA:  Not Available.  NN: Not Nationally Notifiable. NP: Nationally notifiable but not published. Cum: Cumulative year-to-date counts. Med: Median. Max: Maximum. \r\n\r\n* Case counts for reporting years 2017 and 2018 are provisional and subject to change. Data for years 2013 through 2016 are finalized. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf.",
+            "title": "NNDSS - Table II. Chlamydia trachomatis infection to Coccidioidomycosis",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5egk-p6rd/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5egk-p6rd/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5egk-p6rd/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/5egk-p6rd/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/ycku-mvk7",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2024-11-13",
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
+            "identifier": "fe676dcf-c49f-592c-a11c-2c0f3e9ab684",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "CoreSet filters v2.10.64 (coreset-cmsdev)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/coreset-viz/2.10.64/20250110/filters.csv",
+                    "description": "CoreSet filters v2.10.64 (coreset-cmsdev)",
+                    "@type": "dcat:Distribution",
+                    "title": "CoreSet filters v2.10.64 (coreset-cmsdev)"
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
+            "landingPage": "https://healthdata.gov/d/ycqg-qrdk",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2016-09-26",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-09",
+            "keyword": [
+                "amp",
+                "average manufacturer price"
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
+            "identifier": "80956a7d-e343-54f3-94a7-45d41b34fc0b",
+            "description": "Drugs that have been reported under the Medicaid Drug Rebate Program along with an indication of whether or not the required Average Manufacturer Price (AMP) was reported for each drug. All drugs are identified in the file by the 11-digit National Drug Code, product name, labeler name, and reported (R) or not reported (NR).",
+            "title": "Drug AMP Reporting - Quarterly",
+            "programCode": [
+                "009:076"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/DrugAMPReportingQuarterly3Q2024.csv",
+                    "mediaType": "text/csv"
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
+            "landingPage": "http://www.cdc.gov/nccdphp/dph/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2018-12-04",
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
+            "identifier": "https://data.cdc.gov/api/views/vurf-k5wr",
+            "description": "This is the complete dataset for the 500 Cities project 2017 release. This dataset includes 2015, 2014 model-based small area estimates for 27 measures of chronic disease related to unhealthy behaviors (5), health outcomes (13), and use of preventive services (9). Data were provided by the Centers for Disease Control and Prevention (CDC), Division of Population Health, Epidemiology and Surveillance Branch. The project was funded by the Robert Wood Johnson Foundation (RWJF) in conjunction with the CDC Foundation. It represents a first-of-its kind effort to release information on a large scale for cities and for small areas within those cities. It includes estimates for the 500 largest US cities and approximately 28,000 census tracts within these cities. These estimates can be used to identify emerging health problems and to inform development and implementation of effective, targeted public health prevention activities. Because the small area model cannot detect effects due to local interventions, users are cautioned against using these estimates for program or policy evaluations. Data sources used to generate these measures include Behavioral Risk Factor Surveillance System (BRFSS) data (2015, 2014), Census Bureau 2010 census population data, and American Community Survey (ACS) 2011-2015, 2010-2014 estimates. Because some questions are only asked every other year in the BRFSS, there are 7 measures from the 2014 BRFSS that are the same in the 2017 release as the previous 2016 release. More information about the methodology can be found at www.cdc.gov/500cities.",
+            "title": "500 Cities: Local Data for Better Health, 2017 release",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vurf-k5wr/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vurf-k5wr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vurf-k5wr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vurf-k5wr/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/ydu5-gw79",
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
+            "identifier": "8c491ff0-8e6e-4988-b02a-e4736783aed3",
+            "description": "The Service Area PUF (SA-PUF) is one of the files that comprise the Health Insurance Exchange Public Use Files. The SA-PUF contains issuer-level data on geographic service areas including state, county, and zip code.",
+            "title": "Service Area PUF \u2013 PY2023",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2023/service_area_puf.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/vx8v-gfyf",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2019-04-26",
+            "@type": "dcat:Dataset",
+            "modified": "2019-05-30",
+            "keyword": [
+                "2019",
+                "age <5 years",
+                "all ages",
+                "all serotypes",
+                "gonorrhea",
+                "haemophilus influenzae",
+                "invasive disease",
+                "nedss",
+                "netss",
+                "nndss",
+                "serotype b",
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
+            "identifier": "https://data.cdc.gov/api/views/vx8v-gfyf",
+            "description": "NNDSS - TABLE 1M. Gonorrhea to Haemophilus influenzae, invasive disease (age <5 years), Serotype b - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1M. Gonorrhea to Haemophilus influenzae, invasive disease (age <5 years), Serotype b",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vx8v-gfyf/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vx8v-gfyf/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vx8v-gfyf/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vx8v-gfyf/rows.xml?accessType=DOWNLOAD",
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
+                "osh",
+                "policy",
+                "state system",
+                "tax"
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
+            "identifier": "https://data.cdc.gov/api/views/kwbr-syv2",
+            "description": "1995-2024. Centers for Disease Control and Prevention (CDC). State Tobacco Activities Tracking and Evaluation (STATE) System.  E-Cigarette Legislation\u2014Tax. The STATE System houses current and historical state-level legislative data on tobacco use prevention and control policies. Data are reported on a quarterly basis. Data include state excise taxes on e-cigarettes and tax stamps.",
+            "title": "CDC STATE System E-Cigarette Legislation - Tax",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kwbr-syv2/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kwbr-syv2/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kwbr-syv2/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/kwbr-syv2/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Legislation/CDC-STATE-System-E-Cigarette-Legislation-Tax/kwbr-syv2",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "theme": [
+                "Legislation"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/nvss/index.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-02-03",
+            "temporal": "2020/2023",
+            "@type": "dcat:Dataset",
+            "modified": "2023-09-27",
+            "keyword": [
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
+                "drug overdose",
+                "homicide",
+                "influenza",
+                "kidney disease",
+                "monthly",
+                "mortality",
+                "motor vehicle accidents",
+                "natural cause",
+                "nchs",
+                "nvss",
+                "pneumonia",
+                "provisional",
+                "respiratory disease",
+                "septicemia",
+                "suicide",
+                "unintentional injuries",
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
+            "identifier": "https://data.cdc.gov/api/views/9dzk-mvmi",
+            "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nProvisional counts of deaths by the month the death occurred and by select causes of death for 2020-2023.",
+            "title": "Monthly Provisional Counts of Deaths by Select Causes, 2020-2023",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9dzk-mvmi/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9dzk-mvmi/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9dzk-mvmi/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9dzk-mvmi/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/yf25-8bdz",
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
+            "identifier": "e6bda299-3940-5edc-8ef9-7af3d675d14e",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome.",
+            "title": "prodAuto_states_measures",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20241106_ETL_DEV/states_measures.csv",
+                    "description": "{\"dataset\": \"states_measures\", \"stage\": \"prodAuto\", \"update_id\": \"20241106_ETL_DEV\"}",
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
+            "landingPage": "https://data.cms.gov/cms-innovation-center-programs/pioneer-aco-model/pioneer-aco-model",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-05-26",
+            "temporal": "2012-01-01/2016-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "2023-05-25",
+            "references": [
+                "https://data.cms.gov/resources/pioneer-aco-model-methodology"
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
+            "identifier": "https://data.cms.gov/data-api/v1/dataset/bb2a336c-0710-4de9-80ad-6a2a5cbdbdeb/data-viewer",
+            "description": "The Pioneer Accountable Care Organization (ACO) Model Public Use File (PUF) provides information on ACOs participating in the model. This dataset includes information on each ACO regarding beneficiaries, financial and quality results.",
+            "title": "Pioneer ACO Model",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/bb2a336c-0710-4de9-80ad-6a2a5cbdbdeb/data",
+                    "description": "latest",
+                    "@type": "dcat:Distribution",
+                    "title": "Pioneer ACO Model : 2016-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/9ab35aa5-3473-4864-80a8-02d7848fd222/PIONEER_PY5_PUF1.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pioneer ACO Model : 2016-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/28d8f11a-6585-4f69-898c-15fa6e150e7b/data",
+                    "mediaType": "text/html",
+                    "title": "Pioneer ACO Model : 2016-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/b9487e7e-6586-4260-97b4-9b08ca8de2b0/PIONEER_PY4_PUF1.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pioneer ACO Model : 2015-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/eefd1ce2-c224-4a53-b713-0e126686fc1b/data",
+                    "mediaType": "text/html",
+                    "title": "Pioneer ACO Model : 2015-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/3792bd15-79b3-43a4-8f1f-ff8ddac051fc/PIONEER_PY3PUF1.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pioneer ACO Model : 2014-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/0a6be0a3-53bf-4b53-a144-9ab782ec7571/data",
+                    "mediaType": "text/html",
+                    "title": "Pioneer ACO Model : 2014-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/621859b0-15f8-4d25-accf-e6c28ef81c94/PIONEER_PY2PUF1.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pioneer ACO Model : 2013-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/669080d5-1ec1-455f-99c6-507735a73e28/data",
+                    "mediaType": "text/html",
+                    "title": "Pioneer ACO Model : 2013-12-01"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/sites/default/files/2023-05/c6d635e9-9891-4a72-aa57-2acbcf189b95/PIONEER_PY1PUF1.csv",
+                    "mediaType": "text/csv",
+                    "title": "Pioneer ACO Model : 2012-05-11"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cms.gov/data-api/v1/dataset/f5e39eff-5830-4979-a9f6-7a840ead66ad/data",
+                    "mediaType": "text/html",
+                    "title": "Pioneer ACO Model : 2012-05-11"
+                }
+            ],
+            "describedBy": "https://data.cms.gov/resources/pioneer-aco-model-performance-year-2015-2016-data-dictionary",
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
+            "landingPage": "http://www.fda.gov/AboutFDA/ContactFDA/StayInformed/RSSFeeds/Consumers/rss.xml",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2012-05-30",
+            "keyword": [
+                "approved",
+                "community health",
+                "fda",
+                "health",
+                "items",
+                "notifications",
+                "products",
+                "safety",
+                "updates"
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
+            "identifier": "82319f7a-9d6e-4b9e-b67f-cf8ff1a4980e",
+            "description": "This feed provides new health and safety updates related to FDA approved products",
+            "title": "Health Information Updates",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.fda.gov/AboutFDA/ContactFDA/StayInformed/RSSFeeds/Consumers/rss.xml",
+                    "mediaType": "application/rss+xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/dataset/cooperative-research-and-development-agreement-crada-opportunities-nih",
+            "bureauCode": [
+                "001:05"
+            ],
+            "issued": "2012-05-30",
+            "temporal": "1981-01-01T00:00:00-05:00/1981-01-01T00:00:00-05:00",
+            "@type": "dcat:Dataset",
+            "modified": "2023-07-26",
+            "keyword": [
+                "administrative",
+                "biomedical",
+                "collaboration",
+                "community health",
+                "crada",
+                "innovation",
+                "invention",
+                "licensing",
+                "materials",
+                "medical",
+                "nih",
+                "patents",
+                "reasearch",
+                "technology"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "admin",
+                "hasEmail": "mailto:HealthData@hhs.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "National Institutes of Health (NIH), Department of Health & Human Services"
+            },
+            "identifier": "8bbc3620-957c-44b4-aadc-e9c818de609c",
+            "description": "<p>This RSS Feed represents all Collaborative Research and Development (CRADA) opportunities available from the National Institutes of Health (NIH).The intent of Congress in establishing CRADAs was to promote national technological competitiveness and the rapid transfer of the fruits of innovation to the marketplace. CRADA research and development at the NIH should be directed to the development of biological and behavioral technology, products, and processes by transferring relevant knowledge acquired from NIH research efforts to state and local governments, universities, and the private sector.</p>",
+            "title": "National Institues of Health: Outreach",
+            "programCode": [
+                "009:048"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.ott.nih.gov/rss/CRADARSS.XML",
+                    "mediaType": "text/html",
+                    "title": "Feed "
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
+            "landingPage": "https://healthdata.gov/d/yhga-m8m2",
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
+            "identifier": "2e201fad-8bc8-51b2-b810-e14bb45dd65c",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "implAuto_concernLevel",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/concernLevel.csv",
+                    "description": "{\"dataset\": \"concernLevel\", \"stage\": \"implAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
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
+            "landingPage": "https://healthdata.gov/d/yi85-3s6j",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2023-08-09",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-16",
+            "keyword": [
+                "py2023",
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
+            "identifier": "5eb5f179-5e8c-433e-85a3-2a38d2c75ba2",
+            "description": "The Dental SHOP Market file of the QHP Landscape Files contains information on certified dental plans offered through an Exchange to employers in the Small Business Health Options Program (SHOP) market. These plans are also known as Stand-alone Dental Plans (SADPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
+            "title": "QHP Landscape PY2023 Dental SHOP",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2023/shop_market_dental.zip",
+                    "mediaType": "application/zip"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "restricted public",
+            "landingPage": "https://www.cdc.gov/rdc/index.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "This dataset is restricted to authorized researchers due to indirect identifying sensitive information. Researchers must apply for data access through a proposal process, take confidentiality training and sign a data use agreement. If approved, data access would occur at a NCHS or Federal Statistical Research Data Center. For more information about submitting a proposal for data access, please see: https://www.cdc.gov/rdc/leftbrch/presubmit.htm.",
+            "issued": "2022-12-22",
+            "@type": "dcat:Dataset",
+            "temporal": "1982/2020",
+            "modified": "2023-04-14",
+            "keyword": [
+                "county",
+                "date of delivery",
+                "fetal death",
+                "nchs",
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
+            "identifier": "https://data.cdc.gov/api/views/mny7-y385",
+            "description": "This dataset includes all fetal deaths for a given year and includes all items released in the public-use file. Additional information in this file includes state and county of residence (cities with a population of 250,000 or greater) and exact date of delivery (which includes day of month, month, and year).",
+            "title": "NCHS - All-County Fetal Death File with Exact Date of Delivery",
+            "isPartOf": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/html",
+                    "downloadURL": "https://www.cdc.gov/rdc/leftbrch/presubmit.htm",
+                    "description": "This dataset includes all fetal deaths for a given year and includes all items released in the public-use file. Additional information in this file includes state and county of residence (cities with a population of 250,000 or greater) and exact date of delivery (which includes day of month, month, and year).",
+                    "@type": "dcat:Distribution",
+                    "title": "NCHS - All-County Fetal Death File with Exact Date of Delivery"
+                }
+            ],
+            "spatial": "50 states and District of Columbia, all counties and cities with a population of 100,000 or greater",
+            "describedBy": "All registered fetal deaths occurring to residents of the United States for a given year",
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "NCHS"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/yix6-vnec",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2024-07-25",
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
+            "identifier": "f2872f69-7ad7-5863-a87d-f95199d333be",
+            "description": "This is a dataset created for use by the DQ Atlas website, and is not intended for use outside that application. For more information on the DQ Atlas and the information contained in this dataset see https://www.medicaid.gov/dq-atlas/welcome",
+            "title": "featAuto_briefType",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/dq-atlas/20250114_ETL_DEV/briefType.csv",
+                    "description": "{\"dataset\": \"briefType\", \"stage\": \"featAuto\", \"update_id\": \"20250114_ETL_DEV\"}",
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
+            "landingPage": "https://oculus.nlm.nih.gov/cgi/t/text/text-idx?page=browsecolls",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2022-03-01",
+            "@type": "dcat:Dataset",
+            "modified": "2024-07-19",
+            "keyword": [
+                "dataset",
+                "history of medicine",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/ebin-whwr",
+            "description": "NLM History of Medicine Division's XML-encoded online oral histories provide access to a wealth of digitized transcripts, and audio when available.",
+            "title": "Online Oral Histories",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://oculus.nlm.nih.gov/cgi/t/text/text-idx?page=browsecolls",
+                    "mediaType": "text/html",
+                    "title": "Online Oral Histories"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Historical Curated Content"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "ftp://ftp.ncbi.nlm.nih.gov/blast/db/FASTA",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-06-30",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-04",
+            "keyword": [
+                "computational biology",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/f52g-xt9u",
+            "description": "Sequence databases in FASTA format for use with the stand-alone BLAST programs. These databases must be formatted using formatdb before they can be used with BLAST.",
+            "title": "FASTA BLAST Databases",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://ftp.ncbi.nlm.nih.gov/blast/db/FASTA",
+                    "mediaType": "text/html",
+                    "title": "Download FASTA BLAST Data"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Molecular biology/Genetics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfCLIA/clia.cfm",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2013-11-01",
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
+            "identifier": "c13343cf-eda1-425d-b346-6186c92e3992",
+            "description": "This database contains the commercially marketed in vitro test systems categorized by the FDA since January 31, 2000, and tests categorized by the Centers for Disease Control and Prevention (CDC) prior to that date.",
+            "title": "Clinical Laboratory Improvement Amendments",
+            "programCode": [
+                "009:005"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/cdrh/cfdocs/cfCLIA/clia.cfm",
+                    "mediaType": "text/html"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/vmgc-uspy",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2022-01-14",
+            "@type": "dcat:Dataset",
+            "modified": "2022-02-11",
+            "keyword": [
+                "2022",
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
+            "identifier": "https://data.cdc.gov/api/views/vmgc-uspy",
+            "description": "NNDSS - TABLE 1W. Meningococcal disease, All serogroups to Meningococcal disease, Serogroup B - 2022. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotes:\n\n\u2022\tThese are weekly cases of selected infectious national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables available at https://www.cdc.gov/nndss/data-statistics/index.html. Cases reported by state health departments to CDC for weekly publication are subject to ongoing revision of information and delayed reporting. Therefore, numbers listed in later weeks may reflect changes made to these counts as additional information becomes available. Case counts in the tables are presented as published each week. See also Guide to Interpreting Provisional and Finalized NNDSS Data at https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2022 Notices, errata, and other notes are available in the Notice To Data Users page at https://wonder.cdc.gov/nndss/NTR.html.\n\u2022\tThe list of national notifiable infectious diseases and conditions and their national surveillance case definitions are available at https://ndc.services.cdc.gov/. This list incorporates the Council of State and Territorial Epidemiologists (CSTE) position statements approved by CSTE for national surveillance.\n\nFootnotes:\n\n*Case counts for reporting years 2021 and 2022 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://www.cdc.gov/nndss/docs/Readers-Guide-WONDER-Tables-20210421-508.pdf.\n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.",
+            "title": "NNDSS - TABLE 1W. Meningococcal disease, All serogroups to Meningococcal disease, Serogroup B",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vmgc-uspy/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vmgc-uspy/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vmgc-uspy/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vmgc-uspy/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/ymbn-wcu8",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2017-09-08",
+            "@type": "dcat:Dataset",
+            "modified": "2025-01-15",
+            "keyword": [
+                "applications",
+                "child enrollment",
+                "chip",
+                "eligibility determinations",
+                "enrollment",
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
+            "identifier": "6165f45b-ca93-5bb5-9d06-db29c692a360",
+            "description": "All states (including the District of Columbia) are required to provide data to The Centers for Medicare & Medicaid Services (CMS) on a range of Medicaid and Children\u2019s Health Insurance Program (CHIP) indicators related to key application, eligibility, enrollment and call center processes. These data reflect enrollment activity for all populations receiving comprehensive Medicaid and CHIP benefits in all states, as well as state program performance.<br/>\r\nStates submit this data via the Performance Indicator dataset. Further information about this dataset is available at:  <a href=\"https://www.medicaid.gov/medicaid/national-medicaid-chip-program-information/medicaid-chip-enrollment-data/performance-indicator-technical-assistance/index.html\">https://www.medicaid.gov/medicaid/national-medicaid-chip-program-information/medicaid-chip-enrollment-data/performance-indicator-technical-assistance/index.html</a>.",
+            "title": "State Medicaid and CHIP Applications, Eligibility Determinations, and Enrollment Data",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://download.medicaid.gov/data/pi-dataset-january-2025-release.csv",
+                    "mediaType": "text/csv"
+                }
+            ],
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1M",
+            "theme": [
+                "Enrollment"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/bptw-uw4i",
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
+            "identifier": "https://data.cdc.gov/api/views/bptw-uw4i",
+            "description": "Rate of deaths by age/gender (per 100,000 population) for people killed in crashes involving a driver with BAC =>0.08%, 2012, 2014. 2012 Source: Fatality Analysis Reporting System (FARS). 2014 Source: National Highway Traffic Administration's (NHTSA) Fatality Analysis Reporting System (FARS), 2014 Annual Report File. Note: Blank cells indicate data are suppressed. Fatality rates based on fewer than 20 deaths are suppressed.",
+            "title": "Impaired Driving Death Rate, by Age and Gender, 2012 & 2014, Region 2 - New York",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bptw-uw4i/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bptw-uw4i/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bptw-uw4i/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/bptw-uw4i/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/ypj4-jmx6",
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
+                "qhp landscape instructions",
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
+            "identifier": "5fce65a2-11d2-493d-9c68-f576d09d0ce1",
+            "description": "The Dental Individual Market file of the QHP Landscape Files contains information on certified dental plans offered through an Exchange to consumers in the individual market. These plans are also known as Stand-alone Dental Plans (SADPs). The file reports plans offered by county for states in the Federally-facilitated Exchanges including states performing plan management functions, and State Based Exchanges using the federal platform for eligibility and enrollment.",
+            "title": "QHP Landscape Instructions PY2022 Individual Dental",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.healthcare.gov/datafile/py2022/den-ind-lndscp-in.pdf",
+                    "mediaType": "application/pdf"
+                }
+            ],
+            "accrualPeriodicity": "R/PT1S"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.ncbi.nlm.nih.gov/geo/",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-06-30",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-04",
+            "keyword": [
+                "dataset",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/6m2g-frjb",
+            "description": "GEO (Gene Expression Omnibus) is a public functional genomics data repository supporting MIAME-compliant data submissions. There are also tools provided to help users query and download experiments and curated gene expression profiles.",
+            "title": "GEO (Gene Expression Omnibus)",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/geo/",
+                    "mediaType": "text/html",
+                    "title": "GEO (Gene Expression Omnibus) Homepage"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://www.ncbi.nlm.nih.gov/geo/info/download.html",
+                    "mediaType": "text/html",
+                    "title": "Download GEO (Gene Expression Omnibus) Data"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "Molecular biology/Genetics"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/275g-9x8h",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-02-08",
+            "@type": "dcat:Dataset",
+            "temporal": "2021-10-01/2023-11-10",
+            "modified": "2025-01-14",
+            "keyword": [
+                "coronavirus",
+                "covid-19",
+                "otc",
+                "self-tests"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Jasmine Chaitram",
+                "hasEmail": "mailto:zoa6@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/275g-9x8h",
+            "description": "This dataset includes COVID-19 self-test result data voluntarily reported by users of tests through manufacturer websites and mobile companion applications. At this time, the dataset does not include data reported through the MakeMyTestCount website. All fields are self-reported by the user voluntarily reporting the test result. This dataset will be updated monthly.\n\nPlease note that there are limitations with these data, including:\n1.\tData are not comprehensive of all self-tests performed. Data represent results voluntarily reported by an individual via manufacturer-provided website or companion mobile applications. Not all self-test manufacturers are currently capturing and sending data to CDC. Similarly, these data do not include self-test results that were reported to state and local health departments if they were not also reported through the manufacturer-provided website or companion mobile applications. The true denominator (number of tests completed) cannot be ascertained, but based on manufacturer production numbers, this dataset reflects a small fraction of the number of self-tests used.   \n\n2.\tData are not verified. The quality of specimen, appropriate execution of self-test, result produced, and person tested are unverified; therefore, reported interpretation of results cannot be confirmed. All results and accompanying demographic information are also self-reported and cannot be verified. \n\n3.\tData reports are not complete. Manufacturer-provided websites and companion mobile applications vary widely in terms of the data elements collected. Not all data elements are required, and many results are missing demographic information. \n\n4.\tData are not representative. Based on the limited number of self-reported test results, this dataset is not representative of the use of self-testing by demographic, nor is the dataset inclusive of all self-testing completed within each jurisdiction. This dataset represents a small proportion of overall COVID-19 testing conducted in each jurisdiction and reported volumes are much lower than testing conducted in point of care and laboratory settings.  \n\n5.\tData represent individual test results, not persons tested. Data in this dataset are not linkable and do not allow for analyses around serial testing. Data also cannot be disaggregated to identify multiple reports by the same individual. \n\nAll analyses should be completed with these limitations in mind.\n\nFor more information about the challenges and opportunities around self-test data, please refer to the following article: Ritchey MD, Rosenblum HG, Del Guercio K, et al. COVID-19 Self-Test Data: Challenges and Opportunities \u2014 United States, October 31, 2021\u2013June 11, 2022. MMWR Morb Mortal Wkly Rep 2022;71:1005\u20131010. DOI: http://dx.doi.org/10.15585/mmwr.mm7132a1",
+            "title": "U.S. COVID-19 Self-Test Data",
+            "programCode": [
+                "009:038"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/275g-9x8h/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/275g-9x8h/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/275g-9x8h/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/275g-9x8h/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "spatial": "US",
+            "license": "https://www.usa.gov/government-works",
+            "accrualPeriodicity": "R/P1M",
+            "theme": [
+                "Public Health Surveillance"
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
+            "issued": "2021-05-25",
+            "@type": "dcat:Dataset",
+            "temporal": "2019-12-29/2023-07-29",
+            "modified": "2023-09-27",
+            "keyword": [
+                "all causes",
+                "coronavirus",
+                "covid-19",
+                "deaths",
+                "mortality",
+                "nchs",
+                "nvss",
+                "provisional",
+                "social vulnerability index",
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
+            "identifier": "https://data.cdc.gov/api/views/9hdi-ekmb",
+            "description": "Effective September 27, 2023, this dataset will no longer be updated. Similar data are accessible from wonder.cdc.gov.\n\nDeaths involving COVID-19 reported to NCHS by week and county Social Vulnerability Index (SVI) in the United States. SVI scores are from CDC/ASTDR's Geospatial Research, Analysis & Service Program 2018 database. These scores range from 0 to 1, and categorized as low (0-0.333), moderate (0.334-0.666) or high (0.667-1).\n\nMore information on SVI can be found here: https://www.atsdr.cdc.gov/placeandhealth/svi/index.html",
+            "title": "Provisional COVID-19 Deaths by Week and County Social Vulnerability Index",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9hdi-ekmb/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9hdi-ekmb/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9hdi-ekmb/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/9hdi-ekmb/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/i4eq-dgfc",
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
+            "identifier": "https://data.cdc.gov/api/views/i4eq-dgfc",
+            "description": "NNDSS - TABLE 1LL. Vibriosis, Confirmed to Vibriosis, Probable - 2019. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents. \r\n\r\nNote: \r\nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \r\n\r\nFootnotes:\r\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\r\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\r\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\r\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\r\nNP: Nationally notifiable but not published \u2014 CDC does not have data because of changes in how conditions are categorized.\r\nCum: Cumulative year-to-date counts.\r\nMax: Maximum \u2014 Maximum case count during the previous 52 weeks.\r\n* Case counts for reporting years 2018 and 2019 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the US, a US territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-US Residents' category. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \r\n\u2020 Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data).",
+            "title": "NNDSS - TABLE 1LL. Vibriosis, Confirmed to Vibriosis, Probable",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/i4eq-dgfc/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/i4eq-dgfc/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/i4eq-dgfc/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/i4eq-dgfc/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/healthyyouth/about/index.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2023-07-18",
+            "@type": "dcat:Dataset",
+            "modified": "2023-08-25",
+            "keyword": [
+                "global",
+                "gshs",
+                "risk behavior",
+                "student health",
+                "survey",
+                "youth online"
+            ],
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "DASH Publc Inquiries",
+                "hasEmail": "mailto:nccdDashInfo@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/pxpe-pgrg",
+            "description": "2003-2015. Global School dataset.  The Global School-based Student Health Survey (GSHS) was developed by the World Health Organization (WHO) in collaboration with the United Nations' UNICEF, UNESCO, and UNAIDS; and with technical assistance from CDC.  The GSHS is a school-based survey conducted primarily among students aged 13-17 years in countries around the world.  It uses core questionnaire modules that address the leading causes of morbidity and mortality among children and adults worldwide: 1) Alcohol use, 2) dietary behaviors, 3) drug use, 4) hygiene, 5) mental health, 6) physical activity, 7) protective factors, 8) sexual behaviors that contribute to HIV infection, other sexually-transmitted infections, and unintended pregnancy, 9) tobacco use, and 10) violence and unintentional injury.  This dataset contains global data from 2003 \u2013 2015.  Additional information about the GSHS can be found at https://www.cdc.gov/gshs/index.htm.",
+            "title": "DASH - Global School-based Student Health Survey (GSHS)",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pxpe-pgrg/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pxpe-pgrg/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pxpe-pgrg/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pxpe-pgrg/rows.xml?accessType=DOWNLOAD",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "describedBy": "https://chronicdata.cdc.gov/Youth-Risk-Behaviors/DASH-Global-School-based-Student-Health-Survey-GSH/pxpe-pgrg",
+            "license": "http://opendatacommons.org/licenses/by/1.0/",
+            "theme": [
+                "Youth Risk Behaviors"
+            ]
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://data.cdc.gov/d/ppmd-3u54",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2021-01-21",
+            "@type": "dcat:Dataset",
+            "modified": "2022-01-12",
+            "keyword": [
+                "2021",
+                "crimean-congo hemorrhagic fever virus",
+                "ebola virus",
+                "guanarito virus",
+                "nedss",
+                "netss",
+                "nndss",
+                "viral hemorrhagic fevers",
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
+            "identifier": "https://data.cdc.gov/api/views/ppmd-3u54",
+            "description": "NNDSS - TABLE 1MM. Viral hemorrhagic fevers, Crimean-Congo hemorrhagic fever virus to Guanarito virus \u2013 2021. In this Table, provisional cases* of notifiable diseases are displayed for United States, U.S. territories, and Non-U.S. residents.\n\nNotice: Due to data processing issues at CDC, data for the following jurisdictions may be incomplete for week 7: Alaska, Arizona, California, Connecticut, Delaware, Florida, Hawaii, Louisiana, Maryland, Michigan, Missouri, North Dakota, New Hampshire, New York City, Oregon, Pennsylvania, and Rhode Island.\n\nNote: \nThis table contains provisional cases of national notifiable diseases from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data from the 50 states, New York City, the District of Columbia and the U.S. territories are collated and published weekly on the NNDSS Data and Statistics web page (https://wwwn.cdc.gov/nndss/data-and-statistics.html). Cases reported by state health departments to CDC for weekly publication are provisional because of the time needed to complete case follow-up. Therefore, numbers presented in later weeks may reflect changes made to these counts as additional information becomes available. The national surveillance case definitions used to define a case are available on the NNDSS web site at https://wwwn.cdc.gov/nndss/. Information about the weekly provisional data and guides to interpreting data are available at: https://wwwn.cdc.gov/nndss/infectious-tables.html. \n\nFootnotes:\nU: Unavailable \u2014 The reporting jurisdiction was unable to send the data to CDC or CDC was unable to process the data.\n-: No reported cases \u2014 The reporting jurisdiction did not submit any cases to CDC.\nN: Not reportable \u2014 The disease or condition was not reportable by law, statute, or regulation in the reporting jurisdiction.\nNN: Not nationally notifiable \u2014 This condition was not designated as being nationally notifiable.\nNP: Nationally notifiable but not published.\nNC: Not calculated \u2014 There is insufficient data available to support the calculation of this statistic.\nCum: Cumulative year-to-date counts.\n Max: Maximum \u2014 Maximum case count during the previous 52 weeks.\n  * Case counts for reporting years 2020 and 2021 are provisional and subject to change. Cases are assigned to the reporting jurisdiction submitting the case to NNDSS, if the case's country of usual residence is the U.S., a U.S. territory, unknown, or null (i.e. country not reported); otherwise, the case is assigned to the 'Non-U.S. Residents' category. Country of usual residence is currently not reported by all jurisdictions or for all conditions. For further information on interpretation of these data, see https://wwwn.cdc.gov/nndss/document/Users_guide_WONDER_tables_cleared_final.pdf. \n\u2020Previous 52 week maximum and cumulative YTD are determined from periods of time when the condition was reportable in the jurisdiction (i.e., may be less than 52 weeks of data or incomplete YTD data). \n\u00a7 Prior to 2015, CDC's National Notifiable Diseases Surveillance System (NNDSS) did not receive electronic data about incident cases of specific viral hemorrhagic fevers; instead data were collected in aggregate as \"viral hemorrhagic fevers\". NNDSS was updated beginning in 2015 to receive data for each of the viral hemorrhagic fevers listed.",
+            "title": "NNDSS - TABLE 1MM. Viral hemorrhagic fevers, Crimean-Congo hemorrhagic fever virus to Guanarito virus",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ppmd-3u54/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ppmd-3u54/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ppmd-3u54/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/ppmd-3u54/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://healthdata.gov/d/yt5k-6i8y",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-02-22",
+            "@type": "dcat:Dataset",
+            "modified": "2023-02-21",
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
+            "identifier": "17022a65-b21b-45ae-8224-3cee48c42ef3",
+            "description": "The data below contains newly reported, active covered outpatient drugs which were reported by participating drug manufacturers since the last quarterly update of the Drug Products in the Medicaid Drug Rebate Program (MDRP) database.",
+            "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-02-13-to-2023-02-19",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.medicaid.gov/sites/default/files/uploaded_resources/mdrp-newly-rprt-drug-02132023-to-02192023.csv",
+                    "mediaType": "text/csv",
+                    "title": "Product Data for Newly Reported Drugs in the Medicaid Drug Rebate Program 2023-02-13-to-2023-02-19"
+                }
+            ],
+            "license": "http://www.usa.gov/publicdomain/label/1.0/",
+            "accrualPeriodicity": "R/P10Y"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/nchs/data-visualization/potentially-excess-deaths/",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2017-01-19",
+            "@type": "dcat:Dataset",
+            "modified": "2022-03-30",
+            "keyword": [
+                "cancer",
+                "chronic lower respiratory disease",
+                "heart disease",
+                "stroke",
+                "unintentional injury"
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
+            "identifier": "https://data.cdc.gov/api/views/vdpk-qzpr",
+            "description": "MMWR Surveillance Summary 66 (No. SS-1):1-8 found that nonmetropolitan areas have significant numbers of potentially excess deaths from the five leading causes of death. These figures accompany this report by presenting information on potentially excess deaths in nonmetropolitan and metropolitan areas at the state level. They also add additional years of data and options for selecting different age ranges and benchmarks.\r\n\r\nPotentially excess deaths are defined in MMWR Surveillance Summary 66(No. SS-1):1-8 as deaths that exceed the numbers that would be expected if the death rates of states with the lowest rates (benchmarks) occurred across all states. They are calculated by subtracting expected deaths for specific benchmarks from observed deaths.\r\n\r\nNot all potentially excess deaths can be prevented; some areas might have characteristics that predispose them to higher rates of death. However, many potentially excess deaths might represent deaths that could be prevented through improved public health programs that support healthier behaviors and neighborhoods or better access to health care services.\r\n\r\nMortality data for U.S. residents come from the National Vital Statistics System. Estimates based on fewer than 10 observed deaths are not shown and shaded yellow on the map.\r\n\r\nUnderlying cause of death is based on the International Classification of Diseases, 10th Revision (ICD-10)\r\n\r\nHeart disease (I00-I09, I11, I13, and I20\u2013I51)\r\nCancer (C00\u2013C97)\r\nUnintentional injury (V01\u2013X59 and Y85\u2013Y86)\r\nChronic lower respiratory disease (J40\u2013J47)\r\nStroke (I60\u2013I69)\r\nLocality (nonmetropolitan vs. metropolitan) is based on the Office of Management and Budget\u2019s 2013 county-based classification scheme.\r\n\r\nBenchmarks are based on the three states with the lowest age and cause-specific mortality rates.\r\n\r\nPotentially excess deaths for each state are calculated by subtracting deaths at the benchmark rates (expected deaths) from observed deaths.\r\n\r\nUsers can explore three benchmarks:\r\n\r\n\u201c2010 Fixed\u201d is a fixed benchmark based on the best performing States in 2010.\r\n\u201c2005 Fixed\u201d is a fixed benchmark based on the best performing States in 2005.\r\n\u201cFloating\u201d is based on the best performing States in each year so change from year to year.\r\n \r\nSOURCES\r\n\r\nCDC/NCHS, National Vital Statistics System, mortality data (see http://www.cdc.gov/nchs/deaths.htm); and CDC WONDER (see http://wonder.cdc.gov).\r\n\r\nREFERENCES \r\n\r\n1. Moy E, Garcia MC, Bastian B, Rossen LM, Ingram DD, Faul M, Massetti GM, Thomas CC, Hong Y, Yoon PW, Iademarco MF. Leading Causes of Death in Nonmetropolitan and Metropolitan Areas \u2013 United States, 1999-2014. MMWR Surveillance Summary 2017; 66(No. SS-1):1-8.\r\n\r\n2. Garcia MC, Faul M, Massetti G, Thomas CC, Hong Y, Bauer UE, Iademarco MF. Reducing Potentially Excess Deaths from the Five Leading Causes of Death in the Rural United States. MMWR Surveillance Summary 2017; 66(No. SS-2):1\u20137.",
+            "title": "NCHS - Potentially Excess Deaths from the Five Leading Causes of Death",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vdpk-qzpr/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vdpk-qzpr/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vdpk-qzpr/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/vdpk-qzpr/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/3h4m-i8xf",
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
+            "identifier": "https://data.cdc.gov/api/views/3h4m-i8xf",
+            "description": "Occupational exposure to 4,4\u2019-methylene diphenyl diisocyanate (MDI), the most widely used monomeric diisocyanate (dNCO), is associated with occupational asthma (OA) development. Recruitment of immune cells to the lung microenvironment via secreted chemokines by alveolar macrophages may plays important roles during asthma pathogenesis. Our prior studies identified MDI/MDI-GSH-exposure downregulates endogenous human/murine(hsa/mmu)-microRNA(miR)-206-3p, resulting in the activation of mmu/hsa-miR-206-3p-regulated signaling including KLF4-mediated signaling in M\u00d8s. The hsa-miR-206-3p-regulated signaling activation leading to induction of chemokines and chemotaxis activities of immune cells. However, the underlying molecular mechanism(s) by which MDI/ MDI in the form of MDI-GSH conjugate exposure downregulated endogenous hsa-miR-206-3p expression is unclear. Circular RNAs (circRNAs) play important roles in many different biological processes by targeting endogenous miRs, affecting protein translation and gene transcription in different cell types. The circRNA expression can be regulated via outside stimuli exposures; however, whether MDI-exposure influence circRNAs expression is unknown. Several circRNAs have been identified to regulate hsa-miR-206-3p levels through miR binding/targeting. We hypothesize that MDI-exposure induces endogenous circRNA(s) to regulate hsa-miR-206-3p in M\u00d8s. The first aim of this study was to identified candidate hsa-miR-206-3p-binding circRNA(s) that can be regulated by MDI/MDI-GSH regulated. The second aim of this study was to examine whether MDI/MDI-GSH regulated hsa-miR-206-3p-binding circRNA(s) can indeed regulate the endogenous hsa-miR-206-3p in M\u00d8s. After identified the roles of endogenous circRNA(s) in regulation of endogenous hsa-miR-206-3p after MDI/MDI-GSH-exposure, we investigated the roles of circRNAs in regulation of hsa-miR-206-3p-mediated M2 macrophage-associated markers and chemokines\u2019 expressions in relation to the exposure to MDI.",
+            "title": "Circular RNA hsa_circ_0008726 Targets the hsa-miR-206-3p/KLF4 Axis to Modulate 4,4\u2019-Methylene Diphenyl Diisocyanate-Glutathione Conjugate-Induced Chemokine Transcription in Macrophages",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/3h4m-i8xf/application/x-zip-compressed",
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
+            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225441.htm",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "temporal": "2009-01-01/2009-12-31",
+            "@type": "dcat:Dataset",
+            "modified": "1900-01-01",
+            "keyword": [
+                "community health",
+                "h1n1",
+                "health",
+                "influenza",
+                "market",
+                "notifications",
+                "ora",
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
+            "identifier": "8b366073-48df-4c87-9120-9878f4875373",
+            "description": "This list is intended to alert consumers about Web sites that are or were illegally marketing unapproved, uncleared, or unauthorized products in relation to the 2009 H1N1 Flu Virus (sometimes referred to as the 'swine flu' virus).",
+            "title": "Fraudulent 2009 H1N1 Influenza Products",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/h1n1flu/FraudulentH1N1ProductsList2009.xml",
+                    "mediaType": "application/xml"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "accrualPeriodicity": "irregular"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://www.cdc.gov/covidvaxview/weekly-dashboard/adult-vaccination-coverage.html",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-09-26",
+            "@type": "dcat:Dataset",
+            "temporal": "2023-2024, 2024-25",
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
+            "identifier": "https://data.cdc.gov/api/views/8yup-c35n",
+            "description": "\u2022 Weekly COVID-19 Vaccination Coverage and Comparison among adults 18 Years and Older by Jurisdiction\n\n \u2022 Weekly estimates of COVID-19 vaccination coverage and intent for vaccination among adults are calculated using data from the National Immunization Survey\u2013Adult COVID Module (NIS\u2013ACM) (https://www.cdc.gov/nis/about/index.html).\n\n \u2022 Weekly comparisons to previous season should take into account differences between seasons in vaccine availability dates. 2023\u201324 COVID-19 vaccines were first available mid-September 2023, and 2024\u201325 COVID-19 vaccines were first available at the end of August 2024.\u202f",
+            "title": "Weekly Differences in Cumulative COVID-19 Vaccination Coverage and Comparison Between 2024\u201325 and 2023\u201324 Among Adults 18 Years, Overall, by Selected Demographics",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8yup-c35n/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8yup-c35n/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8yup-c35n/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/8yup-c35n/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "http://www.fda.gov/AboutFDA/Transparency/OpenGovernment/ucm225439.htm",
+            "bureauCode": [
+                "009:10"
+            ],
+            "issued": "2021-02-25",
+            "@type": "dcat:Dataset",
+            "modified": "2010-10-01",
+            "keyword": [
+                "community health",
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
+            "identifier": "1fce6941-625f-4dac-ae3b-6664fcfeea6d",
+            "description": "Contains data for FDA peanut product recalls since January 2009.",
+            "title": "FDA Peanut Product Recalls",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "http://www.accessdata.fda.gov/scripts/peanutbutterrecall/PeanutButterProducts2009.xls",
+                    "mediaType": "application/vnd.ms-excel"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/"
+        },
+        {
+            "accessLevel": "public",
+            "landingPage": "https://healthdata.gov/d/yunm-3wmu",
+            "bureauCode": [
+                "009:38"
+            ],
+            "issued": "2023-06-29",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-11",
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
+            "identifier": "c3d4ec55-f9ea-5b76-9eba-93cc3664c1f1",
+            "description": "This is a dataset created for the Medicaid Scorecard website (https://www.medicaid.gov/state-overviews/scorecard/index.html), and is not intended for use outside that application.",
+            "title": "Scorecard measure_value v2.11.9 (impl)",
+            "programCode": [
+                "009:000"
+            ],
+            "distribution": [
+                {
+                    "mediaType": "text/csv",
+                    "downloadURL": "https://download.medicaid.gov/data/scorecard/2.11.9/20241107/measure_value.csv",
+                    "description": "Scorecard measure_value v2.11.9 (impl)",
+                    "@type": "dcat:Distribution",
+                    "title": "Scorecard measure_value v2.11.9 (impl)"
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
+            "landingPage": "https://data.cdc.gov/d/xm7q-e7uu",
+            "bureauCode": [
+                "009:20"
+            ],
+            "issued": "2024-11-15",
+            "@type": "dcat:Dataset",
+            "modified": "2024-11-20",
+            "contactPoint": {
+                "@type": "vcard:Contact",
+                "fn": "Physical Effects Research Branch (PERB), Health Effects Laboratory Division (HELD)",
+                "hasEmail": "mailto:sa-cin-webteam@cdc.gov"
+            },
+            "publisher": {
+                "@type": "org:Organization",
+                "name": "Centers for Disease Control and Prevention"
+            },
+            "identifier": "https://data.cdc.gov/api/views/xm7q-e7uu",
+            "description": "Working with vibrating hand tools is associated with the development of hand-arm vibration syndrome (HAVS).  HAVS is characterized by cold-induced vasospasms, finger blanching and changes in sensory function.  Vibration plays a major role in the development of the symptoms that are characteristic of HAVS, however, the hands and fingers of worker using tools are also exposed to pressure applied as the workers grip tools.  The pressure applied by gripping a tool might also affect blood flow and sensorineural function.  Therefore, this study examined the effects of applied pressure [2 and 4 newtons (N)] on peripheral vascular and sensorineural function using a characterized rat tail model.  The tails of rats were exposed to 0, 2 or 4N of applied force for 10 days.  Blood flow (laser doppler) and sensitivity of the tail to pressure (Randall-Selitto pressure test) was measured on days 1, 5 and 10 of the exposure.  The sensitivity of the tail nerves to electrical stimulation was measured on days 2 and 9.",
+            "title": "Applied force alters sensorineural and peripheral vascular function in an animal model of hand-arm vibration syndrome",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/xm7q-e7uu/application/x-zip-compressed",
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
+            "landingPage": "https://data.cdc.gov/d/pb4z-432k",
+            "bureauCode": [
+                "009:00"
+            ],
+            "issued": "2016-01-07",
+            "@type": "dcat:Dataset",
+            "modified": "2016-01-07",
+            "keyword": [
+                "2015",
+                "anthrax",
+                "arboviral diseases",
+                "botulism",
+                "brucellosis",
+                "california serogroup virus disease",
+                "chancroid",
+                "chikungunya virus",
+                "cholera",
+                "crimean-congo",
+                "cyclosporiasis",
+                "diphtheria",
+                "eastern equine virus disease",
+                "ebola",
+                "encephalitis",
+                "guanarito",
+                "haemophilus influenzae invasive",
+                "hansen disease",
+                "hantavirus infection",
+                "hantavirus pulmonary syndrome",
+                "hemolytic uremic syndrome",
+                "hepatitis b infection perinatal",
+                "influenza-associated pediatric mortality",
+                "junin",
+                "lassa fever",
+                "leptospirosis",
+                "listeriosis",
+                "lujo virus",
+                "machupo",
+                "marburg fever",
+                "measles",
+                "meningococcal disease invasive",
+                "mmwr",
+                "nedss",
+                "netss",
+                "nndss",
+                "novel influenza a",
+                "plague",
+                "poliomyelitis paralytic",
+                "polio virus infection nonparalytic",
+                "postdiarrheal",
+                "powassan virus disease",
+                "psittacosis",
+                "q fever",
+                "rabies human",
+                "sabia-associated",
+                "sars-cov",
+                "smallpox",
+                "st. louis virus disease",
+                "streptococcal toxic-shock syndrome",
+                "syphilis congenital (age <1 yr)",
+                "toxic-shock syndrome (staphylococcal)",
+                "trichinellosis",
+                "tularemia",
+                "typhoid fever",
+                "vancomycin",
+                "viral hemorrhagic fever",
+                "western equine virus disease",
+                "wonder",
+                "yellow fever"
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
+            "identifier": "https://data.cdc.gov/api/views/pb4z-432k",
+            "description": "NNDSS - Table I. infrequently reported notifiable diseases - 2015.  In this Table, provisional cases of selected infrequently reported notifiable diseases (<1,000 cases reported during the preceding year) are displayed.  Note:These are provisional cases of selected national notifiable diseases, from the National Notifiable Diseases Surveillance System (NNDSS). NNDSS data reported by the 50 states, New York City, the District of Columbia, and the U.S. territories are collated and published weekly as numbered tables printed in the back of the Morbidity and Mortality Weekly Report (MMWR). Cases reported by state health departments to CDC for weekly publication are provisional because of ongoing revision of information and delayed reporting. Case counts in these tables are presented as they were published in the MMWR issues. Therefore, numbers listed in later MMWR weeks may reflect changes made to these counts as additional information becomes available. Footnote:-: No reported cases    N: Not reportable.    NN: Not Nationally Notifiable.    NP: Nationally notifiable but not published.    Cum: Cumulative year-to-date counts. * Three low incidence conditions, rubella, rubella congenital, and tetanus, have been moved to Table 2 to facilitate case count verification with reporting jurisdictions. \ufffd\ufffd\ufffd Case counts for reporting year  2015 are provisional and subject to change. For further information on interpretation of these data, see http://wwwn.cdc.gov/nndss/document/ProvisionalNationaNotifiableDiseasesSurveillanceData20100927.pdf. \ufffd\ufffd Calculated by summing the incidence counts for the current week, the 2 weeks preceding the current week, and the 2 weeks following the current week, for a total of 5 preceding years. The total sum of incident cases is then divided by 25 weeks. Additional information is available at http://wwwn.cdc.gov/nndss/document/5yearweeklyaverage.pdf. \ufffd\ufffd Data for the Arboviral disease, Chikungunya, and Hantavirus infection disease, non-Hantavirus Pulmonary Syndrome (HPS), will be displayed in this table after the CDC obtains Office of Management and Budget Paperwork Reduction Act approval to receive data for these conditions. ** Includes both neuroinvasive and nonneuroinvasive. Updated weekly from reports to the Division of Vector-Borne Infectious Diseases, National Center for Zoonotic, Vector-Borne, and Enteric Diseases (ArboNET Surveillance). Data for West Nile virus are available in Table II. \ufffd\ufffd\u0289\ufffd\ufffd Not reportable in all states. Data from states where the condition is not reportable are excluded from this table except starting in 2007 for the arboviral diseases, STD data, TB data, and influenza-associated pediatric mortality, and in 2003 for SARS-CoV. Reporting exceptions are available at http://wwwn.cdc.gov/nndss/downloads.html.  \ufffd\ufffd\ufffd\ufffd Data for H. influenzae (all ages, all serotypes) are available in Table II. \ufffd\ufffd\ufffd\ufffd Updated weekly from reports to the Influenza Division, National Center for Immunization and Respiratory Diseases. Please refer to the MMWR publication for weekly updates to the footnote for this condition. *** Please refer to the MMWR publication for weekly updates to the footnote for this condition. \ufffd\ufffd\u0289\ufffd\u0289\ufffd\ufffd Data for meningococcal disease (all serogroups) are available in Table II. \ufffd\ufffd\ufffd\ufffd\ufffd\ufffd Please refer to the MMWR publication for weekly updates to the footnote for this condition. \ufffd\ufffd\ufffd\ufffd\ufffd\ufffd Updated weekly from reports to the Division of STD Prevention, National Center for HIV/AIDS, Viral Hepatitis, STD, and TB Prevention. **** Please refer to the MMWR publication for weekly updates to the footnote for this condition. See Table II for Dengue Hemorrhagic Fever.",
+            "title": "NNDSS - Table I. infrequently reported notifiable diseases",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pb4z-432k/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pb4z-432k/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pb4z-432k/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/pb4z-432k/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://www.cdc.gov/nchs/data_access/vitalstatsonline.htm",
+            "bureauCode": [
+                "009:20"
+            ],
+            "rights": "public",
+            "issued": "2015-12-02",
+            "@type": "dcat:Dataset",
+            "temporal": "1990/2010",
+            "modified": "2022-03-29",
+            "keyword": [
+                "hispanic women",
+                "nchs",
+                "pregnancy rate",
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
+            "identifier": "https://data.cdc.gov/api/views/hdy7-e2a3",
+            "description": "https://www.cdc.gov/nchs/data-visualization/natality-trends/index.htm",
+            "title": "NCHS - Pregnancy Rates, by Age for Hispanic Women: United States, 1990-2010",
+            "isPartOf": "NCHS - Pregnancy Rates, by Age for Hispanic Women: United States, 1990-2010",
+            "programCode": [
+                "009:020"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hdy7-e2a3/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hdy7-e2a3/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hdy7-e2a3/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/api/views/hdy7-e2a3/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://datadiscovery.nlm.nih.gov/d/9jbh-ypax",
+            "bureauCode": [
+                "009:25"
+            ],
+            "issued": "2021-09-15",
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
+            "identifier": "https://datadiscovery.nlm.nih.gov/api/views/9jbh-ypax",
+            "description": "Health Services Research Information Central (HSRIC) is a web portal and current awareness service of information on health services research. Alerts the communities to meetings, webinars, new web-born reports (analyses, statistics), datasets, and general news. Currently contains over 3,000 items.\n\nThis resource was retired on September 14, 2021 and is no longer updated.",
+            "title": "Health Services Research Information Central (HSRIC)",
+            "programCode": [
+                "009:041"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/9jbh-ypax/rows.csv?accessType=DOWNLOAD",
+                    "mediaType": "text/csv"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/9jbh-ypax/rows.rdf?accessType=DOWNLOAD",
+                    "mediaType": "application/rdf+xml"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/9jbh-ypax/rows.json?accessType=DOWNLOAD",
+                    "mediaType": "application/json"
+                },
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://datadiscovery.nlm.nih.gov/api/views/9jbh-ypax/rows.xml?accessType=DOWNLOAD",
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
+            "landingPage": "https://data.cdc.gov/d/aian-amjw",
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
+            "identifier": "https://data.cdc.gov/api/views/aian-amjw",
+            "description": "Workers involved in oil exploration and production in the upstream petroleum industry are exposed to crude oil vapor (COV).  COV levels in the proximity of workers during production tank gauging and opening of thief hatches can exceed regulatory standards, and several deaths have occurred after opening thief hatches.  There is a paucity of information regarding the effects of COV inhalation in the lung.  To address these knowledge gaps, the present hazard identification study was one of six undertaken to investigate the effects of inhaled COV in a rat animal model.",
+            "title": "Biological effects of inhaled crude oil vapor. III. Pulmonary effects",
+            "programCode": [
+                "009:034"
+            ],
+            "distribution": [
+                {
+                    "@type": "dcat:Distribution",
+                    "downloadURL": "https://data.cdc.gov/download/aian-amjw/application/x-zip-compressed",
+                    "mediaType": "application/x-zip-compressed"
+                }
+            ],
+            "license": "http://opendefinition.org/licenses/odc-odbl/",
+            "theme": [
+                "National Institute for Occupational Safety and Health"
+            ]
+        }
+    ]
 }
```

### Changes from 4ce8de3 to 761a84b (Part 1/4)
**Author:** Automated

**Date:** 2025-01-31 08:11:08+00:00

**Message:** Updated data: Fri Jan 31 08:11:08 UTC 2025

```diff
diff --git a/healthdata.json b/healthdata.json
index b0171a3..e2ed06c 100644
--- a/healthdata.json
+++ b/healthdata.json
@@ -5,5 +5,5 @@
   "conformsTo": "https://project-open-data.cio.gov/v1.1/schema",
   "describedBy": "https://project-open-data.cio.gov/v1.1/schema/catalog.json",
   "dataset": [
```

